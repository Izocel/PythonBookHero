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
(1, 1, 0, '<h1>Introduction: Avertir le roi</h1>\n<p>\nAu nord du royaume du Sommerlund, il est de tradition depuis \ndes siècles d\'envoyer les fils des Seigneurs de la Guerre au \nmonastère Kaï. C\'est là qu\'on leur enseigne l\'art et la science de \nleurs nobles ancêtres.\nLes Moines Kaï sont de grands maîtres dans l\'art qu\'ils \nenseignent. Pour transmettre leurs connaissances, ils doivent \nfaire subir à leurs disciples de rudes épreuves au cours de leur \napprentissage, mais ces derniers ne s\'en plaignent jamais. Ils leur \ntémoignent au contraire amour et respect, sachant très bien \nqu\'ils quitteront un jour le monastère en possédant tous les \nsecrets de la tradition Kaï: ils pourront alors rentrer chez eux, \nl\'esprit et le corps formés aux techniques de la guerre. \nProfondément attachés à leur patrie, ils seront ainsi prêts à la \ndéfendre contre le danger constant qui la menace : la soif de \nconquête des Maîtres des Ténèbres venus de l\'ouest.\nAu temps jadis, à l\'époque de la Lune Noire, les Maîtres des \nTénèbres menèrent une guerre sans merci contre le royaume du \nSommerlund. Ce fut une longue et douloureuse épreuve de force \nà l\'issue de laquelle les guerriers du Sommerlund remportèrent la \nvictoire lors de la grande bataille de Maaken. Le roi Ulnar et ses \nalliés de Durenor anéantirent l\'armée des Maîtres des Ténèbres \ndans le défilé de Moytura et précipitèrent l\'ennemi au fond de la \ngorge de Maaken. Vashna, le plus puissant parmi les Maîtres des \nTénèbres, périt d\'un coup mortel que le roi Ulnar lui porta de sa \npuissante épée, l\'Epée du Soleil, que l\'on désigne généralement \nsous le nom de «Glaive de Sommer». Depuis ce temps, les \nMaîtres des Ténèbres ont juré de prendre leur revanche sur le \nroyaume du Sommerlund et la Maison d\'Ulnar.\nLorsque l\'aube se lève sur le premier jour de votre aventure, tous \nles Seigneurs Kaï sont présents au monastère : on doit, en effet, \ncélébrer aujourd\'hui même la grande fête de Fehmarn et l\'on se \nprépare tôt le matin aux réjouissances. Mais soudain, un \nimmense nuage noir s\'élève au ciel d\'occident: d\'énormes \ncréatures aux ailes sombres emplissent les nues en si grand \nnombre que le soleil semble s\'éteindre. Cette invasion porte la \nmarque des Maîtres des Ténèbres. Les ennemis jurés du \nRoyaume du Sommerlund passent une nouvelle fois à l\'attaque : \nla guerre a recommencé. En ce matin fatal, Loup Silencieux (c\'est \nle nom qui vous a été donné par les Moines Kaï) est allé chercher \ndu bois dans la forêt : c\'est la corvée qu\'on vous a assignée pour \nvous punir de votre inattention en classe. Or, sur le chemin du \nretour, vous apercevez tout à coup ce gigantesque nuage de \ncréatures noires qui fond sur le monastère et semble l\'engloutir \naussitôt. Vous laissez tomber votre bois à terre et vous vous \nprécipitez sur le lieu de la bataille. Mais les monstres noirs ont \nobscurci le soleil et il fait à présent si sombre que vous trébuchez \ncontre une racine en tombant tête la première. Dans votre chute, \nvous heurtez violemment du front une branche basse qui vous \nassomme. Une fraction de seconde avant de perdre \nconnaissance, vous avez cependant le temps de saisir du regard \nun terrifiant spectacle: les murs du monastère Kaï sont en train \nde s\'écrouler sur eux-mêmes dans un fracas de tonnerre. Vous ne \nreprenez conscience qu\'au bout de plusieurs heures et, les larmes \naux yeux, vous contemplez avec horreur le tas de ruines que \nl\'ennemi a laissé derrière lui. Les Guerriers Kaï ont été ensevelis \nsous les décombres et il ne reste plus aucun survivant parmi vos \ncompagnons. Avec une infinie douleur, vous levez alors votre \nvisage vers le ciel, à nouveau clair, et vous faites le serment de \nvenger la mort des Moines et des Seigneurs Kaï. Vous ferez payer \nleur crime aux Maîtres des Ténèbres ! Votre tâche d\'ailleurs \ncommence à l\'instant même : il vous faut, en effet, gagner la \ncapitale du royaume pour prévenir le Roi en personne de \nl\'effroyable péril qui menace le pays ; car maintenant, l\'ennemi \nest en marche, et si vous n\'agissez pas à temps, votre patrie \ntombera sous son joug. Vous êtes le dernier des Seigneurs Kaï et \nle sort de votre peuple repose désormais entre vos seules mains: \nle Loup Silencieux est devenu Loup Solitaire et les envahisseurs \nferont tout pour vous empêcher d\'atteindre le Palais du Roi....\n</p>'),
(2, 2, 0, '<h1>Introduction: Avertir le roi</h1>\n<p>\nAu nord du royaume du Sommerlund, il est de tradition depuis \ndes siècles d\'envoyer les fils des Seigneurs de la Guerre au \nmonastère Kaï. C\'est là qu\'on leur enseigne l\'art et la science de \nleurs nobles ancêtres.\nLes Moines Kaï sont de grands maîtres dans l\'art qu\'ils \nenseignent. Pour transmettre leurs connaissances, ils doivent \nfaire subir à leurs disciples de rudes épreuves au cours de leur \napprentissage, mais ces derniers ne s\'en plaignent jamais. Ils leur \ntémoignent au contraire amour et respect, sachant très bien \nqu\'ils quitteront un jour le monastère en possédant tous les \nsecrets de la tradition Kaï: ils pourront alors rentrer chez eux, \nl\'esprit et le corps formés aux techniques de la guerre. \nProfondément attachés à leur patrie, ils seront ainsi prêts à la \ndéfendre contre le danger constant qui la menace : la soif de \nconquête des Maîtres des Ténèbres venus de l\'ouest.\nAu temps jadis, à l\'époque de la Lune Noire, les Maîtres des \nTénèbres menèrent une guerre sans merci contre le royaume du \nSommerlund. Ce fut une longue et douloureuse épreuve de force \nà l\'issue de laquelle les guerriers du Sommerlund remportèrent la \nvictoire lors de la grande bataille de Maaken. Le roi Ulnar et ses \nalliés de Durenor anéantirent l\'armée des Maîtres des Ténèbres \ndans le défilé de Moytura et précipitèrent l\'ennemi au fond de la \ngorge de Maaken. Vashna, le plus puissant parmi les Maîtres des \nTénèbres, périt d\'un coup mortel que le roi Ulnar lui porta de sa \npuissante épée, l\'Epée du Soleil, que l\'on désigne généralement \nsous le nom de «Glaive de Sommer». Depuis ce temps, les \nMaîtres des Ténèbres ont juré de prendre leur revanche sur le \nroyaume du Sommerlund et la Maison d\'Ulnar.\nLorsque l\'aube se lève sur le premier jour de votre aventure, tous \nles Seigneurs Kaï sont présents au monastère : on doit, en effet, \ncélébrer aujourd\'hui même la grande fête de Fehmarn et l\'on se \nprépare tôt le matin aux réjouissances. Mais soudain, un \nimmense nuage noir s\'élève au ciel d\'occident: d\'énormes \ncréatures aux ailes sombres emplissent les nues en si grand \nnombre que le soleil semble s\'éteindre. Cette invasion porte la \nmarque des Maîtres des Ténèbres. Les ennemis jurés du \nRoyaume du Sommerlund passent une nouvelle fois à l\'attaque : \nla guerre a recommencé. En ce matin fatal, Loup Silencieux (c\'est \nle nom qui vous a été donné par les Moines Kaï) est allé chercher \ndu bois dans la forêt : c\'est la corvée qu\'on vous a assignée pour \nvous punir de votre inattention en classe. Or, sur le chemin du \nretour, vous apercevez tout à coup ce gigantesque nuage de \ncréatures noires qui fond sur le monastère et semble l\'engloutir \naussitôt. Vous laissez tomber votre bois à terre et vous vous \nprécipitez sur le lieu de la bataille. Mais les monstres noirs ont \nobscurci le soleil et il fait à présent si sombre que vous trébuchez \ncontre une racine en tombant tête la première. Dans votre chute, \nvous heurtez violemment du front une branche basse qui vous \nassomme. Une fraction de seconde avant de perdre \nconnaissance, vous avez cependant le temps de saisir du regard \nun terrifiant spectacle: les murs du monastère Kaï sont en train \nde s\'écrouler sur eux-mêmes dans un fracas de tonnerre. Vous ne \nreprenez conscience qu\'au bout de plusieurs heures et, les larmes \naux yeux, vous contemplez avec horreur le tas de ruines que \nl\'ennemi a laissé derrière lui. Les Guerriers Kaï ont été ensevelis \nsous les décombres et il ne reste plus aucun survivant parmi vos \ncompagnons. Avec une infinie douleur, vous levez alors votre \nvisage vers le ciel, à nouveau clair, et vous faites le serment de \nvenger la mort des Moines et des Seigneurs Kaï. Vous ferez payer \nleur crime aux Maîtres des Ténèbres ! Votre tâche d\'ailleurs \ncommence à l\'instant même : il vous faut, en effet, gagner la \ncapitale du royaume pour prévenir le Roi en personne de \nl\'effroyable péril qui menace le pays ; car maintenant, l\'ennemi \nest en marche, et si vous n\'agissez pas à temps, votre patrie \ntombera sous son joug. Vous êtes le dernier des Seigneurs Kaï et \nle sort de votre peuple repose désormais entre vos seules mains: \nle Loup Silencieux est devenu Loup Solitaire et les envahisseurs \nferont tout pour vous empêcher d\'atteindre le Palais du Roi....\n</p>'),
(3, 1, 1, '<h1>Chapitre 1</h1>\n<p>\nIl faut vous hâter, car quelque chose vous dit qu\'il serait \nimprudent de vous attarder parmi les ruines fumantes du \nmonastère détruit. Les monstres volants peuvent, en effet, \nreparaître à tout moment. Il n\'y a d\'ailleurs pas de temps à \nperdre : vous devez au plus vite prendre la route de Holmgard, la \ncapitale du Sommerlund, pour aller annoncer au Roi cette \nterrible nouvelle : les Guerriers Kaï, l\'élite du pays, ont tous été \nmassacrés, à l\'exception de vous-même. Or sans l\'autorité et le \nsavoir des Seigneurs Kaï pour commander l\'armée, le royaume \ndu Sommerlund se trouve à la merci de ses plus anciens \nennemis: les Maîtres des Ténèbres. En retenant vos larmes à \ngrand-peine, vous dites adieu à vos compagnons morts et vous \nfaites le serment de les venger. Vous tournez alors le dos aux \nruines et vous descendez avec précaution le sentier escarpé qui \ns\'ouvre devant vous. Au pied de la colline, le chemin aboutit à \nune bifurcation. Là, deux autres sentiers mènent l\'un et l\'autre à \nune grande forêt en empruntant deux directions différentes. Si \nvous souhaitez prendre le sentier de droite, rendez-vous au 85.\nSi vous préférez suivre celui de gauche, rendez-vous au 275.\nEnfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, \nrendez-vous au 141.\n</p>'),
(4, 2, 1, '<h1>Chapitre 1</h1>\n<p>\nIl faut vous hâter, car quelque chose vous dit qu\'il serait \nimprudent de vous attarder parmi les ruines fumantes du \nmonastère détruit. Les monstres volants peuvent, en effet, \nreparaître à tout moment. Il n\'y a d\'ailleurs pas de temps à \nperdre : vous devez au plus vite prendre la route de Holmgard, la \ncapitale du Sommerlund, pour aller annoncer au Roi cette \nterrible nouvelle : les Guerriers Kaï, l\'élite du pays, ont tous été \nmassacrés, à l\'exception de vous-même. Or sans l\'autorité et le \nsavoir des Seigneurs Kaï pour commander l\'armée, le royaume \ndu Sommerlund se trouve à la merci de ses plus anciens \nennemis: les Maîtres des Ténèbres. En retenant vos larmes à \ngrand-peine, vous dites adieu à vos compagnons morts et vous \nfaites le serment de les venger. Vous tournez alors le dos aux \nruines et vous descendez avec précaution le sentier escarpé qui \ns\'ouvre devant vous. Au pied de la colline, le chemin aboutit à \nune bifurcation. Là, deux autres sentiers mènent l\'un et l\'autre à \nune grande forêt en empruntant deux directions différentes. Si \nvous souhaitez prendre le sentier de droite, rendez-vous au 85.\nSi vous préférez suivre celui de gauche, rendez-vous au 275.\nEnfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, \nrendez-vous au 141.\n</p>'),
(5, 1, 2, '<h1>Chapitre 2</h1>\n<p>\nTandis que vous courez à perdre haleine dans la forêt qui \ns\'épaissit, les cris des Gloks s\'évanouissent peu à peu derrière \nvous. Vous les avez presque semés lorsque vous trébuchez \nsoudain en tombant tête la première dans un enchevêtrement de \nbranches basses. Utilisez la Table de Hasard pour obtenir un \nchiffre. Si vous tirez entre 0 et 4, rendez-vous au 343. Entre 5 et \n9, rendez-vous au 276.\n</p>'),
(6, 2, 2, '<h1>Chapitre 2</h1>\n<p>\nTandis que vous courez à perdre haleine dans la forêt qui \ns\'épaissit, les cris des Gloks s\'évanouissent peu à peu derrière \nvous. Vous les avez presque semés lorsque vous trébuchez \nsoudain en tombant tête la première dans un enchevêtrement de \nbranches basses. Utilisez la Table de Hasard pour obtenir un \nchiffre. Si vous tirez entre 0 et 4, rendez-vous au 343. Entre 5 et \n9, rendez-vous au 276.\n</p>'),
(7, 1, 3, '<h1>Chapitre 3</h1>\n<p>\nVous emboîtez le pas à l\'officier qui franchit une porte en arcade, \npuis monte quelques marches menant à un grand hall. Des \nsoldats courent en tous sens, porteurs de parchemins ornés qu\'ils \ndoivent remettre à des officiers postés le long des murs de la \nville. Un homme au visage couturé de cicatrices, l\'air hagard, \ns\'approche de vous et vous offre de le suivre jusqu\'à la citadelle. \nIl porte la toge blanche et pourpre en usage à la cour du Roi. Si \nvous souhaitez suivre cet homme, rendez-vous au 196. Si vous \npréférez décliner son offre et retourner dans les rues populeuses, \nrendez-vous au 144.\n</p>'),
(8, 2, 3, '<h1>Chapitre 3</h1>\n<p>\nVous emboîtez le pas à l\'officier qui franchit une porte en arcade, \npuis monte quelques marches menant à un grand hall. Des \nsoldats courent en tous sens, porteurs de parchemins ornés qu\'ils \ndoivent remettre à des officiers postés le long des murs de la \nville. Un homme au visage couturé de cicatrices, l\'air hagard, \ns\'approche de vous et vous offre de le suivre jusqu\'à la citadelle. \nIl porte la toge blanche et pourpre en usage à la cour du Roi. Si \nvous souhaitez suivre cet homme, rendez-vous au 196. Si vous \npréférez décliner son offre et retourner dans les rues populeuses, \nrendez-vous au 144.\n</p>'),
(9, 1, 4, '<h1>Chapitre 4</h1>\n<p>\nC\'est un petit canoë à une place, en très mauvais état. Des pièces \nde bois disjointes laissent apparaître des trous en plusieurs \nendroits de la coque et il vous faut les boucher à la hâte avec de \nl\'argile. Vous videz ensuite l\'embarcation de son eau et il vous \nsemble alors qu\'elle est en état de flotter. Vous rangez votre \néquipement à l\'avant du canoë, puis vous descendez le cours de \nla rivière en pagayant à l\'aide d\'un débris de bois ramassé à la \nsurface de l\'eau. Un instant plus tard, vous entendez des chevaux \ngaloper dans votre direction, le long de la rive gauche. Si vous \nsouhaitez vous cacher au fond du canoë, rendez-vous au 75. Si \nvous préférez au contraire attirer l\'attention des cavaliers, \nrendez-vous au 175. Si vous maîtrisez la Discipline Kaï du \nSixième Sens, rendez-vous au 218.\n</p>'),
(10, 2, 4, '<h1>Chapitre 4</h1>\n<p>\nC\'est un petit canoë à une place, en très mauvais état. Des pièces \nde bois disjointes laissent apparaître des trous en plusieurs \nendroits de la coque et il vous faut les boucher à la hâte avec de \nl\'argile. Vous videz ensuite l\'embarcation de son eau et il vous \nsemble alors qu\'elle est en état de flotter. Vous rangez votre \néquipement à l\'avant du canoë, puis vous descendez le cours de \nla rivière en pagayant à l\'aide d\'un débris de bois ramassé à la \nsurface de l\'eau. Un instant plus tard, vous entendez des chevaux \ngaloper dans votre direction, le long de la rive gauche. Si vous \nsouhaitez vous cacher au fond du canoë, rendez-vous au 75. Si \nvous préférez au contraire attirer l\'attention des cavaliers, \nrendez-vous au 175. Si vous maîtrisez la Discipline Kaï du \nSixième Sens, rendez-vous au 218.\n</p>'),
(11, 1, 5, '<h1>Chapitre 5</h1>\n<p>\nVous avez marché pendant environ une heure lorsque le sentier \ns\'oriente peu à peu vers l\'est. Vous atteignez bientôt un gué qui \ntraverse un ruisseau coulant vers le sud. Le courant en est rapide \net le lit, rocheux et escarpé. Au-delà du gué, le sentier que vous \nsuivez croise un chemin plus large, orienté nord-sud. En allant \nvers le nord, vous vous éloigneriez de la capitale et vous décidez \ndonc de prendre à droite, en direction du sud. Rendez-vous au\n111.\n</p>'),
(12, 2, 5, '<h1>Chapitre 5</h1>\n<p>\nVous avez marché pendant environ une heure lorsque le sentier \ns\'oriente peu à peu vers l\'est. Vous atteignez bientôt un gué qui \ntraverse un ruisseau coulant vers le sud. Le courant en est rapide \net le lit, rocheux et escarpé. Au-delà du gué, le sentier que vous \nsuivez croise un chemin plus large, orienté nord-sud. En allant \nvers le nord, vous vous éloigneriez de la capitale et vous décidez \ndonc de prendre à droite, en direction du sud. Rendez-vous au\n111.\n</p>');

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
(1, 'Les Maître Des Ténèbres', 'esbf123456789', 'Joe Dever et Gary Chalk'),
(2, 'Les Maître Des Ténèbres II', 'e234dfg877789', 'Joe Dever et Gary Chalk'),
(3, 'Les Maître Des Ténèbres III', '11d4dkvl67789', 'Joe Dever et Gary Chalk'),
(4, 'Les Maître Des Ténèbres IV', 'edkfws09ki54789', 'Joe Dever et Gary Chalk');

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
/* S'assurrer que la première lettre du titre d'un livre inséré dans la bd sois en Majuscule! (À l'insertion)*/	
CREATE TRIGGER titre_livre_maj BEFORE INSERT ON livres
  FOR EACH ROW
	BEGIN
		SET NEW.titre = Concat(UPPER(LEFT(NEW.titre,1)),LOWER(SUBSTRING(NEW.titre,2)));
	END $$        
DELIMITER ;

DROP TRIGGER IF EXISTS verif_courriel;
DELIMITER $$
/* Vérifier que le courriel n'est pas vide et que le @ soit présent, sinon lève une execption.*/
CREATE TRIGGER verif_courriel BEFORE INSERT ON usagers
  FOR EACH ROW
	BEGIN
    DECLARE msg VARCHAR(128);
    
    IF NEW.courriel IS NOT NULL AND NEW.courriel LIKE '%@%' THEN 
          SET NEW.courriel = NEW.courriel;
	ELSE
        SET msg = concat('CourrielTriggerErreur: Courriel invalide sans @ ou courriel vide. Désolé!: ', cast(NEW.courriel AS CHAR));
        SIGNAL SQLSTATE '45000' set message_text = msg;
    END IF;
		
	END $$        
	
DELIMITER ;


CREATE USER 'legarsdulivre'@'localhost' IDENTIFIED BY '123456';
GRANT SELECT, INSERT, UPDATE, EXECUTE ON `python_book_hero`.* TO `legarsdulivre`@`localhost`;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
