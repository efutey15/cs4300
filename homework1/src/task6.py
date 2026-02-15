#Tsak 6: Text Processing
import string

#Counting the number of words in the file
def count_words():
    filename = 'src/task6_read_me.txt'
    try:
        with open(filename, 'r') as file:
            content = file.read()

            #Removing punctuation from the text
            cleaned = content.translate(str.maketrans("","",string.punctuation))

            words = cleaned.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return -1