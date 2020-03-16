def triple_trouble(one, two, three):
    answer = ''
    for i in range(len(one)):
        answer += one[i] + two[i] + three[i]
    return answer


print(triple_trouble('aaa', 'bbb', 'ccc'))
