def hello_world():
  print("Hello world")
  
hello_world()

def sum(num1=0, num2=0): 
  if (type(num1) is not int or type(num2) is not int):
    return 0
  return num1 + num2
  
# total = sum(2, 4)
total = sum(1, 2)

print(total)

# function handling multiple parameters without knowledge of how many 

def multiple_items(*args): 
  print(args)
  print(type(args))
  
multiple_items("Dave", "John", "Sara")
#this returns as tuples

#for keywords args like num1 instead of args with unknown keywords
#kwargs = keyword args
def mult_named_items(**kwargs):
  print(kwargs)
  print(type(kwargs))
  
mult_named_items(first = "Dave", last = "Gray")
#this returns as dictionaries