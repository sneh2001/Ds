def search_value(value,hash_table):
	hash_value = hash_function(value,list_size)
	print(value,hash_table[hash_value])
	if value in hash_table[hash_value]:
		print("Value found")
	else:
		print("value was not found")


def hash_function(value,list_size):
	return value % list_size

def create_hash_table(main_table,hash_table):
	for element in main_table:
		hash_value = hash_function(element,list_size)
		if hash_table[hash_value][0]:
			print("collision Detected")
			hash_table[hash_value].append(element)
		else:
			hash_table[hash_value][0] = element

list_size = 10
main_table = [45,92,13,34,75,96,71,83,69,10]
hash_table = [[None] for i in range(list_size)]
print(hash_table)
create_hash_table(main_table,hash_table)
print(hash_table)
search_value(71,hash_table)
