---
deliverable: D4-Annexes
project: "SPOTIFY - DATA & AI GOVERNANCE PROJECT"
author: Nicolas Pichon
program: AIA RNCP 38777 / BC01 / Présentation / Annexes
version: v5
date: 2026/10/15
locale: fr
slide_size: "13.333x7.5in"      # LAYOUT_WIDE (16:9), identique à D4
source_file: 5011b9cd-spotify-step-4-presentation--annexes.pptx
source_status: current          # remplace la source issue du .md v4 (obsolète)
slide_count: 12
backup_pages: 9                 # B1 à B9 ; B3 et B6 occupent chacune 2 diapositives
footer: "Nicolas Pichon --- AIA RNCP 38777 / BC01 / Présentation / Annexes / v5 --- 2026/10/15"   # présent uniquement sur S01
slide_number_format: "{n} / {N}"
theme_ref: "spotify-step-4-presentation.pptx-source.md (front matter : theme)"   # mêmes polices et palette que D4
theme:
  fonts: {heading: Cambria, body: Calibri}
  colors:
    navy: "1B2A4A"             # S01 (fond), en-têtes de tableau, titres
    green: "1C8C68"
    green_light: "2DBE8C"
    green_pale: "EAF7F1"       # bandeaux et cartes vertes
    terracotta: "B8574A"       # icône d'alerte (B6), bandeau d'alerte
    gray_line: "D8DEE6"
    gray_text: "5B6B84"
    gray_soft: "8493A8"
    gray_bg: "F2F4F7"
    white: "FFFFFF"
  sizes_pt: {kicker: 12, title: 28, title_cover: 36, body: "8.7-12", table: "8-10", source: 9.5}
---

## Spécification du format (section ignorée par le générateur)

Source structurée pour un script de génération PPTX (python-pptx ou pptxgenjs) du **pptx des slides de backup du D4** (12 diapositives, 13,33 × 7,5 in, une seule mise en page « Blank »). Le texte est repris **tel quel** (coquilles et abréviations comprises) ; les écarts de cohérence sont signalés par des commentaires `<!-- ÉCART … -->`, **non corrigés**. Le générateur ignore les commentaires HTML.

**Grammaire** (identique à `spotify-step-4-presentation.pptx-source.md`, avec les ajouts signalés *)

1. Le front matter YAML porte les métadonnées et le thème du deck. Tout ce qui précède le premier `## S..` est ignoré.
2. Une diapositive commence par `## S<NN> - <nom court>`.
3. Métadonnées de diapositive : liste `- clé: valeur`.
   - `layout` : `index-dark` | `table-text` | `cards-2x2` | `callout-table` | `table-stack` | `two-tables` | `table` | `numbered-cards` | `table-banner` ;
   - `background` : `dark` | `light` ;
   - `backup_id` * : identifiant de backup (B1…B9) affiché en kicker ; `page` * : `n/N` pour les backups sur plusieurs diapositives ;
   - `icon` : icône dans le disque (haut droite, x=12.18 in, y=0.4 in, 0.72 in) ; absent sur S01 ;
   - `source_line` : `bottom` (x=0.6 in, y=7.08 in, 9,5 pt, italique gris) ;
   - `answers` * : questions de [R11] auxquelles la diapositive peut servir de réserve (**proposition**, absente du pptx) ;
   - `overflow_risk` : `low` | `medium` | `high`.
