def shortest_dist_to_char(S, C):
    target = float('-inf')
    result = []
    for i, c in enumerate(S):
        if c == C:
            target = i
        result.append(i - target)

    target = float('inf')
    for i in range(len(S) - 1, -1, -1):
        if S[i] == C:
            target = i
        result[i] = min(result[i], target - i)
    return result

S = "loveleetcode"
C = 'e'
print(shortest_dist_to_char(S, C))