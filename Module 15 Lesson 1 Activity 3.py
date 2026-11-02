n=4
g=input("Predict how many items are in the list(n=4): ")
p=list(range(1,n+1))
print("Guess: ", g, "List: ", p, "Length: ", len(p))
input("Predict what happens when n grows in memory, Press enter to run.")
for i in [4, 10, 100, 1000]:
    print(f"n= {i:<5}. List uses {i:>5} item in memory.")