def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"
    
    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)

import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall(r'[A-Z][a-z]+',simple_string)
    
    # YOUR CODE HERE
    raise NotImplementedError()

assert len(names()) == 4, "There are four names in the simple_string"


def grades():
    with open ("//recursion/cousera/grades.txt", "r") as file:
        grades = file.read()

        list_of_B = re.findall(r"[\w ]*:\sB", grades, re.MULTILINE)
        full_name = [list.split(":")[0] for list in list_of_B]
        return full_name
            

    # YOUR CODE HERE
    #raise NotImplementedError()

def logs():
    with open("//recursion/cousera/logdata.txt", "r") as file:
        logdata = file.read()
        list_of_dictionaries = []
        for data in logdata.splitlines():
            raw_data = data.split(" ")

            list_of_dictionaries.append(
                {
                    'host':raw_data[0],
                    'user_name' : raw_data[2],
                    'time': raw_data[3].strip('[') + ' '+ raw_data[4].strip(']'),
                    'request': raw_data[5].strip('"') + ' '+raw_data[6] + ' '+raw_data[7].strip('"')
                }
            )
            
        return list_of_dictionaries[0]
    # YOUR CODE HERE
    #raise NotImplementedError()

print(grades())
#print(logs())