/* Création de la table Administration */
CREATE TABLE Administration (
    id_ad INT(10),
    Nom_ad VARCHAR(50),
    Prenoms_ad VARCHAR(100),
    Email VARCHAR(50) NOT NULL
);

/* Insertion de quelques enregistrements */
INSERT INTO Administration (id_ad, Nom_ad, Prenoms_ad, Email)
VALUES (2454, "ZANNOU", "Jean", "jeanz@gmail.com"),
       (3553, "OGBO", "Sophie", "ogbosophie@gmail.com"),
       (2232, "SOSSA", "Pierre", "sopierre@gmail.com");

/* Affichage des enregistrements insérés */
SELECT * FROM Administration;


/* Création de la table Filiere */
CREATE TABLE Filiere (
    id_fil INT(8),
    Nom_fil VARCHAR(50) NOT NULL,
    INDEX(id_fil)
);

/* Insertion de quelques enregistrements */
INSERT INTO Filiere (id_fil, Nom_fil)
VALUES (0009, "Intelligence Artificielle"),
       (0004, "Génie Logiciel "),
       (0002, "Internet et Multimédia"),
       (0007, "Sécurité Informatique"),
       (0005, "Système Embarqué"); 

/* Affichage des enregistrements insérés */
SELECT * FROM Filiere;


/* Création de la table Etudiants */
CREATE TABLE Etudiants (
    Matricule INT(10) NOT NULL,
    Nom VARCHAR(50),
    Prenoms VARCHAR(100),
    Email VARCHAR(100) NOT NULL,
    Sexe ENUM('M', 'F') NOT NULL,
    Age INT(2) NOT NULL,
    Semestre INT(1),
    id_fil INT, 
    FOREIGN KEY (id_fil) REFERENCES Filiere(id_fil)
);

/* Insertion de quelques enregistrements */
INSERT INTO Etudiants (Matricule, Nom, Prenoms, Email, Sexe, Age, Semestre, id_fil)
VALUES (12357553, "KAKA", "Jean", "kakajean@gmail.com", "M", 20, 1, 0004),
       (24421134, "AGA", "Rose",  "arose@gmail.com", "F", 22, 4, 0005),
       (56523077, "Dubois", "Pierre", "pdubois@gmail.com", "M", 19, 1, 0009);

/* Affichage des enregistrements insérés */
SELECT * FROM Etudiants;


/* Création de la table Salle */
CREATE TABLE Salle (
    id_sal INT(8),
    Nom_sal VARCHAR(50),
    Capacite INT(4) NOT NULL,
    INDEX(id_sal)
);

/* Insertion de quelques enregistrements */
INSERT INTO Salle (id_sal, Nom_sal, Capacite)
VALUES (355, "IRAN 1", 500),
       (688, "IRAN 2", 396),
       (098, "PADTICE", 200),
       (665, "MOOCS", 70);

/* Affichage des enregistrements insérés */
SELECT * FROM Salle;



/* Création de la table UE */
CREATE TABLE UE (
    Code_ue INT(8) NOT NULL,
    Nom_ue VARCHAR(50) NOT NULL,
    Credits INT(1) NOT NULL,
    Semestre INT(1) NOT NULL,
    INDEX(Code_ue)
);

/* Insertion de quelques enregistrements */
INSERT INTO UE (Code_ue, Nom_ue, Credits, Semestre)
VALUES (34425, "Mathématiques générales", 5, 1),
       (57800, "Programmation", 4, 1),
       (54432, "Anglais", 1, 1),
       (5665, "TEEO", 2, 1),
       (57810, "Programmation avancée", 2, 2);

/* Affichage des enregistrements insérés */
SELECT * FROM UE;


/* Création de la table Matiere */
CREATE TABLE Matiere (
    id_mat INT(8),
    Nom_mat VARCHAR(50),
    Horaires INT(2),
    Code_ue INT,
    FOREIGN KEY (Code_ue) REFERENCES UE(Code_ue),
    INDEX(id_mat)
);

