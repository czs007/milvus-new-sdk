#### pymilvus.Index

---

##### Accessing and constructing Index

| Methods                                     | Descriptions                                                 |
| ------------------------------------------- | ------------------------------------------------------------ |
| Index(collection, field_name, index_params) | Create index on a specified column according to the index parameters. |
| Index.name                                  | Return the index name.                                       |
| Index.params                                | Return the index params.                                     |
| Index.collection_name                       | Return corresponding collection name.                        |
| Index.field_name                            | Return corresponding column name.                            |
|                                             |                                                              |

##### Manipulating

| Methods      | Descriptions                                  |
| ------------ | --------------------------------------------- |
| Index.drop() | Drop index and its corresponding index files. |
