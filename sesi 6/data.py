name = "nugraha", "john", "jane", "doe"
age = "36", "35", "33", "31"

print("no| name    | age ")
 
for i, (x,y) in enumerate(zip(name,age),start=1):
    print(f"{i} | {x:<7} | {y}")