4. Sections de niveau 3, dans l'ordre d'affichage : `### kicker`, `### title`, `### subtitle`, `### block: <type> {attributs}` (répétable), `### source`, `### notes`.
5. Types de bloc : `index`*, `cards`, `table`, `bullets`, `numbered`, `callout`, `caption`, `text`.
6. Attributs de bloc : `{col=left|right}`, `{cols=N}`, `{style=...}` (`green`, `alert`, `index`, `numbered-cards`), `{header=...}`, `{tag=...}` (étiquette verte alignée à droite de l'en-tête d'une carte), `{x= y= w= h=}` en pouces.
7. Bloc `cards` : `- **Titre**` avec attribut `{tag=…}` puis sous-puces indentées de 2 espaces.
8. Bloc `table` : première ligne = en-tête ; `<br>` = retour à la ligne ; les cellules vides d'une colonne sont héritées de la ligne précédente (`merge_down=col1`).
9. Inline : `**gras**`, `*italique*`. Les références `[X, §Y]` sont du texte ordinaire (conservées telles quelles, y compris les formes `[D3-C]`).
10. Une section finale `## REFS` * liste les références citées ; elle est **dérivée** du contenu (le pptx n'a pas de diapositive de références), marquée `render: false`.

---

## S01 - Index des backups
- layout: index-dark
- background: dark
- icon:
- source_line:
- overflow_risk: low

### kicker
SPOTIFY - DATA & AI GOVERNANCE PROJECT

### title
Annexes - Slides de Backup

### subtitle
Slides de réserve destinées à répondre aux questions du Comité Exécutif et du Leadership IA, dans l'esprit du guide [R11], sans alourdir le corps de la présentation [D4].

### block: index {cols=3 style=index}
- [B1] Comparaison des modèles d'organisation
- [B2] Justification complète de la sélection d'outils
- [B3] Circuit de gouvernance IA - RACI complètes
- [B4] Plan pilote - calendrier détaillé des jalons
- [B5] Méthode de mesure des KPIs et du double rattachement
- [B6] Gestion des risques du pilote
- [B7] Conditions de passage à l'échelle
- [B8] Ajustements attendus au cadre de gouvernance
- [B9] Trajectoire de maturité détaillée
<!-- ÉCART : les intitulés de l'index diffèrent de ceux des diapositives : B1 « Comparaison des modèles… » / « Modèles d'organisation de la gouvernance data » ; B2 « Justification complète… » / « Justification de la sélection d'outils » ; B3 « …RACI complètes » / « Circuit de gouvernance IA (1/2) - critères de classification » et « (2/2) - matrices RACI » ; B8 « Ajustements attendus au cadre… » / « Ajustements du cadre de gouvernance ». « RACI complètes » : « RACI » est utilisé au féminin pluriel (« matrices RACI »). B3 apparaît sur 2 diapositives (4, 5) et B6 sur 2 (8, 9), mais l'index n'indique pas les numéros de diapositive. -->

### block: caption {align=bottom}
Nicolas Pichon --- AIA RNCP 38777 / BC01 / Présentation / Annexes / v5 --- 2026/10/15
<!-- ÉCART : le D4 v6 porte « Presentation / v6 » (sans accent, sans « Annexes ») ; le pied de page des annexes dit « Présentation / Annexes / v5 » : version v5 ≠ v6, « Présentation » ≠ « Presentation ». L'en-tête « Step 4 » des autres livrables est absent. -->

### notes
Ces slides de backup portent le detail qui etaye le corps de la presentation [D4] : elles sont concues pour repondre en direct a une question precise du comite (modele organisationnel, choix d'outils, circuits RACI, calendrier, risques, criteres de passage a l'echelle) sans alourdir le deroule principal. Contenu repris fidelement des annexes 3.A-3.G du plan d'implementation [D3].
<!-- ÉCART : « annexes 3.A-3.G du plan d'implementation [D3] » → [D3-Annexes, §3.A-3.G] ; or le contenu des backups B3 vient aussi de [D21-Annexes, §2.1.A] et [D22-Annexes, §2.2.C], B5 de [D1-Annexes, §1.A], et il est condensé (« repris fidèlement » : voir les écarts par diapositive). Notes sans accents (« etaye », « concues », « repondre »…). Le D4 v6 ne renvoie à aucune slide de backup. -->

---

## S02 - B1 Modèles d'organisation
- layout: table-text
- background: light
- backup_id: B1
- icon: icon_users.png
- source_line: bottom
- answers: Q5
- overflow_risk: medium

### kicker
B1

### title
Modèles d'organisation de la gouvernance data

### block: table {x=0.6 y=1.75}
| Modèle | Avantages | Limites |
|---|---|---|
| Centralisé | Simple à implémenter, priorisation facile | Déconnexion business/data ; les besoins métier dépassent la capacité de l'équipe centrale |
| Embarqué | Agilité, proximité business/data, spécialisation | Absence de source unique de vérité, silos, difficile à piloter sans bagage technique |
| Center of Excellence | Combine les avantages des deux modèles précédents | Couche de coordination supplémentaire, peu adaptée aux petites/moyennes structures |

### block: bullets {col=left header="Structure générale du modèle CoE (dit aussi hub-and-spoke) :"}
- Le hub : petite équipe d'experts - standards, briques réutilisables, plateforme technique partagée
- Les spokes : rôles embarqués dans chaque unité de métier, agilité et connaissance du domaine locale
- Le conseil de gouvernance : réuni périodiquement, arbitre priorités et exceptions

### block: bullets {col=right header="Analyse d'adéquation au cas Spotify - deux écarts assumés :"}
- Centralisé écarté : isolerait la fonction data, retirerait aux DO l'autorité de proximité (E1)
- Embarqué écarté : reconduirait les silos (E1), disperserait le juridique (E3)
- CoE retenu : seul modèle qui répond simultanément à E1, E3 et E5
- Écart 1 : infrastructure technique maintenue dans Engineering (dépt. pair, pas le hub)
- Écart 2 : autorités de conformité (DPO/Legal) et de gouvernance (CDO/DGC) séparées, toutes deux rattachées au CEO
<!-- OK : contenu conforme à [D3-Annexes, §3.B.1-3.B.4], [D3, §3.3] et [D22] (écarts, E1/E3/E5). ÉCART : l'en-tête « Analyse d'adéquation… - deux écarts assumés » regroupe sous un même titre l'analyse des 3 modèles et les 2 écarts au modèle canonique ([D3-Annexes, §3.B.4] : « deux points », « Nuance #1/#2 »). « Center of Excellence » (D3-Annexes, tableau 3.B.1 : « Centre of Excellence »). Sigles DO, DPO, DGC, CDO, CEO, Legal non définis. -->

### block: callout {style=green}
Principe : « gouverner et outiller au centre, exécuter à la périphérie »

Surcoût du CoE assumé : à l'échelle de Spotify, la charge de coordination est une nécessité fonctionnelle, non un coût additionnel.

### source
Source : [D3-B], annexe 3.B.1-3.B.4 - [R7]
<!-- ÉCART : locator « [D3-B], annexe 3.B.1-3.B.4 » → [D3-Annexes, §3.B.1-3.B.4] (la forme « [D3-B] » ne suit pas la convention de locator). -->

---

## S03 - B2 Sélection des outils
- layout: cards-2x2
- background: light
- backup_id: B2
- icon: icon_tool.png
- source_line: bottom
- answers: Q8, Q4, Q10
- overflow_risk: high

### kicker
B2

### title
Justification de la sélection d'outils

### block: bullets {x=0.6 y=1.75 w=12.13 h=0.95}
- Repartir de [R8], compléter par l'open source, prioriser l'open source
- Économie de licence compensée par l'hébergement, absorbée par la capacité d'ingénierie Spotify [R2]
- Risque réglementaire chiffrable (E3, E4) → garanties commerciales ; risque opérationnel (E1, E2, E5) → coût de défaillance interne seulement

### block: cards {cols=2 style=cards-2x2}
- **Catalogage** {tag="OpenMetadata + Collibra"}
  - Apache Atlas écarté : ancré Hadoop, absent de la stack Spotify
  - Alation/Collibra retenues pour la garantie de service (E3) ; Collibra choisie pour son socle de gouvernance plus solide
  - Connecteur officiel OpenMetadata ↔ Collibra (sync glossaires, correspondance des actifs)
- **Qualité** {tag="Soda Core (replis Cuallee / TestGen)"}
  - Talend écarté : redondant avec l'ETL existant
  - Informatica écartée : fragmentation, compétences incompatibles avec le profil DS, coût/délais disproportionnés
  - Ataccama écartée : coût élevé et opaque, non justifié pour des enjeux opérationnels
  - Soda Core retenu (E2, E5) ; repli Cuallee (contrôles ML) ou TestGen (si dépriorisation confirmée)
- **Conformité réglementaire** {tag="TrustArc"}
  - VeraSafe écarté : conseil/services managés, pas un logiciel
  - DataGuard écarté : positionné PME, hors échelle Spotify
  - TrustArc retenue sur OneTrust : automatisation multi-juridictionnelle + ergonomie DPO
  - Couvre nativement les DSAR, attendu du dispositif central [R11, Q4]
- **Sécurisation données & accès** {tag="Wazuh + OpenBao"}
  - DataGuard reclassée avec les outils de conformité
  - Vormetric écartée (licence propriétaire) au profit d'OpenBao (mêmes services de gestion des clés, sans coût de licence)
  - OpenBao : gestion des clés + chiffrement à l'appel via Transit - pas un chiffrement transparent automatique
<!-- ÉCART : (1) titre « Justification de la sélection d'outils » ≠ index « Justification complète… » ; la sélection n'est pas complète : Splunk (rejeté au profit de Wazuh, [D3-Annexes, §3.C.5]) n'apparaît pas, ni les outils de gouvernance des modèles MLflow, DVC, AIF360, AIX360 ([D3-Annexes, §3.C.6]) que le D4 v6 S08 cite. (2) « TrustArc… Couvre nativement les DSAR, attendu du dispositif central [R11, Q4] » : [R11, Q4] évoque des « outils de gestion des demandes » sans « nativement » ([D3-Annexes, §3.C.4] formule « attendue nativement ») ; B8 (point 4) prévoit par ailleurs de valider séparément la couverture DSAR de TrustArc avant la phase 3 : la diapositive l'affirme comme acquis. (3) Informatica : « coût/délais disproportionnés » : les délais (1 à 2 semestres) de [D3-Annexes, §3.C.3] ne sont pas repris. (4) « DS » (Data Steward), « ETL », « DSAR », « E1…E5 » non définis. (5) Texte en 8,7 pt dans les cartes : lisibilité. (6) Conforme au fond de [D3-Annexes, §3.C.1-3.C.5] (hors points ci-dessus). -->

### source
Source : [D3-C] - Alternatives évaluées : [R8]
<!-- ÉCART : locator « [D3-C] » → [D3-Annexes, §3.C.1-3.C.5]. -->

---

## S04 - B3 Circuit de gouvernance IA (1/2)
- layout: callout-table
- background: light
- backup_id: B3
- page: 1/2
- icon: icon_cpu.png
- source_line: bottom
- answers: Q12
- overflow_risk: medium

### kicker
B3

### title
Circuit de gouvernance IA (1/2) - critères de classification

### block: callout {style=green}
La gouvernance IA est proportionnée au niveau d'impact de chaque modèle sur l'utilisateur et sur l'entreprise, car les procédures applicables aux modèles fortement impactants ne doivent pas freiner le déploiement des modèles à faible risque (qui peuvent bénéficier d’une procédure plus simple).
<!-- ÉCART : le D4 v6 / [D21, §2.1.5] ne contiennent pas cette formulation (le texte de P8 [D21, §2.1.3] non plus) ; la proportionnalité est posée en [D21, §2.1.5] et [D21-Annexes, §2.1.A]. « fortement impactants » / « faible risque » : [D21] dit « impact fort / faible ». -->

### block: text {header="Critères de classification avec degré d'automatisation [D3-E] :"}
Critères de classification avec degré d'automatisation [D3-E] :

### block: table
| Niveau | Critères | Automatisation |
|---|---|---|
| Fort impact | Portée majoritaire des utilisateurs actifs | Calculé (métadonnées MLflow) |
| | Exposition art. 22 GDPR | Calculé (lineage OpenMetadata/Collibra) |
| | Décision peu réversible | Déclaratif (Model Owner) |
| | Fonctionnalité principale du produit | Déclaratif (Model Owner) |
| Impact modéré | Portée partielle (cohorte, marché, A/B test) | Calculé |
| | Décision réversible sous délai court | Déclaratif |
| Impact faible | Aucun critère de fort impact rempli | Par défaut |
<!-- ÉCART : (1) ligne « Exposition art. 9 RGPD (données personnelles) - calculé automatiquement » de [D3-Annexes, §3.E] absente, alors que [D21, §2.1.5] cite les art. 9 et 22 ; note « (*) sauf pour la mesure de l'effet significatif (déclaré) » absente. (2) « GDPR » → RGPD dans les annexes. (3) Le tableau croise la définition des niveaux ([D21-Annexes, §2.1.A.1], source unique) et la calculabilité ([D3-Annexes, §3.E]) : les critères sont dupliqués ; « Impact faible » : [D21-Annexes, §2.1.A.1] dit « fonction auxiliaire, sans exposition directe à l'utilisateur final ». (4) « [D3-E] » → [D3-Annexes, §3.E]. -->

### block: caption
Trois activités distinctes : classification (unique, création) - approbation de déploiement (chaque version, hérite du niveau) - reclassification (rare).
<!-- OK : conforme à [D21-Annexes, §2.1.A.4]. -->

### source
Source : [D21-A]
<!-- ÉCART : locator « [D21-A] » → [D21-Annexes, §2.1.A] (ou §2.1.A.1, A.3, A.4). -->

---

## S05 - B3 Circuit de gouvernance IA (2/2)
- layout: table-stack
- background: light
- backup_id: B3
- page: 2/2
- icon: icon_cpu.png
- source_line: bottom
- answers: Q12
- overflow_risk: medium

### kicker
B3

### title
Circuit de gouvernance IA (2/2) - matrices RACI

### block: text {header="Classification (événement unique, à la création du modèle dans le registre)"}
Classification (événement unique, à la création du modèle dans le registre)

### block: table
| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Classifier un modèle | I | I | – | I | I | I | R | A | – | I |

### block: text {header="Approbation de déploiement (répétée à chaque version, hérite du niveau fixé)"}
Approbation de déploiement (répétée à chaque version, hérite du niveau fixé)

### block: table
| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Fort impact | A | C | I | I | I | I | C | R | C | I |
| Impact modéré | I | C | I | I | I | I | R | A | I | I |
| Impact faible (auto-certif.) | – | I | – | I | I | I | RA | I | – | – |

### block: text {header="Contrôle a posteriori et reclassification (événements rares)"}
Contrôle a posteriori et reclassification (événements rares)

### block: table
| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Contrôle par échantillonnage (faible) | I | I | – | I | I | I | I | RA | – | – |
| Reclasser un modèle | I | I | – | I | I | I | C | RA | – | I |

### block: legend
R = Responsible, A = Accountable, C = Consulted, I = Informed.

### block: caption
Le nombre de parties prenantes décroît mécaniquement avec le niveau d'impact.
<!-- OK : les 5 lignes RACI correspondent à [D22-Annexes, §2.2.C] (Classifier ; Approuver fort/modéré ; Déployer faible ; Contrôler par échantillonnage ; Reclassifier) et la phrase finale à sa « Lecture des matrices ». ÉCART : sigles DGC, CDO, DPO, DO, DS, DC, MO, MRM non définis (seuls R/A/C/I le sont) ; « RACI » masculin/féminin : « matrices RACI » / « RACI complètes ». -->

### source
Source : [D21-A]
<!-- ÉCART : la matrice RACI provient de [D22-Annexes, §2.2.C], pas de [D21-Annexes, §2.1.A] (qui renvoie à [D22-Annexes, §2.2.C] pour le RACI) ; locator « [D21-A] » incorrect pour cette diapositive. -->

---

## S06 - B4 Plan pilote : jalons
- layout: two-tables
- background: light
- backup_id: B4
- icon: icon_map.png
- source_line: bottom
- answers: Q7, Q10
- overflow_risk: high

### kicker
B4

### title
Plan pilote - calendrier détaillé des jalons

### block: table {col=left x=0.6 y=1.72 w=5.9}
| Jalon | Sem. | Actions | Porteur |
|---|---|---|---|
| 01 | S1 | Lancement, confirmation annuaire central SAML/OIDC | PPM, DC |
| 02 | S1-S3 | Sécurisation infra. préexistantes ; régén. secrets, collecte profils | DC |
| 03 | S3-S4 | Vérification capacités SSO/sync. groupes de TrustArc | DPO, Legal |
| 04 | S4-S5 | Vérification RBAC natif MLflow, AIF360, AIX360, Wazuh | DC, MO, MRM |
| 05 | S5-S6 | Test d'intégration bout-en-bout (annuaire, OMD, Collibra, TrustArc, OpenBao) | DC |
| 06 | S7 | Revue phase de sécurisation : poursuite ou suspension | PPM, DGC |
| 07.1 | S8-S11 | Déploiement technique (OMD, DVC, Soda Core, MLflow, AIF360, AIX360, Wazuh, OpenBao) | DC |
| 07.2 | S8-S17 | Population initiale du RoPA (TrustArc) scopée PD | DPO, Legal |
| 08.1 | S12 | Vérif. recouvrement Soda Core / module qualité OpenMetadata | DC |

### block: table {col=right x=6.65 y=1.72 w=5.9}
| Jalon | Sem. | Actions | Porteur |
|---|---|---|---|
| 08.2 | S12 | Population initiale du glossaire Collibra scopée PD | DS |
| 09 | S13 | Vérification du connecteur Collibra-OpenMetadata | DC |
| 10.1 | S14 | Classification initiale du modèle testé | MO, MRM |
| 10.2 | S14-S17 | Exécution réelle : qualité courante et données d'entraînement, entraînement/évaluation | DS, MO |
| 11 | S16 | Vérification technique intermédiaire (résultats Soda Core) | DS |
| 12 | S17 | Revue intermédiaire (Engineering overhead, adoption standards) | PPM |
| 13 | S18 | 1er passage du circuit d'approbation (niveau classé au J.10.1) | MRM, DGC |
| 14 | S19 | Consolidation des indicateurs, recueil des retours | Toute l'équipe |
| 15 | S20 | Revue de synthèse | PPM |
| 16 | S21 | Revue finale et clôture du pilote | DGC |
<!-- OK : 16 jalons, semaines (21 semaines, sécurisation S1-S7 = jalons 01-06, cf. D4 v6 S08) et porteurs conformes à [D3-Annexes, §3.F.4]. ÉCART : (1) « (x) Phase de sécurisation » et colonne « Repère » (A à G, lien avec les jalons A-G de [D3, §3.5]) supprimées : aucun lien visible entre la phase de sécurisation et les jalons 01-06. (2) Abréviations non définies : PPM, DC, DS, MO, MRM, DGC, DPO, OMD (OpenMetadata, abréviation propre à cette diapositive), PD, RoPA, SSO, RBAC, SAML/OIDC. (3) Jalon 13 : « selon niveau » (MRM, DGC selon niveau) omis ; jalon 11 : « premiers résultats » omis ; notation « J.10.1 » ≠ « Jalon 10.1 ». (4) Tableaux en 8 pt : lisibilité. -->

### block: caption {x=0.6 y=6.05 w=12.13}
Livrables : rapport qualité des données - rapport de validation du circuit de classification/approbation - estimation Engineering overhead - note de recouvrement technique - note de synchronisation catalogage - note de contrôle d'accès - rapport de migration de sécurisation - rapport de déploiement initial Collibra/RoPA - retours des parties prenantes - rapport d'évaluation du double rattachement.
<!-- OK : les 10 livrables de [D3-Annexes, §3.F.5] et [D3, §3.5] (version condensée : précisions « main-d'œuvre uniquement », « TrustArc à valider spécifiquement » omises). -->

### source
Source : [D3-F]
<!-- ÉCART : locator « [D3-F] » → [D3-Annexes, §3.F.4-3.F.5]. -->

---

## S07 - B5 Mesure des KPIs
- layout: table-stack
- background: light
- backup_id: B5
- icon: icon_barchart.png
- source_line: bottom
- answers: Q6
- overflow_risk: high

### kicker
B5

### title
Méthode de mesure des KPIs et du double rattachement

### block: text {header="Méthode de mesure des dimensions DMAT (re-cotation sur le périmètre pilote uniquement) :"}
Méthode de mesure des dimensions DMAT (re-cotation sur le périmètre pilote uniquement) :

### block: table
| Dimension | Porteur | Jalon | Instrument de mesure |
|---|---|---|---|
| Data Governance | PPM (auto-éval.), validation DGC | J.16 | Re-cotation Q1-Q6, Q10-Q13 [R1] |
| Data Quality | Data Steward, PPM | J.12 puis 16 | Re-cotation Q36-Q39 [R1], journaux Soda Core |
| Analytics & BI (IA) | Model Owner, MRM | J.12 puis 16 | Re-cotation Q55-Q57 [R1], dossier + AIF360/AIX360 |

### block: callout
Nature de l'exercice : jugement qualitatif ancré à des artefacts opérationnels datés (logs, horodatages, dossiers) plutôt qu'à un texte narratif rédigé a posteriori - la validation DGC réduit le biais d'auto-évaluation sans rendre le jugement objectif.

### block: text {header="Évaluation du double rattachement des Data Stewards - 5 indicateurs complémentaires :"}
Évaluation du double rattachement des Data Stewards - 5 indicateurs complémentaires :

### block: table
| Indicateur | Méthode de mesure | Source |
|---|---|---|
| Taux d'adoption des standards CDO | Règles Soda Core « standard CDO » vs « spécifique domaine » | DC |
| Délai de propagation d'une MàJ | Horodatage du workflow de révision/approbation Collibra | PPM |
| Fréquence de sollicitation fonctionnelle | Comptage des échanges DS → CDO sur Collibra | DS |
| Cohérence terminologique | Taux de correspondance exacte au glossaire Collibra | DC, DS |
| Autonomie départementale préservée | Part des décisions métier prises sans blocage, registre DO | DO |

### block: caption
Le critère négatif (absence de conflit) devient insuffisant seul : un canal jamais utilisé afficherait aussi zéro conflit. L'indicateur d'autonomie sert de garde-fou.
<!-- OK : conforme à [D3-Annexes, §3.F.6] (3 dimensions, jalons 12 puis 16, Q de [D1-Annexes, §1.A], 5 indicateurs, lecture combinée) et cohérent avec D4 v6 S10 (revues DMAT en milieu et en fin de pilote = jalons 12 et 16). ÉCART : « Jalon » : « J.16 », « J.12 puis 16 » (D3-Annexes : « Jalon 16 »/« #16 ») ; la mention « 3 des 5 indicateurs captés nativement par Collibra » et le calendrier de collecte (jalons 01, 10.2, 12, 16) de [D3-Annexes, §3.F.6] ne sont pas repris ; « MàJ » abréviation ; « critère négatif » : terme de [D3-Annexes, §3.F.6] non défini ici (« critère de passage à l'échelle du double rattachement », [D3-Annexes, §3.G.1]). -->

### source
Source : [D3-F]
<!-- ÉCART : locator → [D3-Annexes, §3.F.6] et [D1-Annexes, §1.A] pour la liste des questions Q1-Q6, Q10-Q13 ; Q36-Q39 ; Q55-Q57. -->

---

## S08 - B6 Risques du pilote (1/2)
- layout: table-stack
- background: light
- backup_id: B6
- page: 1/2
- icon: icon_alert.png
- icon_style: terracotta
- source_line: bottom
- answers: Q11, Q2
- overflow_risk: medium

### kicker
B6

### title
Gestion des risques du pilote (1/2) - suspension & débordement

### block: text {header="Risques de suspension (sans repli) :"}
Risques de suspension (sans repli) :

### block: table
| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Absence d'annuaire central apte SAML/OIDC (J.01) | Faible à moyenne | Suspension totale | Devient un chantier d'infrastructure séparé |
| Défaut de sécurisation non corrigeable (J.02) | Faible | Suspension si non corrigé avant J.06 | Repli possible si périmètre isolable |

### block: text {header="Risques de débordement de planning :"}
Risques de débordement de planning :

### block: table
| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Délai de réponse TrustArc (SSO, J.03) | Moyenne | Débordement du J.03 | Gestion manuelle temporaire, documentée |
| Échec du test d'intégration bout-en-bout (J.05) | Moyenne | Débordement du J.06, retard en cascade | Identifier le maillon défaillant avant correction |
| Compression de l'exécution réelle (J.10.2, 4 sem.) | Moyenne | Fiabilité réduite des indicateurs | Rallongement ponctuel si J.11 instable |

### block: callout {style=alert}
Ces deux catégories sont propres à la phase de sécurisation (Jalons 01-06) et signalées explicitement plutôt que noyées dans le reste du tableau des risques opérationnels (slide suivante).
<!-- OK : conforme à [D3-Annexes, §3.F.8] (4 risques, probabilités, impacts, mitigations ; catégories propres à la phase de sécurisation, jalons 01-06) et à [D3, §3.5] (risques A.1 et A.2). ÉCART : le D4 v6 S08 écrit « débordement de planning dans la phase de déploiement technique » ; cette diapositive (et [D3, §3.5]) rattache le débordement à la phase de sécurisation (J.03, J.05, J.10.2) : les deux textes du D4 divergent. « slide suivante » : « diapositive ». « (J.xx) » vs « Jalon xx ». -->

### source
Source : [D3] §3.F.8
<!-- ÉCART : locator « [D3] §3.F.8 » → [D3-Annexes, §3.F.8]. -->

---

## S09 - B6 Risques du pilote (2/2)
- layout: table
- background: light
- backup_id: B6
- page: 2/2
- icon: icon_alert.png
- icon_style: terracotta
- source_line: bottom
- answers: Q11, Q2
- overflow_risk: medium

### kicker
B6

### title
Gestion des risques du pilote (2/2) - risques opérationnels

### block: table
| Risque | Prob. | Impact | Mitigation |
|---|---|---|---|
| Charge Data Custodians sous-estimée (4 outils/10) | Élevée | Élevé | Suivi hebdo ; bascule possible vers Collate |
| Collecte incomplète des profils d'accès (J.02) | Moyenne | Élevé | Recoupement systématique avant redéfinition |
| Soda Core insuffisant pour E5 | Moyenne | Moyen | Vérif. J.08.1/11 ; repli Cuallee |
| Dépriorisation long terme de Soda Core | Moyenne | Faible-moyen | Suivi post-pilote ; repli TestGen si confirmé |
| Décalage sync. Collibra/OpenMetadata | Faible | Moyen | Vérif. J.09 ; calibrage sur délai 72h |
| Seuils de classification mal calibrés | Moyenne | Moyen | Mesure du délai réel au J.13 ; resserrement |
| Résistance au changement du dépt. pilote | Moyenne | Moyen | Cf. formation §3.F.9 |
| Désalignement cycles budgétaires trimestriels | Moyenne | Moyen | Anticiper la demande Phase 3 avant clôture P2 |
| Déploiement Collibra/RoPA plus long que prévu | Moyenne | Moyen | Prioriser la classification des données sensibles |
| Absence de classification préalable (RoPA) | Élevée | Moyen | Population du RoPA documentée comme provisoire |
<!-- OK : 10 risques, probabilités et impacts conformes à [D3-Annexes, §3.F.8] et à [D3, §3.5] (liste B). ÉCART : « Charge Data Custodians sous-estimée (4 outils/10) » : [D3, §3.5] dit « 3 outils sur 10 » (OpenMetadata, Wazuh, OpenBao opérés par les DC, [D3, §3.4]) ; [D3-Annexes, §3.F.8] ne donne pas de décompte. « Cf. formation §3.F.9 » → [D3-Annexes, §3.F.9] (D3-Annexes : l'offre managée « Collate » n'est pas définie ici). Abréviations « P2 » (Phase 2), « dépt. », « Vérif. », « J.xx ». Tableau 9,3 pt. -->

### source
Source : [D3] §3.F.8
<!-- ÉCART : locator → [D3-Annexes, §3.F.8]. -->

---

## S10 - B7 Conditions de passage à l'échelle
- layout: table
- background: light
- backup_id: B7
- icon: icon_flag.png
- source_line: bottom
- answers: Q11, Q6, Q7
- overflow_risk: medium

### kicker
B7

### title
Conditions de passage à l'échelle (feu 🟢 🟠 🔴)

### block: table
| Dispositif testé | Critère de passage à l'échelle | Si échec / résultat mitigé |
|---|---|---|
| Double rattachement Data Steward (E1) | Absence de conflit d'autorité rapporté | Clarifier par écrit avant extension, plutôt qu'abandonner |
| Soda Core / module qualité OpenMetadata | Décision explicite au Jalon 08.1 | Généraliser uniquement l'outil retenu |
| Connecteur Collibra/OpenMetadata | Synchronisation vérifiée (J.09), compatible délai 72h | Resserrer la fréquence ou intégration complémentaire |
| Soda Core pour la qualité ML (E5) | Contrôles jugés suffisants entre J.08.1 et 11 | Bascule vers Cuallee, sans réintroduire Deequ/Spark |
| Circuit de classification/approbation ([D3-E]) | Délai mesuré au J.13, compatible mise en prod. | Resserrer les critères plutôt qu'alléger le circuit |
| Déploiement incrémental Collibra/RoPA (E1, E3) | Configuration scopée PD extensible sans reconstruction | Revoir l'architecture avant Phase 3 |
| Engineering overhead Data Custodians | Estimation (J.12) vs capacité réelle | Séquencer le déploiement sur plusieurs trimestres |
| Phase de sécurisation elle-même | Franchissement du J.06 sans suspension | Traiter comme chantier séparé avant généralisation |
<!-- OK : 8 dispositifs, critères et replis conformes à [D3-Annexes, §3.G.1] et [D3, §3.6]. ÉCART : « Circuit de classification/approbation ([D3-E]) » : les circuits sont dans [D21-Annexes, §2.1.A.3] (que [D3-Annexes, §3.G.1] cite) ; [D3-Annexes, §3.E] ne traite que de la calculabilité. « Soda Core pour la qualité ML (E5) » ≠ « données d'entraînement (E5) » ([D3-Annexes, §3.G.1]). « Deequ/Spark » non défini ; « Jalon 08.1 » / « J.09 » : deux notations dans la même table ; emoji dans le titre (rendu variable selon la police) ; phrase « Traiter comme chantier séparé avant généralisation » : [D3-Annexes, §3.G.1] précise « avant toute généralisation, pas seulement avant la Phase 2 » (nuance omise). -->

### source
Source : [D3-G]
<!-- ÉCART : locator → [D3-Annexes, §3.G.1]. -->

---

## S11 - B8 Ajustements du cadre
- layout: numbered-cards
- background: light
- backup_id: B8
- icon: icon_shield.png
- source_line: bottom
- answers: Q9, Q8
- overflow_risk: low

### kicker
B8

### title
Ajustements du cadre de gouvernance

### block: numbered {style=numbered-cards}
1. Calibrer les seuils des critères des niveaux d’impact des modèles =, selon les résultats du pilote
2. Réviser le tableau d'outils sur les deux lignes explicitement testées (recouvrement Soda Core/OpenMetadata & capacité de Soda Core / E5)
3. Établir un coût total de possession (infrastructure, maintenance pluriannuelle) dès qu’un historique d'exploitation suffisant est disponible
4. Valider la couverture DSAR de TrustArc (en s'appuyant sur le RoPA pilote)
5. Documenter l'extension légère de sécurisation (régénération des secrets, collecte des profils) - répétée pour chaque département
<!-- OK : 5 ajustements dans l'ordre de [D3-Annexes, §3.G.3] ; l'ancien point « intégration formelle de l'amendement dans [D21]/[D22] » n'y figure plus (faite en D21 v15, D21-Annexes v15, D22-Annexes v14) : cohérent. ÉCART : point 1 : coquille « =, » ; titre « Ajustements du cadre » ≠ index « Ajustements attendus au cadre » ; point 4 : l'exercice « séparé, porté par DPO/Legal Team, avant l'ouverture de la phase 3 (Marketing) » et la réserve « sous réserve que la classification préalable des données soit établie » ([D3-Annexes, §3.G.3]) sont omis ; point 2 : « tableau d'outils » sans renvoi à [D3, §3.4] ; point 5 : « répétée pour chaque département » ([D3-Annexes, §3.G.3] : « distincte de la phase de sécurisation complète »). -->

### source
Source : [D3-G]
<!-- ÉCART : locator → [D3-Annexes, §3.G.3]. -->

---

## S12 - B9 Trajectoire de maturité
- layout: table-banner
- background: light
- backup_id: B9
- icon: icon_globe.png
- source_line: bottom
- answers: Q7, Q6
- overflow_risk: low

### kicker
B9

### title
Trajectoire de maturité détaillée

### block: table
| Échéance | Étape | Niveau de maturité visé | Repère exécutif [R11, Q7] |
|---|---|---|---|
| M5 | Pilote clos, décisions go/no-go prises | Niveau 2 sur le périmètre pilote (Governance, Quality) | Borne haute fourchette pilote (3-6 mois) |
| M10 | Product Development couvert dans son ensemble | Niveau 2-3 sur Governance et Quality, étendu à tout PD | Dans la fenêtre de déploiement (+12-18 mois) |
| M15 | Marketing couvert | Niveau 2-3 sur Compliance et Data Usage & Accessibility | Dans la fenêtre de déploiement |
| M20 | Content Curation couvert, Engineering élargi | Niveau 3 sur Metadata et Master & Reference Data | Borne haute du déploiement complet |
| M22-M24 | Ensemble des départements couverts | Niveau 3 généralisé [D21 §2.1.7] | Borne haute de la fourchette [R11, Q7] |

### block: caption {style=banner}
Trajectoire indicative : chaque jalon de phase est un point de réévaluation, la feuille de route elle-même soumise au principe d'amélioration continue qu'elle sert à mettre en œuvre
<!-- OK : échéances M5/M10/M15/M20/M22-M24 identiques à D4 v6 S09 ; étapes et niveaux conformes à [D3-Annexes, §3.G.4] et [D3, §3.6]. ÉCART : (1) ligne M20 : « Borne haute du déploiement complet » ≠ [D3-Annexes, §3.G.4] « Approche la borne haute du déploiement complet » (la borne haute est M22-M24) ; (2) la fenêtre « +12-18 mois » de [R11, Q7] s'applique après le pilote : de M5 à M24 le déploiement dure 19 mois ; [D3-Annexes, §3.G.4] lit la fourchette sur le total (15-24 mois) ; la ligne M15 omet « (+12-18 mois) » ; (3) « Governance », « Quality » (noms DMAT : « Data Governance », « Data Quality ») ; (4) la durée totale de 22-24 mois et les marges de 2 mois entre phases de [D3-Annexes, §3.G.4] ne figurent pas ; (5) « [D21 §2.1.7] » → [D21, §2.1.7] ; « Niveau 3 généralisé » : [D3-Annexes] précise « sur l'ensemble des dimensions actuellement en niveau 1 » ; (6) colonne « Repère exécutif » ≠ « Position par rapport au budget de référence [R11, Q7] » ([D3-Annexes, §3.G.4]). -->

### source
Source : [D3-G]
<!-- ÉCART : locator → [D3-Annexes, §3.G.4]. -->

---

## REFS
- render: false
- derived_from_content: true
<!-- ÉCART : le pptx n'a ni diapositive de références ni légende des sigles, contrairement aux annexes écrites ([D21-Annexes], [D22-Annexes], [D3-Annexes]). Liste dérivée des renvois cités. -->

### block: bullets {header="Livrables"}
- [D1] Data & AI Maturity Assessment Report
- [D21] Data & AI Governance Policy Document (cité « [D21 §2.1.7] », « [D21-A] »)
- [D3] Data & AI Governance Implementation Plan (cité « [D3] », « [D3] §3.F.8 », « [D3-B] », « [D3-C] », « [D3-E] », « [D3-F] », « [D3-G] »)
- [D4] Présentation (corps du deck)

### block: bullets {header="Annexes (cités sous une forme abrégée non conforme)"}
- [D21-Annexes] (cité « [D21-A] »)
- [D3-Annexes] (cité « [D3-B] », « [D3-C] », « [D3-E] », « [D3-F] », « [D3-G] »)
- [D22-Annexes] (non cité : source des matrices RACI de S05)
- [D1-Annexes] (non cité : source des questions DMAT de S07)

### block: bullets {header="Ressources"}
- [R1] Australian Government Data Maturity Assessment Tool (2026)
- [R2] Spotify Business Case
- [R7] Organizational Models
- [R8] Tech Tools Overview
- [R11] Executive Q&A Guide
