pyuic5 -x BookHeroProjectDesigner/ecrandeveloppeur.ui -o Application/Bibli_ui/ecrandeveloppeur.py
pyuic5 -x BookHeroProjectDesigner/ecrandeveloppeur.ui -o BookHeroProjectDesigner/last_ui/ecrandeveloppeur.py
copy BookHeroProjectDesigner\ecrandeveloppeur.ui Application\Bibli_ui\ecrandeveloppeur.ui


pyuic5 -x BookHeroProjectDesigner/ecranacceuil.ui -o Application/Bibli_ui/ecranacceuil.py
pyuic5 -x BookHeroProjectDesigner/ecranacceuil.ui -o BookHeroProjectDesigner/last_ui/ecranacceuil.py
copy BookHeroProjectDesigner\ecranacceuil.ui Application\Bibli_ui\ecranacceuil.ui

pyuic5 -x BookHeroProjectDesigner/selectionchapitres.ui -o Application/Bibli_ui/selectionchapitres.py
pyuic5 -x BookHeroProjectDesigner/selectionchapitres.ui -o BookHeroProjectDesigner/last_ui/selectionchapitres.py
copy BookHeroProjectDesigner\selectionchapitres.ui Application\Bibli_ui\selectionchapitres.ui

echo Succes !!!