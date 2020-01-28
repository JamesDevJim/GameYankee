import serial
import time
import pyfirmata
import pygame

#BUTTON CONSTANTS
BUTTON_START = 1
BUTTON_RESET = 1
BUTTON_BLUE = 1
BUTTON_YELLOW = 1
BUTTON_DOWN = 1
BUTTON_UP = 1
BUTTON_LEFT = 1
BUTTON_RIGHT = 1


#Game premise: Buttons that are lit are lava. You Touch, you fail. LIGHT_1 & LIGHT_2 indicate which button you need to push. LIGHT_3 indicates special condition.


#PREGAME
    # PLAY introMusic
    # DISPLAY gray circle
    # Moves to case 2 is start button is pushed
    # LIGHT_GREEN is blinking

# INITGAMEPLAY
    # PLAY gamePlayMusic
    # DISPLAY green circle
    # LIGHT_GREEN ON
    # BUTTON_ALL activate
    # BUTTON_UP and BUTTON_DOWN deactivated. 
    # move to Gate 1

#GAME CONTROL
    # One button light is always lit. Either LIGHT_BLUE or LIGHT_YELLOW
    # BUTTON_LEFT moves light left
    # BUTTON_RIGHT moves light right
    # IF two lights (on last gate) then activate BUTTON_UP and BUTTON_DOWN
        # BUTTON_DOWN or BUTTON UP moves both LIGHT_BLUE and LIGHT_YELLOW OFF 
    # if Buttons are deactived play rejection sound. 
    # Gate Timer = 20 secs. 20 seconds for each gate. i.e., timer resets onces new gate is reached

#GATE 1
    # LIGHT_1 ON (indicating BUTTON_BLUE is the correct choice)
    # LIGHT_YELLOW ON
    # LIGHT_BLUE OFF
    # BUTTON_UP and BUTTON_DOWN deactivated.
    # if push BUTTON_YELLOW then Fail
    # if push BUTTON_BLUE then procceed to gate 2

#GATE 2    
    # LIGHT_3 ON (Indicating BUTTON_YELLOW is the correct choice)
    # LIGHT_YELLOW ON
    # LIGHT_BLUE OFF
    # BUTTON_UP and BUTTON_DOWN deactivated.
    # Must move light to the right with butRight
    # if push BUTTON_YELLOW (with light) then Fail
    # if push BUTTON_BLUE (without light) then procceed to gate 3

#GATE 4
    # LIGHT_3 ON (Indicating BUTTON_YELLOW is the correct choice)
    # LIGHT_YELLOW ON
    # LIGHT_BLUE OFF
    # Must move light to the right with butRight
    # if push BUTTON_YELLOW (with light) then Fail
    # if push BUTTON_BLUE (without light) then procceed to gate 4

#GATE 5
    # BUTTON_UP and BUTTON_DOWN activated. 
    # BUTTON_Left and BUTTON_RIGHT deactivated.
    # LIGHT_2 ON (Indicating no button is correct. BUTTON_YELLOW is the correct choice)
    # LIGHT_YELLOW OFF
    # LIGHT_BLUE OFF
    # Must move lava back to buttons.
    # IF Button_UP or BUTTON_DOWN is activated.
        # Then LIGHT_1 ON and LIGHT_BLUE ON and BUTTON_Left and BUTTON_RIGHT activated.
    # Must move lava right
    # if push BUTTON_YELLOW (with light) then Fail
    # if push BUTTON_BLUE (without light) then SUCCESS

#GAMEFAIL
    # BUTTON_ALL deactivate (except for restart)
    # PLAY fail sound
    # DISPLAY red circle
    # Wait for player to hit restart
        #then go to PREGAME

#GAMESUCCESS
    # BUTTON_ALL deactivate (except for restart)
    # LIGHT_GREEN Fade_on and off
    # Play win sound
    # DISPLAY Green circle fade in and out
    # Activate badge collection #TODO: Will code badge collection at a later date. 
    # Wait for player to hit restart
        #then go to PREGAME




