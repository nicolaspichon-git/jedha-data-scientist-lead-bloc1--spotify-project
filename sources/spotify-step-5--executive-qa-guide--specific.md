---
version: v2
status: draft
source: 10-executive-qa-guide.pdf ([R11], 12 questions)
---

# Guide de questions-réponses spécifique

###### Méthode 

Chaque réponse est réécrite pour coller aux livrables : les affirmations génériques de [R11] sont remplacées par les choix, chiffres et limites documentés dans [D1], [D21], [D22], [D3] et leurs annexes. Chaque réponse est suivie de ses points d'appui (locators) et d'une note « Adaptation » qui indique ce qui change par rapport à [R11]. Les réponses sont rédigées pour être dites à l'oral (environ 1 minute à 1 minute 30, soit 140 à 195 mots).

###### Limite générale

***Les livrables ne chiffrent aucun coût ni aucun gain financier*** : les réponses ne donnent donc aucun montant, et le disent quand la question l'exige (Q3, Q8).

---

## Q1. Pourquoi Spotify a-t-elle besoin d'un cadre de gouvernance des données dès maintenant ?

###### *Réponse originale*
_La portée mondiale de Spotify et le volume considérable de données qu'il traite rendent la garantie de la qualité, de la sécurité et de la conformité des données plus importante que jamais. Avec l'augmentation des exigences réglementaires, comme le RGPD, le CCPA et la norme PCI-DSS, ainsi que le besoin de rationaliser les flux de données dans l'ensemble des opérations mondiales, un cadre de gouvernance des données solide est indispensable pour préserver l'efficacité opérationnelle, éviter les amendes et gagner la confiance des utilisateurs._

###### Réponse spécifique
Parce que l'écart est aujourd'hui mesurable. Le diagnostic place *Spotify* à un niveau de maturité moyen de 1,25 sur 5 : une capacité analytique avancée, avec un moteur de recommandation en production, mais une gouvernance locale, réactive et dispersée. Le cadre est défini, avec des rôles et des outils, mais il n'est pas déployé : ni audit, ni monitoring, ni politique appliquée sur le terrain.

En face, l'exposition augmente : plus de 450 millions d'utilisateurs actifs dans plus de 180 pays, des régimes hétérogènes (RGPD, CCPA, PDPA, PCI-DSS, nouvelles réglementations sur l'IA), des silos entre départements, et des modèles d'IA dont la traçabilité, les biais et l'approbation ne sont pas gouvernés. Agir maintenant permet de maintenir l'efficacité opérationnelle, d'éviter les sanctions et de préserver la confiance des utilisateurs, avant que cette dette de gouvernance ne grandisse avec l'échelle.

**Points d'appui.** [D1, §1.1] (maturité 1,25, cadre non déployé) ; [D1, §1.2] (enjeux E1 à E6, E5 absent du business case) ; [D21, §2.1.1-2.1.2] ; [R2].

**Adaptation.** [R11] reste générique (« portée mondiale, exigences croissantes ») ; la réponse s'appuie sur le diagnostic chiffré de [D1] et cite l'enjeu IA (E5), que [R11] n'évoque pas.

---

<div style="page-break-after: always;"></div>

## Q2. Quel sera l'impact du cadre sur les opérations de données existantes ?

###### *Réponse originale*
_Le cadre de gouvernance des données améliorera les opérations existantes en renforçant la qualité et la cohérence des données, en réduisant les silos de données et en simplifiant les processus de conformité. Des changements initiaux dans les rôles et les processus sont possibles, mais les bénéfices à long terme incluent des flux de données plus fluides, une meilleure prise de décision et une protection renforcée contre les violations de données._

###### Réponse spécifique
Le cadre ne remplace pas les opérations existantes : il leur ajoute des responsabilités explicites et des outils. Les départements gardent l'autorité sur leurs données, avec un *Data Owner* par département. Les *Data Stewards* ont un double rattachement : fonctionnel au CDO pour les standards, organisationnel au département. L'infrastructure technique reste dans Engineering, avec les *Data Custodians*, qui servent tous les départements.

Les changements les plus concrets sont les suivants. Un catalogue commun (Collibra, OpenMetadata) et des contrôles de qualité (Soda Core) apparaissent. Les modèles d'IA passent par un circuit d'approbation proportionné à leur niveau d'impact. Les accès sont centralisés par un annuaire central et le SSO.

Le coût de ces changements est réel et nous l'assumons : il pèse d'abord sur les *Data Custodians*, dont la charge est mesurée pendant le pilote. L'impact est volontairement limité au départ : le pilote ne touche que le système de recommandation de Product Development, avant toute généralisation.

**Points d'appui.** [D22] (rattachements, double rattachement des DS, DC dans Engineering) ; [D3, §3.3-3.5] ; [D3-Annexes, §3.F.2] (mesure de l'*engineering overhead*) ; [D3-Annexes, §3.F.8] (charge DC sous-estimée) ; [D21-Annexes, §2.1.A.3].

