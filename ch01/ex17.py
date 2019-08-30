def print_two(*args):
    args1, args2 = args
    print(f"args1 : {args1}\nargs2 :{args2}")
                                                    
def print_two_again(args1, args2):
    print(f"args1 : {args1}\nargs2 :{args2}")         #function decleration

def print_one(args1):
    print(f"args1 : {args1}")

def print_none():
    print("I got nothing\n")



print_two("nabeel","mohammed")
print_two_again("fabi","mohammed")
print_one("hello!")
print_none()       