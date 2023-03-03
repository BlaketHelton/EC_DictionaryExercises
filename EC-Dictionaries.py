john = open('book of john text.txt','r')

content = john.read()

words = content.split()

word_dict = {
    'Father': 0, 
    'God': 0, 
    'Christ': 0, 
    'Spirit': 0, 
    'spirit': 0, 
    'life': 0, 
    'man': 0
    }

for word in words:
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1

print(f"Father: {word_dict['Father']}")
print(f"God: {word_dict['God']}")
print(f"Christ: {word_dict['Christ']}")
print(f"Spirit: {word_dict['Spirit']}")
print(f"spirit: {word_dict['spirit']}")
print(f"life: {word_dict['life']}")
print(f"man: {word_dict['man']}")