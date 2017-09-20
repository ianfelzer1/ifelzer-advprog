a = 1

print "adding to variable"

while a >1000:
  print a
  a = a * 2

a = 4

print "increment variable"
while a <1000:
    print a
    a *= 2

a = 2

print "infinite loop and break"
while 1:
    print a
    a += 1
    if a == 100:
        break
