# когато диапазонът НЕ започва с 0

n = int(input())
odd_sum = 0
even_sum =0

for number in range(1, n+1):
    current_sum = int(input())
    if number%2 == 0:
        even_sum +=current_sum
    else:
        odd_sum +=current_sum

print(even_sum)
print(odd_sum)

# когато диапазонът Започва с 0

n = int(input())
odd_sum = 0
even_sum =0

for number in range(0, n):
    current_sum = int(input())
    if number+1%2 == 0:
        even_sum +=current_sum
    else:
        odd_sum +=current_sum

print(even_sum)
print(odd_sum)