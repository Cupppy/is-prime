n = [5, 21, 34, 45, 15, 26, 77, 80, 9, 10, 11, 12, 13, 14, 15]
p=[]
np=[]

for i in range(len(n)):
    c=0
    for k in range(2,int(n[i]**0.5)+1):
        if n[i]/k == n[i]//k:
            c+=1
    if c==0:
        p.append(n[i])
    else:
        np.append(n[i])
print(p,np)



