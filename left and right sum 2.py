n = int(input())
left_sum = 0
right_sum = 0

for number in range(0, n):
    current_number = int(input())
    left_sum += current_number

for number in range(0, n):
    current_number = int(input())
    right_sum += current_number

if left_sum == right_sum:
    print("Yes, sum = " + str(right_sum))
else:
    diff = abs(left_sum - right_sum)
    print("No, diff = " + str(diff))