**Adaptation.** [R11] promet des bénéfices sans coût ; la réponse nomme les changements précis (rôles, outils, circuits) et reconnaît la charge d'ingénierie, risque identifié « élevé » dans [D3-Annexes, §3.F.8].

---

## Q3. Quelle est la valeur business d'un investissement dans la gouvernance des données ?

###### *Réponse originale*
_La valeur commerciale se décline de plusieurs manières :_

- _**Économies :** en améliorant la qualité des données et en réduisant les inefficacités causées par des données de mauvaise qualité, nous pouvons optimiser nos opérations._
- _**Conformité :** éviter des amendes coûteuses en respectant des réglementations comme le RGPD et le CCPA._
- _**Confiance :** renforcer la sécurité et la transparence des données augmentera la confiance et la fidélité des utilisateurs._
- _**Évolutivité :** le cadre garantit que l'infrastructure de données de Spotify pourra évoluer au rythme de sa base d'utilisateurs mondiale en croissance._

###### Réponse spécifique
Quatre sources de valeur, qui correspondent aux enjeux du diagnostic.

- **Économies :** une meilleure qualité des données (E2) et la fin des silos (E1) réduisent les inefficiences liées à une donnée inexacte et des métadonnées obsolètes, qui dégradent aujourd'hui les recommandations.
- **Conformité :** nous évitons des sanctions pouvant aller jusqu'à 4 % du chiffre d'affaires mondial pour le RGPD, grâce au socle RGPD/CCPA/PCI-DSS, au DPO et à la cartographie marché par marché.
- **Confiance :** transparence, minimisation, droits des utilisateurs et sécurité renforcés (principes P2, P3, P6, P7).
- **Scalabilité :** le modèle Center of Excellence et le déploiement par phases préparent la croissance mondiale.

À ce stade, nous ne chiffrons pas ces bénéfices : le pilote produit les premières mesures, de qualité et de maturité, sur lesquelles un calcul de retour sur investissement pourra s'appuyer.

**Points d'appui.** [D1, §1.2] (E1, E2, E3, E4) ; [D21, §2.1.3] (P2, P3, P6, P7) ; [D21, §2.1.4] ; [D3, §3.6] ; [R2] (plafond de 4 % du CA mondial, RGPD uniquement).

