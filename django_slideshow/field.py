from elasticsearch_dsl import field


class ElasticsearchImageField(field.Integer):
    def to_es(self, data):
        return data.id
