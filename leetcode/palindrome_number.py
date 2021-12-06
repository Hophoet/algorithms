# palindrome number it reads the same backward as forward


def is_palindrome(x:int):
	""" palindrome """
	x_list = [n for n in str(x)]	
	x_list.reverse()
	reverse_x = int( ''.join(x_list)) 
	return True if x == reverse_x else False


#print(is_palindrome(121))
#print(is_palindrome(123))