**Adaptation.** Les quatre piliers de [R11] sont conservés. Le plafond de 4 % est rattaché au seul RGPD (il ne s'applique pas au CCPA) et l'absence de chiffrage des bénéfices est signalée plutôt que passée sous silence.

---

## Q4. Comment le cadre garantit-il la conformité RGPD / CCPA ?

###### *Réponse originale*
_Le cadre intègre des mesures de conformité à chaque étape du traitement des données, notamment :_

- _Des politiques claires pour obtenir le consentement des utilisateurs (la « base légale » du RGPD)._
- _Des outils de gestion des demandes des utilisateurs concernant leurs données, comme l'accès, la modification ou la suppression (RGPD et CCPA)._
- _Des mesures de minimisation et de sécurité des données alignées sur la norme PCI-DSS pour les informations de paiement sensibles._
- _La désignation d'un délégué à la protection des données (DPO) chargé de surveiller la conformité dans toutes les régions._

###### Réponse spécifique
La politique traite chaque cadre séparément, avec ses exigences propres. Pour le RGPD : traitement licite, loyal et transparent, consentement explicite et éclairé, droits d'accès, de rectification et de suppression, notification des violations à l'autorité de contrôle sous 72 heures, et nomination d'un DPO. Pour le CCPA : transparence sur l'opt-out de la vente de données, droits d'accès, de modification et de suppression, non-discrimination. La minimisation (P6) et la sécurité alignée sur PCI-DSS complètent le dispositif pour les données de paiement.

Côté outils, TrustArc fournit le registre des traitements, les analyses d'impact, la notification de violation et la gestion des demandes des personnes concernées. Côté organisation, le DPO est *Accountable* sur la conformité et les droits des utilisateurs, avec la Legal Team en appui. Un processus de cartographie réglementaire, marché par marché (le PDPA à Singapour, par exemple), couvre la dimension multi-juridictionnelle.

Un point de vigilance : le pilote ne couvre pas la conformité complète au RGPD. Un registre des traitements sur un seul département ne suffit pas à satisfaire l'article 30. La couverture des demandes des personnes concernées par TrustArc sera validée séparément avant la phase 3, celle de Marketing.

**Points d'appui.** [D21, §2.1.4] ; [D22-Annexes, §2.2.C] (DPO « RA » sur conformité et droits, « R » sur la notification) ; [D3, §3.4-3.5] ; [D3-Annexes, §3.C.4] (TrustArc, DSAR) ; [D3-Annexes, §3.G.3] (validation DSAR avant la phase 3) ; [A1], [A2], [A3], [A4].

**Adaptation.** [R11] cite « les mesures de minimisation et de sécurité alignées sur PCI-DSS » comme un seul bloc ; [D21] distingue la minimisation (P6, principe général) et PCI-DSS (cadre propre aux paiements). Les limites du pilote ([D3, §3.5]) sont ajoutées.

---

## Q5. Quel modèle organisationnel recommander, et pourquoi ?

###### *Réponse originale*
_Je recommande le modèle de centre d'excellence (CoE). Il combine une gouvernance centralisée solide avec une flexibilité permettant à chaque département de gérer ses besoins spécifiques en matière de données. Cette approche hybride garantit que les principes fondamentaux de la gouvernance des données restent cohérents, tout en permettant aux équipes d'adapter les solutions à leurs défis particuliers. C'est le modèle le mieux adapté à la structure mondiale et diversifiée de Spotify._

###### Réponse spécifique
Nous recommandons un modèle Center of Excellence modifié, adapté à l'existant chez Spotify. Il combine une gouvernance centralisée, portée par le CDO et le comité de gouvernance, avec des départements partiellement autonomes qui gardent la responsabilité opérationnelle de leurs données.

Nous l'avons comparé aux deux autres modèles courants. Le modèle centralisé retirerait aux *Data Owners* l'autorité de proximité dont ils ont besoin, alors que les départements se sont déjà approprié la donnée. Le modèle embarqué reconduirait les silos et disperserait les ressources juridiques. Le Center of Excellence est le seul à répondre simultanément à trois enjeux : le décloisonnement (E1), la conformité multi-juridictionnelle (E3) et la gouvernance de l'IA (E5).

Nous l'adaptons sur deux points : l'infrastructure technique reste dans Engineering, et l'autorité de conformité (DPO, Legal Team) est séparée de l'autorité de gouvernance (CDO, comité). Ce modèle a un surcoût de coordination, que nous assumons : à l'échelle de Spotify, c'est une nécessité fonctionnelle.

**Points d'appui.** [D3, §3.3] ; [D3-Annexes, §3.B.2-3.B.4] (analyse des trois modèles, deux écarts, surcoût) ; [D22] (organigramme) ; [R7].

**Adaptation.** [R11] affirme que le modèle est « le mieux adapté » ; la réponse expose la comparaison des trois modèles, les deux écarts au modèle canonique et le surcoût de coordination, tels que documentés dans [D3-Annexes, §3.B].

---

## Q6. Comment mesurer le succès du cadre de gouvernance ?

###### *Réponse originale*
_Le succès sera mesuré à travers :_

- _**Amélioration des indicateurs de qualité des données :** moins d'écarts, d'erreurs et de doublons._
- _**Respect de la conformité :** aucune sanction ni amende réglementaire._
- _**Efficacité opérationnelle :** accès plus rapide aux données, moins de retards liés aux silos de données et processus de reporting rationalisés._
- _**Confiance des utilisateurs :** plus de transparence et moins de plaintes concernant l'utilisation des données._

###### Réponse spécifique
Nous mesurons le succès avec l'échelle de maturité DMAT, la même que celle du diagnostic initial. Au terme du pilote, trois dimensions sont réévaluées : *Data Governance* et *Data Quality* passent du niveau 1 au niveau 2, *Analytics & BI* (volet gouvernance de l'IA) du niveau 2 au niveau 3. La re-cotation est faite à la revue intermédiaire, puis à la revue finale, où le comité de gouvernance valide le score final. L'objectif à moyen terme est le niveau 3 à l'échelle de l'organisation.

