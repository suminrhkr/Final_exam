Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222087 이름 : 곽수민

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution1(my_string, target):
    if (target in my_string):   # x in 문자열 -> x가 문자열 안에 존재하는지
        answer = 1              # 존재한다면 answer = 1
    else:                       # 그렇지 않으면
        answer = 0              # answer = 0
    return answer               # answer의 값을 반환한다

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution2(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    s = letter.split()                          # 공백으로 문자열 분리, s 리스트로 반환됨
    answer = ''.join([morse[i] for i in s])     # s 문자열 안의 i에 대한 morse[i]를 계산해서 리스트에 저장하고, 저장된 리스트를 공백이었던 answer에 삽입
    return answer                               # answer의 값을 반환한다

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
... # age가 매개변수로 주어질 때
... # PROGEAMMER-857식 나이를 return 하도록
... # solution 함수를 완성하시오.
... #
... # 제한사항
... # age는 자연수입니다.
... # age ≤ 1,000
... # PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.
... 
... def solution3(age):
...     e = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']      # e[0] = 'a', e[1] = 'b', ... , e[9] = 'j'
...     answer = ''.join([e[int(i)] for i in str(age)])             # 문자형으로 변환한 age 문자열 안의 문자 i에 대한 e[int(i)]를 계산해서 리스트에 저장하고, 그 리스트를 공백이었던 answer에 삽입
...     return answer                                               # answer의 값을 반환한다
... 
... # Q.4 10점
... #
... # x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
... # 서로 다른 크기의 원이 두 개 주어집니다.
... # 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
... # 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
... # return하도록 solution 함수를 완성해주세요.
... # ※ 각 원 위의 점도 포함하여 셉니다.
... #
... # 제한사항
... # 1 ≤ r1 < r2 ≤ 1,000,000
... 
... import math 
... def solution4(r1, r2):
...     answer = 0                                                                                              # answer = 0으로 초기화
...     for i in range(1, r2 + 1) :                                                                             # 1부터 r2+1 미만의 숫자들을 포함하는 range객체 생성, i는 1부터 r2까지 1씩 증가되며 반복된다
...         answer += math.floor(math.sqrt(r2**2 - i**2)) - math.ceil(math.sqrt(max(0, r1**2 - i**2))) + 1      # 큰 원과 작은 원 사이에 겹치지 않는 부분의 점의 개수를 구한
...     return answer*4                                                                                         # 위 코드는 제 1사분면의 점들만 계산한 것이기 때문에 answer에 4를 곱한 값을 반환한다
... 
... # Q.5 10점
... #
... # 0 또는 양의 정수가 주어졌을 때,
... # 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
... #
... # 예를 들어, 주어진 정수가 [6, 10, 2]라면
... # [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
... # 이중 가장 큰 수는 6210입니다.
... #
... # 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
... # 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
... # return 하도록 solution 함수를 작성해주세요.
... #
... # 제한사항
... # numbers의 길이는 1 이상 100,000 이하입니다.
... # numbers의 원소는 0 이상 1,000 이하입니다.
... # 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
... #
... # numbers = [8, 30, 17, 2, 23]
... 
... def solution5(numbers):
...     num = list(map(str, numbers))                   # 리스트 numbers의 원소들을 문자형으로 바꾼 후 새로운 num list에 저장
...     num.sort(key = lambda x:x*3, reverse = True)    # 각 요소들을 3번 반복하고, 요소들을 내림차순으로 정렬한다
...     for i in numbers:                               # 정수인 numbers의 원소들을
...         answer = ''.join(num)                       # 새롭게 내림차순으로 정렬한 num list의 순서대로 다시 정렬하고 이를 문자열 answer에 저장한다
...     return answer                                   # answer의 값을 반환한다
