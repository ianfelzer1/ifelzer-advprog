def main():
    num=input("Enter a # and I'll tell you all perfect numbers up to that #:  ")
    for i in range(1,num+1):
        sum=0
        for j in range(1,(i/2)+1): # why +1?
            if i%j==0:        # check if remainder is 0
                sum=sum+j
                   # print "factor: ",i
        if sum==i:
            print sum,"is Perfect!"
    print "That's all there are!"

main()
