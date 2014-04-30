#! /usr/bin/python -tt
import sys
entry = ' '
le = 0
sum = 0
s = []
su = 0
e = []
def repeat():
	entry = raw_input("")

	if len(entry) >= 3:
		e = entry.split(' ')
		le = len(e)
		repeats(le-1, e, sum)
		repeat()
		
	elif len(entry) == 1:
		repeat()
		
	else :	
		length = len(s)
		repeatss(length, s[::-1])
		return

def repeats(l, en, su):

	if  str(en[l]).isdigit() == False :
		repeats(l-1, en, su)
		
	else:
		su = (int(en[l])*int(en[l])) + su
		if l-1 >= 0:
			repeats(l-1, en, su)
		
		else:
			s.append(su)	
			return

def repeatss(leng, s1):
	
	if leng > 0:
		print s1[leng-1]
		leng = leng - 1
		repeatss(leng, s1)
	else:
		return
def main(): 
	repeat()
	

if __name__=='__main__':
	main()
