*SPOTIFY DATA & AI GOVERNANCE* PROJECT
===

# 4. *Final Presentation to Stakeholders*

> *Nicolas Pichon - AIA RNCP 38777 / BC01 Présentation du 2026/10/13 - v3.*

---

## Annexes — Slides de backup

*Slides de réserve destinées à répondre aux questions du Comité Exécutif et du Leadership IA, dans l'esprit du guide \[R11\], sans alourdir le corps de la présentation \[D4\].*

---

### B1. Comparaison des modèles d'organisation de la gouvernance data

| Modèle | Avantages | Limites |
|---|---|---|
| Centralisé | Simple à implémenter, priorisation facile | Déconnexion business/data ; les besoins métier finissent par dépasser la capacité de l'équipe centrale |
| Embarqué | Agilité, proximité business/data, spécialisation | Absence de source unique de vérité, création de silos, difficile à piloter pour les métiers sans bagage technique |
| Center of Excellence (CoE) | Combine les avantages des deux modèles précédents | Nécessite une couche de coordination supplémentaire, peu adaptée aux petites/moyennes structures |

**Structure générale du modèle CoE** — un modèle *hub-and-spoke* (centre-et-antennes) à trois composantes :
- Le **hub** : une petite équipe d'experts qui fixe les standards, construit les briques réutilisables (méthodologie, outillage, formation) et porte la plateforme technique partagée.
- Les **spokes** : des rôles embarqués dans chaque unité de métier, exécutant avec la connaissance du domaine et l'agilité locale.
- Le **conseil de gouvernance** : réuni périodiquement, arbitre priorités et exceptions.

Principe résumé : *« gouverner et outiller au centre, exécuter à la périphérie »*.

**Analyse d'adéquation au cas Spotify** \[D3 §3.B\] :

- *Centralisé* — isolerait la fonction data dans une organisation où les départements se sont déjà appropriée la donnée (\[D1\] : littératie data et usage analytique bien implantés, portés par des équipes de métier autonomes) ; retirerait aux Data Owners l'autorité de proximité nécessaire à E1.
- *Embarqué* — reconduirait par construction l'enjeu E1 à l'origine des silos ; disperserait les ressources juridiques à travers départements et marchés, empêchant de traiter E3.
- *CoE* — le seul des trois modèles courants qui réponde simultanément à E1 (décompartimentation), E3 (conformité multi-juridictionnelle globale/locale) et E5 (gouvernance IA).

**Les deux écarts au modèle canonique** \[D22, D3 §3.B.4\] :

1. **Infrastructure et compétences techniques maintenues dans *Engineering*.** Le modèle générique CoE place la plateforme technique partagée au sein du hub, au même niveau que l'autorité de standards. Ce n'est pas le cas ici : les Data Custodians sont rattachés organiquement à *Engineering*, traité comme un département de métier pair (au même niveau que Marketing, Product Development, etc.), non comme une entité élevée au niveau CDO/DGC.
2. **Autorités de conformité et de gouvernance des données séparées et indépendantes.** Le modèle générique CoE ne distingue normalement pas ces deux autorités sous un hub unique. Ici, elles sont toutes deux rattachées directement au CEO, sans hiérarchie entre elles : gouvernance (CDO, DGC) d'un côté, conformité (DPO, Legal Team) de l'autre.

**Surcoût du CoE, assumé** : le CoE est réputé difficile à adapter aux petites/moyennes structures du fait de la charge de coordination supplémentaire. Mais à l'échelle de Spotify (450M+ utilisateurs, 180+ pays, départements autonomes, régimes réglementaires hétérogènes), cette charge est une nécessité fonctionnelle, non un coût additionnel — seul ce modèle est structurellement conçu pour l'absorber.

*Source : \[D3\] §3.B, annexe 3.B.1-3.B.4 · \[R7\]*

---

### B2. Justification complète de la sélection d'outils

