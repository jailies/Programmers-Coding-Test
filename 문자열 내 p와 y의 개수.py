def solution(s):
    answer = True
    s = s.upper()
    pcount = 0
    ycount = 0
    for i in s:
        if i == 'P':
            pcount += 1
        elif i == 'Y':
            ycount += 1
    if pcount == ycount:
        answer = True
    else:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer