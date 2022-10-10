from os import error
import re

def welcome_message():
    """
    the welcome message function
    """
    print("Welcome to madlib Game, we are glad to share this game with you")

def read_template(file):
    """
    in this function i will import the data from test and return it again
    """
    try:
        with open(file,'r') as reader:
            '''
            strip():
            all leading and trailing whitespaces are removed from the string.
            '''
            str=reader.read().strip()
            return(str)
    except FileNotFoundError:
            raise FileNotFoundError('Not the right path!')


def parse_template(str):
    """
    in this function i will parse the function within two parts,
    first part will stripped the sentence 
    and the second part will put theese words in a list!
    """
    stripped = re.sub('\{[a-zA-Z0-9\' -]*\}', "{}", str)
    list=re.findall("\{[a-zA-Z0-9\' -]*\}", str)
    x=0
    for y in list: 
            list[x] = y.strip('{').strip('}')
            x += 1
    list=tuple(list)
    return stripped,list

# print(parse_template(str))

def user_inputs_things(game_template):
    """
    in this function will prompt to the user to input the words to complete the lab template
    """
    user_input=[]
    x = 0
    for word in game_template:
        user_input.append(input("Select a " +game_template[x]+ " -> "))
        x += 1
    return user_input

# print(user_inputs_things(game_template))

def merge(str,user_input):
    ''' add the input list in template and return template with input  '''
    print("Are You Ready for the story?")
    user_input=tuple(user_input)
    the_text= str.format(*user_input)
    print("\n",the_text,"\n")
    place = "assets/game.txt"
    with open(place, 'w') as folder:
        folder.write(the_text)
    return the_text
if __name__ == '__main__':
    """
    Call functions
    """
    welcome_message()
    template_read = read_template('assets/make_me_a_video_game_template.txt')

    values,inputs = parse_template(template_read) 

    user_inputs = user_inputs_things(inputs)

    merge(values,user_inputs)


