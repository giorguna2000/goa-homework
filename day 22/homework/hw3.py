# 4) ცვლადში შეინახეთ თქვენი საყვარელი სიმღერის სახელი, შემდეგ კი მომხმარებელს შემოატანინეთ მისი საყვარელი სიმღერა. იმ შემთხვევაში თუ თქვენი და მომხმარებლის საყვარელი სიმღერა ემთხვევა - გამოიტანეთ "we have the same favorite song", სხვა შემთხვევაში კი გამოიტანეთ "we have different favorite songs"

my_favorite_song = "Shape of You"
user_favorite_song = input("What is your favorite song? ")
if my_favorite_song == user_favorite_song:
    print("We have the same favorite song.")
else:
    print("We have different favorite songs.")