import streamlit as st
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Naveen CI/CD Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 Naveen Maurya - Jenkins CI/CD Dashboard")
st.subheader("Streamlit application deployed using Jenkins + Docker")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ Controls")

name = st.sidebar.text_input(
    "Enter your name",
    value="Naveen"
)

environment = st.sidebar.selectbox(
    "Select Environment",
    ["Development", "Testing", "Production"]
)

# -----------------------------
# Main Dashboard
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Application Status",
        value="ONLINE",
        delta="Healthy"
    )

with col2:
    st.metric(
        label="Environment",
        value=environment
    )

with col3:
    st.metric(
        label="Deployment",
        value="Jenkins",
        delta="CI/CD"
    )

st.divider()

# -----------------------------
# Greeting
# -----------------------------
st.header("👋 Welcome")

st.write(
    f"Hello **{name}**! 👋"
)

st.write(
    "This Streamlit application is running through a Jenkins CI/CD pipeline."
)

# -----------------------------
# Interactive Feature
# -----------------------------
st.header("🧪 Test Application")

number = st.slider(
    "Select a number",
    min_value=1,
    max_value=100,
    value=10
)

if st.button("Calculate Square 🚀"):
    result = number ** 2

    st.success(
        f"The square of {number} is **{result}**"
    )

# -----------------------------
# Health Check
# -----------------------------
st.divider()

st.header("🏥 Application Health")

if st.button("Check Health"):

    st.success("✅ Application is healthy!")

    st.json({
        "status": "healthy",
        "application": "Naveen CI/CD Dashboard",
        "environment": environment,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# -----------------------------
# Deployment Information
# -----------------------------
st.divider()

st.header("🔄 CI/CD Information")

st.info(
    """
    **Pipeline Flow**

    GitHub → Jenkins → Docker Build → Docker Container → Streamlit UI
    """
)

st.write("### Current Application")

st.code(
    """
    Streamlit
        ↓
    Docker
        ↓
    Jenkins
        ↓
    GitHub
    """,
    language="text"
)

st.divider()

st.caption(
    "Built by Naveen Maurya | Jenkins CI/CD Learning Project 🚀"
)