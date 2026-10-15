---
version: v3
status: draft
source: spotify-step-4-presentation.pptx (v6)
duration_target: 15:00
duration_range: 12:30 - 18:30
speaking_rate: ~125 w/minute
---
*SPOTIFY'S DATA & AI GOVERNANCE* PROJECT
===

# Présentation orale \[DRAFT\]

---

## S01 : Titre (✅)

**CIBLE : 0:45  - FIN : 0:45  - TEMPS RESTANT :  14:15**

Je vous présente le projet de gouvernance des données et de l'intelligence artificielle pour *Spotify*.

*Spotify* est une plateforme d'envergure mondiale de distribution de contenus audios numériques en streaming. Il compte plus de 450 millions d'utilisateurs actifs, 200 millions d'abonnés premium, plus de 180 pays. Son activité repose en grande partie sur la valorisation de la donnée, non seulement par les contenus proposés, mais aussi à travers des recommandations, des personnalisations, et des monétisations.

Le projet vise, d'une part, la conception d'un cadre de gouvernance des données unifié, d'autre part, l'intégration la gouvernance de l'IA dans le cadre de gouvernance global.

L'objectif de cette session est de valider le cadre de gouvernance proposé, son organisation, ainsi qu'un plan de déploiement passant par une phase pilote.

---

## S02 : Diagnostic (✅)

**CIBLE : 1:45 - FIN : 2:30 - TEMPS RESTANT : 12:30**

Nous avons évalué 12 dimensions de la maturité data en suivant la méthodologie DMAT du gouvernement australien, appliquée au business case de Spotify. L'échelle de maturité va de zéro à cinq : le niveau 1 correspond à une gouvernance initiale non systématisée, le niveau 3 à une gouvernance globale et bien définie.

[montrer le graphique]

Le résultat : un niveau moyen un peu supérieur à 1.

9 dimensions sur 12 sont au niveau 1 :  gouvernance, qualité, architecture, sécurité, conformité, métadonnées. Ce niveau signifie que la gouvernance reste locale, réactive, et dispersée : des initiatives existent, mais elles ne sont ni généralisées ni mesurées.

3 dimensions sont au niveau 2 : usage & accessibilité, littératie *data* et analytique/business. 
A ce niveau de maturité, la gouvernance du domaine *à l'échelle de l'entreprise* est en cours de développement mais inachevé. 

On notera que le niveau de maturité avancé de la dimension analytique/business est en partie justifié par un moteur de recommandation déjà déployé est en production.

[montrer les cartes de droite]

Notre cible à moyen terme est le niveau 3 : une gouvernance globale et bien définie, portée par une politique.

Aujourd'hui, le cadre est partiellement défini, avec des rôles et des outils, mais il n'est pas déployé : pas d'audit, pas de monitoring, pas de politique appliquée sur le terrain.

Le message clé pour le comité : l'entreprise sait déjà produire de la valeur avec la donnée. Le risque n'est pas dans cette capacité, il est dans la gouvernance de cette capacité.

---

## S03 : Enjeux (✅)

**CIBLE : 1:15 - FIN : 3:45 - TEMPS RESTANT : 11:15**

Le travail d'évaluation précédent permet d'identifier 6 enjeux majeurs qui permette de guider et de structurer la construction du cadre de gouvernance.

Les enjeux identifiés présentés sont classés ici *par ordre de criticité*.

[ne pas lire les cartes, désigner E1 (décloisonnement) puis E5 (gouvernance IA)]

Le premier enjeu est le décloisonnement (E1) : des silos de données cloisonnés dans les départements produisent des vues incomplètes et incohérentes. 

Les enjeux suivants concernent (E2) la qualité des données, dont dépendent les recommandations, (E3) la conformité multi-juridictionnelle, qui doit réussir à concilier RGPD, CCPA, PDPA, les réglementations sur l'IA et les réglementation locales, et (E4) la vie privée et l'usage éthique.

Le cinquième enjeu est la gouvernance des données d'IA (E5) : traçabilité, détection et réduction des biais, explicabilité des modèles du moteur de recommandation, responsabilisation et pilotage des processus de déploiement des modèles en production. 

C'est le seul enjeu qui ne figurait pas dans le business case. 

~~Le sixième enjeu est la montée en compétences (E) : une culture de gouvernance à construire, avec un risque de résistance au changement.~~

