#Project 2: Basic Data Manipulation
#Author: Mackenzie Zappe
#Class: CS457.1001
#Date: 10/8/2021
##Testing GIT commit
#Libraries used
import os 
import fileinput
import sys

#Uses stdin and stores into global List
lines_of_data = fileinput.input()

#Lists created for string parsing
data =[]
userInput = []
commandWords = []
tableInfo = []

#Determines the 'default' directory
defaultDirectory = os.getcwd()


########### - Begining of functions - ###########

#Creates Database
def createDirectory (databaseName):
    #Finds current directory
    current_directory = os.getcwd()
    #Makes current directory the dest. directory
    final_directory = os.path.join(current_directory, databaseName)
    if not os.path.exists(final_directory):
        #Creates Directory
        os.makedirs(final_directory)
        print(f"Database {databaseName} created.")
    else:
        #Directory already exists so print statement
        print(f"!Failed to create {databaseName} because it already exists.")

#goes to stated directory 
def useDirectory (databaseName):
    #Resets current directory to defaultDirectory
    os.chdir(defaultDirectory)
    #Determines custom path to database
    path = os.getcwd() + '/' + databaseName
    #Changes current directory to custom path
    os.chdir(path)
    print(f"Using database {databaseName}.")


#Creates Table
def createFile (fileName, tableInfo):
    #checks if Table already exists in current directory
    if os.path.exists(fileName):
        print(f"!Failed to create table {fileName} becuase it already exists.")
    else:
        #splits table info into table attributes
        tableInfo = tableInfo.split(");")[0]
        individualAttributes = tableInfo.split(',')
        current_directory = os.getcwd()
        #opens file as apend 
        newFile = open(fileName, 'a')

        #lists to hold attributes 
        attributes = []
        attrubuteName = []

        #loop through elements of individual Atrributes 
        for i in range(len(individualAttributes)):
            col = []
            # for j in range(1):
            attributeName = individualAttributes[i].split()
            col.append(attributeName[0])
            col.append(attributeName[1])
            #writes attribute name/type to open file
            newFile.write(attributeName[0])
            newFile.write(' ')
            newFile.write(attributeName[1])
            newFile.write(' | ' if i < len(individualAttributes) - 1 else '')

            attributes.append(col)

        #Close file
        newFile.close()

        print(f"Table {fileName} created.")

#Delete Table
def removeFile (fileName):
    #Check if file exists
    if os.path.exists(fileName):
        os.remove(fileName)
        print(f"Table {fileName} created.")
    else:
        #if file doesnt exist, print statement
        print(f"!Failed to delete {fileName} because it does not exitst.")

#Delete 'empty' Database
def removeDirectory (databaseName):
    #Check if database exists
    if os.path.exists(databaseName):
        os.rmdir(databaseName)
        print(f"Database {databaseName} deleted.")
    else:
        #if no database then print statement
        print(f"!Failed to delete {databaseName} because it does not exists.")

#Select * FROM table 
def readFile (fileName):
    #Find the directory where the Table exists
    tableDirectory = find(fileName, defaultDirectory)
    #move to that directory
    os.chdir(tableDirectory)
    #Check if the file exists in current directory
    if os.path.exists(fileName):
        #if yes, open file and read
        readFile = open(fileName, 'r')
        print(readFile.read())
    else:
        #if no, open file and print statement
        print(f"!Failed to query table {fileName} because it does not exist.")

#Select Certain Attributes from Table
def readSpecific(fileName, dependentCondition, selectedAttributes):
    #Find the directory where the Table exists
    tableDirectory = find(fileName, defaultDirectory)
    #move to that directory
    os.chdir(tableDirectory)
    #Check if the file exists in current directory
    if os.path.exists(fileName):
        #if yes, open file and read
        print(f"{fileName} selected. ")
        print(f"{dependentCondition} is the dependent condition ")
        print(f"{selectedAttributes} are the selected attributes ")
    else:
        #if no, open file and print statement
        print(f"!Failed to query table {fileName} because it does not exist.")

#Finds path to queried table
def find(name, path):
    #searches defaultDirectory
    for root, directories, files in os.walk(defaultDirectory):
        #if table exists somewhere in defaultDirectory
        if name in files:
            #return current directory
            return os.getcwd()

