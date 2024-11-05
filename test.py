# import re

# from dstProcessor import DstUtils

# path = './details.dst'



# with open(path, "r") as dataHandle:
#     readData = dataHandle.readlines()

#     # 'Student:[name=str, age=int]', 'Employee:[id=int, name=str]'
#     withoutNewLines = [eachLine.strip() for eachLine in readData]

#     # ClassName:[str=[str, int, float]]


# for eachExtractedLine in withoutNewLines:
#     # get the data in the line
#     foundDefinitions = DstUtils().processDstLine(eachExtractedLine)

#     if not foundDefinitions is None:
#         print(foundDefinitions)

#     else:
#         print('No data was found for ')




