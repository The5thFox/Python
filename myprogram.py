from mymodule import my_func #Same folder C:\Users\Q\Desktop\mymodule
my_func()

from MyMainPackage import some_main_script #Different folder "C:\Users\Q\Desktop\MyMainPackage" + __init__.py
from MyMainPackage.SubPackage import mysubscript #Sub folder within different folder "C:\Users\Q\Desktop\MyMainPackage\SubPackage" + __init__.py

some_main_script.report_main()
mysubscript.sub_report()