**Principes** \[D3 §3.C.1\] :
1. Repartir des recommandations \[R8\], compléter par des alternatives open source, prioriser l'open source.
2. L'économie de licence est généralement compensée par le coût d'hébergement/exploitation — mais la capacité d'ingénierie interne de Spotify \[R2\] permet de la maintenir au niveau des solutions propriétaires.
3. Les enjeux à risque réglementaire chiffrable (E3, E4) justifient des garanties contractuelles commerciales ; les enjeux organisationnels/opérationnels (E1, E2, E5) ne portent qu'un coût de défaillance interne.

**Catalogage** — *OpenMetadata (inventaire technique, lineage) + Collibra (glossaires, workflows)*
- *Apache Atlas* \[R8\] : solide et open source, mais historiquement ancré dans l'écosystème Hadoop, absent de l'infrastructure Spotify (data lakes, bases relationnelles, cloud) \[R2\]. OpenMetadata couvre nativement cette stack (BigQuery, Snowflake, S3, Iceberg, Power BI).
- Compte tenu du risque réglementaire (E3), les fonctions de gouvernance (workflows, glossaires, audit) exigent une garantie de service contractuelle. *Alation* et *Collibra* \[R8\] sont retenues à ce titre ; Collibra l'emporte pour son socle de gouvernance prédéfini plus solide.
- Un connecteur officiel documenté OpenMetadata ↔ Collibra synchronise les glossaires et fait correspondre les actifs.

**Qualité** — *Soda Core*, replis Cuallee et/ou TestGen
- *Talend* \[R8\] : suite ETL globale, fonctions qualité non autonomes — redondant avec l'infrastructure ETL déjà existante chez Spotify.
- *Informatica* \[R8\] : écartée pour 3 raisons — fragmentation architecturale imposant une charge de réconciliation au Data Custodian sans bénéfice pour E1 ; compétences requises incompatibles avec le profil Data Steward ; coût opaque et délais (1-2 semestres) disproportionnés au regard du risque des enjeux opérationnels (E2, E5).
- *Ataccama* \[R8\] : plateforme unifiée solide mais coût élevé et opaque, non justifié pour des enjeux opérationnels.
- *Soda Core* (noyau open source de Soda) retenu pour le contrôle courant (E2) et les données d'entraînement (E5) ; connecteurs couvrant l'ensemble des sources \[R2\].
- **Réserve 1** : si les vérifications déclaratives s'avèrent insuffisantes pour les contrôles statistiques ML, repli vers *Cuallee* (bibliothèque spécialisée ML, indépendante du moteur de calcul : Pandas, Snowflake, DuckDB, Spark).
- **Réserve 2** : la feuille de route éditeur s'oriente vers l'offre commerciale *Soda Cloud* — risque de parité fonctionnelle dégradée sur le noyau open source. *TestGen* (génération automatique de tests par profilage) documenté comme repli, sous réserve de vérifier sa maturité d'écosystème.

