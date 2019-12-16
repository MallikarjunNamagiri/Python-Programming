# Function to calculate Largest
# Palindrome which is 
# Product of two n-digits numbers

# Source: https://www.geeksforgeeks.org/largest-palindrome-product-two-n-digit-numbers/

def larrgestPalindrome(n):
	upper_limit = 0

	# loop to calculate upper bound(Largest no.of n-digit)

	for i in range(1, n+1):

		upper_limit = upper_limit * 10
		upper_limit = upper_limit + 9

	# Largest number of n-1 digit. 
	# One Plus this number is lower limit which is 
	# Product of two numbers

	lower_limit = 1 + upper_limit//10

	max_product = 0 # initialize result
	for i in range(upper_limit, lower_limit-1, -1):

		for j in range(i, lower_limit,-1):
			# calculating product of two digit numbers
			product = i * j
			if (product < max_product):
				break
			number = product
			reverse = 0

			# calculating reverse of product to check 
			# wether it is palindrome or not
			while (number != 0):
				
				reverse = reverse * 10 + number % 10
				number = number // 10

			# update new product if exist and if 
			# greater than previous one
			if (product == reverse and product > max_product):
				max_product = product
	return max_product


# Derive Code
n = 3
print(larrgestPalindrome(n)) 