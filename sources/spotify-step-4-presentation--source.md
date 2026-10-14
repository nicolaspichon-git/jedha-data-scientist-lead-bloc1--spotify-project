---
deliverable: D4
title: Gouvernance des Données & de l'IA
subtitle: Évaluation, cadre, organisation et plan de mise en œuvre
project: "SPOTIFY - DATA & AI GOVERNANCE PROJECT"
author: Nicolas Pichon
program: AIA RNCP 38777 / BC01 / Presentation
version: v6
date: 2026/10/15
locale: fr
slide_size: "13.333x7.5in"   # LAYOUT_WIDE (16:9)
source_file: 38b5c3d6-spotify-step-4-presentation.pptx
source_status: current        # remplace la source issue du .md v4 (obsolète)
slide_count: 10
footer: "Nicolas Pichon --- AIA RNCP 38777 / BC01 / Presentation / v6 --- 2026/10/15"   # présent uniquement sur S01 et S10
slide_number_format: "{n} / {N}"
theme:
  fonts: {heading: Cambria, body: Calibri}
  colors:
    navy: "1B2A4A"        # fond des diapositives S01 et S10 ; titres
    green: "1C8C68"       # accent principal, kickers, pastilles d'icône
    green_light: "2DBE8C"
    green_pale: "EAF7F1"  # fond des cartes vertes
    terracotta: "B8574A"  # badges E1…E6, ligne « Fort »
    gray_line: "D8DEE6"
    gray_text: "5B6B84"
    gray_soft: "8493A8"
    gray_bg: "F2F4F7"
    ice: "CADCFC"
    white: "FFFFFF"
  sizes_pt: {title: "28-34", body: "12-14", card: "9.5-11", source: "9"}
---

## Spécification du format (section ignorée par le générateur)

Source structurée pour un script de génération PPTX (python-pptx ou pptxgenjs), établie à partir du **fichier pptx v6 (38b5c3d6)** (10 diapositives). Le texte est repris **tel quel** (coquilles comprises) : les écarts de cohérence et de forme relevés dans le rapport sont signalés ici par des commentaires `<!-- ÉCART … -->`, **non corrigés**. Le générateur ignore les commentaires HTML.

**Grammaire**

1. Le front matter YAML porte les métadonnées et le thème du deck.
2. Tout ce qui précède le premier titre `## S..` est ignoré.
3. Une diapositive commence par `## S<NN> — <nom court>` (identifiant lisible, pas un titre affiché).
4. Puis une liste de métadonnées `- clé: valeur` :
   - `layout` : `title-dark` | `chart-cards` | `cards-grid` | `clusters` | `image-text` | `columns` | `cards-table` | `two-panels` | `timeline` | `pillars-dark` ;
   - `background` : `dark` | `light` ;
   - `icon` : nom de l'icône dans le disque vert (haut droite, x=12.2 in, y=0.4 in, 0.7 in) ; absent sur S01 ;
   - `source_line` : `bottom` (ligne de source en italique gris, bas de diapositive) ;
   - `overflow_risk` : `low` | `medium` | `high`.
5. Sections de niveau 3, dans l'ordre d'affichage :
   - `### kicker` : étiquette verte en petites capitales au-dessus du titre ;
   - `### title` / `### subtitle` ;
   - `### block: <type> {attributs}` : bloc répétable. Types : `kpis`, `chart`, `cards`, `card`, `bullets`, `numbered`, `table`, `image`, `callout`, `banner`, `timeline`, `legend`, `text` ;
   - `### notes` : notes de l'orateur ;
   - `### source` : ligne de source (une ligne, affichée en pied).
