#DataFetcher
class DataFetcher:
    def __init__(self, directory, data_name, labels_name):
        self.directory = directory
        self. data_name = data_name 
        self.labels_name = labels_name 
    
    @property
    def directory(self):
        return self._directory
    
    @directory.setter
    def directory(self, string):
        if type(string) != str:
            raise ValueError("Invalid Input: Input must ne string!")
        else:
            self._directory = string

    @property
    def data_name(self):
        return self._data_name
    
    @data_name.setter
    def directory(self, string):
        if type(string) != str:
            raise ValueError("Invalid Input: Input must ne string!")
        else:
            self._data_name = string

    
    @property
    def labels_name(self):
        return self._labels_name
    
    @labels_name.setter
    def directory(self, string):
        if type(string) != str:
            raise ValueError("Invalid Input: Input must ne string!")
        else:
            self._labels_name = string
            
    #get directory
    def _get_train_data_path(self, traing_data_name, subset_number):
        return "./{self._directory}/train{traing_data_name}" + str(subset_number)
    
    def _get_train_labels_path(self, traing_labels_name, subset_number):
        return "./{self._directory}/train{traing_labels_name}" + str(subset_number)
    