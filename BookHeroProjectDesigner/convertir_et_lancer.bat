pyuic5 -x BookHeroProjectDesigner/mainwindow.ui -o Bibli_ui_designer/mainwindow.py
pyuic5 -x BookHeroProjectDesigner/mainwindow.ui -o BookHeroProjectDesigner/last_ui/mainwindow.py

pyuic5 -x BookHeroProjectDesigner/dbbrowser.ui -o Bibli_ui_designer/dbbrowser.py
pyuic5 -x BookHeroProjectDesigner/dbbrowser.ui -o BookHeroProjectDesigner/last_ui/dbbrowser.py

echo Succes !!!

E:/Python3.9.7/python.exe "Application/main_app.py"