sentence = "hippo runs to us!"
text = {}

for i in sentence :
    count = 0
    for j in sentence :
        if i == j :
            count += 1
    text.update({i:count})
print(text)
