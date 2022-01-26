#Question1

s = "Python is a case sensitive language"
print(len(s))
r = "Python is a case sensitive language"[::-1]
print(r)
c = slice(10,26)
print(s[c])
s2 = s
x = s2.replace("a case sensitive", "object oriented")
print(x)

t = s.find("a")
print(t)

s = ''.join(s.split())
print(f"'{s}'")


#Question2


print("Input name, SID, department name, CGPA")
name = input()
sid = input()
dept = input()
cgpa = int(input())

print(f"Hey, '{name}' Here! \n My SID is {sid} \n I am from {dept} department and my CGPA is {cgpa} ")



#Question3

a = 56
b = 10

print(a&b)
print(a|b)
print(a^b)

a << 2
b << 2
print(a,b)

a = 56
b = 10

a >> 2
b >> 4
print(a,b)



#Question4

print('Enter three sides')
s1 = int(input())
s2 = int(input())
s3 = int(input())


if s1>s2 and s1>s3:
 print(s1," is greatest")
if s2>s1 and s2>s3:
 print(s2," is greatest")
if s3>s1 and s3>s2:
 print(s3," is greatest")
 


#Question5

print("Enter string")
s = input()
t = s.find("name")

if t!= -1:
  print("True")


#Question6

print('Enter three sides')
s1 = int(input())
s2 = int(input())
s3 = int(input())


if (s1+s2) > s3:
   if (s2+s3) > s1:
      if (s1+s3) > s2:
         print("Yes")
      else:
        print("No")
   else:
     print("No")
else:
   print("No")