import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Configure page
st.set_page_config(page_title="App 2 - Data Distributions", layout="wide")


st.title("App 2: Data Distributions")
st.write(
    "Demographic, health, lifestyle, and cost-related"
    "distributions in the customers dataset."
)

# Load dataset
df = pd.read_csv("data/processed/cleaned_customers.csv")

# Column groups
demographic_cols = ["region", "urban_rural", "age", "sex"]
health_cols = [
    "hypertension",
    "diabetes",
    "asthma",
    "copd",
    "cardiovascular_disease",
    "cancer_history",
]
lifestyle_cols = ["bmi", "smoker", "alcohol_freq", "visits_last_year"]


# FUNCTIONS
def plot_demographics(df):
    st.subheader("Demographic and Socioeconomic Distributions")
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    # Sex distribution
    sns.countplot(
        data=df,
        x="sex",
        palette=["royalblue", "darksalmon", "peachpuff"],
        ax=axes[0, 0],
    ).set_title("Sex Distribution", fontsize=15, fontweight="bold")

    # Age distribution
    sns.histplot(
        data=df,
        x="age",
        bins=20,
        color="royalblue",
        ax=axes[0, 1],
    ).set_title("Age Distribution", fontsize=15, fontweight="bold")

    # Income distribution
    sns.histplot(
        data=df,
        x="income",
        bins=50,
        color="royalblue",
        ax=axes[1, 0],
    ).set_title("Income Distribution", fontsize=15, fontweight="bold")

    # Employment status bar chart
    counts = df["employment_status"].value_counts()
    sns.barplot(
        x=counts.index,
        y=counts.values,
        palette="muted",
        ax=axes[1, 1],
    )
    axes[1, 1].set_title("Employment Status", fontsize=15, fontweight="bold")
    axes[1, 1].set_xlabel("Employment Status", fontsize=12)
    axes[1, 1].set_ylabel("Count", fontsize=12)
    axes[1, 1].tick_params(axis="x", rotation=30)
    axes[1, 1].grid(True, linestyle="--", alpha=0.6)

    # Formatting for all axes
    for ax in axes.flat:
        ax.set_xlabel(ax.get_xlabel().replace("_", " ").title(), fontsize=12)
        ax.set_ylabel(ax.get_ylabel().replace("_", " ").title(), fontsize=12)
        ax.tick_params(axis="x", rotation=30)
        ax.grid(True, linestyle="--", alpha=0.6)

    fig.suptitle(
        "Demographic and Socioeconomic Distributions",
        fontsize=18,
        fontweight="bold",
    )
    plt.tight_layout()
    st.pyplot(fig)


