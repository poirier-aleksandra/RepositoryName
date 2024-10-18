# TODO заменить значение пропущенного элемента средним арифметическим

valid_nambers = [number for number in numbers if number is not None]
a = sum(valid_nambers)/(len(valid_nambers)+1)

for b in range(len(numbers)):
    if numbers[b] is None:
        numbers[b] = a

print("Измененный список:", numbers)
