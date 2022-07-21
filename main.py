for i in range(5):
    for j in range(5):
        if(i==0 or i==3) or(j==4 or j==1):
            print("*",end=" ")
        print(" ",end=" ")
    print("")