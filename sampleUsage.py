from dstore import Collection

# connect to the database
databaseInstance = Collection().connect('./learn/details.dst')

# meta information
print(databaseInstance.meta)

print(databaseInstance.definitions)


# data
dataToSave = {
    'age': 67,
    'name': 'Peter'
}

# b700798d-9529-482b-9ecc-e5f363c58eb8
recordId = databaseInstance.save("Student", dataToSave)

# print(recordId)

# fetch
# data = databaseInstance.fetch("Employee", ['name', 'id'])

# print(data)

# update
# databaseInstance.update("Employee", ['name'], ['Peter'], ('name', 'Grace'))

# print('Finished')

# delete : all data in table
# databaseInstance.drop("Student")

# data record based onc conditions
# databaseInstance.delete("Employee", [('id', 67)])

# delete the actual table
# databaseInstance.drop("Student")

print('Done')