# Three different number sequences given from the question 2023-12-09
input = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]

# Answer Output
answer = 0

# Iterate through all the different puzzels
for seq in input:
    prev = seq
    v = seq[-1]
    while True:
        output = [prev[i] - prev[i-1] for i in range(1, len(prev))]
        v += output[-1]
        prev = output

        # Break the while-loop if we only have zeros in our array
        if all(v == 0 for v in output):
            break
        
    answer += v
print(answer)