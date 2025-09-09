# File handling in python

# Reading a file

file = open('python/info.txt', 'r')  # open a file in read mode

print(file.read(4))  # read first 4 characters
print(file.tell())  # get the current position of the cursor
file.seek(0)  # move the cursor to the beginning of the file

# print(file.read())  # read the whole file
# print(file.readline())  # read a single line
# print(file.readlines())  # read all lines and return as a list

file.close()  # close the file


# Writing to a file

file = open('python/info1.txt', 'w')  # open a file in write mode

# file.write("Hii, I am Mohammed Nowfel Badhusha") # erase and write to the file
file.writelines(["hii\n", "hello\n", "how are you\n"]) # erase and write multiple lines to the file

file.close()  # close the file


# Appending to a file

file = open('python/info2.txt', 'a')  # open a file in append mode

# file.write("  Bsc Computer Science") # append to the file
file.writelines(["hii\n", "hello\n", "how are you\n"]) # append multiple lines to the file


file.close()  # close the file


# Using 'with' statement to handle files (it automatically closes the file after the block is executed)
'''
with open('python/info.txt', 'r') as file:  # open a file in read mode
    print(file.read())  # read the whole file
'''

# file.flush()  # flush the internal buffer to the file (useful in write and append mode)

