#0-indexed BFS
import queue
print("位数:",end="")
n=int(input()) #頂点数
print("サイズ:",end="")
m=int(input()) #辺の数
color=[-1]*(n) #各頂点の色(-1:まだ彩色してない　彩色してるなら(0)or(1))
rinsetu_list=[[] for i in range(n)] #隣接リスト
jisu=[0]*(n) #次数
can_paint=True #彩色可能ならTrue,不可能ならFalse
queue=queue.Queue() #キュー
depth=[-1]*(n) #各頂点の根からの深さ
for i in range(m):
    print(str(i+1)+"本目の辺:",end="")
    a,b=map(int,input().split())
    rinsetu_list[a].append(b)
    rinsetu_list[b].append(a)
    jisu[a]+=1
    jisu[b]+=1

for i in range(n):
    if(color[i]>=0):
        continue
    queue.put(i)
    color[i]=0
    depth[i]=0
    while(not(queue.empty())):
        now=queue.get()
        for i in range(jisu[now]):
            next=rinsetu_list[now][i]
            if(color[next]==-1):
                depth[next]=depth[now]+1
                color[next]=depth[next]%2
                queue.put(next)
            else:
                if(abs(depth[now]-depth[next])%2==0):
                    can_paint=False
                    break
    if(not(can_paint)):
        break
if(can_paint):
    print("彩色可能")
    for i in range(n):
        print("頂点"+str(i)+"の色:"+str(color[i]))
else:
    print("彩色不可能")
            
        

    
