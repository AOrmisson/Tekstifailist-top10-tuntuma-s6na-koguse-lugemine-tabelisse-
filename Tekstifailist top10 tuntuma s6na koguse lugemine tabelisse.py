import string

filename = input("Enter a file name: ")

with open(filename, "r") as file:
    text = file.read()
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [char.translate(table) for char in words]
#Eemaldasin kirjavahemärgid tekstist

word_dict = dict()

for word in stripped:
    if word in word_dict:
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1
#Loendan kõik sõnad hulga poolest ja lisan nad dictionarisse

for word in tuple(word_dict.keys()):
    if word.isdigit():
        del word_dict[word]
#Ei võimalda lisada nubmreid dictionarisse

#print(sorted(zip(word_dict.values(), word_dict.keys())))

from collections import Counter

C = Counter(word_dict)
high = C.most_common(10)

print("Top10 sõna")
print("Nimi: Kogus")

for i in high:
    print(i[0]," :",i[1]," ")
#Otsin välja top10 enim esinevat sõna ja prindin need välja tabelina













