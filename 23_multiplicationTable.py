def MultiplicationTable(digit):
    for i in range(1,10+1):
        print(f"{i} * {digit} = {i*digit}")
    
print(MultiplicationTable(5))