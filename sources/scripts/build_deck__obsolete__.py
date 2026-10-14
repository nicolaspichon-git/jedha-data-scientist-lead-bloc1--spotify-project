"""
Génère spotify-step-4-presentation.pptx avec python-pptx.
Équivalent Python de build_deck.js (pptxgenjs). Le contenu de chaque slide est
retranscrit directement en structures Python (chaînes, listes, tables) - ce
script n'analyse pas syntaxiquement les fichiers markdown sources. Pour
modifier le texte d'une slide, éditez le bloc `# --- SLIDE N ---` correspondant
puis relancez la génération.

Prérequis : pip install python-pptx Pillow
Lancer d'abord build_icons.py pour générer les icônes utilisées ici.
"""

from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.oxml.ns import qn

# ---------------------------------------------------------------------------
# THEME
# ---------------------------------------------------------------------------
NAVY = "1B2A4A"          # primary dark
NAVY_SOFT = "2A3C60"     # slightly lighter navy for cards on dark bg
LIGHT_BG = "F2F4F7"      # content slide background
WHITE = "FFFFFF"
GREEN = "2DBE8C"         # accent fills
GREEN_TEXT = "1C8C68"    # accent text (contrast-safe)
SLATE = "5B6B84"         # secondary text
SLATE_LT = "8493A8"      # muted captions
TERRA = "B8574A"         # risk / alert fills
TERRA_TEXT = "97402F"    # risk / alert text
LINE_LT = "D8DEE6"       # subtle borders / gridlines
CARD_BG = "FFFFFF"

TITLE_FONT = "Cambria"
BODY_FONT = "Calibri"

PAGE_W = 13.333
PAGE_H = 7.5
TOTAL_SLIDES = 10


def ICON(name):
    return f"icons/{name}.png"


prs = Presentation()
prs.slide_width = Inches(PAGE_W)
prs.slide_height = Inches(PAGE_H)
BLANK_LAYOUT = prs.slide_layouts[6]

# ---------------------------------------------------------------------------
# LOW-LEVEL HELPERS
# ---------------------------------------------------------------------------

def C(hex_str):
    return RGBColor.from_string(hex_str)


def zero_margins(tf):
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Emu(0)


def set_char_spacing(run, pt_value):
    rPr = run._r.get_or_add_rPr()
    rPr.set("spc", str(int(pt_value * 100)))


def set_bullet(paragraph, char="\u2022", indent_in=0.2):
    pPr = paragraph._p.get_or_add_pPr()
    marL = Inches(indent_in)
    pPr.set("marL", str(marL))
    pPr.set("indent", str(-marL))
    buFont = etree.SubElement(pPr, qn("a:buFont"))
    buFont.set("typeface", "Arial")
    buChar = etree.SubElement(pPr, qn("a:buChar"))
    buChar.set("char", char)


def strip_shadow(shape):
    """Ensure a shape has NO shadow at all. Setting shadow.inherit=False and an
    empty <a:effectLst/> is not always enough in LibreOffice's renderer while
    the shape still carries a <p:style> effectRef to the theme; removing that
    style block entirely is the reliable fix (fill/line are already set
    explicitly on every shape here, so removing it doesn't change colors)."""
    shape.shadow.inherit = False
    spPr = shape._element.spPr
    if spPr.find(qn("a:effectLst")) is None:
        etree.SubElement(spPr, qn("a:effectLst"))
    style = shape._element.find(qn("p:style"))
    if style is not None:
        shape._element.remove(style)


def add_shadow(shape, color=NAVY, alpha=12000, blur=63500, dist=19050, direction=5400000):
    spPr = shape._element.spPr
    effectLst = spPr.find(qn("a:effectLst"))
    if effectLst is None:
        effectLst = etree.SubElement(spPr, qn("a:effectLst"))
    outerShdw = etree.SubElement(effectLst, qn("a:outerShdw"))
    outerShdw.set("blurRad", str(blur))
    outerShdw.set("dist", str(dist))
    outerShdw.set("dir", str(direction))
    outerShdw.set("rotWithShape", "0")
    clr = etree.SubElement(outerShdw, qn("a:srgbClr"))
    clr.set("val", color)
    a = etree.SubElement(clr, qn("a:alpha"))
    a.set("val", str(alpha))
    style = shape._element.find(qn("p:style"))
    if style is not None:
        shape._element.remove(style)


# ---------------------------------------------------------------------------
# SLIDE-BUILDING HELPERS
# ---------------------------------------------------------------------------

def new_slide(bg_hex):
    slide = prs.slides.add_slide(BLANK_LAYOUT)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(bg_hex)
    return slide


def add_text(slide, text, x, y, w, h, *, font=BODY_FONT, size=12, bold=False,
             italic=False, color=NAVY, align=None, valign=None,
             line_spacing=None, char_spacing=None):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    zero_margins(tf)
    if valign is not None:
        tf.vertical_anchor = valign
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if align is not None:
            p.alignment = align
        if line_spacing is not None:
            p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = C(color)
        if char_spacing is not None:
            set_char_spacing(run, char_spacing)
    return box


def add_bullets(slide, items, x, y, w, h, *, font=BODY_FONT, size=12,
                 color=NAVY, space_after=10, valign=None, bold=False):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    zero_margins(tf)
    if valign is not None:
        tf.vertical_anchor = valign
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after if i < len(items) - 1 else 0)
        set_bullet(p)
        run = p.add_run()
        run.text = item
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = C(color)
    return box


