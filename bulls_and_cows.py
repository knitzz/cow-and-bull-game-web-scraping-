import bs4 as bs
import urllib.request
import html.parser
import string
import random

chances=0
Four_letter_dictionary=[]
alphabet_list=list(string.ascii_lowercase[:])

'''
use this code to generate dictionary with all alphabets

# for i in range(0,len(alphabet_list)):

# 	u='https://www.morewords.com/unique-letters/4' + alphabet_list[i] + '/'
'''


u='https://www.morewords.com/unique-letters/4a/'
sauce=urllib.request.urlopen(u).read()

soup=bs.BeautifulSoup(sauce,'html.parser')

x=soup.div.find_all('p')
y=x[2]
word=y.find_all('a')




for w in word:
	Four_letter_dictionary.append(w.text)
	

random_word=random.choice(Four_letter_dictionary)
#print(random_word)

def cow_and_bull(w):
 	global chances
 	
 	chances= chances+ 1
 	j=0
 	cow=0
 	bull=0
 	for l in w:
 		if(random_word[0]==l ):
 			if(l==random_word[j]):
 				bull=bull+1
 			else:
 				cow=cow+1
 		if(random_word[1]==l ):
 			if(l==random_word[j]):
 				bull=bull+1
 			else:
 				cow=cow+1
 		if(random_word[2]==l ):
 			if(l==random_word[j]):
 				bull=bull+1
 			else:
 				cow=cow+1
 		if(random_word[3]==l ):
 			if(l==random_word[j]):
 				bull=bull+1
 			else:
 				cow=cow+1
 		j=j+1
 			
 	print("No. of bulls :" , bull)
 	print("no. of cows :" , cow)


 	if(bull==4):
 		print("you won")
		
 	else:
 		if(chances<10):
 			user_input()
 		else:
 			print("chances exceed , you lost")



def user_input():
		global chances
	
		print("enter your guess No.", chances+1)
		user_guess=input()
		user_guess=user_guess.lower()
		if(len(user_guess)!=4):
			print("wrong input , length string of string should be 4  \n")
			user_input()
		if(len(set(user_guess))!=len(user_guess)):
			print("wrong input , repeated letters")
			user_input()


		cow_and_bull(user_guess)
		

def start():
	start=int(input("type 1 to play :  "))
	if(start==1):
		user_input()





print("GAME: COW AND BULL")
print("BASIC RULES \n")
print("A word has been chosen by this program. It is a 4-letter meaningful word.\n You have 10 chances to guess that word.")
print("All of your guess must be 4-letter words with no letter repeated in a single word.")
print("No. of Bulls obtained after each guess denotes the no. of letters that exist in both your guess and the word to be guessed with identical position of occurrence.")
print("No. of Cows obtained after each guess denotes the no. of letters that exist in both your guess and the word to be guessed but with dissimilar positions.\n")

start()