#Q1

print("Enter String")
txt = input()

def instances(txt, word):
     
    a = txt.split(" ")
 
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
           count = count + 1
            
    return count 

x = txt.split()

for i in range (len(x)):
    print(x[i], ":", instances(txt,x[i]))


#Q2

print("Input Date")
d = int(input())
print("Input Month")
m = int(input())
print("Input Year")
y = int(input())

if m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
   if d == 31:
      d = 1
      m = m + 1
   if m == 12:
      d = 1
      m = 1
      y = y + 1


if m == 2 and (m % 12 == 0):
   if d == 28:
      d = 1
      m = 3
   else:
      d = d+1

if d == 31 and m == 12:
    d = 1
    m = 1
    y = y + 1

print("The date is " ,d,"/" ,m,"/" ,y,"/") 


#Q3

print("enter length of the list")
r = int(input())
a = []

for i in range(0,r)
  l[i] = input()

a=[(l[x],l[x]**2) for x in range(0,4)]
print(a)
print(t)


#Q4

print("Enter grade")
g = int(input())

if g>=4 and g<=10:
  if g == 10:
     print("Your Grade is A+ and Outstanding Performance")
  if g == 9:
     print("Your Grade is A and Excellent Performance")
  if g == 8:
     print("Your Grade is B+ and Very Good Performance")
  if g == 7:
     print("Your Grade is B and Good Performance")
  if g == 6:
     print("Your Grade is C+ and Average Performance")
  if g == 5:
     print("Your Grade is C and Below Average Performance")
  if g == 4:
     print("Your Grade is D and Poor Performance")


#Q5

for star in range(11,0,-2):
  t = int((11-star)/2)
  print( t * ' ' , end = "")
  for alpha in range(65,65+star):
     print(chr(alpha), end = "" )
     
  print("\n")


#Q6


dic = {}
c = 'Y'
while c == 'Y':
   print("Enter SID")
   SID = input()
   print("Enter name")
   name = input()
   
   dic[SID] = name
   
   print("Do you wish to continue")
   c = input()

dic2=dic.copy()
dic3=dic.copy()
dic4=dic.copy()

#a
print(dic)

#b
sortd = sorted(dic.items(), key=operator.itemgetter(1))
print(sortd)

#c
items = dic2.items()
sorti = sorted(items)
print(sorti)

#d
print("Enter SID to search")
s = input()
print(dic2.get(s))



#Q7  

print("Enter number of terms")
t = int(input())

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

if t <= 0:
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(t):
       x = x + fibo(i))
       print(fibo(i))
       

#Q8

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

# a.

setU = set.union(set1,set2)
print(setU)

#b

diff = set.difference(set1,set2)
Diff = set.diiference(diff,set3)
print(Diff)


#d

set10 = {1,2,3,4,5,6,7,8,9,10}
diff10 = set.difference(set10,set1)
print(diff10)


#e

SET = set.union(setU,set3)
diffSET = set.difference(SET,set10)
setf = set.intersection(diffSET,set10)
print(setf)
   
    

   
   
  






