words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
          'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
          'flow', 'neon']

rst = {}

for value in words:
    key = ''.join(sorted(list(value)))
    if key in rst.keys():
        rst[key] = rst[key] + [value]
    else:
        rst[key] = [value]

print(rst)


