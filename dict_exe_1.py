# Store info about a Person using dictionaries
# person = {"f_name": 'Doreen', 'l_name': 'Plange',
        #   'age': 27, 'city': 'Tema'}
# for key, value in person.items():
    # print(f"{key}: {value}")
    
# Favorite Numbers
# fav_num = {"Persis": 7, "Nate": 6, "Josh": 6, "Babs": 4}
# for key, value in fav_num.items():
    # print(f"{key}'s favorite num is {value}")
    
# Glossary
glossary = {"print": "to output something to screen",
            "format": "present output in readable and neat form",
            "def": "keyword for defining a function",
            "run": "process of executing a program",
            "clear": "function to remove everything from a list or dictionary",
            "iteration": "go through a set of data in sequence"
            }
for word, definition in glossary.items():
    print(f"{word}\n: {definition}\n")