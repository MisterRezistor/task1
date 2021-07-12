line = input("Введіть рядок для опрацювання: ")
lineSplit = line.split()
numbers = []

i = 0
while i < len(lineSplit):
    if lineSplit[i].isdecimal():
        numbers.append(int(lineSplit.pop(i)))
        continue
    digits = "".join(filter(lambda i: i.isdecimal(), lineSplit[i]))
    if digits:
        numbers.append(int(digits))
        lineSplit[i] = "".join(filter(lambda i: not i.isdecimal(), lineSplit[i]))
    i += 1

lineSplit = list(map(lambda item: item.title()[:-1] + item[-1].upper(), lineSplit))

maxNumber = 0
numbersPowered = list()
if numbers:
    maxNumber = max(numbers)
    numbersPowered = list(
        map(lambda x: x ** numbers.index(x) if x != maxNumber else x, numbers)
    )

lineEdited = " ".join(lineSplit)

print("", f"Ваша стрічка: {line}", "", f"Стрічка після редагування: {lineEdited}", "", sep="\n")

if numbers:
    print(
        f"Числа: {numbers}",
        "",
        f"Максимальне число: {maxNumber}",
        "",
        f"Числа після долучення: {numbersPowered}",
        sep="\n",
    )