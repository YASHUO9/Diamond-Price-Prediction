from src.DimondPricePrediction.pipelines.training_pipeline import TrainingPipeline


object = TrainingPipeline()

train,test = object.start_data_ingestion()

train , test = object.start_data_transformation(train,test)
object.start_trainig()  
object.start_model_training() 

# Compare this snippet from src/DimondPricePrediction/components/data_ingestion.py:
