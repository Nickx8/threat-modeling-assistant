import streamlit as st
from risk import calculate_risk

st.set_page_config(
    page_title="Threat Modeling Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Threat Modeling Assistant")
st.write(
    "Analyze an application and generate assets, threats, "
    "risk scores, and security mitigations."
)

# -----------------------------
# Threat database
# -----------------------------

THREAT_DATABASE = [
    {
        "asset": "User Accounts",
        "threat": "Account Takeover",
        "likelihood": 4,
        "impact": 5,
        "mitigation": "Use MFA, strong password policies, account lockout, and secure authentication."
    },
    {
        "asset": "Database",
        "threat": "SQL Injection",
        "likelihood": 4,
        "impact": 5,
        "mitigation": "Use parameterized queries, input validation, and least-privilege database access."
    },
    {
        "asset": "User Input",
        "threat": "Cross-Site Scripting (XSS)",
        "likelihood": 3,
        "impact": 4,
        "mitigation": "Validate input, encode output, and implement a suitable Content Security Policy."
    },
    {
        "asset": "User Sessions",
        "threat": "Session Hijacking",
        "likelihood": 3,
        "impact": 4,
        "mitigation": "Use HTTPS, Secure and HttpOnly cookies, session expiration, and session rotation."
    },
    {
        "asset": "Personal Data",
        "threat": "Data Leakage",
        "likelihood": 3,
        "impact": 5,
        "mitigation": "Encrypt sensitive data and apply least-privilege access controls."
    },
    {
        "asset": "Application Functions",
        "threat": "Broken Access Control",
        "likelihood": 4,
        "impact": 5,
        "mitigation": "Perform authorization checks on the server and enforce least privilege."
    }
]


# -----------------------------
# Risk calculation
# -----------------------------

# -----------------------------
# Application information
# -----------------------------

st.subheader("1️⃣ Application Information")

application_name = st.text_input(
    "Application Name",
    placeholder="Example: E-Commerce Website"
)

application_type = st.selectbox(
    "Application Type",
    [
        "Web Application",
        "Mobile Application",
        "Desktop Application",
        "API",
        "Other"
    ]
)

authentication = st.selectbox(
    "Authentication Method",
    [
        "Username and Password",
        "Multi-Factor Authentication (MFA)",
        "Single Sign-On (SSO)",
        "No Authentication"
    ]
)

database = st.selectbox(
    "Database",
    [
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "SQLite",
        "Other",
        "No Database"
    ]
)

internet_facing = st.selectbox(
    "Is the application Internet-facing?",
    ["Yes", "No"]
)

sensitive_data = st.selectbox(
    "Does the application handle sensitive data?",
    ["Yes", "No"]
)


# -----------------------------
# Generate model
# -----------------------------

