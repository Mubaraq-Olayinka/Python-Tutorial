def add_one(num):
  if (num >= 9):
    return num + 1
    
  total = num + 1 
  print(total)
    
  return add_one(total)

add_one(0) #this doesn't print the value in the if statement

my_new_total = add_one(0)
print(my_new_total) #this now prints the value in the if statement 