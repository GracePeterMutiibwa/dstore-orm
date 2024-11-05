from DStore import Collection

# connect to the database
databaseInstance = Collection().connect('./store/details.dst')

# print(databaseInstance.meta)

# data
# dataToSave = {
#     'age': 67,
#     'name': 'Sample'
# }

# 5ec3c47e-85e9-4cd3-b531-083c18bda522
# recordId = databaseInstance.save("Student", dataToSave)

# print(recordId)

# fetch
# data = databaseInstance.fetch("Employee", ['name', 'id'])

# print(data)

# update
# databaseInstance.update("Student", ['age'], [22], ('name', 'Bless'))

# print('Finished')

# delete : all data in table
# databaseInstance.drop("Student")

# data record based onc conditions
# databaseInstance.delete("Employee", [('id', 67)])

# delete the actual table
# databaseInstance.drop("Student")

print('Done')