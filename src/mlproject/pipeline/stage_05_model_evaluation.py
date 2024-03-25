
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_transformation import DataTransformation
from mlproject.components.model_trainer import ModelTrainer
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        #model_evaluation_config.log_into_mlflow()
        model_evaluation_config.save_results()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = ModelEvaluationTrainPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e