6. Attributs entre accolades : `{col=1}`, `{badge=E1}`, `{color=terracotta}`, `{x= y= w= h=}` (en pouces, facultatifs).
7. Bloc `cards` : chaque carte est une liste `- **Titre** :` suivie de lignes en retrait ; attribut `badge` entre crochets `[E1]`.
8. Bloc `table` : première ligne = en-tête ; `<br>` = retour à la ligne dans une cellule.
9. Bloc `image` : `path:`, `alt:`, `x/y/w/h`.
10. Bloc `chart` : `type:`, `title:`, `series:`, puis table `| Category | Série |`.
11. Inline : `**gras**`, `*italique*`. Références `[X, §Y]` en texte ordinaire.
12. Notes : un paragraphe par ligne ; ligne vide = saut de paragraphe.
13. Aucune section `REFS` ni diapositive de backup : le deck v6 n'en comporte pas.

---

## S01 — Titre
- layout: title-dark
- background: dark
- icon:
- source_line:
- overflow_risk: low

### kicker
SPOTIFY - DATA & AI GOVERNANCE PROJECT

### title
Gouvernance des Données & de l'IA

### subtitle
Évaluation, cadre, organisation et plan de mise en œuvre

### block: kpis
| Valeur | Libellé |
|---|---|
| 450M+ | utilisateurs actifs |
| 200M | abonnés premium |
| 180+ | pays d'opération |

### block: caption {align=bottom}
Nicolas Pichon --- AIA RNCP 38777 / BC01 / Presentation / v6 --- 2026/10/15
<!-- ÉCART : « Presentation » (EN) alors que le deck est en français ; l'en-tête des autres livrables est « Step N » ([D1]…[D3]). -->

### notes
Introduction :

Spotify opère a l’échelle mondiale
(450M+ utilisateurs, 180+ pays)
avec une dépendance forte aux données
(recommandation, personnalisation, monétisation).

Le projet répond a une demande de cadrage transverse : gouvernance des données ET de l'IA.

Objectif de la session : valider le cadre de gouvernance, l'organisation cible, le plan de déploiement (pilote puis généralisation).

---

## S02 — Diagnostic
- layout: chart-cards
- background: light
- icon: icons/icon_barchart.png
- source_line: bottom
- overflow_risk: medium

### kicker
DIAGNOSTIC

### title
Une maturité data en phase initiale

### block: chart {x=0.55 y=1.85 w=7.6 h=4.9}
type: bar-clustered-horizontal   <!-- BAR_CLUSTERED natif, sans légende ni étiquettes de valeur -->
title: Niveau de maturité par dimension (échelle 0–5)
axis_max: 5
series: Niveau de maturité

| Category | Niveau de maturité |
|---|---|
| Analytics & BI | 2.0 |
| Intégration | 1.0 |
| Métadonnées | 1.0 |
| Master & Reference Data | 1.0 |
| Littératie data | 2.0 |
| Sécurité | 1.0 |
| Usage & Accessibilité | 2.0 |
| Conformité | 1.0 |
| Opérations | 1.0 |
| Architecture | 1.0 |
| Qualité | 1.0 |
| Gouvernance | 1.0 |

### block: card {col=right order=1 style=kpi}
**1,25 / 5**
Niveau moyen de maturité actuel
Gouvernance locale, réactive, dispersée

### block: card {col=right order=2}
**Cible à moyen terme : niveau 3**
Gouvernance globale & bien définie,
portée par une politique de gouvernance

### block: card {col=right order=3}
Cadre partiellement défini (rôles, outils)
mais pas encore déployé :
- pas d’audit,
- pas de monitoring,
- pas de politique appliquée sur le terrain.

### source
Source : [D1] (Data & AI Maturity Assessment Report) - Méthodologie [R1] (Australian Government DMAT)
<!-- ÉCART : pas de locator ([D1, §1.1.1]) ; titre cité = titre H1 de [D1] (la liste de références de D21/D21-Annexes écrit « Data Maturity Assessment Report »). Libellés des dimensions traduits en français (D1 : noms DMAT anglais, ex. « Data Usage & Accessibility »). -->

### notes
12 dimensions évaluées selon DMAT [R1], appliquée au business case Spotify [R2].
Niveau moyen ~1,25 sur 5.
Points d'appui de niveau 2 :
Data Usage & Accessibilité,
Data Literacy,
Analytics & BI
(moteur de recommandation déjà en production).
Les autres dimensions encore au niveau 1 :
initiatives locales, non généralisées, non mesurées.

