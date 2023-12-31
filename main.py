from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started !!!! <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.start()
    logger.info(f">>>> Stage {STAGE_NAME} Completed !!!! <<<<\n\n X=======================X")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started !!!! <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.start()
    logger.info(f">>>> Stage {STAGE_NAME} Completed !!!! <<<<\n\n X=======================X")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started !!!! <<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.start()
    logger.info(f">>>> Stage {STAGE_NAME} Completed !!!! <<<<\n\n X=======================X")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started !!!! <<<<")
    model_training = ModelTrainingPipeline()
    model_training.start()
    logger.info(f">>>> Stage {STAGE_NAME} Completed !!!! <<<<\n\n X=======================X")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started !!!! <<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.start()
    logger.info(f">>>> Stage {STAGE_NAME} Completed !!!! <<<<\n\n X=======================X")

except Exception as e:
    logger.exception(e)
    raise e