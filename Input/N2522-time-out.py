import sys

# 아이디어: 왼쪽이 모두 나보다 작고, 오른쪽도 모두 나보다 크면 꼬이지 않는다.

def bulb_num(K, N, switches):
    # 꼬인 스위치들
    twisted_bulbs = []

    # 전구 숫자들
    bulb_nums = []

   # 꼬인 스위치 구하기  
    for i in range(N):
        twisted_bulb = set([switches[i]])

        for j in range(0, i, 1):
            if switches[j] > switches[i]:
                twisted_bulb.add(switches[j])

        for k in range(i, N, 1):
            if switches[k] < switches[i]:
                twisted_bulb.add(switches[k])

        if len(twisted_bulb) > 1:
            twisted_bulbs.append(twisted_bulb)

    # 전구 숫자 구하기
    candidate_num = 0
    index = 0
    temp = list(map(lambda x: 2 ** x, range(N)))

    while index <= K-1:
        bulb_on = []
    
        for l in range(N):
            if temp[l] & candidate_num:
                bulb_on.append(l+1)
        
        switch_on = set([switches[N-x] for x in bulb_on])

        if is_valid_switch(twisted_bulbs, switch_on):
            bulb_nums.append(candidate_num)
            index += 1

        candidate_num += 1

    return bulb_nums[index-1]

# 전구 숫자에 대한 스위치 타당성 검사
def is_valid_switch(twisted_bulbs, switch_on):
    for i in range(len(twisted_bulbs)):
            if twisted_bulbs[i].issubset(switch_on):
                return False
    return True

# 스위치 수
N = int(sys.stdin.readline().rstrip())

# B_N, B_{N-1}, ..., B_1과 연결된 스위치
switches = list(map(int, sys.stdin.readline().rstrip().split()))

# K
K = int(sys.stdin.readline().rstrip())

print(bulb_num(K, N, switches))