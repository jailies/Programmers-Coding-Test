def solution(n):
    answer = [int(x) for x in str(n)[::-1]]
    #[::-1]은 거꾸로 뒤집는 역할
    return answer