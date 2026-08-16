import streamlit as st
import pandas as pd
from joblib import load

st.set_page_config(
    page_title="Predict | Real Estate Price Predictor",
    page_icon="🏠",
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
        "primary-strong": "#967DE0",
        "accent": "#4BBDB3",
        "text": "#282238",
        "text-soft": "#282238",
        "text-muted": "#665E76",
        "border": "#D1C8E3",
        "shadow": "rgba(90, 70, 130, 0.10)",
        "soft-purple": "rgba(118, 87, 217, 0.12)",
        "soft-cyan": "rgba(75, 189, 179, 0.14)",
        "input-bg": "#F1EDF7",
        "button-text": "#FFFFFF",
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
        "primary-strong": "#8F76E6",
        "accent": "#4BBDB3",
        "text": "#EDE9FE",
        "text-soft": "#EDE9FE",
        "text-muted": "#B8AED8",
        "border": "rgba(129, 111, 184, 0.25)",
        "shadow": "rgba(10, 7, 18, 0.24)",
        "soft-purple": "rgba(118, 87, 217, 0.18)",
        "soft-cyan": "rgba(75, 189, 179, 0.18)",
        "input-bg": "rgba(18, 14, 29, 0.96)",
        "button-text": "#FFFFFF",
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
    --primary-strong: __PRIMARY_STRONG__;
    --accent: __ACCENT__;
    --text: __TEXT__;
    --text-soft: __TEXT_SOFT__;
    --text-muted: __TEXT_MUTED__;
    --border: __BORDER__;
    --shadow: __SHADOW__;
    --soft-purple: __SOFT_PURPLE__;
    --soft-cyan: __SOFT_CYAN__;
    --input-bg: __INPUT_BG__;
    --button-text: __BUTTON_TEXT__;
    --sidebar-bg: __SIDEBAR_BG__;
    --sidebar-item-active: __SIDEBAR_ITEM_ACTIVE__;
    --sidebar-item-active-text: __SIDEBAR_ITEM_ACTIVE_TEXT__;
    --sidebar-item-hover: __SIDEBAR_ITEM_HOVER__;
    --sidebar-text: __SIDEBAR_TEXT__;
    --sidebar-text-secondary: __SIDEBAR_TEXT_SECONDARY__;
}

.stApp {
    background: radial-gradient(circle at 12% 8%, rgba(124, 92, 252, 0.14), transparent 26%),
        radial-gradient(circle at 85% 18%, rgba(103, 220, 207, 0.12), transparent 20%),
        linear-gradient(135deg, var(--bg-1) 0%, var(--bg-2) 50%, var(--bg-3) 100%);
    color: var(--text);
}

[data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: var(--bg-1);
}