~~Les enjeux majeurs de la gouvernance guident la construction du cadre : l'organisation répond à E1 (décloisonnement), E3 (conformité) et E5 (gouvernance IA), la politique répond à E2 (qualité), E3 (conformité), E4 (éthique) et E5 (gouvernance IA), et E6 (formation) est couvert à la fois par les rôles de l'organisation et par le principe d'amélioration continue.~~

---

## S04 : Politique (✅)

**CIBLE : 1:15 - FIN : 5:00 - TEMPS RESTANT : 10:00**

La politique de gouvernance est structurée par neuf principes, regroupés ici en quatre ensembles.

[ne pas lire les neuf principes, balayer les quatre blocs]

Le premier ensemble, responsabilité et qualité : chaque actif de données et chaque modèle a un responsable (un "owner"), et des règles de qualité mesurables sont auditées régulièrement. 

Le deuxième, la confiance utilisateur : transparence, minimisation de la collecte, droits d'accès, de modification, de suppression et d'opposition. 

Le troisième, sécurité et conformité : chiffrement, contrôle d'accès par rôle, PCI-DSS, et une veille réglementaire continue. 

Le quatrième, IA responsable et amélioration continue.

~~Ces principes sont issus du référentiel de principes de gouvernance, que nous avons repris pour la politique avec peu de changements. Par exemple, nous avons inversé les principes 8 et 9.~~

Le principe d'éthique et de gouvernance de l'IA (P8), est le plus *opérationnalisé* : 

il se traduit par 4 exigences concrètes : traçabilité, détection et réduction des biais, explicabilité des systèmes de décisions automatisées, responsabilisation et pilotage des déploiements des modèles en production. 

---

## S05 : Organisation (✅)

**CIBLE : 1:45 - FIN : 6:45 - TEMPS RESTANT : 8:15**

L'organisation des rôles et des responsabilités est formalisée par un modèle *Center of Excellence* modifié, adapté aux structures déjà existantes chez Spotify : 

La gouvernance est à la fois centralisée, portée par un Chief Data Officer (CDO) et un comité de gouvernance (DGC), et distribuée sur les départements, maîtres de leur données, placées sous l'autorité autonome des Data Owners.

