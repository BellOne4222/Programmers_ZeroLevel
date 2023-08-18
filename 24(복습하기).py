# 문자열 뒤집기

def solution(my_string):
    answer = list(my_string) # 문자열을 리스트로 변환
    answer.reverse() # 리스트 뒤집기
    answer = ''.join(answer) # ''.join을 사용하여 리스트 안의 요소들을 합치기
    return answer