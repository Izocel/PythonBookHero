use python_book_hero;
# Non-testé RVÐ

DROP FUNCTION IF EXISTS acheter_livre_usager;
DELIMITER $$
CREATE FUNCTION acheter_livre_usager(usager_id int, livre_id int) RETURNS TINYINT(1)
DETERMINISTIC CONTAINS SQL

BEGIN
DECLARE deja_present int;
DECLARE usager int;
DECLARE livre int;
DECLARE resultat bool;

SET deja_present = (SELECT id_livre FROM permission_livres_usagers
    WHERE id_usager = usager_id 
    and id_livre = livre_id);

if not deja_present THEN

    SET usager = (SELECT id FROM usagers
    WHERE id = usager_id);

    SET livre = (SELECT id FROM livres
    WHERE id = livre_id);

    if usager AND livre THEN

        INSERT id_usager, id_livre INTO permission_livres_usagers values(
            usager_id,
            livre_id
        );
        set resultat = 1;
    ELSE THEN
        SET resultat = 0;
    END IF;

ELSE THEN
   SET resultat = 2;
END IF;

return resultat;
END $$


DELIMITER ;;


DROP FUNCTION IF EXISTS insertion_chapitre;
DELIMITER $$
CREATE FUNCTION insertion_chapitre(livre_id INT, le_numero INT, ccontenu_chapitre TEXT) RETURNS INT
DETERMINISTIC CONTAINS SQL

BEGIN

INSERT id_livre, numero, contenue INTO chapitres_livres values(
    livre_id, le_numero, ccontenu_chapitre
);

return (select id FROM chapitres_livres WHERE id_livre = livre_id 
    AND numero = le_numero
    AND contenue = ccontenu_chapitre
    ORDER BY id desc;
END $$