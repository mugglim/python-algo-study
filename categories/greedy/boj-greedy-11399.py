n = int(input())
burst_time_list = list(map(int,input().split()))

def get_sjf_time(burst_time_list):
    total_time = 0
    waiting_time = 0

    for burst_time in sorted(burst_time_list):
        total_time += waiting_time + burst_time
        waiting_time += burst_time

    return total_time

print(get_sjf_time(burst_time_list))