import streamlit as st

st.set_page_config(
    page_title="Model | Real Estate Price Predictor",
    page_icon="📊",
    layout="wide",
)

try:
    theme_type = st.context.theme.type
except Exception:
    theme_type = "dark"

theme_mode = "light" if theme_type == "light" else "dark"

if theme_mode == "light":
    palette = {
        "bg-1": "#EEEAF7",
        "bg-2": "#E8E3F3",
        "bg-3": "#EEEAF7",
        "panel-bg": "#F8F6FC",
        "panel-bg-alt": "#F5F1FA",
        "primary": "#7657D9",
        "accent": "#4BBDB3",
        "accent-light": "#967DE0",
        "text": "#282238",
        "text-soft": "#282238",
        "text-muted": "#665E76",
        "border": "#D1C8E3",
        "shadow": "rgba(90, 70, 130, 0.10)",
        "soft-purple": "rgba(118, 87, 217, 0.12)",
        "sidebar-bg": "#E4DDF0",
        "sidebar-item-active": "#DCD2F1",
        "sidebar-item-active-text": "#282238",
        "sidebar-item-hover": "rgba(118, 87, 217, 0.10)",
        "sidebar-text": "#282238",
        "sidebar-text-secondary": "#665E76",
    }
else:
    palette = {
        "bg-1": "#0B0818",
        "bg-2": "#100B24",
        "bg-3": "#17122D",
        "panel-bg": "#17122D",
        "panel-bg-alt": "#14102A",
        "primary": "#7657D9",
        "accent": "#4BBDB3",
        "accent-light": "#73ebde",
        "text": "#EDE9FE",
        "text-soft": "#EDE9FE",
        "text-muted": "#B8AED8",
        "border": "rgba(129, 111, 184, 0.25)",
        "shadow": "rgba(10, 7, 18, 0.24)",
        "soft-purple": "rgba(118, 87, 217, 0.18)",
        "sidebar-bg": "#100B24",
        "sidebar-item-active": "#241A45",
        "sidebar-item-active-text": "#FFFFFF",
        "sidebar-item-hover": "rgba(118, 87, 217, 0.18)",
        "sidebar-text": "#EDE9FE",
        "sidebar-text-secondary": "#B8AED8",
    }


style_css = """
<style>

:root {
    --bg-1: __BG_1__;
    --bg-2: __BG_2__;
    --bg-3: __BG_3__;
    --panel-bg: __PANEL_BG__;
    --panel-bg-alt: __PANEL_BG_ALT__;
    --primary: __PRIMARY__;
    --accent: __ACCENT__;
    --accent-light: __ACCENT_LIGHT__;
    --text: __TEXT__;
    --text-soft: __TEXT_SOFT__;
    --text-muted: __TEXT_MUTED__;
    --border: __BORDER__;
    --shadow: __SHADOW__;
    --soft-purple: __SOFT_PURPLE__;
    --sidebar-bg: __SIDEBAR_BG__;
    --sidebar-item-active: __SIDEBAR_ITEM_ACTIVE__;
    --sidebar-item-active-text: __SIDEBAR_ITEM_ACTIVE_TEXT__;
    --sidebar-item-hover: __SIDEBAR_ITEM_HOVER__;
    --sidebar-text: __SIDEBAR_TEXT__;
    --sidebar-text-secondary: __SIDEBAR_TEXT_SECONDARY__;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(124, 92, 252, 0.12),
            transparent 26%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(103, 220, 207, 0.12),
            transparent 20%
        ),
        linear-gradient(
            135deg,
            var(--bg-1) 0%,
            var(--bg-2) 45%,
            var(--bg-3) 100%
        );
    color: var(--text);
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: var(--bg-1);
}

header[data-testid="stHeader"] {
    background: var(--bg-1) !important;
    border-bottom: 1px solid rgba(209, 200, 227, 0.55);
    box-shadow: none !important;
}

.block-container {
    max-width: 1000px;
    padding-top: 2.5rem;
    padding-bottom: 2rem;
}

.title {
    font-size: clamp(2.3rem, 4vw, 3.1rem);
    font-weight: 800;
    letter-spacing: -0.05em;
    background: linear-gradient(90deg, var(--primary) 0%, #A78BFA 42%, var(--accent) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 1rem;
}

.card {
    background: var(--panel-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.4rem 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 18px 30px var(--shadow);
}

.heading {
    color: var(--text);
    font-size: 1.2rem;
    font-weight: 800;
    margin-bottom: 0.7rem;
}

.body {
    color: var(--text-muted);
    line-height: 1.8;
    font-size: 1rem;
}

.metric {
    background: var(--panel-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 12px 24px rgba(124, 92, 252, 0.06);
}

.metric-label {
    color: var(--text-muted);
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}

.metric-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text);
}

.pipeline-flow {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.pipeline-step {
    background: var(--panel-bg-alt);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.8rem 1.2rem;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text);
    text-align: center;
    white-space: nowrap;
}

.pipeline-arrow {
    color: var(--accent);
    font-size: 1.2rem;
    font-weight: 800;
    flex-shrink: 0;
}

[data-testid="stSidebar"] {
    background: var(--sidebar-bg) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--sidebar-text) !important;
}

[data-testid="stSidebar"] a {
    border-radius: 10px;
    color: var(--sidebar-text) !important;
}

[data-testid="stSidebar"] a:hover {
    background: var(--sidebar-item-hover) !important;
    color: var(--sidebar-text) !important;
}

[data-testid="stSidebar"] a[aria-current="page"] {
    background: var(--sidebar-item-active) !important;
    color: var(--sidebar-item-active-text) !important;
    border: 1px solid rgba(118, 87, 217, 0.18) !important;
}

[data-testid="stSidebar"] .stSidebarNav a span,
[data-testid="stSidebar"] .stSidebarNav a div {
    color: var(--sidebar-text) !important;
}

[data-testid="stSidebar"] .stSidebarNav a[aria-current="page"] span,
[data-testid="stSidebar"] .stSidebarNav a[aria-current="page"] div {
    color: var(--sidebar-item-active-text) !important;
}

</style>
"""


