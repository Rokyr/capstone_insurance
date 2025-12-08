import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    # Wide layout
    st.set_page_config(layout="wide")
    st.title("Capstone Insurance ETL Dashboard")
    st.divider()

    # Load cleaned dataset
    customers_df = pd.read_csv("data/processed/cleaned_customers.csv")

    # Define column groups
    demographics_cols = [
        "age",
        "income",
        "education",
        "household_size",
        "dependents",
    ]
    health_cols = [
        "bmi",
        "smoker",
        "alcohol_freq",
        "chronic_count",
        "hypertension",
        "diabetes",
        "asthma",
        "copd",
        "cardiovascular_disease",
        "cancer_history",
        "kidney_disease",
        "liver_disease",
        "arthritis",
        "mental_health",
        "systolic_bp",
        "diastolic_bp",
        "ldl",
        "hba1c",
    ]
    claims_cols = [
        "visits_last_year",
        "had_major_procedure",
        "hospitalizations_last_3yrs",
        "days_hospitalized_last_3yrs",
        "medication_count",
        "proc_imaging_count",
        "proc_surgery_count",
        "proc_physio_count",
        "proc_consult_count",
        "proc_lab_count",
    ]
    risk_cols = [
        "claims_count",
        "avg_claim_amount",
        "total_claims_paid",
        "risk_score",
        "is_high_risk",
    ]
    insurance_cols = [
        "deductible",
        "copay",
        "policy_term_years",
        "policy_changes_last_2yrs",
        "provider_quality",
        "annual_medical_cost",
        "annual_premium",
        "monthly_premium",
    ]

    groups = {
        "Demographics": demographics_cols,
        "Health & Conditions": health_cols,
        "Healthcare & Claims": claims_cols,
        "Risk Indicators": risk_cols,
        "Insurance & Plan": insurance_cols,
    }

    # Assign parent colors
    group_colors = {
        "Demographics": "lightblue",
        "Health & Conditions": "lightgreen",
        "Healthcare & Claims": "lightcoral",
        "Risk Indicators": "khaki",
        "Insurance & Plan": "plum",
    }
    # Child color mapping
    var_colors = {}
    for i, j in groups.items():
        for col in j:
            var_colors[col] = group_colors[i]

    # Split into two columns
    col1, col2 = st.columns([1, 4])

    with col1:
        st.header("Select Data Groups")

        selected_groups = []
        for i in groups.keys():
            # Further split into two small columns: 1 for the checkbox,
            # 1 for the colored label
            c1, c2 = st.columns([0.1, 0.9])
            with c1:
                checked = st.checkbox(
                    "",
                    value=False,  # nothing pre-selected
                    key=i,
                )
            with c2:
                st.markdown(
                    f"<span style='color:{group_colors[i]}; "
                    f"font-weight:bold;'>{i}</span>",
                    unsafe_allow_html=True,
                )

            if checked:
                selected_groups.append(i)

        # Collect selected columns
        selected_cols = []
        for g in selected_groups:
            selected_cols.extend(groups[g])

        # Create search box to find correlations
        numeric_cols = customers_df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()
        numeric_cols = sorted(numeric_cols)

        st.markdown(
            "<h3><b>Select variable to explore correlations:</b></h3>",
            unsafe_allow_html=True,
        )

        target_col = st.selectbox(
            "",
            options=numeric_cols,
            help="Start typing to see suggestions",
        )

        # Show correlation with annual_premium
        if "annual_premium" in customers_df.columns:
            corr_value = (
                customers_df[numeric_cols]
                .corr()
                .loc[target_col, "annual_premium"]
            )
            r_squared = corr_value**2

            st.metric(
                "Correlation with annual_premium (r)", f"{corr_value:.3f}"
            )
            st.metric("Coefficient of determination (r²)", f"{r_squared:.3f}")
            st.caption(
                "Correlation (r) shows how strongly and in which direction"
                "the variable relates to annual_premium. The "
                "r² value shows how much of the variation in annual_premium"
                "is explained by that variable."
            )
        else:
            st.warning("annual_premium column not found in dataset.")

    with col2:
        if selected_cols:
            # Compute correlations with the selected variable,
            # Only for the values in the SELECT DATA GROUPS.
            corr_all = (
                customers_df[numeric_cols].corr()[target_col].drop(target_col)
            )
            corr_with_target = corr_all.loc[
                corr_all.index.intersection(selected_cols)
            ]
            corr_with_target = corr_with_target.sort_values(ascending=False)

            st.subheader(f"Correlation with {target_col}")
            fig, ax = plt.subplots(figsize=(8, 6))

            # Assign colors based on groups
            palette = [
                var_colors.get(var, "grey") for var in corr_with_target.index
            ]
            sns.barplot(
                x=corr_with_target.values,
                y=corr_with_target.index,
                palette=palette,
                ax=ax,
            )
            ax.set_title(f"Correlation of variables with {target_col}")
            ax.set_xlabel("Correlation coefficient")
            ax.set_ylabel("Variable")
            ax.axvline(0, color="black", linewidth=0.8)

            st.pyplot(fig)
        else:
            st.info("Graph will appear once you select data groups.")


if __name__ == "__main__":
    main()
