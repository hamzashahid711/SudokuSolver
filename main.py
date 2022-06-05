import colorama
import sys
import time
from colorama import Fore
global array1 
global array2 
global array3 
global array4 
global array5 
global array6 
global array7 
global count 
global array8
global array9 
global list
global beginx
global beginy
global x 
global y
class number:
  def __init__(self, value,given,row,col):
    self.value = value
    self.given = given
    self.row= row
    self.col = col


test1 = number(1, False,0,0)
test2 = number(2, False,0,0)
test3 = number(3, False,0,0)
test4 = number(4, False,0,0)
test5 = number(5, False,0,0)
test6 = number(6, False,0,0)
test7 = number(7, False,0,0)
test8 = number(8, False,0,0)
test9 = number(9, False,0,0)
filler= number(0,False,0,0)
s = [
[filler, filler, filler, filler, filler, filler, filler, filler, filler],[filler, filler, filler, filler, filler, filler, filler, filler, filler],[filler, filler, filler, filler, filler, filler, filler, filler, filler], [filler, filler, filler, filler, filler, filler, filler, filler, filler], [filler, filler, filler, filler, filler, filler, filler, filler, filler],[filler, filler, filler, filler, filler, filler, filler, filler, filler], [filler, filler, filler, filler, filler, filler, filler, filler, filler], [filler, filler, filler, filler, filler, filler, filler, filler, filler],[filler, filler, filler, filler, filler, filler, filler, filler, filler]
]
def arrays():
	global array1
	global array2 
	global array3 
	global array4 
	global array5 
	global array6 
	global array7 
	global array8 
	global array9 
	array1= []
	array2= []
	array3= []
	array4= []
	array5= []
	array6= []
	array7= []
	array8= []
	array9= []
	x = 6
	y = 0
	for i in range(0,len(s)-x):
		for j in range(0,3):
			array1.append(s[i][j].value)
	for i in range(0,len(s)-x):
		for j in range(3,6):
			array2.append(s[i][j].value)
	for i in range(0,len(s)-x):
		for j in range(6,9):
			array3.append(s[i][j].value)
	for i in range(3,len(s)-3):
		for j in range(0,3):
			array4.append(s[i][j].value)
	for i in range(3,len(s)-3):
		for j in range(3,6):
			array5.append(s[i][j].value)
	for i in range(3,len(s)-3):
		for j in range(6,9):
			array6.append(s[i][j].value)
	for i in range(6,len(s)):
		for j in range(0,3):
			array7.append(s[i][j].value)
	for i in range(6,len(s)):
		for j in range(3,6):
			array8.append(s[i][j].value)
	for i in range(6,len(s)):
		for j in range(6,9):
			array9.append(s[i][j].value)

def checkArray(obj,value):
	if(obj.row <3 and obj.col <3):
		if(value in array1):
			return False
	if(obj.row < 3 and obj.col > 2 and  obj.col < 6):
		if(value in array2):
			return False
	if(obj.row < 3 and obj.col > 5 ):
		if(value in array3):
			return False
	if(obj.row > 2 and obj.row < 6 and obj.col < 3):
		if(value in array4):
			
			return False
	if(obj.row > 2 and obj.row < 6 and obj.col > 5):
			if(value in array6):
				return False 
	if(obj.row > 5 and obj.col < 3 ):
		if(value in array7):
			return False
	if(obj.row > 5 and obj.col > 2 and obj.col < 6):
		if(value in array8):
			return False
	if(obj.row > 5 and obj.col >5 ):
		if(value in array9):
			return False
	return True

def checkRules(obj, row, col, value):
	
	for i in range(row,row+1):
		for j in range(0, len(s[0])):
			if(s[i][j].value == value):			
				return False
	for i in s:
		if(i[col].row == obj.row and i[col].col == obj.col):
			continue
		if(i[col].value == value):
			return False
	
			
			
	if(checkArray(obj,value) == False):
		return False
	return True

def backTrack(row, col):

	global x,y
	x =0
	y =0
	s[row][col].value = 0
	if((col-1)%9 == 8):
		row = row -1
		if(row <= -1):
			row =0
	col = (col-1)%9

	if(s[row][col].given ):
		
		
	
		while(s[row][col].given):
			if((col-1)%9 == 8):
				row = row -1
				if(row <= -1):
					row =0
			col = (col-1)%9

	if(s[row][col].value==9):

		backTrack(row,col)
		return
	if(s[row][col].value < 9 and row != 0 and col != 3):
		for i in range(s[row][col].value,10):
			if(checkRules(s[row][col],row,col,i)):
				s[row][col].value = i
				s[row][col].row = row
				s[row][col].col = col
				if(col + 1> 8):
					row = row +1
				col =( col + 1 )%9
				x = row
				y = col
				break
			if(i == 9):
				backTrack(row,col)
				return
	else:
		for i in range(1,10):
			if(checkRules(s[row][col],row,col,i)):
				s[row][col].value = i
				s[row][col].row = row
				s[row][col].col = col
				if(col + 1> 8):
					row = row +1
				col =( col + 1 )%9
				x = row
				y = col
				break
	
