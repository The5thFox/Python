import os
import win32api
import webbrowser

os.environ['USERNAME']
x = win32api.GetUserName()

if x == 'qtodd200':
    webbrowser.open('https://github.com/The5thFox/Python')
    webbrowser.open('https://www.udemy.com/complete-python-bootcamp/learn/')
    filepath1 = r'"C:\Users\qtodd200\AppData\Local\GitHubDesktop\GitHubDesktop.exe"'
    os.startfile(filepath1)
    filepath2 = r'"C:\Users\qtodd200\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Jupyter Notebook.lnk"'
    os.startfile(filepath2)
    filepath3 = r'"C:\Users\qtodd200\workbooks\Python Example Code\Python"'
    os.startfile(filepath3)
else:
    webbrowser.open('https://github.com/The5thFox/Python')
    webbrowser.open('https://www.udemy.com/complete-python-bootcamp/learn/')
    filepath1 = r'"C:\Users\qtodd200\AppData\Local\GitHubDesktop\GitHubDesktop.exe"'
    os.startfile(filepath1)
    filepath2 = r'"C:\Users\qtodd200\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Jupyter Notebook.lnk"'
    os.startfile(filepath2)
    filepath3 = r'"C:\Users\qtodd200\workbooks\Python Example Code\Python"'
    os.startfile(filepath3)