---
version: v5
status: draft
source: spotify-step-4-presentation.pptx (v6)
duration_target: 15:00
duration_range: 12:30 - 18:30
speaking_rate: ~125 w/minute
---
*SPOTIFY'S DATA & AI GOVERNANCE* PROJECT
===

# Présentation orale

---

## S01 : Titre (✅)

**CIBLE : 0:45  - FIN : 0:45  - TEMPS RESTANT :  14:15**

Je vous présente le projet de gouvernance des données et de l'intelligence artificielle pour *Spotify*.

*Spotify* est une plateforme d'envergure mondiale, de distribution de contenus, audios, numériques, en streaming. Son activité repose en grande partie sur la valorisation de la donnée, non seulement par les contenus proposés, mais aussi à travers des recommandations, des personnalisations, et des monétisations.

Le projet vise, d'une part, la conception d'un cadre de gouvernance des données unifié, d'autre part, l'intégration de la gouvernance de l'IA dans ce cadre global.

L'objectif de cette session est de valider le cadre de gouvernance proposé, son organisation, ainsi qu'un plan de déploiement incluant par une phase pilote.

---

## S02 : Diagnostic (✅)

**CIBLE : 1:45 - FIN : 2:30 - TEMPS RESTANT : 12:30**

Nous avons évalué 12 dimensions de la maturité data en suivant la méthodologie DMAT du gouvernement australien. L'échelle de maturité va de zéro à cinq : le niveau 1 correspond à une gouvernance initiale non systématisée, le niveau 3 à une gouvernance globale et bien définie.

Le résultat de cette évaluation est un niveau moyen un peu supérieur à 1.

9 dimensions sur 12 sont au niveau 1 :  gouvernance, qualité, architecture, sécurité, conformité, métadonnées. Ce niveau signifie que la gouvernance reste locale, réactive, et dispersée : des initiatives existent, mais elles ne sont ni généralisées ni mesurées.

3 dimensions sont au niveau 2 : usage & accessibilité, littératie *data* et analytique/business. 
A ce niveau de maturité, la gouvernance du domaine *à l'échelle de l'entreprise* est en cours de développement mais elle reste inachevé. 

La nature des domaines de maturité avancée montre que l'entreprise sait déjà produire de la valeur avec ses données.

Notre cible de maturité à moyen terme est le niveau 3 : une gouvernance globale, bien définie, et portée par une politique.

Aujourd'hui, le cadre  de gouvernance est partiellement défini, avec des rôles et des outils, mais il n'est pas déployé : pas d'audit, pas de monitoring, pas de politique appliquée sur le terrain.

---

## S03 : Enjeux (✅)

**CIBLE : 1:15 - FIN : 3:45 - TEMPS RESTANT : 11:15**

Le travail d'évaluation précédent permet d'identifier 6 enjeux majeurs, qui guident et qui structurent la construction du cadre de gouvernance.

Les enjeux identifiés sont classés ici *par ordre de criticité*.

Le premier est le décloisonnement des données (E1) et consiste à défaire les silos de données enfermés dans les départements et qui produisent des vues des utilisateurs incomplètes et incohérentes. 

Les enjeux suivants concernent la qualité des données (E2) - dont dépendent les recommandations, la conformité réglementaire multi-juridictionnelle (E3) et la garantie du respect de la vie privée et de l'usage éthique des données (E4).

Le cinquième enjeu est la gouvernance des données d'IA (E5) : traçabilité, détection et réduction des biais, explicabilité des modèles, responsabilisation et pilotage des processus de déploiement des modèles. 

Le dernier enjeu est la montée en compétence *data* (E) : une culture de gouvernance à construire, avec un risque de résistance au changement.

---

## S04 : Politique (✅)

**CIBLE : 1:15 - FIN : 5:00 - TEMPS RESTANT : 10:00**

La politique de gouvernance est structurée par neuf principes, regroupés ici en quatre ensembles.

