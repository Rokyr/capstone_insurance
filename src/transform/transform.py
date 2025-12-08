import pandas as pd
from src.transform.transform_all import clean_customers
from src.utils.logging_utils import setup_logger
from src.transform.transform_all import produce_correlation_table

logger = setup_logger("transform_data", "transform_data.log")


def transform_data(data) -> pd.DataFrame:
    try:
        logger.info("Starting data transformation process...")
        # Enrich and clean customer data
        logger.info("Clean and enrich customer data...")
        cleaned_customers = clean_customers(data)
        logger.info("Customer data cleaned and enriched successfully.")

        # Produce a correlation table
        logger.info("Producing correlation table...")
        correlation_table = produce_correlation_table(cleaned_customers)

        return cleaned_customers, correlation_table

    except Exception as e:
        logger.error(f"Data transformation failed: {str(e)}")
        raise
