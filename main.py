import array as np 
def menu():
  print('________________________________________________')
  print('-------------PRIME NUMBER FINDER----------------')
  print('________________________________________________')
  print('------------------MAIN MENU---------------------')
  print('1.FOR LOOP')
  print('2.WHILE LOOP')
  print('3.EXIT')
  print('________________________________________________')
  
def numinput(num): #error handling when user inputs string
  try:
     int(num)
     return True
  except:
    return False

def posinput(num): #error handling when the user inputs negative number
  if num>0:
    return True
  else:
    return False

    
def for_loop():  
  print('========================')
  print('EXECUTION OF FOR LOOP')
  print('========================')
  array=np.array('i')
  n=(input('How many numbers do you want to input?:'))
  while (True):#handling error
      if numinput(n):
          break
      else:
          print('ERROR! INVALID INPUT')
          n=input('How many numbers do you want to input?:')
  n=int(n)
  while True: #handling error
      if posinput(n):
          break
      else:
          print('ERROR! You entered a negative number')
          n=int(input('Please enter how many numbers you want to input:'))
      
  for a in range(1,n+1):
    x=(input('Enter a number:'))
    while (True): #handling error
         if numinput(x):
            break
         else:
           print('ERROR!')
           x=(input('please enter a valid number:'))
    x=int(x)
    while(True): #handling error
        if (posinput(x)):
            break
        else:
            print("ERROR!, You entered a negative number ")
            x=int(input('PLEASE ENTER A POSITIVE NUMBER:'))
            
    #prime numbers
    if x>1:
   # check for factors
      for i in range(2,x):
          if (x % i) == 0:
            break
      else:
          if x in array:
              print('Number already entered')
            
          else:
            array.append(x)
          
    else:
        print('1 is not a prime number')
 
  calc(array)
  return array
          
def calc(array):
  largest=0
  smallest=0
  for i in range(len(array)):
    if array[i]>largest:
      largest=array[i]
    if array[i]<smallest or smallest==0:
      smallest=array[i]
  Difference=largest-smallest
  
  if largest>0 and smallest>0:
      print('Prime numbers entered are:')
      for i in range(len(array)):
          print(array[i])
      
      print('Differene is',Difference)
  else:
      print('No prime numbers entered')

  
  
def while_loop():
    print('========================')
    print('EXECUTION OF WHILE LOOP')
    print('========================')
    array=np.array('i')
    b=input("Let's start yes/no:")

    while True:
       if b =='yes' or b=='no':
         break
       else:
         print('VALUE ERROR')
         b=input('Please enter yes/no:')
         
    while b=='yes':
      z=(input('Enter a number:'))
         
      while True:
          if numinput(z):
              break
          else:
              print('ERROR!')
              z=input('Enter enter a valid number:')

      z=int(z)
      while True:
          if posinput(z):
              break
          else:
              print('ERROR! You entered a negative number')
              z=int(input('Enter a positive number:'))
              

      
      if z>1:
            for i in range(2,z):
                   if (z % i) == 0:
                     break
            
            else:
                 if z in array:
                     print('Number already entered')
                 else:
                   array.append(z)  
                
                    
            b=input('Do you want to continue:')
                    
            while True:
               if b =='yes' or b=='no':
                 break
               else:
                 print('VALUE ERROR')
                 b=input('Please enter yes/no:')
            if b=='no':
                break
            
      else:
        print('1 is not a prime number')
           
    calc(array)
          
         #------------------------main body-----------------------------

while True:
    menu()      
    a=(input('Please choose an option 1-3:'))
    while True:
        if numinput(a):
            break
        else:
            print('ERROR! INVALID INPUT')
            a=(input('Please enter an option 1-3:'))
    a=int(a)
    if a==1:
      for_loop()
    elif a==2:
      while_loop()
    elif a==3:
      print("You've exited the program!")
      break
    else:
        print('Invalid option')