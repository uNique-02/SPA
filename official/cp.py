import random
from node import Node

def main():
    n = int(input("Enter the number of nodes: "))
    m = n - 1
    
    x = 0
    g = []
    while x < n:
        g.append(x)
        x+=1
    nodes = {Node(f'x{x}') for x in g}
    
    for x in nodes:
        connected = random.randint(0,m)
        print(f"connected: {connected}")
        x.connected_vertices = []
        while connected>0:
            index = random.randint(0,len(nodes)-1)
            range = len(list(nodes))
            node_list = list(nodes)
            nodex = node_list[index].get_name()
            if nodex != x.get_name and nodex not in x.get_connected_vertices(): 
                weight = random.randint(1,10)
                x.append_connected_vertices(nodex, weight)
                connected -= 1
            else:
                connected -= 1
                continue
            
        print(f"node : { x.name} \n connected: {x.get_connected_vertices()} ")
        
        
    
    nodeNum = print(random.randint(0,9))
    
    

if __name__ == "__main__":
    main()
