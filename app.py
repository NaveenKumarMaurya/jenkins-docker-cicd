
import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Naveen CI/CD Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    font-size: 20px;
    color: #777;
}

.card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Controls")

name = st.sidebar.text_input(
    "👤 Your Name",
    "Naveen"
)

environment = st.sidebar.selectbox(
    "🌍 Environment",
    ["Development", "Testing", "Production"]
)

team = st.sidebar.selectbox(
    "👥 Team",
    ["Data Science", "GenAI", "DevOps", "Engineering"]
)

show_pipeline = st.sidebar.checkbox(
    "Show CI/CD Pipeline",
    True
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🚀 Naveen CI/CD Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Interactive Streamlit Application powered by Jenkins + Docker</div>',
    unsafe_allow_html=True
)

st.divider()

# ============================================================
# LIVE STATUS
# ============================================================

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🟢 Application",
        "ONLINE",
        "Healthy"
    )

with col2:
    st.metric(
        "🌍 Environment",
        environment
    )

with col3:
    st.metric(
        "👥 Team",
        team
    )

with col4:
    st.metric(
        "🕐 Server Time",
        current_time
    )

# ============================================================
# WELCOME
# ============================================================

st.header(f"👋 Welcome, {name}!")

st.write(
    f"""
You are currently running the application in the **{environment}**
environment as part of the **{team}** team.
"""
)

# ============================================================
# DYNAMIC CALCULATOR
# ============================================================

st.divider()

st.header("🧮 Interactive Calculator")

col1, col2, col3 = st.columns(3)

with col1:
    number1 = st.number_input(
        "First Number",
        value=10
    )

with col2:
    operation = st.selectbox(
        "Operation",
        ["+", "-", "×", "÷", "²"]
    )

with col3:
    number2 = st.number_input(
        "Second Number",
        value=5
    )

if st.button("Calculate 🚀"):

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    elif operation == "×":
        result = number1 * number2

    elif operation == "÷":
        if number2 == 0:
            st.error("❌ Cannot divide by zero")
            result = None
        else:
            result = number1 / number2

    else:
        result = number1 ** 2

    if result is not None:
        st.success(f"Result = {result}")

# ============================================================
# DYNAMIC DATA GENERATOR
# ============================================================

st.divider()

st.header("📊 Dynamic Data Generator")

rows = st.slider(
    "Number of data points",
    min_value=5,
    max_value=100,
    value=20
)

generate = st.button("Generate Data 📈")

if generate:

    np.random.seed(int(time.time()))

    data = pd.DataFrame({
        "Time": range(rows),
        "Performance": np.random.randint(50, 100, rows),
        "Requests": np.random.randint(10, 500, rows),
        "Latency": np.random.randint(20, 200, rows)
    })

    st.session_state["data"] = data

if "data" in st.session_state:

    data = st.session_state["data"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Performance")
        st.line_chart(
            data,
            x="Time",
            y="Performance"
        )

    with col2:
        st.subheader("⚡ Request Load")
        st.bar_chart(
            data,
            x="Time",
            y="Requests"
        )

    st.subheader("📋 Generated Data")

    st.dataframe(
        data,
        use_container_width=True
    )

# ============================================================
# PROGRESS TRACKER
# ============================================================

st.divider()

st.header("🎯 Project Progress")

progress = st.slider(
    "How much of the project is complete?",
    0,
    100,
    70
)

st.progress(progress / 100)

st.write(
    f"### {progress}% Complete"
)

if progress < 30:
    st.warning("🚧 Project is just getting started!")

elif progress < 70:
    st.info("🔨 Project is under development.")

elif progress < 100:
    st.success("🔥 Almost there!")

else:
    st.success("🎉 Project completed!")

# ============================================================
# TASK MANAGER
# ============================================================

st.divider()

st.header("📝 Mini Task Manager")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input(
    "Enter a new task"
)

if st.button("Add Task ➕"):

    if task.strip():

        st.session_state.tasks.append({
            "Task": task,
            "Status": "Pending"
        })

        st.success("Task added!")

if st.session_state.tasks:

    for i, item in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([5, 2, 1])

        with col1:
            st.write(f"**{i + 1}. {item['Task']}**")

        with col2:

            status = st.selectbox(
                "Status",
                ["Pending", "In Progress", "Completed"],
                index=[
                    "Pending",
                    "In Progress",
                    "Completed"
                ].index(item["Status"]),
                key=f"status_{i}"
            )

            st.session_state.tasks[i]["Status"] = status

        with col3:

            if st.button(
                "🗑️",
                key=f"delete_{i}"
            ):

                st.session_state.tasks.pop(i)
                st.rerun()

# ============================================================
# HEALTH CHECK
# ============================================================

st.divider()

st.header("🏥 Application Health")

if st.button("🔍 Run Health Check"):

    with st.spinner("Checking application..."):

        time.sleep(1)

    st.success("✅ Application is healthy!")

    health_data = {
        "Application": "Naveen CI/CD Dashboard",
        "Status": "Healthy",
        "Environment": environment,
        "Container": "Running",
        "Framework": "Streamlit",
        "Port": "8501",
        "Checked At": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    st.json(health_data)

# ============================================================
# CI/CD PIPELINE
# ============================================================

if show_pipeline:

    st.divider()

    st.header("🔄 CI/CD Pipeline")

    pipeline_steps = [
        "💻 Developer",
        "🐙 GitHub",
        "🔨 Jenkins",
        "🐳 Docker Build",
        "📦 Docker Image",
        "🚀 Deployment",
        "🌐 Streamlit"
    ]

    cols = st.columns(len(pipeline_steps))

    for col, step in zip(cols, pipeline_steps):

        with col:

            st.success(step)

    st.write("")

    if st.button("🚀 Simulate Deployment"):

        progress_bar = st.progress(0)

        status_text = st.empty()

        steps = [
            "Checking GitHub...",
            "Jenkins starting build...",
            "Running tests...",
            "Building Docker image...",
            "Starting container...",
            "Deploying application...",
            "Deployment successful!"
        ]

        for i, step in enumerate(steps):

            status_text.info(step)

            progress_bar.progress(
                int((i + 1) / len(steps) * 100)
            )

            time.sleep(0.5)

        st.success(
            "🎉 Deployment completed successfully!"
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    f"🚀 Naveen Maurya | Jenkins + Docker + Streamlit | "
    f"Environment: {environment}"
)

