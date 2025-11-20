from gpiozero import LED
from gpiozero import Button

# Initialize LED connected to GPIO pin 0
led = LED(0)
# Initialize button connected to GPIO pin 1
button = Button(1)

while True:
    if button.is_pressed:
        #Turn on LED when button is pressed
        led.on()
        print("Button is pressed")
    else:
        #Turn off LED when button is not pressed
        led.off()
        print("Button is not pressed")
