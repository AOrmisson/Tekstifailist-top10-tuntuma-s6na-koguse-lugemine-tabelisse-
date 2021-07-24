import string

filename = input("Enter a file name: ")

with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [char.translate(table) for char in words]
    #print(stripped)

word_dict = dict()

for word in stripped:
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1

for word in tuple(word_dict.keys()):
    if word.isdigit():
        del word_dict[word]

#print(sorted(zip(word_dict.values(), word_dict.keys())))

from collections import Counter

C = Counter(word_dict)
high = C.most_common(10)

print("Top10 nime")
print("Nimi: Kogus")

for i in high:
    print(i[0]," :",i[1]," ")














