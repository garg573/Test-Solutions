num = input('Enter yout number: ')
#taking number as a string

if(len(num)<8 or len(num)>8):
    print('Invalid Input')
else:
    n1 = num[0:2]
    n2 = num[2:4]
    n3 = num[4:6]
    n4 = num[6:8]

    n1  = int(n1, 16)
    n2  = int(n2, 16)
    n3  = int(n3, 16)
    n4  = int(n4, 16)

    print(str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4))
    if(n1>0 and n1<=126 and n2<=255 and n3<=255 and n4<=255):
        print("A")
    elif(n1==127 and n2==0 and n3==0 and n4==0):
        print("A")
    elif (n1>=128 and n1<=190 and n2<=255 and n3<=255 and n4<=255):
        print("B")
    elif (n1==191 and n2<=255 and n3==0 and n4 ==0):
        print("B")
    elif (n1>=192 and n1<=222 and n2<=255 and n3<=255 and n4 <=255):
        print("C")
    elif (n1==223 and n2<=255 and n3<=255 and n4 ==0):
        print("C")
    elif (n1>=224 and n1<=239 and n2<=255 and n3<=255 and n4 <=255):
        print("D")
    elif (n1>=240 and n1<=255 and n2<=255 and n3<=255 and n4 <=255):
        print("E")


    
