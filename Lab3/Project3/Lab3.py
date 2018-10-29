# import the regex library
import re

'''
# compile the regex into a regex object
p = re.compile('c[abc]*t')

# use the regex object to find all matches in a target string with the findall() function
matches = p.findall('ctcatcabt')

# matches is a list of matches, so we iterate over the list....
for i in matches:
    print(i)


# open a file in read mode
f = open('junk.txt', 'r')

a = f.read()

print(a)

f.close()
'''

# or we can loop over lines
f = open('junk.txt', 'r')
for line in f:
    # why do we need this end=''?
    print(line, end='')
f.close()

#or we can read them as a list
f = open('junk.txt', 'r')
a = f.readlines()
for i in a:
    # why does this print a blank line between the file lines?
    print(i)
