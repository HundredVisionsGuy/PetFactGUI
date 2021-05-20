##########################################################
# API_test.py
# by Chris Winikka 
#
# Purpose:  demonstrate how to use Python 3 and requests
#           to capture and process JSON data 
#
# Credits:  API Integration in Python 
#           [https://realpython.com/api-integration-in-python]
#           
#           Public APIs
#           [https://github.com/public-apis/public-apis]
##########################################################

# import statements
import requests

import PySimpleGUI as sg

# Build out a new API call url
def get_pet_fact(animal_type):
  if not type:
    return
  else:
    base_url = "https://cat-fact.herokuapp.com"
    endpoint = "/facts/random"
    query = "?animal_type="+animal_type+"&amount=1"
    url = base_url + endpoint + query

    # new API call
    resp2 = requests.get(url)
    fact = resp2.json()
    return fact['text']

sg.theme('dark grey 9')

# Define the window's contents
layout = [[sg.Text("Welcome to Pet Facts. Select a pet and \nhow many facts you want.")],
          [sg.Text("Dog or Cat?: "), sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,10), key='-OUTPUT-')],
          [sg.Button('Get a fact'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Pet Facts', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    pet_fact = get_pet_fact(values['-INPUT-'])
    window['-OUTPUT-'].update('Here is your ' + values['-INPUT-'] + " Fact:" + pet_fact)

# Finish up by removing from the screen
window.close()

