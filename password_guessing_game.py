import time
password = "divya123"
tries = 3

print("<<-- Welcome To Password Guessing Game -->>")
time.sleep(1)

while tries > 0:
    guess = input("guess the password :")
    if guess == password:
        print("~ ~ congratualtions ! you guessed it right!")
        break
    else:
        tries -= 1
        print(f"wrong password ! you have {tries} tries left")
        time.sleep(1)
if tries == 0:
    print("game over ! you couldn't guess the password")
    print(f"the correct password was : {password}")
