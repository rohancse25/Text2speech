from gtts import gTTS
print("**********************************************WELCOME TO TEXT TO SPEECH MODULE********************************")
print("\nENTER YOUR CHOISE")
print("1.Enter your text")
print("2.Import .txt file")
print("3.Exit")
while 1:
	n=int(input())
	if n==3:
		break
	elif n==1:
		print("\nEnter you text")
		st=input()
		tts=gTTS(text=st, lang="en", slow=False)
		tts.save(r"C:\Users\ROHAN VERMA\Documents\output.mp3")
		print("done!")
	elif n==2:
		print("Enter file url")
		url=input()
		f1=open(url,"r")
		k=f1.read()
		tts=gTTS(text=k, lang="en", slow=False)
		tts.save(r"C:\Users\ROHAN VERMA\Documents\output.mp3")
		f1.close()
		print("done!")
	else:
		print("Enter valid choice")
