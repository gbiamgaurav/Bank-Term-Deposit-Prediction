
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.get_data_transformation()
        data_transformation.save_preprocessor()
        data_transformation.train_test_split()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = DataTransformationTrainPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e