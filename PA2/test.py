


#Libraries used
import os 
import fileinput




import sys 

data2 = []
data = []

# for lines in sys.stdin:
#     if lines.startswith('-'):
#         pass
#     else:
#         print(lines)

stringofdata = ' '.join(line.rstrip() for line in sys.stdin if not line.startswith('-'))

#print(stringofdata)

data2 = stringofdata.split(';')

for i in range(len(data2)):
    data.append(data2[i].upper())

for i in range(len(data)):
    commandWords = data[i].split('(', 1)
    print(commandWords)
    #check if there are attributes for a table
    if len(commandWords) > 1:
        #determine command vs table info if applicable
        commandInfo = commandWords[0].strip(';')
        tableInfo = commandWords[1]
        print(tableInfo)
    else:
        commandInfo = commandWords[0].strip(';')

    #split commandInfo into specific command words
    individualCommandWords = commandInfo.split()
    print(individualCommandWords)


# # for line in sys.stdin:
# #     if not line.startswith('-'):
# #         if line.rstrip().endswith(';'):
# #             print(line.rstrip())
# #             data.append(line.rstrip())



# # #Uses stdin and stores into global List
# lines_of_data = fileinput.input()

# #Lists created for string parsing

# commandWords = []
# tableInfo = []
# userInput = []

# print(lines_of_data)
# print('\n\n')


# for line in lines_of_data:
#     if not line.rstrip().startswith('-'):

        # while not ';' in line:
        #     print(line)
        #     userInput.append(line)


# #Loops through number of command lines
# for i in range(len(userInput)):
#     #check that command line is not blank
#     if not userInput[i] == '' :
#         #split info into commandWords
#         commandWords = userInput[i].split('(', 1)
#         print(commandWords)
#         #check if there are attributes for a table
#         if len(commandWords) > 1:
#             #determine command vs table info if applicable
#             commandInfo = commandWords[0].strip(';')
#             tableInfo = commandWords[1]
#         else:
#             commandInfo = commandWords[0].strip(';')

#         #split commandInfo into specific command words
#         individualCommandWords = commandInfo.split()
