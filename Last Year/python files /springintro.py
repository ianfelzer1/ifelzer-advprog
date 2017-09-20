## simple lists
# Matt Z
# November, 2015

# Key concepts:  defining a list, noting elements, slice notation

def main():
    A=[]
    for i in range (5):
        num = input("Enter a number: ")
        A.append (num)
    print "the entire list: ",A
    print "the list, without brackets: "
    for i in A:
        print i,
    print
    print "elements 2-3 (actually 3-4)"
    print A[2:4]
    maxA = A[0]
    for i in range (1,5):
        if A[i] > maxA:
            maxA = A[i]
    print 'maximum is ',maxA
    minA = A[0]
    for i in range (1,5):
        if A[i] < minA:
            minA = A[i]
    print "The minimum value is",minA, "and its index value is",A.index(minA)
main()    