def filled():
	coutn = 0
	for i in range(0,len(s[0])):
		for j in range(0,9):
			if(s[i][j].value >0):
				coutn = coutn + 1
	if(coutn == 76):
		return True
	return False
def solve():
	global x,y
	
	row = 0
	col = 0
	while(1):
		if(s[7][3].value >0):
			grid()
		if(filled() == True):
			break
		if(s[row][col].given == False):
			
			for i in range(1,10):
		
				if(checkRules(s[row][col], row, col, i)):
					s[row][col].value = i
					s[row][col].row = row
					s[row][col].col = col
					if(col + 1> 8):
						row = row +1
					col =( col + 1 )%9
					print("\n")
					grid()
					break
				if(i == 9 ):
			
					backTrack(row, col)
					if((col +1)%9 == 0):
						row= row +1
					col = (col +1)%9
					row = x
					col = y
		if(s[row][col].given):
			if(col + 1> 8):
				row = row +1
			col =( col + 1 )%9
					
		
def grid():
	count  = -1
	num =0
	print(Fore.RED,"a    b    c    d    e    f    g    h    i")
	for i in s:
		print("\n")
		count =-1
	

		for j in i:
			count = count +1
	
			if(count == len(i)-1):
				
				print(Fore.WHITE,j.value,"|", end = " ")
				print(Fore.RED,num,end = " ")
				count = 0
				num = num +1
			else:
				print(Fore.WHITE,j.value,"|", end = " ")


def user():
	thisdict = {
  	"a": 0,
  	"b": 1,
  	"c": 2,
  	"d": 3,
  	"e": 4,
  	"f": 5,
  	"g": 6,
  	"h": 7,
  	"i": 8
	}
	done = "Y"
	y= "0"
	x = "0"
	while(done != "N" and done != "n"):
		print("\n")
		y = input(" Enter in a letter a-i ")
		x = input(" Enter in a number 0-8 ")
		num = input(" Enter in the number ")
		y =thisdict[y]
		x= int(x)
		obj = number(num, True,x,y)
		s[x][y] = obj
		done = input(" Do you want to continue ? Y/N "  )


def easyBoard():
	array1 =[]
	array2 =[]
	array3 =[]
	array4 =[]
	array5 =[]
	array6 =[]
	array7 =[]
	array8 =[]
	array9 =[]
	array1 = [6,7,2,0,0,1,9,8,4]
	array2 = [0,3,1,0,0,0,0,0,0]
	array3 = [0,4,0,0,2,0,0,0,3]
	array4 = [4,0,5,0,0,0,3,0,8]
	array5 = [9,2,0,3,7,0,5,0,0]
	array6 = [7,6,0,0,0,0,0,2,0]
	array7 = [0,0,6,4,9,0,8,3,2]
	array8 = [3,0,4,0,0,0,0,4,5]
	array9 = [0,0,0,0,5,0,1,9,6]


	for i in range(0,1):
		for j in range(0,9):
			if(array1[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
				
			else:
				obj = number(array1[j], True, i , j)
				s[i][j] = obj
	for i in range(1,2):
		for j in range(0,9):
			if(array2[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array2[j], True, i , j)
				s[i][j] = obj
	for i in range(2,3):
		for j in range(0,9):
			if(array3[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array3[j], True, i , j)
				
				s[i][j] = obj
	for i in range(3,4):
		for j in range(0,9):
			if(array4[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array4[j], True, i , j)
				s[i][j] = obj
	for i in range(4,5):
		for j in range(0,9):
			if(array5[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array5[j], True, i , j)
				s[i][j] = obj
	for i in range(5,6):
		for j in range(0,9):
			if(array6[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array6[j], True, i , j)
				s[i][j] = obj
	for i in range(6,7):
		for j in range(0,9):
			if(array7[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array7[j], True, i , j)
				s[i][j] = obj
	for i in range(7,8):
		for j in range(0,9):
			if(array8[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array8[j], True, i , j)
				s[i][j] = obj
	for i in range(8,9):
		for j in range(0,9):
			if(array9[j] == 0 ):
				obj = number(0,False,i,j)
				s[i][j] = obj
			else:
				obj = number(array9[j], True, i , j)
				s[i][j] = obj
				
		
		
			
sys.setrecursionlimit(2000)
easyBoard()
arrays()
grid()
print("\n")
solve()
grid()