**Conformité réglementaire** — *TrustArc (RoPA/DPIA/BN/DSAR)*
- *VeraSafe* \[R8\] : cabinet de conseil et services managés, pas une solution logicielle.
- *DataGuard* \[R8\] : plateforme de conformité positionnée PME (DPO/juristes inclus à l'abonnement) — écartée d'office, Spotify n'étant pas à cette échelle.
- *OneTrust* et *TrustArc* \[R8\] : équivalentes au regard des enjeux E3/E4. TrustArc retenue pour : (1) une automatisation multi-juridictionnelle explicite — le point le plus difficile de E3 selon \[D1\] (GDPR, CCPA, PDPA et régimes locaux simultanément) ; (2) une meilleure facilité d'usage et qualité de support pour le DPO, opérateur quotidien.
- \[R11, Q4\] confirme que la couverture DSAR est attendue nativement du dispositif central.

**Sécurisation des données et des accès** — *Wazuh (SIEM) + OpenBao (chiffrement & clés)*
- *DataGuard* reclassée avec les outils de conformité (ce n'est pas un outil de chiffrement/détection).
- *Vormetric* \[R8\] (racheté par Thales) : solution solide mais tarification commerciale classique et licence propriétaire. Écartée au profit d'*OpenBao*, qui propose les mêmes services de gestion des clés sans coût de licence — avec la nuance que son fonctionnement réel est *gestion des clés + chiffrement à l'appel via Transit*, pas un chiffrement transparent automatique.

*Source : \[D3\] §3.C.1-§3.C.5 · Alternatives évaluées : \[R8\]*

---

### B3. Circuit de gouvernance des modèles d'IA — matrices RACI complètes

**Amendement à la politique** \[D21 §2.1.3, P8\] : *« Cette gouvernance est proportionnée au niveau d'impact de chaque modèle sur l'utilisateur et sur l'entreprise, selon les critères et les circuits de validation différenciés définis en section 2.1.5, afin que l'intensité du contrôle ne freine pas disproportionnellement le déploiement des modèles à faible risque. »*

**Critères de classification, avec degré d'automatisation** \[D3 annexe 3.E\] :

| Niveau | Critères | Automatisation |
|---|---|---|
| Fort impact | Portée majorité des utilisateurs actifs | Calculé (métadonnées MLflow) |
| | Exposition art. 22 GDPR | Calculé (lineage OpenMetadata/Collibra) |
| | Décision peu réversible | Déclaratif (Model Owner) |
| | Fonctionnalité principale du produit | Déclaratif (Model Owner) |
| Impact modéré | Portée partielle (cohorte, marché, A/B test) | Calculé |
| | Décision réversible sous délai court | Déclaratif |
| Impact faible | Aucun critère de fort impact rempli | Par défaut |

**RACI — Classification** *(événement unique, à la création du modèle dans le registre)*

| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Classifier un modèle | I | I | – | I | I | I | R | A | – | I |

**RACI — Approbation de déploiement** *(répétée à chaque version, hérite du niveau fixé à la classification)*

| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Fort impact | A | C | I | I | I | I | C | R | C | I |
| Impact modéré | I | C | I | I | I | I | R | A | I | I |
| Impact faible (auto-certification) | – | I | – | I | I | I | RA | I | – | – |

**RACI — Contrôle a posteriori et reclassification** *(événements rares)*

| Activité | DGC | CDO | DPO | DO | DS | DC | MO | MRM | Legal | CEO |
|---|---|---|---|---|---|---|---|---|---|---|
| Contrôle par échantillonnage (impact faible) | I | I | – | I | I | I | I | RA | – | – |
| Reclasser un modèle | I | I | – | I | I | I | C | RA | – | I |

*Sur la ligne « fort impact », le Model Owner est Consulted et le Model Risk Manager Responsible — conforme à la matrice RACI d'origine \[D22, annexe 2.2.C\], qui réserve au MO un rôle de consultation, non d'exécution, sur ce palier. Le nombre de parties prenantes décroît mécaniquement avec le niveau d'impact, rendant la proportionnalité visible dans la matrice elle-même.*

**Distinction structurelle** : la **classification** porte sur le modèle en tant qu'entité conceptuelle (une seule fois, à sa création) ; l'**approbation de déploiement** porte sur une version (répétée à chaque mise en production, héritant du niveau sans le rouvrir) ; la **reclassification** est un événement rare (changement substantiel ou détection en audit). Confondre ces trois activités reviendrait à répéter à chaque cycle de release un coût de classification qui ne devrait être payé qu'une fois.

*Statut* : ces éléments sont proposés comme amendements à \[D21 §2.1.3/§2.1.5\] et comme lignes supplémentaires de la matrice RACI \[D22, annexe 2.2.C\] — leur intégration formelle dans ces deux documents reste à faire séparément.

*Source : \[D3\] annexe 3.E*

---

### B4. Plan pilote — calendrier détaillé des jalons

| Jalon | Semaine | Actions | Porteur |
|---|---|---|---|
| 01 (x) | S1 | Lancement du pilote, confirmation de l'existence d'un annuaire d'entreprise central apte SAML/OIDC | PPM, DC |
| 02 (x) | S1-S3 | Sécurisation des infrastructures préexistantes ; régénération des secrets et collecte des profils du stockage initial | DC |
| 03 (x) | S3-S4 | Vérification directe des capacités SSO et de synchronisation de groupes de TrustArc | DPO, Legal Team |
| 04 (x) | S4-S5 | Vérification du RBAC natif de MLflow, AIF360, AIX360 et Wazuh | DC, MO, MRM |
| 05 (x) | S5-S6 | Test d'intégration bout-en-bout (annuaire → OpenMetadata, Collibra, TrustArc, identifiant AWS dynamique OpenBao) | DC |
| 06 (x) | S7 | Revue de la phase de sécurisation : poursuite ou suspension | PPM, DGC |
| 07.1 | S8-S11 | Déploiement technique (OpenMetadata, DVC, Soda Core, MLflow, AIF360, AIX360, Wazuh, OpenBao) | DC |
| 07.2 | S8-S17 | Population initiale du RoPA (TrustArc) scopée PD | DPO, Legal Team |
| 08.1 | S12 | Vérification du recouvrement Soda Core / module qualité natif OpenMetadata | DC |
| 08.2 | S12 | Population initiale du glossaire Collibra scopée PD | DS |
| 09 | S13 | Vérification du connecteur Collibra-OpenMetadata | DC |
| 10.1 | S14 | Classification initiale du modèle testé | MO, MRM |
| 10.2 | S14-S17 | Exécution en conditions réelles : qualité courante et données d'entraînement, entraînement/évaluation | DS, MO |
| 11 | S16 | Vérification technique intermédiaire (premiers résultats Soda Core) | DS |
| 12 | S17 | Revue intermédiaire (Engineering overhead, adoption des standards) | PPM |
| 13 | S18 | Premier passage du circuit d'approbation (niveau classé au Jalon 10.1) | MRM, DGC selon niveau |
| 14 | S19 | Consolidation des indicateurs, recueil des retours | Toute l'équipe |
| 15 | S20 | Revue de synthèse | PPM |
| 16 | S21 | Revue finale et clôture du pilote | DGC |

**Livrables attendus** \[D3 §3.F.5\] : rapport qualité des données · rapport de validation du circuit de classification/approbation · estimation de l'Engineering overhead (main-d'œuvre uniquement) · note de recouvrement technique (Soda Core/OpenMetadata) · note de synchronisation catalogage (connecteur Collibra) · note de contrôle d'accès (RBAC/SSO, TrustArc à valider spécifiquement) · rapport de migration de sécurisation · rapport de déploiement initial Collibra/RoPA · retours des parties prenantes (DS, MO, DO) · rapport d'évaluation du double rattachement.

*Source : \[D3\] §3.F.4-§3.F.5*

---

### B5. Méthode de mesure des KPIs et du double rattachement

**Méthode de mesure des dimensions DMAT** — la re-cotation porte uniquement sur les sous-questions déjà mappées à chaque dimension \[D1, annexe 1.A\], sur le périmètre pilote uniquement (pas l'ensemble de l'organisation) :

| Dimension | Porteur | Jalon | Instrument de mesure |
|---|---|---|---|
| Data Governance | PPM (auto-évaluation), validation DGC | Jalon 16 | Re-cotation Q1-Q6, Q10-Q13 \[R1\] |
| Data Quality | Data Steward, PPM (consolidation) | Jalon 12 puis 16 | Re-cotation Q36-Q39 \[R1\], journaux Soda Core |
| Analytics & BI (gouvernance IA) | Model Owner, Model Risk Manager | Jalon 12 puis 16 | Re-cotation Q55-Q57 \[R1\], dossier de classification + AIF360/AIX360 |

*Nature de l'exercice* : la re-cotation reste un jugement qualitatif — les niveaux DMAT sont des descriptions textuelles, non des seuils calculables automatiquement. La validation DGC réduit le risque de biais d'auto-évaluation sans rendre le jugement objectif : ce que le pilote améliore, c'est la matière sur laquelle le jugement s'exerce — des artefacts opérationnels produits en direct (logs, horodatages, dossiers) plutôt qu'un texte narratif rédigé a posteriori. Chaque score doit être ancré à une preuve explicitement citée.

**Évaluation du double rattachement des Data Stewards** — le critère retenu pour le passage à l'échelle (absence de conflit d'autorité rapporté) ne mesure que l'absence de dysfonctionnement, pas la valeur produite. Cinq indicateurs complémentaires :

