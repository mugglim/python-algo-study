import sys
sys.setrecursionlimit(10**6)


answer = [[],[]]

class Node:
    def __init__(self,x,data):
        self.data = int(data)
        self.x = x
        self.left = None
        self.right = None


def preorder(root):
    answer[0].append(root.data)
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)

def postorder(root):
    if root.left != None:
        postorder(root.left)
    if root.right != None:
        postorder(root.right)

    answer[1].append(root.data)


def solution(nodeinfo):
    nodeinfo = [l+[i+1] for i,l in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x:(-x[1],x[0])) # y값을 기준으로 내림차순 정렬
    y_to_lv = {nodeinfo[0][1]:0}
    dic = {0:[Node(nodeinfo[0][0],nodeinfo[0][-1])]}

    lv = 0

    for node in nodeinfo[1:]:
        y = node[1]
        if y not in y_to_lv:
            lv += 1
            y_to_lv[y] = lv
        if lv not in dic:
            dic[lv] = []

        dic[lv].append(Node(node[0],node[-1]))


    # 이진 트리로 구성하기.
    for lv in list(dic.keys())[1:]:
        for child in dic[lv]:
            curr = dic[0][0]
            while True:
                if child.x < curr.x:
                    if curr.left == None:
                        curr.left = child
                        break
                    curr = curr.left
                elif child.x > curr.x:
                    if curr.right == None:
                        curr.right = child
                        break
                    curr = curr.right

    root = dic[0][0]
    preorder(root)
    postorder(root)

    return answer