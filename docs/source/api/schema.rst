.. _Schema:

Schema
=========
.. currentmodule:: arctern

Schema inherits pandas DataFrame. It is a DataFrame to store and process geometric data.

Constructor
-----------
.. autosummary::
   :toctree: api/
   :template: autosummaryclass.rst

   Schema

Schema Functions
---------------------
.. autosummary::
   :toctree: api/

    Schema.to_geopandas
    Schema.from_geopandas
    Schema.to_json
    Schema.from_file
    Schema.to_file
    Schema.crs
    Schema.set_geometry
    Schema.dissolve
    Schema.merge
