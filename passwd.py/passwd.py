import random
import pyautogui
import time

startTime = time.time()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!'
ch_list = list(chars)
password = pyautogui.password('Enter your password: ')
guess = ''
while password != str(guess):
    guess = random.choices(ch_list, k=len(password))
    print('Guess = '+ str(guess))
    
endTime = time.time()
elapsedTime = startTime - endTime
print ('The password is: ' + ''.join(guess))
print ('that took: ' + elapsedTime + 'seconds.')