def add_card(slide, x, y, w, h, *, fill=CARD_BG, line_color=LINE_LT, shadow=True):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = 0.08
    shp.fill.solid()
    shp.fill.fore_color.rgb = C(fill)
    strip_shadow(shp)
    if line_color:
        shp.line.color.rgb = C(line_color)
        shp.line.width = Pt(0.75)
    else:
        shp.line.fill.background()
    if shadow:
        add_shadow(shp)
    return shp


def add_badge(slide, text, x, y, d, *, fill=GREEN, text_color=NAVY, font_size=13):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    shp.fill.solid()
    shp.fill.fore_color.rgb = C(fill)
    shp.line.fill.background()
    strip_shadow(shp)
    add_text(slide, text, x, y, d, d, font=BODY_FONT, size=font_size, bold=True,
              color=text_color, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    return shp


def add_header(slide, kicker, title, icon_path=None, dark=False, title_w=11.4):
    k_color = GREEN if dark else GREEN_TEXT
    t_color = WHITE if dark else NAVY
    add_text(slide, kicker.upper(), 0.6, 0.42, 8, 0.32, font=BODY_FONT, size=12,
              bold=True, color=k_color, char_spacing=2)
    add_text(slide, title, 0.6, 0.72, title_w, 0.95, font=TITLE_FONT, size=28,
              bold=True, color=t_color, valign=MSO_ANCHOR.TOP, line_spacing=1.02)
    if icon_path:
        slide.shapes.add_picture(icon_path, Inches(PAGE_W - 1.15), Inches(0.4), Inches(0.72), Inches(0.72))


def add_footer(slide, page_num, source_text=None, dark=False):
    c = "9FB0C9" if dark else SLATE_LT
    if source_text:
        add_text(slide, source_text, 0.6, PAGE_H - 0.42, 9.5, 0.3, font=BODY_FONT,
                  size=9.5, italic=True, color=c)
    add_text(slide, f"{page_num} / {TOTAL_SLIDES}", PAGE_W - 1.3, PAGE_H - 0.42, 0.9, 0.3,
              font=BODY_FONT, size=9.5, color=c, align=PP_ALIGN.RIGHT)


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def style_cell(cell, text, *, size=11, bold=False, color=NAVY, fill=None, align=PP_ALIGN.LEFT):
    if fill:
        cell.fill.solid()
        cell.fill.fore_color.rgb = C(fill)
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.margin_left = Inches(0.12)
    cell.margin_right = Inches(0.12)
    cell.margin_top = Inches(0.05)
    cell.margin_bottom = Inches(0.05)
    tf = cell.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = BODY_FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = C(color)


# ===========================================================================
# SLIDE 1 - TITRE
# ===========================================================================
s = new_slide(NAVY)

add_text(s, "SPOTIFY - DATA & AI GOVERNANCE PROJECT", 0.7, 0.75, 9, 0.35,
          font=BODY_FONT, size=13, bold=True, color=GREEN, char_spacing=2)

add_text(s, "Gouvernance des Données et de l'Intelligence Artificielle", 0.7, 1.55, 9.3, 1.7,
          font=TITLE_FONT, size=40, bold=True, color=WHITE, line_spacing=1.05)

add_text(s, "Cadre, organisation et plan de mise en œuvre - Présentation au Comité Exécutif et au Leadership IA",
          0.7, 3.15, 8.6, 0.7, font=BODY_FONT, size=17, italic=True, color="CADCFC")

stats = [
    ("450M+", "utilisateurs actifs"),
    ("200M", "abonnés premium"),
    ("180+", "pays d'opération"),
]
stat_y, stat_w, gap = 4.55, 2.6, 0.35
for i, (num, label) in enumerate(stats):
    x = 0.7 + i * (stat_w + gap)
    add_text(s, num, x, stat_y, stat_w, 0.75, font=TITLE_FONT, size=34, bold=True, color=GREEN)
    add_text(s, label, x, stat_y + 0.72, stat_w, 0.4, font=BODY_FONT, size=12.5, color="CADCFC")

add_text(s, "Nicolas Pichon - AIA RNCP 38777 - BC01 - Step 4 - v2 - 2026/10/13",
          0.7, PAGE_H - 0.55, 8, 0.3, font=BODY_FONT, size=10.5, color="9FB0C9")
add_text(s, "1 / 10", PAGE_W - 1.3, PAGE_H - 0.55, 0.9, 0.3, font=BODY_FONT, size=10.5,
          color="9FB0C9", align=PP_ALIGN.RIGHT)

add_notes(s,
    "Introduction : Spotify opere a l'echelle mondiale (450M+ utilisateurs, 180+ pays) avec une "
    "dependance forte aux donnees (recommandation, personnalisation, monetisation). Le projet "
    "presente aujourd'hui repond a une demande de cadrage transverse : gouvernance des donnees ET de l'IA, "
    "pas seulement conformite. Objectif de la session : validation du cadre, de l'organisation cible, "
    "et du plan de deploiement propose (pilote puis generalisation)."
)

# ===========================================================================
# SLIDE 2 - DIAGNOSTIC DE MATURITE
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Diagnostic", "Une maturité data en phase initiale, un potentiel analytique déjà avancé",
            icon_path=ICON("icon_barchart"), title_w=10.4)

