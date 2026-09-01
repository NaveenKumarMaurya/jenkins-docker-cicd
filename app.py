import streamlit as st
# ============================================================
# MECHANICAL ENGINEERING CALCULATOR
# ============================================================

st.divider()

st.header("⚙️ Mechanical Engineering Calculator")

st.write(
    "Perform common mechanical engineering calculations "
    "and experiment with different engineering parameters."
)

calculation = st.selectbox(
    "Select Calculation",
    [
        "🔩 Torque",
        "⚡ Power from Torque & RPM",
        "🏗️ Normal Stress",
        "📏 Strain",
        "🧱 Young's Modulus",
        "🔧 Beam Bending Stress",
        "🛡️ Factor of Safety"
    ]
)

# ============================================================
# TORQUE
# ============================================================

if calculation == "🔩 Torque":

    st.subheader("🔩 Torque Calculator")

    col1, col2 = st.columns(2)

    with col1:
        force = st.number_input(
            "Force (N)",
            min_value=0.0,
            value=100.0,
            step=10.0
        )

    with col2:
        radius = st.number_input(
            "Lever Arm / Radius (m)",
            min_value=0.0,
            value=0.5,
            step=0.1
        )

    if st.button("Calculate Torque", key="torque"):

        torque = force * radius

        st.success(
            f"Torque = **{torque:.2f} N·m**"
        )

        st.metric(
            "Torque",
            f"{torque:.2f} N·m"
        )


# ============================================================
# POWER
# ============================================================

elif calculation == "⚡ Power from Torque & RPM":

    st.subheader("⚡ Motor Power Calculator")

    col1, col2 = st.columns(2)

    with col1:
        torque = st.number_input(
            "Torque (N·m)",
            min_value=0.0,
            value=50.0,
            step=5.0
        )

    with col2:
        rpm = st.number_input(
            "Speed (RPM)",
            min_value=0.0,
            value=1500.0,
            step=100.0
        )

    if st.button("Calculate Power", key="power"):

        power_watts = (2 * np.pi * rpm * torque) / 60
        power_kw = power_watts / 1000

        st.success(
            f"Mechanical Power = **{power_kw:.2f} kW**"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Power",
                f"{power_kw:.2f} kW"
            )

        with col2:
            st.metric(
                "Power",
                f"{power_watts:.0f} W"
            )


# ============================================================
# NORMAL STRESS
# ============================================================

elif calculation == "🏗️ Normal Stress":

    st.subheader("🏗️ Normal Stress Calculator")

    col1, col2 = st.columns(2)

    with col1:
        force = st.number_input(
            "Applied Force (N)",
            min_value=0.0,
            value=10000.0,
            step=1000.0
        )

    with col2:
        area = st.number_input(
            "Cross-sectional Area (mm²)",
            min_value=0.01,
            value=100.0,
            step=10.0
        )

    if st.button("Calculate Stress", key="stress"):

        # N/mm² = MPa
        stress = force / area

        st.success(
            f"Normal Stress = **{stress:.2f} MPa**"
        )

        st.metric(
            "Stress",
            f"{stress:.2f} MPa"
        )


# ============================================================
# STRAIN
# ============================================================

elif calculation == "📏 Strain":

    st.subheader("📏 Strain Calculator")

    col1, col2 = st.columns(2)

    with col1:
        original_length = st.number_input(
            "Original Length (mm)",
            min_value=0.01,
            value=100.0,
            step=10.0
        )

    with col2:
        change_length = st.number_input(
            "Change in Length (mm)",
            value=0.5,
            step=0.1
        )

    if st.button("Calculate Strain", key="strain"):

        strain = change_length / original_length

        st.success(
            f"Strain = **{strain:.6f}**"
        )

        st.metric(
            "Engineering Strain",
            f"{strain:.6f}"
        )


# ============================================================
# YOUNG'S MODULUS
# ============================================================

elif calculation == "🧱 Young's Modulus":

    st.subheader("🧱 Young's Modulus Calculator")

    col1, col2 = st.columns(2)

    with col1:
        stress = st.number_input(
            "Stress (MPa)",
            min_value=0.0,
            value=200.0,
            step=10.0
        )

    with col2:
        strain = st.number_input(
            "Strain",
            min_value=0.000001,
            value=0.001,
            format="%.6f"
        )

    if st.button("Calculate Young's Modulus", key="young"):

        young_modulus = stress / strain

        st.success(
            f"Young's Modulus = **{young_modulus:.2f} MPa**"
        )

        st.metric(
            "Young's Modulus",
            f"{young_modulus / 1000:.2f} GPa"
        )


# ============================================================
# BEAM BENDING STRESS
# ============================================================

elif calculation == "🔧 Beam Bending Stress":

    st.subheader("🔧 Beam Bending Stress")

    st.info(
        "Formula: σ = Mc / I"
    )

    col1, col2 = st.columns(2)

    with col1:
        bending_moment = st.number_input(
            "Bending Moment M (N·m)",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )

        distance = st.number_input(
            "Distance from Neutral Axis c (m)",
            min_value=0.0001,
            value=0.05,
            step=0.01
        )

    with col2:
        moment_inertia = st.number_input(
            "Second Moment of Area I (m⁴)",
            min_value=0.00000001,
            value=0.00001,
            format="%.8f"
        )

    if st.button(
        "Calculate Bending Stress",
        key="bending"
    ):

        bending_stress = (
            bending_moment * distance
        ) / moment_inertia

        stress_mpa = bending_stress / 1_000_000

        st.success(
            f"Bending Stress = **{stress_mpa:.2f} MPa**"
        )

        st.metric(
            "Bending Stress",
            f"{stress_mpa:.2f} MPa"
        )


# ============================================================
# FACTOR OF SAFETY
# ============================================================

elif calculation == "🛡️ Factor of Safety":

    st.subheader("🛡️ Factor of Safety Calculator")

    col1, col2 = st.columns(2)

    with col1:
        yield_strength = st.number_input(
            "Material Yield Strength (MPa)",
            min_value=0.0,
            value=250.0,
            step=10.0
        )

    with col2:
        working_stress = st.number_input(
            "Working Stress (MPa)",
            min_value=0.01,
            value=100.0,
            step=10.0
        )

    if st.button(
        "Calculate Factor of Safety",
        key="fos"
    ):

        fos = yield_strength / working_stress

        st.metric(
            "Factor of Safety",
            f"{fos:.2f}"
        )

        if fos < 1:
            st.error(
                "⚠️ Factor of Safety < 1 — unsafe condition!"
            )

        elif fos < 1.5:
            st.warning(
                "⚠️ Low Factor of Safety"
            )

        elif fos < 2:
            st.info(
                "ℹ️ Moderate Factor of Safety"
            )

        else:
            st.success(
                "✅ Factor of Safety is above 2"
            )

