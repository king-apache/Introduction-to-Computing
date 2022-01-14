#question1

print('Enter num 1')
num1 = int(input())
print('Enter num 2')
num2 = int(input())
print('Enter num 3')
num3 = int(input())


avg = (num1 + num2 + num3)/3

print ('The average is ' , avg)




#question2


print('Enter your Gross Income')
gross = int(input())
print('Enter the number of Dependants')
dep = int(input())

inc = gross - 10000 - (dep * 3000)
tax = inc*(0.2)

print('Tax = ', tax)




#question3

list = []

print('Enter SID')
SID = int(input())
list.append(SID)

print('Enter Name')
name = input()
list.append(name)

print('Enter Course Name')
course = input()
list.append(course)

print('Enter Gender')
gender = input()
list.append(gender)

print('Enter CGPA')
gpa = float(input())
list.append(gpa)
print(list)



#question4

print('Enter 5 numbers')
list = []

for i in range(0,5):
   num = int(input())
   list.append(num)

list.sort()
print(list)




#question5

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color.pop(3)
print(color)


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] #method1

in1 = color.index('Black')
in2 = color.index('Pink')

color.remove('Black')
color.remove('Pink')

color.insert(in1 , 'Purple')
color.insert(in2 , 'Purple')
print(color)


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] #method2
color[3:5]=['Purple']
print(color)
  