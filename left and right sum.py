n = int(input())
left_sum = 0
right_sum = 0

for number in range(0, n*2):
    current_number = int(input())
    if number < n:
        left_sum += current_number
    elif number >= n:
        right_sum = current_number

if left_sum == right_sum:
    print("Yes, sum = " + str(right_sum))
else:
    diff = abs(left_sum - right_sum)
    print("No, diff = " + str(diff))
