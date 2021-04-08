#### pymilvus.Collection

---



##### Accessing and constructing collection

| Constructor                             | Descriptions                                                 |
| --------------------------------------- | :----------------------------------------------------------- |
| Collection(name, schema=None, **kwargs) | Return the collection corresponding to name. Create a new one if not existed. |



##### Manipulating and querying collection meta

| Properties              | Descriptions                           |
| ----------------------- | -------------------------------------- |
| Collection.schema       | Return the collection schema           |
| Collection.description  | Return the description text            |
| Collection.name         | Return the collection name             |
| Collection.is_empty     | Return whether the collection is empty |
| Collection.num_entities | Return the number of entities          |



##### Manipulating, loading, and querying collection

| Methods                                                      | Descriptions                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| pymilvus.Collection.drop()                                   | Drop the collection, as well as its indexes.                 |
| pymilvus.Collection.load(field_names=None, index_names=None, partition_names=None, **kwargs) | Load the collection from disk to memory.                     |
| pymilvus.Collection.release()                                | Release the collection from memory.                          |
| pymilvus.Collection.insert(data, **kwargs)                   | Insert data into the collection, or into one of its partitions. |
| pymilvus.Collection.search(data, limit, params, expr=None, partition_names=None, fields=None, **kwargs) | Vector similarity search with an optional boolean expression as filters. |



##### Accessing and constructing partition

| Methods                                       | Descriptions                                                 |
| --------------------------------------------- | ------------------------------------------------------------ |
| pymilvus.Collection.partitions                | Return all partitions of the collection.                     |
| pymilvus.Collection.partition(partition_name) | Return the partition corresponding to name. Create a new one if not existed. |



##### Accessing and constructing index

| Methods                               | Descriptions                                                 |
| ------------------------------------- | ------------------------------------------------------------ |
| pymilvus.Collection.indexes           | Return all indexes of the collection.                        |
| pymilvus.Collection.index(index_name) | Return the index corresponding to name. Create a new one if not existed. |

