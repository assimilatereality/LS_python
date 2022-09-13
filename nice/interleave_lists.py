a = [1,2,3]
b = [4,5,6]
interleaved_list = [val for pair in zip(a,b) for val in pair]
print(interleaved_list)
