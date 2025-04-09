from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)


left_score = 0
right_score = 0


left_name = input("Enter left player's name: ")
right_name = input("Enter right player's name: ")

def pressed(button):

    global led_on_time, left_score, right_score


    reaction_time = round(time() - led_on_time, 3)

    if button.pin.number == 14:
        print(f"{left_name} pressed the button in {reaction_time} seconds!")
        left_score += 1
    else:
        print(f"{right_name} pressed the button in {reaction_time} seconds!")
        right_score += 1


    led.off()


    print(f"Current Scores: {left_name}: {left_score}, {right_name}: {right_score}")
    sleep(1)

left_button.when_pressed = pressed
right_button.when_pressed = pressed

print("Game starts now!")

rounds = int(input("Enter number of rounds to play: "))
for round_num in range(1, rounds + 1):
    print(f"Round {round_num} of {rounds}")

    sleep(uniform(2, 5))
    led.on()
    led_on_time = time() 

print("Game Over!")
print(f"Final Scores: {left_name}: {left_score}, {right_name}: {right_score}")
