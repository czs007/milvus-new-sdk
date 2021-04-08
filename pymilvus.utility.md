#### pymilvus.utility

---



##### Checking job states

| Methods                                                      | Descriptions                                 |
| ------------------------------------------------------------ | -------------------------------------------- |
| pymilvus.utility.loading_progress(collection_name, partition_name=None) | Show # loaded entities vs. # total entities  |
| pymilvus.utility.wait_for_loading_complete(collection_name, partition_name=None) | Block until loading is done.                 |
| pymilvus.utility.index_building_progress(collection_name, index_name=None) | Show # indexed entities vs. # total entities |
| pymilvus.utility.wait_for_index_building_complete(collection_name, index_name=None) | Block until building is done.                |

