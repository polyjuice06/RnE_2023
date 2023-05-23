n=4
m=3
B=[10,20,30]
w=[[1,4,5],[6,34,2],[7,5,3],[9,3,8]]
x=[[0]*m for _ in range(n)]
u=[[0]*m for _ in range(n)]
h=[[0]*m for _ in range(n)]

da=[[] for _ in range(m)]
for a in range(m):
  for k in range(n):
    if w[k][a]>0 : da[a].append(k)

dk=[[] for _ in range(n)]
for k in range(n):
  for a in range(m):
    if w[k][a]>0 : dk[k].append(a)

def g(z,a,k):
  global x
  global u
  calc=0
  calc2=0
  for e in da[a]:
    if e==k : continue
    calc+=x[e][a]*w[e][a]
    calc2+=x[e][a]*u[e][a]
  return max(0,z-calc)-calc2

def gs(z,d,a,k):
  global x
  if d>=m:
    return g(z,a,k)
  ret=1000000
  x[d][a]=0
  ret=min(ret,gs(z,d+1,a,k))
  x[d][a]=1
  ret=min(ret,gs(z,d+1,a,k))
  return ret

for _ in range(100):
  for k in range(n):
    for a in range(m):
      h[k][a]=(gs(B[a],0,a,k)-gs(B[a]-w[k][a],0,a,k))
  for k in range(n):
    for a in range(m):
      maxi=-100000
      for b in dk[k]:
        if b==a: continue
        maxi=max(maxi,h[k][b])
      u[k][a]=(-maxi)

for k in range(n):
  for a in range(m):
    print((int)(u[k][a]+h[k][a]>0),end=" ")
  print()