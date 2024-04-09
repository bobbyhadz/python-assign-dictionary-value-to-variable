# Assign a dictionary value to a Variable in Python

my_dict = {
    'first_name': 'Bobby',
    'last_name': 'Hadz',
    'site': 'bobbyhadz.com',
}

first = my_dict['first_name']
print(first)  # 👉️ Bobby

first = list(my_dict.values())[0]
print(first)  # 👉️ Bobby

key = 'last_name'
value = my_dict[key]
print(value)  # 👉️ Hadz