categories = [
    "Analytics & BI", "Intégration", "Métadonnées", "Master & Reference Data",
    "Littératie data", "Sécurité", "Usage & Accessibilité", "Conformité",
    "Opérations", "Architecture", "Qualité", "Gouvernance",
]
values = [2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1]

chart_data = CategoryChartData()
chart_data.categories = categories
chart_data.add_series("Niveau de maturité", values)
gframe = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.55), Inches(1.85),
                              Inches(7.6), Inches(4.9), chart_data)
chart = gframe.chart
chart.has_legend = False
chart.has_title = True
chart.chart_title.text_frame.text = "Niveau de maturité par dimension (échelle 0-5)"
ttl_run = chart.chart_title.text_frame.paragraphs[0].runs[0]
ttl_run.font.size = Pt(12)
ttl_run.font.bold = True
ttl_run.font.name = BODY_FONT
ttl_run.font.color.rgb = C(NAVY)

plot = chart.plots[0]
plot.gap_width = 35
plot.has_data_labels = True
dls = plot.data_labels
dls.number_format = "0"
dls.number_format_is_linked = False
dls.font.size = Pt(10)
dls.font.name = BODY_FONT
dls.font.color.rgb = C(NAVY)

series = plot.series[0]
for i, v in enumerate(values):
    pt = series.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = C(GREEN if v >= 2 else "A9B6C9")

val_axis = chart.value_axis
val_axis.minimum_scale = 0
val_axis.maximum_scale = 5
val_axis.major_unit = 1
val_axis.has_major_gridlines = True
val_axis.major_gridlines.format.line.color.rgb = C(LINE_LT)
val_axis.format.line.color.rgb = C(LINE_LT)
val_axis.tick_labels.font.size = Pt(9.5)
val_axis.tick_labels.font.color.rgb = C(SLATE)

cat_axis = chart.category_axis
cat_axis.has_major_gridlines = False
cat_axis.format.line.color.rgb = C(LINE_LT)
cat_axis.tick_labels.font.size = Pt(10.5)
cat_axis.tick_labels.font.color.rgb = C(NAVY)
cat_axis.tick_labels.font.name = BODY_FONT

add_card(s, 8.45, 1.85, 4.3, 1.55)
add_text(s, "1,25 / 5", 8.7, 1.98, 3.8, 0.7, font=TITLE_FONT, size=30, bold=True, color=NAVY)
add_text(s, "Niveau moyen de maturité actuel - gouvernance locale, réactive, dispersée",
          8.7, 2.68, 3.85, 0.6, font=BODY_FONT, size=11.5, color=SLATE)

add_card(s, 8.45, 3.55, 4.3, 1.35, fill="EAF7F1")
add_text(s, "Cible à moyen terme : niveau 3", 8.7, 3.68, 3.85, 0.4, font=BODY_FONT,
          size=14, bold=True, color=GREEN_TEXT)
add_text(s, "Gouvernance bien définie et globale, portée par la politique de gouvernance",
          8.7, 4.08, 3.85, 0.65, font=BODY_FONT, size=11, color=SLATE)

add_card(s, 8.45, 5.05, 4.3, 1.7, fill=WHITE)
add_text(s, "Un cadre est défini (rôles, outils identifiés) mais pas encore déployé : "
              "ni audit, ni monitoring, ni politique appliquée sur le terrain.",
          8.7, 5.2, 3.85, 1.4, font=BODY_FONT, size=11.5, color=NAVY, italic=True, valign=MSO_ANCHOR.TOP)

add_footer(s, 2, "Source : [D1] Data & AI Maturity Assessment Report - Méthodologie [R1] Australian Government DMAT")

add_notes(s,
    "12 dimensions evaluees selon la methodologie DMAT [R1], appliquee au business case Spotify [R2]. "
    "Niveau moyen ~1,25 sur 5. Points d'appui a 2 : usage/accessibilite, litteratie data, analytics & BI "
    "(le moteur de recommandation est deja en production). Le reste (gouvernance, qualite, securite, "
    "conformite, architecture, operations, metadonnees, integration, master data) reste au niveau 1 : "
    "initiatives locales, non generalisees, non mesurees. Message cle pour le comite : l'entreprise sait deja "
    "produire de la valeur avec la donnee, le risque est dans la gouvernance de cette capacite, pas dans la capacite elle-meme."
)

# ===========================================================================
# SLIDE 3 - 6 ENJEUX MAJEURS
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Enjeux", "Six enjeux majeurs, par ordre de criticité",
            icon_path=ICON("icon_alert"), title_w=10.4)

enjeux = [
    ("E1", "Décompartimenter les données", "Silos départementaux \u2192 vues incohérentes ou incomplètes, angles morts décisionnels."),
    ("E2", "Maîtriser la qualité des données", "Données et métadonnées inexactes : recommandations dégradées, règles de qualité à définir."),
    ("E3", "Conformité multi-juridictionnelle", "GDPR, CCPA, PDPA + réglementations IA à concilier sans perdre en cohérence globale."),
    ("E4", "Vie privée & usage éthique", "Transparence, contrôle utilisateur, anonymisation - au-delà de la seule conformité légale."),
    ("E5", "Gouverner les données IA", "Traçabilité, biais, responsabilité des modèles du moteur de recommandation en production."),
    ("E6", "Monter en compétences data", "Culture de gouvernance partagée encore à construire ; risque de résistance au changement."),
]

