use python_book_hero;


 ### NON-TESTÉ RVÐ 06-11-2021
DROP PROCEDURE IF EXISTS liste_livres_usager;
DELIMITER //
CREATE PROCEDURE liste_livres_usager(IN usager_id INT)
BEGIN

        SELECT titre,auteur FROM permission_livres_usagers 
        INNER JOIN livres ON id_livre = livres.id 
        WHERE id_usager = usager_id;
        
END //
#test
CALL liste_livres_usager(1);


DROP PROCEDURE IF EXISTS liste_sauvgardes_usager;
DELIMITER //
CREATE PROCEDURE liste_sauvgardes_usager(IN usager_id INT)
BEGIN

	SELECT date_partie, page, numero, titre FROM sauvegardes_parties 
        INNER JOIN chapitres_livres ON id_chapitre = chapitres_livres.id 
        INNER JOIN livres ON chapitres_livres.id_livre = livres.id 
        WHERE id_usager = usager_id;

    # ajouter un check usager détient permission sur livre

END //
#test
CALL liste_sauvgardes_usager(1);




