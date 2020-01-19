# automatically fills in form

import pyautogui
import time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
             'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
             'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}, ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

for person in formData:
    # give user chance to kill script
    print('5 SECOND PAUSE TO LET USER PRESS CTRL-C')
    time.sleep(5)

    print(f'Entering {person["name"]} info')
    pyautogui.write(['\t', '\t'])

    # fill out name field
    pyautogui.write(person['name'] + '\t')

    # fill out greatest fear field
    pyautogui.write(person['fear'] + '\t')

    # fill out wizards field
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)

    # fill out robocop field
    if person['robocop'] == 1:
        pyautogui.write(['', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)

    # fill out additional comments field
    pyautogui.write(person['comments'] + '\t')

    # click submit button
    time.sleep(0.5)
    pyautogui.press('enter')

    # wait for form to load
    print('Submitted Form.')
    time.sleep(5)

    # get new form
    pyautogui.write(['\t', '\n'], 0.5)
