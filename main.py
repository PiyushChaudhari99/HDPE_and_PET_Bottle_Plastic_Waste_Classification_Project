from src.cnnImageClassifier import logger
from src.cnnImageClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnImageClassifier.pipeline.stage_02_prepare_base_model   import PrepareBaseModelTrainingPipeline
from src.cnnImageClassifier.pipeline.stage_03_model_training   import ModelTrainingPipeline

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




STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e