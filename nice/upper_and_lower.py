def myfunc(word):
    out = []
    for index in range(0, len(word)):
        if index % 2 == 0:
            out.append(word[index].upper())
        else:
            out.append(word[index].lower())
    return ''.join(out)

print(myfunc('Anthropomorphism'))
