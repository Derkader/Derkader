'''
Created on Jun 25, 2022

@author: derek nash

File I/O Using Tuples Assignment
'''

""" this accepts a tuple to be added to the end of a text file
:param args, a tuple with a name and array of scores
"""
def write_to_file(args):
    filename = 'student_info.txt'
    f = open(filename, 'a')

    name = args[0]
    scores = str(args[1])
    my_line = name + " " + scores + "\n"

    f.writelines(my_line)
    f.close()


"""
    Prompts the user to input as many test scores as they wish
    Stores the information (name and scores) in a tuple
    Calls the function write_to_file() sending the tuple to be written to the end of the file
"""
def get_student_info():
    name = input("Give me a name: ")
    scores = []
    score = input("Give me as many scores as you wish, or type 'OK': ")
    while score != 'OK' and score != 'ok':
        scores.append(score)
        score = input("Give me as many scores as you wish, or type 'OK': ")
    my_tuple = (name, scores)
    write_to_file(my_tuple)


'''
    Reads a file line by line
    Prints each line to the console
'''
def read_from_file():
    filename = 'student_info.txt'
    f = open(filename, 'r')

    lines = f.readlines()
    for line in lines:
        print(line)


if __name__ == '__main__':
    open("student_info.txt","w").close()

    get_student_info()
    get_student_info()
    get_student_info()
    get_student_info()
    read_from_file()
    