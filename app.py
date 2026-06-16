"""Streamlit recruiter demo for an interpretable Decision Tree classifier.

This app intentionally trains a clean scikit-learn Pipeline from the original
Adult Income dataset. It avoids the target-leakage issue found in the legacy
notebook by never using the target label or target-derived cluster as a feature.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree


DATA_PATH = os.path.join("data", "adult_dataset.csv")
TARGET_ORIGINAL = "Unnamed: 14"
TARGET_COLUMN = "income_class"
RANDOM_STATE = 99

SENSITIVE_FEATURES = ["race", "sex"]
NUMERIC_FEATURES_BASE = [
    "age",
    "fnlwgt",
    "education.num",
    "capital.gain",
    "capital.loss",
    "hours.per.week",
]
CATEGORICAL_FEATURES_BASE = [
    "workclass",
    "education",
    "marital.status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native.country",
]


@dataclass
class ModelBundle:
    pipeline: Pipeline
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series
    y_pred: np.ndarray
    feature_names: np.ndarray
    numeric_features: List[str]
    categorical_features: List[str]
    dataset: pd.DataFrame


def make_one_hot_encoder() -> OneHotEncoder:
    """Create an OneHotEncoder compatible with recent and older sklearn versions."""
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:  # sklearn < 1.2
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


@st.cache_data(show_spinner=False)
def load_dataset(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.replace("?", np.nan)
    df = df.rename(columns={TARGET_ORIGINAL: TARGET_COLUMN})
    df[TARGET_COLUMN] = df[TARGET_COLUMN].astype(str).str.strip()
    return df


@st.cache_resource(show_spinner=False)
def train_model(exclude_sensitive_features: bool = True, max_depth: int = 5) -> ModelBundle:
    df = load_dataset()

    numeric_features = NUMERIC_FEATURES_BASE.copy()
    categorical_features = CATEGORICAL_FEATURES_BASE.copy()

    if exclude_sensitive_features:
        categorical_features = [f for f in categorical_features if f not in SENSITIVE_FEATURES]

    features = numeric_features + categorical_features
    X = df[features].copy()
    y = df[TARGET_COLUMN].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    numeric_pipeline = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median"))]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", make_one_hot_encoder()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ],
        remainder="drop",
    )

    classifier = DecisionTreeClassifier(
        criterion="gini",
        max_depth=max_depth,
        min_samples_leaf=50,
        min_samples_split=50,
        random_state=100,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", classifier),
        ]
    )
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    feature_names = pipeline.named_steps["preprocessor"].get_feature_names_out()

    return ModelBundle(
        pipeline=pipeline,
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        y_pred=y_pred,
        feature_names=feature_names,
        numeric_features=numeric_features,
        categorical_features=categorical_features,
        dataset=df,
    )


def clean_feature_name(name: str) -> str:
    name = name.replace("num__", "").replace("cat__", "")
    for raw_col in CATEGORICAL_FEATURES_BASE:
        prefix = f"{raw_col}_"
        if name.startswith(prefix):
            return f"{raw_col} = {name[len(prefix):]}"
    return name


def make_input_form(bundle: ModelBundle) -> pd.DataFrame:
    df = bundle.dataset
    user_input: Dict[str, object] = {}

    st.sidebar.header("Input profile")
    st.sidebar.caption("Isi profil sederhana, lalu lihat prediksi dan rule path model.")

    with st.sidebar.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            user_input["age"] = st.slider("Age", 17, 90, 35)
            user_input["education.num"] = st.slider("Education number", 1, 16, 10)
            user_input["hours.per.week"] = st.slider("Hours per week", 1, 99, 40)
        with col2:
            user_input["capital.gain"] = st.number_input("Capital gain", min_value=0, value=0, step=100)
            user_input["capital.loss"] = st.number_input("Capital loss", min_value=0, value=0, step=100)
            user_input["fnlwgt"] = st.number_input("fnlwgt", min_value=1, value=int(df["fnlwgt"].median()), step=1000)

        for feature in bundle.categorical_features:
            values = sorted(df[feature].dropna().astype(str).unique().tolist())
            default_index = values.index("Private") if feature == "workclass" and "Private" in values else 0
            if feature == "native.country" and "United-States" in values:
                default_index = values.index("United-States")
            user_input[feature] = st.selectbox(feature, values, index=default_index)

        submitted = st.form_submit_button("Predict income class")

    # Streamlit re-runs after every interaction; prediction is shown with current values.
    input_df = pd.DataFrame([user_input], columns=bundle.numeric_features + bundle.categorical_features)
    if submitted:
        st.session_state["submitted_once"] = True
    return input_df


def get_rule_path(bundle: ModelBundle, input_df: pd.DataFrame) -> List[Dict[str, object]]:
    pipeline = bundle.pipeline
    transformed = pipeline.named_steps["preprocessor"].transform(input_df)
    tree = pipeline.named_steps["model"].tree_
    node_indicator = pipeline.named_steps["model"].decision_path(transformed)
    leaf_id = pipeline.named_steps["model"].apply(transformed)

    rules: List[Dict[str, object]] = []
    node_index = node_indicator.indices[
        node_indicator.indptr[0] : node_indicator.indptr[1]
    ]

    for node_id in node_index:
        if leaf_id[0] == node_id:
            continue
        feature_index = tree.feature[node_id]
        threshold = tree.threshold[node_id]
        if feature_index < 0:
            continue

        feature_name = clean_feature_name(str(bundle.feature_names[feature_index]))
        feature_value = float(transformed[0, feature_index])
        comparator = "<=" if feature_value <= threshold else ">"
        rules.append(
            {
                "Feature": feature_name,
                "Value used by model": round(feature_value, 3),
                "Rule": f"{feature_name} {comparator} {threshold:.3f}",
            }
        )
    return rules


def plot_confusion_matrix(bundle: ModelBundle) -> plt.Figure:
    labels = list(bundle.pipeline.named_steps["model"].classes_)
    cm = confusion_matrix(bundle.y_test, bundle.y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(5, 4))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(ax=ax, values_format="d", colorbar=False)
    ax.set_title("Confusion Matrix - Clean Decision Tree")
    return fig


def plot_decision_tree(bundle: ModelBundle) -> plt.Figure:
    model = bundle.pipeline.named_steps["model"]
    readable_features = [clean_feature_name(str(name)) for name in bundle.feature_names]
    fig, ax = plt.subplots(figsize=(18, 8))
    plot_tree(
        model,
        feature_names=readable_features,
        class_names=[str(c) for c in model.classes_],
        filled=True,
        rounded=True,
        max_depth=3,
        fontsize=8,
        ax=ax,
    )
    ax.set_title("Decision Tree Preview (first 3 levels)")
    return fig


def main() -> None:
    st.set_page_config(
        page_title="Decision Tree Interpretability Demo",
        page_icon="🌳",
        layout="wide",
    )

    st.title("🌳 Decision Tree Interpretability Demo")
    st.caption(
        "Recruiter-facing demo based on the Adult Income Decision Tree project. "
        "The app focuses on simple prediction, rule-path explanation, and transparent evaluation."
    )

    with st.expander("Important audit note", expanded=True):
        st.markdown(
            """
            The legacy notebook produced a perfect score because it included a `cluster` feature derived from the target label.
            This demo avoids that target leakage by training a fresh scikit-learn Pipeline directly from the original dataset features.

            This is an educational portfolio demo, not a production decision system.
            """
        )

    exclude_sensitive = st.toggle(
        "Exclude sensitive attributes from model input (`race`, `sex`)",
        value=True,
        help="Recommended for a safer recruiter demo. Turn off only to inspect the original dataset feature set.",
    )
    max_depth = st.slider(
        "Decision tree max depth",
        min_value=2,
        max_value=10,
        value=5,
        help="Lower depth is easier to explain; higher depth may fit more complex patterns.",
    )

    bundle = train_model(exclude_sensitive_features=exclude_sensitive, max_depth=max_depth)
    input_df = make_input_form(bundle)

    prediction = bundle.pipeline.predict(input_df)[0]
    probabilities = bundle.pipeline.predict_proba(input_df)[0]
    classes = bundle.pipeline.named_steps["model"].classes_
    probability_df = pd.DataFrame(
        {"Class": classes, "Probability": probabilities}
    ).sort_values("Probability", ascending=False)

    test_accuracy = accuracy_score(bundle.y_test, bundle.y_pred)

    metric_col1, metric_col2, metric_col3 = st.columns(3)
    metric_col1.metric("Predicted class", str(prediction))
    metric_col2.metric("Test accuracy", f"{test_accuracy:.3f}")
    metric_col3.metric("Test rows", f"{len(bundle.y_test):,}")

    st.subheader("Prediction confidence")
    st.dataframe(probability_df, use_container_width=True, hide_index=True)

    st.subheader("Explanation: decision path")
    rules = get_rule_path(bundle, input_df)
    if rules:
        st.write("Model mencapai prediksi di atas melalui rule berikut:")
        st.dataframe(pd.DataFrame(rules), use_container_width=True, hide_index=True)
    else:
        st.info("Rule path tidak tersedia untuk input ini.")

    st.subheader("Model evaluation")
    tab_cm, tab_report, tab_tree, tab_data = st.tabs(
        ["Confusion matrix", "Classification report", "Tree preview", "Dataset notes"]
    )

    with tab_cm:
        st.pyplot(plot_confusion_matrix(bundle), clear_figure=True)

    with tab_report:
        report = classification_report(bundle.y_test, bundle.y_pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose().reset_index().rename(columns={"index": "label"})
        st.dataframe(report_df, use_container_width=True, hide_index=True)

    with tab_tree:
        st.pyplot(plot_decision_tree(bundle), clear_figure=True)
        st.caption("Preview dibatasi sampai 3 level pertama agar tetap mudah dibaca.")

    with tab_data:
        st.markdown(
            f"""
            - Dataset rows: **{len(bundle.dataset):,}**
            - Target column: **{TARGET_COLUMN}**
            - Numeric features: `{', '.join(bundle.numeric_features)}`
            - Categorical features: `{', '.join(bundle.categorical_features)}`
            - Sensitive attributes excluded: **{exclude_sensitive}**
            - Split strategy: **70% train / 30% test, stratified by target**
            - Preprocessing: **median imputation for numeric features, most-frequent imputation + one-hot encoding for categorical features**
            """
        )
        st.write("Target distribution:")
        st.dataframe(
            bundle.dataset[TARGET_COLUMN].value_counts().rename_axis("class").reset_index(name="count"),
            use_container_width=True,
            hide_index=True,
        )


if __name__ == "__main__":
    main()