Message clé pour le comité : l'entreprise sait déjà produire de la valeur avec la donnée, le risque est dans la gouvernance de cette capacité, pas dans la capacité elle-même

---

## S03 — Enjeux
- layout: cards-grid        <!-- 3 rangées × 2 colonnes -->
- background: light
- icon: icons/icon_alert.png
- source_line: bottom
- overflow_risk: medium

### kicker
ENJEUX

### title
Six enjeux majeurs - par ordre de criticité

### block: cards {cols=2 badge_color=terracotta}
- [E1] **Décompartimenter les données**
  Silos départementaux → vues incohérentes / incomplètes
- [E2] **Maîtriser la qualité des données**
  Données inexactes / métadonnées obsolètes → recommandations dégradées
  Règles de qualité à définir
- [E3] **Maîtrise la conformité en contexte multi-juridictionnel**
  GDPR, CCPA, PDPA + réglementations IA → concilier sans perdre la cohérence globale
- [E4] **Garantir la vie privée & l’usage éthique des données**
  Transparence, anonymisation, maîtrise de l’utilisateur
  Au-delà de la seule conformité légale
- [E5] **Gouverner spécifiquement  les données d’IA**
  Traçabilité, biais, explicabilité, responsabilité des modèles du moteur de recommandation en production
- [E6] **Accompagner la montée en compétences data**
  Culture de gouvernance partagée encore à construire
  Risque de résistance au changement
<!-- ÉCART : titre E3 « Maîtrise la conformité en contexte multi-juridictionnel » ≠ [D1] / [D21-Annexes, §2.1.B] « Maîtriser la mise en conformité réglementaire dans un contexte multi-juridictionnel » (infinitif → nom, « réglementaire » omis) ; E5 « données d'IA » ≠ « données IA » ; double espace dans « spécifiquement  les ». E6 aligné sur [D1]. -->

### source
Source : [D1] (Data & AI Maturity Assessment Report) - enjeux dérivés de [R2] - sauf E5

### notes
L’ordre de criticité est justifié dans [D1].

E5 (gouvernance IA) est le seul enjeu qui n'est pas déjà identifié dans le business case [R2].

Le modèle organisationnel répond spécifiquement aux enjeux E1 (désilotage), E3 (conformité), E5 (gouvernance IA).
<!-- ÉCART : cohérent avec S05 (E1, E3, E5) ; mais [D22-Annexes, §2.2.B] couvre E1…E6 par l'organisation (E3 et E4 « couverts », E1, E2, E5, E6 « partiellement résolus ») et [D21-Annexes, §2.1.B] relie les 6 enjeux à la politique : la répartition « organisation = E1, E3, E5 / politique = E2, E3, E4, E5 » est une sélection, E6 est traité à part (note suivante). « Le modèle organisationnel » : suppression de « suivant » (S05 vient après S04, pas S03). -->

La politique de gouvernance répond aux enjeux E2 (qualité), E3 (conformité), E4 (éthique), E5 (gouvernance IA).
<!-- ÉCART : E1 absent de la liste alors que [D21-Annexes, §2.1.B] relie E1 à P1, P4 et §2.1.6 ; E4 « éthique » = raccourci (D1 : « vie privée et usage éthique »). -->

E6 (formation) couvert par l’organisation des rôles et des responsabilités [D22] et aussi par P9 (amélioration continue) [D21]
<!-- OK : conforme à [D22-Annexes, §2.2.B] (E6 partiellement résolu par les Data Owners/Stewards) et [D21-Annexes, §2.1.B] (E6 → P1, §2.1.6, P9). Libellé « formation » ≠ « montée en compétences » ; locators absents. -->

---

## S04 — Politique
- layout: clusters          <!-- 4 groupes, badges P1…P9 -->
- background: light
- icon: icons/icon_shield.png
- source_line: bottom
- overflow_risk: high

### kicker
POLITIQUE DE GOUVERNANCE

### title
Principes structurants du cadre de gouvernance

