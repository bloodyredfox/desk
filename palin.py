def rev(s):
	s = s[::-1]
	return s

n = input("Enter a number:")
print(n)
if n == rev(n):
	print("Palindrome")
else:
	print("Not Palindrome")

	