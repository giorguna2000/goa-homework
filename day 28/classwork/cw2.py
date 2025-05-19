# 2)მომხმარებელს შემოატანინეთ მისი სახელი და შეამოწმეთ, თუ მისის ასო იწყება დიდი ასოთი, მაშინ დაბეჭდეთ "Hello!", სხვა შემთხვევაში "Bye..."
 
name = input("Enter your name: ")

if name[0].isupper():
    print("Hello!")
else:
    print("Bye...")