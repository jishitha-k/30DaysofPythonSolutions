import random
import string

def random_user_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
print(random_user_id())

def user_id_gen_by_user():
    ch = int(input("No.of characters:\n"))
    no = int(input("No.of numbers:\n"))
    characters = string.ascii_letters + string.digits
    Id = []
    for i in range(no):
        user_id =  ''.join(random.choices(characters, k=ch))
        Id.append(user_id)
    return Id
print(user_id_gen_by_user())

def rgb_color_gen():
    rgb = []
    for i in range(3):
        col = random.randint(0,255)
        rgb.append(col)
    return rgb
print(rgb_color_gen())

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
#(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        hex_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        hex_colors.append(hex_color)
    return hex_colors
print(list_of_hexa_colors(7))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        rgb_color = 'rgb({}, {}, {})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(rgb_color)
    return rgb_colors
print(list_of_rgb_colors(5))

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type, n):
    if type == 'hexa':
        return list_of_hexa_colors(n)
    elif type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid type. Please use 'hexa' or 'rgb'."
print(generate_colors('hexa', 3)) 
print(generate_colors('rgb', 3)) 

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print("Shuffled List:", shuffle_list([1,2,3,4,5]))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)
print("Unique Random Numbers:", unique_random_numbers())