CREATE TABLE dim_date (
  date_key      INT PRIMARY KEY,              -- format AAAAMMJJ
  date_complete DATE NOT NULL UNIQUE,
  jour          TINYINT NOT NULL,
  mois          TINYINT NOT NULL,
  nom_mois      VARCHAR(15) NOT NULL,
  trimestre     TINYINT NOT NULL,
  semestre      TINYINT NOT NULL,
  annee         SMALLINT NOT NULL,
  jour_semaine  TINYINT NOT NULL,             
  nom_jour      VARCHAR(15) NOT NULL,
  est_weekend   BOOLEAN NOT NULL              
) ENGINE=InnoDB;

CREATE TABLE dim_client (
  client_key  INT AUTO_INCREMENT PRIMARY KEY, -- cle de substitution
  client_id   INT NOT NULL,                   -- cle metier (OLTP)
  nom_complet VARCHAR(101) NOT NULL,
  segment     VARCHAR(20) NOT NULL,
  tranche_age VARCHAR(10) NOT NULL,
  date_debut  DATE NOT NULL,                  -- pret pour SCD type 2
  date_fin    DATE NOT NULL DEFAULT '9999-12-31',
  est_courant BOOLEAN NOT NULL DEFAULT TRUE,
  KEY idx_dim_client_id (client_id)
) ENGINE=InnoDB;