Le premier ensemble, responsabilité et qualité, dit que chaque actif de données et chaque modèle doit avoir un responsable, d'une part, et que des règles de qualité mesurables et auditées régulièrement doivent être mise en place, d'autre part. 

Le deuxième ensemble, la confiance des utilisateurs, regroupe les principes de transparence, de minimisation de la collecte, et de droits d'accès/modification/suppression/opposition. 

Le troisième volet, sécurité et conformité, rassemble les questions de chiffrement, de contrôle d'accès par rôle, de conformité et de veille réglementaire continue. 

Le dernier volet couvre les questions de gouvernance de l'IA, de son usage éthique, et de l'amélioration continue des processus de gouvernance globale.

~~Le principe de gouvernance de l'IA (P8), est le plus *opérationnalisé*. Il se traduit par plusieurs exigences concrètes qui seront revues en détails aux slides suivants : traçabilité, détection et réduction des biais, explicabilité des décisions automatisées, responsabilisation et pilotage des déploiements des modèles. ~~

---

## S05 : Organisation (✅)

**CIBLE : 1:45 - FIN : 6:45 - TEMPS RESTANT : 8:15**

L'organisation des rôles et des responsabilités est formalisée par un modèle *Center of Excellence* modifié, adapté aux structures déjà existantes chez Spotify : 

La gouvernance est à la fois centralisée, portée par un Chief Data Officer (CDO) et un comité de gouvernance (DGC), et distribuée sur les départements, maîtres de leur données qui sont placées sous l'autorité autonome des Data Owners.

Sur l'organigramme, le trait plein est un rattachement *hiérarchique*, tandis que le trait pointillé un rattachement *fonctionnel* ou *transverse*. Ainsi CDO, DPO et Legal Team rapportent au CEO. 

Noter que l'indépendance du DPO est exigée par le RGPD.

Le modèle proposé s'écarte du modèle standard sur deux points.

Premièrement, l'infrastructure technique reste dans le département *Engineering* : 
les *Data Custodians* y sont centralisés et servent tous les départements transversalement. 

Deuxièmement, l'autorité de conformité (portée par DPO et Legal Team), est séparée de l'autorité de gouvernance (portée par CDO et le comité de gouvernance).

Le *Model Risk Manager* rapporte au CDO au quotidien, mais peut escalader directement au comité de gouvernance. C'est ce qui préserve son indépendance vis-à-vis des équipes dont il évalue les modèles. 

Les *Model Owners* appartiennent au département *Product Development* et n'ont pas de lien hiérarchique avec les Model Risk Managers (en application du principe de séparation entre exécution et contrôle).

Le levier principal de cette organisation contre le cloisonnement est le double rattachement des Data Stewards : fonctionnel au CDO, organisationnel au département. 

---

## S06 : Conformité (✅)

**CIBLE : 0:45 - FIN : 7:30 - TEMPS RESTANT : 7:30 \[MI-PARCOURS\]** 

La politique proposée structure la conformité réglementaire en reprenant les exigences opérationnelles, réglementation par réglementation (sans les regrouper par thème).

RGPD cadre les questions de consentement explicite, de droits d'accès et de modification, d'obligation de notification des violations, d'obligation de nommer un DPO. 

CCPA couvre les questions de *opt-out* sur la vente de données, de non-discrimination mais aussi des droits d'accès et de modification. 

PCI-DSS concerne les données de paiement : chiffrement, gestion des vulnérabilités, accès strictement contrôlé.

L'enjeu spécifique de Spotify est de gérer sa conformité pour de nombreuses réglementations distinctes \[enjeu de conformité E3\], y compris des réglementations locales, spécifiques à un marché, comme PDPA pour Singapour. Les marchés locaux sont cartographiés séparément, sous la responsabilité de *Legal Team* et de *DPO*.

---

## S07 : Gouvernance de l'IA (✅) (❗)

**CIBLE : 2:15 - FIN : 9:45 - TEMPS RESTANT : 5:15**

