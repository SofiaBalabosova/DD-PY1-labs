numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summary=0
amount=len(numbers)
for i in range(amount):
    if numbers[i] == None:
        j = i
        continue
    summary += numbers[i]

average = summary/amount
numbers[j] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
