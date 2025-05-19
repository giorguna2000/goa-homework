# 3) შექმენით სია, სადაც შეინახავთ რიცხვებს 20-იდან 30-ის ჩათვლით. Slicing-ის გამოყენებით დაბეჭდეთ ამ სიიდან  ყველა ლუწი რიცხვი. (მინიშნება: step)

numbers = list(range(20, 31))
even_numbers = numbers[::2]
print(even_numbers)