[montrer les quatre cartes]

La gouvernance de l'IA repose sur quatre exigences :

L'exigence de traçabilité dit que chaque jeu d'entraînement est documenté, avec sa source, sa période, ses transformations et son lineage. 

L'exigence de détection et de réduction des biais implique une évaluation périodique des biais algorithmiques pour les modèles à fort impact. 

L'exigence d'explicabilité impose que les décisions automatisées à impact significatif doivent pouvoir être expliquées de manière intelligible (réglementation RGPD).

La responsabilisation et le pilotage des processus de déploiement des modèles en production place chaque modèle en production sous la responsabilité d'un *Model Owner* et soumet le modèle à un circuit d'approbation de déploiement proportionnel à son niveau d'impact sur les utilisateurs. 

[montrer le tableau]

L'objectif de la différenciation des circuits d'approbation est d'éviter qu'un circuit lourd, prévu pour les modèles à fort impact, freine inutilement le déploiement des modèles mineurs. De plus, les circuits d'approbation sont conçus de telle sorte que *CDO* est, au mieux, *consulté*, y compris pour les modèles à fort impact : on évite ainsi que CDO soit à la fois juge et partie sur ses propres arbitrages d'IA.

Nous définissons 3 niveaux d'impact, définis par une combinaison de 4 propriétés du modèle 1) sa portée (en terme d'utilisateurs), 2) la réversibilité de son déploiement, 3) son exposition réglementaire, 4) sa priorité fonctionnelle. 

Pour un modèle à fort impact, *Model Owner* est consulté, *Model Risk Manager* est exécuteur, et le comité de gouvernance est responsable de l'approbation. 

Pour un modèle à impact modéré, *Model Owner* est exécuteur et *Model Risk Manager* est responsable. 

Pour un modèle à impact faible, *Model Owner* s'auto-certifie, et *Model Risk Manager* contrôle le modèle a posteriori par échantillonnage.

---

## S08 : Mise en œuvre (✅) (❗)

**CIBLE : 2:15 - FIN : 12:00 - TEMPS RESTANT : 3:00 \[POINT DE CONTROLE -3\]**

La mise en oeuvre du cadre de gouvernance commence par un projet *pilote* de 21 semaines. 
Son objectif  est de tester l'organisation précédente et les outils affectés, en conditions réelles, *au sein d'un périmètre réduit*.

[montrer la colonne de gauche]

**À gauche**, les outils retenus sont présentés par catégorie : chaque outil est affecté à un rôle précis de l'organisation et répond à l'un des enjeux majeurs. 

Le catalogage porte les enjeux de décloisonnement (E1) et de conformité réglementaire  (E3).
Le contrôle de la qualité porte les enjeux de qualité (E2) et de gouvernance IA (E5).
Le contrôle de la conformité porte les enjeux de conformité (E3) et d'éthique (E4).
Les outils de sécurisation répondent au principe politique de sécurité des données (P8).
Les outils de gouvernance des modèles porte l'enjeu de gouvernance IA (E5).

Les outils recommandés dans le cadre du business case Spotify ont été comparés à des alternatives open-sources, retenues sur la majorité des lignes, sauf *Collibra* et *TrustArc* (pour des questions contractuelles).

[montrer la colonne de droite]

**À droite**, une brève présentation du pilote : 21 semaines dont 7 pour une phase de *sécurisation* bloquante destinée à s'assurer de l'existence d'un annuaire central, de la migration des accès, et de l'intégration SSO. 

Le périmètre du pilote est limité aux modèles et aux données d'entraînement du système de recommandation, au sein du département *Product Development*. 

Il permet de valider les points suivants, en amont d'une éventuelle généralisation : le rattachement fonctionnel des *Data Stewards*, les circuits d'approbation des modèles et le coût réel d'ingénierie.

Les indicateurs de succès reposent sur le DMAT : la gouvernance et la qualité passent du niveau 1 au niveau 2, la gouvernance de l'IA du niveau 2 au niveau 3.

