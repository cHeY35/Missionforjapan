#! /usr/bin/python -tt
import sys
entry = []
le = 0
sum = 0
s = []
su = 0

def repeat():
	entry = raw_input("")
	if len(entry) >= 2:
		le = len(entry)
		repeats(le, entry, sum)
		repeat()
		
	elif len(entry) == 1:
		repeat()
	else :	
		length = len(s)
		repeatss(length, s[::-1])
		return

def repeats(l, en, su):

	if  str(en[l-2]).isdigit() == False and str(en[l-2]).isspace() == False:
		repeats(l-3, en, su) 

	else:
		su = (int(en[l-1])*int(en[l-1])) + su
		if l-2 >= 0:
			repeats(l-2, en, su)
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
