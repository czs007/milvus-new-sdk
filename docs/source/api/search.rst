.. _search:

Search
=========
.. currentmodule:: arctern

Search inherits pandas Series. It is a Series to store and process geometric data, and internally stores geometries as bytes objects.

Constructor 
-----------
.. autosummary::
   :toctree: api/
   :template: autosummaryclass.rst

   Search


Attributes
----------
.. autosummary::
   :toctree: api/

   Search.is_valid
   Search.is_simple
   Search.is_empty
   Search.length
   Search.area
   Search.geom_type
   Search.centroid
   Search.convex_hull
   Search.npoints
   Search.envelope
   Search.boundary

.. TODO: should we use this title?

Constructing Geometry
---------------------
.. autosummary::
   :toctree: api/

    Search.point
    Search.polygon_from_envelope
    Search.geom_from_geojson
    Search.from_geopandas
    Search.from_file
    Search.as_geojson
    Search.to_wkt
    Search.to_wkb
    Search.to_geopandas
    Search.to_json
    Search.to_file

Processing Geometry
-------------------
.. autosummary::
   :toctree: api/

   Search.buffer
   Search.precision_reduce
   Search.intersection
   Search.union
   Search.make_valid
   Search.simplify
   Search.set_crs
   Search.crs
   Search.to_crs
   Search.curve_to_line
   Search.exterior
   Search.difference
   Search.symmetric_difference
   Search.scale
   Search.affine_transform
   Search.translate
   Search.rotate

Spatial Relationship
--------------------
.. autosummary::
   :toctree: api/

   Search.geom_equals
   Search.touches
   Search.overlaps
   Search.crosses
   Search.contains
   Search.intersects
   Search.within
   Search.disjoint

Measurement
-----------
.. autosummary::
   :toctree: api/

   Search.distance_sphere
   Search.distance
   Search.hausdorff_distance

Aggregation
-----------
.. autosummary::
   :toctree: api/

   Search.unary_union
   Search.envelope_aggr

Pandas Methods
--------------
.. TODO: add describe here
.. autosummary::
   :toctree: api/

   Search.isna
   Search.notna
   Search.fillna
   Search.equals
