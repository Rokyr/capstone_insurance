import pandas as pd
from src.extract.extract_all import extract_all
from src.utils.logging_utils import setup_logger
import logging

logger = setup_logger(__name__, "extract.log", level=logging.DEBUG)


def extract_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        logger.info("Starting data extraction process")

        customers = extract_all()

        logger.info(
            f"Data extraction completed successfully - "
            f"Customers:{customers.shape}"
        )
        return customers
    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")
        raise
