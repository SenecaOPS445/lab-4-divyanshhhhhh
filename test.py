

# dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}

# print('These are the keys' + str(dict_york.values()))
# print('These are the keys' + str(dict_york.keys()))

# dict_york['Country'] = 'Canada'
# print(dict_york)
# print(dict_york.values())
# print(dict_york.keys())

# list1 = ['address','hahahaha']
# list2 = ['Leys']
# list_of_keys = list(dict_york.keys())

# empt = {}
# print(list_of_keys[0])
# empt[list2[0]] = [list1[0]]

# print(empt)

list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

temp_Dict = {}
count = 0
while count < len(keys):
    temp_Dict(keys[count]) = values[count]
    count += 1

print(temp_Dict)