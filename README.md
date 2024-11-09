# How to start using `dstore`

Ready for use , with minimal features like all CRUD operations are supported

Developed by `Mutiibwa Grace Peter`, `Tukasiima Blessing` (c) 2024

## Examples of How To Use dstore

1. Creating a `definitions` file

The **definitions file** should have an extension of `.dst`

```markdown
# Inside the the .dst file  you can add definitions like;

Student:[name=str]
```

- Above , `Student` is the name of the table and the list `[name=str]` is a definition of the fields the `Student` table will have


```markdown

# With many tables and many fields

Student: [name=str, age=int]

Color: [name=str, code=str]

```

Suppose the `details.dst` is located in a folder called `learn`

> Note: If the `dst` file is  put in a folder, that folder should exist. 

---


2. Creating a connection to the `database` in our python file or code via the `definitions` file.

```python

from dstore import SqliteORM


# path to definitions
definition_path = './learn/details.dst'

# connect to the definitions file
datase_connection = SqliteORM().connect(definition_path)
```

Get meta information about the database created using the `meta` and `definitions` attribute
```python

# display a list of tables as defined in the database
print(datase_connection.meta)

# display the structure of the databse tables
print(datase_connection.definitions)
```

