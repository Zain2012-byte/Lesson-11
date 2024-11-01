num= int(input('Enter your first value:'))
sum=0
temp= num
while temp>0:
     digit=temp%10             #getting the last digit of a number
     sum= sum+ digit**3        #getting the power of 3
     temp= temp//10

if num==sum:
     print(num,"It's  an Armstrong number")
else:
     print(num,"It's not an Armstrong number")
     
     