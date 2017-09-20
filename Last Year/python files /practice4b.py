# take a 4-digit number, add first 2 to last 2, square, find if it = original
#MZ
# October 2016

def main():
    for i in range(1000,10000):
    ##        first2=i/100
    ##        last2=i % 100
    ## #       print first2,last2
    ##        sum=first2+last2
    ##        sumsq=sum**2
    ## #       print sumsq
    ##        if sumsq==i:
    ##             print i

        stri=str(i)
        first2=stri[0:2]
        last2=stri[2:4]
        first2=int(first2)
        last2=int(last2)
        sum=first2+last2
        sumsq=sum**2
    ## #       print sumsq
        if sumsq==i:
            print i


main()
