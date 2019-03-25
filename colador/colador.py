import json
import os

from colador.data_source.data_source import DataSource
from colador.messages_group import MessagesGroup

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)


class Colador(object):

    STOP_WORDS_ES = frozenset(json.load(
        open(os.path.join(__location__, 'stopwords-es.json'))
    ))

    def __init__(self, data_source: DataSource):

        self.data_source = data_source

    def get_messages(self):

        return MessagesGroup(self, self.data_source.get_messages())

    def update_message(self, message, field, value):

        self.data_source.update_message(message, field, value)
