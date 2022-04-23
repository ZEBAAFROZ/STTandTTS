#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PySimpleGUI as sg
import pyttsx3
import speech_recognition as sr

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#758283',
                                            'TEXT': '#FFFFFF','INPUT': '#CAD5E2',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#99CC99',
                                            'BUTTON': ('#FFFFFF', '#6A1B4D'),
                                            'PROGRESS': ('#D1826B', '#CC8019'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0,
                                            'PROGRESS_DEPTH': 0, }

def t2s():
    sg.theme('MyCreatedTheme')

    engine = pyttsx3.init()

    layout = [
        [sg.Text('Enter Your Text Here', font=("Helvetica", 15))],
        [sg.Text('Enter'), sg.InputText()],
        [sg.Button('Home'),sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('TEXT TO SPEECH', layout,size=(400,150), element_justification='c',
                       margins=(20, 10),element_padding=(5, 5),grab_anywhere=True).finalize()
    window.bind('<Escape>','-ESCAPE-')
    window.Maximize()

    v = engine.getProperty('voices')
    engine.setProperty('voice', v[2].id)
    engine.setProperty("rate", 100)

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == '-ESCAPE-' or event == sg.WINDOW_CLOSED:
            break
        if event == 'Home':
            window.hide()
            main()
            break
           
        engine.say(values[0])
        engine.runAndWait()

   
    window.close()

def s2t():
    sg.theme('MyCreatedTheme')

    r = sr.Recognizer()
    mic = sr.Microphone()

    values = ['HINDI', 'ENGLISH']

    layout = [
        [sg.Text('Select language', font=("Garamond", 15))],
        [sg.Combo((values), size=(41), font=("Garamond", 13), key='combo')],
        [sg.Button('Home'), sg.Button('Submit'), sg.Cancel()],
        [sg.Text('You Said:-', font=("Garamond", 15))],
        [sg.Output( size=(50,2),font=("Garamond", 11),key='-KEY-')]
    ]

    window = sg.Window('SPEECH TO TEXT', layout,  margins=(20, 10),
                       element_padding=(5, 5),grab_anywhere=True).finalize()
    window.bind('<Escape>','-ESCAPE-')
    window.Maximize()
   

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == '-ESCAPE-' or event == sg.WINDOW_CLOSED:
            break
           
        if event == 'Home':
            window.hide()
            main()
            break

        combo = values['combo']
        if event == 'Submit' and combo == 'ENGLISH':
            with mic as source:
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    window['-KEY-'].update(text)

                except:
                    window['-KEY-'].update('Error')

        if event == 'Submit' and combo == 'HINDI':
            with mic as source:
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language='hi-IN')
                    window['-KEY-'].update(text)

                except:
                    window['-KEY-'].update('Error')
                   
   
    window.close()

def main():
    sg.theme('MyCreatedTheme')

    t = sg.Text('NATURAL LANGUAGE PROCESSING', justification='center',font=("Helvetica", 19))
    r1 = sg.Radio('SPEECH TO TEXT', "RADIO1", size=(50, 1), font=("Helvetica", 15),
                  default=False, key="-r1-")
    r2 = sg.Radio('TEXT TO SPEECH', "RADIO1", font=("Helvetica", 15), default=False,
                  key="-r2-")
    f1 = sg.Frame(layout=[[r1], [r2]], title='OPTIONS', relief=sg.RELIEF_SUNKEN)
    s = sg.Button('Submit')
    c = sg.Cancel()

    layout = [[t], [f1], [s, c]]

    w = sg.Window('NLP', layout, element_justification='c', margins=(20, 10),
                  element_padding=(5, 5),grab_anywhere=True).finalize()
    w.bind('<Escape>','-ESCAPE-')
    w.Maximize()
   

    while True:
        event, values = w.read(close=True)
        if event == 'Cancel' or event == '-ESCAPE-' or event == sg.WINDOW_CLOSED:
            break
        elif values["-r1-"] == True:
            s2t()
            break
        elif values["-r2-"] == True:
            t2s()
            break
       

if __name__ == "__main__":
       main()


# In[ ]:




