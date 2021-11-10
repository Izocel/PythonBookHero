use python_book_hero;


DROP PROCEDURE IF EXISTS update_sauvegarde;
DELIMITER //
CREATE PROCEDURE update_sauvegarde(IN id_save INT, IN usager_id INT, IN livre_id INT, chapitre_id INT)
BEGIN
  UPDATE sauvegardes_parties
  SET
    id_chapitre = chapitre_id,
    date_partie = CURRENT_TIMESTAMP
  WHERE
    id = id_save
    AND
    id_usager = usager_id
    AND
    id_livre = livre_id;
END //


DROP PROCEDURE IF EXISTS insert_sauvegarde;
DELIMITER //
CREATE PROCEDURE insert_sauvegarde(IN usager_id INT, IN livre_id INT, chapitre_id INT)
BEGIN
  INSERT INTO sauvegardes_parties (id_usager, id_livre, id_chapitre)
    VALUES (usager_id, livre_id, chapitre_id);
END //
