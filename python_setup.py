def hello():   
    return("Hello from inside the file")
print(hello())


def pack(a, b, c):
    list = [a,b,c]
    return(list)
print(pack("cheese", "bread", "mayo"))

def eat_lunch(*items):
    if items == 0:
        print("My lunch box is empty")
    else: 
        first = True
        for x in items:
            if first:
                first = False
                print("First I eat " + x)
            else:
                print("Next I eat " + x)
eat_lunch("Sandwhich", "sushi", "pasta")
    