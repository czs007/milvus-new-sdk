| Methods                                        | Descriptions                     | 参数                    | 返回值                |
| ---------------------------------------------- | :------------------------------- | ----------------------- | --------------------- |
| Connections.configure(**kwargs)                | Configure connections.           | copy from ElasticSearch | None或Raise Exception |
| Connections.add_connection(alias, conn)        | Add a connection using alias.    |                         |                       |
| Connections.remove_connection(alias)           | Remove a connection by alias.    |                         |                       |
| Connections.create_connection(alias, **kwargs) | Create a connection named alias. |                         |                       |
| Connections.get_connection(alias)              | Get a connection by alias.       |                         |                       |
