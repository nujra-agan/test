{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 x = int(input('Enter the size of array: '))\par
arr = []\par
for i in range(x):\par
    arr.append(int(input('enter the values')))\par
print("the given list is ",arr)\par
highest = arr[0]\par
highest_index = 0\par
for i in range(0, x):\par
    if arr[i] > highest :\par
        highest = arr[i]\par
        highest_index = i\par
print("the highest values : " ,highest)\par
print("the position of the highest value is : " ,highest_index+1)   \par
lowest = arr[0]\par
lowest_index = 0\par
for i in range(0, x):\par
    if arr[i] < lowest :\par
        lowest = arr[i]\par
        lowest_index = i\par
print("the lowest values : " ,lowest)\par
print("the position of the lowest value is : " ,lowest_index+1)      \par
}
 