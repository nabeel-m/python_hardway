zoo = ('python', 'elephant', 'tiger')

print("No. of animals in the zoo is",len(zoo))

new_zoo = 'Monkey','Camel',zoo

print("No. of cages in the new zoo is",len(new_zoo))
print("All the animals in new zoo are",new_zoo)
print("Animals brought new zoo are",new_zoo[2])
print("The last animal brought new zoo are",new_zoo[2][2])
print("The no.of animals new zoo is",len(new_zoo)-1+len(new_zoo[2]))