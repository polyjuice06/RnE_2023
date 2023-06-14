N=4
w=[[],[0,8,2,8,1],[0,7,8,7,2],[0,1,2,9,9],[0,4,9,8,4]]
b=[[0]*(N+1) for _ in range(N+1)]
a=[[0]*(N+1) for _ in range(N+1)]
n=[[0]*(N+1) for _ in range(N+1)]
p=[[0]*(N+1) for _ in range(N+1)]

t=100

while t>0:
  t-=1
  for i in range(1,N+1):
    for j in range(1,N+1):
      b[i][j]/=2
      b[i][j]+=(w[i][j]+a[i][j])/2

  for i in range(1,N+1):
    for j in range(1,N+1):
      maxi=-12345678
      for k in range(1,N+1):
        if k!=j:maxi=max(maxi,b[i][k])
      n[i][j]/=2
      n[i][j]+=-maxi/2

  for i in range(1,N+1):
    for j in range(1,N+1):
      p[i][j]/=2
      p[i][j]+=(w[i][j]+n[i][j])/2

  for i in range(1,N+1):
    for j in range(1,N+1):
      maxi=-12345678
      for k in range(1,N+1):
        if k!=i: maxi=max(maxi,p[k][j])
      a[i][j]/=2
      a[i][j]+=-maxi/2

for i in range(1,N+1):
  for j in range(1,N+1) : print(int(a[i][j]+p[i][j]>0),end=" ")
  print()
