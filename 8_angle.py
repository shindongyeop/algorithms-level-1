def solution(angle):
    if angle <90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle <180:
        return 3
    elif angle == 180:
        return 4
    
print(solution(72))  # 1
print(solution(154)) # 3