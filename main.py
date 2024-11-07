import random
from node import Node

def main():
    n = int(input("Enter the number of nodes: "))
    m = n - 1
    
    label = [range(1,n)]
    nodes = {Node(f'x{x}') for x in label}
    
    for x in nodes:
        connected = random.randint(0,m)
        while m>0:
            index = random.randint(0,len(nodes))
            range = len(list(nodes))
            node_list = list(nodes)
            nodex = node_list[index].get_name()
            if nodex != x.get_name & nodex not in x.get_connected_vertices():
                x.set_connected_vertices(nodex)
                m -= 1
                print(x.get_connected_vertices())
            else:
                continue
        
    
    nodeNum = print(random.randint(0,9))
    
    

if __name__ == "__main__":
    main()
