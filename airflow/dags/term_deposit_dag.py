
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
from src.mlproject.pipeline.stage_04_model_training import ModelTrainingTrainPipeline
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainPipeline
from src.mlproject import logger

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_project_workflow',
    default_args=default_args,
    description='Machine Learning Project Workflow',
    schedule_interval=timedelta(days=1),  # Set the schedule interval as needed
)

def run_ml_stage(stage_name, pipeline_class):
    try:
        logger.info(f"Stage {stage_name} Started")
        obj = pipeline_class()
        obj.main()
        logger.info(f"Stage {stage_name} Completed")
    except Exception as e:
        logger.exception(e)
        raise e

# Define tasks in the DAG
data_ingestion_task = PythonOperator(
    task_id='data_ingestion',
    python_callable=run_ml_stage,
    op_args=['Data Ingestion Stage', DataIngestionTrainPipeline],
    dag=dag,
)

data_validation_task = PythonOperator(
    task_id='data_validation',
    python_callable=run_ml_stage,
    op_args=['Data Validation Stage', DataValidationTrainPipeline],
    dag=dag,
)

data_transformation_task = PythonOperator(
    task_id='data_transformation',
    python_callable=run_ml_stage,
    op_args=['Data Transformation Stage', DataTransformationTrainPipeline],
    dag=dag,
)

model_training_task = PythonOperator(
    task_id='model_training',
    python_callable=run_ml_stage,
    op_args=['Model Training Stage', ModelTrainingTrainPipeline],
    dag=dag,
)

model_evaluation_task = PythonOperator(
    task_id='model_evaluation',
    python_callable=run_ml_stage,
    op_args=['Model Evaluation Stage', ModelEvaluationTrainPipeline],
    dag=dag,
)

# Set task dependencies
data_ingestion_task >> data_validation_task >> data_transformation_task >> model_training_task >> model_evaluation_task
