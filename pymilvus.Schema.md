| Properties              | Descriptions                           |
| ----------------------- | -------------------------------------- |
| Schema(fields=None, **kwargs) | Construct a schema object. Fields is a list, every item in fields is a field which must contain name, type, and if the field is a vector field, it can contain index parameters. |
| Schema.add_field(field) | Add a field to schema, the field is a dict which must contain name, type, and if the field is a vector field, it can contain index parameters. |
| Schema.fields() | Return all fields.  |


| DataType Enum  |
| ----------------------- |
| DataType.BOOL |
| DataType.INT8 |
| DataType.INT16 |
| DataType.INT32 |
| DataType.INT64 |
| DataType.FLOAT |
| DataType.DOUBLE |
| DataType.BINARY_VECTOR |
| DataType.FLOAT_VECTOR |


fields example:

```python
fields = [
    {"field": "A", "type": DataType.INT32}
    {"field": "B", "type": DataType.INT64},
    {"field": "C", "type": DataType.FLOAT},
    {"field": "Vec", "type": DataType.FLOAT_VECTOR, "params": {"dim": 128}}]

schema = Schema(fields)

assert len(schema.fields()) == len(fields)
```