[montrer l'organigramme]

Sur l'organigramme, le trait plein est un rattachement *hiérarchique*, le trait pointillé un rattachement *fonctionnel* ou *transverse*. CDO, DPO et Legal Team rapportent au CEO. 

Noter que l'indépendance du DPO est exigée par le RGPD, article 38.

Le modèle proposé s'écarte du modèle standard sur deux points.

Premièrement, l'infrastructure technique reste dans le département  *Engineering* : 
les *Data Custodians* y sont centralisés et servent tous les départements transversalement. 

Deuxièmement, l'autorité de conformité (portée par DPO et Legal Team), est séparée de l'autorité de gouvernance (portée par CDO et le comité de gouvernance).

Le *Model Risk Manager* rapporte au CDO au quotidien, mais peut escalader directement au comité de gouvernance. C'est ce qui préserve son indépendance vis-à-vis des équipes dont il évalue les modèles. 

Les *Model Owners* appartiennent au département *Product Development* (l'entité qui développe les modèles d'IA) et n'ont pas de lien hiérarchique avec les Model Risk Managers (en application du principe de séparation entre exécution et contrôle).

Le levier principal de cette organisation contre le cloisonnement est le double rattachement des Data Stewards : fonctionnel au CDO, organisationnel au département. 

~~Le surcoût de coordination propre au modèle Center of Excellence est assumé : à l'échelle de Spotify, c'est une nécessité structurelle.~~

---

## S06 : Conformité (✅)

**CIBLE : 0:45 - FIN : 7:30 - TEMPS RESTANT : 7:30 \[MI-PARCOURS\]** 

La politique proposée structure la conformité réglementaire en reprenant les exigences opérationnelles réglementation par réglementation \[ne regroupe pas les exigences par thème\].

[balayer les trois colonnes d'un geste]

RGPD : consentement explicite, droits des personnes, notification des violations sous 72 heures, DPO nommé. 

CCPA : opt-out sur la vente de données et non-discrimination. 

PCI-DSS pour les données de paiement : chiffrement, gestion des vulnérabilités, accès strictement contrôlé.

[montrer le bandeau du bas]

L'enjeu spécifique de Spotify est de gérer sa conformité pour de nombreuses réglementations distinctes \[enjeu de conformité E3\], y compris des réglementations  locales, spécifiques à un marché, comme PDPA pour Singapour. Les marchés locaux sont cartographiés séparément, sous la responsabilité de *Legal Team* et de *DPO*.

---

## S07 : Gouvernance de l'IA (✅) (❗)

**CIBLE : 2:15 - FIN : 9:45 - TEMPS RESTANT : 5:15**

~~Venons-en à la gouvernance de l'IA, qui est le cœur de notre apport.~~

[montrer les quatre cartes]

La gouvernance de l'IA repose sur quatre exigences :

La traçabilité : chaque jeu d'entraînement est documenté, avec sa source, sa période, ses transformations et son lineage. 

Les biais : une évaluation périodique des biais algorithmiques, pour les modèles à fort impact. 

L'explicabilité : les décisions automatisées à impact significatif doivent pouvoir être expliquées de manière intelligible.

La responsabilisation et le pilotage des processus de déploiement des modèles en production : chaque modèle en production est placé sous la responsabilité d'un *Model Owner*, et est soumis à un circuit d'approbation de déploiement proportionnel à son niveau d'impact sur les utilisateurs. 

[montrer le tableau]

~~Le niveau d'un modèle donné est déterminé lors de son enregistrement, puis il est hérité par chacune de ses versions. ~~

L'objectif de la différenciation des circuits d'approbation est d'abord d'éviter qu'un circuit lourd, prévu pour les modèles à fort impact, freine inutilement le déploiement des modèles mineurs. De plus, les circuits d'approbation sont conçus de telle sorte que *CDO* est, au mieux, *consulté*, y compris pour les modèles à fort impact : on évite que CDO soit à la fois juge et partie sur ses propres arbitrages d'IA.

Nous définissons trois niveaux d'impact : fort/modéré/faible, définis par une combinaison de 4 propriétés du modèle 1) sa portée (en terme d'utilisateurs), 2) la réversibilité de son déploiement, 3) son exposition réglementaire, 4) sa priorité fonctionnelle. 

~~Dans l'exemple présenté, la règle de combinaison des critères est un OU logique : si un seul des critères dépasse le seuil spécifique à un niveau, le modèle est classé dans ce niveau (par exemple, un modèle *fort* est un modèle à portée majoritaire, ou un modèle exposé réglementairement, ou une fonction principale, etc.).~~

Pour un modèle à fort impact, *Model Owner* est consulté, *Model Risk Manager* est exécuteur, et le comité de gouvernance est responsable de l'approbation. 

Pour un modèle à impact modéré, *Model Owner* est exécuteur et *Model Risk Manager* est responsable. 

Pour un modèle à impact faible, *Model Owner* s'auto-certifie, et *Model Risk Manager* contrôle le contrôle le modèle a posteriori par échantillonnage.

~~Les seuils des critères de niveau sont évalués et recalibrés continûement (une première fois à la suite des résultats du pilote).~~

---

## S08 : Mise en œuvre (✅) (❗)

**CIBLE : 2:15 - FIN : 12:00 - TEMPS RESTANT : 3:00 \[POINT DE CONTROLE -3\]** **

La mise en oeuvre commence par un projet pilote de 21 semaines. L'objectif du pilote est de tester les outils et les rôles en conditions réelles *dans un périmètre réduit*.

[montrer la colonne de gauche]

**À gauche**, les outils retenus sont présentés par catégorie : chaque outil opère un rôle précis du modèle *Center of Excellence* et répond à l'un des enjeux majeurs. 

Le catalogage porte les enjeux de décloisonnement (E1)) et de conformité (E3).
Le contrôle de la qualité porte les enjeux de qualité (E2) et de gouvernance IA (E5).
Le contrôle de la conformité porte les enjeux de conformité (E3)) et d'éthique (E4).
Les outils de gouvernance des modèles porte l'enjeu de gouvernance IA (E5).

~~la sécurité répond au principe P3 (sécurité des données). ~~

~~Catalogage : Collibra, sous licence commerciale, et OpenMetadata. Qualité : Soda Core. Conformité : TrustArc, sous licence commerciale. Sécurité : Wazuh et OpenBao. Gouvernance de l'IA : MLflow, DVC, AIF360 et AIX360. ~~

