import numpy as np

from sklearn.cluster import KMeans


class MessagesGroup(object):

    def __init__(self, colador, messages):

        self.colador = colador
        self.messages = messages

    def cluster_kmeans(
            self, feature_field: str, num_clusters: int
    ):
        features = np.array([m[feature_field] for m in self.messages])
        kmeans = KMeans(
            n_clusters=num_clusters, random_state=0, n_jobs=-1
        ).fit(features)

        clusters = [[] for i in range(0, num_clusters)]
        for message, cluster in zip(
                (m for m in self.messages), kmeans.predict(features)
        ):
            clusters[cluster].append(message)

        clusters.sort(key=lambda c: len(c))

        from colador.clusters_group import ClustersGroup
        return ClustersGroup([
            MessagesGroup(self.colador, cluster) for cluster in clusters
        ])

    def word_cloud(self, text_field='text', top_n=40):

        from word_cloud.word_cloud_generator import WordCloud
        wc = WordCloud(stopwords=self.colador.STOP_WORDS_ES)
        texts = [m[text_field] for m in self.messages]
        try:
            embed_code = wc.get_embed_code(
                text=texts, random_color=True, topn=top_n
            )
        except ValueError as e:
            embed_code = str(e)

        from IPython.core.display import HTML
        return HTML(embed_code)

    def merge_with(self, another_group: 'MessagesGroup'):

        return MessagesGroup(
            self.colador, self.messages + another_group.messages
        )

    def update_field(self, field: str, value_func):

        for m in self.messages:
            self.colador.update_message(m, field, value_func(m))

    def __add__(self, another_group: 'MessagesGroup'):
        return self.merge_with(another_group)

    def __iter__(self):
        return iter(self.messages)

    def __len__(self):
        return len(self.messages)

    def __getitem__(self, item):
        return self.messages[item]
