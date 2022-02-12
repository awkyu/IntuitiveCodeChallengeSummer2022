import os


def check_file(argv):
    """
    Function to check the arguments of the input to see if there are a valid number of args and if there are
    enough arguments and if the file input exists

    :param argv: the argv from the command line input
    :return: the file_path from the argv if a valid input filename
    :raise Exception: if the number of arguments is invalid (argv must be length 2)
    :raise FileNotFoundError: if the filename is invalid
    """
    if len(argv) != 2:
        raise Exception("Invalid Number of Arguments")
    file_path = os.getcwd() + "\\\\" + str(argv[1])
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist")
    else:
        return file_path


def usage():
    """
    function that just returns how to use the error checker

    :return: None (just prints the message)
    """
    print("Usage:   python Encoder_Potentiometer_ErrorCheck.py <filename>")
    print("Example: python Encoder_Potentiometer_ErrorCheck.py 'Code Challenge Data\\normal.txt'")
