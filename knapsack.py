p=[20,10,6,9,18,12,16,30,13]
print(sum(p))
w=[4,5,6,3,2,5,4,6,6]
pwr=[]
pro=[]
wei=[]
print(len(p))
for i in range(len(p)):
    pwr.append(p[i]/w[i])
max_weight=30
print("Profit Weight Ratio: ",pwr)
while max_weight>=0:
    if sum(pwr) is 0:
        break
    max_pwr=max(pwr)
    max_index=pwr.index(max_pwr)
    if w[max_index]<=max_weight:
        pro.append(p[max_index])
        wei.append(w[max_index])
        max_weight=max_weight-w[max_index]
    pwr[max_index]=0
print("max_profit: ",sum(pro))
print("max_weight: ",sum(wei))

    
