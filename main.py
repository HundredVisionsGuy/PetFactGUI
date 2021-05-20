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
  print("animal type is " + animal_type)
  if not type:
      return
  else:
      base_url = "https://cat-fact.herokuapp.com"
      endpoint = "/facts/random"
      query = "?animal_type=" + animal_type.lower() + "&amount=1"
      url = base_url + endpoint + query

      # new API call
      resp2 = requests.get(url)
      fact = resp2.json()
      return fact['text']


sg.theme('dark grey 9')

choices = ("Dog", "Cat")

# Define the window's contents
layout = [[
    sg.Text(
        "Welcome to Pet Facts. Select a pet and \nhow many facts you want.")
],
          [
              sg.Text("Dog or Cat?: "),
              sg.Listbox(choices, size=(10, len(choices)), key='-PET_TYPE-')
          ], [sg.Text(size=(40, 5), key='-OUTPUT-')],
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
    if event == "Get a fact":
        if values['-PET_TYPE-']:
            pet_type = values['-PET_TYPE-'][0]
            print(pet_type)
            pet_fact = get_pet_fact(pet_type)
            window['-OUTPUT-'].update('Here is your ' + values['-PET_TYPE-'][0] +
                                      " Fact: " + pet_fact)

# Finish up by removing from the screen
window.close()
