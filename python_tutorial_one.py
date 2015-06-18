#print "Hello world"
#print "James, you are a programmer guy, now."

#this program prints hello james.
#In case you forgot what happens...
x = "Hello, James"
#print x

y = [x,"stuff",18,["yes","i","am","doing","this"]]
for element in y:
    if element == "stuff":
        print element
    elif type(element) == type(int()):
        print element,"this is a number!"
    else:
        print "wellllll, I wish it had worked, but it didn't."
        print "le-si"
        
