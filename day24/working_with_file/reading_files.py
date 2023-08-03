file = open("my_file.txt")
content = file.read()
print(content)
file.close()

# Alternatively
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
# for this one you don't need to remember to close file everytime
