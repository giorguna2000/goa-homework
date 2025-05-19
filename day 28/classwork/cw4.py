# 4)მომხმარებელს შემოატანინეთ მისი საყვარელი ფერი, თუ ეს ფერი შეიცავს "p" ასოს, მაშინ დაბეჭდეთ "Gamarjoba", სხვა შემთხვევაში "Naxvamdis"

color = input("Enter your favorite color: ")

if 'p' in color.lower():
    print("Gamarjoba")
else:
    print("Naxvamdis")