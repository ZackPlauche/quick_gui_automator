import os 
from pyautogui import *
from time import sleep

# Utility Functions 

def pause():
    os.system('pause')

def validate_input(message, data_type, error_message):
    while True:
        user_input = input(message)
        if not user_input:
            break
        else:
            try:
                value = data_type(user_input)
                return value
            except:
                print(f'\n{error_message}\n')
                sleep(1)
    return ''

class Automation:
    coordinates = []
    seconds_between_clicks = 0
    coordinate_count = 1
    iterations = 1

    def find_coordinates(self, short=True):
        """Set which coordinates that the automation will take an action on
        (in order) by pressing Ctrl and C on the desired cursor position for
        the automation to take an action on."""

        # Print instructions
        print('INSTRUCTIONS: Make sure you\'re focused on this window, then press Ctrl + C when you\'re on the spot you want to click.')

        
        for i, coordinate in enumerate(range(self.coordinate_count)):
            displayMousePosition()
            x, y = position()
            self.coordinates.append((x, y))
            print(f'Coordinate saved ({i+1} of {self.coordinate_count}, {self.coordinate_count - (i+1)} remaining)')

    def set_coordinate_count(self, short=True):
        """Set the number of coordinates that will be available (if setting the coordinates manually)"""
        message = '# of coordinates: ' if short else 'How many coordinates do you need?'
        error_message = 'ERROR: Value must be a whole number, otherwise leave blank to use default (default=1)'
        if coordinate_count := validate_input(message, int, error_message):
            self.coordinate_count = coordinate_count

    def set_iterations(self, short=True):
        """Set the number of times the automation will take an action at each coordinate"""
        message = 'Iterations: ' if short else 'How many times would you like this automation to iterate?: '
        error_message = 'ERROR: Value must be a whole number, otherwise leave blank to use default (default=1)'
        if iterations := validate_input(message, int, error_message):
            self.iterations = iterations
        
    def set_seconds_between_clicks(self, short=True):
        """Set the number of seconds between each action of the automation."""
        message = 'Seconds between clicks: ' if short else 'How many seconds would you like between clicks?: '
        error_message = 'ERROR: Value must be a number, otherwise leave blank to use default (default=1)'
        if seconds_between_clicks := validate_input(message, float, error_message):
            self.seconds_between_clicks = seconds_between_clicks

    def list_coordinates(self):
        """List the automation's coordinates if they were set. Otherwise, tell 
        that there are none set."""
        if self.coordinates:
            print('Coordinates:')
            for i, coordinate in enumerate(self.coordinates):
                print(f'{i+1}. X: {coordinate[0]} Y: {coordinate[1]}')
        else:
            print('No coordinates to display')

    def run(self, check=False):
        """Run the automation with optional pause before hand."""
        if check:
            user_decision = input('Would you like to begin the automation? (y/n): ')
            decision = True if user_decision.lower() in {'y', 'yes'} else False
        else:
            decision = True

        if decision == True:
            print('Automation starting...')
            print('NOTE: Slam mouse pointer to top right of screen while automation is running to cancel.')
            for iteration in range(self.iterations):
                for coordinate in self.coordinates:
                    click(coordinate[0], coordinate[1])
                    sleep(self.seconds_between_clicks)
            print('Automation complete.')
        else:
            print('Automation cancelled by User')
    

def main():
    test_automation = Automation()
    test_automation.set_coordinate_count()
    test_automation.set_iterations()
    test_automation.set_seconds_between_clicks()
    test_automation.find_coordinates()
    test_automation.run(check=True)

if __name__ == '__main__':
    main()
