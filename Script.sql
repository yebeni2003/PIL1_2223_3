CREATE DATABASE TIMEPLAN;
USE TIMEPLAN;
-- Création de la table Filières
CREATE TABLE Filières (
    id_Fil INT(10) NOT NULL,
    nom_Fil VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_Fil)
);
-- Création de la table Etudiants

CREATE TABLE Etudiants (
    matricule_Etu INT(10) NOT NULL,
    nom_Etu VARCHAR(50) NOT NULL,
    prenom_Etu VARCHAR(100) NOT NULL,
    sexe_Etu VARCHAR(1) NOT NULL,
    date_nais_Etu DATE,
    age_Etu INT(3) NOT NULL,
    Contact INT(8) UNIQUE NOT NULL,
    email_Etu VARCHAR(100) UNIQUE NOT NULL,
    PRIMARY KEY (matricule_Etu),
    id_Fil INT(10),
    FOREIGN KEY (id_Fil) REFERENCES Filières(id_Fil)
);

-- Insertion des données dans la table Etudiants
INSERT INTO Etudiants (matricule_Etu, nom_Etu, prenom_Etu, sexe_Etu, date_nais_Etu, age_Etu, Contact, email_Etu, id_Fil)
VALUES ('125872', 'ADO', 'PAUL', 'M', '2002-02-24', '21', '94215898', 'paulado@gmail.com', 1),
       ('125225', 'DOKO', 'Clarisse', 'F', '2005-11-30', '18', '95052141', 'clarisedoko@gmail.com', 2),
       ('172853', 'ADOGBE', 'Pierre', 'M', '2000-07-28', '23', '90545825', 'adopierre@gmail.com', 3);

-- Création de la table Professeurs
CREATE TABLE Professeurs (
    id_Prof INT(10) NOT NULL,
    nom_Prof VARCHAR(50) NOT NULL,
    prenom_Prof VARCHAR(100) NOT NULL,
    sexe_Prof VARCHAR(1) NOT NULL,
    contact_Prof INT(8),
    email_Prof VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_Prof),
    id_Mat INT(10),
    FOREIGN KEY (id_Mat) REFERENCES Matières(id_Mat)
);

-- Insertion des données dans la table Professeurs
INSERT INTO Professeurs (id_Prof, nom_Prof, prenom_Prof, sexe_Prof, contact_Prof, email_Prof, id_Mat)
VALUES ('121', 'DOSSOU', 'Jean', 'M', '66210205', 'jeandossou@gmail.com', 11),
       ('122', 'KODO', 'Sophie', 'F', '60252874', 'sophikodo@gmail.com', 12),
       ('123', 'ADOGBE', 'Pierre', 'M', '90545825', 'adopierre@gmail.com', 13);

-- Création de la table Administrations
CREATE TABLE Administrations (
    id_Admin INT(10) NOT NULL,
    nom_Admin VARCHAR(50) NOT NULL,
    prenom_Admin VARCHAR(100) NOT NULL,
    sexe_Admin VARCHAR(1) NOT NULL,
    email_Admin VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_Admin)
);

-- Insertion des données dans la table Administrations
INSERT INTO Administrations (id_Admin, nom_Admin, prenom_Admin, sexe_Admin, email_Admin)
VALUES ('200', 'ALIMAN', 'Felicienne', 'F', 'feliciennealiman.com'),
       ('201', 'NOUNANGNON', 'Pierre', 'M', 'pierrenounangnon.com'),
       ('202', 'ADJAKA', 'Serge', 'M', 'sergeadjaka@gmail.com');




-- Insertion des données dans la table Filières
INSERT INTO Filières (id_Fil, nom_Fil)
VALUES (1, 'Genie Logiciel'),
       (2, 'Internet et Multimedias'),
       (3, 'Securite Informatique');

-- Création de la table Salles
CREATE TABLE Salles (
    id_Sal VARCHAR(20) NOT NULL,
    nom_Sal VARCHAR(20) NOT NULL,
    cap_Sal INT(4) NOT NULL,
    PRIMARY KEY (id_Sal)
);

-- Insertion des données dans la table Salles
INSERT INTO Salles (id_Sal, nom_Sal, cap_Sal)
VALUES ('A', 'Salle A1', 50),
       ('B', 'Salle B1', 30),
       ('C', 'Salle C1', 20);

-- Création de la table UE
CREATE TABLE UE (
    code_UE VARCHAR(10) NOT NULL,
    nom_UE VARCHAR(100) NOT NULL,
    nombre_credit_UE INT(1),
    type_semestre_UE INT(1),
    PRIMARY KEY (code_UE)
);

-- Insertion des données dans la table UE
INSERT INTO UE (code_UE, nom_UE, nombre_credit_UE, type_semestre_UE)
VALUES ('UE1', 'Logique et arithmetique', 6, 1),
       ('UE2', 'Comptabilité générale', 4, 1),
       ('UE3', 'Analyse Mathematique', 4, 2);

-- Création de la table Matières
CREATE TABLE Matières (
    id_Mat INT(10) NOT NULL,
    nom_Mat VARCHAR(50) NOT NULL,
    Horaire_Mat INT(3),
    PRIMARY KEY (id_Mat),
    code_UE VARCHAR(10),
    FOREIGN KEY (code_UE) REFERENCES UE(code_UE)
);

-- Insertion des données dans la table Matières
INSERT INTO Matières (id_Mat, nom_Mat, Horaire_Mat, code_UE)
VALUES (11, 'Analyse', 20, 'UE1'),
       (12, 'Probabilité', 30, 'UE2'),
       (13, 'langage C', 25, 'UE3');
