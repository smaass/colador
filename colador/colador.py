import inspect
import json
import os

from data_source.data_source import DataSource
from messages_group import MessagesGroup
import stop_words


class Colador(object):

    STOP_WORDS_PATH = os.path.dirname(inspect.getfile(stop_words))
    STOP_WORDS_ES = frozenset(json.load(
        open(os.path.join(STOP_WORDS_PATH, 'stopwords-es.json'))
    ))

    def __init__(self, data_source: DataSource):

        self.data_source = data_source

    def get_messages(self):

        return MessagesGroup(self, self.data_source.get_messages())

    def update_message(self, message, field, value):

        self.data_source.update_message(message, field, value)
