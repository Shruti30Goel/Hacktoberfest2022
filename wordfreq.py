# Python3 code to demonstrate working of 
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
  
# initializing string
test_str = 'Hello World'
  
# printing original string
print("The original string is : " + str(test_str))
  
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
res = {key: test_str.count(key) for key in test_str.split()}
  
# printing result 
print("The words frequency : " + str(res))
