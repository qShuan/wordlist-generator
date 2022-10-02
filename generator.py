from itertools import permutations
import sys

#Make a list
keyword = []
keyword_rev = []

#howto
print('\n')
print("##### With special characters #####")
print("##### Type 'run' to run the program #####")
print('\n')

#Add words to the list
for x in range(0, 1000):
	keyword.append(input("VALUE: "))
	if keyword[x] == "run":
		keyword.remove(keyword[x])
		print('\n')
		break
		

#Reverse keywords
for x in range(0, len(keyword)):

	#Don't reverse special characters to avoid duplicates
	match keyword[x]:
		case '!':
			print("##### ! - Not reversing to avoid duplicates #####")
		case '@':
			print("##### @ - Not reversing to avoid duplicates #####")
		case '#':
			print("##### # - Not reversing to avoid duplicates #####")
		case '$':
			print("##### $ - Not reversing to avoid duplicates #####")
		case '%':
			print("##### % - Not reversing to avoid duplicates #####")
		case '^':
			print("##### ^ - Not reversing to avoid duplicates #####")
		case '&':
			print("##### & - Not reversing to avoid duplicates #####")
		case '*':
			print("##### * - Not reversing to avoid duplicates #####")
		case '(':
			print("##### ( - Not reversing to avoid duplicates #####")
		case ')':
			print("##### ) - Not reversing to avoid duplicates #####")
		case '-':
			print("##### - -- Not reversing to avoid duplicates #####")
		case '_':
			print("##### _ - Not reversing to avoid duplicates #####")
		case '[':
			print("##### [ - Not reversing to avoid duplicates #####")
		case ']':
			print("##### ] - Not reversing to avoid duplicates #####")
		case '{':
			print("##### { - Not reversing to avoid duplicates #####")
		case '}':
			print("##### } - Not reversing to avoid duplicates #####")
		case ';':
			print("##### ; - Not reversing to avoid duplicates #####")
		case ':':
			print("##### : - Not reversing to avoid duplicates #####")
		case '<':
			print("##### < - Not reversing to avoid duplicates #####")
		case '>':
			print("##### > - Not reversing to avoid duplicates #####")	
		case '?':
			print("##### ? - Not reversing to avoid duplicates #####")
		case '/':
			print("##### / - Not reversing to avoid duplicates #####")
		case '\\':
			print("##### \\ - Not reversing to avoid duplicates #####")
		case '|':
			print("##### | - Not reversing to avoid duplicates #####")
		case ',':
			print("##### , - Not reversing to avoid duplicates #####")
		case '.':
			print("##### . - Not reversing to avoid duplicates #####")
		case '"':
			print("##### Not reversing to avoid duplicates #####")
		case "'":
			print("##### Not reversing to avoid duplicates #####")
		case '=':
			print("##### = - Not reversing to avoid duplicates #####")
		case '+':
			print("##### + - Not reversing to avoid duplicates #####")
		case '`':
			print("##### ` - Not reversing to avoid duplicates #####")
		case '~':
			print("##### ~ - Not reversing to avoid duplicates #####")
		case _:
			keyword_rev.append(keyword[x][::-1])
	

run = False

while(run != True):
	#Add reversed keywords to the list
	for x in range(0, len(keyword_rev)):
		keyword.append(keyword_rev[x])

	#Print all
	for x in range(0, len(keyword)):
		print("============= KEYWORDS: " + keyword[x] + " =============")
		print('\n')
	
	inp = input("Do you want to generate with these keywords (y/n): ")
	if inp == 'y':
		run = True
	if inp == 'n':
		print("Closing...")
		sys.exit()
		

#Make combinations
for i in range(0, len(keyword) + 1):
	for group in permutations(keyword, i):
     		print(''.join(group))
