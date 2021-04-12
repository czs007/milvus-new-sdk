.. _Connections:

Connections
=========
.. currentmodule:: arctern

Connections inherits pandas DataFrame. It is a DataFrame to store and process geometric data.

Constructor
-----------
.. autosummary::
   :toctree: api/
   :template: autosummaryclass.rst

   Connections

Connections Functions
---------------------
.. autosummary::
   :toctree: api/

    Connections.to_geopandas
    Connections.from_geopandas
    Connections.to_json
    Connections.from_file
    Connections.to_file
    Connections.crs
    Connections.set_geometry
    Connections.dissolve
    Connections.merge