cols, card_w, card_h, gap_x, gap_y = 2, 5.85, 1.5, 0.35, 0.28
start_x, start_y = 0.6, 1.85
for i, (code, label, desc) in enumerate(enjeux):
    col, row = i % cols, i // cols
    x = start_x + col * (card_w + gap_x)
    y = start_y + row * (card_h + gap_y)
    add_card(s, x, y, card_w, card_h)
    add_badge(s, code, x + 0.22, y + 0.22, 0.62, fill=TERRA, text_color=WHITE, font_size=14)
    add_text(s, label, x + 1.0, y + 0.16, card_w - 1.2, 0.42, font=BODY_FONT, size=14.5, bold=True, color=NAVY)
    add_text(s, desc, x + 1.0, y + 0.58, card_w - 1.2, 0.85, font=BODY_FONT, size=11, color=SLATE, valign=MSO_ANCHOR.TOP)

add_footer(s, 3, "Source : [D1] §1.2 - enjeux dérivés de [R2], à l'exception de E5")

add_notes(s,
    "Ordre de criticite justifie dans [D1]. E5 (gouvernance IA) est le seul enjeu qui n'est pas deja nomme "
    "comme tel dans le business case [R2] : c'est un gap identifie par le diagnostic, pas une demande initiale "
    "de Spotify. Le modele organisationnel choisi a la slide suivante repond specifiquement a E1 et E6 ; "
    "la politique de gouvernance repond a E2, E3, E4, E5."
)

# ===========================================================================
# SLIDE 4 - 9 PRINCIPES
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Politique de gouvernance", "Neuf principes structurent le cadre de gouvernance",
            icon_path=ICON("icon_shield"), title_w=10.6)

clusters = [
    ("Responsabilité & qualité", [
        ("P1", "Responsabilité - un responsable identifié par actif de données et par modèle"),
        ("P4", "Qualité - règles mesurables (exactitude, complétude, fraîcheur), auditées régulièrement"),
    ]),
    ("Confiance utilisateur", [
        ("P2", "Transparence - information claire et gestion du consentement"),
        ("P6", "Minimisation - collecte limitée aux finalités métier"),
        ("P7", "Droits des utilisateurs - accès, modification, suppression, opposition"),
    ]),
    ("Sécurité & conformité", [
        ("P3", "Sécurité - chiffrement, contrôle d'accès par rôle, protocoles PCI-DSS"),
        ("P5", "Conformité - GDPR, CCPA, PCI-DSS et réglementations locales, veille continue"),
    ]),
    ("IA responsable & amélioration continue", [
        ("P8", "Éthique & gouvernance IA - traçabilité, biais, explicabilité"),
        ("P9", "Amélioration continue - revues périodiques alignées sur la méthodologie DMAT"),
    ]),
]

card_w, card_h, gap_x, gap_y, start_x, start_y = 5.85, 2.35, 0.35, 0.25, 0.6, 1.8
for i, (title, items) in enumerate(clusters):
    col, row = i % 2, i // 2
    x = start_x + col * (card_w + gap_x)
    y = start_y + row * (card_h + gap_y)
    add_card(s, x, y, card_w, card_h)
    add_text(s, title, x + 0.3, y + 0.18, card_w - 0.6, 0.36, font=BODY_FONT, size=14, bold=True, color=GREEN_TEXT)
    ty = y + 0.62
    for code, text in items:
        add_badge(s, code, x + 0.3, ty, 0.42, fill=NAVY, text_color=WHITE, font_size=10.5)
        add_text(s, text, x + 0.85, ty - 0.03, card_w - 1.15, 0.62, font=BODY_FONT, size=10.8,
                  color=NAVY, valign=MSO_ANCHOR.TOP)
        ty += 0.62

add_footer(s, 4, "Source : [D21] §2.1.3 - principes issus de [R4]")

add_notes(s,
    "Les 9 principes viennent du referentiel fourni [R4] et sont reprises telles quelles dans la politique "
    "[D21]. Point notable pour le comite : P8 (ethique & gouvernance IA) est le principe le plus operationnalise "
    "dans le document -- il donne lieu a 4 exigences concretes (tracabilite, biais, responsabilite/approbation "
    "proportionnee, explicabilite), detaillees a la slide Gouvernance IA."
)

# ===========================================================================
# SLIDE 5 - ORGANISATION (Center of Excellence)
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Organisation", "Un modèle Center of Excellence, adapté à Spotify",
            icon_path=ICON("icon_users"), title_w=10.4)

left_x, left_w = 0.6, 4.5
add_card(s, left_x, 1.85, left_w, 5.0, fill=WHITE)
ly = 2.1
left_blocks = [
    ("Le modèle", "Gouvernance centralisée (CDO, DGC) combinée à une autonomie départementale (Data Owners par métier)."),
    ("Deux écarts assumés", "Infrastructure technique maintenue dans Engineering ; autorité de conformité (DPO/Legal) séparée de l'autorité de gouvernance (CDO/DGC)."),
    ("Le mécanisme clé", "Double rattachement des Data Stewards - fonctionnel au CDO, organisationnel au département - principal levier contre le cloisonnement (E1)."),
]
for h, t in left_blocks:
    add_text(s, h, left_x + 0.3, ly, left_w - 0.6, 0.32, font=BODY_FONT, size=13, bold=True, color=GREEN_TEXT)
    add_text(s, t, left_x + 0.3, ly + 0.36, left_w - 0.6, 1.15, font=BODY_FONT, size=11.5, color=NAVY, valign=MSO_ANCHOR.TOP)
    ly += 1.62