### block: cards {id=cluster-1 title="Responsabilité & qualité" position=top-left}
- [P1] **Responsabilité**
  - un responsable / actif de données et / modèle
- [P4] **Qualité**
  - règles mesurables (exactitude, complétude, fraîcheur), auditées régulièrement

### block: cards {id=cluster-2 title="Confiance utilisateur" position=top-right}
- [P2] **Transparence**
  - information claire et gestion du consentement
- [P6] **Minimisation**
  - collecte limitée aux finalités métier
- [P7] **Droits des utilisateurs**
  - accès, modification, suppression, opposition

### block: cards {id=cluster-3 title="Sécurité & conformité" position=bottom-left}
- [P3] **Sécurité**
  - chiffrement, contrôle d'accès / rôle, protocoles PCI-DSS
- [P5] **Conformité**
  - GDPR, CCPA, PCI-DSS et réglementations locales, veille continue

### block: cards {id=cluster-4 title="IA responsable & amélioration continue" position=bottom-right}
- [P8] **Éthique & gouvernance IA**
  - traçabilité, biais, explicabilité
- [P9] **Amélioration continue**
  - revues périodiques de réalignement DMAT

### source
Source : [D21] (Data & AI Governance Policy Document) - principes issus de [R4]
<!-- ÉCART : [D21] indique « adaptés du référentiel [R4] » ; la note dit « repris tels quels ». Pas de locator ([D21, §2.1.3]). -->

### notes
Les 9 principes sont issus du référentiel [R4]
Ils sont repris pour la politique [D21] avec peu de changements (inversion P8/P9, ...).
<!-- OK : [D21] « adaptés du référentiel [R4] » ; inversion confirmée ([R4] : 8 = amélioration continue, 9 = usage éthique ; [D21] : P8 = éthique & IA, P9 = amélioration continue). Les autres changements (« ... ») ne sont pas explicités : [D21-Annexes, §2.1.C] les détaille principe par principe. -->

P8 est le principe le plus opérationnalisé,
avec 4 exigences concrètes :
traçabilité, biais, responsabilité, explicabilité,
<!-- ÉCART : « responsabilité » ≠ « approbation » ([D21, §2.1.5] et S07 : traçabilité, biais, approbation, explicabilité). -->
détaillées dans la slide Gouvernance IA.

