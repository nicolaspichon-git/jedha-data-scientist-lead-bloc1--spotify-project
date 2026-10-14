---
deliverable: D4
title: Discours oral de la présentation
based_on: spotify-step-4-presentation.pptx (v6)
duration_target: "15:00"
duration_range: "12:30 - 18:30"
speaking_rate: "~125 mots/minute de parole effective (pauses et gestes inclus dans la cible)"
locale: fr
---

# Discours oral — Gouvernance des Données & de l'IA

Chaque section donne la durée cible, l'heure de fin de diapositive (compteur écoulé / restant) et le texte à dire. Les indications entre crochets `[…]` sont des repères de jeu, à ne pas lire.

---

## S01 — Titre
**Cible 0:45 · fin à 0:45 · restant 14:15**

Bonjour à tous. Je vous présente le projet de gouvernance des données et de l'IA de Spotify.

Spotify opère à l'échelle mondiale : plus de 450 millions d'utilisateurs actifs, 200 millions d'abonnés premium, plus de 180 pays. Son activité repose sur la donnée : recommandation, personnalisation, monétisation.

Le projet répond à une demande de cadrage transverse : gouverner les données, et gouverner l'IA.

Je vous demande aujourd'hui de valider trois choses : le cadre de gouvernance, l'organisation cible, et le plan de déploiement, avec un pilote puis une généralisation.

---

## S02 — Diagnostic
**Cible 1:45 · fin à 2:30 · restant 12:30**

Commençons par le diagnostic. Nous avons évalué douze dimensions de la maturité data avec la méthode DMAT du gouvernement australien, appliquée au business case de Spotify. L'échelle va de zéro à cinq : le niveau 1 correspond à une gouvernance initiale, le niveau 3 à une gouvernance définie.

[montrer le graphique]

Le résultat : un niveau moyen de 1,25 sur 5. Neuf dimensions sur douze sont au niveau 1, parmi lesquelles la gouvernance, la qualité, l'architecture, la sécurité, la conformité et les métadonnées. Ce niveau signifie une gouvernance locale, réactive, dispersée : des initiatives qui existent, mais qui ne sont ni généralisées ni mesurées.

Trois dimensions sont au niveau 2 : l'usage et l'accessibilité, la littératie data, et l'analytique. C'est notre point d'appui, puisque le moteur de recommandation est déjà en production.

[montrer les cartes de droite]

Notre cible à moyen terme est le niveau 3 : une gouvernance globale et bien définie, portée par une politique.

Aujourd'hui, le cadre est partiellement défini, avec des rôles et des outils, mais il n'est pas déployé : pas d'audit, pas de monitoring, pas de politique appliquée sur le terrain.

Le message clé pour le comité : l'entreprise sait déjà produire de la valeur avec la donnée. Le risque n'est pas dans cette capacité, il est dans la gouvernance de cette capacité.

---

## S03 — Enjeux
**Cible 1:15 · fin à 3:45 · restant 11:15**

De ce diagnostic découlent six enjeux, classés par ordre de criticité.

[ne pas lire les cartes, désigner E1 puis E5]

Le premier, E1, est le décloisonnement : des silos départementaux produisent des vues incohérentes. Le deuxième, E2, est la qualité des données, dont dépendent les recommandations. Le troisième, E3, est la conformité multi-juridictionnelle : concilier RGPD, CCPA, PDPA et réglementations sur l'IA. Le quatrième, E4, est la vie privée et l'usage éthique.

Le cinquième, E5, est la gouvernance des données d'IA : traçabilité, biais, explicabilité des modèles du moteur de recommandation. C'est le seul enjeu qui ne figurait pas dans le business case. Le sixième, E6, est la montée en compétences : une culture de gouvernance à construire, avec un risque de résistance au changement.

Ces enjeux guident la suite. L'organisation répond d'abord à E1, E3 et E5. La politique répond à E2, E3, E4 et E5. Et E6 est couvert à la fois par les rôles de l'organisation et par le principe d'amélioration continue.

---

## S04 — Politique
**Cible 1:15 · fin à 5:00 · restant 10:00**

Venons-en à la politique : neuf principes, regroupés en quatre ensembles.

[ne pas lire les neuf principes, balayer les quatre blocs]

Le premier ensemble, responsabilité et qualité : chaque actif de données et chaque modèle a un responsable, et des règles de qualité mesurables sont auditées régulièrement. Le deuxième, la confiance utilisateur : transparence, minimisation de la collecte, droits d'accès, de modification, de suppression et d'opposition. Le troisième, sécurité et conformité : chiffrement, contrôle d'accès par rôle, PCI-DSS, et une veille réglementaire continue. Le quatrième, IA responsable et amélioration continue.

