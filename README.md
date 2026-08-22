\# 🛡️ Threat Modeling Assistant



\## Project Overview



Threat Modeling Assistant is a simple cybersecurity application that helps identify application assets, potential threats, risk levels, and recommended security mitigations.



The project is designed as a small MVP for security analysis in an authorized or isolated environment.



\## Objective



The objective of this project is to demonstrate how threat modeling can be partially automated by taking basic application information and generating:



\- Application assets

\- Potential security threats

\- STRIDE threat categories

\- Likelihood and impact values

\- Risk scores

\- Risk levels

\- Recommended mitigations

\- Threat model reports



\## Features



\### 1. Application Information



The user provides:



\- Application name

\- Application type

\- Authentication method

\- Database

\- Internet-facing status

\- Sensitive data status



\### 2. Asset Identification



The application identifies important assets such as:



\- User accounts

\- Application data

\- Database

\- Authentication credentials

\- Sensitive or personal data

\- Application functions



\### 3. Threat Identification



The assistant identifies potential threats including:



\- Account Takeover

\- SQL Injection

\- Cross-Site Scripting

\- Session Hijacking

\- Data Leakage

\- Broken Access Control

\- Unauthorized Data Modification

\- Insufficient Audit Logging

\- Application Denial of Service



\## Threat Modeling Methodology



The project uses the STRIDE methodology.



\### STRIDE



\- \*\*Spoofing\*\* — Pretending to be another identity

\- \*\*Tampering\*\* — Unauthorized modification of data

\- \*\*Repudiation\*\* — Denying an action or transaction

\- \*\*Information Disclosure\*\* — Unauthorized exposure of information

\- \*\*Denial of Service\*\* — Affecting availability of a service

\- \*\*Elevation of Privilege\*\* — Obtaining unauthorized privileges



\## Risk Calculation



Risk is calculated using:



\*\*Risk Score = Likelihood × Impact\*\*



Both likelihood and impact use a scale from 1 to 5.



\### Risk Levels



| Score | Risk Level |

|---|---|

| 1–4 | Low |

| 5–9 | Medium |

| 10–16 | High |

| 17–25 | Critical |



\## Security Features



The application includes:



\- Application name input validation

\- Maximum input length validation

\- Risk value validation

\- Error handling for invalid values

\- Safe in-memory CSV report generation

\- Least-privilege recommendations

\- Risk-based threat prioritization



\## Technology Used



\- Python

\- Streamlit

\- Pandas

\- Pytest



\## Project Structure



```text

threat-modeling-assistant/

│

├── app.py

├── risk.py

├── requirements.txt

├── README.md

│

└── tests/

&#x20;   └── test\_risk.py

