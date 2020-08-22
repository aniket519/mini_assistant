import pyttsx3
import os

pyttsx3.speak("Welcome to my application")
while True:
    print("How may i help you: ",end = '')
    pyttsx3.speak("How may i help you:")
    p = input()

    if (('run' in p) or('open' in p)) and (('notepad' in p)):
        os.system('notepad')

    elif ('text' in p) or ('editor' in p):
        print('notepad\nsublime text 3\natom')
        pyttsx3.speak('notepad sublime text natom')
        pyttsx3.speak('choose text editor')
        q = input('choose text editor: ')
        if 'notepad' in q:
            os.system('notepad')
        elif 'sublime' in q:
            os.system(sublime_text)
        elif 'atom' in q:
            os.system(atom)
        else:
            pyttsx3.speak('wrong input')

    elif (('run' in p) or ('open' in p)) and (('atom' in p)):
        os.system('atom')

    elif (('run' in p) or ('open' in p)) and (('sublime' in p)):
        os.system('sublime_text')

    elif (('run' in p) or 'open' in p) and ('word' in p):
        os.system('WINWORD')

    elif (('run' in p) or ('open' in p)) and ('chrome' in p):
        os.system('chrome')

    elif (('run' in p) or ('open' in p)) and (('mozila' in p) or ('firefox' in p)):
        os.system('firefox')

    elif (('run' in p) or ('open' in p)) and ('codeblocks' in p):
        pyttsx3.speak('It may take some time')
        os.system('codeblocks')

    elif (('run' in p) or ('open' in p)) and ('netbeans' in p):
        pyttsx3.speak('It may take some time')
        os.system('netbeans64')

    elif (('run' in p) or ('open' in p)) and ('androidstudio' in p):
        pyttsx3.speak('It may take some time')
        os.system('studio')

    elif (('run' in p) or ('open' in p)) and ('sqlite3' in p):
        os.system('sqlite3')

    elif (('run' in p) or ('open' in p)) and ('jupyter' in p):
        os.system('jupyter-notebook')

    elif (('run' in p) or ('open' in p)) and ('camera' in p):
        os.system('start microsoft.windows.camera:')

    elif (('run' in p) or ('open' in p)) and ('skype' in p):
        os.system('skype.exe')

    elif (('run' in p) or ('open' in p)) and ('calculator' in p):
        os.system('calc')

    elif (('run' in p) or ('open' in p)) and ('paint' in p):
        os.system('mspaint')

    elif (('run' in p) or ('open' in p)) and ('snipping' in p):
        os.system('SnippingTool')

    elif (('run' in p) or ('open' in p)) and ('taskmanager' in p):
        os.system('Taskmgr')

    elif (('run' in p) or ('open' in p)) and (('clock' in p) or ('alarm' in p)):
        os.system('start ms-clock:')

    elif (('run' in p) or ('open' in p)) and (('calender' in p)):
        os.system('start outlookcal:')

    elif (('run' in p) or ('open' in p)) and (('mail' in p) or ('gmail' in p)):
        os.system('start outlookmail:')

    elif (('run' in p) or ('open' in p)) and (('music' in p) or ('groove' in p)):
        os.system('start mswindowsmusic:')

    elif (('run' in p) or ('open' in p)) and (('map' in p) or ('maps' in p)):
        os.system('start bingmaps:')

    elif (('run' in p) or ('open' in p)) and (('messaging' in p)):
        os.system('start ms-chat:')

    elif (('run' in p) or ('open' in p)) and (('clock' in p) or ('alarm' in p)):
        os.system('start ms-clock:')

    elif (('run' in p) or ('open' in p)) and (('store' in p)):
        os.system('start ms-windows-store:')

    elif (('run' in p) or ('open' in p)) and (('people' in p) or ('mspeople' in p) or ('ms-people') in p):
        os.system('start ms-people:')

    elif (('run' in p) or ('open' in p)) and (('photos' in p) or ('msphotos' in p)):
        os.system('start ms-photos:')

    elif (('run' in p) or ('open' in p)) and (('settings' in p) or ('setting' in p)):
        os.system('start ms-settings:')

    elif (('run' in p) or ('open' in p)) and (('xbox' in p) or ('x-xbox' in p)):
        os.system('start xbox:')

    elif (('run' in p) or ('open' in p)) and ('zoom' in p):
        os.system('Zoom')

    elif (('run' in p) or ('open' in p)) and ('vlc' in p):
        os.system('vlc')

    elif (('run' in p) or ('open' in p)) and ('fifa19' in p):
        pyttsx3.speak('It may take some time')
        os.system('FIFA19')

    elif (('run' in p) or ('open' in p)) and ('callofduty' in p):
        pyttsx3.speak('It may take some time')
        os.system('iw3sp')

    elif ('break' in p) or ('exit' in p) or ('quit' in p) or ('terminate' in p):
        break

    else:
        print("Don't support!")
        pyttsx3.speak("Don't support!")
