-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 11, 2021 at 08:26 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_book_hero`
--
DROP DATABASE IF EXISTS `python_book_hero`;
CREATE DATABASE IF NOT EXISTS `python_book_hero` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `python_book_hero`;

DELIMITER $$
--
-- Procedures
--
DROP PROCEDURE IF EXISTS `insert_aventure`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_aventure` (IN `save_id` INT, IN `discipline` TEXT, IN `armes` TEXT, IN `objets_sac` TEXT, IN `repas_sac` TEXT, IN `habileter` TEXT, IN `endurance` TEXT, IN `objets_speciaux` TEXT, IN `bourse` TEXT, IN `endurance_loup` TEXT, IN `quotien_attaque` TEXT, IN `endurance_ennemie` TEXT, OUT `retour_proc` INT)  BEGIN
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
END$$

DROP PROCEDURE IF EXISTS `insert_sauvegarde`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_sauvegarde` (IN `usager_id` INT, IN `livre_id` INT, `chapitre_id` INT, INOUT `out_save_id` INT)  BEGIN
  INSERT INTO sauvegardes_parties (id_usager, id_livre, id_chapitre)
    VALUES (usager_id, livre_id, chapitre_id);

     SET out_save_id = (SELECT id FROM sauvegardes_parties ORDER BY date_partie DESC LIMIT 1);
END$$

DROP PROCEDURE IF EXISTS `update_aventure`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_aventure` (IN `save_id` INT, IN `discipline` TEXT, IN `armes` TEXT, IN `objets_sac` TEXT, IN `repas_sac` TEXT, IN `habileter` TEXT, IN `endurance` TEXT, IN `objets_speciaux` TEXT, IN `bourse` TEXT, IN `endurance_loup` TEXT, IN `quotien_attaque` TEXT, IN `endurance_ennemie` TEXT)  BEGIN
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
END$$

