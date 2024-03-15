# ECOR 1042 Lab 3 - Individual submission for character_luck_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "55"

#==========================================#
# Place your character_luck_list function after this line
import string
def character_luck_list(filename: str, luck_threshold: float) -> list:
    """Return a list of dictionaries imported from a given CSV file.
    (For all characters whose luck is less than the luck threshold 
    & the attribute is not "Luck")
    
    >>> character_luck_list('characters-mat.csv', 0.4)
    [{'Occupation': 'AT',
      'Strength': 12,
      'Agility': 3,
      'Stamina': 7,
      'Personality': 13,
      'Intelligence': 11,
      'Armor': 8,
      'Weapon': 'Staff'},
     {'Occupation': 'AT',
      'Strength': 19,
      'Agility': 9,
      'Stamina': 9,
      'Personality': 10,
      'Intelligence': 12,
      'Armor': 10,
      'Weapon': 'Dagger'},....
    
    >>> character_luck_list('characters-mat.csv', 0.2)
    [{'Occupation': 'VF',
      'Strength': 12,
      'Agility': 4,
      'Stamina': 2,
      'Personality': 14,
      'Intelligence': 14,
      'Armor': 9,
      'Weapon': 'Dagger'}]
    """
    
    characters = [] #Empty list initialized to store dictionaries
    row_counter = 0
    with open(filename) as file: #Opening CSV to read
        for item in file:
            row_counter += 1
            
            my_list = item.strip().split(',')
            
            if row_counter > 1:
                if float(my_list[6]) < luck_threshold:
                    character_dict = {'Occupation': my_list[0], 'Strength': int(my_list[1]),
                                      'Agility': int(my_list[2]), 'Stamina': int(my_list[3]),
                                      'Personality': int(my_list[4]), 'Intelligence': int(my_list[5]),
                                      'Armor': int(my_list[7]), 'Weapon': my_list[8]}
                    
                    characters.append(character_dict)
            
    return characters   

# Do NOT include a main script in your submission