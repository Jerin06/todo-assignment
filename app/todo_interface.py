from abc import ABC, abstractmethod

class ITodo(ABC):
    @abstractmethod
    def add_task(self, id, task, is_done):
        pass
    
    @abstractmethod
    def get_task_by_id(self, id):
        pass
    
    @abstractmethod
    def update_task_status(self, id):
        pass
    
    @abstractmethod
    def delete_task(self, id):
        pass
    