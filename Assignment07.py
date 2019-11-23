#Title: Assignment 07
#Description: Demonstrates the Workings of Structured Error-Handling and Pickling
#ChangeLog: KBhattarai, Created script, 11/20/2019
#---------------------------------------------------------------------------------#
import pickle  # This imports code from another code file!

#Data -------------------------------------------- #
strFileName = 'InvData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, inv_data):

    objFile = open(file_name, "wb")
    pickle.dump(inv_data, objFile)
    objFile.close()

def read_data_from_file(file_name):

    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)
    print(objFileData)
    objFile.close()


# Presentation ------------------------------------ #
# Get user input and store it in a list object
#Check to make sure Id has numeric data, and first name and last name are non-numeric.
#Raise exceptions if this is not followed

try:
    intID = int(input("Enter ID: "))
    strFirstName = input("Enter first name here: ")
    strLastName = input("Enter last name here: ")
    strName = strFirstName.title() + " " + strLastName.title()
    lstCustomer = [intID, strName]

    if (str(strFirstName).isnumeric() == True or strFirstName.isnumeric() == True):
        print("Please enter non-numeric values for First Name and Last Name")
    else:
        print(lstCustomer)
        Save_data = save_data_to_file(strFileName, lstCustomer)
        print('Data saved')
except ValueError:
    print("Please enter ID as integer number!")

# store the list object into a binary file
# Read the data from the file into a new list object and display the contents
print("\n\nHere is your current list:\n")
Read_data = read_data_from_file(strFileName)

# Error Handling------------------------------------ #

# store the list object into a binary file
try:
    objFile = open('InvData.dat', 'ab')
    pickle.dump(lstCustomer, objFile)
    objFile.close()

except Exception as e:
    print("There was an error! Try to get the permission of the file. << Custom Message")
    print(e, e.__doc__, type(e), sep='\n')

# Read the data from the file into a new list object and display the contents
#Define exception class
class FileNotDatError(Exception):
    """ File extension must end with dat to indicate it is a dat file """
    def __str__(self):
        return 'File extension is not dat'

#try block to handle exception
try:
    file_name = input("Enter name of the '.dat' file you want to read: ")
    if file_name.lower().endswith('.dat') == False:
         raise FileNotDatError
    objFile = open(file_name.lower(), 'rb')
    print(f'Here is your current data in {file_name.title()} file')
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)

#except block to handle FileNotFoundError exception
except FileNotFoundError as e:
    print("The file must exist before running this script!")
    print(e, e.__doc__, type(e), sep='\n')

#another except block to handle a different exception
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
