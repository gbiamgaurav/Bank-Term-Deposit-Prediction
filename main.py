
from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataValidationTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataTransformationTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

