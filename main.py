from src.cnnImageClassifier import logger
from src.cnnImageClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'DATA_INGESTION_STAGE'


try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e