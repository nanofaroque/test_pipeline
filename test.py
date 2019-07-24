def file_write(input_str):
    file = open('testfile.txt', 'a')
    file.write(input_str)

file_write("Hello I am here")
