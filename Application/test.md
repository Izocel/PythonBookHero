### HtoFix connection btnLivre et btnSave

> #### Modifications
    > Les connnections n'utilisent plus aucun paramêtre, mais les bouttons on les informations stockées en propriétées. Voici l'utilisation:
    > ```python
    > --> connect(ecran_chapitre.field_selection_chapitre)
    > ```
> 
    > ```python    
        > --> def field_selection_chapitre(self): 
        > sender = self.sender()
        > id_livre = sender.id_livre
        > num_save_chapitre = sender.num_chapitre
        > ```

Example livre:

```python
def fetch_livre(self, usager_id:int) -> None:
        livres_user = liste_livre_usager(usager_id)

        layout:QtWidgets.QHBoxLayout = self.LivreshorizontalLayout
        clearLayout(layout)

        ecran_chapitre:ECRAN_CHAPITRE = self.parent.findChild(QDialog, 'EcranChapitres')
        _translate = QtCore.QCoreApplication.translate

        self.livrespushButton = QtWidgets.QPushButton(self.sectionHaut_groupBox)
        self.livrespushButton.setAutoFillBackground(False)
        self.livrespushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.livrespushButton.clicked.connect(ecran_chapitre.field_selection_chapitre)
        self.livrespushButton.setStyleSheet(":!active, :active{font-size:32px;border-radius:20px;\n""background-color: rgb(170, 255, 255);\n"
        "}\n"":hover{\n""background-color: rgb(23, 250, 250);\n""}")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        i = 0
        for livre in livres_user:
            id_livre = livre[0]
            nomLivre = livre[1]
            auteurLivre = livre[2]

            self.livrespushButton.id_livre = id_livre
            self.livrespushButton.num_chapitre = 0
            self.livrespushButton.setObjectName(f"livrespushButton_{i}")
            self.livrespushButton.setSizePolicy(sizePolicy)
            self.livrespushButton.setText(_translate("EcranUsager", f"{nomLivre} \n {auteurLivre}"))

            if(i >0):
                sizePolicy.setHeightForWidth(self.livrespushButton.sizePolicy().hasHeightForWidth())
            layout.addWidget(self.livrespushButton)
            i+=1
```


