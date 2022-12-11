def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ##OK
    f=open(file_name,'r')
    file_contents=f.read()
    print(file_contents)
    return file_contents
    

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    # f=open(file_name,'r')
    # file_contents=f.read()
    # list=file_contents.split("\n")
    # return list
    f=open(file_name,'r')
    file_contents=f.readlines()
    
    return file_contents

    

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ##OK
    lines=file_contents.split('\n')
    with open(output_filename, 'w') as f:
        f.writelines(lines[0])
    
    ece=open(output_filename,'r')
    ecee=ece.read()
    print(ecee)


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
   
    # list=" "
    # i = 0
    # f = open(file_name,'r')
    # for line in f.readlines():
    #     if i % 2 == 0 :
    #         list +=  line 
    #     i += 1
    
    # return list

    even_list = []
    f=open(file_name,'r')
    file_contents=f.readlines()
    #print("The original list : " + str(file_contents))
    for i in range(0, len(file_contents)):
        if i % 2:
         even_list.append(file_contents[i])

    return even_list

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    f=open(file_name,'r')
    file_contents=f.readlines()
    
    reversed_list = []
    for value in file_contents:
        reversed_list = [value] + reversed_list
    print(reversed_list)
    
    return reversed_list
  

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()