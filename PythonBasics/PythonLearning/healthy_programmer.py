# Exercise 7
import pygame
import time

pygame.init()
pygame.mixer.init()


def play_audio(audio_name, log_file, work_name, stop_command):
    pygame.mixer.music.load("water.mp3")
    pygame.mixer.music.play()
    # sound_obj = pygame.mixer.Sound(audio_name)
    # sound_obj.play()
    command = input(f"Time to {work_name}.\n\nType \"{stop_command}\" when you are finished: ")
    while command != stop_command:
        command = input(f"Wrong command entered.\nPlease enter \"{stop_command}\" if you are finished with the {work_name}: ")

    pygame.mixer.music.stop()

    def log(file_name, log_name):
        with open(file_name, "a") as logfile:
            curr_time = time.asctime(time.localtime(time.time()))
            logfile.write(f"[{curr_time}] -->> {log_name}")

    log(log_file, work_name)
    print(f"{work_name} has been logged in the {log_file}. You can resume your work. Happy Coding!!")


required_start_command = "begin"
log_file_name = "FileWork/healthy_programmer.txt"
start_command = input("Type \"begin\" when you start working: ")

while start_command != required_start_command:
    start_command = input("Wrong input. Type \"begin\" when you start working: ")

play_audio("water.mp3", log_file_name, "Drink Water", "Drank")