img_x, img_w = 5.35, 7.4
img_h = img_w / (1419 / 864)
s.shapes.add_picture("assets/spotify-step-2-2-organizational-chart--diagram.png",
                      Inches(img_x), Inches(1.85), Inches(img_w), Inches(img_h))
add_text(s, "Trait plein = rattachement hiérarchique - Trait pointillé = rattachement fonctionnel / transverse",
          img_x, 1.85 + img_h + 0.08, img_w, 0.35, font=BODY_FONT, size=10, italic=True,
          color=SLATE_LT, align=PP_ALIGN.CENTER)

add_footer(s, 5, "Source : [D22] Roles and Responsibilities Organizational Chart")

add_notes(s,
    "CDO, DPO et Legal Team rapportent au CEO (independance DPO exigee par le GDPR art. 38 par. 3). "
    "Le DGC est preside par le CDO. Le Model Risk Manager rapporte au CDO au quotidien mais peut escalader "
    "directement au DGC -- ce qui preserve son independance vis-a-vis des equipes dont il evalue les modeles. "
    "Les Data Custodians sont centralises dans Engineering mais servent tous les departements transversalement. "
    "Les Model Owners sont dans Product Development, separes du Model Risk Manager (separation execution / controle)."
)

# ===========================================================================
# SLIDE 6 - CONFORMITE REGLEMENTAIRE
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Conformité", "Un socle réglementaire structuré cadre par cadre",
            icon_path=ICON("icon_lock"), title_w=10.4)

reg_cols = [
    ("GDPR", [
        "Traitement licite, loyal et transparent",
        "Droits d'accès, rectification, suppression",
        "Consentement explicite préalable",
        "Notification de violation sous 72h",
        "Data Protection Officer nommé",
    ]),
    ("CCPA", [
        "Opt-out sur la vente de données",
        "Droit d'accès, modification, suppression",
        "Non-discrimination envers les utilisateurs exerçant leurs droits",
    ]),
    ("PCI-DSS", [
        "Sécurisation de l'infrastructure réseau",
        "Chiffrement des données de carte bancaire",
        "Gestion des vulnérabilités",
        "Contrôle d'accès strict aux données de paiement",
        "Tests réguliers des dispositifs de sécurité",
    ]),
]

card_w, card_h, gap_x, start_x, start_y = 3.95, 4.05, 0.24, 0.6, 1.85
for i, (name, items) in enumerate(reg_cols):
    x = start_x + i * (card_w + gap_x)
    add_card(s, x, start_y, card_w, card_h)
    header_shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x + 0.3), Inches(start_y + 0.25),
                                      Inches(card_w - 0.6), Inches(0.5))
    header_shp.adjustments[0] = 0.06
    header_shp.fill.solid()
    header_shp.fill.fore_color.rgb = C(NAVY)
    header_shp.line.fill.background()
    strip_shadow(header_shp)
    add_text(s, name, x + 0.3, start_y + 0.25, card_w - 0.6, 0.5, font=BODY_FONT, size=16,
              bold=True, color=WHITE, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
    add_bullets(s, items, x + 0.3, start_y + 0.95, card_w - 0.6, card_h - 1.2,
                 font=BODY_FONT, size=11.5, color=NAVY, space_after=10, valign=MSO_ANCHOR.TOP)

add_card(s, 0.6, 6.05, 12.13, 0.72, fill="EAF7F1", shadow=False)
add_text(s, "Complété par une cartographie réglementaire marché par marché (PDPA à Singapour, etc.), "
              "pilotée par Legal Team en lien avec le DPO.",
          0.9, 6.05, 11.5, 0.72, font=BODY_FONT, size=12, bold=True, color=GREEN_TEXT, valign=MSO_ANCHOR.MIDDLE)

add_footer(s, 6, "Source : [D21] §2.1.4 - Référentiel [R5]")

add_notes(s,
    "Les trois cadres sont traites separement dans la politique [D21], chacun avec ses propres exigences "
    "operationnelles issues de la checklist de conformite [R5]. La difficulte specifique de Spotify est la "
    "dimension multi-juridictionnelle (enjeu E3) : au-dela du socle GDPR/CCPA/PCI-DSS, chaque marche local "
    "(ex. PDPA a Singapour) doit etre cartographie separement, sous la responsabilite conjointe de Legal Team et du DPO."
)

# ===========================================================================
# SLIDE 7 - GOUVERNANCE DE L'IA
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Gouvernance de l'IA", "Une responsabilité proportionnée au niveau d'impact du modèle",
            icon_path=ICON("icon_cpu"), title_w=10.6)

reqs = [
    ("Traçabilité", "Chaque jeu d'entraînement documenté : source, période, transformations, lineage."),
    ("Biais", "Évaluation périodique des biais algorithmiques pour les modèles à fort impact."),
    ("Approbation", "Responsabilité confiée à un Model Owner ; circuit proportionné au niveau d'impact."),
    ("Explicabilité", "Décisions automatisées à impact significatif explicables de manière intelligible."),
]
r_w, r_h, gap, start_x, start_y = 2.9, 1.15, 0.22, 0.6, 1.95
for i, (h, t) in enumerate(reqs):
    x = start_x + i * (r_w + gap)
    add_card(s, x, start_y, r_w, r_h)
    add_text(s, h, x + 0.2, start_y + 0.12, r_w - 0.4, 0.3, font=BODY_FONT, size=12.5, bold=True, color=GREEN_TEXT)
    add_text(s, t, x + 0.2, start_y + 0.44, r_w - 0.4, 0.65, font=BODY_FONT, size=9.8, color=NAVY, valign=MSO_ANCHOR.TOP)

