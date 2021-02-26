from datetime import datetime
import random
class Config:

    """
                  This class is used for configuration instance attribute!!.

                  Written By: Mustafa Khan
                  Version: 1.0
                  Revisions: None

                  """

    def __init__(self):
        self.training_data_path = 'data/training_data'
        self.training_database = 'training'
        self.prediction_data_path = 'data/prediction_data'
        self.prediction_database = 'prediction'

    def get_run_id(self):
        """
                      This method is used to give unique run_id and helps to logfile!!.

                      Written By: Mustafa Khan
                      Version: 1.0
                      Revisions: None

                      """

        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H%M%S")
        return str(self.date) + "_" + str(self.current_time) + "_" + str(random.randint(100000000, 999999999))