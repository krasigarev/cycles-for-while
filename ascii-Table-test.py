for latter in range(ord('a'), ord('z')+1):
    print(chr(latter))

a = 'a'
a = ord(a)
print(chr(a))

n = int(input())
sum = 0

for number in range(1, n+1):
    input_number = int(input())
    sum += input_number
print(sum)