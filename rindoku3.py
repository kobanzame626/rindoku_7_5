#0-indexed DFS+BFS(cycle)
print("位数:",end="")
n=int(input()) #頂点数
print("サイズ:",end="")
m=int(input()) #辺の数
rinsetu_list=[[] for i in range(n)] #隣接リスト
jisu=[0]*(n) #次数
for i in range(m):
    print(str(i+1)+"本目の辺:",end="")
    a,b=map(int,input().split())
    rinsetu_list[a].append(b)
    rinsetu_list[b].append(a)
    jisu[a]+=1
    jisu[b]+=1

can_paint=True #彩色可能ならTrue,不可能ならFalse
stack=[] #スタック
parent=[-1]*n #親を記録
out_node1=-1
out_node2=-1

# B1
color=[-1]*(n) #各頂点の色(-1:まだ彩色してない　彩色してるなら(0)or(1))
w=n
# B2-B8
while(w>=0):
    # B2
    if(w==0): #彩色成功
        break
    w-=1
    # B3
    if(color[w]>=0):
        continue # B2へ戻る
    stack.append(w) #スタックにwを追加
    color[w]=0
    # B4-B5-B7-B8
    while(stack!=[]): #スタックが空になるまで続ける
        now=stack.pop() #スタックの末尾を取り出す
        for i in range(jisu[now]): #頂点nowの隣接頂点を調べる
            next=rinsetu_list[now][i]
            # B6
            if(color[next]==-1): #まだnextが彩色されてない
                color[next]=1-color[now]
                parent[next]=now
                stack.append(next)
            else:
                if(color[next]==color[now]): #彩色できない
                    can_paint=False
                    out_node1=now 
                    out_node2=next
                    break
        if(not(can_paint)):
            break
    if(not(can_paint)):
        break
if(can_paint):
    print("彩色可能")
    for i in range(n):
        print("頂点"+str(i)+"の色:"+str(color[i]))
else:
    print("彩色不可能")
    print("サイクル")
    cycle=[]
    cycle.append(out_node1)
    while(parent[out_node1]!=-1):
        cycle.append(parent[out_node1])
        out_node1=parent[out_node1]
    cycle.append(out_node2)
    while(parent[out_node2]!=-1):
        cycle.append(parent[out_node2])
        out_node2=parent[out_node2]
    cycle.pop() #根が重複してるので、1つ削除
    for i in range(len(cycle)):
        print(str(cycle[i])+" ",end="")
    print()
            
        

    
