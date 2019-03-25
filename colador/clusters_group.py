from functools import reduce
from typing import List

from colador.messages_group import MessagesGroup


class ClustersGroup(object):

    def __init__(self, clusters: List[MessagesGroup]):

        self.clusters = clusters

    def word_clouds(self):

        clouds_html = [
            '<h3>Cluster %s</h3><br>%s' % (i, c.word_cloud().__html__())
            for i, c in enumerate(self.clusters)
        ]

        from IPython.core.display import HTML
        return HTML(reduce(str.__add__, clouds_html, ''))

    def merge_with(self, another_group: 'ClustersGroup'):
        return ClustersGroup(self.clusters + another_group.clusters)

    def __add__(self, another_group: 'ClustersGroup'):
        return self.merge_with(another_group)

    def __iter__(self):
        return iter(self.clusters)

    def __len__(self):
        return len(self.clusters)

    def __getitem__(self, item):
        return self.clusters[item]