| Indicateur | Méthode de mesure | Source |
|---|---|---|
| Taux d'adoption des standards CDO | Proportion de règles Soda Core taguées « standard CDO » vs « spécifique domaine » | DC |
| Délai de propagation d'une mise à jour | Horodatage du workflow de révision/approbation Collibra | PPM |
| Fréquence de sollicitation fonctionnelle | Comptage des échanges DS → CDO sur les termes/actifs Collibra | DS |
| Cohérence terminologique | Taux de correspondance exacte au glossaire Collibra | DC, DS |
| Autonomie départementale préservée | Part des décisions métier prises sans blocage, registre DO dédié | DO |

Trois de ces cinq indicateurs sont captés nativement par Collibra, sans outil supplémentaire. *Lecture combinée* : le critère négatif (absence de conflit) devient insuffisant seul — un pilote pourrait afficher zéro conflit simplement parce que le canal fonctionnel n'est jamais utilisé, masquant un échec silencieux. L'indicateur d'autonomie sert de garde-fou contre une dérive de centralisation de fait.

*Source : \[D3\] §3.F.6*

---

### B6. Gestion des risques du pilote

**Risques de suspension (sans repli)**

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Absence d'annuaire d'entreprise central apte SAML/OIDC (Jalon 01) | Faible à moyenne | Suspension totale | Devient un chantier d'infrastructure séparé, hors calendrier du pilote |
| Défaut de sécurisation non corrigeable sur l'existant (Jalon 02) | Faible | Suspension si non corrigé avant Jalon 06 | Repli possible si le défaut est circonscrit à un périmètre isolable |

