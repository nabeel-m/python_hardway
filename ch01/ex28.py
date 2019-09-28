ten_things="apple orange crows telephone light sugar"
print("There are no ten things in that list,let's fix that")

stuff = ten_things.split(' ')
more_stuff=["Day","night","song","frisbee",
            "corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one=more_stuff.pop()
    print("Adding :",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go",stuff) 
print("let's do something to the stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))