DROP PROCEDURE IF EXISTS `update_sauvegarde`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_sauvegarde` (IN `id_save` INT, IN `usager_id` INT, IN `livre_id` INT, `chapitre_id` INT)  BEGIN
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
END$$

--
-- Functions
--
DROP FUNCTION IF EXISTS `acheter_livre_usager`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `acheter_livre_usager` (`usager_id` INT, `livre_id` INT) RETURNS TINYINT(1) DETERMINISTIC CONTAINS SQL BEGIN
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
END$$

DROP FUNCTION IF EXISTS `insertion_chapitre`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `insertion_chapitre` (`livre_id` INT, `le_numero` INT, `contenu_chapitre` TEXT) RETURNS INT(11) DETERMINISTIC CONTAINS SQL BEGIN
INSERT INTO chapitres_livres (id_livre, numero, contenue)  values(livre_id, le_numero, contenu_chapitre);

return (select id FROM chapitres_livres WHERE id_livre = livre_id
	AND numero = le_numero AND contenue = contenu_chapitre ORDER BY id desc);

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `chapitres_livres`
--
-- Creation: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `chapitres_livres`;
CREATE TABLE IF NOT EXISTS `chapitres_livres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_livre` int(11) NOT NULL,
  `numero` tinyint(4) NOT NULL,
  `contenue` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_livre` (`id_livre`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `chapitres_livres`
--

INSERT INTO `chapitres_livres` (`id`, `id_livre`, `numero`, `contenue`) VALUES
(1, 1, 0, '<h1>Introduction: Avertir le roi</h1>\n<p>\nAu nord du royaume du Sommerlund, il est de tradition depuis \ndes si??cles d\'envoyer les fils des Seigneurs de la Guerre au \nmonast??re Ka??. C\'est l?? qu\'on leur enseigne l\'art et la science de \nleurs nobles anc??tres.\nLes Moines Ka?? sont de grands ma??tres dans l\'art qu\'ils \nenseignent. Pour transmettre leurs connaissances, ils doivent \nfaire subir ?? leurs disciples de rudes ??preuves au cours de leur \napprentissage, mais ces derniers ne s\'en plaignent jamais. Ils leur \nt??moignent au contraire amour et respect, sachant tr??s bien \nqu\'ils quitteront un jour le monast??re en poss??dant tous les \nsecrets de la tradition Ka??: ils pourront alors rentrer chez eux, \nl\'esprit et le corps form??s aux techniques de la guerre. \nProfond??ment attach??s ?? leur patrie, ils seront ainsi pr??ts ?? la \nd??fendre contre le danger constant qui la menace : la soif de \nconqu??te des Ma??tres des T??n??bres venus de l\'ouest.\nAu temps jadis, ?? l\'??poque de la Lune Noire, les Ma??tres des \nT??n??bres men??rent une guerre sans merci contre le royaume du \nSommerlund. Ce fut une longue et douloureuse ??preuve de force \n?? l\'issue de laquelle les guerriers du Sommerlund remport??rent la \nvictoire lors de la grande bataille de Maaken. Le roi Ulnar et ses \nalli??s de Durenor an??antirent l\'arm??e des Ma??tres des T??n??bres \ndans le d??fil?? de Moytura et pr??cipit??rent l\'ennemi au fond de la \ngorge de Maaken. Vashna, le plus puissant parmi les Ma??tres des \nT??n??bres, p??rit d\'un coup mortel que le roi Ulnar lui porta de sa \npuissante ??p??e, l\'Ep??e du Soleil, que l\'on d??signe g??n??ralement \nsous le nom de ??Glaive de Sommer??. Depuis ce temps, les \nMa??tres des T??n??bres ont jur?? de prendre leur revanche sur le \nroyaume du Sommerlund et la Maison d\'Ulnar.\nLorsque l\'aube se l??ve sur le premier jour de votre aventure, tous \nles Seigneurs Ka?? sont pr??sents au monast??re : on doit, en effet, \nc??l??brer aujourd\'hui m??me la grande f??te de Fehmarn et l\'on se \npr??pare t??t le matin aux r??jouissances. Mais soudain, un \nimmense nuage noir s\'??l??ve au ciel d\'occident: d\'??normes \ncr??atures aux ailes sombres emplissent les nues en si grand \nnombre que le soleil semble s\'??teindre. Cette invasion porte la \nmarque des Ma??tres des T??n??bres. Les ennemis jur??s du \nRoyaume du Sommerlund passent une nouvelle fois ?? l\'attaque : \nla guerre a recommenc??. En ce matin fatal, Loup Silencieux (c\'est \nle nom qui vous a ??t?? donn?? par les Moines Ka??) est all?? chercher \ndu bois dans la for??t : c\'est la corv??e qu\'on vous a assign??e pour \nvous punir de votre inattention en classe. Or, sur le chemin du \nretour, vous apercevez tout ?? coup ce gigantesque nuage de \ncr??atures noires qui fond sur le monast??re et semble l\'engloutir \naussit??t. Vous laissez tomber votre bois ?? terre et vous vous \npr??cipitez sur le lieu de la bataille. Mais les monstres noirs ont \nobscurci le soleil et il fait ?? pr??sent si sombre que vous tr??buchez \ncontre une racine en tombant t??te la premi??re. Dans votre chute, \nvous heurtez violemment du front une branche basse qui vous \nassomme. Une fraction de seconde avant de perdre \nconnaissance, vous avez cependant le temps de saisir du regard \nun terrifiant spectacle: les murs du monast??re Ka?? sont en train \nde s\'??crouler sur eux-m??mes dans un fracas de tonnerre. Vous ne \nreprenez conscience qu\'au bout de plusieurs heures et, les larmes \naux yeux, vous contemplez avec horreur le tas de ruines que \nl\'ennemi a laiss?? derri??re lui. Les Guerriers Ka?? ont ??t?? ensevelis \nsous les d??combres et il ne reste plus aucun survivant parmi vos \ncompagnons. Avec une infinie douleur, vous levez alors votre \nvisage vers le ciel, ?? nouveau clair, et vous faites le serment de \nvenger la mort des Moines et des Seigneurs Ka??. Vous ferez payer \nleur crime aux Ma??tres des T??n??bres ! Votre t??che d\'ailleurs \ncommence ?? l\'instant m??me : il vous faut, en effet, gagner la \ncapitale du royaume pour pr??venir le Roi en personne de \nl\'effroyable p??ril qui menace le pays ; car maintenant, l\'ennemi \nest en marche, et si vous n\'agissez pas ?? temps, votre patrie \ntombera sous son joug. Vous ??tes le dernier des Seigneurs Ka?? et \nle sort de votre peuple repose d??sormais entre vos seules mains: \nle Loup Silencieux est devenu Loup Solitaire et les envahisseurs \nferont tout pour vous emp??cher d\'atteindre le Palais du Roi....\n</p>'),
(2, 2, 0, '<h1>Introduction: Avertir le roi</h1>\n<p>\nAu nord du royaume du Sommerlund, il est de tradition depuis \ndes si??cles d\'envoyer les fils des Seigneurs de la Guerre au \nmonast??re Ka??. C\'est l?? qu\'on leur enseigne l\'art et la science de \nleurs nobles anc??tres.\nLes Moines Ka?? sont de grands ma??tres dans l\'art qu\'ils \nenseignent. Pour transmettre leurs connaissances, ils doivent \nfaire subir ?? leurs disciples de rudes ??preuves au cours de leur \napprentissage, mais ces derniers ne s\'en plaignent jamais. Ils leur \nt??moignent au contraire amour et respect, sachant tr??s bien \nqu\'ils quitteront un jour le monast??re en poss??dant tous les \nsecrets de la tradition Ka??: ils pourront alors rentrer chez eux, \nl\'esprit et le corps form??s aux techniques de la guerre. \nProfond??ment attach??s ?? leur patrie, ils seront ainsi pr??ts ?? la \nd??fendre contre le danger constant qui la menace : la soif de \nconqu??te des Ma??tres des T??n??bres venus de l\'ouest.\nAu temps jadis, ?? l\'??poque de la Lune Noire, les Ma??tres des \nT??n??bres men??rent une guerre sans merci contre le royaume du \nSommerlund. Ce fut une longue et douloureuse ??preuve de force \n?? l\'issue de laquelle les guerriers du Sommerlund remport??rent la \nvictoire lors de la grande bataille de Maaken. Le roi Ulnar et ses \nalli??s de Durenor an??antirent l\'arm??e des Ma??tres des T??n??bres \ndans le d??fil?? de Moytura et pr??cipit??rent l\'ennemi au fond de la \ngorge de Maaken. Vashna, le plus puissant parmi les Ma??tres des \nT??n??bres, p??rit d\'un coup mortel que le roi Ulnar lui porta de sa \npuissante ??p??e, l\'Ep??e du Soleil, que l\'on d??signe g??n??ralement \nsous le nom de ??Glaive de Sommer??. Depuis ce temps, les \nMa??tres des T??n??bres ont jur?? de prendre leur revanche sur le \nroyaume du Sommerlund et la Maison d\'Ulnar.\nLorsque l\'aube se l??ve sur le premier jour de votre aventure, tous \nles Seigneurs Ka?? sont pr??sents au monast??re : on doit, en effet, \nc??l??brer aujourd\'hui m??me la grande f??te de Fehmarn et l\'on se \npr??pare t??t le matin aux r??jouissances. Mais soudain, un \nimmense nuage noir s\'??l??ve au ciel d\'occident: d\'??normes \ncr??atures aux ailes sombres emplissent les nues en si grand \nnombre que le soleil semble s\'??teindre. Cette invasion porte la \nmarque des Ma??tres des T??n??bres. Les ennemis jur??s du \nRoyaume du Sommerlund passent une nouvelle fois ?? l\'attaque : \nla guerre a recommenc??. En ce matin fatal, Loup Silencieux (c\'est \nle nom qui vous a ??t?? donn?? par les Moines Ka??) est all?? chercher \ndu bois dans la for??t : c\'est la corv??e qu\'on vous a assign??e pour \nvous punir de votre inattention en classe. Or, sur le chemin du \nretour, vous apercevez tout ?? coup ce gigantesque nuage de \ncr??atures noires qui fond sur le monast??re et semble l\'engloutir \naussit??t. Vous laissez tomber votre bois ?? terre et vous vous \npr??cipitez sur le lieu de la bataille. Mais les monstres noirs ont \nobscurci le soleil et il fait ?? pr??sent si sombre que vous tr??buchez \ncontre une racine en tombant t??te la premi??re. Dans votre chute, \nvous heurtez violemment du front une branche basse qui vous \nassomme. Une fraction de seconde avant de perdre \nconnaissance, vous avez cependant le temps de saisir du regard \nun terrifiant spectacle: les murs du monast??re Ka?? sont en train \nde s\'??crouler sur eux-m??mes dans un fracas de tonnerre. Vous ne \nreprenez conscience qu\'au bout de plusieurs heures et, les larmes \naux yeux, vous contemplez avec horreur le tas de ruines que \nl\'ennemi a laiss?? derri??re lui. Les Guerriers Ka?? ont ??t?? ensevelis \nsous les d??combres et il ne reste plus aucun survivant parmi vos \ncompagnons. Avec une infinie douleur, vous levez alors votre \nvisage vers le ciel, ?? nouveau clair, et vous faites le serment de \nvenger la mort des Moines et des Seigneurs Ka??. Vous ferez payer \nleur crime aux Ma??tres des T??n??bres ! Votre t??che d\'ailleurs \ncommence ?? l\'instant m??me : il vous faut, en effet, gagner la \ncapitale du royaume pour pr??venir le Roi en personne de \nl\'effroyable p??ril qui menace le pays ; car maintenant, l\'ennemi \nest en marche, et si vous n\'agissez pas ?? temps, votre patrie \ntombera sous son joug. Vous ??tes le dernier des Seigneurs Ka?? et \nle sort de votre peuple repose d??sormais entre vos seules mains: \nle Loup Silencieux est devenu Loup Solitaire et les envahisseurs \nferont tout pour vous emp??cher d\'atteindre le Palais du Roi....\n</p>'),
(3, 1, 1, '<h1>Chapitre 1</h1>\n<p>\nIl faut vous h??ter, car quelque chose vous dit qu\'il serait \nimprudent de vous attarder parmi les ruines fumantes du \nmonast??re d??truit. Les monstres volants peuvent, en effet, \nrepara??tre ?? tout moment. Il n\'y a d\'ailleurs pas de temps ?? \nperdre : vous devez au plus vite prendre la route de Holmgard, la \ncapitale du Sommerlund, pour aller annoncer au Roi cette \nterrible nouvelle : les Guerriers Ka??, l\'??lite du pays, ont tous ??t?? \nmassacr??s, ?? l\'exception de vous-m??me. Or sans l\'autorit?? et le \nsavoir des Seigneurs Ka?? pour commander l\'arm??e, le royaume \ndu Sommerlund se trouve ?? la merci de ses plus anciens \nennemis: les Ma??tres des T??n??bres. En retenant vos larmes ?? \ngrand-peine, vous dites adieu ?? vos compagnons morts et vous \nfaites le serment de les venger. Vous tournez alors le dos aux \nruines et vous descendez avec pr??caution le sentier escarp?? qui \ns\'ouvre devant vous. Au pied de la colline, le chemin aboutit ?? \nune bifurcation. L??, deux autres sentiers m??nent l\'un et l\'autre ?? \nune grande for??t en empruntant deux directions diff??rentes. Si \nvous souhaitez prendre le sentier de droite, rendez-vous au 85.\nSi vous pr??f??rez suivre celui de gauche, rendez-vous au 275.\nEnfin, si vous ma??trisez la Discipline Ka?? du Sixi??me Sens, \nrendez-vous au 141.\n</p>'),
(4, 2, 1, '<h1>Chapitre 1</h1>\n<p>\nIl faut vous h??ter, car quelque chose vous dit qu\'il serait \nimprudent de vous attarder parmi les ruines fumantes du \nmonast??re d??truit. Les monstres volants peuvent, en effet, \nrepara??tre ?? tout moment. Il n\'y a d\'ailleurs pas de temps ?? \nperdre : vous devez au plus vite prendre la route de Holmgard, la \ncapitale du Sommerlund, pour aller annoncer au Roi cette \nterrible nouvelle : les Guerriers Ka??, l\'??lite du pays, ont tous ??t?? \nmassacr??s, ?? l\'exception de vous-m??me. Or sans l\'autorit?? et le \nsavoir des Seigneurs Ka?? pour commander l\'arm??e, le royaume \ndu Sommerlund se trouve ?? la merci de ses plus anciens \nennemis: les Ma??tres des T??n??bres. En retenant vos larmes ?? \ngrand-peine, vous dites adieu ?? vos compagnons morts et vous \nfaites le serment de les venger. Vous tournez alors le dos aux \nruines et vous descendez avec pr??caution le sentier escarp?? qui \ns\'ouvre devant vous. Au pied de la colline, le chemin aboutit ?? \nune bifurcation. L??, deux autres sentiers m??nent l\'un et l\'autre ?? \nune grande for??t en empruntant deux directions diff??rentes. Si \nvous souhaitez prendre le sentier de droite, rendez-vous au 85.\nSi vous pr??f??rez suivre celui de gauche, rendez-vous au 275.\nEnfin, si vous ma??trisez la Discipline Ka?? du Sixi??me Sens, \nrendez-vous au 141.\n</p>'),
(5, 1, 2, '<h1>Chapitre 2</h1>\n<p>\nTandis que vous courez ?? perdre haleine dans la for??t qui \ns\'??paissit, les cris des Gloks s\'??vanouissent peu ?? peu derri??re \nvous. Vous les avez presque sem??s lorsque vous tr??buchez \nsoudain en tombant t??te la premi??re dans un enchev??trement de \nbranches basses. Utilisez la Table de Hasard pour obtenir un \nchiffre. Si vous tirez entre 0 et 4, rendez-vous au 343. Entre 5 et \n9, rendez-vous au 276.\n</p>'),
(6, 2, 2, '<h1>Chapitre 2</h1>\n<p>\nTandis que vous courez ?? perdre haleine dans la for??t qui \ns\'??paissit, les cris des Gloks s\'??vanouissent peu ?? peu derri??re \nvous. Vous les avez presque sem??s lorsque vous tr??buchez \nsoudain en tombant t??te la premi??re dans un enchev??trement de \nbranches basses. Utilisez la Table de Hasard pour obtenir un \nchiffre. Si vous tirez entre 0 et 4, rendez-vous au 343. Entre 5 et \n9, rendez-vous au 276.\n</p>'),
(7, 1, 3, '<h1>Chapitre 3</h1>\n<p>\nVous embo??tez le pas ?? l\'officier qui franchit une porte en arcade, \npuis monte quelques marches menant ?? un grand hall. Des \nsoldats courent en tous sens, porteurs de parchemins orn??s qu\'ils \ndoivent remettre ?? des officiers post??s le long des murs de la \nville. Un homme au visage coutur?? de cicatrices, l\'air hagard, \ns\'approche de vous et vous offre de le suivre jusqu\'?? la citadelle. \nIl porte la toge blanche et pourpre en usage ?? la cour du Roi. Si \nvous souhaitez suivre cet homme, rendez-vous au 196. Si vous \npr??f??rez d??cliner son offre et retourner dans les rues populeuses, \nrendez-vous au 144.\n</p>'),
(8, 2, 3, '<h1>Chapitre 3</h1>\n<p>\nVous embo??tez le pas ?? l\'officier qui franchit une porte en arcade, \npuis monte quelques marches menant ?? un grand hall. Des \nsoldats courent en tous sens, porteurs de parchemins orn??s qu\'ils \ndoivent remettre ?? des officiers post??s le long des murs de la \nville. Un homme au visage coutur?? de cicatrices, l\'air hagard, \ns\'approche de vous et vous offre de le suivre jusqu\'?? la citadelle. \nIl porte la toge blanche et pourpre en usage ?? la cour du Roi. Si \nvous souhaitez suivre cet homme, rendez-vous au 196. Si vous \npr??f??rez d??cliner son offre et retourner dans les rues populeuses, \nrendez-vous au 144.\n</p>'),
(9, 1, 4, '<h1>Chapitre 4</h1>\n<p>\nC\'est un petit cano?? ?? une place, en tr??s mauvais ??tat. Des pi??ces \nde bois disjointes laissent appara??tre des trous en plusieurs \nendroits de la coque et il vous faut les boucher ?? la h??te avec de \nl\'argile. Vous videz ensuite l\'embarcation de son eau et il vous \nsemble alors qu\'elle est en ??tat de flotter. Vous rangez votre \n??quipement ?? l\'avant du cano??, puis vous descendez le cours de \nla rivi??re en pagayant ?? l\'aide d\'un d??bris de bois ramass?? ?? la \nsurface de l\'eau. Un instant plus tard, vous entendez des chevaux \ngaloper dans votre direction, le long de la rive gauche. Si vous \nsouhaitez vous cacher au fond du cano??, rendez-vous au 75. Si \nvous pr??f??rez au contraire attirer l\'attention des cavaliers, \nrendez-vous au 175. Si vous ma??trisez la Discipline Ka?? du \nSixi??me Sens, rendez-vous au 218.\n</p>'),
(10, 2, 4, '<h1>Chapitre 4</h1>\n<p>\nC\'est un petit cano?? ?? une place, en tr??s mauvais ??tat. Des pi??ces \nde bois disjointes laissent appara??tre des trous en plusieurs \nendroits de la coque et il vous faut les boucher ?? la h??te avec de \nl\'argile. Vous videz ensuite l\'embarcation de son eau et il vous \nsemble alors qu\'elle est en ??tat de flotter. Vous rangez votre \n??quipement ?? l\'avant du cano??, puis vous descendez le cours de \nla rivi??re en pagayant ?? l\'aide d\'un d??bris de bois ramass?? ?? la \nsurface de l\'eau. Un instant plus tard, vous entendez des chevaux \ngaloper dans votre direction, le long de la rive gauche. Si vous \nsouhaitez vous cacher au fond du cano??, rendez-vous au 75. Si \nvous pr??f??rez au contraire attirer l\'attention des cavaliers, \nrendez-vous au 175. Si vous ma??trisez la Discipline Ka?? du \nSixi??me Sens, rendez-vous au 218.\n</p>'),
(11, 1, 5, '<h1>Chapitre 5</h1>\n<p>\nVous avez march?? pendant environ une heure lorsque le sentier \ns\'oriente peu ?? peu vers l\'est. Vous atteignez bient??t un gu?? qui \ntraverse un ruisseau coulant vers le sud. Le courant en est rapide \net le lit, rocheux et escarp??. Au-del?? du gu??, le sentier que vous \nsuivez croise un chemin plus large, orient?? nord-sud. En allant \nvers le nord, vous vous ??loigneriez de la capitale et vous d??cidez \ndonc de prendre ?? droite, en direction du sud. Rendez-vous au\n111.\n</p>'),
(12, 2, 5, '<h1>Chapitre 5</h1>\n<p>\nVous avez march?? pendant environ une heure lorsque le sentier \ns\'oriente peu ?? peu vers l\'est. Vous atteignez bient??t un gu?? qui \ntraverse un ruisseau coulant vers le sud. Le courant en est rapide \net le lit, rocheux et escarp??. Au-del?? du gu??, le sentier que vous \nsuivez croise un chemin plus large, orient?? nord-sud. En allant \nvers le nord, vous vous ??loigneriez de la capitale et vous d??cidez \ndonc de prendre ?? droite, en direction du sud. Rendez-vous au\n111.\n</p>');

-- --------------------------------------------------------

--
-- Table structure for table `feuilles_aventure`
--
-- Creation: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `feuilles_aventure`;
CREATE TABLE IF NOT EXISTS `feuilles_aventure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_save` int(11) NOT NULL,
  `discipline` text,
  `armes` text,
  `objets_sac` text,
  `repas_sac` text,
  `habileter` text,
  `endurance` text,
  `objets_speciaux` text,
  `bourse` text,
  `endurance_loup` text,
  `quotien_attaque` text,
  `endurance_ennemie` text,
  PRIMARY KEY (`id`),
  KEY `id_save` (`id_save`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `livres`
--
-- Creation: Nov 11, 2021 at 08:12 PM
-- Last update: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `livres`;
CREATE TABLE IF NOT EXISTS `livres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(150) NOT NULL,
  `isbn` varchar(255) NOT NULL,
  `auteur` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `livres`
--

INSERT INTO `livres` (`id`, `titre`, `isbn`, `auteur`) VALUES
(1, 'Les Ma??tre Des T??n??bres', 'esbf123456789', 'Joe Dever et Gary Chalk'),
(2, 'Les Ma??tre Des T??n??bres II', 'e234dfg877789', 'Joe Dever et Gary Chalk'),
(3, 'Les Ma??tre Des T??n??bres III', '11d4dkvl67789', 'Joe Dever et Gary Chalk'),
(4, 'Les Ma??tre Des T??n??bres IV', 'edkfws09ki54789', 'Joe Dever et Gary Chalk');

-- --------------------------------------------------------

--
-- Table structure for table `permission_livres_usagers`
--
-- Creation: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `permission_livres_usagers`;
CREATE TABLE IF NOT EXISTS `permission_livres_usagers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_usager` int(11) NOT NULL,
  `id_livre` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usager` (`id_usager`),
  KEY `id_livre` (`id_livre`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `permission_livres_usagers`
--

INSERT INTO `permission_livres_usagers` (`id`, `id_usager`, `id_livre`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 1, 2),
(6, 2, 2),
(7, 3, 2),
(8, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `sauvegardes_parties`
--
-- Creation: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `sauvegardes_parties`;
CREATE TABLE IF NOT EXISTS `sauvegardes_parties` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_usager` int(11) NOT NULL,
  `id_livre` int(11) NOT NULL,
  `id_chapitre` int(11) NOT NULL,
  `page` tinyint(8) DEFAULT NULL,
  `date_partie` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_usager` (`id_usager`),
  KEY `id_livre` (`id_livre`),
  KEY `id_chapitre` (`id_chapitre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usagers`
--
-- Creation: Nov 11, 2021 at 08:12 PM
-- Last update: Nov 11, 2021 at 08:12 PM
--

DROP TABLE IF EXISTS `usagers`;
CREATE TABLE IF NOT EXISTS `usagers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prenom` varchar(50) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `age` tinyint(3) DEFAULT NULL,
  `courriel` varchar(255) NOT NULL,
  `mot_de_passe` varchar(512) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `usagers`
--

INSERT INTO `usagers` (`id`, `prenom`, `nom`, `age`, `courriel`, `mot_de_passe`) VALUES
(1, 'Bob', 'Dumoulin', 13, 'triangle1232009@Hotmail.com', 'daaad6e5604e8e17bd9f108d91e26afe6281dac8fda0091040a7a6d7bd9b43b5'),
(2, 'John', 'Dumoulin', 18, 'whateverid@Hotmail.com', '01c4c0092dc6f090f2d58115c9df6aaebdd5adc595df12bd5dffcc8eaae33006'),
(3, 'Lulu', 'Dumoulin', 21, 'imashutthisoff@ny.com', 'fab6d43655bbca6e71240739f3aad3f9050b5a051924ab3a3bd17a9678525a74'),
(4, 'Allan', 'Dumoulin', 32, 'momoiscool@Hotmail.com', '58f3e330fe458b29f3b50d1cdbe2bf10007f528ba883e2061db944030f504e9a');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chapitres_livres`
--
ALTER TABLE `chapitres_livres`
  ADD CONSTRAINT `chapitres_livres_ibfk_1` FOREIGN KEY (`id_livre`) REFERENCES `livres` (`id`);

--
-- Constraints for table `feuilles_aventure`
--
ALTER TABLE `feuilles_aventure`
  ADD CONSTRAINT `feuilles_aventure_ibfk_1` FOREIGN KEY (`id_save`) REFERENCES `sauvegardes_parties` (`id`);

--
-- Constraints for table `permission_livres_usagers`
--
ALTER TABLE `permission_livres_usagers`
  ADD CONSTRAINT `permission_livres_usagers_ibfk_1` FOREIGN KEY (`id_usager`) REFERENCES `usagers` (`id`),
  ADD CONSTRAINT `permission_livres_usagers_ibfk_2` FOREIGN KEY (`id_livre`) REFERENCES `livres` (`id`);

--
-- Constraints for table `sauvegardes_parties`
--
ALTER TABLE `sauvegardes_parties`
  ADD CONSTRAINT `sauvegardes_parties_ibfk_1` FOREIGN KEY (`id_usager`) REFERENCES `usagers` (`id`),
  ADD CONSTRAINT `sauvegardes_parties_ibfk_2` FOREIGN KEY (`id_livre`) REFERENCES `livres` (`id`),
  ADD CONSTRAINT `sauvegardes_parties_ibfk_3` FOREIGN KEY (`id_chapitre`) REFERENCES `chapitres_livres` (`id`);
COMMIT;




DROP TRIGGER IF EXISTS titre_livre_maj;
DELIMITER $$
/* S'assurrer que la premi??re lettre du titre d'un livre ins??r?? dans la bd sois en Majuscule! (?? l'insertion)*/	
CREATE TRIGGER titre_livre_maj BEFORE INSERT ON livres
  FOR EACH ROW
	BEGIN
		SET NEW.titre = Concat(UPPER(LEFT(NEW.titre,1)),LOWER(SUBSTRING(NEW.titre,2)));
	END $$        
DELIMITER ;

DROP TRIGGER IF EXISTS verif_courriel;
DELIMITER $$
/* V??rifier que le courriel n'est pas vide et que le @ soit pr??sent, sinon l??ve une execption.*/
CREATE TRIGGER verif_courriel BEFORE INSERT ON usagers
  FOR EACH ROW
	BEGIN
    DECLARE msg VARCHAR(128);
    
    IF NEW.courriel IS NOT NULL AND NEW.courriel LIKE '%@%' THEN 
          SET NEW.courriel = NEW.courriel;
	ELSE
        SET msg = concat('CourrielTriggerErreur: Courriel invalide sans @ ou courriel vide. D??sol??!: ', cast(NEW.courriel AS CHAR));
        SIGNAL SQLSTATE '45000' set message_text = msg;
    END IF;
		
	END $$        
	
DELIMITER ;


CREATE USER 'legarsdulivre'@'localhost' IDENTIFIED BY '123456';
GRANT SELECT, INSERT, UPDATE, EXECUTE ON `python_book_hero`.* TO `legarsdulivre`@`localhost`;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
