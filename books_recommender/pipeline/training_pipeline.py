from books_recommender.components.stage_00_data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_trainer.initiate_model_trainer() 