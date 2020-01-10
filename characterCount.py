import pprint
print('Enter anything')
message = input()
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)