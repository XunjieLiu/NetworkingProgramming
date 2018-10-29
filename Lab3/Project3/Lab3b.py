import re

def search(key, fileName):
    pattern = re.compile(key, flags=re.IGNORECASE)
    lineNum = 0

    f = open(fileName, 'r')
    a = f.readlines()
    for line in a:
        lineNum = lineNum + 1

        if len(pattern.findall(line)):
            for j in pattern.finditer(line):
                print('Line #', lineNum,'position:', j.span()[0])

    f.close()

search('STU', 'junk.txt')

'''


source = "123145"

pattern = re.compile('1')

#result = re.search('1', source)

for i in pattern.finditer(source):
    print(i.span()[0])
'''