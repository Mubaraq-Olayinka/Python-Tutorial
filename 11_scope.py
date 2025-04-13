name = "Dave" #global scope 
count = 1

def another():
    color = "blue" #local scope 
    global count 
    count += 1
    print(count)
    
    def greeting(firstname):
        nonlocal color
        color = "red"
        print(color)
        print("hello" + " " + name)
        print(firstname)
        
    greeting("Dave")
    
another()