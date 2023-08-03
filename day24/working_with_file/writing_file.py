with open("my_file.txt", mode="a") as file:
    file.write("new yes.")

# by default, the mode is read only. unless i specify the mode the program wouldnt write my file. Also while using mode = "w", it will replace the content of previous file.
# if i want to add i will use mode = "w"
# more over if there is no file mode = "w" will create a file.
