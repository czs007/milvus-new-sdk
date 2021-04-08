#### pymilvus.utility

---



##### Checking job states

| Methods                                                      |                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| utility.loading_progress(collection_name, partition_name=None) | Show # loaded entities vs. # total entities             |
| utility.wait_for_loading_complete(collection_name, partition_name=None) | Block until loading is done.                            |
| utility.index_building_progress(collection_name, index_name=None) | Show # indexed entities vs. # total entities            |
| utility.wait_for_index_building_complete(collection_name, index_name=None) | Block until building is done.                           |
| utility.has_collection(collection_name)                      | Checks whether a specified collection exists.           |
| utility.has_partition(collecton_name, partition_name)        | Checks if a specified partition exists in a collection. |