table_y = 3.45
col_widths = [1.5, 6.83, 3.8]
row_heights = [0.5, 0.85, 0.85, 0.85]
gframe = s.shapes.add_table(4, 3, Inches(0.6), Inches(table_y),
                              Inches(sum(col_widths)), Inches(sum(row_heights)))
tbl = gframe.table
tbl.first_row = False
tbl.horz_banding = False
for i, w in enumerate(col_widths):
    tbl.columns[i].width = Inches(w)
for i, h in enumerate(row_heights):
    tbl.rows[i].height = Inches(h)

headers = ["Niveau d'impact", "Critères (extraits)", "Circuit de validation"]
for c, htext in enumerate(headers):
    style_cell(tbl.cell(0, c), htext, size=12.5, bold=True, color=WHITE, fill=NAVY,
               align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

impact_rows = [
    ("Fort", "Majorité des utilisateurs actifs - décision peu réversible - art. 22 GDPR - fonctionnalité principale",
     "MO (C) \u2192 MRM (R) \u2192 DGC (A)", TERRA, "FBEDEA"),
    ("Modéré", "Utilisateurs ciblés (cohorte, marché, A/B test) - décision réversible sous délai court",
     "MO (R) \u2192 MRM (A)", "C99A3C", "FBF3E2"),
    ("Faible", "Fonction auxiliaire, sans exposition directe à l'utilisateur final",
     "MO (RA) - contrôle a posteriori par MRM (échantillonnage)", GREEN_TEXT, "EAF7F1"),
]
for r, (level, crit, circuit, badge_color, row_fill) in enumerate(impact_rows, start=1):
    style_cell(tbl.cell(r, 0), level, size=12, bold=True, color=badge_color, fill=row_fill, align=PP_ALIGN.CENTER)
    style_cell(tbl.cell(r, 1), crit, size=11, color=NAVY, fill=row_fill, align=PP_ALIGN.LEFT)
    style_cell(tbl.cell(r, 2), circuit, size=11, bold=True, color=NAVY, fill=row_fill, align=PP_ALIGN.LEFT)

add_text(s, "MO = Model Owner - MRM = Model Risk Manager - DGC = Data Governance Committee - "
              "R = Responsible, A = Accountable, C = Consulted",
          0.6, table_y + 3.15, 12.13, 0.35, font=BODY_FONT, size=9.5, italic=True, color=SLATE_LT)

add_footer(s, 7, "Source : [D21] §2.1.5")

add_notes(s,
    "La proportionnalite du circuit d'approbation est le point cle a defendre devant le comite : elle evite "
    "qu'un circuit concu pour les modeles a fort impact ne devienne un frein systematique au deploiement des "
    "modeles a impact modere ou faible. Le DGC est Accountable sur l'approbation des modeles a fort impact, "
    "alors que le CDO -- qui preside le DGC -- n'est que Consulted sur cette decision : c'est volontaire, pour "
    "eviter que le CDO soit juge et partie sur ses propres arbitrages IA. Le calibrage final des seuils sera "
    "affine avec les resultats du pilote [D3]."
)

# ===========================================================================
# SLIDE 8 - MISE EN OEUVRE : OUTILLAGE & PILOTE
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Mise en œuvre", "Un outillage ciblé, testé sur un pilote de 21 semaines",
            icon_path=ICON("icon_tool"), title_w=10.6)

left_x, left_w = 0.6, 6.3
add_text(s, "Outillage par catégorie", left_x, 1.75, left_w, 0.35, font=BODY_FONT, size=14, bold=True, color=NAVY)
tools = [
    ("Catalogage", "Collibra - OpenMetadata", "E1"),
    ("Qualité", "Soda Core", "E2, E5"),
    ("Conformité", "TrustArc", "E3, E4"),
    ("Sécurité", "Wazuh - OpenBao", "P3"),
    ("Gouvernance IA", "MLflow - DVC - AIF360 - AIX360", "E5"),
]
ty = 2.2
row_h = 0.86
for cat, names, enjeu in tools:
    add_card(s, left_x, ty, left_w, row_h - 0.1)
    add_badge(s, enjeu, left_x + 0.18, ty + (row_h - 0.1) / 2 - 0.24, 0.48, fill=GREEN, text_color=NAVY, font_size=9.5)
    add_text(s, cat, left_x + 0.85, ty + 0.08, left_w - 1.1, 0.3, font=BODY_FONT, size=12.5, bold=True, color=NAVY)
    add_text(s, names, left_x + 0.85, ty + 0.38, left_w - 1.1, 0.32, font=BODY_FONT, size=11, color=SLATE)
    ty += row_h

right_x, right_w = 7.2, 5.55
add_text(s, "Pilote - système de recommandation", right_x, 1.75, right_w, 0.35, font=BODY_FONT, size=14, bold=True, color=NAVY)

