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
    filepath2 = r'"C:\Users\qtodd200\Jupyter Notebook.lnk"'
    os.startfile(filepath2)
    filepath3 = r'"C:\Users\qtodd200\workbooks\Python Example Code\Python"'
    os.startfile(filepath3)
else:
    webbrowser.open('https://github.com/The5thFox/Python')
    webbrowser.open('https://www.udemy.com/complete-python-bootcamp/learn/')
    filepath1 = r'"C:\Users\Q\AppData\Local\GitHubDesktop\GitHubDesktop.exe"'
    os.startfile(filepath1)
    filepath2 = r'"C:\Users\Q\Jupyter Notebook.lnk"'
    os.startfile(filepath2)
    filepath3 = r'"C:\Users\Q\workbooks\Python Example Code\Python\"'
    os.startfile(filepath3)