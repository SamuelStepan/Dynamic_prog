import igraph as ig
import numpy as np

def naiv_Fibonacci(n:int, output = True)->None:
    """Naive algorithm (not using memoization) that computes the n-th fibonacci number"""
    def fib(n:int)->int:
        if(n <= 2):
            return 1
        else:
            return fib(n-1) + fib(n-2)
    if(not output):
        fib(n)
        return
    #computes the n-th number and prints it
    print(f"The {n}-th Fibonacci number is {fib(n)}")

def memo_Fibonacci(n:int, output = True)->None:
    """Algorithm that computes the n-th fibonacci number using memoization """
    memo = {1:1, 2:1}   #dictionary that will keep values of fibonnaci numbers
    def fib(n:int)->int:
        if(n in memo):
            return memo[n]
        else:
            f = fib(n-1) + fib(n-2)
            memo[n] = f
            return f
    if(not output):
        fib(n)
        return
    #computes the n-th number and prints it
    print(f"The {n}-th Fibonacci number is {fib(n)}")

def bottom_up_Fibonaci(n:int, output = True):
    """Algorithm that computes the n-th fibonacci number using bottom up aproach"""
    fib_d = {1:1, 2:1}  #dictionary that will keep values of fibonnaci numbers
    for k in range(3, n+1):
        fib_d[k] = fib_d[k-1] + fib_d[k-2]
    if(not output):
        return
    print(f"The {n}-th Fibonacci number is {fib_d[n]}")
        


def naiv_short_path(num_nodes: int, s_node: int, t_node: int, w: dict[tuple,float], output = True)->None:
    """Naive algorithm (not using memoization) to find shortest path from node s to t, it prints results to console"""
    edges = w.keys()

    #creating dictionary that will hold list of parent nodes for each node
    parents = {node: [] for node in range(num_nodes)}   #saving empty list representing parents for each node
    for parent, child in edges:
        parents[child].append(parent)
    
    min_parents = {node: -1 for node in range(num_nodes)}   #dictionary to save minimal parent node for each node  
    #defining recursive funcion

    def delta(s_node, t_node)->float:
        """recursive function that will return value of minimal path from node s to node u"""
        if(s_node == t_node):   #boundary condition
            return 0
        if(len(parents[t_node]) == 0):
            return float("inf")
        else:
            options = np.array([w[(u_node, t_node)] + delta(s_node, u_node) for u_node in parents[t_node]])
            min_indx = np.argmin(options)
            min_parents[t_node] = parents[t_node][min_indx] #saving which node is on the shortest path from s to t before t
            return options[min_indx]

    #finding sollution
    path_val = delta(s_node, t_node)
    if(not output):
        return
    if(path_val == float('inf')):
        print("In graph does not exist path from node s to node t")
        return
    print("Value of shortest path is", path_val)
    #constructing shortest path
    path = [t_node]
    child = t_node
    loop_b = True
    while(loop_b):
        par = min_parents[child]
        path.append(par)
        child = par
        if(par == s_node):
            loop_b = False
    #printing shortest path
    print("Shortest path is:")
    for node in reversed(path[1:]):
        print(node, "->", end=" ")
    print(path[0])

def memo_short_path(num_nodes: int, s_node: int, t_node: int, w: dict[tuple,float], output = True)->tuple:
    """Algorithm to find shortest path from node s to t using memoization, it prints results to console"""
    edges = w.keys()

    memo = {}
    #creating dictionary that will hold list of parent nodes for each node
    parents = {node: [] for node in range(num_nodes)}   #saving empty list representing parents for each node
    for parent, child in edges:
        parents[child].append(parent)
    
    min_parents = {node: -1 for node in range(num_nodes)}   #dictionary to save minimal parent node for each node  
    #defining recursive funcion

    def delta(s_node, t_node):
        """recursive function that will return value of minimal path from node s to node u"""
        if(t_node in memo):
            return memo[t_node]
        if(s_node == t_node):   #boundary condition
            return 0
        if(len(parents[t_node]) == 0):
            return float("inf")
        else:
            options = np.array([w[(u_node, t_node)] + delta(s_node, u_node) for u_node in parents[t_node]])
            min_indx = np.argmin(options)
            min_parents[t_node] = parents[t_node][min_indx] #saving which node is on the shortest path from s to t before t
            return options[min_indx]

    #finding sollution
    path_val = delta(s_node, t_node)
    if(not output):
        return
    if(path_val == float('inf')):
        print("There does not exist path from node s to node t")
        return
    print("Value of shortest path is", path_val)
    #constructing shortest path
    path = [t_node]
    child = t_node
    loop_b = True
    while(loop_b):
        par = min_parents[child]
        path.append(par)
        child = par
        if(par == s_node):
            loop_b = False
    #printing shortest path
    print("Shortest path is:")
    for node in reversed(path[1:]):
        print(node, "->", end=" ")
    print(path[0])


