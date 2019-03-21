import numpy as np
import pymongo
from pymongo import MongoClient

from colador.data_source.data_source import DataSource


class MongoDbSource(DataSource):

    def __init__(self, host='127.0.0.1', port=27017, db_name='db_name'):

        client = MongoClient(host, port)
        self.db = client[db_name]

        self.messages = None
        self.messages_updated = False
        self.messages_cursor = None
        self.vector_fields = []

    def set_messages_query(
            self, query, fields_to_fetch, sort_fields, limit=None
    ):
        self.messages_updated = False
        self.messages_cursor = self.db.message.find(
            query,
            {f: 1 for f in fields_to_fetch}
        ).sort(
            [(f, pymongo.ASCENDING) for f in sort_fields]
        )

        if limit is not None:
            self.messages_cursor = self.messages_cursor.limit(limit)

    def set_vector_fields(self, fields):

        self.vector_fields = fields
        self.messages_updated = False

    def vectors_to_numpy(self, message):

        for field in self.vector_fields:
            message[field] = np.array(message[field])
        return message

    def refresh_messages(self):

        self.messages = list(
            self.vectors_to_numpy(m)
            for m in self.messages_cursor
        )
        self.messages_updated = True

    def get_messages(self):

        if not self.messages_updated:
            self.refresh_messages()

        return self.messages