Le pilote suit aussi des indicateurs opérationnels : le double rattachement des *Data Stewards* (adoption des standards, délai de propagation, fréquence de sollicitation, cohérence terminologique, autonomie départementale), le délai d'approbation des modèles par niveau d'impact, et la charge d'ingénierie des *Data Custodians*.

Une précision honnête : la re-cotation DMAT reste un jugement qualitatif, validé par le comité pour limiter l'auto-évaluation. Les résultats alimentent ensuite une décision feu V/O/R pour chaque dispositif avant la généralisation.

**Points d'appui.** [D21, §2.1.7] ; [D3, §3.5] (indicateurs) ; [D3-Annexes, §3.F.6] (KPIs, méthode, nature de l'exercice) ; [D3-Annexes, §3.F.10] ; [D3-Annexes, §3.G.1] (critères de passage à l'échelle).

**Adaptation.** [R11] liste des indicateurs génériques (moins d'erreurs, absence d'amende, accès plus rapide, moins de plaintes). Les livrables retiennent des niveaux de maturité DMAT et des critères de passage à l'échelle : ces indicateurs remplacent la liste de [R11]. L'absence de sanction est un résultat attendu, mais ce n'est pas un indicateur du pilote, dont le périmètre exclut E3/E4.

---

## Q7. Combien de temps pour mettre en œuvre intégralement le cadre ?

###### Réponse spécifique
Le déploiement est progressif, sur 22 à 24 mois au total.

Le pilote dure 21 semaines, soit environ cinq mois, dans la fourchette de trois à six mois de référence. Il inclut sept semaines de phase de sécurisation bloquante : annuaire central, migration des accès, intégration SSO. Il porte sur le système de recommandation de Product Development.

Viennent ensuite trois phases de trois mois : le reste de Product Development, Marketing en priorité pour E1, E3 et E4 car le risque réglementaire y est le plus élevé, puis Content Curation pour la qualité et les métadonnées. Une marge de deux mois sépare les phases, puis une consolidation clôt le projet à M22-M24. Les phases suivantes sont plus courtes, car la phase de sécurisation n'est pas refaite : seule une migration allégée est reconduite pour chaque département.

La durée totale atteint la borne haute de la fourchette de référence, 15 à 24 mois : c'est le coût assumé de la sécurisation et des marges. Chaque jalon est un point de réévaluation, pas un engagement figé.

**Points d'appui.** [D3, §3.5-3.6] ; [D3-Annexes, §3.G.2] (séquencement) ; [D3-Annexes, §3.G.4] (trajectoire, position par rapport à [R11, Q7]) ; [R11, Q7].

**Adaptation.** [R11] donne 3 à 6 mois pour le pilote puis 12 à 18 mois supplémentaires. Les livrables précisent 21 semaines (~5 mois), le détail des phases et des marges, et un total de 22 à 24 mois, à la borne haute de la fourchette de 15 à 24 mois.

---

<div style="page-break-after: always;"></div>

## Q8. Quels sont les coûts associés à la mise en œuvre du cadre ?

###### Réponse spécifique
Les livrables identifient les postes de coût, mais ne les chiffrent pas encore. Nous préférons le dire que présenter un montant que nous ne pouvons pas défendre.

- **Outils.** Deux outils sont sous licence commerciale, Collibra et TrustArc, car les enjeux à risque réglementaire chiffrable (E3, E4) justifient des garanties de service contractuelles. Les autres sont open source : l'économie de licence est compensée par l'hébergement et l'exploitation, que la capacité d'ingénierie interne de Spotify doit absorber. Wazuh remplace ainsi un SIEM commercial facturé au volume de données.
- **Ingénierie.** Le pilote mesure le temps d'ingénierie des *Data Custodians*. Le coût total de possession (infrastructure, maintenance pluriannuelle) sera établi une fois qu'un historique d'exploitation sera disponible.
- **Personnel.** Les rôles de l'organigramme (DPO, CDO, *Data Stewards*, *Model Owners*, *Model Risk Manager*, *Content Managers*) sont à nommer ou confirmer.
- **Formation.** Une session dédiée au *Data Steward* et au *Product Manager*, reconduite à chaque phase.

Nous anticipons aussi le décalage possible avec les cycles budgétaires trimestriels : la demande de budget de la phase suivante est faite avant la clôture de la précédente.

**Points d'appui.** [D3-Annexes, §3.C.1] (principes de sélection des outils) ; [D3-Annexes, §3.C.5] (Wazuh contre Splunk) ; [D3-Annexes, §3.F.2, §3.F.9] ; [D3-Annexes, §3.F.8] (risque budgétaire) ; [D3-Annexes, §3.G.3] (TCO) ; [D22].

**Adaptation.** [R11] liste technologie, formation et personnel avec une compensation par les économies futures ; la réponse ne reprend pas cette compensation, qui n'est pas chiffrée dans les livrables. Elle ajoute l'arbitrage licences commerciales / open source, le coût d'ingénierie mesuré par le pilote et le risque budgétaire inter-phases.

---

## Q9. Comment le cadre s'adaptera-t-il à l'évolution des réglementations et des technologies ?

###### Réponse spécifique
Il est conçu pour évoluer, à trois niveaux.

- **Réglementation.** Un processus de veille légale est inscrit dans la politique (principe P5). Il est complété par une cartographie réglementaire marché par marché, pilotée par la Legal Team et le DPO. Un nouveau marché est cartographié séparément, en complément du socle.
- **Politique et organisation.** Le principe d'amélioration continue (P9) prévoit des revues périodiques, mesurées avec la méthode DMAT. La politique et l'organigramme peuvent être révisés après la phase 1.
- **Technologie.** Le tableau d'outils n'est pas définitif : deux lignes sont testées en pilote (recouvrement Soda Core/OpenMetadata, suffisance de Soda Core pour E5), avec des solutions de repli documentées. Les seuils des niveaux d'impact des modèles sont calibrés avec les résultats du pilote.

Pour l'IA, les exigences d'explicabilité sont déjà alignées sur les obligations émergentes, et un modèle peut être reclassé si sa finalité ou sa portée change.

**Points d'appui.** [D21, §2.1.3] (P5, P9), [D21, §2.1.4], [D21, §2.1.5] ; [D21-Annexes, §2.1.A.4] (reclassification) ; [D3, §3.6] (ajustements attendus) ; [D3-Annexes, §3.G.3].

**Adaptation.** [R11] reste générique (« audits, mises à jour, outils évolutifs ») ; la réponse indique les mécanismes concrets des livrables : P5, P9, cartographie par marché, ajustements après le pilote, reclassification des modèles.

---

<div style="page-break-after: always;"></div>

## Q10. Comment traiter les données utilisateur sensibles de manière sécurisée dans ce cadre ?

###### Réponse spécifique
La sécurité est le principe P3 de la politique : chiffrement, contrôle d'accès par rôle, protocoles PCI-DSS pour les données de paiement. La minimisation (P6) réduit en amont l'exposition en cas de violation.

La mise en œuvre commence par une phase de sécurisation bloquante, au tout début du pilote. Elle établit un annuaire central avec SSO, vérifie la sécurisation de l'infrastructure existante, collecte les droits d'accès pour les centraliser, et déploie OpenBao pour la gestion des clés et des secrets. Wazuh assure la détection d'événements de sécurité. Ces outils sont opérés par les *Data Custodians*.

Les données personnelles sont classées dès l'entrée : OpenMetadata les détecte, Collibra valide la classification, et le DPO tranche les cas ambigus. En cas de violation, la notification à l'autorité de contrôle intervient sous 72 heures : le DPO l'exécute, et le CEO en est redevable.

Une limite : aucun schéma formel de classification des données n'est encore établi dans le plan, et le registre des traitements sera donc provisoire jusqu'à ce qu'il le soit.

**Points d'appui.** [D21, §2.1.3] (P3, P6) ; [D21, §2.1.4] ; [D3, §3.4-3.5] ; [D3-Annexes, §3.C.5] ; [D3-Annexes, §3.D] (cartographie de la sécurisation) ; [D3-Annexes, §3.F.8] ; [D22-Annexes, §2.2.C] (DPO « R » sur la notification de violation).

**Adaptation.** [R11] mentionne des « pare-feu, chiffrement et stockage sécurisé » sans lien avec un outil ou un rôle ; la réponse décrit la phase de sécurisation, les outils (OpenBao, Wazuh), les rôles (DC, DPO) et reconnaît la limite de la classification.

---

## Q11. Quels sont les principaux risques de ce cadre, et comment les atténuer ?

###### Réponse spécifique

Nous distinguons trois sources de risque: 
 - les risques du pilote, 
 - ceux de la phase de sécurisation, 
 - et ceux de la généralisation.

- **Suspension du projet sans solution de repli.** L'absence d'un annuaire d'entreprise central, prérequis du SSO, bloquerait tout le dispositif. Ce prérequis devient alors un chantier d'infrastructure séparé, et le projet ne se poursuit pas tant qu'il n'est pas livré.
- **Débordement de planning.** Il vient du délai de réponse de TrustArc, d'un échec du test d'intégration sans marge pour une seconde itération, et d'une phase d'exécution compressée à quatre semaines. Nous gérons les accès manuellement en dérogation temporaire si besoin, et envisageons un rallongement ponctuel plutôt que de clôturer sur des données fragiles.
- **Charge des *Data Custodians* sous-estimée** (probabilité élevée). Elle est suivie chaque semaine et arbitrée à la revue intermédiaire, avec une option d'offre managée.
- **Résistance au changement.** Formation ciblée du *Data Steward* et du *Product Manager* sur le double rattachement, et retours des parties prenantes collectés à la revue finale.
- **Dépassements de budget et de calendrier.** Marges de deux mois entre les phases, et décision feu V/O/R à chaque jalon, avec anticipation de la demande budgétaire de la phase suivante.

**Points d'appui.** [D3, §3.5] (risques) ; [D3-Annexes, §3.F.8] (tableau complet : probabilités, impacts, mitigations) ; [D3-Annexes, §3.F.9] ; [D3-Annexes, §3.G.1] ; [D3-Annexes, §3.G.4] ; [R11, Q11].

**Adaptation.** [R11] cite trois risques génériques (résistance au changement, retards, dépassements de coûts) avec des mitigations génériques. La réponse les reprend en les rattachant aux risques documentés dans [D3-Annexes, §3.F.8], dont deux ne figurent pas dans [R11] : la suspension sans repli et la charge des *Data Custodians*.

---

<div style="page-break-after: always;"></div>

## Q12. Ce cadre affectera-t-il l'agilité de Spotify dans l'innovation et le développement produit ?

###### Réponse spécifique
Il est conçu pour que la plupart des modèles ne soient pas freinés, mais nous ne dirons pas qu'il n'y aura aucun effet.

Le circuit d'approbation des modèles est proportionné à leur impact. Un modèle à impact faible, une fonction auxiliaire, est auto-certifié par son *Model Owner* sur la base d'une checklist, avec un simple contrôle *a posteriori* par échantillonnage. Un modèle à impact modéré passe par le *Model Owner* puis le *Model Risk Manager*. Seuls les modèles à fort impact suivent le circuit complet jusqu'au comité de gouvernance. La classification d'un modèle n'est faite qu'une seule fois : chaque nouvelle version en hérite le niveau, sans réouvrir la question.

Côté données, le catalogue commun, la qualité mesurée et la fin des silos donnent aux équipes des données plus fiables et plus accessibles. Les départements gardent leur autonomie, avec leurs *Data Owners*.

Le délai d'approbation par niveau est mesuré pendant le pilote. Si le palier fort impact est trop lent, nous resserrons les critères de classification plutôt que d'alléger le circuit.

**Points d'appui.** [D21, §2.1.5] ; [D21-Annexes, §2.1.A.3-2.1.A.4] (circuits, classification) ; [D22-Annexes, §2.2.C] (RACI des déploiements) ; [D3-Annexes, §3.G.1] (critère de délai, mesure au pilote) ; [D3-Annexes, §3.E].

**Adaptation.** [R11] répond par un « Non » catégorique, sans mécanisme. La réponse décrit les trois circuits proportionnés et la mesure du délai pendant le pilote, et reconnaît que le circuit fort impact ajoute des étapes.

---

## Écarts relevés dans les livrables (signalés, non corrigés)

1.~~**Référence erronée dans [D3-Annexes, §3.G.2]** : le budget de référence « pilote 3-6 mois, déploiement complet +12-18 mois, soit 15-24 mois » est cité comme « [R1, Q7] » ; la source est [R11, Q7] (cité correctement en §3.G.4 et dans [D3, §3.6]).~~
1. **Fourchette de déploiement [R11, Q7]** : « déploiement complet +12-18 mois » s'applique après le pilote. De M5 (fin du pilote) à M22-M24, le déploiement dure 17 à 19 mois, soit un mois de plus que la borne haute de 18 mois à M24. [D3-Annexes, §3.G.4] lit la fourchette sur le total (15-24 mois) : la réponse Q7 retient cette lecture.
2. **Plafond de 4 % du CA mondial** : il vient de [R2] et ne concerne que le RGPD ; [R11, Q3] ne le donne pas, et il n'est pas repris dans [D1], [D21] ou [D3]. La réponse Q3 le cite avec cette limite.
3. **Aucun chiffrage des coûts ni des bénéfices** dans [D1], [D21], [D22], [D3] : les réponses Q3 et Q8 ne contiennent donc aucun montant.