Deux risques clés sont identifiés : 1) une suspension du projet sans solution de repli (par exemple, en cas de défaillance de l'annuaire central), et 2) un débordement de planning, en particulier dans la phase de déploiement technique des outils.

---

## S09 : Feuille de route (✅)

**CIBLE : 1:45 - FIN : 13:45 - TEMPS RESTANT : 1:15**

L'objectif du déploiement général est de porter le nouveau cadre de gouvernance à tous les départements et d'amener la maturité globale de l'entreprise au niveau 3.

La feuille de route de la généralisation aux autres départements comporte quatre phases.

[suivre la frise de gauche à droite]

Phase 1, le projet pilote, réalisé en 21 semaines, jusqu'au jalon de phase M5 (cinquième mois). 

Phase 2, extension du déploiement aux activités restantes du département *Product Development,* réalisé en 3 mois, jusqu'au jalon de phase M10.

Phase 3, déploiement dans le département *Marketing*, en 3 mois, jusqu'à M15, en priorisant les enjeux de décloisonnement (E1), de conformité (E3) et d'éthique (E4).

Phase 4, déploiement dans le département *Content Curation*, en 3 mois, jusqu'au jalon M20, en priorisant la qualité (E2) et les métadonnées. 

Pour finir, une consolidation sur l'ensemble des départements est réalisée jusqu'jalon final (M24).

On note qu'une marge de 2 mois est insérée entre chaque phase (5 + 2 + 3 = 10, puis 15, puis 20).

Le séquencement précédent suit le niveau de risque et le coût marginal. Ainsi, *Marketing* passe en premier, car le risque réglementaire y est le plus élevé. 

*Les phases 2 , 3, 4 sont plus courtes*, car la phase de sécurisation n'est pas refaite : seule une migration allégée est reconduite pour chaque département. 

La durée totale de 24 mois est la borne haute de la fourchette de référence (15-24 mois). 
Elle finance la phase de sécurisation initiale et les périodes inter-phases.

Chaque jalon de phase est un point de *réévaluation* de la feuille de route restante, un feu vert, orange ou rouge. C'est le principe d'amélioration continue appliqué à la feuille de route elle-même.

---

## S10 : Valeur & prochaines étapes (✅)

**CIBLE : 1:15 - FIN : 15:00 - TEMPS RESTANT : 0:00**

Pour conclure, on propose un cadre de gouvernance qui soutient la croissance à venir et qui valorise la confiance des utilisateurs. 

Les bénéfices attendus couvrent la réduction de dépense, la réduction des failles de conformité réglementaire, l'amélioration de la confiance des utilisateurs et l'amélioration de la scalabilité.

Les économies de dépense viennent d'une réduction des inefficiences liées à des données de mauvaise qualité. 

L'amélioration de la conformité réglementaire permet d'éviter des sanctions pouvant aller jusqu'à 4 % du chiffre d'affaires dans le cas de faille RGPD. 

L'amélioration de la confiance est poussée par une plus grande transparence et une sécurité renforcée auprès des utilisateurs. 

L'amélioration de scalabilité est le résultat d'une infrastructure de gouvernance préparée à une croissance mondiale.

[montrer « Prochaines étapes »]

Les prochaines étapes sont concrètes et actionnables immédiatement. 

La première étape est de lancer le pilote sur le système de recommandation. 
La seconde étape est de nommer, ou de confirmer, les rôles structurant du cadre de gouvernance : DPO, CDO, Data Stewards et Model Owners. 

L'étape suivante est de préparer des revues de maturité DMAT en milieu et en fin de pilote. 

Enfin, la feuille de route proposée n'est pas un engagement fixe sur 24 mois, mais elle est soumise à une réévaluation régulière, phase après phase, pour décider du passage à l'échelle suivant.

Je vous remercie. Je suis à votre disposition pour vos questions.
