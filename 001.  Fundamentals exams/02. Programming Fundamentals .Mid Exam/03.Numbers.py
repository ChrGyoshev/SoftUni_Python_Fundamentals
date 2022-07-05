numbers = list(map(int, input().split()))
avg = sum(numbers) / len(numbers)

filtered = [nums for nums in numbers if nums > avg]
filtered.sort()
filtered.reverse()
if not filtered:
    print("No")

if len(filtered)<=5:
    print(*filtered,sep=" ")

else:
    print(*filtered[:5],sep=" ")