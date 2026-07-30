String = input("PLease enter  a word: ")

string2 = ('')

for i in String:
    string2 = i + string2
    
print(f"\nThe original word= {String}")
print(f"\nThe reversed String = {string2}")