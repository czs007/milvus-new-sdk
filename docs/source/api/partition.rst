.. _partition:

Partition
=========
.. currentmodule:: arctern

Partition inherits pandas Series. It is a Series to store and process geometric data, and internally stores geometries as bytes objects.

Constructor 
-----------
.. autosummary::
   :toctree: api/
   :template: autosummaryclass.rst

   Partition


Attributes
----------
.. autosummary::
   :toctree: api/

   Partition.is_valid
   Partition.is_simple
   Partition.is_empty
   Partition.length
   Partition.area
   Partition.geom_type
   Partition.centroid
   Partition.convex_hull
   Partition.npoints
   Partition.envelope
   Partition.boundary

.. TODO: should we use this title?

Constructing Geometry
---------------------
.. autosummary::
   :toctree: api/

    Partition.point
    Partition.polygon_from_envelope
    Partition.geom_from_geojson
    Partition.from_geopandas
    Partition.from_file
    Partition.as_geojson
    Partition.to_wkt
    Partition.to_wkb
    Partition.to_geopandas
    Partition.to_json
    Partition.to_file

Processing Geometry
-------------------
.. autosummary::
   :toctree: api/

   Partition.buffer
   Partition.precision_reduce
   Partition.intersection
   Partition.union
   Partition.make_valid
   Partition.simplify
   Partition.set_crs
   Partition.crs
   Partition.to_crs
   Partition.curve_to_line
   Partition.exterior
   Partition.difference
   Partition.symmetric_difference
   Partition.scale
   Partition.affine_transform
   Partition.translate
   Partition.rotate

Spatial Relationship
--------------------
.. autosummary::
   :toctree: api/

   Partition.geom_equals
   Partition.touches
   Partition.overlaps
   Partition.crosses
   Partition.contains
   Partition.intersects
   Partition.within
   Partition.disjoint

Measurement
-----------
.. autosummary::
   :toctree: api/

   Partition.distance_sphere
   Partition.distance
   Partition.hausdorff_distance

Aggregation
-----------
.. autosummary::
   :toctree: api/

   Partition.unary_union
   Partition.envelope_aggr

Pandas Methods
--------------
.. TODO: add describe here
.. autosummary::
   :toctree: api/

   Partition.isna
   Partition.notna
   Partition.fillna
   Partition.equals