header[data-testid="stHeader"] {
    background: var(--bg-1) !important;
    border-bottom: 1px solid rgba(209, 200, 227, 0.55);
    box-shadow: none !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

.hero {
    padding: 1.5rem 1rem 2.2rem;
    text-align: center;
}

.hero-badge {
    display: inline-block;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 700;
    color: var(--primary);
    background: rgba(167, 139, 250, 0.12);
    border: 1px solid rgba(124, 92, 252, 0.18);
    margin-bottom: 1rem;
}

.hero-icon {
    font-size: 3rem;
    margin-bottom: 0.4rem;
    filter: drop-shadow(0 0 18px rgba(124, 92, 252, 0.12));
}

.hero-title {
    font-size: clamp(2.4rem, 4vw, 4rem);
    line-height: 1.08;
    font-weight: 800;
    letter-spacing: -0.05em;
    margin: 0;
    background: linear-gradient(90deg, #7C5CFC 0%, #A78BFA 42%, #67DCCF 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero-subtitle {
    color: var(--text-muted);
    font-size: 1.08rem;
    margin-top: 0.85rem;
}

.section-wrap {
    margin-top: 1.2rem;
    margin-bottom: 1.3rem;
    background: var(--panel-bg);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.2rem 1.2rem 0.8rem;
    box-shadow: 0 12px 26px var(--shadow);
}

.section-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}

.section-header h3 {
    margin: 0;
    color: var(--text);
    font-size: 1.2rem;
    font-weight: 700;
}

.section-header .dot {
    width: 0.7rem;
    height: 0.7rem;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    box-shadow: 0 0 16px rgba(124, 92, 252, 0.18);
}

label {
    color: var(--text-soft) !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] {
    background: var(--input-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(124, 92, 252, 0.12) !important;
}

div[data-baseweb="input"] input {
    color: var(--text) !important;
    background: transparent !important;
}

div[data-baseweb="select"] > div {
    background: var(--input-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    box-shadow: none !important;
}

.stNumberInput, .stSelectbox {
    margin-bottom: 0.6rem;
}

.stButton > button {
    width: 100%;
    height: 3.1rem;
    border: none;
    border-radius: 14px;
    background: linear-gradient(90deg, var(--primary) 0%, #8F73FF 42%, #A78BFA 100%);
    color: var(--button-text);
    font-size: 1.02rem;
    font-weight: 700;
    letter-spacing: 0.01em;
    box-shadow: 0 12px 26px rgba(124, 92, 252, 0.18);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 16px 30px rgba(124, 92, 252, 0.22);
}

.secondary-button > button {
    background: var(--panel-bg) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-soft) !important;
    box-shadow: none !important;
}

.prediction-box {
    margin-top: 1.7rem;
    padding: 1.8rem 1.5rem 1.5rem;
    text-align: center;
    border-radius: 22px;
    border: 1px solid var(--border);
    background: var(--panel-bg);
    box-shadow: 0 18px 32px var(--shadow);
}

.prediction-label {
    color: var(--text-muted);
    font-size: 0.92rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    font-weight: 700;
}

.prediction-price {
    font-size: clamp(2.2rem, 4vw, 3.5rem);
    letter-spacing: -0.05em;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 0.75rem;
}

.prediction-model {
    color: var(--text-soft);
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.prediction-note {
    color: var(--text-muted);
    font-size: 0.9rem;
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

@media (max-width: 768px) {
    .hero {
        padding-top: 1rem;
    }

    .section-wrap {
        padding: 1rem 0.8rem 0.5rem;
    }
}
</style>
"""

style_css = (
    style_css.replace("__BG_1__", palette["bg-1"])
    .replace("__BG_2__", palette["bg-2"])
    .replace("__BG_3__", palette["bg-3"])
    .replace("__PANEL_BG__", palette["panel-bg"])
    .replace("__PANEL_BG_ALT__", palette["panel-bg-alt"])
    .replace("__PRIMARY__", palette["primary"])
    .replace("__PRIMARY_STRONG__", palette["primary-strong"])
    .replace("__ACCENT__", palette["accent"])
    .replace("__TEXT__", palette["text"])
    .replace("__TEXT_SOFT__", palette["text-soft"])
    .replace("__TEXT_MUTED__", palette["text-muted"])
    .replace("__BORDER__", palette["border"])
    .replace("__SHADOW__", palette["shadow"])
    .replace("__SOFT_PURPLE__", palette["soft-purple"])
    .replace("__SOFT_CYAN__", palette["soft-cyan"])
    .replace("__INPUT_BG__", palette["input-bg"])
    .replace("__BUTTON_TEXT__", palette["button-text"])
    .replace("__SIDEBAR_BG__", palette["sidebar-bg"])
    .replace("__SIDEBAR_ITEM_ACTIVE__", palette["sidebar-item-active"])
    .replace("__SIDEBAR_ITEM_ACTIVE_TEXT__", palette["sidebar-item-active-text"])
    .replace("__SIDEBAR_ITEM_HOVER__", palette["sidebar-item-hover"])
    .replace("__SIDEBAR_TEXT__", palette["sidebar-text"])
    .replace("__SIDEBAR_TEXT_SECONDARY__", palette["sidebar-text-secondary"])
)

st.markdown(style_css, unsafe_allow_html=True)


@st.cache_resource
def load_model():
    return load("RealEstate.joblib")


model = load_model()

FEATURES = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]


def get_default_values():
    return {
        "CRIM": 1.0,
        "ZN": 10.0,
        "INDUS": 10.0,
        "CHAS": 0,
        "NOX": 0.5,
        "RM": 6.0,
        "AGE": 50.0,
        "DIS": 4.0,
        "RAD": 4,
        "TAX": 300,
        "PTRATIO": 18.0,
        "B": 350.0,
        "LSTAT": 10.0,
    }


if "input_values" not in st.session_state:
    st.session_state.input_values = get_default_values()


st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">AI-Powered Estimation</div>
        <div class="hero-icon">🏠</div>
        <div class="hero-title">Real Estate Price Predictor</div>
        <div class="hero-subtitle">Estimate property value using machine learning</div>
    </div>
    """,
    unsafe_allow_html=True,
)


with st.form("prediction_form"):
    st.markdown(
        """
        <div class="section-wrap">
            <div class="section-header"><span class="dot"></span><h3>Property</h3></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    prop_col1, prop_col2, prop_col3 = st.columns(3)
    with prop_col1:
        st.number_input(
            "Average Number of Rooms",
            key="RM",
            min_value=0.0,
            value=float(st.session_state.input_values["RM"]),
            step=0.1,
            help="Average number of rooms per dwelling.",
        )
    with prop_col2:
        st.number_input(
            "Age of Houses",
            key="AGE",
            min_value=0.0,
            value=float(st.session_state.input_values["AGE"]),
            step=0.1,
            help="Proportion of owner-occupied homes built before 1940.",
        )
    with prop_col3:
        st.number_input(
            "Distance to Employment Centres",
            key="DIS",
            min_value=0.0,
            value=float(st.session_state.input_values["DIS"]),
            step=0.1,
            help="Weighted average distance to employment centers.",
        )

    st.markdown(
        """
        <div class="section-wrap">
            <div class="section-header"><span class="dot"></span><h3>Location</h3></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    loc_col1, loc_col2, loc_col3 = st.columns(3)
    with loc_col1:
        st.number_input(
            "Crime Rate",
            key="CRIM",
            min_value=0.0,
            value=float(st.session_state.input_values["CRIM"]),
            step=0.01,
            help="Per-capita crime rate in the area.",
        )
    with loc_col2:
        st.number_input(
            "Residential Land Zone",
            key="ZN",
            min_value=0.0,
            value=float(st.session_state.input_values["ZN"]),
            step=0.1,
            help="Proportion of residential land zoned for large lots.",
        )
    with loc_col3:
        st.selectbox(
            "Charles River Location",
            key="CHAS",
            options=[0, 1],
            index=int(st.session_state.input_values["CHAS"]),
            help="1 if the property borders the Charles River; otherwise 0.",
        )

    loc_col4, _, _ = st.columns([1, 1, 1])
    with loc_col4:
        st.number_input(
            "Highway Accessibility",
            key="RAD",
            min_value=0,
            value=int(st.session_state.input_values["RAD"]),
            help="Accessibility index to radial highways.",
        )

    st.markdown(
        """
        <div class="section-wrap">
            <div class="section-header"><span class="dot"></span><h3>Economic & Community</h3></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    eco_col1, eco_col2, eco_col3 = st.columns(3)
    with eco_col1:
        st.number_input(
            "Property Tax",
            key="TAX",
            min_value=0,
            value=int(st.session_state.input_values["TAX"]),
            help="Property tax rate per $10,000.",
        )
    with eco_col2:
        st.number_input(
            "Pupil-Teacher Ratio",
            key="PTRATIO",
            min_value=0.0,
            value=float(st.session_state.input_values["PTRATIO"]),
            step=0.1,
            help="Average student-to-teacher ratio by town.",
        )
    with eco_col3:
        st.number_input(
            "Lower Status Population",
            key="LSTAT",
            min_value=0.0,
            value=float(st.session_state.input_values["LSTAT"]),
            step=0.1,
            help="Percentage of lower-status population in the area.",
        )

    eco_col4, eco_col5, eco_col6 = st.columns(3)
    with eco_col4:
        st.number_input(
            "Non-Retail Business Area",
            key="INDUS",
            min_value=0.0,
            value=float(st.session_state.input_values["INDUS"]),
            step=0.1,
            help="Proportion of non-retail business acres per town.",
        )
    with eco_col5:
        st.number_input(
            "Nitric Oxide Concentration",
            key="NOX",
            min_value=0.0,
            value=float(st.session_state.input_values["NOX"]),
            step=0.001,
            help="Air pollution concentration (NOx).",
        )
    with eco_col6:
        st.number_input(
            "Population Index",
            key="B",
            min_value=0.0,
            value=float(st.session_state.input_values["B"]),
            step=0.1,
            help="Population proportion index for the area.",
        )

    predict_button, reset_button = st.columns([3, 1])

    with predict_button:
        submitted = st.form_submit_button("✨ Predict House Price", use_container_width=True)

    with reset_button:
        # reset is handled outside the form to avoid form-state confusion
        pass


if st.button("↻ Reset", key="reset_button", use_container_width=True, type="secondary"):
    for key in list(st.session_state.keys()):
        if key in ["input_values"]:
            continue
        st.session_state.pop(key, None)
    st.session_state.input_values = get_default_values()
    st.rerun()


if "prediction_result" in st.session_state:
    price = st.session_state["prediction_result"]
    st.markdown(
        """
        <div class="prediction-box">
            <div class="prediction-label">Your Estimated Value</div>
            <div class="prediction-price">$%s</div>
            <div class="prediction-model">Random Forest Regression</div>
            <div class="prediction-note">Based on the property information you provided</div>
        </div>
        """ % f"{price:,.0f}",
        unsafe_allow_html=True,
    )


if submitted:
    input_data = pd.DataFrame(
        [[
            st.session_state["CRIM"],
            st.session_state["ZN"],
            st.session_state["INDUS"],
            st.session_state["CHAS"],
            st.session_state["NOX"],
            st.session_state["RM"],
            st.session_state["AGE"],
            st.session_state["DIS"],
            st.session_state["RAD"],
            st.session_state["TAX"],
            st.session_state["PTRATIO"],
            st.session_state["B"],
            st.session_state["LSTAT"],
        ]],
        columns=FEATURES,
    )

    with st.spinner("Analyzing property..."):
        prediction = model.predict(input_data)
        price = prediction[0] * 1000
        st.session_state["prediction_result"] = price

    st.rerun()
