#### pymilvus.Collection

---



##### Accessing and constructing collection

| Methods                                          | Descriptions                                                 |
| ------------------------------------------------ | :----------------------------------------------------------- |
| pymilvus.Collection(name, schema=None, **kwargs) | Return the collection corresponding to name. Create a new one if not existed. |



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
| Collection.drop()                                            | Drop the collection, as well as its indexes.                 |
| Collection.load(field_names=None, index_names=None, partition_names=None, **kwargs) | Load the collection from disk to memory.                     |
| Collection.release()                                         | Release the collection from memory.                          |
| Collection.insert(data, **kwargs)                            | Insert data into the collection, or into one of its partitions. |
| Collection.search(data, limit, params, expr=None, partition_names=None, fields=None, **kwargs) | Vector similarity search with an optional boolean expression as filters. |



##### Accessing and constructing partition

| Methods                                  | Descriptions                                                 |
| ---------------------------------------- | ------------------------------------------------------------ |
| Collection.partitions                    | Return all partitions of the collection.                     |
| Collection.partition(partition_name)     | Return the partition corresponding to name. Create a new one if not existed. |
| Collection.has_partition(partition_name) | Checks if a specified partition exists.                      |



##### Accessing and constructing index

| Methods                          | Descriptions                                                 |
| -------------------------------- | ------------------------------------------------------------ |
| Collection.indexes               | Return all indexes of the collection.                        |
| Collection.index(index_name)     | Return the index corresponding to name. Create a new one if not existed. |
| Collection.has_index(index_name) | Checks if a specified Index exists.                          |

