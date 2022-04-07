import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

def print_post_order(pre_order_list, l, r):
    if l > r: return

    right_root_idx = r + 1

    for i in range(l+1,r+1):
        if pre_order_list[i] > pre_order_list[l]:
            right_root_idx = i
            break

    # 만약 오른쪽 서브트리가 없는 경우
    # 1) [l+1, right_root_idx-1] : 기존의 r을 유지.. 
    # 2) [right_root_idx, r] : right_root_idx > r 이므로, 종료
    print_post_order(pre_order_list, l+1, right_root_idx-1)
    print_post_order(pre_order_list, right_root_idx, r)
    print(pre_order_list[l])

if __name__ == "__main__":
    pre_order_list = []

    # for EOF
    while True:
        try:
            pre_order_list.append(int(input()))
        except:
            break

    print_post_order(pre_order_list,0, len(pre_order_list)-1)