[D21] propose une différenciation des workflows d’approbation de déploiement des modèles ML/IA  en fonction de leur impact sur les utilisateurs,
détaillée au slide 7 (Responsabilité adaptées [...])
<!-- ÉCART : « [D21-E] » corrigé en [D21] mais sans locator : [D21, §2.1.5] (principe, critères) et [D21-Annexes, §2.1.A] (définitions, circuits). « Responsabilité adaptées [...] » : accord fautif et titre ≠ S07 (« Responsabilité adaptée au niveau d'impact du modèle »). « slide » vs « diapositive ». -->

---

## S05 — Organisation
- layout: image-text
- background: light
- icon: icons/icon_users.png
- source_line: bottom
- overflow_risk: medium

### kicker
ORGANISATION

### title
Modèle d’organisation Center of Excellence

### block: card {col=left w=3.9}
**Le modèle : CoE + adaptation Spotify**
Gouvernance centralisée (CDO, DGC)

combinée à une autonomie départementale (Data Owners / métier).

> répond simultanément aux enjeux E1, E3, E5

**Écarts par rapport au modèle standard**
Maintien de l’infrastructure technique dans Engineering (≠ hub)

Séparation des autorités :
- autorité de conformité (DPO/Legal)
- autorité de gouvernance (CDO/DGC).
Levier principal contre le cloisonnement
Le double rattachement des Data Stewards :
- fonctionnel au CDO
- organisationnel au département
<!-- ÉCART : « Levier principal contre le cloisonnement » : placement ambigu (se rattache au double rattachement, pas à la séparation des autorités). « CDO/DGC » : le DGC est présidé par le CDO et lui rapporte ([D22]) ; [D3, §3.3] dit « CDO et DGC ». Coquille « de de » corrigée dans le deck. -->

### block: image {x=4.57 y=1.38 w=8.17 h=4.98}
path: assets/orgchart.png    <!-- extrait : ppt/media/image5.png (1419×864 px) -->
alt: Organigramme CoE Spotify : CEO → Legal Team, DPO, CDO ; CDO → DGC, MRM ; départements Engineering (HoE, Data Custodians), Marketing (MD, Data Stewards), Product Development (PM, Model Owners, Data Stewards), Content Curation (Content Managers, Data Stewards).

### block: legend
Trait plein = rattachement hiérarchique - Trait pointillé = rattachement fonctionnel / transverse

### source
Source : [D22] (Roles and Responsibilities Organizational Chart)
<!-- ÉCART : pas de locator ; titre cité = « Roles and Responsibilities Organizational Chart » (H1 de [D22] : « Roles & Responsibilities Organizational Chart » ; références D21 : « Organizational Chart »). Organigramme à comparer au diagramme Mermaid v13 (image non vérifiable en détail). -->

### notes
CDO, DPO & Legal Team rapportent au CEO (indépendance DPO exigée par GDPR art. 38).
<!-- ÉCART : [D22] écrit « RGPD, art. 38 ». -->

DGC présidé par CDO.

MRM rapporte au CDO au quotidien mais peut escalader directement au DGC -- ce qui préserve son indépendance vis-a-vis des équipes dont il évalue les modèles,

DCs centralisés dans Engineering + servent tous les départements transversalement.

MOs dans Product Development, séparés du MRM (principe de séparation exécution / contrôle).

Surcoût de coordination assumé :
à l'échelle de Spotify, cette charge est une nécessité
structurelle.

---

## S06 — Conformité
- layout: columns            <!-- 3 colonnes + bandeau -->
- background: light
- icon: icons/icon_lock.png
- source_line: bottom
- overflow_risk: medium

### kicker
CONFORMITÉ

### title
Socle réglementaire structuré cadre par cadre

### block: card {col=1 header="GDPR"}
- Traitement licite, loyal et transparent
- Droits d'accès, rectification, suppression
- Consentement explicite préalable
- Notification de violation sous 72h
- Data Protection Officer nommé

### block: card {col=2 header="CCPA"}
- Opt-out sur la vente de données
- Droit d'accès, modification, suppression
- Non-discrimination envers les utilisateurs exerçant leurs droits

### block: card {col=3 header="PCI-DSS"}
- Sécurisation de l'infrastructure réseau
- Chiffrement des données de carte bancaire
- Gestion des vulnérabilités
- Contrôle d'accès strict aux données de paiement
- Tests réguliers des dispositifs de sécurité

### block: banner
+ cartographie réglementaire marché par marché - pilotée par Legal Team en lien avec DPO

### source
Source : [D21] (Data & AI Gouvernance Policy) + détails P5 (conformité réglementaire) issus du référentiel [R5] (Compliance Checklist)
<!-- ÉCART : « Gouvernance » (FR) dans un titre anglais et « Document » omis (H1 de [D21] : « Data & AI Governance Policy Document ») ; locator [D21, §2.1.4] absent ; [A1], [A2], [A4] jamais cités ; PDPA absent des colonnes (présent en S03 et en note). -->

### notes
Les trois cadres sont traités séparément dans la politique [D21], chacun avec ses propres exigences opérationnelles issues de la check-liste [R5].

La difficulté spécifique de Spotify est la dimension multi-juridictionnelle (enjeu E3) :

au-delà du socle GDPR/CCPA/PCI-DSS, chaque marché local (ex. PDPA à Singapour) doit être cartographié séparément, sous la responsabilité conjointe de Legal Team et DPO.

---

## S07 — Gouvernance de l'IA
- layout: cards-table
- background: light
- icon: icons/icon_cpu.png
- source_line: bottom
- overflow_risk: high

### kicker
GOUVERNANCE DE L'IA

### title
Responsabilité adaptée au niveau d'impact du modèle

### block: cards {cols=4}
- **Traçabilité**
  Chaque jeu d'entraînement documenté : source, période, transformations, lineage.
- **Biais**
  Évaluation périodique des biais algorithmiques
  pour les modèles à fort impact.
- **Approbation**
  Responsabilité confiée à un Model Owner ;
  circuit proportionné au niveau d'impact.
- **Explicabilité**
  Décisions automatisées à impact significatif explicables de manière intelligible.

### block: table {row_colors="Fort=terracotta,Modéré=green,Faible=gray"}
| Niveau d'impact | Critères | Circuit de validation |
| --- | --- | --- |
| Fort | Majorité des utilisateurs actifs - décision peu réversible - RGPD - fonctionnalité principale | MO (C) → MRM (R) → DGC (A) |
| Modéré | Utilisateurs ciblés (cohorte, marché, A/B test) - décision réversible sous délai court | MO (R) → MRM (A) |
| Faible (défaut) | Fonction auxiliaire, sans exposition directe à l'utilisateur final | MO (RA) + contrôle a posteriori par MRM (échantillonnage) |
<!-- ÉCART : ligne « Fort » : « RGPD » seul remplace « art. 22 RGPD » ([D21-Annexes, §2.1.A.1] : exposition art. 22 ; [D21, §2.1.5] : art. 9 et 22) : le critère d'exposition réglementaire devient imprécis (le RGPD entier ne caractérise pas un fort impact) ; « (extraits) » supprimé alors que les critères restent abrégés (le critère « exposition réglementaire » n'est pas défini pour modéré/faible). « Faible (défaut) » : « défaut » absent de [D21-Annexes, §2.1.A.1/A.3]. « Approbation : Responsabilité confiée à un Model Owner » : le MO est C (fort), R (modéré), RA (faible), cf. [D22-Annexes, §2.2.C]. -->

