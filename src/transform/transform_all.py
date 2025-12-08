import pandas as pd

from src.utils.file_utils import save_dataframe_to_csv
from src.utils.logging_utils import setup_logger

pd.set_option("future.no_silent_downcasting", True)


OUTPUT_DIR = "data/processed"
FILE_NAME_CLEAN_CUSTOMERS = "cleaned_customers.csv"
FILE_NAME_CORRELATION_TABLE = "correlation_table.csv"

logger = setup_logger("transform_data_all", "transform_data_all.log")


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    # Trim values
    logger.info("Running trim_values(customers)...")
    customers = trim_values(customers)
    # Remove duplicate rows
    logger.info("Running drop_duplicates(customers)...")
    customers = drop_duplicates(customers)

    # Map categorical features to numeric codes
    logger.info("Running map_alcohol_freq(customers)..")
    customers = map_alcohol_freq(customers)
    logger.info("Running map_smoker_freq(customers)..")
    customers = map_smoker_freq(customers)
    logger.info("Running map_education_freq(customers)..")
    customers = map_education(customers)

    # Save the dataframe as a CSV for logging purposes
    # Ensure the directory exists
    logger.info(
        "Running save_dataframe_to_csv(customers, "
        "OUTPUT_DIR, FILE_NAME_CLEAN_CUSTOMERS).."
    )
    save_dataframe_to_csv(customers, OUTPUT_DIR, FILE_NAME_CLEAN_CUSTOMERS)
    logger.info(
        f"Cleaned customers with shape {customers.shape} saved to CSV."
    )

    return customers


def produce_correlation_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Produce and save a correlation table for numeric
    columns in the given DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame containing mixed data types.

    Returns:
        pd.DataFrame: Correlation table with explicit headers,
        suitable for saving or loading into database!
    """

    # Isolate numeric columns
    logger.info("Running create_numeric_cols_df(df)...")
    numeric_cols = create_numeric_cols_df(df)

    # Create a correlation table for numeric columns
    logger.info("Creating correlation table...")
    correlation_table = df[numeric_cols].corr()

    # Reset index and rename columns
    correlation_table = correlation_table.reset_index().rename(
        columns={"index": "feature"}
    )

    # Save the correlation table
    save_dataframe_to_csv(
        correlation_table, OUTPUT_DIR, FILE_NAME_CORRELATION_TABLE
    )
    logger.info(
        f"Correlation table with shape {correlation_table.shape} saved to CSV."
    )
    return correlation_table


def trim_values(customers: pd.DataFrame) -> pd.DataFrame:
    # Apply strip() to all object/string columns
    for col in customers.select_dtypes(include=["object", "string"]).columns:
        customers[col] = customers[col].astype(str).str.strip()

    return customers


def drop_duplicates(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate rows from the DataFrame
    customers = customers.drop_duplicates()
    return customers


def map_alcohol_freq(customers: pd.DataFrame) -> pd.DataFrame:
    # Map alcohol frequency categories to numerics
    customers["alcohol_freq"] = (
        customers["alcohol_freq"]
        .replace({"nan": 0, "Weekly": 7, "Daily": 30, "Occasional": 2})
        .fillna(0)
        .infer_objects(copy=False)
    )
    return customers


def map_smoker_freq(customers: pd.DataFrame) -> pd.DataFrame:
    # Map smoker categories to numerics
    customers["smoker"] = (
        customers["smoker"]
        .replace({"Never": 0, "Current": 30, "Former": 7})
        .astype("int64")
        .infer_objects(copy=False)
    )
    return customers


def map_education(customers: pd.DataFrame) -> pd.DataFrame:
    # Map education categories to numerics
    education_map = {
        "No HS": 0,
        "HS": 1,
        "Some College": 2,
        "Bachelors": 3,
        "Masters": 4,
        "Doctorate": 5,
    }
    customers["education"] = (
        customers["education"]
        .replace(education_map)
        .astype("int64")
        .infer_objects(copy=False)
    )

    return customers


def create_numeric_cols_df(df: pd.DataFrame) -> pd.DataFrame:
    # Isolate numeric columns from dataframe
    numeric_cols = (df.select_dtypes(include=["float64", "int64"])).columns
    return numeric_cols
