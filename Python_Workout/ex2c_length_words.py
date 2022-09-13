def mysum(words):
    output = [0, 0, 0]
    tmp = []
    for word in words:
        tmp.append(len(word))
    print(tmp)
    return (min(tmp), sum(tmp)/len(tmp),max(tmp))


print(mysum(['one', 'fourteen', 'seven', 'five']))
