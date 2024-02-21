# Leia 4 notas, mostre as notas e a média
grades = [10, 8.8, 9.2, 6.2]
sum = 0
average = 0
number_elements = len(grades)

for elements_average in grades:
    print(elements_average)
    sum += elements_average
    average = sum / number_elements

print(f"Média: {average}")

