pyuic5 -x BookHeroProjectDesigner/ecranusager.ui -o BookHeroProjectDesigner/last_python_ui/ecranusager.py
copy BookHeroProjectDesigner\ecranusager.ui Application\Bibli_ui\ecranusager.ui

pyuic5 -x BookHeroProjectDesigner/ecranacceuil.ui -o BookHeroProjectDesigner/last_python_ui/ecranacceuil.py
copy BookHeroProjectDesigner\ecranacceuil.ui Application\Bibli_ui\ecranacceuil.ui

pyuic5 -x BookHeroProjectDesigner/selectionchapitres.ui -o BookHeroProjectDesigner/last_python_ui/selectionchapitres.py
copy BookHeroProjectDesigner\selectionchapitres.ui Application\Bibli_ui\selectionchapitres.ui

echo Succes !!!