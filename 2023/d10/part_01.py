D = open('input.txt').read().strip()
L = D.split('\n')

G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])

for r in range(R):
  for c in range(C):
    if G[r][c]=='S':
      sr,sc = r,c
      up_valid = (G[r-1][c] in ['|','7','F'])
      right_valid = (G[r][c+1] in ['-','7','J'])
      down_valid = (G[r+1][c] in ['|','L','J'])
      left_valid = (G[r][c-1] in ['-','L','F'])
      assert sum([up_valid, right_valid, down_valid, left_valid]) == 2
      if up_valid and down_valid:
        G[r][c]='|'
        sd = 0
      elif up_valid and right_valid:
        G[r][c]='L'
        sd = 0
      elif up_valid and left_valid:
        G[r][c]='J'
        sd = 0
      elif down_valid and right_valid:
        G[r][c]='F'
        sd = 2
      elif down_valid and left_valid:
        G[r][c]='7'
        sd = 2
      elif left_valid and right_valid:
        G[r][c]='-'
        sd = 1
      else:
        assert False

DR = [-1,0,1,0]
DC = [0,1,0,-1]
r = sr
c = sc
d = sd
dist = 0
while True:
  dist += 1
  r += DR[d]
  c += DC[d]
  if G[r][c]=='L':
    if d not in [2,3]:
      break
    elif d==2:
      d = 1
    else:
      d = 0
  if G[r][c]=='J':
    if d not in [1,2]:
      break
    elif d==1:
      d = 0
    else:
      d = 3
  if G[r][c]=='7':
    if d not in [0,1]:
      break
    elif d==0:
      d = 3
    else:
      d = 2
  if G[r][c]=='F':
    if d not in [0,3]:
      break
    elif d==0:
      d = 1
    else:
      d = 2
  assert G[r][c] != '.'
  if (r,c) == (sr,sc):
    print(dist//2)
    break