.. _collection:

Collection
=========
.. currentmodule:: milvus_orm

Collection inherits pandas DataFrame. It is a DataFrame to store and process geometric data.

Constructor
-----------
.. autosummary::
   :toctree: api/
   :template: autosummaryclass.rst

   Collection

Collection Functions
---------------------
.. autosummary::
   :toctree: api/

    Collection.to_geopandas
    Collection.from_geopandas
    Collection.to_json
    Collection.from_file
    Collection.to_file
    Collection.crs
    Collection.set_geometry
    Collection.dissolve
    Collection.merge
