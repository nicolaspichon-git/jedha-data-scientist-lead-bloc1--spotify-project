*SPOTIFY'S DATA & AI GOVERNANCE* PROJECT
===

# 2.2. *Organizational Roles & Responsibilities* Chart

> *Nicolas Pichon - AIA RNCP 38777 / BC01  / Step 2.2 / v13 - 2026/10/13.*

---

L'organigramme ci-dessous s'appuie sur les rôles pré-définis dans \[R6\] (*CDO*, *DPO*, *DGC*, *DS*) et sur les rôles manquants identifiés dans \[D1\] (*Data Owner*, *Data Custodian*, *Model Owner*, *Model Risk Manager*).

![Organigramme de gouvernance des données et de l'IA chez Spotify](aia-spotify/step-2/spotify-step-2-2-organizational-chart--diagram.png)

> *Convention : trait plein = rattachement hiérarchique, trait pointillé = rattachement fonctionnel, d'escalade, ou relation transverse.*

> (\*) *HoE* est *DO* des données d'infrastructure et de fonctionnement que le département produit et comprend en propre : journaux d'accès, journaux applicatifs, télémétrie, métriques d'infrastructure, journaux d'audit de sécurité.

<div style="page-break-after: always; page-break-inside: avoid;"></div>

*CDO*, *DPO* et *Legal Team* rapportent directement au *CEO*. Le rattachement du *CDO* au *CEO* reprend la tendance dominante des organisations *data-driven*, celui du *DPO* répond à une exigence légale d'indépendance (RGPD, art. 38§3), et celui de *Legal Team* s'inspire d'une pratique qui permet d'éviter que l'ensemble de la fonction juridique soit subordonné au seul mandat de la protection des données.

*Data Governance Committee* (DGC) est présidé par *CDO* et lui rapporte directement.

Le*Model Risk Manager* rapporte au *CDO* pour les affaires courantes, et au *DGC*, en *escalade directe*, pour certaines décisions. La possibilité de s'adresser directement au *DGC* permet de préserver l'indépendance du *MRM* dans sa fonction de contrôle, sans la faire dépendre des entités dont elle évalue les modèles.

Les *Data Stewards* ont un double rattachement : fonctionnel au *CDO* (standards, méthodologie, qualité) et organisationnel au département dans lequel ils sont intégrés. Ce mécanisme contribue à ouvrir les silos de données identifiés dans \[R2\] en alignant les départements sur le standard commun porté par *CDO*, tout en leur permettant de conserver la responsabilité des données de métier.

Les *Data Custodians*, du fait de leur fonction technique (garde, sécurité, sauvegarde de l'infrastructure), sont intégrés dans le département *Engineering*, d'où ils servent transversalement l'ensemble des domaines métiers (y compris *Engineering*) en exécutant les décisions d'accès et de sécurité de chaque *Data Owner*.

Les *Model Owners* sont intégrés dans le département *Product Development*, l'entité décisionnelle où sont développés les produits *data-driven* (moteur de recommandation, etc.). Conformément à la pratique du *model risk management*, la fonction de *Model Owners* (au plus près de la production des modèles) est séparée de celle de *Model Risk Manager* (qui les contrôle).

---
## Sources
- \[R2\] Spotify Business Case
- \[R6\] Data Governance Roles Template
- \[D1\] *Data Maturity Assessment Report*
