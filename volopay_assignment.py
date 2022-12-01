# printing the airplane seating structure
def pr(mat,arr):
    n=len(mat)
    m=len(mat[0])
    j=0
    x=0
    for i in arr:
        x=max(x,i[0])
    while(True):
        for i in range(n):
            if arr[i][0]<=j:
                print(' '*(len(mat[i])+len(mat[i])-1),end=' ')
            else:
                print(mat[i][j],end=' ')
        j+=1
        print()
        if x<=j:
            break
    return 
def fun(arr,pas):
    n=len(arr)
    mat=[]

    for i in range(n):
        mat.append([[' ']*arr[i][1] for j in range(arr[i][0])]) #preparing matrix storing the answers for ith matrix[i]


    j=0  # used for maintaining the height so that we receive the correct passenger number.

    count=1   # counter for the number of passengers

    # working for aisle means that filling it one by one 
    x=0
    # x is flag for quiting the while loop when mat cant be filled for aisle loop_terminates(either ile places are finished or passenger are finshed)
    while(pas>0):
        f=0    # flag tells whether we have selected an aisle seat or not

        for i in range(n):
            if arr[i][0]<=j:            # checking for height condition
                continue

            # filling the empty aisle seats on the basis of order(left->right & then top->bottom)
            if i==0:                    
                if mat[i][j][-1]==' ':  
                    f=1
                    mat[i][j][-1]=count
                    break

            elif i==n-1:
                if mat[i][j][0]==' ':
                    f=1
                    mat[i][j][0]=count
                    break                   

            else:
                if mat[i][j][0]==' ':   
                    f=1
                    mat[i][j][0]=count
                    break
                if mat[i][j][-1]==' ':
                    f=1
                    mat[i][j][-1]=count
                    break              

        # if we cant find aisle seat 
        if f==0:
            if x==1:  # it confirms that there is no aisle seat and break from the loop
                break
            x+=1      # increasing the value of x denotes we didn't find aisle seat.
            j+=1      # else we increase the height 
            continue
        x=0            
        pas-=1    
        count+=1

    # working for window means that filling it one by one
    j=0
    x=0

    while(pas>0):

        f=0   
        if arr[0][0]>j and mat[0][j][0]==' ':
            f=1
            mat[0][j][0]=count
        elif arr[-1][0]>j and mat[-1][j][-1]==' ':  
            f=1
            mat[-1][j][-1]=count

        # found the window seat
        if f==1:
            pas-=1
            count+=1
            x=0            # it states that my previous call to find window seat was successful
            continue

        # didnt found the window seat
        if f==0:
            if x==1:     # confirms that we didnt find it again
                break
            x+=1
            j+=1


    # working for middle means that filling it one by one

    j=0
    while(pas>0):
        for i in range(n):
            if arr[i][0]<=j:
                continue

            new=mat[i][j]

            for k in range(len(new)):
                '''after filling the window and aisle seat we are checking the empty seats
                   and filling out the left over passengers as stated ''' 

                if pas>0 and mat[i][j][k]==' ':
                  mat[i][j][k]=count
                  count+=1
                  pas-=1

            if pas<=0:   # if all passengers are seated, then we break from the loop
                break
        j+=1

    # printing the airplane seating structure
    pr(mat,arr)

    return None

n = int(input("Enter the length of the 2D list: "))
arr = []
for i in range(n):
    arr.append(list(map(int, input("Enter the value of col and row: ").split()[::-1])))
pas =int(input("Enter the number of passengers: "))
fun(arr,pas)
