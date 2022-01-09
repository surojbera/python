
'''Python Program to convert a number (Upto NINE digit) into its corresponding word. ---- By Suroj Bera'''
import sys

#Initializing some lists
single_digits=['zero','one','two','three','four','five','six','seven','eight','nine']
two_digits=['ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens_multiple=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
tens_power=['hundred','thousand','lakh','crore']


#num=int(input('Enter the number: '))        #Taking Input
num=sys.argv[1]
num_digit_list=[int(x) for x in str(num)]   #Storing the digits of the number in a list
num_digit_list.reverse()                    #Reversing the list
length=len(num_digit_list)                  #Finding length of the list

def single_digit_number(list1):             #Method for single digit number
    print(single_digits[list1[0]],end=' ')


def two_digit_number(list2):                #Method for double digit number
    temp_list=list2[0:2]
    if temp_list[1]==1:                         #For numbers from 10 to 19
        print(two_digits[temp_list[0]],end=' ')
    elif temp_list[1]>1 and temp_list[0]==0:    #For numbers like 10, 20,30,40,....,90
        print(tens_multiple[temp_list[1]],end=' ')  
    elif temp_list[1]>1 and temp_list[0]>0:         #For other two digit numbers like 57,66,98.. etc
        print(tens_multiple[temp_list[1]]+' '+single_digits[temp_list[0]],end=' ')
    elif temp_list[1]==0 and temp_list[0]>0:        #For numbers like 05,06,07,08.. etc when used with higher digit numbers. Example - 34506
        print(single_digits[temp_list[0]],end=' ')


def three_digit_number(list3):             #Method for three digit number        
    temp_list1=list3[2:]
    temp_list2=list3[0:2]
    if temp_list1[0]!=0:                   #For defining the WORD before hundred
        print(single_digits[temp_list1[0]]+' '+tens_power[0],end=' ')
    if temp_list2[0]==0:                   #For numbers like 360,350,680.. etc
        print(tens_multiple[temp_list2[1]],end=' ')
    else:                                  #For other three digit numbers
        two_digit_number(temp_list2)


def four_or_five_digit_number(list4_5):     #Method for four and five digit number
    temp_list1=list4_5[3:]
    temp_list2=list4_5[0:3]
    flag=0
    if len(temp_list1)==1 and temp_list1[0]!=0:     #Checking and defining the WORD before thousand for four digit numbers
        single_digit_number(temp_list1)
        print(tens_power[1],end=' ')
    else:                                           #Checking and defining the WORD before thousand for five digit numbers
        if temp_list1[0]==0 and temp_list1[1]==0:   
            flag =1
        if flag==0:                                 #For numbers like 01006,60005,00007..etc when used with higher digit numbers. Example - 201006,260005,200007
            two_digit_number(temp_list1)
            print(tens_power[1],end=' ')
    three_digit_number(temp_list2)                  #Defining WORD for last three digit of the original number


def six_or_seven_digit_number(list6_7):     #Method for six and seven digit number
    temp_list1=list6_7[5:]
    temp_list2=list6_7[0:5]
    flag=0
    if len(temp_list1)==1 and temp_list1[0]!=0: #Checking and defining the WORD before lakh for six digit numbers
        single_digit_number(temp_list1)
        print(tens_power[2],end=' ')
    else:                                       #Checking and defining the WORD before lakh for seven digit numbers
        if temp_list1[0]==0 and temp_list1[1]==0:
            flag =1
        if flag==0:                         #For numbers like 0100006,6000005,0000007..etc when used with higher digit numbers. Example - 20001006,26000005,20000007
            two_digit_number(temp_list1)
            print(tens_power[2],end=' ')
    four_or_five_digit_number(temp_list2)   #Defining WORD for last five digit of the original number


def eight_or_nine_digit_number(list8_9):    #Method for eight and nine digit number
    temp_list1=list8_9[7:]
    temp_list2=list8_9[0:7]
    flag=0
    if len(temp_list1)==1 and temp_list1[0]!=0: #Checking and defining the WORD before crore for eight digit numbers
        single_digit_number(temp_list1)
        print(tens_power[3],end=' ')
    else:                                       #Checking and defining the WORD before crore for nine digit numbers
        if temp_list1[0]==0 and temp_list1[1]==0:
            flag =1
        if flag==0: #For numbers like 0100006,6000005,0000007..etc when used with higher digit numbers. Example - 2000001006,2600000005,2000000007
            two_digit_number(temp_list1)
            print(tens_power[3],end=' ')
    six_or_seven_digit_number(temp_list2)   #Defining WORD for last seven digit of the original number

#def more_than_nine_digit_number(list_9):           #We may define the logic for any number whose length is more than NINE
    
if length==0:   #Checking whether user has enter any or not
    print('You have not entered any number. Please enter a number and try again.')
else:           #Checking the length of the given number
    if length ==1:
        single_digit_number(num_digit_list)
    elif length==2:
        two_digit_number(num_digit_list)
    elif length==3:
        three_digit_number(num_digit_list)
    elif length==4 or length==5:
        four_or_five_digit_number(num_digit_list)
    elif length==6 or length==7:
        six_or_seven_digit_number(num_digit_list)
    elif length==8 or length==9:
        eight_or_nine_digit_number(num_digit_list)