CREATE TABLE dim_agence (
  agence_key  INT AUTO_INCREMENT PRIMARY KEY,
  agence_id   INT NOT NULL UNIQUE,
  code_agence VARCHAR(10) NOT NULL,
  nom_agence  VARCHAR(60) NOT NULL,
  ville       VARCHAR(40) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE dim_compte (                     
  compte_key     INT AUTO_INCREMENT PRIMARY KEY,
  compte_id      INT NOT NULL UNIQUE,
  rib            VARCHAR(20) NOT NULL,
  type_compte    VARCHAR(40) NOT NULL,
  taux_interet   DECIMAL(5,2) NOT NULL,
  statut         VARCHAR(10) NOT NULL,
  date_ouverture DATE NOT NULL,
  annee_ouverture SMALLINT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE dim_type_operation (
  type_operation_key INT AUTO_INCREMENT PRIMARY KEY,
  type_operation_id  INT NOT NULL UNIQUE,
  libelle            VARCHAR(40) NOT NULL,
  sens               CHAR(1) NOT NULL,
  categorie          VARCHAR(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE fact_operation (   
  operation_key      BIGINT AUTO_INCREMENT PRIMARY KEY,
  operation_id       BIGINT NOT NULL UNIQUE,  
  date_key           INT NOT NULL,
  client_key         INT NOT NULL,
  compte_key         INT NOT NULL,
  agence_key         INT NOT NULL,
  type_operation_key INT NOT NULL,
  montant            DECIMAL(15,2) NOT NULL,  
  montant_signe      DECIMAL(15,2) NOT NULL,  
  CONSTRAINT fk_fo_date   FOREIGN KEY (date_key)           REFERENCES dim_date(date_key),
  CONSTRAINT fk_fo_client FOREIGN KEY (client_key)         REFERENCES dim_client(client_key),
  CONSTRAINT fk_fo_compte FOREIGN KEY (compte_key)         REFERENCES dim_compte(compte_key),
  CONSTRAINT fk_fo_agence FOREIGN KEY (agence_key)         REFERENCES dim_agence(agence_key),
  CONSTRAINT fk_fo_type   FOREIGN KEY (type_operation_key) REFERENCES dim_type_operation(type_operation_key),
  KEY idx_fo_date_agence (date_key, agence_key)
) ENGINE=InnoDB;

CREATE TABLE fact_pret (                      
  pret_key        INT AUTO_INCREMENT PRIMARY KEY,
  pret_id         INT NOT NULL UNIQUE,       
  date_octroi_key INT NOT NULL,
  client_key      INT NOT NULL,
  compte_key      INT NOT NULL,
  agence_key      INT NOT NULL,
  statut_pret     VARCHAR(15) NOT NULL,
  capital         DECIMAL(15,2) NOT NULL,
  taux            DECIMAL(5,2) NOT NULL,      
  duree_mois      INT NOT NULL,
  mensualite      DECIMAL(15,2) NOT NULL,
  CONSTRAINT fk_fp_date   FOREIGN KEY (date_octroi_key) REFERENCES dim_date(date_key),
  CONSTRAINT fk_fp_client FOREIGN KEY (client_key)      REFERENCES dim_client(client_key),
  CONSTRAINT fk_fp_compte FOREIGN KEY (compte_key)      REFERENCES dim_compte(compte_key),
  CONSTRAINT fk_fp_agence FOREIGN KEY (agence_key)      REFERENCES dim_agence(agence_key)
) ENGINE=InnoDB;

INSERT INTO dim_date (date_key, date_complete, jour, mois, nom_mois, trimestre, semestre,
                      annee, jour_semaine, nom_jour, est_weekend)
WITH RECURSIVE jours (d) AS (
  SELECT DATE('2022-01-01')
  UNION ALL
  SELECT d + INTERVAL 1 DAY FROM jours WHERE d < '2025-12-31'
)
SELECT CAST(DATE_FORMAT(d, '%Y%m%d') AS UNSIGNED), d, DAY(d), MONTH(d), MONTHNAME(d),
       QUARTER(d), IF(MONTH(d) <= 6, 1, 2), YEAR(d), WEEKDAY(d) + 1, DAYNAME(d),
       WEEKDAY(d) IN (4, 5)
FROM jours;

INSERT INTO dim_client (client_id, nom_complet, segment, tranche_age, date_debut)
SELECT c.client_id,
       CONCAT(c.prenom, ' ', c.nom),
       c.segment,
       CASE WHEN TIMESTAMPDIFF(YEAR, c.date_naissance, '2025-06-30') < 25 THEN '<25'
            WHEN TIMESTAMPDIFF(YEAR, c.date_naissance, '2025-06-30') < 35 THEN '25-34'
            WHEN TIMESTAMPDIFF(YEAR, c.date_naissance, '2025-06-30') < 45 THEN '35-44'
            WHEN TIMESTAMPDIFF(YEAR, c.date_naissance, '2025-06-30') < 55 THEN '45-54'
            ELSE '55+' END,
       '2025-01-01'
FROM banque_oltp.client c;

INSERT INTO dim_agence (agence_id, code_agence, nom_agence, ville)
SELECT agence_id, code_agence, nom, ville FROM banque_oltp.agence;

INSERT INTO dim_compte (compte_id, rib, type_compte, taux_interet, statut, date_ouverture, annee_ouverture)
SELECT c.compte_id, c.rib, tc.libelle, tc.taux_interet, c.statut, c.date_ouverture, YEAR(c.date_ouverture)
FROM banque_oltp.compte c
JOIN banque_oltp.type_compte tc ON tc.type_compte_id = c.type_compte_id;

INSERT INTO dim_type_operation (type_operation_id, libelle, sens, categorie)
SELECT t.type_operation_id, t.libelle, t.sens,
       CASE t.type_operation_id
            WHEN 1 THEN 'Espèces' WHEN 3 THEN 'Espèces'
            WHEN 2 THEN 'Virement' WHEN 4 THEN 'Virement'
            WHEN 5 THEN 'Carte' WHEN 6 THEN 'Frais' ELSE 'Crédit' END
FROM banque_oltp.type_operation t;

INSERT INTO fact_operation (operation_id, date_key, client_key, compte_key, agence_key,
                            type_operation_key, montant, montant_signe)
SELECT o.operation_id,
       CAST(DATE_FORMAT(o.date_operation, '%Y%m%d') AS UNSIGNED),
       dc.client_key, dcp.compte_key, da.agence_key, dto.type_operation_key,
       o.montant,
       CASE t.sens WHEN 'C' THEN o.montant ELSE -o.montant END
FROM banque_oltp.operation o
JOIN banque_oltp.type_operation t ON t.type_operation_id = o.type_operation_id
JOIN banque_oltp.compte c         ON c.compte_id = o.compte_id
JOIN banque_oltp.titulaire ti     ON ti.compte_id = c.compte_id AND ti.role = 'Titulaire'
JOIN dim_client dc                ON dc.client_id = ti.client_id AND dc.est_courant = 1
JOIN dim_compte dcp               ON dcp.compte_id = c.compte_id
JOIN dim_agence da                ON da.agence_id = c.agence_id
JOIN dim_type_operation dto       ON dto.type_operation_id = o.type_operation_id;

INSERT INTO fact_pret (pret_id, date_octroi_key, client_key, compte_key, agence_key,
                       statut_pret, capital, taux, duree_mois, mensualite)
SELECT p.pret_id,
       CAST(DATE_FORMAT(p.date_octroi, '%Y%m%d') AS UNSIGNED),
       dc.client_key, dcp.compte_key, da.agence_key,
       p.statut, p.capital, p.taux, p.duree_mois,
       ROUND(p.capital * (p.taux / 1200) / (1 - POW(1 + p.taux / 1200, -p.duree_mois)), 2)
FROM banque_oltp.pret p
JOIN banque_oltp.compte c ON c.compte_id = p.compte_id
JOIN dim_client dc        ON dc.client_id = p.client_id AND dc.est_courant = 1
JOIN dim_compte dcp       ON dcp.compte_id = p.compte_id
JOIN dim_agence da        ON da.agence_id = c.agence_id;

SELECT (SELECT COUNT(*) FROM banque_oltp.operation) AS nb_oltp,
       (SELECT COUNT(*) FROM fact_operation)        AS nb_dw,
       (SELECT SUM(montant) FROM banque_oltp.operation) AS montant_oltp,
       (SELECT SUM(montant) FROM fact_operation)        AS montant_dw;

SELECT d.trimestre, d.mois, d.nom_mois,
       SUM(IF(f.montant_signe > 0,  f.montant_signe, 0)) AS total_credits,
       SUM(IF(f.montant_signe < 0, -f.montant_signe, 0)) AS total_debits,
       SUM(f.montant_signe) AS flux_net,
       COUNT(*) AS nb_operations
FROM fact_operation f JOIN dim_date d ON d.date_key = f.date_key
GROUP BY d.trimestre, d.mois, d.nom_mois
ORDER BY d.mois;

SELECT a.nom_agence, a.ville,
       SUM(IF(f.montant_signe > 0,  f.montant_signe, 0)) AS total_credits,
       SUM(IF(f.montant_signe < 0, -f.montant_signe, 0)) AS total_debits,
       SUM(f.montant_signe) AS flux_net,
       COUNT(*) AS nb_operations,
       COUNT(DISTINCT f.compte_key) AS nb_comptes
FROM fact_operation f JOIN dim_agence a ON a.agence_key = f.agence_key
GROUP BY a.nom_agence, a.ville
ORDER BY flux_net DESC;

SELECT t.categorie, t.sens, COUNT(*) AS nb_operations, SUM(f.montant) AS volume
FROM fact_operation f JOIN dim_type_operation t ON t.type_operation_key = f.type_operation_key
GROUP BY t.categorie, t.sens
ORDER BY volume DESC;

SELECT c.segment, COUNT(*) AS nb_prets, SUM(p.capital) AS capital_total,
       ROUND(SUM(p.capital * p.taux) / SUM(p.capital), 2) AS taux_moyen_pondere,
       SUM(p.mensualite) AS mensualites_totales
FROM fact_pret p JOIN dim_client c ON c.client_key = p.client_key
GROUP BY c.segment;

SELECT a.nom_agence, cp.type_compte, SUM(f.montant_signe) AS flux_net
FROM fact_operation f
JOIN dim_agence a  ON a.agence_key = f.agence_key
JOIN dim_compte cp ON cp.compte_key = f.compte_key
GROUP BY a.nom_agence, cp.type_compte WITH ROLLUP;

SELECT c.nom_complet, c.segment, SUM(f.montant) AS volume, COUNT(*) AS nb_operations
FROM fact_operation f JOIN dim_client c ON c.client_key = f.client_key
GROUP BY c.client_key, c.nom_complet, c.segment
ORDER BY volume DESC
LIMIT 5;
