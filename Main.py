#work in progress atm
from copy import deepcopy
f = open('/content/Spellcast.txt', 'r')
file_contents = f.read()
word_list = file_contents.split()
word_len = len(word_list)
tile_values = {'a' : 1, 'b' : 4, 'c' : 5, 'd' : 3, 'e' : 1, 'f' : 5, 'g' : 3, 'h' : 4, 'i' : 1, 'j' : 7, 'k' : 6, 'l' : 3, 'm' : 4, 'n' : 2, 'o' : 1, 'p' : 4, 'q' : 8, 'r' : 2, 's' : 2, 't' : 2, 'u' : 4, 'v' : 5, 'w' : 5, 'x' : 7, 'y' : 4, 'z' : 8,}
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def valid(x):
    l = 0
    r = word_len - 1
    while (l <= r):
        m = (l + r)// 2
        y = word_list[m][:len(x)]
        if y > x:
            r = m - 1
        elif y < x:
            l = m + 1
        else:
            return True
    return False
def exmatch(x):
    l = 0
    r = word_len
    while (l <= r):
        m = l + ((r - l) // 2)
        if (x == word_list[m]):
            return True
        if (x > word_list[m]):
            l = m + 1
        else:
            r = m - 1
    return False
board = [
["i","r","i","e","e"],
["i","o","d","p","b"],
["n","w","m","a","q"],
["s","y","n","n","i"],
["n","m","d","d","r"]]

twox =[1,1]
visited = [[False for i in range(5)] for j in range(5)]
top_words = []
def dfs(word,visited,x,y,boardl):
  word = word+boardl[x][y]
  visited = deepcopy(visited)
  if(visited[x][y]):
    return 0
  if(not valid(word)):
    return 0
  if(exmatch(word)):
    score = 0
    for i in word:
      score+=tile_values[i]
    if(len(word)>=6):
      score+=10
    if visited[twox[0]][twox[1]]:
      score*=2
    if(score>20):
        top_words.append(word)
        top_words.append(score)
  visited[x][y] = True
  
for i in range(-1,2):
    for j in range(-1,2):
      if ((i == 0) and (j==0)) or (x+i>4) or (x+i<0) or (y+j>4) or (y+j<0):
        continue
      dfs(word,visited, x+i, y+j,board)
for i in range(5):
  for j in range(5):
    dfs("",visited,i,j,board)
print(top_words)
