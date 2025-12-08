import pandas as pd
from typing import Optional
from src.load.load_correlation import (
    load_correlation,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__, "load_data.log")


def load_data(transformed_data: Optional[pd.DataFrame]) -> None:
    """
    Load transformed data into the target database.

    Args:
        transformed_data (pd.DataFrame): The cleaned and transformed
        data to load.

    Raises:
        QueryExecutionError: If database operations fail.
    """
    try:
        logger.info("Starting data load process")

        if transformed_data is None or transformed_data.empty:
            logger.warning("No data provided to load.")
        else:
            logger.info(
                f"transformed data to be loaded shape:{transformed_data.shape}"
            )

        # correlation table load
        load_correlation(transformed_data)

        logger.info(
            f"Data load completed successfully - "
            f"Rows loaded: {len(transformed_data)}"
        )

    except Exception as e:
        logger.error(f"Data load failed: {str(e)}")
        raise
