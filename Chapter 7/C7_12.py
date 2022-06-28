try:
    file_name = input("Enter the file name : ")
    infile = open(file_name, "r")
    infile_list = []
    count = 0
    for i in infile:
        file_line = i.rstrip()
        infile_list.append(file_line)
        count += 1
    print(f"The file contains {count} lines.")

    line_number = int(input("\nwhich line do you want to print?"))
    print(infile_list[line_number - 1])
except IOError:
    print("\nCheck the file name.")
except ValueError:
    print(
        "\ninvalid value for the line number.\nPlease enter a valid poi=sitive integer."
    )
except IndexError:
    print("\nThere are not as many lines in the file.")