Les outils recommandés dans le cadre du business case Spotify ont été comparés à des alternatives open-sources, retenues sur la majorité des lignes, sauf *Collibra* et *TrustArc* (pour des questions contractuelles).

[montrer la colonne de droite]

**À droite**, une brève présentation du pilote  : 21 semaines dont 7 pour une phase de *sécurisation* bloquante : existence d'un annuaire central, migration des accès, intégration SSO. 

Le périmètre du pilote est limité aux modèles et aux données d'entraînement du système de recommandation, au sein du département *Product Development*. 

Il permet de valider avant une éventuelle généralisation : le rattachement fonctionnel des *Data Stewards*, les circuits d'approbation des modèles et le coût réel d'ingénierie, avant généralisation.

Les indicateurs de succès reposent sur le DMAT : la gouvernance et la qualité passent du niveau 1 au niveau 2, la gouvernance de l'IA du niveau 2 au niveau 3.

Deux risques clés sont identifiés : 1) une suspension du projet sans solution de repli (par exemple, en cas d'absence d'annuaire central), et 2) un débordement de planning, en particulier dans la phase de déploiement technique.

A propos de la conformité RGPD :  la conformité complète au RGPD ne peut pas rentrer dans le périmètre du pilote, du fait, en particulier, qu'un registre des traitements (RoPA) ne portant que sur un seul département ne suffit pas à satisfaire l'article 30 (qui impose un registre global).

---

## S09 : Feuille de route (✅)

**CIBLE : 1:45 - FIN : 13:45 - TEMPS RESTANT : 1:15**

L'objectif du déploiement général est de porter le nouveau cadre de gouvernance à tous les départements et d'amener la maturité globale de l'entreprise au niveau 3.

La feuille de route de la généralisation aux autres départements comporte quatre phases.

[suivre la frise de gauche à droite]

Phase 1, le pilote : 21 semaines, jusqu'à M5. 

Phase 2 : les activités restantes du département *Product Development,* 3 mois, jusqu'à M10.

Phase 3 : *Marketing*, 3 mois, jusqu'à M15, en priorisant les enjeux de décloisonnement (E1), de conformité (E3) et d'éthique (E4).

Phase 4 : *Content Curation*, 3 mois, jusqu'à M20, en priorisant l'enjeu de qualité (E2) et les métadonnées. 

Pour finir, une consolidation sur l'ensemble des départements jusqu'à M22-M24.

Une marge de 2 mois est inséré entre chaque phase, u (5 + 2 + 3 = 10, puis 15, puis 20).

Le séquencement précédent suit le niveau de risque et le coût marginal : *Marketing* passe en premier, car le risque réglementaire y est le plus élevé. 

*Les phases 2 , 3,  4 sont plus courtes*, car la phase de sécurisation n'est pas refaite : seule une migration allégée est reconduite pour chaque département. 

La durée totale de 24 mois est la borne haute de la fourchette de référence (15-24 mois). 
Elle finance la phase de sécurisation initiale et les période inter-phase.

Chaque jalon est un point de *réévaluation* de la feuille de route restante, un feu vert, orange ou rouge. C'est le principe d'amélioration continue appliqué à la feuille de route elle-même.

---

## S10 : Valeur & prochaines étapes (\*)

**CIBLE : 1:15 - FIN : 15:00 - TEMPS RESTANT : 0:00**

~~Pour conclure, quatre bénéfices.~~

Des économies : moins d'inefficiences liées à une donnée de mauvaise qualité. 
La conformité : éviter des sanctions pouvant aller jusqu'à 4 % du chiffre d'affaires, pour le RGPD. La confiance : transparence et sécurité renforcées auprès des utilisateurs. 
La scalabilité : une infrastructure de gouvernance prête pour la croissance mondiale.

[montrer « Prochaines étapes »]

Quatre prochaines étapes, concrètes et actionnables tout de suite. 
Un : lancer le pilote sur le système de recommandation. 
Deux : nommer ou confirmer le DPO, le CDO, les Data Stewards et les Model Owners. 
Trois : mener des revues de maturité DMAT en milieu et en fin de pilote. 
Quatre : décider du passage à l'échelle phase par phase, à chaque jalon, plutôt que de nous engager d'emblée sur 24 mois.

Je vous remercie. Je suis à votre disposition pour vos questions.
