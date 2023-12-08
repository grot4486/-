Часть №1
a, b = 1, 2
print(a)
print(b)
Часть №2
a, b = (1, 2)
print(a)
print(b)
Часть №3
name, age, company = ("Виктория", 18, "МВД")
print(name)
print(age)
print(company)
Часть №4
people = ["Антон", "Семен", "Полина"]
first, second, third = people
print(first)
print(second)
print(third)
Часть №5
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
print(dictionary[g])
Часть №6
people = [
    ("Антон", 17, "ФСБ"),
    ("Семен", 17, "ФСБ"),
    ("Полина", 19, "МЧС")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")
    Часть №7
    people = ["Андрей", "Семен", "Полина"]
for index, name in enumerate(people):
    print(f"{index}.{name}")
    Часть №8
    person =("Виктория", 18, "МВД")
name, _, company = person
print(name)
print(company)
Часть №9
name, _, company = person
print(_)
Часть №10
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)
Часть №11
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
Часть №12
*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
Часть №13
head, *middle, tail = [1, 2, 3, 4, 5]

print(head)
print(middle)
print(tail)
Часть №14
first, second, *other = [1, 2, 3, 4, 5]

print(first)
print(second)
print(other)
Часть №15
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]

print(first)
print(third)
print(last)
Часть №16
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}

print(red)
print(green)
print(other)
Часть №17
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
nums3 = [*nums1, *nums2]
print(nums3)
Часть №18
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)
