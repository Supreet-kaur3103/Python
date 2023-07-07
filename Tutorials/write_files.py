#To write to files you use the write method.
#In case the file already exists, its entire content will be replaced when you open it in write mode using "w".

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()


#If you want to add content to an existing file, you can open it using the "a" mode, which stand for "append": 
file = open("/usercode/files/books.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()


#The write method returns the number of bytes written to a file, if successful.
#To write something other than a string, it needs to be converted to a string first.
msg = "Hello world!"
file = open("newfile.txt", "w")  # Open the file in write mode ("w")

amount_written = file.write(msg)  # Write the content of the `msg` variable to the file
print(amount_written)  # Print the number of characters written to the file

file.close()  # Close the file

# Explanation:
# The code opens the file "newfile.txt" in write mode ("w") using the `open()` function.
# It creates a new file if it doesn't exist or overwrites the existing file.

# The line `file.write(msg)` writes the content of the `msg` variable to the file.
# The `write()` method returns the number of characters written, which is stored in the `amount_written` variable.

# The line `print(amount_written)` prints the number of characters written to the file.

# Finally, the file is closed using the `close()` method.

#Please note that if the file "newfile.txt" already exists, its previous contents will be overwritten by the new content. Make sure to use the appropriate file path and handle file operations responsibly.


print("*"*40)
n = int(input())  # Prompt the user to enter a number

file = open("numbers.txt", "w+")  # Open the file in write and read mode ("w+")

# Write numbers from 1 to n to the file
for i in range(1, n + 1):
    file.write(str(i) + '\n')  # Write each number followed by a newline character

file.close()  # Close the file

f = open("numbers.txt", "r")  # Open the file in read mode
print(f.read())  # Read and print the contents of the file

f.close()  # Close the file

# Explanation:
# The code prompts the user to enter a number and stores it in the variable `n`.

# The line `file = open("numbers.txt", "w+")` opens the file "numbers.txt" in write and read mode ("w+").
# If the file already exists, its previous contents will be overwritten.
# If the file doesn't exist, a new file will be created.

# The `for` loop writes numbers from 1 to `n` to the file.
# Each number is converted to a string using `str(i)` and written to the file.
# The `'\n'` is added to insert a newline character after each number.

# After writing the numbers, the file is closed using `file.close()`.

# The line `f = open("numbers.txt", "r")` opens the file in read mode.
# The line `print(f.read())` reads and prints the contents of the file.

# Finally, the file is closed using `f.close()`.

#Please make sure to handle file operations responsibly and provide the correct file path if the file is not in the current working directory.
