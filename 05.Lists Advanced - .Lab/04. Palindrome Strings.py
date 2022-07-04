word = input().split()
palindrome = input()

#list = [n for n in word if n == n[::-1]]
list = list(filter(lambda n: n == n[::-1], word))
palindrome_count = word.count(palindrome)
a=5
print(list)
print(f'Found palindrome {palindrome_count} times')