add_card(s, right_x, 2.2, right_w, 1.1, fill="EAF7F1")
add_text(s, "21 semaines (~5 mois)", right_x + 0.25, 2.32, right_w - 0.5, 0.45, font=TITLE_FONT, size=20, bold=True, color=GREEN_TEXT)
add_text(s, "dont 7 semaines de phase de sécurisation bloquante (annuaire central, migration des accès)",
          right_x + 0.25, 2.78, right_w - 0.5, 0.48, font=BODY_FONT, size=10.5, color=SLATE)

add_card(s, right_x, 3.45, right_w, 1.3)
add_text(s, "Périmètre", right_x + 0.25, 3.58, right_w - 0.5, 0.3, font=BODY_FONT, size=12, bold=True, color=NAVY)
add_text(s, "Modèles et données d'entraînement du système de recommandation - département Product Development",
          right_x + 0.25, 3.9, right_w - 0.5, 0.8, font=BODY_FONT, size=11, color=SLATE, valign=MSO_ANCHOR.TOP)

add_card(s, right_x, 4.9, right_w, 1.3)
add_text(s, "Indicateurs clés (DMAT)", right_x + 0.25, 5.03, right_w - 0.5, 0.3, font=BODY_FONT, size=12, bold=True, color=NAVY)
add_text(s, "Gouvernance & Qualité : niveau 1 \u2192 2 - Gouvernance IA (Analytics & BI) : niveau 2 \u2192 3",
          right_x + 0.25, 5.35, right_w - 0.5, 0.8, font=BODY_FONT, size=11, color=SLATE, valign=MSO_ANCHOR.TOP)

add_card(s, right_x, 6.35, right_w, 0.68, fill="FBEDEA", shadow=False)
add_text(s, "Risques clés : suspension sans repli (absence d'annuaire central) - débordement de planning",
          right_x + 0.22, 6.35, right_w - 0.44, 0.68, font=BODY_FONT, size=10.2, bold=True,
          color=TERRA_TEXT, valign=MSO_ANCHOR.MIDDLE)

add_footer(s, 8, "Source : [D3] §3.4 (outils) - §3.5 (plan pilote)")

add_notes(s,
    "Chaque outil repond a un role precis du modele CoE et a un enjeu identifie en [D1]. La selection resulte "
    "d'une comparaison entre les outils recommandes [R8] et des alternatives open source (retenues sur la "
    "majorite des lignes, sauf Collibra et TrustArc). Le pilote est volontairement resserre sur un seul "
    "sous-perimetre (systeme de recommandation) pour valider le rattachement fonctionnel des Data Stewards, "
    "le circuit d'approbation des modeles, et le cout reel d'ingenierie avant generalisation. La conformite "
    "GDPR complete (E3/E4) reste hors perimetre du pilote : un RoPA scope a un seul departement ne vaut pas "
    "conformite article 30."
)

# ===========================================================================
# SLIDE 9 - FEUILLE DE ROUTE DE GENERALISATION
# ===========================================================================
s = new_slide(LIGHT_BG)
add_header(s, "Feuille de route", "Une généralisation en quatre phases, jusqu'au niveau 3",
            icon_path=ICON("icon_map"), title_w=10.6)

phases = [
    ("Phase 1 - Pilote", "Product Development\n(entraînement recommandation)", "21 semaines", "M5"),
    ("Phase 2", "Product Development\n(reste des activités)", "3 mois", "M10"),
    ("Phase 3", "Marketing\n(E1 / E3 / E4)", "3 mois", "M15"),
    ("Phase 4", "Content Curation\n(E2 / métadonnées)", "3 mois", "M20"),
    ("Consolidation", "Ensemble des départements\nNiveau 3 généralisé", "-", "M22-M24"),
]

margin_x = 0.6
content_w = PAGE_W - 2 * margin_x
col_w = content_w / len(phases)
line_y = 4.15
node_d = 0.32

line_shp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(margin_x + col_w / 2), Inches(line_y - 0.015),
                                Inches(content_w - col_w), Inches(0.03))
line_shp.fill.solid()
line_shp.fill.fore_color.rgb = C(LINE_LT)
line_shp.line.fill.background()
strip_shadow(line_shp)

for i, (label, scope, duration, month) in enumerate(phases):
    cx = margin_x + col_w * i + col_w / 2
    card_w = col_w - 0.28
    card_x = cx - card_w / 2
    is_last = i == len(phases) - 1

    add_card(s, card_x, 1.85, card_w, 1.95, fill="EAF7F1" if is_last else WHITE)
    add_text(s, label, card_x + 0.15, 2.0, card_w - 0.3, 0.35, font=BODY_FONT, size=12.5, bold=True,
              color=GREEN_TEXT if is_last else NAVY)
    add_text(s, scope, card_x + 0.15, 2.38, card_w - 0.3, 0.95, font=BODY_FONT, size=10, color=SLATE, valign=MSO_ANCHOR.TOP)
    add_text(s, duration, card_x + 0.15, 3.38, card_w - 0.3, 0.35, font=BODY_FONT, size=10.5, italic=True, bold=True, color=NAVY)

    node = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - node_d / 2), Inches(line_y - node_d / 2),
                                Inches(node_d), Inches(node_d))
    node.fill.solid()
    node.fill.fore_color.rgb = C(GREEN if is_last else NAVY)
    node.line.color.rgb = C(WHITE)
    node.line.width = Pt(2)
    strip_shadow(node)

    add_text(s, month, cx - col_w / 2 + 0.14, line_y + 0.22, col_w - 0.28, 0.35, font=BODY_FONT,
              size=13, bold=True, color=GREEN_TEXT, align=PP_ALIGN.CENTER)

