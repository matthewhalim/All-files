num = input("Enter a sequence of numbers seperated by whitespace:")
num = num.split(" ")
seq = []
for x in range(len(num)):
    if num[x].isdigit():
        n = int(num[x])
        seq.append(n)
subs = []
stack = [(0, [])]
while stack:
    start_index, current_seq = stack.pop()
    if len(current_seq) > 1 and all(current_seq[i] < current_seq[i+1] for i in range(len(current_seq)-1)):
        subs.append(current_seq)
    for i in range(start_index, len(seq)):
        if not current_seq or seq[i] > current_seq[-1]:
            stack.append((i+1, current_seq+[seq[i]]))
y = [1] * len(subs)
for x in range(1, len(subs)):
    for i in range(x):
        if len(subs[x]) > len(subs[i]):
            y[x] = max(y[x], y[i] + 1)
j = max(y)
loc = y.index(j)
seq = subs[loc]
print(seq)