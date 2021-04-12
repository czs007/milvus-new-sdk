from . import connections
from .collection import Collection
from .partition import Partition
from .index import Index

class Utility(object):
    _using = "default"

    @classmethod
    def reset_connection(cls, using):
        cls._using = using

    @classmethod
    def _get_connection(cls):
        return connections.get_connection(cls._using)

    @classmethod
    def loading_progress(cls, collection_name, partition_name=None):
        pass

    @classmethod
    def wait_for_loading_complete(cls, collection_name, partition_name=None):
        pass

    @classmethod
    def index_building_progress(cls, collection_name, index_name=None):
        pass

    @classmethod
    def wait_for_index_building_complete(cls, collection_name, index_name=None):
        pass

    @classmethod
    def has_collection(cls, collection_name):
        pass

    @classmethod
    def has_partition(cls, collecton_name, partition_name):
        pass
