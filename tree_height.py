# python3

import sys
import threading

def compute_height(n, parents):
    # Write this function
    heights = {}
    def calculate_height(node):
        if node in heights:
            return heights[node]
        
        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = 1 + calculate_height(parents[node])

        return heights[node]
    # Your code here
    max_height = 0
    for node in range(n):
        max_height = max(max_height, calculate_height(node))

    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if "F" in text:
        file = input()
        with open("./test/" + file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            print(compute_height(n, data))
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        print(compute_height(n, data))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
