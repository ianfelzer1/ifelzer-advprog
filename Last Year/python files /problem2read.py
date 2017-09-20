def main():
     b=["Hello","I","Am","Ian"]
     filename=raw_input("Filename:")
     f=open(filename,"w")
     for i in range (4):
          text="line "+str(i+1)+" : "
          linetext= text + b[i] + "\n"
          f.write(linetext)
     f.close()
    
main()



