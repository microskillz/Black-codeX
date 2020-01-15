prime = [2, 5, 1, 8, 7]
alpha = sorted(prime)

print("The sorted list is:\n")
print(alpha)

print()

print("The maximum number is:\n")
print(max(alpha))

print("Second maximum number is:\n")
alpha.remove(max(alpha))
print(max(alpha))
