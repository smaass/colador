from colador.data_source.data_source import DataSource


class Colador(object):

    def __init__(self, data_source: DataSource):

        self.data_source = data_source
