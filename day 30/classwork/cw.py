# 1) კომენტარის სახით ახსენით რას აკეთებს len(), append(), insert() და pop() ფუნქციები
my_list = [1, 2, 3, 4]

length = len(my_list)  
my_list.append(5) 

my_list.insert(2, 99)  
removed = my_list.pop(3) 

# 2) შექმენით სია და შეინახეთ  5 სახელი. მომხმარებელს შემოატანინეთ სახელი და დაამატეთ ამ სიაში. ბოლოს, დაბეჭდეთ ამ სიის სიგრძე და სიის განახლებული ვერსია.
names = ["ანა", "ლუკა", "მარიამი", "გიორგი", "ნინო"]

new_name = input("enter your name ")
names.append(new_name)

print("სიის სიგრძეა:", len(names))
print("განახლებული სია:", names)

 
# 3) შექმენით სია: fruits = ["Melon", "Orange", "Banana", "Watermelon", "Kiwi"]
# ამოაგდეთ სიიდან ბოლო ელემენტი და მესამე ინდექსზე ჩასვით "Pomegranate".

fruits = ["Melon", "Orange", "Banana", "Watermelon", "Kiwi"]
fruits.pop() 
fruits.insert(3, "Pomegranate")
print(fruits)