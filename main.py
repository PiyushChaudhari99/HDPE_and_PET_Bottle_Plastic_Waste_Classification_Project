from src.cnnImageClassifier import logger
from src.cnnImageClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnImageClassifier.pipeline.stage_02_prepare_base_model   import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'DATA_INGESTION_STAGE'


try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'PREPARE_BASE_MODEL'


try:
    logger.info(f"************************")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e