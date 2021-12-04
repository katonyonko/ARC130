import io
import sys

_INPUT = """\
6
253
286
345
556
123
987987
11111111111111111111
111111111111111111111111111111
123
987989
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a=input()
  b=input()
  r=0
  if len(a)<len(b):
    a,b=b,a
    r=1
  A=[0]*10
  B=[0]*10
  for i in range(len(a)):
    A[int(a[i])]+=1
  for i in range(len(b)):
    B[int(b[i])]+=1

  tmp=A.copy()
  tmp[9]-=min(len(a)-len(b),tmp[9])
  tmp2=B.copy()
  ans1,ans2=[],[]
  x,y=9,1
  k=0
  for i in range(len(b)):
    while tmp[x]==0:
      x-=1
    y=10-x-k
    ans1.append(str(x))
    tmp[x]-=1
    while y<10 and tmp2[y]==0:
      y+=1
    if y==10:
      y=1
      while y<10 and tmp2[y]==0:
        y+=1
    ans2.append(str(y))
    tmp2[y]-=1
    if x+y+k>=10:
      k=1
    else:
      k=0
  ans1=ans1[::-1]
  ans2=ans2[::-1]
  if len(str(int(''.join(ans1))+int(''.join(ans2))))>len(b):
    t=[]
    for i in range(10):
      for j in range(tmp[i]):
        t.append(str(i))
    ans1=t+['9']*min(len(a)-len(b),A[9])+ans1
  else:
    tmp=A.copy()
    tmp2=B.copy()
    ans1,ans2=[],[]
    x,y=9,1
    k=0
    for i in range(len(b)):
      while tmp[x]==0:
        x-=1
      y=10-x-k
      ans1.append(str(x))
      tmp[x]-=1
      while y<10 and B[y]==0:
        y+=1
      if y==10:
        y=1
        while y<10 and B[y]==0:
          y+=1
      ans2.append(str(y))
      B[y]-=1
      if x+y+k>=10:
        k=1
      else:
        k=0
    t=[]
    for i in range(10):
      for j in range(tmp[i]):
        t.append(str(i))
    ans1=t+ans1[::-1]
    ans2=ans2[::-1]

  if r==0:
    print(''.join(ans1))
    print(''.join(ans2))
  else:
    print(''.join(ans2))
    print(''.join(ans1))