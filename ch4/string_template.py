import string

# Call the substitute method -->
# Can use ${..} or $..
template = string.Template('${artist} sang $song in $year')

print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))

# Or use a dictionary -->
d = dict(artist = 'Billy Idol', song = 'Eyes Without a Face', year = 1984)
print(template.substitute(d))

d = dict(artist = 'Billy Idol', song = 'Eyes Without a Face')
print(template.safe_substitute(d))
#----------------variable does not have to be 'template'
pattern = string.Template('$artist sang $song in $year')

print(pattern.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))

d = dict(artist = 'Billy Idol', song = 'Eyes Without a Face', year = 1984)
print(pattern.substitute(d))

d = dict(artist = 'Billy Idol', song = 'Eyes Without a Face')
print(pattern.safe_substitute(d))
