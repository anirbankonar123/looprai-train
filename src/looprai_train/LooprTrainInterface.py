from abc import abstractmethod
import mlflow

class LooprTrainInterface():

    @abstractmethod
    def convert_input(self,train_input_path:str, test_input_path:str): pass

    def get_dataset(self, project_id:str, dataset_id:str, output_path:str):
        return "For test"

    def setMlfowTracking(self, expt_name:str, mlflow_tracking_uri:str):
        mlflow.set_tracking_uri(mlflow_tracking_uri)
        mlflow.set_experiment(expt_name)

    @abstractmethod
    def train(self): pass

