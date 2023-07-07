#You can use Python to read and write the contents of files.
#This is particularly useful when you need to work with a lot of data that is saved in a file. 
#For example, in data science and analytics, the data is commonly in CSV (comma-separated values) files.
#Let's start by working with text files, as they are the easiest to manipulate. 
#Before a file can be edited, it must be opened, using the open function. 
myfile = open("filename.txt")
#The argument of the open function is the path to the file. If the file is in the current working directory of the program, you can specify only its name.



#You can specify the mode used to open a file by applying a second argument to the open function.
#Sending "r" means open in read mode, which is the default. 
#Sending "w" means write mode, for rewriting the contents of a file.
#Sending "a" means append mode, for adding new content to the end of the file.
#Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")



#Once a file has been opened and used, you should close it.
#This is done with the close method of the file object. 
file = open("filename.txt", "w")
# do stuff to the file
file.close()


print("*"*40)
#The contents of a file that has been opened in text mode can be read using the read method. 
#We have created a books.txt file on the server which includes titles of books. Let's read the file and output the content:

file = open("/usercode/files/books.txt")
cont = file.read()
print(cont)
file.close()



#To read only a certain amount of a file, you can provide the number of bytes to read as an argument to the read function. 
#Each ASCII character is 1 byte: 

try:
    with open("/usercode/files/books.txt", "r") as file:
        content = file.read(5)  # Read the first 5 characters from the file
        print(content)

        content = file.read(7)  # Read the next 7 characters from the file
        print(content)

        content = file.read()  # Read the rest of the file
        print(content)
        
except FileNotFoundError:
    print("File not found or path is incorrect.")
except IOError:
    print("Error occurred while reading the file.")


#To retrieve each line in a file, you can use the readlines() method to return a list in which each element is a line in the file.
try:
    file = open("/usercode/files/books.txt", "r")  # Open the file in read mode

    for line in file.readlines():
        print(line)  # Print each line from the file

except FileNotFoundError:
    print("File not found or path is incorrect.")
except IOError:
    print("Error occurred while reading the file.")

finally:
    file.close()  # Close the file, regardless of any exceptions

# Explanation:
# The code opens the file named "books.txt" in read mode using the `open()` function.
# It then uses a `for` loop to iterate over each line in the file.
# Inside the loop, each line is printed to the console using the `print()` function.
# After processing all the lines, the `finally` block is executed to ensure the file is closed.
# The `finally` block uses the `close()` method to close the file.
# Additionally, exceptions like `FileNotFoundError` and `IOError` are caught and handled using `except` blocks.
# These blocks provide error messages or handle exceptions as needed.

#Please make sure to replace "/usercode/files/books.txt" with the correct file path and ensure that the file exists in that location.


#If you do not need the list for each line, you can simply iterate over the file variable:
try:
    file = open("/usercode/files/books.txt", "r")  # Open the file in read mode

    for line in file:
        print(line)  # Print each line from the file

except FileNotFoundError:
    print("File not found or path is incorrect.")
except IOError:
    print("Error occurred while reading the file.")

finally:
    file.close()  # Close the file, regardless of any exceptions

# Explanation:
# The code opens the file named "books.txt" in read mode using the `open()` function.
# It then uses a `for` loop to iterate over each line in the file.
# Inside the loop, each line is printed to the console using the `print()` function.
# After processing all the lines, the `finally` block is executed to ensure the file is closed.
# The `finally` block uses the `close()` method to close the file.
# Additionally, exceptions like `FileNotFoundError` and `IOError` are caught and handled using `except` blocks.
# These blocks provide error messages or handle exceptions as needed.

#Please make sure to replace "/usercode/files/books.txt" with the correct file path and ensure that the file exists in that location.



print("*"*40)
try:
    file = open("/usercode/files/books.txt", "r")  # Open the file in read mode

    N = int(input())  # Prompt the user to enter the number of characters to read

    content = file.read(N)  # Read the first N characters from the file
    print(content)

except FileNotFoundError:
    print("File not found or path is incorrect.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except IOError:
    print("Error occurred while reading the file.")

finally:
    file.close()  # Close the file, regardless of any exceptions

# Explanation:
# The code opens the file named "books.txt" in read mode using the `open()` function.
# It then prompts the user to enter the number of characters (N) to read from the file.

# Inside the `try` block:
# - The `int(input())` statement converts the user's input into an integer.
# - The `file.read(N)` statement reads the first N characters from the file.

# If the file is not found, a `FileNotFoundError` will be raised and caught in the corresponding `except` block.
# If the user enters an invalid input (not a valid number), a `ValueError` will be raised and caught.
# If there is an error while reading the file, an `IOError` will be raised and caught.

# Regardless of whether an exception occurs or not, the `finally` block will be executed to close the file.

#Please make sure to replace "/usercode/files/books.txt" with the correct file path and ensure that the file exists in that location.





#It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.
try:
    f = open("/usercode/files/books.txt")  # Open the file

    cont = f.read()  # Read the contents of the file
    print(cont)  # Print the contents

finally:
    f.close()  # Close the file, regardless of any exceptions

# Explanation:
# The code opens the file named "books.txt" located at "/usercode/files" using the `open()` function.
# The file is opened in the default read mode ("r").

# Inside the `try` block:
# - The line `f.read()` reads the contents of the file and stores them in the `cont` variable.
# - The line `print(cont)` prints the contents of the file to the console.

# The `finally` block is used to ensure proper closure of the file.
# Whether an exception occurs or not, the `finally` block is executed.
# In this case, the `finally` block uses the `f.close()` statement to close the file.

#Please make sure that the file path "/usercode/files/books.txt" is correct and the file exists in that location. Also, note that using an absolute file path may depend on the specific environment or platform.

#An alternative way of doing this is by using with statements.This creates a temporary variable (often called f),  which is only accessible in the indented block of the with statement. 
#The file is automatically closed at the end of the with statement, even if exceptions occur within it.
with open("/usercode/files/books.txt") as f:
  print(f.read())
  
  
print("*"*40)
with open("/usercode/files/books.txt") as f:
    j = 1  # Initialize a variable to keep track of the line number
    
    for line in f:
        word_count = len(line.split(" "))  # Count the number of words in the current line
        print("Line " + str(j) + ": " + str(word_count) + " words")
        j += 1  # Increment the line number counter

# Explanation:
# The code uses a `with` statement to open the file "books.txt" located at "/usercode/files".
# The `with` statement ensures proper file handling and closure, even if an exception occurs.

# Inside the `with` block:
# - The line `j = 1` initializes a variable to keep track of the line number.
# - The `for` loop iterates over each line in the file.
# - For each line, the line is split into words using `line.split(" ")`, assuming words are separated by spaces.
# - The `len()` function is used to count the number of words in the line.
# - The line number (`j`) and the word count are printed using the `print()` function.
# - The line number (`j`) is incremented after processing each line.

# The `with` statement automatically handles the closure of the file after the block is executed.

#Please make sure that the file path "/usercode/files/books.txt" is correct and the file exists in that location.
N#ote that word counting based on spaces as separators may not accurately handle all cases of word boundaries.
