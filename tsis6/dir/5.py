fruits =['apple', 'banana', 'orange', 'cherry']
with open('input5.txt', 'w') as x:
    for f in fruits:
        x.write("%s\n" % f)