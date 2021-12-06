# palindrome number it reads the same backward as forward

def is_palindrome(x:int):
	""" palindrome """
	x_list:list = [n for n in str(x)]	
	x_list.reverse()
	return True if str(x) == ''.join(x_list) else False

# print(is_palindrome(121))
# print(is_palindrome(-121))
# print(is_palindrome(123))