def plot_health_conditions(df):
    st.subheader("Health Condition Distribution")
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))

    # Hypertension
    counts = df["hypertension"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[0, 0].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[0, 0].set_title(
        f"Hypertension\n({pct:.1f}% affected)", fontsize=15, fontweight="bold"
    )

    # Diabetes
    counts = df["diabetes"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[0, 1].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[0, 1].set_title(
        f"Diabetes\n({pct:.1f}% affected)", fontsize=15, fontweight="bold"
    )

    # Asthma
    counts = df["asthma"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[0, 2].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[0, 2].set_title(
        f"Asthma\n({pct:.1f}% affected)", fontsize=15, fontweight="bold"
    )

    # COPD
    counts = df["copd"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[1, 0].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[1, 0].set_title(
        f"COPD\n({pct:.1f}% affected)", fontsize=15, fontweight="bold"
    )

    # Cardiovascular disease
    counts = df["cardiovascular_disease"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[1, 1].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[1, 1].set_title(
        f"Cardiovascular Disease\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )

    # Cancer history
    counts = df["cancer_history"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    axes[1, 2].pie(
        counts,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        colors=["royalblue", "darksalmon"],
        startangle=90,
    )
    axes[1, 2].set_title(
        f"Cancer History\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )

    fig.suptitle(
        "Health Condition Distribution", fontsize=18, fontweight="bold"
    )
    plt.tight_layout()
    st.pyplot(fig)


def plot_health_conditions_varied(df):
    st.subheader("Health Condition Distribution (Varied Graphs)")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Hypertension: Bar plot vs cost
    counts = df["hypertension"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    sns.barplot(
        x=df["hypertension"].map({0: "No", 1: "Yes"}),
        y=df["annual_medical_cost"],
        palette=["royalblue", "darksalmon"],
        ax=axes[0, 0],
    )
    axes[0, 0].set_title(
        f"Hypertension vs Cost\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )

    # COPD: Bar plot vs cost
    counts = df["copd"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    sns.barplot(
        x=df["copd"].map({0: "No", 1: "Yes"}),
        y=df["annual_medical_cost"],
        palette=["royalblue", "darksalmon"],
        ax=axes[0, 1],
    )
    axes[0, 1].set_title(
        f"COPD vs Cost\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )

    # Cardiovascular Disease: Bar plot vs cost
    counts = df["cardiovascular_disease"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100
    sns.barplot(
        x=df["cardiovascular_disease"].map({0: "No", 1: "Yes"}),
        y=df["annual_medical_cost"],
        palette=["royalblue", "darksalmon"],
        ax=axes[1, 0],
    )
    axes[1, 0].set_title(
        f"Cardiovascular Disease vs Cost\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )

    # Cancer History: Histogram split by cancer history
    counts = df["cancer_history"].value_counts()
    pct = counts.get(1, 0) / counts.sum() * 100

    sns.barplot(
        x=df["cancer_history"].map({0: "No", 1: "Yes"}),
        y=df["annual_medical_cost"],
        palette=["royalblue", "darksalmon"],
        ax=axes[1, 1],
    )

    axes[1, 1].set_title(
        f"Cancer History vs Cost\n({pct:.1f}% affected)",
        fontsize=15,
        fontweight="bold",
    )
    axes[1, 1].set_xlabel("Cancer History", fontsize=12)
    axes[1, 1].set_ylabel("Average Annual Medical Cost", fontsize=12)
    axes[1, 1].grid(True, linestyle="--", alpha=0.6)

    # Title
    axes[1, 1].set_title(
        "Cancer History vs Cost Distribution", fontsize=15, fontweight="bold"
    )

    # Formatting
    for ax in axes.flat:
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.set_ylabel(ax.get_ylabel().replace("_", " ").title(), fontsize=12)

    fig.suptitle(
        "Health Condition Distribution (Varied Graphs)",
        fontsize=18,
        fontweight="bold",
    )
    plt.tight_layout()
    st.pyplot(fig)


def plot_cost_factors(df):
    st.subheader("Various Factors Affecting Annual Medical Cost")
    fig, axes = plt.subplots(2, 3, figsize=(20, 13))
    fig.suptitle(
        "Various Factors Affecting Annual Medical Cost",
        fontsize=18,
        fontweight="bold",
    )

    sns.scatterplot(
        x=df["bmi"],
        y=df["annual_medical_cost"],
        ax=axes[0, 0],
        color="royalblue",
    ).set_title("BMI vs Annual Medical Cost", fontsize=15, fontweight="bold")

    sns.scatterplot(
        x=df["age"],
        y=df["annual_medical_cost"],
        ax=axes[0, 1],
        color="darksalmon",
    ).set_title("Age vs Annual Medical Cost", fontsize=15, fontweight="bold")

    sns.histplot(
        data=df,
        x="annual_medical_cost",
        bins=50,
        color="royalblue",
        ax=axes[0, 2],
    ).set_title(
        "Annual Medical Cost Distribution", fontsize=15, fontweight="bold"
    )

    sns.barplot(
        x=df["smoker"],
        y=df["annual_medical_cost"],
        ax=axes[1, 0],
        palette=["royalblue", "darksalmon", "gold"],
    ).set_title(
        "Smoker vs Annual Medical Cost", fontsize=15, fontweight="bold"
    )

    # Average cost vs age group bar plot
    bins = [0, 30, 40, 50, 60, 70, 120]
    labels = ["<30", "30-40", "40-50", "50-60", "60-70", "70+"]

    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)

    sns.barplot(
        data=df,
        x="age_group",
        y="annual_medical_cost",
        palette="Blues",
        ax=axes[1, 1],
    )

    axes[1, 2].set_title(
        "Average Annual Medical Cost by Age Group",
        fontsize=15,
        fontweight="bold",
    )
    axes[1, 2].set_xlabel("Age Group", fontsize=12)
    axes[1, 2].set_ylabel("Average Annual Medical Cost", fontsize=12)
    axes[1, 2].grid(True, linestyle="--", alpha=0.6)

    # Chronic count: Bar plot vs cost
    df["chronic_bucket"] = pd.cut(
        df["chronic_count"],
        bins=[0, 1, 2, 3, 4, float("inf")],
        labels=["1", "2", "3", "4", "5+"],
        right=True,
    )

    #
    sns.barplot(
        data=df,
        x="chronic_bucket",
        y="annual_medical_cost",
        palette="coolwarm",
        ax=axes[1, 2],
    )

    axes[1, 2].set_title(
        "Average Annual Medical Cost by Chronic Condition Count",
        fontsize=15,
        fontweight="bold",
    )
    axes[1, 2].set_xlabel("Number of Chronic Conditions", fontsize=12)
    axes[1, 2].set_ylabel("Average Annual Medical Cost", fontsize=12)
    axes[1, 2].grid(True, linestyle="--", alpha=0.6)

    # Loop all axes
    for ax in axes.flat:
        ax.set_xlabel(ax.get_xlabel().replace("_", " ").title(), fontsize=12)
        ax.set_ylabel(ax.get_ylabel().replace("_", " ").title(), fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    st.pyplot(fig)


plot_demographics(df)
plot_health_conditions(df)
plot_health_conditions_varied(df)
plot_cost_factors(df)
# plot_sex_vs_cost(df)
