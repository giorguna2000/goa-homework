# 3)მომხმარებელს შემოატანინე მისი გვარი, თუ ეს გვარი იწყება "m" ასოთი მაშინ დაბეჭდეთ მომხმარებლის შემოტანილი გვარი გადიდებული, თუ იწყება "g" ასოთი, მაშინ დაბეჭდეთ მომხმარებლის სახელი დაპატარავებული

name = input("Enter your name: ")
surname = input("Enter your surname: ")

if surname[0].lower() == 'm':
    print(surname.upper())
elif surname[0].lower() == 'g':
    print(name.lower())
else:
    print("Nothing to show.")