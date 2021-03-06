# 계수 정렬(Count Sort) : '특정 조건'이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 특정 조건 : (중요) 데이터의 크기 범위가 '정수' 형태로 표현할 수 있을 때만 사용 O
#           -> 데이터의 값이 무한한 범위를 가질 수 있는 '실수'형 데이터가 주어지는 경우 사용 X
# 정렬 방식 : 선택 정렬, 삽입 정렬, 퀵 정렬 등과 같은 "비교 기반 정렬 알고리즘"(직접 데이터의 값을 비교한 뒤 위치를 변경하며 정렬)이 아님!
#           1. 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성하고 모든 데이터를 0으로 초기화
#           2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 index의 데이터를 1씩 증가시키면 계수 정렬 완료 (각 데이터가 몇 번 등장했는지 횟수가 기록됨)
# 특징 : 1. 모든 데이터가 '양의 정수'인 상황일 때 : 데이터의 개수가 N, 데이터 중 최댓값이 K라면, 최악의 경우에도 수행 시간 O(N + K)를 보장
#          -> 데이터의 크기가 제한되어 있을 때에 한해서 데이터의 개수가 매우 많더라도 빠르게 동작함!
#       2. 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있음
#          -> '모든 범위를 담을 수 있는 크기의 리스트를 선언'해야 하기 때문
# 시간 복잡도(= O(N + K)) : (N) 앞에서부터 데이터를 하나씩 확인하면서 리스트에서 적절한 index의 값을 1씩 증가시키고, 
#                        (K) 리스트의 각 index에 해당하는 값들을 확인할 때 최댓값의 크기만큼 반복을 수행해야 하기 때문
#                        -> 현존하는 정렬 알고리즘 중 '기수 정렬(Radix Sort)'과 더불어 가장 빠른 알고리즘
# 공간 복잡도(= O(N + K)) : 최댓값과 최소값을 포함하여 모두 담을 수 있는 리스트를 선언해야 함
#                        -> 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하며, 때에 따라서 심각한 비효율성을 초래할 수 있음
# (cf) 퀵 정렬은 일반적인 경우에서 평균적으로 빠르게 동작하므로, 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리함

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]     # 모든 원소의 값이 0보다 크거나 같다고 가정
count = [0] * (max(array) + 1)                            # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)

##### 오름차순 정렬
for i in range(len(array)):
    count[array[i]] += 1       # 각 데이터에 해당하는 index의 값 증가

for i in range(len(count)):    # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        # 띄어쓰기를 구분으로 등장한 횟수만큼 index 출력
        print(i, end = ' ')    # (ex) 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9

##### 내림차순 정렬
for i in range(len(array)):
    count[array[i]] += 1       # 각 데이터에 해당하는 index의 값 증가
    
for i in range(len(count) - 1, -1, -1):   # 초기값 ~ 끝나는 값 : 9 ~ 0
    for j in range(count[i]):
        print(i, end = ' ')    # (ex) 9 9 8 7 6 5 5 4 3 2 2 1 1 0 0