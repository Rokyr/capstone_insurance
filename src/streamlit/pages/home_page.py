import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Capstone Insurance ETL Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Home Page")
st.subheader("Welcome to the Capstone Insurance ETL Dashboard")

st.markdown(
    """
The dataset used in this project comes from Kaggle:
[Medical Insurance Cost Prediction
Dataset](https://www.kaggle.com/datasets/mohankrishnathalla/medical-insurance-cost-prediction/data)
"""
)

# Helpful navigation guide
st.markdown(
    """
    ###  Available Pages
    - **App 1** — Comparison and interactive correlation dashboard
    - **App 2** — Analysis and visualisations
    """
)

st.divider()


# Demographics
st.markdown(
    "This dataset is organised into several groups"
    "of variables, each reflecting different aspects "
    "of patient information, healthcare usage, and insurance details."
)

# Demographics
st.header("1. Demographics & Socioeconomic Factors")
st.write(
    """
These columns describe the background and living circumstances of
each individual:
- **age**: Age of the person
- **income**: Annual income level
- **education**: Highest level of education attained
- **household_size**: Number of people in the household
- **dependents**: Number of dependants supported
"""
)

# Health
st.header("2. Health & Clinical Indicators")
st.write(
    """
These variables capture lifestyle habits and medical conditions:
- **bmi**: Body Mass Index
- **smoker**: Smoking status
- **alcohol_freq**: Frequency of alcohol consumption
- **chronic_count**: Number of chronic conditions
- **hypertension**, **diabetes**, **asthma**, **copd**,
**cardiovascular_disease**, **cancer_history**, **kidney_disease**,
**liver_disease**, **arthritis**, **mental_health**
- **systolic_bp**, **diastolic_bp**: Blood pressure readings
- **ldl**: Cholesterol level
- **hba1c**: Blood sugar control marker
"""
)

# Claims
st.header("3. Healthcare Utilisation & Claims")
st.write(
    """
These features track healthcare usage and procedures:
- **visits_last_year**: Number of GP or hospital visits in the past year
- **had_major_procedure**: Whether a major procedure was undertaken
- **hospitalisations_last_3yrs**: Number of hospital admissions
in the last three years
- **days_hospitalised_last_3yrs**: Total days spent in hospital
- **medication_count**: Number of prescribed medicines
- **proc_imaging_count**, **proc_surgery_count**,
**proc_physio_count**, **proc_consult_count**, **proc_lab_count**:
Counts of different procedure types
"""
)

# Risk
st.header("4. Risk Assessment")
st.write(
    """
These variables summarise financial and clinical risk:
- **claims_count**: Total number of claims submitted
- **avg_claim_amount**: Average claim value
- **total_claims_paid**: Total amount paid in claims
- **risk_score**: Calculated risk score
- **is_high_risk**: Indicator for high-risk individuals
"""
)

# Insurance
st.header("5. Insurance & Policy Details")
st.write(
    """
These columns describe the insurance plan and associated costs:
- **deductible**: Deductible amount
- **copay**: Co-payment amount
- **policy_term_years**: Length of policy term
- **policy_changes_last_2yrs**: Number of changes in the last two years
- **provider_quality**: Quality rating of provider
- **annual_medical_cost**: Annual medical expenses
- **annual_premium**: Annual insurance premium
- **monthly_premium**: Monthly insurance premium
"""
)
