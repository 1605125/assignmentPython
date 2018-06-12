# convert input data to upper case into another file


def fn_read(my_file1):
    my_file1 = open(my_file1)
    data = my_file1.read()
    my_file1.close()
    return data


def fn_upper(file_data):
    my_file2 = open("new_upper", 'w')
    my_file2.write(file_data.upper())
    my_file2.close()
    return my_file2.name


file = open('file_upper', 'w')
my_string = input("The file is open now! \n Enter your text: ")
file.write(my_string)
file.close()

content = fn_read(file.name)
print("\n content of file:" + content)

new_file = fn_upper(content)
print('\n Content of the new file :'+fn_read(new_file))