if st.button("🔍 Generate Threat Model"):

    if not application_name.strip():

        st.error("Please enter an application name.")

    else:

        # Basic input validation
        if len(application_name) > 100:
            st.error("Application name must be 100 characters or less.")
            st.stop()

        st.success(
            f"Threat model generated for {application_name}."
        )

        # -----------------------------
        # Application summary
        # -----------------------------

        st.subheader("2️⃣ Application Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("**Application**")
            st.write(application_name)

        with col2:
            st.write("**Type**")
            st.write(application_type)

        with col3:
            st.write("**Internet-facing**")
            st.write(internet_facing)

        st.write(f"**Authentication:** {authentication}")
        st.write(f"**Database:** {database}")
        st.write(f"**Sensitive Data:** {sensitive_data}")


        # -----------------------------
        # Asset identification
        # -----------------------------

        st.subheader("3️⃣ Identified Assets")

        assets = [
            "User Accounts",
            "Application Data"
        ]

        if database != "No Database":
            assets.append("Database")

        if authentication != "No Authentication":
            assets.append("Authentication Credentials")

        if sensitive_data == "Yes":
            assets.append("Sensitive / Personal Data")

        assets.append("Application Functions")

        for asset in assets:
            st.write(f"🔹 {asset}")


        # -----------------------------
        # Threat selection
        # -----------------------------

        selected_threats = []

        for threat in THREAT_DATABASE:

            if threat["threat"] == "SQL Injection":
                if database != "No Database":
                    selected_threats.append(threat)

            elif threat["threat"] == "Data Leakage":
                if sensitive_data == "Yes":
                    selected_threats.append(threat)

            elif threat["threat"] == "Session Hijacking":
                if authentication != "No Authentication":
                    selected_threats.append(threat)

            elif threat["threat"] == "Account Takeover":
                if authentication != "No Authentication":
                    selected_threats.append(threat)

            elif threat["threat"] == "Cross-Site Scripting (XSS)":
                if application_type in ["Web Application", "API"]:
                    selected_threats.append(threat)

            elif threat["threat"] == "Broken Access Control":
                selected_threats.append(threat)


        # -----------------------------
        # Threat analysis
        # -----------------------------

        st.subheader("4️⃣ Threat Analysis")

        for item in selected_threats:

            score, level = calculate_risk(
                item["likelihood"],
                item["impact"]
            )

            with st.expander(
                f"⚠️ {item['threat']} — {level}"
            ):

                st.write(f"**Asset:** {item['asset']}")
                st.write(
                    f"**Likelihood:** {item['likelihood']}/5"
                )
                st.write(
                    f"**Impact:** {item['impact']}/5"
                )
                st.write(
                    f"**Risk Score:** {score}/25"
                )
                st.write(
                    f"**Risk Level:** {level}"
                )

                st.write(
                    f"**Recommended Mitigation:** "
                    f"{item['mitigation']}"
                )


        # -----------------------------
        # Risk summary
        # -----------------------------

        st.subheader("5️⃣ Risk Summary")

        critical = 0
        high = 0
        medium = 0
        low = 0

        for item in selected_threats:

            score, level = calculate_risk(
                item["likelihood"],
                item["impact"]
            )

            if level == "Critical":
                critical += 1
            elif level == "High":
                high += 1
            elif level == "Medium":
                medium += 1
            else:
                low += 1

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Critical", critical)

        with col2:
            st.metric("High", high)

        with col3:
            st.metric("Medium", medium)

        with col4:
            st.metric("Low", low)

            # -----------------------------
        # Risk matrix
        # -----------------------------

        st.subheader("6️⃣ Risk Matrix")

        st.write(
            "Risk Score = Likelihood × Impact"
        )

        st.write(
            """
            **Risk Levels**

            - 1–4 → Low
            - 5–9 → Medium
            - 10–16 → High
            - 17–25 → Critical
            """
        )

        st.write("### Likelihood vs Impact")

        matrix_data = []

        for likelihood in range(5, 0, -1):

            row = []

            for impact in range(1, 6):

                score = likelihood * impact

                if score >= 17:
                    level = "Critical"
                elif score >= 10:
                    level = "High"
                elif score >= 5:
                    level = "Medium"
                else:
                    level = "Low"

                row.append(f"{score} ({level})")

            matrix_data.append(row)

        import pandas as pd

        matrix = pd.DataFrame(
            matrix_data,
            index=[
                "Likelihood 5",
                "Likelihood 4",
                "Likelihood 3",
                "Likelihood 2",
                "Likelihood 1"
            ],
            columns=[
                "Impact 1",
                "Impact 2",
                "Impact 3",
                "Impact 4",
                "Impact 5"
            ]
        )

        st.dataframe(
            matrix,
            use_container_width=True
        )


        # -----------------------------
        # Threat report
        # -----------------------------

        st.subheader("7️⃣ Threat Model Report")

        report_data = []

        for item in selected_threats:

            score, level = calculate_risk(
                item["likelihood"],
                item["impact"]
            )

            report_data.append({
                "Asset": item["asset"],
                "Threat": item["threat"],
                "Likelihood": item["likelihood"],
                "Impact": item["impact"],
                "Risk Score": score,
                "Risk Level": level,
                "Mitigation": item["mitigation"]
            })

        report_df = pd.DataFrame(report_data)

        st.dataframe(
            report_df,
            use_container_width=True
        )

        # Convert report to CSV

        csv_report = report_df.to_csv(
            index=False
        )

        st.download_button(
            label="⬇️ Download Threat Model Report",
            data=csv_report,
            file_name="threat_model_report.csv",
            mime="text/csv"
        )


        # -----------------------------
        # Final information
        # -----------------------------

        st.info(
            "Risk scores are calculated using "
            "Likelihood × Impact on a 1–5 scale."
        )

        st.success(
            "Threat modeling analysis completed."
        )

# -----------------------------
# Security Features
# -----------------------------

st.subheader("🔐 Security Features")

st.write(
    """
    The Threat Modeling Assistant includes the following
    security controls:

    - Input validation for application names
    - Maximum application name length of 100 characters
    - Risk value validation between 1 and 5
    - Safe in-memory CSV report generation
    - Error handling for invalid input
    - Least-privilege recommendations in threat mitigations
    """
)

        