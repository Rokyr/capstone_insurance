import os
import sys
from config.env_config import setup_env
from src.extract.extract import extract_data
from src.utils.logging_utils import setup_logger
from src.transform.transform import transform_data
from src.load.load import load_data


def main():
    # Get the argument from the run_etl command and set up the environment
    setup_env(sys.argv)
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")

    try:

        logger.info("Starting ETL pipeline")

        # Extract phase
        print(f'{"="*200}')
        logger.info(f'{"="*20} Beginning data extraction phase {"="*20}')
        print(f'{"="*200}')
        extracted_data = extract_data()

        logger.info("Data extraction phase completed")

        # Transform phase
        print(f'{"="*200}')
        logger.info(f'{"="*20} Beginning data transformation phase {"="*20}')
        print(f'{"="*200}')
        transformed_data = transform_data(extracted_data)
        logger.info(
            f"Data transformation phase completed. "
            f"transformed_data: type = {type(transformed_data)}"
        )

        cleaned_customers, correlation_table = transformed_data

        # Load phase
        print(f'{"="*200}')
        logger.info(f'{"="*20} Beginning loading phase {"="*20}')
        print(f'{"="*200}')

        load_data(correlation_table)
        logger.info("Data load phase completed")
        print("*" * 200)
        print(
            f'{"*"*74} ETL pipeline run successfully in '
            f'{os.getenv("ENV", "error")} environment! {"*"*74}'
        )
        print("*" * 200)
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
