import random
import pyautogui
import time

startTime = time.time()

chars = 'abcdefghijklmnopqrstuvwxyz'
ch_list = list(chars)
password = pyautogui.password('Enter your password: ')
guess = ''
while password != ''.join(guess):
    guess = random.choices(ch_list, k=len(password))
    print('Guess = '+ str(guess))
    
endTime = time.time()
elapsedTime = endTime - startTime
print ('The password is: ' + ''.join(guess))
print (f'that took: {elapsedTime} seconds.')