| Methods                                                      | Descriptions               |
| ------------------------------------------------------------ | -------------------------- |
| Search(collection, data, limit, params, expr=None, partition_names=None, fields=None, **kwargs) | Construct a Search object. |
| Search.execute()                                             | Return the search result.  |


| Methods                     | Descriptions                                                 |
| --------------------------- | ------------------------------------------------------------ |
| SearchResult(grpc_response) | Construct a Search Result from response.                     |
| SearchResult.__iter__()     | Iterate the Search Result. Every iteration returns a `Hits` coresponding to a query. |
| SearchResult[n]             | Return the `Hits` coresponding to the nth query.             |
| SearchResult.__len__()      | Return the number of query of Search Result.                 |


| Methods          | Descriptions                                                 |
| ---------------- | ------------------------------------------------------------ |
| Hits(raw_data)   | Construct a Hits object from response.                       |
| Hits.__iter__()  | Iterate the `Hits` object. Every iteration returns a `Hit` which represent a record coresponding to the query. |
| Hits[k]          | Return the kth `Hit` coresponding to the query.              |
| Hits.__len__()   | Return the number of hit record.                             |
| Hits.ids()       | Return the ids of all hit record.                            |
| Hits.distances() | Return the distances of all hit record.                      |


| Methods        | Descriptions                                                 |
| -------------- | ------------------------------------------------------------ |
| Hit(raw_data)  | Construct a Hit object from response. A hit represent a record coresponding to the query. |
| Hit.id()       | Return the id of the hit record.                             |
| Hit.distance() | Return the distance between the hit record and the query.    |
| Hit.score()    | Return the calculated score of the hit record, now the score is equal to distance. |



