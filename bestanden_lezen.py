f = open("readme.txt") # Open my-file.txt and assign result to f.
content = f.read() # Read contents of file into content variable.
print(content) # Print content.
f.close() # Close the file.

with open("readme.txt") as f:
    content = f.read()
    print(content)

with open("my-file2.txt", "w") as f:
    f.write("Hello, world!!!!!")    