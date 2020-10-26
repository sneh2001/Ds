def search_value(value, hash_table):
	hash_value = hash_function(value,list_size)
	if value in hash_table:
		print("Value found")
	else:
		print("value was not found")


def hash_function(value, list_size):
	return value % list_size


def create_hash_table( main_table , hash_table):

	for element in main_table:
		print(hash_table)
		index = 0
		hash_value = hash_function(element,list_size)
		while index < list_size:

			if hash_table[hash_value]:

				print("collision Detected")
				print("Moving to another slot -->")
				if hash_value == (list_size-1):
					hash_value = 0
					index += 1
				else:
					hash_value += 1
					index += 1
			else:
				hash_table[hash_value] = element
				break

list_size = 10
main_table = [45,92,13,34,75,96,71,83,69,10]
hash_table = [None for i in range(list_size)]
print(hash_table)
create_hash_table(main_table,hash_table)
print(hash_table)
search_value(71, hash_table)
