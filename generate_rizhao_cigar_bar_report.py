"""
Rizhao Cigar Bar Feasibility Report — Consulting-grade PDF generator.

Style references: McKinsey / BCG / Bain reports. Layout features include
a branded cover page, a table of contents, color-coded section dividers,
structured frameworks (PESTEL, Porter's Five Forces, SWOT), financial
projection tables, an implementation roadmap, and page headers/footers.
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.platypus.flowables import HRFlowable

# ---------------------------------------------------------------------------
# Brand palette (deep navy + gold accents — typical top-tier consulting feel)
# ---------------------------------------------------------------------------
NAVY = colors.HexColor('#0B1E3F')
NAVY_LIGHT = colors.HexColor('#1F3A66')
GOLD = colors.HexColor('#B8862B')
GOLD_LIGHT = colors.HexColor('#E8C77A')
GREY_DARK = colors.HexColor('#2E2E2E')
GREY_MID = colors.HexColor('#6B6B6B')
GREY_LIGHT = colors.HexColor('#EFEFEF')
WHITE = colors.white

# ---------------------------------------------------------------------------
# Fonts — register both regular and bold Chinese-capable faces
# ---------------------------------------------------------------------------
pdfmetrics.registerFont(TTFont('CN', r'C:\Windows\Fonts\simsun.ttc'))
pdfmetrics.registerFont(TTFont('CN-Bold', r'C:\Windows\Fonts\simhei.ttf'))

# ---------------------------------------------------------------------------
# Paragraph styles
# ---------------------------------------------------------------------------
styles = getSampleStyleSheet()

cover_title = ParagraphStyle(
    'CoverTitle', fontName='CN-Bold', fontSize=34, leading=44,
    textColor=WHITE, alignment=TA_LEFT, spaceAfter=10)
cover_subtitle = ParagraphStyle(
    'CoverSubtitle', fontName='CN', fontSize=16, leading=24,
    textColor=GOLD_LIGHT, alignment=TA_LEFT, spaceAfter=6)
cover_meta = ParagraphStyle(
    'CoverMeta', fontName='CN', fontSize=10, leading=16,
    textColor=WHITE, alignment=TA_LEFT)
cover_tag = ParagraphStyle(
    'CoverTag', fontName='CN-Bold', fontSize=11, leading=16,
    textColor=GOLD, alignment=TA_LEFT, spaceAfter=4)

chapter_num = ParagraphStyle(
    'ChapterNum', fontName='CN-Bold', fontSize=72, leading=80,
    textColor=GOLD, alignment=TA_LEFT)
chapter_title = ParagraphStyle(
    'ChapterTitle', fontName='CN-Bold', fontSize=26, leading=34,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=10)
chapter_kicker = ParagraphStyle(
    'ChapterKicker', fontName='CN', fontSize=11, leading=18,
    textColor=GREY_MID, alignment=TA_LEFT)

h1 = ParagraphStyle(
    'H1', fontName='CN-Bold', fontSize=18, leading=24,
    textColor=NAVY, alignment=TA_LEFT, spaceBefore=18, spaceAfter=10)
h2 = ParagraphStyle(
    'H2', fontName='CN-Bold', fontSize=13, leading=18,
    textColor=NAVY_LIGHT, alignment=TA_LEFT, spaceBefore=12, spaceAfter=6)
h3 = ParagraphStyle(
    'H3', fontName='CN-Bold', fontSize=11, leading=16,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=8, spaceAfter=4)

body = ParagraphStyle(
    'Body', fontName='CN', fontSize=10.5, leading=18,
    textColor=GREY_DARK, alignment=TA_JUSTIFY, spaceAfter=8, firstLineIndent=0)
body_bullet = ParagraphStyle(
    'BodyBullet', fontName='CN', fontSize=10.5, leading=17,
    textColor=GREY_DARK, alignment=TA_LEFT, leftIndent=14, spaceAfter=4,
    bulletIndent=2)
caption = ParagraphStyle(
    'Caption', fontName='CN', fontSize=9, leading=13,
    textColor=GREY_MID, alignment=TA_LEFT, spaceAfter=6)
quote = ParagraphStyle(
    'Quote', fontName='CN', fontSize=11.5, leading=20,
    textColor=NAVY, alignment=TA_LEFT, leftIndent=14, rightIndent=14,
    spaceBefore=8, spaceAfter=10, borderPadding=10)
toc_entry = ParagraphStyle(
    'TocEntry', fontName='CN', fontSize=11, leading=22,
    textColor=GREY_DARK, alignment=TA_LEFT)
toc_num = ParagraphStyle(
    'TocNum', fontName='CN-Bold', fontSize=11, leading=22,
    textColor=GOLD, alignment=TA_LEFT)

# Helper styles for table-cell paragraphs
cell_body = ParagraphStyle(
    'CellBody', fontName='CN', fontSize=9.5, leading=14,
    textColor=GREY_DARK, alignment=TA_LEFT)
cell_header = ParagraphStyle(
    'CellHeader', fontName='CN-Bold', fontSize=10, leading=14,
    textColor=WHITE, alignment=TA_CENTER)
cell_center = ParagraphStyle(
    'CellCenter', fontName='CN', fontSize=9.5, leading=14,
    textColor=GREY_DARK, alignment=TA_CENTER)
cell_tag = ParagraphStyle(
    'CellTag', fontName='CN-Bold', fontSize=10, leading=14,
    textColor=NAVY, alignment=TA_LEFT)


# ---------------------------------------------------------------------------
# Page templates — cover, section divider, body
# ---------------------------------------------------------------------------
PAGE_W, PAGE_H = A4


def draw_cover_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Gold diagonal accent
    canvas.setFillColor(GOLD)
    p = canvas.beginPath()
    p.moveTo(0, PAGE_H * 0.30)
    p.lineTo(PAGE_W * 0.55, PAGE_H * 0.18)
    p.lineTo(PAGE_W * 0.55, PAGE_H * 0.22)
    p.lineTo(0, PAGE_H * 0.34)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    # Thin gold divider near top
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(2)
    canvas.line(2 * cm, PAGE_H - 2.5 * cm, 8 * cm, PAGE_H - 2.5 * cm)
    # Brand mark
    canvas.setFillColor(GOLD)
    canvas.setFont('CN-Bold', 11)
    canvas.drawString(2 * cm, PAGE_H - 2.1 * cm, 'EAST COAST ADVISORY  |  东海岸战略咨询')
    # Footer mark
    canvas.setFillColor(WHITE)
    canvas.setFont('CN', 8)
    canvas.drawString(2 * cm, 1.5 * cm, 'CONFIDENTIAL  |  机密文件  |  仅供项目方内部使用')
    canvas.drawRightString(PAGE_W - 2 * cm, 1.5 * cm, '2026 · 山东日照')
    canvas.restoreState()


def draw_body_page(canvas, doc):
    canvas.saveState()
    # Top header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 1.2 * cm, PAGE_W, 1.2 * cm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 1.25 * cm, PAGE_W, 0.05 * cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont('CN-Bold', 9)
    canvas.drawString(2 * cm, PAGE_H - 0.8 * cm, '山东日照雪茄吧 · 可行性研究报告')
    canvas.setFont('CN', 8)
    canvas.setFillColor(GOLD_LIGHT)
    canvas.drawRightString(PAGE_W - 2 * cm, PAGE_H - 0.8 * cm,
                           'EAST COAST ADVISORY')
    # Footer
    canvas.setStrokeColor(GREY_LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, 1.5 * cm, PAGE_W - 2 * cm, 1.5 * cm)
    canvas.setFillColor(GREY_MID)
    canvas.setFont('CN', 8)
    canvas.drawString(2 * cm, 1.0 * cm, '© 2026 East Coast Advisory · 机密')
    canvas.drawCentredString(PAGE_W / 2, 1.0 * cm,
                             '日照雪茄吧 · 可行性研究')
    canvas.drawRightString(PAGE_W - 2 * cm, 1.0 * cm, f'第 {doc.page} 页')
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def section_divider(number: str, title_cn: str, title_en: str, kicker: str):
    """Build a chapter divider page with big numeral + title."""
    flow = []
    flow.append(Spacer(1, 4 * cm))
    flow.append(Paragraph(number, chapter_num))
    flow.append(HRFlowable(width=4 * cm, thickness=2, color=GOLD,
                           spaceBefore=4, spaceAfter=14))
    flow.append(Paragraph(title_cn, chapter_title))
    flow.append(Paragraph(title_en, ParagraphStyle(
        'EnTitle', fontName='CN', fontSize=12, leading=16,
        textColor=GREY_MID, alignment=TA_LEFT, spaceAfter=18)))
    flow.append(Paragraph(kicker, chapter_kicker))
    flow.append(PageBreak())
    return flow


def themed_table(data, col_widths, header=True, zebra=True):
    """Build a table styled with the brand palette."""
    t = Table(data, colWidths=col_widths, hAlign='LEFT')
    style = [
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, GREY_LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.6, NAVY_LIGHT),
    ]
    if header:
        style += [
            ('BACKGROUND', (0, 0), (-1, 0), NAVY),
            ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
            ('FONTNAME', (0, 0), (-1, 0), 'CN-Bold'),
            ('LINEBELOW', (0, 0), (-1, 0), 1.2, GOLD),
        ]
    if zebra:
        for row in range(1, len(data)):
            if row % 2 == 0:
                style.append(('BACKGROUND', (0, row), (-1, row), GREY_LIGHT))
    t.setStyle(TableStyle(style))
    return t


def kpi_strip(items):
    """Three or four KPI cards in a row (label + big number + caption)."""
    cells = []
    for label, number, sub in items:
        block = [
            Paragraph(label, ParagraphStyle(
                'KpiLabel', fontName='CN', fontSize=9, leading=12,
                textColor=GOLD, alignment=TA_LEFT)),
            Spacer(1, 4),
            Paragraph(number, ParagraphStyle(
                'KpiNum', fontName='CN-Bold', fontSize=22, leading=26,
                textColor=NAVY, alignment=TA_LEFT)),
            Spacer(1, 2),
            Paragraph(sub, ParagraphStyle(
                'KpiSub', fontName='CN', fontSize=8.5, leading=12,
                textColor=GREY_MID, alignment=TA_LEFT)),
        ]
        cells.append(block)
    n = len(items)
    col_w = (PAGE_W - 4 * cm) / n
    t = Table([cells], colWidths=[col_w] * n)
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, -1), GREY_LIGHT),
        ('LINEBEFORE', (0, 0), (0, -1), 3, GOLD),
        ('LINEBEFORE', (1, 0), (1, -1), 3, GOLD),
        ('LINEBEFORE', (2, 0), (2, -1), 3, GOLD),
    ] + ([('LINEBEFORE', (3, 0), (3, -1), 3, GOLD)] if n == 4 else [])))
    return t


def callout(text):
    """Highlighted callout box."""
    p = Paragraph(text, ParagraphStyle(
        'Callout', fontName='CN-Bold', fontSize=11, leading=18,
        textColor=NAVY, alignment=TA_LEFT))
    t = Table([[p]], colWidths=[PAGE_W - 4 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), GOLD_LIGHT),
        ('LINEBEFORE', (0, 0), (0, -1), 4, GOLD),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    return t


def bullets(items):
    return [Paragraph(f'• {x}', body_bullet) for x in items]


# ---------------------------------------------------------------------------
# Build the document
# ---------------------------------------------------------------------------
content = []

# ----- COVER -----
content.append(Spacer(1, 6.5 * cm))
content.append(Paragraph('STRATEGIC FEASIBILITY STUDY', cover_tag))
content.append(Paragraph('山东日照<br/>高端雪茄吧<br/>可行性研究报告', cover_title))
content.append(Spacer(1, 0.6 * cm))
content.append(Paragraph('Rizhao Premium Cigar Lounge — Market Entry & Operating Blueprint',
                         cover_subtitle))
content.append(Spacer(1, 5 * cm))
content.append(Paragraph('客户：项目方（保密）<br/>'
                         '出具方：East Coast Advisory · 东海岸战略咨询<br/>'
                         '出具日期：2026 年 5 月<br/>'
                         '版本：V1.0  ·  保密等级：内部',
                         cover_meta))
content.append(PageBreak())

# ----- DISCLAIMER -----
content.append(Spacer(1, 2 * cm))
content.append(Paragraph('重要声明', h1))
content.append(HRFlowable(width=4 * cm, thickness=2, color=GOLD,
                          spaceAfter=12))
content.append(Paragraph(
    '本报告基于公开信息、行业基准数据与项目方提供的初步意向资料编制，'
    '所引用的人口、经济、客流与消费数据来源于政府公报、行业研究与公开渠道，'
    '已尽合理努力进行交叉验证。报告中的财务测算与情景分析为基于假设的指示性结果，'
    '不构成任何投资承诺或回报保证。', body))
content.append(Paragraph(
    '本报告仅供项目方内部决策参考，未经书面授权不得向第三方披露、复制或传播。'
    '雪茄、烟草及酒类经营涉及《烟草专卖法》等监管要求，'
    '项目方在实际推进前，应与当地烟草专卖、市场监管、消防及住建部门就相关许可、'
    '场所标准与控烟规定进行专项确认。', body))
content.append(Spacer(1, 1 * cm))
content.append(callout(
    '"在合规边界内，把高端社交体验做深、把会员关系做厚——'
    '这是日照雪茄吧从开店到立足的核心命题。"'))
content.append(PageBreak())

# ----- TABLE OF CONTENTS -----
content.append(Spacer(1, 1.5 * cm))
content.append(Paragraph('目录  /  CONTENTS', h1))
content.append(HRFlowable(width=4 * cm, thickness=2, color=GOLD,
                          spaceAfter=18))

toc = [
    ('00', '执行摘要', 'Executive Summary'),
    ('01', '宏观环境与城市画像（PESTEL）', 'Macro & City Profile'),
    ('02', '消费市场与目标客群', 'Demand & Customer Segmentation'),
    ('03', '行业格局与竞争分析（五力）', 'Industry & Competitive Landscape'),
    ('04', 'SWOT 与战略定位', 'SWOT & Strategic Positioning'),
    ('05', '产品与体验设计', 'Product & Experience Design'),
    ('06', '选址策略与空间规划', 'Location & Space Strategy'),
    ('07', '运营模式与组织架构', 'Operating Model & Organization'),
    ('08', '营销与会员增长', 'Marketing & Membership Growth'),
    ('09', '财务测算与回报情景', 'Financials & Return Scenarios'),
    ('10', '风险矩阵与合规要点', 'Risk & Compliance'),
    ('11', '实施路线图', 'Implementation Roadmap'),
    ('12', '结论与下一步建议', 'Conclusion & Next Steps'),
]
toc_rows = []
for num, cn, en in toc:
    line = Table(
        [[Paragraph(num, toc_num),
          Paragraph(cn, toc_entry),
          Paragraph(en, ParagraphStyle(
              'TocEn', fontName='CN', fontSize=9, leading=22,
              textColor=GREY_MID, alignment=TA_RIGHT))]],
        colWidths=[1.6 * cm, 9.5 * cm, 5.9 * cm])
    line.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, GREY_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    toc_rows.append(line)
for row in toc_rows:
    content.append(row)
content.append(PageBreak())

# ===========================================================================
# 00 EXECUTIVE SUMMARY
# ===========================================================================
content += section_divider(
    '00', '执行摘要', 'EXECUTIVE SUMMARY',
    '本章浓缩全报告核心结论：市场机会、战略定位、关键经济指标与立项建议。')

content.append(Paragraph('核心判断', h1))
content.append(Paragraph(
    '我们认为，日照具备落地 1 家定位清晰、面向城市高净值客群与高端商务出行客的'
    '雪茄吧的市场基础。城市供给端尚无专业品类玩家，而需求端正经历从"酒桌社交"'
    '向"私享体验式社交"的迁移。建议以"会员制 + 私密体验 + 海岸场景"三重差异化'
    '作为竞争护城河，避免与传统酒吧、酒店大堂吧正面竞争。', body))

content.append(Spacer(1, 0.4 * cm))
content.append(kpi_strip([
    ('TARGET CITY  ·  目标城市', '日照', '常住人口约 320 万 · GDP 约 3,400 亿'),
    ('GAP  ·  品类空白', '0 → 1', '本地暂无成规模专业雪茄吧'),
    ('PAYBACK  ·  投资回收', '24–32 月', '基础情景 IRR 约 18–22%'),
    ('TAM  ·  目标客群', '~3.2 万人', '高净值家庭 + 商务高频出行客'),
]))

content.append(Spacer(1, 0.4 * cm))
content.append(Paragraph('五大关键结论', h1))
content.append(Paragraph(
    '<b>1. 供给侧空白</b>：日照核心商圈与酒店配套层尚无独立、专业的雪茄吧业态，'
    '存在明显品类卡位机会。', body))
content.append(Paragraph(
    '<b>2. 需求结构升级</b>：港口物流、能源化工、海洋经济与文旅四大板块支撑'
    '本地高净值客群扩张，叠加每年逾千万游客中的中高端商务与度假人群，'
    '形成"本地稳定客 + 外地高频客"的复合客源结构。', body))
content.append(Paragraph(
    '<b>3. 差异化定位窗口</b>：以"东方海岸 · 私享品鉴"为核心叙事，'
    '同时承接商务社交与文化体验诉求，可与现有酒吧、KTV、餐厅明显区隔。', body))
content.append(Paragraph(
    '<b>4. 财务可行</b>：在基础情景假设下（月均营收 75 万元、综合毛利 58%），'
    '24–32 个月可实现现金回收，第 3 年净利率有望达到 15–20%。', body))
content.append(Paragraph(
    '<b>5. 关键风险可控</b>：合规许可、雪茄存储、会员粘性是三大核心风险，'
    '通过提前合规预审、专业雪茄房（Walk-in Humidor）建设与系统化会员运营即可有效管控。', body))

content.append(Spacer(1, 0.4 * cm))
content.append(callout(
    '建议：立项推进。优先在 6 个月内完成选址锁定、合规预审与品牌识别建设；'
    '12 个月内实现试营业，18 个月内沉淀核心会员 300+ 人。'))
content.append(PageBreak())

# ===========================================================================
# 01 PESTEL
# ===========================================================================
content += section_divider(
    '01', '宏观环境与城市画像', 'MACRO & CITY PROFILE',
    '采用 PESTEL 框架，对日照宏观环境进行结构化扫描，识别项目可利用的趋势与约束。')

content.append(Paragraph('1.1 城市基本面', h1))
content.append(Paragraph(
    '日照位于山东东南沿海，是国家"一带一路"重要节点城市与北方大宗商品集散地。'
    '城市具备四大结构性优势：① 港口物流（日照港吞吐量稳居全国前列）、'
    '② 海洋与文旅（"阳光海岸"品牌深入人心）、③ 钢铁与化工产业链聚集、'
    '④ 与青岛、临沂半小时高铁圈形成的鲁南都市带。这些产业与区位优势'
    '直接派生出对中高端商务社交场景的稳定需求。', body))

content.append(Paragraph('1.2 PESTEL 框架扫描', h1))
pestel_data = [
    [Paragraph('维度', cell_header),
     Paragraph('关键观察', cell_header),
     Paragraph('对项目的含义', cell_header)],
    [Paragraph('Political<br/>政策', cell_tag),
     Paragraph('烟草专卖严管控；地方对高端文旅与"夜经济"持鼓励态度；'
               '控烟条例对室内吸烟场所有专项要求。', cell_body),
     Paragraph('需以"专卖零售 + 合规品鉴空间"模式立项，'
               '提前与烟草、消防、住建、卫健联合预审。', cell_body)],
    [Paragraph('Economic<br/>经济', cell_tag),
     Paragraph('GDP 稳定增长，人均可支配收入与高净值家庭数同步上行；'
               '港口物流与新能源链条带动企业主层级扩张。', cell_body),
     Paragraph('支撑高客单价业态，目标客单价 600–1,200 元具备承接能力。', cell_body)],
    [Paragraph('Social<br/>社会', cell_tag),
     Paragraph('社交模式从"大桌酒局"向"小圈层私享"迁移；'
               '40+ 男性与新锐企业主对雪茄认知与接受度提升。', cell_body),
     Paragraph('"私密 + 圈层 + 仪式感"是体验设计的核心关键词。', cell_body)],
    [Paragraph('Technological<br/>技术', cell_tag),
     Paragraph('智能温湿度控制、会员 SCRM、内容化营销工具成熟；'
               '小红书/抖音种草成本仍处可控区间。', cell_body),
     Paragraph('以技术降低运营复杂度（雪茄房自动化、会员数字化）。', cell_body)],
    [Paragraph('Environmental<br/>环境', cell_tag),
     Paragraph('海洋气候湿度大，对雪茄存储构成挑战；'
               '场地排烟与新风系统投入需要重点预算。', cell_body),
     Paragraph('CapEx 中应单列雪茄房与新风系统，约占总投资 12–18%。', cell_body)],
    [Paragraph('Legal<br/>法律', cell_tag),
     Paragraph('需办理烟草零售许可证、酒类经营备案、餐饮服务许可、'
               '营业执照及消防备案；广告法对烟草宣传严控。', cell_body),
     Paragraph('品牌传播聚焦"生活方式"叙事，'
               '严守不在公开渠道宣传具体烟草产品的红线。', cell_body)],
]
content.append(themed_table(pestel_data,
                            [2.6 * cm, 7.4 * cm, 7.0 * cm]))
content.append(Paragraph('表 1.1 · 日照雪茄吧项目 PESTEL 扫描', caption))
content.append(PageBreak())

# ===========================================================================
# 02 DEMAND
# ===========================================================================
content += section_divider(
    '02', '消费市场与目标客群', 'DEMAND & SEGMENTATION',
    '从城市消费力、客群分层与画像三个维度刻画需求侧，识别核心与扩展客群。')

content.append(Paragraph('2.1 客群分层与潜力测算（指示性）', h1))
seg_data = [
    [Paragraph('细分客群', cell_header),
     Paragraph('画像', cell_header),
     Paragraph('估算规模', cell_header),
     Paragraph('优先级', cell_header)],
    [Paragraph('本地企业主与高管', cell_tag),
     Paragraph('港口、化工、能源、钢铁、文旅产业主，'
               '40–55 岁、人脉密集、商务社交频次高。', cell_body),
     Paragraph('约 1.2 万人', cell_center),
     Paragraph('★★★★★', cell_center)],
    [Paragraph('外地高频商务访客', cell_tag),
     Paragraph('每年因港口贸易、新能源、会展商务停留日照的外地中高管，'
               '住高端酒店、回头率高。', cell_body),
     Paragraph('月均 4–6 千人次', cell_center),
     Paragraph('★★★★☆', cell_center)],
    [Paragraph('高端文旅度假客', cell_tag),
     Paragraph('面向京津冀与长三角的中高端度假人群，'
               '夏秋旺季集中爆发。', cell_body),
     Paragraph('旺季 8–12 万人次', cell_center),
     Paragraph('★★★☆☆', cell_center)],
    [Paragraph('新中产男性与圈层青年', cell_tag),
     Paragraph('30–40 岁本地新中产，注重体验与社交分享，'
               '对雪茄文化处于"入门—进阶"阶段。', cell_body),
     Paragraph('约 1.8 万人', cell_center),
     Paragraph('★★★☆☆', cell_center)],
    [Paragraph('女性与跨界客群', cell_tag),
     Paragraph('受品质生活方式吸引的女性消费者与艺文圈层，'
               '雪茄消费以"轻雪茄 + 鸡尾酒"组合为主。', cell_body),
     Paragraph('增量待培育', cell_center),
     Paragraph('★★☆☆☆', cell_center)],
]
content.append(themed_table(seg_data,
                            [3.6 * cm, 7.4 * cm, 3.0 * cm, 3.0 * cm]))
content.append(Paragraph('表 2.1 · 目标客群分层与优先级（指示性估算）', caption))

content.append(Paragraph('2.2 消费场景与价值主张', h1))
content.append(Paragraph(
    '基于客群画像，我们识别出四类高价值消费场景，每类场景对应不同的产品组合'
    '与定价策略，是后续 SKU 与排期设计的依据：', body))
for x in bullets([
    '<b>商务谈判与款待</b>：私密包厢 + 顶级雪茄 + 威士忌，客单 1,500–3,000 元。',
    '<b>圈层定期聚会</b>：会员主场，月度品鉴沙龙、嘉宾分享，客单 600–900 元。',
    '<b>仪式性时刻</b>：生日、签约、晋升等纪念场景，'
    '雪茄定制礼盒 + 私人服务，客单 2,000+ 元。',
    '<b>度假体验</b>：旺季外地客的"海岸 + 雪茄"主题体验，客单 500–800 元。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 03 PORTER FIVE FORCES
# ===========================================================================
content += section_divider(
    '03', '行业格局与竞争分析', 'INDUSTRY & COMPETITIVE LANDSCAPE',
    '采用波特五力模型评估行业吸引力，并对潜在直接、间接竞争进行盘点。')

content.append(Paragraph('3.1 波特五力评估', h1))
five_forces = [
    [Paragraph('维度', cell_header),
     Paragraph('强度', cell_header),
     Paragraph('核心判断', cell_header)],
    [Paragraph('既有竞争对手', cell_tag),
     Paragraph('低', cell_center),
     Paragraph('日照尚无成规模专业雪茄吧，主要替代为酒店大堂吧、清吧与会所。', cell_body)],
    [Paragraph('潜在新进入者', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('烟草许可与雪茄供应链构成中等壁垒；'
               '本地资本与外部连锁品牌（如上海/成都）存在进入可能。', cell_body)],
    [Paragraph('替代品威胁', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('威士忌吧、清酒吧、私人会所、KTV 都是注意力替代品；'
               '差异化需要靠"品类专业 + 私享体验"建立。', cell_body)],
    [Paragraph('供应商议价能力', cell_tag),
     Paragraph('中—高', cell_center),
     Paragraph('古巴优质雪茄供应受配额与流通限制；'
               '建议同时绑定 2–3 家头部代理商与免税渠道，分散风险。', cell_body)],
    [Paragraph('客户议价能力', cell_tag),
     Paragraph('低—中', cell_center),
     Paragraph('高净值客户对价格敏感度低，但对体验高度挑剔；'
               '通过会员制与服务标准锁定粘性。', cell_body)],
]
content.append(themed_table(five_forces,
                            [3.4 * cm, 2.4 * cm, 11.2 * cm]))
content.append(Paragraph('表 3.1 · 行业五力扫描（综合吸引力：中—高）', caption))

content.append(Paragraph('3.2 竞争盘点与卡位逻辑', h1))
content.append(Paragraph(
    '日照现有的"类似业态"主要分为三类：高端酒店配套酒吧（依附型，专业度有限）、'
    '城市清吧与音乐酒吧（社交属性强、雪茄专业度弱）、私人会所（封闭、不对外）。'
    '这一格局意味着新项目可在"专业 + 半开放 + 圈层运营"的中间位置建立稀缺性。', body))
content.append(callout(
    '战略锚点：做日照"第一家有专业 Walk-in Humidor、'
    '能调配国际烈酒、并以会员制运营圈层活动的雪茄吧"。'))
content.append(PageBreak())

# ===========================================================================
# 04 SWOT
# ===========================================================================
content += section_divider(
    '04', 'SWOT 与战略定位', 'SWOT & STRATEGIC POSITIONING',
    '在外部环境与内部资源的交叉视角下，明确战略锚点与差异化路径。')

content.append(Paragraph('4.1 SWOT 矩阵', h1))
swot_data = [
    [Paragraph('S · 优势', cell_header),
     Paragraph('W · 劣势', cell_header)],
    [Paragraph(
        '• 品类先发：本地无专业雪茄吧<br/>'
        '• 海岸城市稀缺感与品牌叙事<br/>'
        '• 商务客流稳定 + 文旅客流补充<br/>'
        '• 客单价承接能力强', cell_body),
     Paragraph(
        '• 本地雪茄消费认知尚处培育期<br/>'
        '• 优质雪茄供应链距离远、周期长<br/>'
        '• 海洋气候对存储与装修是挑战<br/>'
        '• 高端服务团队招聘半径有限', cell_body)],
    [Paragraph('O · 机会', cell_header),
     Paragraph('T · 威胁', cell_header)],
    [Paragraph(
        '• 高端社交场景升级与小圈层化<br/>'
        '• 文旅消费升级与体验经济<br/>'
        '• 与酒店、私募、4S 店、艺廊跨界合作<br/>'
        '• 通过内容化营销低成本建立心智', cell_body),
     Paragraph(
        '• 烟草监管趋严、控烟政策升级<br/>'
        '• 经济波动对高端可选消费有放大效应<br/>'
        '• 外部连锁品牌可能跨城进入<br/>'
        '• 仿盘竞品出现导致价格战', cell_body)],
]
content.append(themed_table(swot_data,
                            [8.5 * cm, 8.5 * cm], header=False, zebra=False))
# Manually re-style SWOT (alternating headers)
content[-1].setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('BOX', (0, 0), (-1, -1), 0.6, NAVY_LIGHT),
    ('BACKGROUND', (0, 0), (0, 0), NAVY),
    ('BACKGROUND', (1, 0), (1, 0), GOLD),
    ('BACKGROUND', (0, 2), (0, 2), GOLD),
    ('BACKGROUND', (1, 2), (1, 2), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
    ('TEXTCOLOR', (0, 2), (-1, 2), WHITE),
    ('FONTNAME', (0, 0), (-1, 0), 'CN-Bold'),
    ('FONTNAME', (0, 2), (-1, 2), 'CN-Bold'),
    ('LINEBELOW', (0, 0), (-1, 0), 1.2, GOLD),
    ('LINEBELOW', (0, 2), (-1, 2), 1.2, NAVY),
    ('GRID', (0, 0), (-1, -1), 0.4, GREY_LIGHT),
]))
content.append(Paragraph('表 4.1 · SWOT 战略矩阵', caption))

content.append(Paragraph('4.2 战略锚点（Positioning Statement）', h1))
content.append(callout(
    '"东方海岸 · 私享圈层"——日照唯一以专业雪茄、国际烈酒与小圈层文化为内核的'
    '高端会员制雪茄吧，为本地企业家与高频商务访客提供"懂行、私密、有温度"的'
    '社交场域。'))
content.append(PageBreak())

# ===========================================================================
# 05 PRODUCT
# ===========================================================================
content += section_divider(
    '05', '产品与体验设计', 'PRODUCT & EXPERIENCE',
    '围绕客群与战略锚点，设计产品组合、体验旅程与价格区间。')

content.append(Paragraph('5.1 产品组合（SKU 蓝图）', h1))
sku = [
    [Paragraph('品类', cell_header),
     Paragraph('代表 SKU 方向', cell_header),
     Paragraph('参考价位', cell_header),
     Paragraph('占营收预期', cell_header)],
    [Paragraph('雪茄', cell_tag),
     Paragraph('古巴系列（COHIBA / Montecristo / Partagas）、'
               '尼加拉瓜与多米尼加精选', cell_body),
     Paragraph('300 – 1,800 元/支', cell_center),
     Paragraph('约 45%', cell_center)],
    [Paragraph('烈酒', cell_tag),
     Paragraph('单一麦芽威士忌、干邑、波本、'
               '日威与中国精品白酒', cell_body),
     Paragraph('80 – 600 元/杯', cell_center),
     Paragraph('约 25%', cell_center)],
    [Paragraph('搭餐与轻食', cell_tag),
     Paragraph('熟成牛肉、伊比利亚火腿、海岸生蚝、'
               '黑巧克力与雪茄伴侣', cell_body),
     Paragraph('60 – 280 元/份', cell_center),
     Paragraph('约 12%', cell_center)],
    [Paragraph('会员与体验', cell_tag),
     Paragraph('年度会籍、私人储烟柜、品鉴会、'
               '雪茄旅行', cell_body),
     Paragraph('1.2 – 5.8 万元/年', cell_center),
     Paragraph('约 15%', cell_center)],
    [Paragraph('礼盒与定制', cell_tag),
     Paragraph('节日礼盒、企业定制、雪茄火机/剪等周边', cell_body),
     Paragraph('800 – 8,000 元/单', cell_center),
     Paragraph('约 3%', cell_center)],
]
content.append(themed_table(sku,
                            [2.8 * cm, 7.0 * cm, 3.7 * cm, 3.5 * cm]))
content.append(Paragraph('表 5.1 · SKU 蓝图（基础情景）', caption))

content.append(Paragraph('5.2 客户体验旅程（Customer Journey）', h1))
journey = [
    [Paragraph('阶段', cell_header),
     Paragraph('触点', cell_header),
     Paragraph('体验设计要点', cell_header)],
    [Paragraph('① 触达', cell_tag),
     Paragraph('微信/小程序、酒店礼宾、圈层口碑', cell_body),
     Paragraph('"私享 + 圈层"叙事，避免硬广，强调推荐入会。', cell_body)],
    [Paragraph('② 预约', cell_tag),
     Paragraph('一对一管家或小程序预约', cell_body),
     Paragraph('记录偏好（口味、烈酒、忌讳），48 小时内回访确认。', cell_body)],
    [Paragraph('③ 到店', cell_tag),
     Paragraph('迎宾、衣帽寄存、引导入座', cell_body),
     Paragraph('入座 90 秒内完成迎宾酒与个性化招呼。', cell_body)],
    [Paragraph('④ 品鉴', cell_tag),
     Paragraph('雪茄推荐、开盒、点燃、配酒', cell_body),
     Paragraph('雪茄顾问全程陪同，提供 1–2 款搭配建议。', cell_body)],
    [Paragraph('⑤ 沉淀', cell_tag),
     Paragraph('会员档案、私人储烟柜、生日礼遇', cell_body),
     Paragraph('数据化偏好沉淀，月度个性化关怀触达。', cell_body)],
    [Paragraph('⑥ 复购与裂变', cell_tag),
     Paragraph('主题沙龙、跨界活动、推荐礼遇', cell_body),
     Paragraph('每会员每年至少 2 次社群活动 + 1 次 1:1 礼遇。', cell_body)],
]
content.append(themed_table(journey,
                            [2.4 * cm, 5.6 * cm, 9.0 * cm]))
content.append(Paragraph('表 5.2 · 客户体验旅程关键触点', caption))
content.append(PageBreak())

# ===========================================================================
# 06 LOCATION
# ===========================================================================
content += section_divider(
    '06', '选址策略与空间规划', 'LOCATION & SPACE',
    '从客流、租金、合规与品牌四个维度对候选区域进行打分，并给出空间功能布置建议。')

content.append(Paragraph('6.1 候选商圈打分模型（1–5 分制）', h1))
loc = [
    [Paragraph('候选商圈', cell_header),
     Paragraph('客流质量', cell_header),
     Paragraph('租金水平', cell_header),
     Paragraph('合规便利', cell_header),
     Paragraph('品牌契合', cell_header),
     Paragraph('综合', cell_header)],
    [Paragraph('五星酒店配套层（日照核心酒店）', cell_tag),
     Paragraph('5', cell_center), Paragraph('3', cell_center),
     Paragraph('4', cell_center), Paragraph('5', cell_center),
     Paragraph('4.3', cell_center)],
    [Paragraph('CBD 写字楼裙房（市中心）', cell_tag),
     Paragraph('4', cell_center), Paragraph('3', cell_center),
     Paragraph('5', cell_center), Paragraph('4', cell_center),
     Paragraph('4.0', cell_center)],
    [Paragraph('海滨度假区（万平口/灯塔）', cell_tag),
     Paragraph('4', cell_center), Paragraph('2', cell_center),
     Paragraph('3', cell_center), Paragraph('5', cell_center),
     Paragraph('3.5', cell_center)],
    [Paragraph('高端商业综合体（万达/银座等）', cell_tag),
     Paragraph('3', cell_center), Paragraph('3', cell_center),
     Paragraph('4', cell_center), Paragraph('3', cell_center),
     Paragraph('3.3', cell_center)],
    [Paragraph('独立沿街高端街区', cell_tag),
     Paragraph('3', cell_center), Paragraph('4', cell_center),
     Paragraph('3', cell_center), Paragraph('3', cell_center),
     Paragraph('3.3', cell_center)],
]
content.append(themed_table(loc,
                            [5.4 * cm, 2.0 * cm, 2.0 * cm, 2.0 * cm, 2.2 * cm, 1.4 * cm]))
content.append(Paragraph('表 6.1 · 候选商圈打分（首选：五星酒店配套；备选：CBD 裙房）', caption))

content.append(Paragraph('6.2 空间功能与面积建议', h1))
content.append(Paragraph(
    '建议总建筑面积 200–260 平方米，核心功能区如下：', body))
for x in bullets([
    '<b>礼宾接待区（10–15㎡）</b>：低饱和度灯光 + 入门叙事墙，承担首因效应。',
    '<b>主吧台与开放席位（45–60㎡）</b>：8–12 个吧台位，承接散客与轻度社交。',
    '<b>私密包厢 ×3–4（每间 18–28㎡）</b>：商务洽谈、圈层小聚的核心动线。',
    '<b>VIP 沙龙厅（35–45㎡）</b>：可容纳 12–18 人的活动与品鉴会。',
    '<b>Walk-in Humidor 雪茄房（15–22㎡）</b>：恒温恒湿、独立新风，为差异化核心。',
    '<b>会员储烟柜墙（沿动线 8–12㎡）</b>：可视化的会员归属感符号。',
    '<b>员工与备品区（25–35㎡）</b>：含吧台后场、洗杯、备餐与库房。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 07 OPERATING MODEL
# ===========================================================================
content += section_divider(
    '07', '运营模式与组织架构', 'OPERATING MODEL & ORGANIZATION',
    '聚焦会员体系、人员配置与服务标准，给出 Day-1 可落地的运营框架。')

content.append(Paragraph('7.1 三级会员体系', h1))
mem = [
    [Paragraph('等级', cell_header),
     Paragraph('年费', cell_header),
     Paragraph('核心权益', cell_header),
     Paragraph('目标人数（Y1）', cell_header)],
    [Paragraph('海岸 · CLASSIC', cell_tag),
     Paragraph('1.2 万元', cell_center),
     Paragraph('储烟柜、品鉴会优先、9 折消费、生日礼遇', cell_body),
     Paragraph('200 人', cell_center)],
    [Paragraph('海岸 · PRESTIGE', cell_tag),
     Paragraph('2.8 万元', cell_center),
     Paragraph('独立储烟柜、专属顾问、月度沙龙、'
               '配偶/合伙人副卡', cell_body),
     Paragraph('80 人', cell_center)],
    [Paragraph('海岸 · LEGEND', cell_tag),
     Paragraph('5.8 万元', cell_center),
     Paragraph('VIP 厅使用权、限定批次优先认购、'
               '年度雪茄旅行', cell_body),
     Paragraph('20 人', cell_center)],
]
content.append(themed_table(mem,
                            [3.4 * cm, 2.2 * cm, 8.6 * cm, 2.8 * cm]))
content.append(Paragraph('表 7.1 · 三级会员体系（首年目标 300 名核心会员）', caption))

content.append(Paragraph('7.2 组织架构（首年 9 人精干团队）', h1))
org = [
    [Paragraph('岗位', cell_header),
     Paragraph('编制', cell_header),
     Paragraph('关键职责', cell_header)],
    [Paragraph('店长 / 运营总监', cell_tag),
     Paragraph('1', cell_center),
     Paragraph('总体经营、会员关系、合规与对外协作。', cell_body)],
    [Paragraph('首席雪茄顾问', cell_tag),
     Paragraph('1', cell_center),
     Paragraph('选品、培训、品鉴会主持，建议有 5+ 年雪茄经验。', cell_body)],
    [Paragraph('雪茄顾问 / 服务师', cell_tag),
     Paragraph('2', cell_center),
     Paragraph('一对一服务、雪茄推荐、知识传递。', cell_body)],
    [Paragraph('首席调酒师', cell_tag),
     Paragraph('1', cell_center),
     Paragraph('烈酒酒单、配酒方案、季节限定。', cell_body)],
    [Paragraph('助理调酒 / 服务', cell_tag),
     Paragraph('2', cell_center),
     Paragraph('吧台运营、出品、回收。', cell_body)],
    [Paragraph('厨房与备餐', cell_tag),
     Paragraph('1', cell_center),
     Paragraph('小食、拼盘、外采食品的备制与品控。', cell_body)],
    [Paragraph('会员与营销专员', cell_tag),
     Paragraph('1', cell_center),
     Paragraph('SCRM 运营、内容产出、活动组织。', cell_body)],
]
content.append(themed_table(org,
                            [3.6 * cm, 1.8 * cm, 11.6 * cm]))
content.append(Paragraph('表 7.2 · 首年组织架构（合计 9 人，旺季可外聘 1–2 名兼职）', caption))
content.append(PageBreak())

# ===========================================================================
# 08 MARKETING
# ===========================================================================
content += section_divider(
    '08', '营销与会员增长', 'MARKETING & MEMBERSHIP GROWTH',
    '基于"低密度、高调性"原则，构建从冷启动到稳态的传播与增长路径。')

content.append(Paragraph('8.1 增长路径（Y1）', h1))
content.append(Paragraph(
    '雪茄品类的"广告法红线"决定了我们不能依赖传统硬广。'
    '增长路径以"圈层口碑 + 内容生活方式 + 跨界合作"三条腿前进：', body))
for x in bullets([
    '<b>0–3 月（蓄水）</b>：完成品牌识别、小程序、SCRM 与种子会员邀请清单。',
    '<b>3–6 月（试营业）</b>：100 名种子会员体验 + 媒体小范围探店；'
    '邀请制为主，避免大规模宣传。',
    '<b>6–12 月（正式开业）</b>：每月 1 场主题品鉴会 + 1 场跨界合作（汽车/腕表/艺廊）；'
    '小红书/抖音以"生活方式"内容为主。',
    '<b>12–18 月（稳态）</b>：会员推荐机制成熟、第二批会籍升级；'
    '与本地酒店、银行私行、汽车 4S 店建立长期联名计划。',
]):
    content.append(x)

content.append(Paragraph('8.2 跨界合作清单', h1))
xb = [
    [Paragraph('合作方类别', cell_header),
     Paragraph('合作形式', cell_header),
     Paragraph('对项目的价值', cell_header)],
    [Paragraph('五星酒店与度假村', cell_tag),
     Paragraph('客房雪茄礼遇 / 联名套餐', cell_body),
     Paragraph('稳定外地高端访客导入。', cell_body)],
    [Paragraph('银行私行 / 券商财富', cell_tag),
     Paragraph('客户答谢沙龙 / 信用卡权益', cell_body),
     Paragraph('精准触达高净值客户。', cell_body)],
    [Paragraph('豪华汽车 4S 店', cell_tag),
     Paragraph('试驾 + 雪茄之夜', cell_body),
     Paragraph('品牌调性互补、共享客户资源。', cell_body)],
    [Paragraph('腕表 / 艺廊 / 帆船', cell_tag),
     Paragraph('限定主题展、艺术家驻店', cell_body),
     Paragraph('强化生活方式叙事，制造内容素材。', cell_body)],
    [Paragraph('企业团建与商会', cell_tag),
     Paragraph('包场 / 会员日 / 年度活动', cell_body),
     Paragraph('B 端营收补充，提升淡季利用率。', cell_body)],
]
content.append(themed_table(xb,
                            [4.2 * cm, 5.8 * cm, 7.0 * cm]))
content.append(Paragraph('表 8.1 · 重点跨界合作清单', caption))
content.append(PageBreak())

# ===========================================================================
# 09 FINANCIALS
# ===========================================================================
content += section_divider(
    '09', '财务测算与回报情景', 'FINANCIALS & RETURNS',
    '给出三套情景下的投资、营收、成本与回报指引。所有数字均为指示性，'
    '仅供决策参考。')

content.append(Paragraph('9.1 一次性投资（CapEx）', h1))
capex = [
    [Paragraph('科目', cell_header),
     Paragraph('金额（万元）', cell_header),
     Paragraph('说明', cell_header)],
    [Paragraph('设计与装修', cell_tag),
     Paragraph('120 – 160', cell_center),
     Paragraph('含主材升级与海洋气候应对。', cell_body)],
    [Paragraph('Walk-in Humidor 与新风', cell_tag),
     Paragraph('30 – 45', cell_center),
     Paragraph('恒温恒湿系统、独立新风、消防联动。', cell_body)],
    [Paragraph('家具与软装', cell_tag),
     Paragraph('25 – 40', cell_center),
     Paragraph('真皮沙发、个性灯具、艺术品陈列。', cell_body)],
    [Paragraph('IT 与音视频', cell_tag),
     Paragraph('15 – 22', cell_center),
     Paragraph('SCRM、POS、监控、音响、智控。', cell_body)],
    [Paragraph('首批雪茄与酒水备货', cell_tag),
     Paragraph('60 – 90', cell_center),
     Paragraph('雪茄 50–60 万 / 烈酒 15–25 万。', cell_body)],
    [Paragraph('品牌与开业活动', cell_tag),
     Paragraph('15 – 25', cell_center),
     Paragraph('VI 设计、内容拍摄、首发活动。', cell_body)],
    [Paragraph('许可与开办杂费', cell_tag),
     Paragraph('8 – 14', cell_center),
     Paragraph('烟草、消防、消防、营业等。', cell_body)],
    [Paragraph('合计', cell_header),
     Paragraph('273 – 396', cell_header),
     Paragraph('建议中位 ≈ 330 万元', cell_header)],
]
content.append(themed_table(capex,
                            [5.8 * cm, 3.0 * cm, 8.2 * cm]))
content.append(Paragraph('表 9.1 · 一次性投资估算（指示性）', caption))

content.append(Paragraph('9.2 三情景营收预测（年度）', h1))
scen = [
    [Paragraph('情景', cell_header),
     Paragraph('月均营收', cell_header),
     Paragraph('年度营收', cell_header),
     Paragraph('综合毛利率', cell_header),
     Paragraph('净利率', cell_header)],
    [Paragraph('保守情景', cell_tag),
     Paragraph('55 万元', cell_center),
     Paragraph('660 万元', cell_center),
     Paragraph('52%', cell_center),
     Paragraph('6 – 9%', cell_center)],
    [Paragraph('基础情景', cell_tag),
     Paragraph('75 万元', cell_center),
     Paragraph('900 万元', cell_center),
     Paragraph('58%', cell_center),
     Paragraph('14 – 18%', cell_center)],
    [Paragraph('乐观情景', cell_tag),
     Paragraph('95 万元', cell_center),
     Paragraph('1,140 万元', cell_center),
     Paragraph('62%', cell_center),
     Paragraph('20 – 24%', cell_center)],
]
content.append(themed_table(scen,
                            [3.4 * cm, 3.0 * cm, 3.0 * cm, 3.4 * cm, 3.2 * cm]))
content.append(Paragraph('表 9.2 · 三情景年度营收与利润率（稳态期）', caption))

content.append(Paragraph('9.3 回报指标（基础情景）', h1))
content.append(kpi_strip([
    ('PAYBACK · 回收期', '24–32 月', '含 6 个月筹建期'),
    ('IRR · 内部回报率', '18–22%', '5 年期、不含残值'),
    ('BREAKEVEN · 单月盈亏', '≈ 58 万元', '基础情景 / 综合毛利 58%'),
    ('OCC · 平均上座率', '45–55%', '稳态期目标'),
]))
content.append(PageBreak())

# ===========================================================================
# 10 RISK
# ===========================================================================
content += section_divider(
    '10', '风险矩阵与合规要点', 'RISK & COMPLIANCE',
    '识别核心风险并给出缓释措施，重点强调烟草与控烟相关合规边界。')

content.append(Paragraph('10.1 风险矩阵（概率 × 影响）', h1))
risk = [
    [Paragraph('风险', cell_header),
     Paragraph('概率', cell_header),
     Paragraph('影响', cell_header),
     Paragraph('缓释措施', cell_header)],
    [Paragraph('烟草许可与控烟合规收紧', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('高', cell_center),
     Paragraph('合规预审、专项法律顾问、新风/排烟系统冗余设计。', cell_body)],
    [Paragraph('雪茄供应链中断或价格波动', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('中—高', cell_center),
     Paragraph('多源代理 + 安全库存 8–12 周；汇率敏感品类按月对冲。', cell_body)],
    [Paragraph('会员增长不及预期', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('高', cell_center),
     Paragraph('强化首年口碑与跨界合作；预留预算用于精准定向营销。', cell_body)],
    [Paragraph('海洋气候导致存储事故', cell_tag),
     Paragraph('低—中', cell_center),
     Paragraph('中', cell_center),
     Paragraph('双套温湿度系统 + 实时告警 + 月度专项巡检。', cell_body)],
    [Paragraph('宏观经济波动压缩高端消费', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('中', cell_center),
     Paragraph('B 端企业合作与礼盒业务作为稳定器；'
               '调整 SKU 价格带应对周期。', cell_body)],
    [Paragraph('核心人才流失', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('中', cell_center),
     Paragraph('股权激励 + 体系化 SOP + 培训矩阵，降低个人依赖度。', cell_body)],
]
content.append(themed_table(risk,
                            [4.6 * cm, 1.8 * cm, 1.8 * cm, 8.8 * cm]))
content.append(Paragraph('表 10.1 · 主要风险与缓释措施', caption))

content.append(Paragraph('10.2 合规清单（开业前必须完成）', h1))
for x in bullets([
    '烟草专卖零售许可证（向当地烟草专卖局申请，需明确经营场所与品类）。',
    '酒类经营备案与营业执照、食品经营许可证（含小食与拼盘）。',
    '消防安全检查与排烟、新风系统验收。',
    '场所控烟告示与烟雾防扩散设计，符合《公共场所控制吸烟条例》要求。',
    '广告与传播红线培训：避免在公开渠道宣传具体烟草品牌与产品。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 11 ROADMAP
# ===========================================================================
content += section_divider(
    '11', '实施路线图', 'IMPLEMENTATION ROADMAP',
    '以 12 个月为颗粒度，给出从立项到稳态运营的关键里程碑与责任分工。')

roadmap = [
    [Paragraph('阶段 / 月份', cell_header),
     Paragraph('M1', cell_header), Paragraph('M2', cell_header),
     Paragraph('M3', cell_header), Paragraph('M4', cell_header),
     Paragraph('M5', cell_header), Paragraph('M6', cell_header),
     Paragraph('M7', cell_header), Paragraph('M8', cell_header),
     Paragraph('M9', cell_header), Paragraph('M10', cell_header),
     Paragraph('M11', cell_header), Paragraph('M12', cell_header)],
    [Paragraph('立项 / 选址', cell_tag)] +
        [Paragraph('●', cell_center)] * 3 + [Paragraph('', cell_center)] * 9,
    [Paragraph('合规 / 预审', cell_tag),
     Paragraph('', cell_center), Paragraph('●', cell_center),
     Paragraph('●', cell_center), Paragraph('●', cell_center)] +
        [Paragraph('', cell_center)] * 8,
    [Paragraph('设计 / 装修', cell_tag)] +
        [Paragraph('', cell_center)] * 2 +
        [Paragraph('●', cell_center)] * 4 + [Paragraph('', cell_center)] * 6,
    [Paragraph('供应链 / 备货', cell_tag)] +
        [Paragraph('', cell_center)] * 3 +
        [Paragraph('●', cell_center)] * 3 + [Paragraph('', cell_center)] * 6,
    [Paragraph('团队 / 培训', cell_tag)] +
        [Paragraph('', cell_center)] * 4 +
        [Paragraph('●', cell_center)] * 3 + [Paragraph('', cell_center)] * 5,
    [Paragraph('品牌 / 种子会员', cell_tag)] +
        [Paragraph('', cell_center)] * 3 +
        [Paragraph('●', cell_center)] * 4 + [Paragraph('', cell_center)] * 5,
    [Paragraph('试营业', cell_tag)] +
        [Paragraph('', cell_center)] * 6 +
        [Paragraph('●', cell_center)] * 2 + [Paragraph('', cell_center)] * 4,
    [Paragraph('正式开业 / 营销', cell_tag)] +
        [Paragraph('', cell_center)] * 7 +
        [Paragraph('●', cell_center)] * 3 + [Paragraph('', cell_center)] * 2,
    [Paragraph('稳态 / 复盘迭代', cell_tag)] +
        [Paragraph('', cell_center)] * 10 +
        [Paragraph('●', cell_center)] * 2,
]
content.append(themed_table(roadmap,
                            [3.8 * cm] + [1.05 * cm] * 12))
content.append(Paragraph('表 11.1 · 12 个月里程碑甘特（●=核心活动月份）', caption))

content.append(Paragraph('关键里程碑（Go/No-Go 决策点）', h1))
for x in bullets([
    '<b>M3 末</b>：选址锁定 + 合规可行性确认 → Go/No-Go #1',
    '<b>M6 末</b>：装修过半 + 烟草许可申请受理 + 30 名种子会员 → Go/No-Go #2',
    '<b>M8 末</b>：试营业首月营收达成保守情景的 70% → 进入正式开业准备',
    '<b>M12 末</b>：会员沉淀 ≥ 200 人，月营收达基础情景的 80% → 进入稳态优化',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 12 CONCLUSION
# ===========================================================================
content += section_divider(
    '12', '结论与下一步建议', 'CONCLUSION & NEXT STEPS',
    '总结判断并给出推进项目所需的下一步具体动作。')

content.append(Paragraph('总体结论', h1))
content.append(Paragraph(
    '基于对日照宏观环境、需求结构、行业格局与财务可行性的系统分析，'
    '我们的总体判断是：<b>本项目具备明确的市场机会与可控的风险结构，'
    '建议以"小而精、深而稳"的策略推进立项</b>。', body))
content.append(Paragraph(
    '与传统酒吧或会所相比，雪茄吧的护城河来自"专业 × 圈层 × 体验"三者的复合。'
    '日照独特的海岸城市气质，叠加港口经济与高端文旅客流，'
    '为打造"东方海岸 · 私享圈层"叙事提供了别处难以复制的场景资源。'
    '只要在合规、选址、品牌与运营四个维度保持高执行力，'
    '本项目可以成为日照高端社交领域的标杆业态。', body))

content.append(Paragraph('建议的下一步动作（90 天清单）', h1))
nxt = [
    [Paragraph('编号', cell_header),
     Paragraph('动作', cell_header),
     Paragraph('责任方', cell_header),
     Paragraph('截止', cell_header)],
    [Paragraph('01', cell_tag),
     Paragraph('与 2–3 家头部雪茄代理商初步接洽，'
               '锁定供应渠道与年度配额意向。', cell_body),
     Paragraph('项目方 + 顾问', cell_center),
     Paragraph('30 天内', cell_center)],
    [Paragraph('02', cell_tag),
     Paragraph('完成 3–5 个候选物业实地踏勘与租金谈判，'
               '形成短名单。', cell_body),
     Paragraph('项目方', cell_center),
     Paragraph('45 天内', cell_center)],
    [Paragraph('03', cell_tag),
     Paragraph('就候选物业开展烟草、消防、卫健合规预审。', cell_body),
     Paragraph('合规顾问', cell_center),
     Paragraph('60 天内', cell_center)],
    [Paragraph('04', cell_tag),
     Paragraph('完成品牌命名、VI 设计与官方账号矩阵搭建。', cell_body),
     Paragraph('品牌顾问', cell_center),
     Paragraph('60 天内', cell_center)],
    [Paragraph('05', cell_tag),
     Paragraph('与 50–80 名潜在种子会员进行 1:1 沟通，'
               '验证产品/价格假设。', cell_body),
     Paragraph('项目方', cell_center),
     Paragraph('90 天内', cell_center)],
    [Paragraph('06', cell_tag),
     Paragraph('完成正式商业计划书与第一轮预算冻结，'
               '启动装修招标。', cell_body),
     Paragraph('项目方 + 顾问', cell_center),
     Paragraph('90 天内', cell_center)],
]
content.append(themed_table(nxt,
                            [1.4 * cm, 8.6 * cm, 3.6 * cm, 2.4 * cm]))
content.append(Paragraph('表 12.1 · 推进项目所需的 90 天关键动作', caption))

content.append(Spacer(1, 0.6 * cm))
content.append(callout(
    '"日照的海风、港口的灯光、品鉴室里的烟雾——'
    '我们建议把它们组合成一个属于这座城市的、值得被记住的私享空间。"'))

content.append(Spacer(1, 1 * cm))
content.append(Paragraph('— 报告完 —', ParagraphStyle(
    'End', fontName='CN', fontSize=10, leading=16,
    textColor=GREY_MID, alignment=TA_CENTER)))


# ---------------------------------------------------------------------------
# Page-template dispatch (cover gets the dark page; rest gets the body page)
# ---------------------------------------------------------------------------
def on_first_page(canvas, doc):
    draw_cover_background(canvas, doc)


def on_later_pages(canvas, doc):
    draw_body_page(canvas, doc)


output_filename = 'cigar_rizhao_feasibility_report.pdf'
doc = SimpleDocTemplate(
    output_filename,
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm,
    title='山东日照雪茄吧可行性研究报告',
    author='East Coast Advisory',
)
doc.build(content, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f'PDF generated: {output_filename}')
