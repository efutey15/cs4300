#Task 5: Lists and Dictionaries

#Printing first three favorite books
def list_slicing():
    favoriteBooks = ["Before the Coffee gets Cold, Toshikazu Kawaguchi",
                    "Piranesi, Susanna Clarke",
                    "Hamnet, Maggie OFarrell",
                    "Normal People, Sally Rooney",
                    "Percy Jackson, Rick Riordan"]
    
    print(favoriteBooks[:3])

#Student Database Dictionary
def student_dict(name):
    studentDict = {
        "Evan" : 135332,
        "Sam" : 132467,
        "Selin" : 567676,
        "Lindsay" : 903560,
        "Nyx" : 777767,
        "Nova" : 543987
    }
    print(studentDict[name])