/* Insertion de quelques enregistrements */
INSERT INTO Matiere (id_mat, Nom_mat, Horaires, Code_ue)
VALUES (3442, "Statistique", 20, 34425),
       (5780, "Mathématiques discrètes", 30, 34425),
       (5432, "Langage Python", 25, 57810),
       (0665, "TEEO", 15, 5665),
       (5784, "Anglais informatique", 2, 54432);

/* Affichage des enregistrements insérés */
SELECT * FROM Matiere;


/* Création de la table Professeurs */
CREATE TABLE Professeurs (
    id_prof INT(10),
    Nom_prof VARCHAR(50),
    Prenoms_prof VARCHAR(100),
    Sexe VARCHAR(1),
    Email_prof VARCHAR(50) NOT NULL,
    id_mat INT,
    FOREIGN KEY (id_mat) REFERENCES Matiere(id_mat),
    INDEX(id_prof)
);

/* Insertion de quelques enregistrements */
INSERT INTO Professeurs (id_prof, Nom_prof, Prenoms_prof, Sexe, Email_prof, id_mat)
VALUES (2454, "SAMOU", "Jack", "M", "jeansamou@gmail.com", 5784),
       (3553, "OGO", "Ruby", "F", "oruby@gmail.com", 0665),
       (2232, "ABLO", "John", "M", "johnablo@gmail.com", 5432);

/* Affichage des enregistrements insérés */
SELECT * FROM Professeurs;



/* Création de la table EmploiDuTemps */
CREATE TABLE EmploiDuTemps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    semaine_debut DATE,
    semaine_fin DATE,
    jour_semaine VARCHAR(20),
    heure_debut TIME,
    heure_fin TIME,
    id_prof INT,
    id_mat INT,
    id_sal INT,
    FOREIGN KEY (id_prof) REFERENCES Professeurs(id_prof),
    FOREIGN KEY (id_mat) REFERENCES Matiere(id_mat),
    FOREIGN KEY (id_sal) REFERENCES Salle(id_sal)
);

/* Insertion de quelques enregistrements */
INSERT INTO EmploiDuTemps (semaine_debut, semaine_fin, jour_semaine, heure_debut, heure_fin, id_prof, id_mat, id_sal)
VALUES
    -- Lundi
    ('2023-05-15', '2023-05-21', 'Lundi', '09:00:00', '11:00:00', 2454, 5784, 355),
    ('2023-05-15', '2023-05-21', 'Lundi', '11:30:00', '13:30:00', 3553, 665, 688),
    -- Mardi
    ('2023-05-15', '2023-05-21', 'Mardi', '09:00:00', '11:00:00', 2232, 5432, 98),
    ('2023-05-15', '2023-05-21', 'Mardi', '11:30:00', '13:30:00', 3553, 665, 98),
    -- Mercredi
    ('2023-05-15', '2023-05-21', 'Mercredi', '09:00:00', '11:00:00', 2454, 5784, 355),
    ('2023-05-15', '2023-05-21', 'Mercredi', '11:30:00', '13:30:00', 2232, 5432, 665),
    -- Jeudi
    ('2023-05-15', '2023-05-21', 'Jeudi', '09:00:00', '11:00:00', 2454, 5784, 665),
    ('2023-05-15', '2023-05-21', 'Jeudi', '11:30:00', '13:30:00', 2232, 5432, 688),
    -- Vendredi
    ('2023-05-15', '2023-05-21', 'Vendredi', '09:00:00', '11:00:00',3553,  665, 98),
    ('2023-05-15', '2023-05-21', 'Vendredi', '11:30:00', '13:30:00', 2232, 5432, 98),
    -- Samedi
    ('2023-05-15', '2023-05-21', 'Samedi', '09:00:00', '11:00:00', 3553, 665, 355),
    ('2023-05-15', '2023-05-21', 'Samedi', '11:30:00', '13:30:00', 2454, 5784, 355);



SELECT e.id, e.semaine_debut, e.semaine_fin, e.jour_semaine, e.heure_debut, e.heure_fin, p.Nom_prof, p.Prenoms_prof, m.Nom_mat, s.Nom_sal
FROM EmploiDuTemps e
JOIN Professeurs p ON e.id_prof = p.id_prof
JOIN Matiere m ON e.id_mat = m.id_mat
JOIN Salle s ON e.id_sal = s.id_sal;

