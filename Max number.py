alpha = [2, 1, 7, 4, 9, 8]
maximus = (len(alpha))
for i in alpha:
    if i > maximus:
        maximus = i
        second = maximus - 1

print("The maximum number is: \n")
print(maximus)

print()

print("The second maximum number is: \n")
print(second)
