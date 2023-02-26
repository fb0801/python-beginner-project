from playsound import playsound
import time

CLEAR ="\033[2J"
CLEAR_AND_RETURN ="\033[H"


def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1) #wait 1 sec
        time_elapsed +=1

        time_left = seconds -time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm: {minutes_left:02d} : {seconds_left:02d}")
    playsound('sounds/FunnyMusic.mp3')


minutes =int(input("how long: "))
seconds = int(input("how long in seconds"))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)