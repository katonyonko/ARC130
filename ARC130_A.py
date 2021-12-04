import io
import sys

_INPUT = """\
6
7
abbbcca
4
xxxx
2
pp
2
st
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  tmp=[]
  cnt=1
  for i in range(N-1):
    if S[i]==S[i+1]:
      cnt+=1
    else:
      tmp.append(cnt)
      cnt=1
  tmp.append(cnt)
  ans=0
  for i in range(len(tmp)):
    ans+=tmp[i]*(tmp[i]-1)//2
  print(ans)