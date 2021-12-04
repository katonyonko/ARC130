import io
import sys

_INPUT = """\
6
4 5 6 5
1 1 6
1 3 3
2 2 4
2 4 2
1 1 2
1000000000 1000000000 3 5
1 1 2
1 2 2
1 3 2
1 4 2
1 5 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W,C,Q=map(int,input().split())
  query=[]
  for _ in range(Q):
    t,n,c=map(int,input().split())
    c-=1
    query.append([t,n,c])
  tmp=set()
  tmp2=[]
  for i in reversed(range(Q)):
    t,n,c=query[i]
    if (t,n) not in tmp:
      tmp2.append([t,n,c])
      tmp.add((t,n))
  query=tmp2[::-1]
  Q=len(query)
  r,cc=0,0
  rf,cf,rb,cb,ans=[0]*C,[0]*C,[0]*C,[0]*C,[0]*C
  # print(query)
  for i in range(Q):
    t,n,c=query[i]
    if t==1:
      rb[c]+=1
      r+=1
    else:
      cb[c]+=1
      cc+=1
  # print(r,c)
  for i in range(Q):
    t,n,c=query[i]
    if t==1:
      ans[c]+=W-cf[c]-(cc-cb[c])
      # if i==3:
      #   print(W,cf[c],c,cb[c])
      rf[c]+=1
      rb[c]-=1
      r-=1
    else:
      ans[c]+=H-rf[c]-(r-rb[c])
      cf[c]+=1
      cb[c]-=1
      cc-=1
  print(*ans)