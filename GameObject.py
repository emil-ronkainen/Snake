from abc import abstractmethod, ABC

class GameObject(ABC):
  # docstring

    def __init__(self):
        pass


    @abstractmethod
    def update(self, snake):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