add_card(s, 0.6, 4.95, content_w, 0.95, fill="F7F8FA", shadow=False)
add_text(s, "Trajectoire de maturité : niveau 1 (actuel) \u2192 niveau 3 généralisé (M22-M24). "
              "Ce séquencement atteint la borne haute de la fourchette de référence (15-24 mois) - "
              "un compromis assumé pour garantir la rigueur de la phase de sécurisation initiale.",
          0.9, 4.95, content_w - 0.6, 0.95, font=BODY_FONT, size=11.5, color=NAVY, valign=MSO_ANCHOR.MIDDLE)

add_card(s, 0.6, 6.05, content_w, 0.72, fill=WHITE)
add_text(s, "Chaque jalon de phase est un point de réévaluation (feu vert / orange / rouge), pas un "
              "engagement figé - conformément au principe d'amélioration continue (P9).",
          0.9, 6.05, content_w - 0.6, 0.72, font=BODY_FONT, size=10.5, italic=True, color=SLATE, valign=MSO_ANCHOR.MIDDLE)

add_footer(s, 9, "Source : [D3] §3.6")

add_notes(s,
    "Le sequencement suit le niveau de risque et le cout marginal : Marketing en priorite pour E3/E4 "
    "(risque reglementaire le plus eleve), puis Content Curation pour E2/metadonnees. La phase de securisation "
    "(annuaire central, roles OpenBao, integrations SSO) ne se reproduit pas integralement aux phases suivantes : "
    "seule une migration allegee est reconduite par departement. Message pour le comite : la duree totale (22-24 mois) "
    "est deliberement prudente, pas un retard -- elle finance la rigueur de la phase 1."
)

# ===========================================================================
# SLIDE 10 - VALEUR & PROCHAINES ETAPES
# ===========================================================================
s = new_slide(NAVY)
add_header(s, "Valeur & prochaines étapes", "Une gouvernance qui protège la confiance et soutient la croissance",
            icon_path=ICON("icon_flag"), dark=True, title_w=10.6)

pillars = [
    ("icon_check_white", "Économies", "Réduction des inefficiences liées à une donnée de mauvaise qualité"),
    ("icon_lock", "Conformité", "Éviter les sanctions GDPR/CCPA (jusqu'à 4% du CA mondial)"),
    ("icon_shield", "Confiance", "Transparence et sécurité renforcées auprès des utilisateurs"),
    ("icon_globe", "Scalabilité", "Infrastructure de gouvernance prête pour la croissance mondiale"),
]
p_w, p_gap, start_x, p_y = 2.85, 0.28, 0.6, 1.95
for i, (icon, label, desc) in enumerate(pillars):
    x = start_x + i * (p_w + p_gap)
    s.shapes.add_picture(ICON(icon), Inches(x + (p_w - 0.7) / 2), Inches(p_y), Inches(0.7), Inches(0.7))
    add_text(s, label, x, p_y + 0.85, p_w, 0.35, font=BODY_FONT, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, desc, x, p_y + 1.2, p_w, 1.0, font=BODY_FONT, size=10.5, color="CADCFC",
              align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.TOP)

box_shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(4.55), Inches(12.13), Inches(2.05))
box_shp.adjustments[0] = 0.08
box_shp.fill.solid()
box_shp.fill.fore_color.rgb = C(NAVY_SOFT)
box_shp.line.color.rgb = C("3A4C72")
box_shp.line.width = Pt(1)
strip_shadow(box_shp)

add_text(s, "Prochaines étapes", 0.95, 4.72, 6, 0.35, font=BODY_FONT, size=14, bold=True, color=GREEN)
steps = [
    "Lancer le pilote sur le système de recommandation (Product Development)",
    "Nommer / confirmer DPO, CDO, Data Stewards et Model Owners",
    "Première revue de maturité DMAT au jalon intermédiaire (M5)",
    "Décision de passage à l'échelle (feu vert / orange / rouge) à chaque jalon de phase",
]
add_bullets(s, steps, 0.95, 5.12, 11.4, 1.35, font=BODY_FONT, size=12.5, color=WHITE, space_after=8, valign=MSO_ANCHOR.TOP)

add_text(s, "Nicolas Pichon - AIA RNCP 38777 - BC01 - Step 4 - v2 - 2026/10/13",
          0.6, PAGE_H - 0.42, 8, 0.3, font=BODY_FONT, size=9.5, color="9FB0C9")
add_text(s, "10 / 10", PAGE_W - 1.3, PAGE_H - 0.42, 0.9, 0.3, font=BODY_FONT, size=9.5,
          color="9FB0C9", align=PP_ALIGN.RIGHT)

add_notes(s,
    "Synthese de la valeur business [R11, Q3] : economies, conformite, confiance, scalabilite. Les prochaines "
    "etapes sont volontairement concretes et actionnables des la sortie de cette reunion : lancement du pilote, "
    "nomination des roles, premiere revue de maturite a M5, et gouvernance des decisions de passage a l'echelle "
    "phase par phase plutot qu'un engagement global fige sur 24 mois."
)

# ---------------------------------------------------------------------------
prs.save("spotify-step-4-presentation.pptx")
print("Deck written.")