### block: legend
MO = Model Owner - MRM = Model Risk Manager - DGC = Data Governance Committee - R = Responsible, A = Accountable, C = Consulted

### source
Source : [D21] (Data & AI Governance Policy Document) + détails P8 (gouvernance IA)
<!-- ÉCART : titre corrigé ; locators absents : [D21-Annexes, §2.1.A.3] (circuits), [D22-Annexes, §2.2.C] (RACI) ; « détails P8 » : les détails sont dans [D21, §2.1.5] et [D21-Annexes, §2.1.A]. -->

### notes
La différenciation des circuits d'approbation en fonction des niveaux d’impact évite qu'un circuit conçu pour les modèles à fort impact freine inutilement le déploiement des modèles mineurs.

DGC est responsable (Accountable) de l'approbation des modèles a fort impact.

CDO n'est que consultatif (Consulted) sur cette décision pour réduire le risque qu’il soit à la fois juge et partie sur ses propres arbitrages IA.
<!-- OK : CDO = C sur l'approbation d'un modèle à fort impact ([D22-Annexes, §2.2.C]) ; le circuit [D21-Annexes, §2.1.A.3] ne cite que MO/MRM/DGC. -->

Le calibrage final des seuils des critères de niveau sera affiné avec les résultats du pilote [D3].

---

## S08 — Mise en œuvre
- layout: two-panels
- background: light
- icon: icons/icon_tool.png
- source_line: bottom
- overflow_risk: high

### kicker
MISE EN ŒUVRE

### title
Outillage testé sur un pilote de 21 semaines

### block: table {panel=left title="Outillage par catégorie" tag_style=badge}
| Catégorie | Enjeux / Principes | Outils |
|---|---|---|
| Catalogage | E1, E3 | Collibra (licence commerciale) + OpenMetadata (open-source) |
| Qualité | E2, E5 | Soda Core (open-source) |
| Conformité | E3, E4 | TrustArc (licence commerciale) |
| Sécurité | P3 | Wazuh + OpenBao (open-sources) |
| Gouvernance IA | E5 | MLflow + DVC + AIF360 + AIX360 (open-sources) |
<!-- OK : Collibra E1, E3 conforme à [D3, §3.4]. Table [D3, §3.4] : OpenMetadata E1, Soda Core E2/E5, Wazuh/OpenBao P3, MLflow/DVC/AIF360/AIX360 E5 : conformes. -->