#Alter File
def alterFile (fileName, attributeName, atributeType):
    #open file name
    writeFile = open(fileName, 'a')
    writeFile.write(' ')
    writeFile.write(' | ')
    #add new attribute name/type
    writeFile.write(attributeName)
    writeFile.write(' ')
    writeFile.write(atributeType)
    #close file
    writeFile.close()
    print(f'Table {fileName} modified.')

#Insert info into Table
def insertTuple (fileName, tableInfo):
    print(f"{fileName} Selected. ")
    print(f"{tableInfo} Inserted. ")

#Delete tuple from Table
def deleteTuple(fileName, dependentCondition):
    print(f"{fileName} Selected. ")
    print(f"{dependentCondition} Deleted. ")

#Update tuple from Table
def updateTuple(fileName, dependentCondition, newInfo):
    print(f'{fileName} Selected. ')
    print(f'{dependentCondition} is the dependednt condition ')
    print(f'{newInfo} is the new info')


#changes all strings to uppercase
def changeStringLower(mixCase):
    for i in range(len(mixCase)):
        data.append(mixCase[i].lower())

    return data


########### - Begining of "Main" - ###########

# #Pulls only relevant command lines from test file

stringofdata = ' '.join(line.rstrip() for line in sys.stdin if not line.startswith('-'))
mixCase = stringofdata.split(';')

userInput = changeStringLower(mixCase)

#Loops through number of command lines
for i in range(len(userInput)):
    print(i+1)
    commandWords = userInput[i].split('(', 1)
    #print(commandWords)
    #check if there are attributes for a table
    if len(commandWords) > 1:
        #determine command vs table info if applicable
        commandInfo = commandWords[0].strip(';')
        tableInfo = commandWords[1]
        #print(tableInfo)
    else:
        commandInfo = commandWords[0].strip(';')

    #split commandInfo into specific command words
    individualCommandWords = commandInfo.split()
    #print(individualCommandWords)

    #Check individual command words 
    if individualCommandWords[0] == 'create':
        if individualCommandWords[1] == 'database':
            createDirectory(individualCommandWords[2])
        elif individualCommandWords[1] == 'table':
            createFile(individualCommandWords[2].capitalize(), tableInfo)
    
    elif individualCommandWords[0] == 'drop':
        if individualCommandWords[1] == 'database':
            removeDirectory(individualCommandWords[2])
        elif individualCommandWords[1] == 'table':
            removeFile(individualCommandWords[2].capitalize())
        
    elif individualCommandWords[0] == 'use':
        useDirectory(individualCommandWords[1])

    elif individualCommandWords[0] == 'select':
        if individualCommandWords[1] == '*':
            readFile(individualCommandWords[3].capitalize())
        else:
            selectedAttributes = []
            dependentCondition = []
            i = 1 
            while not individualCommandWords[i] == 'from':
                selectedAttributes.append(individualCommandWords[i])
                i+=1
        
            while not individualCommandWords[i] == 'where':
                fileName = individualCommandWords[i]
                i+=1 
            for j in range(i+1, len(individualCommandWords)):
                dependentCondition.append(individualCommandWords[j])
            readSpecific(fileName.capitalize(), dependentCondition, selectedAttributes)
            
    
    elif individualCommandWords[0] == 'alter':
        alterFile(individualCommandWords[2].capitalize(), individualCommandWords[4], individualCommandWords[5])
    
    elif individualCommandWords[0] == 'insert':
        insertTuple(individualCommandWords[2].capitalize(), tableInfo)
    
    elif individualCommandWords[0] == 'delete':
        dependentCondtion = []
        for i in range(4, len(individualCommandWords)):
            dependentCondtion.append(individualCommandWords[i])
        deleteTuple(individualCommandWords[2].capitalize(), dependentCondtion)
    
    elif individualCommandWords[0] == 'update':
        dependentCondtion = []
        newInfo = []
        i = 3 
        while not individualCommandWords[i] == 'where':
            newInfo.append(individualCommandWords[i])
            i+=1
        for j in range(i+1, len(individualCommandWords)):
            dependentCondtion.append(individualCommandWords[j])

        updateTuple(individualCommandWords[2].capitalize(), dependentCondtion, newInfo)
    
    elif individualCommandWords[0] == '.exit':
        print('All done.')
        break

    else:
        print('Invalid Entry. Please Try Again')

    
