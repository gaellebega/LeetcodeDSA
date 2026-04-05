def richestcustomer(accounts):
    total=0
    maximum=float("-inf")
    for i in range(len(accounts)):
        total=sum(accounts[i])
        maximum=max(maximum,total)
    return maximum    
print(richestcustomer([[1,2,3],[4,5]]))