### block: card {panel=right order=1 title="Pilote : Le système de recommandation"}
**21 semaines (~5 mois)**
dont 7 semaines de phase de sécurisation bloquante :
> annuaire central, migration des accès, intégration SSO

### block: card {panel=right order=2 title="Périmètre"}
Modèles et données d'entraînement du système de recommandation
Département Product Development

### block: card {panel=right order=3 title="Indicateurs clés (DMAT)"}
Gouvernance & Qualité : niveau 1 → 2
Gouvernance IA (Analytics & BI) : niveau 2 → 3

### block: card {panel=right order=4 title="Risques clés :"}
- suspension du projet sans solution de repli (absence d'annuaire central, ...)
- débordement de planning dans la phase de déploiement technique
<!-- ÉCART : [D3, §3.5, « Risques » A.2] : le débordement de planning concerne la phase de sécurisation (jalon A, délai TrustArc, test d'intégration, exécution sur 4 semaines), pas le « déploiement technique » (jalon B). Coquille « solution repli » corrigée dans le deck. -->

### source
Source : [D3] (Data & AI Governance Implementation Plan)

### notes
Chaque outil répond a un rôle précis du modèle CoE et un enjeu identifie en [D1].
La sélection résulte d'une comparaison entre les outils recommandes [R8] et des alternatives open source (retenues sur la majorité des lignes, sauf Collibra et TrustArc).

Le pilote est volontairement resserré sur un seul sous-périmètre (système de recommandation)
pour valider :
le rattachement fonctionnel des Data Stewards,
le circuit d'approbation des modèles,
et le coût réel d’ingénierie avant généralisation.

La conformité complète au GDPR (E3/E4) n’est pas dans le périmètre du pilote : un RoPA ne couvrant qu’un seul département ne suffit pas à mettre le projet en conformité avec l’article 30.
<!-- ÉCART : [R8] = tech tools (OK) ; [D3, §3.4] est un locator à ajouter. -->

---

## S09 — Feuille de route
- layout: timeline
- background: light
- icon: icons/icon_map.png
- source_line: bottom
- overflow_risk: medium

### kicker
FEUILLE DE ROUTE

### title
Généralisation en 4 phases vers un niveau 3

### block: timeline {steps=5}
| Phase | Périmètre | Durée | Jalon |
|---|---|---|---|
| Phase 1 - Pilote | Product Development<br>(système de recommandation) | 21 semaines (5 mois) | M5 |
| Phase 2 | Product Development<br>(autres activités) | 3 mois | M10 |
| Phase 3 | Marketing<br>(E1 / E3 / E4) | 3 mois | M15 |
| Phase 4 | Content Curation<br>(E2 / métadonnées) | 3 mois | M20 |
| Consolidation | Ensemble des départements<br>Niveau 3 généralisé | - | M22-M24 |
<!-- OK : durées et jalons M5/M10/M15/M20/M22-M24 conformes à [D3, §3.6] ; « 21 semaines (5 mois) » : [D3, §3.6] « ~5 mois ». La marge de 2 mois après chaque phase 1–3 n'est pas affichée sur la diapositive (voir la note). « Mx » : notation générique, non définie avant ce point (M5…M24 sont affichés au-dessus). -->

### block: banner
Trajectoire de maturité : niveau 1 (actuel) → niveau 3 généralisé (M22 - M24)
M24 = borne haute de la fourchette de référence (15 - 24 mois) pour garantir la rigueur de la phase de sécurisation initiale + marges inter-phases

### block: banner {style=light}
Chaque jalon de phase (Mx) est un point de réévaluation (feu vert / orange / rouge) ≠ engagement figé - conformément au principe d'amélioration continue (P9)

### source
Source : [D3] (Data & AI Governance Implementation Plan)
<!-- ÉCART : fourchette 15-24 mois issue de [R11, Q7] (non cité sur la diapositive, ni la mention des marges inter-phases de [D3, §3.6]) ; « jalon » ici = jalon de phase (M5…M24), distinct des « jalons A–G » de [D3] et des « jalons 01–16 » de [D3-Annexes] : risque de confusion. -->

### notes
Le séquencement suit le niveau de risque et le coût marginal :
- Marketing en priorité pour E3/E4
--- (risque réglementaire le plus élevé),
- puis Content Curation pour E2/métadonnées.

Inter-phases de 2 mois :
5 + 2 + 3 = 10, 10 + 2 + 3 = 15, 15 + 2 + 3 = 20
<!-- OK : arithmétique et marges conformes à [D3, §3.6] (marge de 2 mois après les phases 1, 2 et 3 ; aucune après la phase 4). Puce « --- » (tiret triple) probablement involontaire. -->

La phase de sécurisation (annuaire central, rôles, intégrations SSO) n’est pas reproduite intégralement aux phases suivantes :
seule une migration allégée est reconduite pour chaque département

Message pour le comité : la durée totale du projet  (22-24 mois) est délibérément prudente et sert en grande partie le financement de la phase de sécurisation.

---

## S10 — Valeur & prochaines étapes
- layout: pillars-dark
- background: dark
- icon: icons/icon_flag.png
- source_line:
- overflow_risk: low

### kicker
VALEUR & PROCHAINES ÉTAPES

### title
Une gouvernance qui soutient la confiance & la croissance

### block: cards {cols=4 style=pillar}
- **Économies** {icon=icons/icon_check_white.png}
  Réduction des inefficiences
  liées à une donnée de mauvaise qualité
- **Conformité** {icon=icons/icon_lock.png}
  Éviter les sanctions GDPR/CCPA
  (jusqu'à 4% du CA)
- **Confiance** {icon=icons/icon_shield.png}
  Transparence et sécurité renforcées auprès des utilisateurs
- **Scalabilité** {icon=icons/icon_globe.png}
  Infrastructure de gouvernance prête
  pour la croissance mondiale
<!-- ÉCART : « jusqu'à 4% du CA » : plafond RGPD uniquement, assis sur le CA mondial ([A1, art. 83], [R2]) ; « mondial » supprimé (imprécis) et la formulation « sanctions GDPR/CCPA » l'étend à la CCPA. Ordre des piliers = [R11, Q3] (économies, conformité, confiance, scalabilité) : OK. -->

### block: numbered {title="Prochaines étapes"}
1. Lancer le pilote sur le système de recommandation (Product Development)
2. Nommer / confirmer DPO, CDO, Data Stewards et Model Owners
3. Premières revues de maturité DMAT en milieu et en fin de pilote
4. Décision de passage à l'échelle (feu vert / orange / rouge) à chaque jalon de phase Mx
<!-- OK : deux revues (intermédiaire jalon E, S16-S17 ; finale jalon G, S19-S21 ; [D3, §3.5] et [D3-Annexes, §3.F.4] jalons 12 et 16), cohérent avec la note. Réserve : S17 sur 21 semaines n'est pas « le milieu » ; « Premières » (pluriel) pour deux revues successives ; locator absent. Étape 4 : « jalon de phase Mx » (notation générique). Étape 2 : DGC, MRM, Data Owners, Data Custodians non cités. -->

### block: caption {align=bottom}
Nicolas Pichon --- AIA RNCP 38777 / BC01 / Presentation / v6 --- 2026/10/15
<!-- ÉCART : identique à S01 (séparateurs « --- » cohérents ; « Presentation » en anglais ; en-tête « Step 4 » absent). -->

### notes
Synthèse de la valeur business [R11, Q3] : économies, conformité, confiance, scalabilité.
<!-- ÉCART : le plafond « 4% du CA mondial » ne figure pas dans [R11, Q3] mais dans [R2]. -->

Les prochaines étapes sont volontairement concrètes et actionnables immédiatement :
- lancement du pilote,
- nomination des rôles,
- premières revues DMAT en milieu/fin de pilote,
<!-- OK : note alignée sur la diapositive. -->
- et gouvernance des décisions de passage à l'échelle phase par phase (plutôt qu'un engagement global fige sur 24 mois).
