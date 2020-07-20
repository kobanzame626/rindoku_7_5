#0-indexed DFS
def dfs(x,c):
    global jisu,color,rinsetu_list
    color[x]=c
    for i in range(jisu[x]):
        next=rinsetu_list[x][i]
        if(color[next]==color[x]):
            return False
        if(color[next]==-1 and not(dfs(next,1-color[x]))): #nextが彩色されてなければDFSを実行
            return False
    return True

    
print("位数:",end="")
n=int(input()) #頂点数
print("サイズ:",end="")
m=int(input()) #辺の数
color=[-1]*(n) #各頂点の色(-1:まだ彩色してない　彩色してるなら(0)or(1))
rinsetu_list=[[] for i in range(n)] #隣接リスト
jisu=[0]*(n) #次数　　
can_paint=True #彩色可能ならTrue,不可能ならFalse
for i in range(m):
    print(str(i+1)+"本目の辺:",end="")
    a,b=map(int,input().split())
    rinsetu_list[a].append(b)
    rinsetu_list[b].append(a)
    jisu[a]+=1
    jisu[b]+=1
    
for i in range(n):
    if(color[i]==-1):
        if(not(dfs(i,0))):
            can_paint=False
            break
if(can_paint):
    print("彩色可能")
    for i in range(n):
        print("頂点"+str(i)+"の色:"+str(color[i]))
else:
    print("彩色不可能")


