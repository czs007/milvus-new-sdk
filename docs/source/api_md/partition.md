#### pymilvus.Partition

---

##### Manipulating and querying partition meta

| Methods                         | Descriptions                           |
| ------------------------------- | -------------------------------------- |
| pymilvus.Partition.description  | Return the description text.           |
| pymilvus.Partition.name         | Return the partition name.             |
| pymilvus.Partition.is_empty     | Return whether the partition is empty. |
| pymilvus.Partition.num_entities | Return the number of entities.         |

##### Manipulating, loading, and querying partition

| Methods                                                      | Descriptions                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| pymilvus.Partition.drop()                                    | Drop the partition, as well as its corresponding index files. |
| pymilvus.Partition.load(field_names=None, index_names=None, **kwargs) | Load the partition from disk to memory.                      |
| pymilvus.Partition.release()                                 | Release the partition from memory.                           |
| pymilvus.Partition.insert(data, **kwargs)                    | Insert data into partition.                                  |
| pymilvus.Partition.search(data, limit, params, expr=None, fields=None, **kwargs) | Vector similarity search with an optional boolean expression as filters. |


