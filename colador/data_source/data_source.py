from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def get_messages(self):

        raise NotImplementedError