Ces principes sont issus du référentiel de principes de gouvernance, que nous avons repris pour la politique avec peu de changements. Par exemple, nous avons inversé les principes 8 et 9.

Le principe P8, l'éthique et la gouvernance de l'IA, est le plus opérationnalisé : il se traduit par quatre exigences concrètes, la traçabilité, les biais, l'approbation et l'explicabilité. Je les détaille dans quelques instants, sur la diapositive consacrée à la gouvernance de l'IA.

---

## S05 — Organisation
**Cible 1:45 · fin à 6:45 · restant 8:15**

Passons à l'organisation. Nous retenons le modèle Center of Excellence, adapté à Spotify : une gouvernance centralisée, portée par le Chief Data Officer et le comité de gouvernance, combinée à une autonomie des départements, avec leurs Data Owners.

[montrer l'organigramme]

Sur l'organigramme, le trait plein est un rattachement hiérarchique, le pointillé un rattachement fonctionnel ou transverse. Le CDO, le DPO et la Legal Team rapportent au CEO. L'indépendance du DPO est exigée par le RGPD, article 38.

Nous nous écartons du modèle standard sur deux points. Premièrement, l'infrastructure technique reste dans Engineering : les Data Custodians y sont centralisés et servent tous les départements. Deuxièmement, nous séparons l'autorité de conformité, le DPO et la Legal Team, de l'autorité de gouvernance, le CDO et le comité.

Le Model Risk Manager rapporte au CDO au quotidien, mais peut escalader directement au comité de gouvernance : c'est ce qui préserve son indépendance vis-à-vis des équipes dont il évalue les modèles. Les Model Owners sont dans Product Development, séparés du MRM : c'est la séparation entre exécution et contrôle.

Le levier principal contre le cloisonnement est le double rattachement des Data Stewards : fonctionnel au CDO, organisationnel au département. Le surcoût de coordination est assumé : à l'échelle de Spotify, c'est une nécessité structurelle.

---

## S06 — Conformité
**Cible 0:45 · fin à 7:30 · restant 7:30**

Sur la conformité, la politique traite trois cadres séparément, chacun avec ses exigences opérationnelles.

[balayer les trois colonnes d'un geste]

Le RGPD : consentement explicite, droits des personnes, notification des violations sous 72 heures, DPO nommé. Le CCPA : opt-out sur la vente de données et non-discrimination. Et PCI-DSS pour les données de paiement : chiffrement, gestion des vulnérabilités, accès strictement contrôlé.

[montrer le bandeau du bas]

Le point clé est en bas. La difficulté propre à Spotify est multi-juridictionnelle : c'est l'enjeu E3. Chaque marché local, par exemple le PDPA à Singapour, est cartographié séparément, sous la responsabilité de la Legal Team et du DPO.

---

## S07 — Gouvernance de l'IA
**Cible 2:15 · fin à 9:45 · restant 5:15**

Venons-en à la gouvernance de l'IA, qui est le cœur de notre apport.

[montrer les quatre cartes]

Elle repose sur quatre exigences. La traçabilité : chaque jeu d'entraînement est documenté, avec sa source, sa période, ses transformations et son lineage. Les biais : une évaluation périodique des biais algorithmiques, pour les modèles à fort impact. L'approbation : la responsabilité est confiée à un Model Owner, avec un circuit proportionné au niveau d'impact. Et l'explicabilité : les décisions automatisées à impact significatif doivent pouvoir être expliquées de manière intelligible.

[montrer le tableau]

Le principe central est de ne pas appliquer le même circuit à tous les modèles. Nous définissons trois niveaux d'impact, selon la portée du modèle, la réversibilité d'une décision erronée, l'exposition réglementaire et la priorité fonctionnelle.

Pour un modèle à fort impact, qui touche la majorité des utilisateurs avec une décision peu réversible, le Model Owner est consulté, le Model Risk Manager est responsable, et le comité de gouvernance est redevable de l'approbation. Pour un impact modéré, un public ciblé, le Model Owner est responsable et le MRM redevable. Pour un impact faible, une fonction auxiliaire, le Model Owner s'auto-certifie, et le MRM contrôle après coup, par échantillonnage.

Ces niveaux sont attribués une seule fois, lors de l'enregistrement du modèle, puis hérités à chaque déploiement. Les responsabilités détaillées figurent dans les annexes. Deux conséquences. D'abord, un circuit lourd ne freine plus inutilement le déploiement des modèles mineurs. Ensuite, le CDO n'est que consulté sur les modèles à fort impact : on évite qu'il soit juge et partie sur ses propres arbitrages en matière d'IA.

Enfin, ce cadre est volontairement évolutif : les seuils des critères de niveau seront calibrés avec les résultats du pilote, avant toute généralisation.

---

## S08 — Mise en œuvre
**Cible 2:15 · fin à 12:00 · restant 3:00**

Comment mettre tout cela en œuvre ? Par un pilote de 21 semaines, soit environ cinq mois, qui teste ces outils et ces rôles en conditions réelles, sur un périmètre réduit.

[montrer la colonne de gauche]

À gauche, les outils par catégorie : chaque outil répond à un rôle précis du modèle Center of Excellence et à un enjeu identifié dans le diagnostic. Le catalogage porte E1 et E3, la qualité E2 et E5, la conformité E3 et E4, la gouvernance de l'IA E5 ; la sécurité répond au principe P3. Catalogage : Collibra, sous licence commerciale, et OpenMetadata. Qualité : Soda Core. Conformité : TrustArc, sous licence commerciale. Sécurité : Wazuh et OpenBao. Gouvernance de l'IA : MLflow, DVC, AIF360 et AIX360. Nous avons comparé les outils recommandés à des alternatives open source, retenues sur la majorité des lignes, sauf Collibra et TrustArc.

[montrer la colonne de droite]

À droite, le pilote. Sept semaines sont une phase de sécurisation bloquante : annuaire central, migration des accès, intégration SSO. Le périmètre est volontairement resserré : les modèles et les données d'entraînement du système de recommandation, dans Product Development. Il permet de valider le rattachement fonctionnel des Data Stewards, le circuit d'approbation des modèles et le coût réel d'ingénierie, avant de généraliser.

Les indicateurs reposent sur le DMAT : la gouvernance et la qualité passent du niveau 1 au niveau 2, la gouvernance de l'IA du niveau 2 au niveau 3.

Deux risques clés : une suspension du projet sans solution de repli, en l'absence d'annuaire central, et un débordement de planning.

Un point de vigilance : la conformité complète au RGPD, E3 et E4, est hors du périmètre du pilote. Un registre des traitements sur un seul département ne suffit pas à satisfaire l'article 30.

---

## S09 — Feuille de route
**Cible 1:45 · fin à 13:45 · restant 1:15**

La feuille de route comporte quatre phases, vers un niveau 3 généralisé.

[suivre la frise de gauche à droite]

Phase 1, le pilote : 21 semaines, jusqu'à M5. Phase 2 : les autres activités de Product Development, trois mois, jusqu'à M10. Phase 3 : Marketing, pour E1, E3 et E4, jusqu'à M15. Phase 4 : Content Curation, pour la qualité et les métadonnées, jusqu'à M20. Puis une consolidation sur l'ensemble des départements, à M22-M24.

Le séquencement suit le niveau de risque et le coût marginal : Marketing passe en premier, car le risque réglementaire y est le plus élevé. Les phases 2 à 4 sont plus courtes, car la phase de sécurisation n'est pas refaite : seule une migration allégée est reconduite pour chaque département. Entre les phases, nous prévoyons une marge de deux mois : 5 plus 2 plus 3 font 10, puis 15, puis 20.

La durée totale, 22 à 24 mois, est volontairement prudente : M24 est la borne haute de la fourchette de référence, 15 à 24 mois, et cette marge finance en grande partie la phase de sécurisation initiale.

Enfin, chaque jalon est un point de réévaluation, feu vert, orange ou rouge, et non un engagement figé. C'est le principe d'amélioration continue appliqué à la feuille de route elle-même.

---

## S10 — Valeur & prochaines étapes
**Cible 1:15 · fin à 15:00 · restant 0:00**

Pour conclure, quatre bénéfices.

Des économies : moins d'inefficiences liées à une donnée de mauvaise qualité. La conformité : éviter des sanctions pouvant aller jusqu'à 4 % du chiffre d'affaires, pour le RGPD. La confiance : transparence et sécurité renforcées auprès des utilisateurs. Et la scalabilité : une infrastructure de gouvernance prête pour la croissance mondiale.

[montrer « Prochaines étapes »]

Quatre prochaines étapes, concrètes et actionnables tout de suite. Un : lancer le pilote sur le système de recommandation. Deux : nommer ou confirmer le DPO, le CDO, les Data Stewards et les Model Owners. Trois : mener des revues de maturité DMAT en milieu et en fin de pilote. Quatre : décider du passage à l'échelle phase par phase, à chaque jalon, plutôt que de nous engager d'emblée sur 24 mois.

Je vous remercie. Je suis à votre disposition pour vos questions.
