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
CREATE PROCEDURE insert_sauvegarde(IN usager_id INT, IN livre_id INT, chapitre_id INT, INOUT out_save_id INT)
BEGIN
  INSERT INTO sauvegardes_parties (id_usager, id_livre, id_chapitre)
    VALUES (usager_id, livre_id, chapitre_id);

     SET out_save_id = (SELECT id FROM sauvegardes_parties ORDER BY date_partie DESC LIMIT 1);
END //


DROP PROCEDURE IF EXISTS insert_aventure;
DELIMITER //
CREATE PROCEDURE insert_aventure(
    IN save_id INT,
    IN discipline TEXT,
    IN armes TEXT,
    IN objets_sac TEXT,
    IN repas_sac TEXT,
    IN habileter TEXT,
    IN endurance TEXT,
    IN objets_speciaux TEXT,
    IN bourse TEXT,
    IN endurance_loup TEXT,
    IN quotien_attaque TEXT,
    IN endurance_ennemie TEXT,
    OUT retour_proc INT
    )
BEGIN
  INSERT INTO feuilles_aventure (
    id_save, 
    discipline,
    armes,
    objets_sac,
    repas_sac,
    habileter,
    endurance,
    objets_speciaux,
    bourse,
    endurance_loup,
    quotien_attaque,
    endurance_ennemie
    )

    VALUES (
    save_id,
    discipline,
    armes,
    objets_sac,
    repas_sac,
    habileter,
    endurance,
    objets_speciaux,
    bourse,
    endurance_loup,
    quotien_attaque,
    endurance_ennemie
    );

     SET retour_proc = (SELECT id FROM feuilles_aventure ORDER BY id_save DESC LIMIT 1);
END //

DROP PROCEDURE IF EXISTS update_aventure;
DELIMITER //
CREATE PROCEDURE update_aventure(
  IN save_id INT,
  IN discipline TEXT,
  IN armes TEXT,
  IN objets_sac TEXT,
  IN repas_sac TEXT,
  IN habileter TEXT,
  IN endurance TEXT,
  IN objets_speciaux TEXT,
  IN bourse TEXT,
  IN endurance_loup TEXT,
  IN quotien_attaque TEXT,
  IN endurance_ennemie TEXT
)
BEGIN
  UPDATE feuilles_aventure

  SET
    id_save = save_id,
    discipline = discipline ,
    armes = armes ,
    objets_sac = objets_sac ,
    repas_sac = repas_sac ,
    habileter = habileter ,
    endurance = endurance ,
    objets_speciaux = objets_speciaux ,
    bourse = bourse ,
    endurance_loup = endurance_loup ,
    quotien_attaque = quotien_attaque ,
    endurance_ennemie = endurance_ennemie

  WHERE id_save = save_id;
END //
