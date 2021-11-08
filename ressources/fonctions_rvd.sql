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

SET resultat = 0;

SET deja_present = (SELECT id_livre FROM permission_livres_usagers
    WHERE id_usager = usager_id 
    and id_livre = livre_id);

if ISNULL(deja_present) THEN

    SET usager = (SELECT id FROM usagers WHERE id = usager_id);

    SET livre = (SELECT id FROM livres
    WHERE id = livre_id);

    if not ISNULL(usager) AND not ISNULL(livre) THEN

        INSERT INTO permission_livres_usagers (id_usager, id_livre) values(
            usager_id,
            livre_id
        );
        SET resultat = 1;
    END IF;
END IF;
return resultat;
END $$
DELIMITER ;;

DROP FUNCTION IF EXISTS insertion_chapitre;

DELIMITER $$

CREATE FUNCTION insertion_chapitre(livre_id INT, le_numero INT, contenu_chapitre TEXT) RETURNS INT
DETERMINISTIC CONTAINS SQL
BEGIN
INSERT INTO chapitres_livres (id_livre, numero, contenue)  values(livre_id, le_numero, contenu_chapitre);

return (select id FROM chapitres_livres WHERE id_livre = livre_id
	AND numero = le_numero AND contenue = contenu_chapitre ORDER BY id desc);

END $$