**Risques de débordement de planning**

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Délai de réponse TrustArc (SSO, Jalon 03) | Moyenne | Débordement du Jalon 03 | Gestion manuelle temporaire, documentée comme dérogation |
| Échec du test d'intégration bout-en-bout (Jalon 05) | Moyenne | Débordement du Jalon 06, retard en cascade | Identifier le maillon défaillant avant de corriger |
| Compression de l'exécution réelle (Jalon 10.2, 4 semaines — la plus courte envisagée) | Moyenne | Fiabilité réduite des indicateurs | Rallongement ponctuel si le Jalon 11 s'avère instable |

**Autres risques opérationnels**

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Charge Data Custodians sous-estimée (4 outils sur 10) | Élevée | Élevé | Suivi hebdomadaire ; bascule possible vers l'offre managée Collate |
| Collecte incomplète des profils d'accès (Jalon 02) | Moyenne | Élevé | Recoupement systématique avant redéfinition des droits |
| Soda Core insuffisant pour E5 | Moyenne | Moyen | Vérification Jalon 08.1/11 ; repli Cuallee |
| Dépriorisation long terme de Soda Core | Moyenne | Faible à moyen | Suivi post-pilote ; repli TestGen si confirmé |
| Décalage de synchronisation Collibra/OpenMetadata | Faible | Moyen | Vérification Jalon 09 ; calibrage sur délai de notification 72h |
| Seuils de classification mal calibrés | Moyenne | Moyen | Mesure du délai réel au Jalon 13 ; resserrement si besoin |
| Résistance au changement du département pilote | Moyenne | Moyen | Cf. formation §3.F.9 |
| Désalignement cycles budgétaires trimestriels | Moyenne | Moyen | Anticiper la demande budgétaire Phase 3 avant clôture Phase 2 |
| Déploiement Collibra/RoPA plus long que prévu | Moyenne | Moyen | Prioriser la classification des données les plus sensibles |
| Absence de classification préalable des données du RoPA | Élevée | Moyen | Population du RoPA documentée comme provisoire jusqu'à classification établie |

*Source : \[D3\] §3.F.8*

---

### B7. Conditions de passage à l'échelle (feu vert / orange / rouge)