style_css = (
    style_css
    .replace("__BG_1__", palette["bg-1"])
    .replace("__BG_2__", palette["bg-2"])
    .replace("__BG_3__", palette["bg-3"])
    .replace("__PANEL_BG__", palette["panel-bg"])
    .replace("__PANEL_BG_ALT__", palette["panel-bg-alt"])
    .replace("__PRIMARY__", palette["primary"])
    .replace("__ACCENT__", palette["accent"])
    .replace("__ACCENT_LIGHT__", palette["accent-light"])
    .replace("__TEXT__", palette["text"])
    .replace("__TEXT_SOFT__", palette["text-soft"])
    .replace("__TEXT_MUTED__", palette["text-muted"])
    .replace("__BORDER__", palette["border"])
    .replace("__SHADOW__", palette["shadow"])
    .replace("__SOFT_PURPLE__", palette["soft-purple"])
    .replace("__SIDEBAR_BG__", palette["sidebar-bg"])
    .replace("__SIDEBAR_ITEM_ACTIVE__", palette["sidebar-item-active"])
    .replace(
        "__SIDEBAR_ITEM_ACTIVE_TEXT__",
        palette["sidebar-item-active-text"]
    )
    .replace(
        "__SIDEBAR_ITEM_HOVER__",
        palette["sidebar-item-hover"]
    )
    .replace(
        "__SIDEBAR_TEXT__",
        palette["sidebar-text"]
    )
    .replace(
        "__SIDEBAR_TEXT_SECONDARY__",
        palette["sidebar-text-secondary"]
    )
)

st.markdown(style_css, unsafe_allow_html=True)


st.markdown(
    '<div class="title">Model Overview</div>',
    unsafe_allow_html=True
)


# -------------------------
# METRIC CARDS
# -------------------------

metric_cols = st.columns(4)

with metric_cols[0]:
    st.markdown(
        '''
        <div class="metric">
            <div class="metric-label">Algorithm</div>
            <div class="metric-value">Random Forest</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with metric_cols[1]:
    st.markdown(
        '''
        <div class="metric">
            <div class="metric-label">Preprocessing</div>
            <div class="metric-value">Median + Scaling</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with metric_cols[2]:
    st.markdown(
        '''
        <div class="metric">
            <div class="metric-label">Input Features</div>
            <div class="metric-value">13</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with metric_cols[3]:
    st.markdown(
        '''
        <div class="metric">
            <div class="metric-label">Dataset</div>
            <div class="metric-value">506</div>
        </div>
        ''',
        unsafe_allow_html=True
    )


# -------------------------
# PIPELINE CARD
# -------------------------

st.markdown(
    """
    <div class="card">
        <div class="heading">Pipeline</div>
        <div class="body">
            The project follows the same prediction flow used in the working model: raw property data is processed, missing values are handled, numeric features are standardized, and then a Random Forest Regression model estimates the final house price.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# -------------------------
# PIPELINE FLOW
# -------------------------

st.markdown(
    """
    <div class="card">
        <div class="heading">Prediction Pipeline</div>
        <div class="pipeline-flow">
            <div class="pipeline-step">Raw Property Data</div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">Missing Value Handling</div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">Standard Scaling</div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">Random Forest Regression</div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">Predicted House Price</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)