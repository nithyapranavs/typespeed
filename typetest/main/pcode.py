import time
import getkey
import random
with open("word.txt") as file:
    words = file.read().split("|")

#to generate the text
print("type the below text")
text = ""
for i in range(30):
    text += random.choice(words) + ' '
    if i == 14:
        text += '\n'
print(text)
print()

#getting the input
first_key = getkey.getkey()
start_time = time.time()
typed = first_key + input(first_key)
end_time = time.time()
time_taken = end_time - start_time
print()

text = text.split()
typed = typed.split()
texts = []
#remove \n in text
for i in text:
    texts.append(i.rstrip('\n'))

#checking length
def check():
    if len(typed) < len(texts):
        print("You have not completed the test properly")
    if len(typed) > len(texts):
        l = len(texts)
        del typed[l::]
if len(typed) != len(texts):
    check()


#calculate correct words
no_wrds = len(texts)
error_wrd = 0
for i in range(no_wrds):
    if typed[i] != texts[i]:
        typ_wrd = list(typed[i])
        txt_wrd = list(texts[i])
        c = 0
        txt_len = len(txt_wrd)
        for j in range(len(typ_wrd)):
            if typ_wrd[j] != txt_wrd[j]:
                c += 1
                if c>= (txt_len/2):
                    error_wrd += 1
                    break
crt_wrd = float(no_wrds - error_wrd)

#calculating speed
speed = (crt_wrd/time_taken) * 60
print("speed : ",speed,"wpm")
print()
print("number of error words : ",error_wrd)
