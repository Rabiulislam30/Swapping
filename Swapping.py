#Python program to swap two variables

x = 5
y = 10

#Take two inputs
x = input('Enter value of x: ')
y = input('Enter value of y: ')

#Create a temporary variable and swap the values

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
