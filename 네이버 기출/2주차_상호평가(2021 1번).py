def solution(scores):
    answer = ''
    for i in range(len(scores)):
        arr = []
        for j in range(len(scores)):
          arr.append(scores[j][i])
        if arr[i] == min(arr) and arr.count(arr[i]) == 1:
            del arr[i]
        elif arr[i] == max(arr) and arr.count(arr[i]) == 1:
            del arr[i]
        record = sum(arr) / len(arr)
        
        if record >= 90: answer += 'A'
        elif record >= 80: answer += 'B'
        elif record >= 70: answer += 'C'
        elif record >= 50: answer += 'D'
        else: answer += 'F'
    
    return answer