from dataclasses import dataclass

@dataclass
class DataIngestionArtifact: 
    feature_store_file:str
    train_file_dir:str
    test_file_dir:str

class DataValidationArtifact: ...
class DataTransformationArtifact: ...
class ModelTrainerArtifact: ...
class ModelEvaluationArtifact: ...
class ModelPusherArtifact: ...

