word =(input("Enter a word that you'd like to reverse: "))

string2 =('')

for r in word:
    string2 = r+string2
print(f" \nThe Original Word: {word}")
print(f"\n The reversed String : {string2}\n")