| Dispositif testé | Critère de passage à l'échelle | Si échec / résultat mitigé |
|---|---|---|
| Double rattachement Data Steward (E1) | Absence de conflit d'autorité rapporté | Clarifier par écrit avant extension, plutôt qu'abandonner |
| Soda Core / module qualité OpenMetadata | Décision explicite au Jalon 08.1 | Généraliser uniquement l'outil retenu |
| Connecteur Collibra/OpenMetadata | Synchronisation vérifiée au Jalon 09, compatible avec délai 72h | Resserrer la fréquence ou évaluer une intégration complémentaire |
| Soda Core pour la qualité des données d'entraînement (E5) | Contrôles jugés suffisants entre Jalons 08.1 et 11 | Bascule vers Cuallee, sans réintroduire Deequ/Spark |
| Circuit de classification et d'approbation (§3.E) | Délai mesuré au Jalon 13, compatible avec le rythme de mise en production | Resserrer les critères de classification plutôt qu'alléger le circuit |
| Déploiement incrémental Collibra/RoPA (E1, E3) | Configuration scopée PD extensible sans reconstruction majeure | Revoir l'architecture avant Phase 3 plutôt que répliquer une structure défaillante |
| Engineering overhead Data Custodians | Estimation (Jalon 12) comparée à la capacité réelle | Séquencer le déploiement sur plusieurs trimestres |
| Phase de sécurisation elle-même | Franchissement du Jalon 06 sans suspension | Traiter comme chantier séparé avant toute généralisation |

*Source : \[D3\] §3.G.1*

---

### B8. Ajustements attendus au cadre de gouvernance

1. Intégration formelle dans \[D21 §2.1.3/§2.1.5\] et \[D22, annexe 2.2.C\] de l'amendement de proportionnalité par niveau d'impact (§3.E), avec calibration finale des seuils selon les résultats du pilote.
2. Révision du tableau d'outils §3.4 sur les deux lignes explicitement testées (recouvrement Soda Core/OpenMetadata, suffisance de Soda Core pour E5) — non définitives avant la fin de la phase 1.
3. Établissement d'un coût total de possession complet (infrastructure, maintenance pluriannuelle), au-delà de l'Engineering overhead mesuré en pilote, une fois un historique d'exploitation suffisant disponible.
4. Validation de la couverture DSAR par TrustArc — exercice séparé, porté par DPO/Legal Team, avant l'ouverture de la Phase 3 (Marketing), en s'appuyant sur le RoPA déjà peuplé en pilote, sous réserve que la classification préalable des données soit établie.
5. Formalisation en procédure documentée et réutilisable de l'extension légère de sécurisation (régénération des secrets, collecte des profils) requise à chaque nouveau département, distincte de la phase de sécurisation complète (Jalons 01-06) qui n'a lieu qu'une fois.

*Source : \[D3\] §3.G.3*

---

### B9. Trajectoire de maturité détaillée

| Échéance | Étape | Niveau de maturité visé | Repère exécutif \[R11, Q7\] |
|---|---|---|---|
| M5 | Pilote clos, décisions go/no-go prises | Niveau 2 sur le périmètre pilote (Data Governance, Data Quality) | Borne haute de la fourchette pilote (3-6 mois) |
| M10 | Product Development couvert dans son ensemble | Niveau 2-3 sur Data Governance et Data Quality, étendu à tout PD | Dans la fenêtre de déploiement (+12-18 mois) |
| M15 | Marketing couvert | Niveau 2-3 sur Compliance et Data Usage & Accessibility | Dans la fenêtre de déploiement |
| M20 | Content Curation couvert, Engineering élargi | Niveau 3 sur Metadata et Master & Reference Data | Approche la borne haute du déploiement complet |
| M22-M24 | Ensemble des départements couverts | Niveau 3 sur l'ensemble des dimensions actuellement en niveau 1 \[D21 §2.1.7\] | Borne haute, au maximum de la fourchette \[R11, Q7\] |

*Cette trajectoire reste indicative : chaque jalon de phase est un point de réévaluation, pas un engagement figé — la feuille de route est elle-même soumise au principe d'amélioration continue qu'elle sert à mettre en œuvre.*

*Source : \[D3\] §3.G.4*

---
## Sources

- \[R1\] Australian Government Data Maturity Assessment Tool (2026)
- \[R2\] Spotify Business Case
- \[R7\] Organizational Models Overview
- \[R8\] Tech Tools Overview
- \[R11\] Executive Q&A Guide
- \[D1\] Data Maturity Assessment Report
- \[D21\] Data Governance Policy Document
- \[D22\] Roles and Responsibilities Organizational Chart
- \[D3\] Implementation Plan, annexes 3.A-3.G
