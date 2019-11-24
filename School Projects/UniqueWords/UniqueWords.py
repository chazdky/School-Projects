
# This is a program for taking a text document of words,
# and processing that file into a list of only the unique words,
# and then printing them out for the user


def get_text_from_file(input_file):

    # reading the data from a file and returning a string of seperate words
    textString = input_file.read()
    return textString.split()


def get_unique_words(words):

    # taking a string of words and only keeping the unique or distint words
    distinct_words = set(words)
    return distinct_words


def print_unique_words():

    # the main input file and the programs to run
    input_file = open("text.txt", 'r')
    words = []
    try:
        words = get_text_from_file(input_file)

        unique_words = get_unique_words(words)

        for eachWord in unique_words:
            print(eachWord)

    except IOError:
        print('Sorry, missing text file')
    except EOFError:
        print('File found. But Void of data')
    except:
        print('An Error Occurred')


if __name__ == '__main__':
    while print_unique_words():
        print()
