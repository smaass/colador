from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def get_messages(self):

        raise NotImplementedError

    @abstractmethod
    def update_message(self, message, field, value):

        raise NotImplementedError
