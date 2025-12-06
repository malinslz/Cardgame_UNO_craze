# Our Physical Computing project
"UNO Craze" is an enhanced version of the classic UNO game, supplemented by an interactive box. 
This box uses sensors, colour displays and other visual effects to respond to specific cards and game situations. 
This makes the gaming experience more dynamic, exciting and interactive.

## Concept
### How to play
New Features
This version of UNO includes two new universal cards and an interactive electronic box that adds extra variety to the game.

The New Cards:
Both cards are universal, meaning they can be played on any color.

- Switch (Card Swap)
When the B1 button on the box is pressed, the display shows arrows indicating the direction (left or right) in which all players must pass their entire hand.

- Touch It! (Reaction Card)
When one of the four sensors on the box is pressed, the box detects which player reacted fastest. The fastest player is shown on the display and may discard one card as a reward.

Note: These special cards only take effect when a player places them on the discard pile.

Starting the Game:
The starting player turns on the box using the On-button. The display shows the starting color for the game. 

If You Don’t Have the Required Color:
If it's your turn and you don’t have a card of the required color, press the red buzzer. 

The box will display:
- How many cards you must draw (1–4), and Which color will be played next.
- If you also don’t have the newly displayed color, draw from the normal draw pile as usual and end your turn.


The UNO Craze Box – Interactive Elements:
Buzzer: Activates Screen 1.

Screen 1: Shows how many cards to draw (1–4) and the next color (red, blue, green, yellow).

Button B1: Activates Screen 2.

Screen 2: Shows the direction for passing hands (left or right) — used for the Switch card.

On/Off Button: Turns the box on or off.

4 Distance Sensors: Detect who reacts the fastest — used for the Touch It! reaction card.


Other Rules:
All regular UNO rules remain unchanged. Cards drawn due to +2 or +4 effects are still taken from the normal draw pile, not from the box.


## Requirements
To build this project you will need:
- UNO-Craze Box
- UNO-Cards (+ SpecialCards)
- The Modulino Hardware

### Hardware
* [An Arduino Nano ESP32](https://store.arduino.cc/products/nano-esp32-with-headers)
* A Grove RGB LCD Display 16x2
* A Grove LCD Dislpay 16x2
* 4x Distance Sensors
* 1x Modulino Buzzer
* 1x Modulino Buttons
* 1x Button Buzzer
* A USB-C power bank
  
### Software
* [MicroPython](https://micropython.org/)
* [Arduino Lab for MicroPython](https://labs.arduino.cc/en/labs/micropython)
* [Arduino MicroPython Installer](https://labs.arduino.cc/en/labs/micropython-installer)

### Libraries
* [MicroPython-Button](https://github.com/ubidefeo/MicroPython-Button)
* [MicroPython I2C 16x2 LCD driver](https://github.com/ubidefeo/micropython-i2c-lcd)

## How to build
### Wiring
see the Document: "UNO-Craze_Spielregeln and How to build" ;)

for the UNO-Craze Cube see: "Cube.stl"

### Uploading the code
* Copy the content of your `src` from your computer to your board
* Install the libraries listed above
  
### Feedback and questions
If you are interested in this project and need to ask questions get in touch with us over our emails:
* leandra.gati@ost.ch
* malin.sulzberger@ost.ch
* peter.rachinsky@ost.ch
