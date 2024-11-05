# dstore

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Mutiibwa Grace Peter, Tukasiima Blessing (c) 2024

## Examples of How To Use store

Creating a `definitions` file

The **definitions file** should have an extension of `.dst`

```markdown

# In your file say 'definitions.dst'

Student: [name=str, age=int]

Color: [name=str, code=str]

```

Creating a connection to the `database` via the `definitions` file
```python

from dstore import SqliteORM


# path to definitions
definition_path = './learn/details.dst'

# connect to the definitions file
datase_connection = SqliteORM().connect(definition_path)
```

Get meta information about the database created using the `meta` and `definitions` attribute
```python

print(datase_connection.meta)

print(datase_connection.definitions)
```

