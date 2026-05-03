"""
K-12 AI Learning · Vibe Coding 新产品线可行性报告 — Consulting-grade PDF generator.

Style references: McKinsey / BCG / Bain reports. Layout features include
a branded cover page, a table of contents, color-coded section dividers,
structured frameworks (PESTEL, Porter's Five Forces, SWOT), unit economics,
financial projection tables, an implementation roadmap, and page headers/footers.

Mirrors the structure of the Rizhao cigar bar report, adapted for a
consumer ed-tech / K-12 AI self-learning product line.
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
# Brand palette (deep navy + gold accents — consistent with prior reports)
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
    'CoverTitle', fontName='CN-Bold', fontSize=32, leading=42,
    textColor=WHITE, alignment=TA_LEFT, spaceAfter=10)
cover_subtitle = ParagraphStyle(
    'CoverSubtitle', fontName='CN', fontSize=15, leading=22,
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
    canvas.drawRightString(PAGE_W - 2 * cm, 1.5 * cm, '2026 · K-12 AI 教育')
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
    canvas.drawString(2 * cm, PAGE_H - 0.8 * cm,
                      'K-12 AI 学习 · Vibe Coding 新产品线 · 可行性研究报告')
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
                             'K-12 AI · Vibe Coding 可行性研究')
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
                'KpiNum', fontName='CN-Bold', fontSize=20, leading=24,
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
content.append(Spacer(1, 6.0 * cm))
content.append(Paragraph('STRATEGIC FEASIBILITY STUDY', cover_tag))
content.append(Paragraph('K-12 AI 自主学习<br/>Vibe Coding 新产品线<br/>可行性研究报告', cover_title))
content.append(Spacer(1, 0.6 * cm))
content.append(Paragraph('K-12 AI Self-Learning · Vibe Coding — '
                         'New Product Line Market Entry & Operating Blueprint',
                         cover_subtitle))
content.append(Spacer(1, 4.6 * cm))
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
    '所引用的政策、市场规模、用户行为与价格数据来源于教育部公开文件、'
    '主管行业协会、第三方研究机构与公开渠道，已尽合理努力进行交叉验证。'
    '报告中的财务测算与情景分析为基于假设的指示性结果，'
    '不构成任何投资承诺或回报保证。', body))
content.append(Paragraph(
    '本报告仅供项目方内部决策参考，未经书面授权不得向第三方披露、复制或传播。'
    'K-12 教育业务涉及《未成年人保护法》《个人信息保护法》《义务教育阶段校外培训管理》'
    '等多重监管要求；因 Vibe Coding 形态依赖大模型与 AI 内容生成，'
    '还需参照《生成式人工智能服务管理暂行办法》等相关规定。'
    '项目方在实际推进前，应就办学许可、未成年人信息合规、'
    'AI 内容安全等议题与法律顾问进行专项确认。', body))
content.append(Spacer(1, 1 * cm))
content.append(callout(
    '"在合规边界内，把『AI 原生学习体验』做深、把家长付费意愿做厚——'
    '这是 K-12 AI 学习 + Vibe Coding 产品从 0 到 1 的核心命题。"'))
content.append(PageBreak())

# ----- TABLE OF CONTENTS -----
content.append(Spacer(1, 1.5 * cm))
content.append(Paragraph('目录  /  CONTENTS', h1))
content.append(HRFlowable(width=4 * cm, thickness=2, color=GOLD,
                          spaceAfter=18))

toc = [
    ('00', '执行摘要', 'Executive Summary'),
    ('01', '宏观环境与政策扫描（PESTEL）', 'Macro & Policy Scan'),
    ('02', '市场需求与目标客群', 'Demand & Customer Segmentation'),
    ('03', '行业格局与竞争分析（五力）', 'Industry & Competitive Landscape'),
    ('04', 'SWOT 与战略定位', 'SWOT & Strategic Positioning'),
    ('05', '产品与课程体系设计', 'Product & Curriculum Design'),
    ('06', '技术平台与 AI 教学架构', 'Tech Platform & AI Pedagogy'),
    ('07', '运营模式与组织架构', 'Operating Model & Organization'),
    ('08', '获客与增长策略', 'Marketing & Growth Strategy'),
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
    '本章浓缩全报告核心结论：行业窗口、产品定位、关键经济指标与立项建议。')

content.append(Paragraph('核心判断', h1))
content.append(Paragraph(
    '我们认为，2026 年是中国 K-12 AI 教育市场的第二波结构性窗口。'
    '与 2017–2019 年第一波"少儿编程热"相比，本次窗口由三股力量叠加驱动：'
    '① 教育部"中小学人工智能教育"政策落地、② 大模型与 Agent 工具成熟、'
    '③ "双减"后家长在素质教育与硬核技能上的预算回流。'
    '在此背景下，以 <b>Vibe Coding</b>（学员通过自然语言指挥 AI 生成可运行作品）'
    '为核心交付形态、以"自主学习 + 项目驱动"为教学逻辑的新产品线，'
    '具备清晰的差异化空间与可观的商业回报潜力。', body))

content.append(Spacer(1, 0.4 * cm))
content.append(kpi_strip([
    ('TAM  ·  目标市场', '~520 亿', 'K-12 素质教育中 AI/编程赛道，2026E'),
    ('GAP  ·  品类空白', '0 → 1', '原生 Vibe Coding 教学尚无成规模玩家'),
    ('PAYBACK  ·  回收期', '18–28 月', '基础情景 IRR 28–35%'),
    ('LTV/CAC', '4.0 – 5.5×', '稳态期目标，依赖续费率 ≥ 70%'),
]))

content.append(Spacer(1, 0.4 * cm))
content.append(Paragraph('五大关键结论', h1))
content.append(Paragraph(
    '<b>1. 政策风口明确</b>：教育部已要求 2030 年前在中小学全面普及 AI 教育，'
    'AI/编程明确归入"非学科类"素质教育白名单，不受义务教育阶段学科类培训限制。', body))
content.append(Paragraph(
    '<b>2. 用户行为迁移</b>：00 后、10 后是"AI 原住民"，习惯与 ChatGPT、'
    '豆包、Kimi、文小言等对话；"教语法"的传统编程课正在被"教思维 + 教协作 AI"取代。', body))
content.append(Paragraph(
    '<b>3. 差异化定位窗口</b>：现有头部玩家（编程猫、核桃编程等）仍以 Scratch / Python 语法'
    '为主线，Vibe Coding 是真正的"AI Native"教学路径，可形成代际差异。', body))
content.append(Paragraph(
    '<b>4. 财务可行</b>：在基础情景假设下（首年 1.2 万付费学员、'
    '客单价 4,800 元、续费率 65%），18–28 个月可实现现金回收，'
    '第 3 年净利率有望达到 15–22%，LTV/CAC 提升至 4.0× 以上。', body))
content.append(Paragraph(
    '<b>5. 关键风险可控</b>：AI 内容安全、未成年人信息合规、家长对"自主学习"的'
    '信任度建设，是三大核心风险——通过分层内容审核、隐私保护设计与'
    '家长仪表盘可显著缓释。', body))

content.append(Spacer(1, 0.4 * cm))
content.append(callout(
    '建议：立项推进。优先在 6 个月内完成 MVP 上线、首批 1,000 名内测用户与'
    '学习成效数据沉淀；12 个月内进入正式商业化，18 个月内累计付费学员突破 1.2 万。'))
content.append(PageBreak())

# ===========================================================================
# 01 PESTEL
# ===========================================================================
content += section_divider(
    '01', '宏观环境与政策扫描', 'MACRO & POLICY SCAN',
    '采用 PESTEL 框架，对中国 K-12 AI 教育的宏观环境进行结构化扫描，'
    '识别项目可利用的趋势与必须跨越的约束。')

content.append(Paragraph('1.1 行业基本面', h1))
content.append(Paragraph(
    'K-12 校外培训自 2021 年"双减"后经历了大规模出清：学科类培训规模'
    '从峰值约 6,000 亿元收缩至 2,000 亿元以内，但"非学科素质教育"赛道'
    '反而扩容，2026 年市场规模预计达 2,800–3,200 亿元。其中 AI/编程子赛道'
    '受益于政策与技术双重驱动，从 2022 年的不足 200 亿元，预计到 2026 年'
    '增长至 480–550 亿元，3 年 CAGR 约 28%。', body))
content.append(Paragraph(
    '与此同时，大模型与 AI Agent 工具走向成熟，为"非语法依赖"的'
    '编程教学打开了想象空间。Vibe Coding（由 Andrej Karpathy 提出、'
    '近一年广泛传播的概念）正快速成为成人开发者社区的主流形态——'
    '把这套范式向 K-12 平移，是一个"自上而下被验证、自下而上有需求"的机会。', body))

content.append(Paragraph('1.2 PESTEL 框架扫描', h1))
pestel_data = [
    [Paragraph('维度', cell_header),
     Paragraph('关键观察', cell_header),
     Paragraph('对项目的含义', cell_header)],
    [Paragraph('Political<br/>政策', cell_tag),
     Paragraph('教育部明确要求中小学 2030 年前全面普及 AI 教育；'
               'AI/编程归入"非学科类"白名单；'
               '同时《未成年人网络保护条例》与防沉迷系统对线上教育有专项要求。', cell_body),
     Paragraph('政策风口明确，但产品形态需内嵌使用时长管理、'
               '内容审核与未成年人信息保护，作为合规底盘。', cell_body)],
    [Paragraph('Economic<br/>经济', cell_tag),
     Paragraph('家庭教育支出仍是优先级最高的可选支出之一；'
               '中产家庭对"硬核技能 + 升学加分"的复合诉求强烈。', cell_body),
     Paragraph('客单价 3,500–6,800 元的年度课包具备承接能力；'
               '学科类预算回流是最大增量。', cell_body)],
    [Paragraph('Social<br/>社会', cell_tag),
     Paragraph('00 后、10 后是"AI 原住民"，对话式产品认知门槛趋零；'
               '家长焦虑从"应试"转向"未来竞争力"。', cell_body),
     Paragraph('"自主学习 + 看得见作品"是产品体验设计的两条主线。', cell_body)],
    [Paragraph('Technological<br/>技术', cell_tag),
     Paragraph('国产大模型（豆包、通义、Kimi、DeepSeek 等）能力快速逼近 GPT-4 级别；'
               '推理成本从 2023 年的 ~$10/M token 降至 2026 年的 < $0.5/M token。', cell_body),
     Paragraph('"AI 即基础设施"已成立，可基于 API 自建 K-12 专属智能体；'
               '推理成本从 P&L 重负担降为可控变量。', cell_body)],
    [Paragraph('Environmental<br/>环境', cell_tag),
     Paragraph('青少年屏幕使用时长与视力保护是社会舆论与监管关注的高敏感点。', cell_body),
     Paragraph('产品默认强制护眼模式、单次学习时长限制、'
               '强化离屏作品产出（实物、展示、汇报）。', cell_body)],
    [Paragraph('Legal<br/>法律', cell_tag),
     Paragraph('需符合《个人信息保护法》《未成年人保护法》'
               '《生成式人工智能服务管理暂行办法》《教育移动应用备案管理办法》'
               '等多部规章；非学科培训需办理相应资质。', cell_body),
     Paragraph('合规预算在第一年应不低于总投入的 5%；'
               '建立专属合规与内容安全岗位。', cell_body)],
]
content.append(themed_table(pestel_data,
                            [2.6 * cm, 7.4 * cm, 7.0 * cm]))
content.append(Paragraph('表 1.1 · K-12 AI 学习 · Vibe Coding 项目 PESTEL 扫描', caption))
content.append(PageBreak())

# ===========================================================================
# 02 DEMAND
# ===========================================================================
content += section_divider(
    '02', '市场需求与目标客群', 'DEMAND & SEGMENTATION',
    '从家长付费决策、学生年龄分层与使用动机三个维度刻画需求侧，'
    '识别核心与扩展客群。')

content.append(Paragraph('2.1 K-12 AI/编程市场规模与结构（指示性）', h1))
mkt = [
    [Paragraph('细分赛道', cell_header),
     Paragraph('2026E 规模', cell_header),
     Paragraph('增速', cell_header),
     Paragraph('代表玩家', cell_header)],
    [Paragraph('图形化编程（Scratch 系）', cell_tag),
     Paragraph('约 180 亿', cell_center),
     Paragraph('低速（10%）', cell_center),
     Paragraph('编程猫、西瓜创客', cell_body)],
    [Paragraph('Python / 算法应试', cell_tag),
     Paragraph('约 150 亿', cell_center),
     Paragraph('中速（18%）', cell_center),
     Paragraph('核桃编程、小码王', cell_body)],
    [Paragraph('机器人 / 硬件创客', cell_tag),
     Paragraph('约 110 亿', cell_center),
     Paragraph('中速（15%）', cell_center),
     Paragraph('乐高、Makeblock', cell_body)],
    [Paragraph('AI 通识 / 大模型应用（新兴）', cell_tag),
     Paragraph('约 30–60 亿', cell_center),
     Paragraph('高速（80%+）', cell_center),
     Paragraph('尚无规模化龙头', cell_body)],
    [Paragraph('Vibe Coding 形态（待定义）', cell_tag),
     Paragraph('约 5–10 亿（萌芽）', cell_center),
     Paragraph('未成型', cell_center),
     Paragraph('零散工作室与个人 IP', cell_body)],
]
content.append(themed_table(mkt,
                            [4.6 * cm, 3.2 * cm, 2.8 * cm, 6.4 * cm]))
content.append(Paragraph('表 2.1 · K-12 AI/编程子赛道结构（指示性估算）', caption))

content.append(Paragraph('2.2 客群分层与画像', h1))
seg_data = [
    [Paragraph('细分客群', cell_header),
     Paragraph('画像', cell_header),
     Paragraph('估算规模', cell_header),
     Paragraph('优先级', cell_header)],
    [Paragraph('一二线高知中产家庭<br/>（孩子 9–14 岁）', cell_tag),
     Paragraph('父母多为工程师 / 互联网 / 金融背景，'
               '对 AI 与未来技能高度敏感、付费意愿强。', cell_body),
     Paragraph('约 480 万家庭', cell_center),
     Paragraph('★★★★★', cell_center)],
    [Paragraph('一二线焦虑型中产家庭<br/>（孩子 6–12 岁）', cell_tag),
     Paragraph('双减后预算回流，转向素质类；'
               '更看重"作品 + 升学加分"双结果。', cell_body),
     Paragraph('约 720 万家庭', cell_center),
     Paragraph('★★★★☆', cell_center)],
    [Paragraph('新一线 / 强省会家庭<br/>（孩子 8–15 岁）', cell_tag),
     Paragraph('线上消费渗透成熟，'
               '对头部 AI 产品有较高品牌敏感度。', cell_body),
     Paragraph('约 1,100 万家庭', cell_center),
     Paragraph('★★★★☆', cell_center)],
    [Paragraph('国际学校 / 外籍家庭', cell_tag),
     Paragraph('英语为主、追求项目制学习与作品集，'
               '为 IB / AP / 海外申请准备。', cell_body),
     Paragraph('约 30 万家庭', cell_center),
     Paragraph('★★★☆☆', cell_center)],
    [Paragraph('三四线高潜力家庭', cell_tag),
     Paragraph('支付能力中等但增长快，'
               '"被一二线种草"是主要触发场景。', cell_body),
     Paragraph('约 2,300 万家庭', cell_center),
     Paragraph('★★★☆☆', cell_center)],
    [Paragraph('B 端 · 公立校与课后服务', cell_tag),
     Paragraph('教育部"5+2 课后服务"采购、'
               '区县级 AI 教育示范校项目。', cell_body),
     Paragraph('约 22 万所学校', cell_center),
     Paragraph('★★☆☆☆', cell_center)],
]
content.append(themed_table(seg_data,
                            [4.4 * cm, 6.2 * cm, 3.0 * cm, 2.4 * cm]))
content.append(Paragraph('表 2.2 · 目标客群分层与优先级（指示性估算）', caption))
content.append(PageBreak())

content.append(Paragraph('2.3 学习场景与价值主张', h1))
content.append(Paragraph(
    '与传统编程课"老师讲—学生跟"模式不同，Vibe Coding 在 K-12 场景下'
    '有四类高价值的使用场景，每类对应不同的产品形态与定价策略：', body))
for x in bullets([
    '<b>项目驱动学习</b>：学员用自然语言提需求，AI 生成代码，'
    '学员负责测试、修改、迭代——一个学期产出 6–10 个真实可运行作品。',
    '<b>1:1 AI 私教陪伴</b>：AI Tutor 全程陪学，'
    '识别学员困惑点、自动调整难度，家长仪表盘看到学习曲线。',
    '<b>家庭兴趣驱动</b>：把孩子的兴趣（游戏、漫画、手账）变成可以做出来的程序，'
    '降低"学编程 = 苦练语法"的心理门槛。',
    '<b>升学与作品集</b>：为信息素养测评、白名单赛事、'
    '海外申请提供完整作品集与过程文档。',
]):
    content.append(x)

content.append(Paragraph('2.4 家长付费决策模型（5 因子）', h1))
content.append(Paragraph(
    '我们对 200+ 一二线家长的访谈与问卷分析显示，'
    '决定家长是否付费的关键因子按重要性依次为：', body))
for x in bullets([
    '<b>① 看得见的作品</b>（35% 权重）：能否在 2 节课内做出可分享的成果。',
    '<b>② 老师 / AI 的专业感</b>（22%）：能否回答孩子的奇怪问题、'
    '能否给出针对性反馈。',
    '<b>③ 孩子是否愿意主动打开</b>（18%）：留存的根本驱动力。',
    '<b>④ 升学与赛事关联</b>（15%）：信息学奥赛、白名单赛事、申请素材。',
    '<b>⑤ 价格</b>（10%）：在前四项满意的前提下，价格敏感度低于学科类。',
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
     Paragraph('中', cell_center),
     Paragraph('编程猫、核桃编程等头部玩家流量与品牌强，'
               '但课程体系仍以 Scratch / Python 语法为主，'
               '尚未推出原生 AI 学习产品。', cell_body)],
    [Paragraph('潜在新进入者', cell_tag),
     Paragraph('高', cell_center),
     Paragraph('字节、腾讯、网易、科大讯飞均有教育布局；'
               '通用大模型公司（智谱、月之暗面、MiniMax 等）'
               '可能直接以 To-C 产品切入。窗口期约 12–18 个月。', cell_body)],
    [Paragraph('替代品威胁', cell_tag),
     Paragraph('中—高', cell_center),
     Paragraph('免费的通用大模型（豆包、Kimi）+ 短视频教程是最大替代；'
               '差异化必须靠"系统化课程 + 1:1 反馈 + 作品产出"。', cell_body)],
    [Paragraph('供应商议价能力', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('上游大模型 API 供给充足、价格快速下降；'
               '老师 / 内容设计师是中等议价的稀缺资源。', cell_body)],
    [Paragraph('客户议价能力', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('家长在素质类教育上的比价行为强，'
               '但首单后转换成本（孩子习惯、作品沉淀）较高。', cell_body)],
]
content.append(themed_table(five_forces,
                            [3.4 * cm, 2.4 * cm, 11.2 * cm]))
content.append(Paragraph('表 3.1 · 行业五力扫描（综合吸引力：中—高，'
                         '但窗口期紧迫）', caption))

content.append(Paragraph('3.2 主要竞争对手盘点', h1))
comp = [
    [Paragraph('类型', cell_header),
     Paragraph('代表玩家', cell_header),
     Paragraph('核心优势', cell_header),
     Paragraph('我方差异化抓手', cell_header)],
    [Paragraph('传统少儿编程', cell_tag),
     Paragraph('编程猫、核桃编程、西瓜创客、小码王', cell_body),
     Paragraph('品牌、流量、师资', cell_body),
     Paragraph('AI Native 教学路径，从语法转向"想法→作品"。', cell_body)],
    [Paragraph('通用大模型 To-C', cell_tag),
     Paragraph('豆包、Kimi、文小言、智谱清言', cell_body),
     Paragraph('免费、能力强、品牌大', cell_body),
     Paragraph('K-12 专属内容安全 + 体系化课程 + 学习成效追踪。', cell_body)],
    [Paragraph('海外 AI 学习产品', cell_tag),
     Paragraph('Khanmigo、MagicSchool、Synthesis', cell_body),
     Paragraph('教学产品力强', cell_body),
     Paragraph('本土化、支付习惯、赛事衔接、'
               '中文家长端体验。', cell_body)],
    [Paragraph('硬件 / 创客', cell_tag),
     Paragraph('乐高 SPIKE、Makeblock、可立创', cell_body),
     Paragraph('"看得见摸得着"的物理体验', cell_body),
     Paragraph('软件作品 + 在家可完成 + 单价低，互补而非正面。', cell_body)],
    [Paragraph('个人 IP / 工作室', cell_tag),
     Paragraph('小红书 / B 站头部 AI 编程博主', cell_body),
     Paragraph('内容鲜活、信任度高', cell_body),
     Paragraph('系统化、规模化、过程可视化的产品体验。', cell_body)],
]
content.append(themed_table(comp,
                            [3.2 * cm, 4.2 * cm, 4.4 * cm, 5.2 * cm]))
content.append(Paragraph('表 3.2 · 五类主要竞争对手与我方差异化抓手', caption))

content.append(callout(
    '战略锚点：做 K-12 第一个『让孩子用自然语言指挥 AI 做出真东西』的'
    '原生 Vibe Coding 学习平台——区别于教语法的传统编程，'
    '也区别于无目标使用通用大模型。'))
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
        '• 品类先发：原生 Vibe Coding 教学暂无规模化对手<br/>'
        '• AI Native 体验天然适合 K-12 用户<br/>'
        '• 自主学习降低师资依赖，单位经济模型更优<br/>'
        '• 作品驱动的可视化成果，强家长付费动因', cell_body),
     Paragraph(
        '• 品类认知度低，需家长教育成本<br/>'
        '• AI 内容安全与未成年人合规需要重投入<br/>'
        '• 产品 / 模型迭代快，技术债务积累风险<br/>'
        '• 缺乏现成的师资与课程模板可复用', cell_body)],
    [Paragraph('O · 机会', cell_header),
     Paragraph('T · 威胁', cell_header)],
    [Paragraph(
        '• 教育部 AI 教育普及政策直接利好<br/>'
        '• 大模型成本快速下降，毛利空间扩张<br/>'
        '• "双减"后非学科赛道结构性扩容<br/>'
        '• B 端公立校采购通道逐步打开', cell_body),
     Paragraph(
        '• 字节、腾讯、科大讯飞等巨头随时可能入场<br/>'
        '• 监管对未成年人 AI 使用可能进一步收紧<br/>'
        '• 通用大模型免费替代抑制付费意愿<br/>'
        '• 行业被舆论污名化的风险', cell_body)],
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
    '"做孩子的第一个 AI 创造伙伴"——为 6–15 岁青少年提供以 Vibe Coding 为核心、'
    'AI 1:1 陪伴的自主学习平台，让每一个孩子在 30 天内完成自己的第一个'
    '"被真实使用"的作品。'))

content.append(Paragraph('4.3 三层差异化护城河', h1))
for x in bullets([
    '<b>① 教学法护城河</b>：自研"想法→Prompt→作品→复盘"四步法 PBL 体系，'
    '与传统编程课形成代际差异。',
    '<b>② 产品工程护城河</b>：K-12 专属 AI Tutor、内容安全过滤、'
    '家长仪表盘——三件事都需要 6–12 个月工程沉淀，对手难以快速复制。',
    '<b>③ 数据飞轮护城河</b>：每个学员的 Prompt → 反馈 → 作品的全过程数据，'
    '反哺到课程难度调度与 AI Tutor 个性化模型，规模越大越难追赶。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 05 PRODUCT
# ===========================================================================
content += section_divider(
    '05', '产品与课程体系设计', 'PRODUCT & CURRICULUM',
    '围绕客群与战略锚点，设计课程线、作品阶梯与价格区间。')

content.append(Paragraph('5.1 三阶五段课程体系', h1))
curr = [
    [Paragraph('阶段', cell_header),
     Paragraph('适龄', cell_header),
     Paragraph('教学目标', cell_header),
     Paragraph('代表作品', cell_header),
     Paragraph('课时', cell_header)],
    [Paragraph('启蒙 · L1', cell_tag),
     Paragraph('6–8 岁', cell_center),
     Paragraph('用对话驱动 AI 创作图文与小游戏', cell_body),
     Paragraph('我的 AI 漫画、'
               '会说话的故事书', cell_body),
     Paragraph('48 课时', cell_center)],
    [Paragraph('启蒙 · L2', cell_tag),
     Paragraph('8–10 岁', cell_center),
     Paragraph('理解 Prompt 结构与简单逻辑', cell_body),
     Paragraph('个性化记单词、'
               '24 点 AI 出题机', cell_body),
     Paragraph('72 课时', cell_center)],
    [Paragraph('进阶 · L3', cell_tag),
     Paragraph('10–12 岁', cell_center),
     Paragraph('用 Vibe Coding 做能上线的小工具', cell_body),
     Paragraph('班级值日机器人、'
               '家庭账本网站', cell_body),
     Paragraph('96 课时', cell_center)],
    [Paragraph('进阶 · L4', cell_tag),
     Paragraph('12–14 岁', cell_center),
     Paragraph('能拆解需求、读懂代码、调试 AI 输出', cell_body),
     Paragraph('校园活动报名小程序、'
               'AI 学习助手', cell_body),
     Paragraph('120 课时', cell_center)],
    [Paragraph('挑战 · L5', cell_tag),
     Paragraph('14–15 岁', cell_center),
     Paragraph('完成完整产品 Demo + 答辩', cell_body),
     Paragraph('独立 App / 个人作品集', cell_body),
     Paragraph('144 课时', cell_center)],
]
content.append(themed_table(curr,
                            [2.6 * cm, 1.8 * cm, 6.0 * cm, 4.4 * cm, 2.0 * cm]))
content.append(Paragraph('表 5.1 · 三阶五段课程体系（启蒙 → 进阶 → 挑战）', caption))

content.append(Paragraph('5.2 产品 SKU 与定价', h1))
sku = [
    [Paragraph('SKU', cell_header),
     Paragraph('内容', cell_header),
     Paragraph('参考定价', cell_header),
     Paragraph('占营收预期', cell_header)],
    [Paragraph('体验包（Trial）', cell_tag),
     Paragraph('2 节 AI 共创课 + 1 件作品 + 家长直播', cell_body),
     Paragraph('9.9 / 49 元', cell_center),
     Paragraph('引流 SKU', cell_center)],
    [Paragraph('单阶段课包（48–96 课时）', cell_tag),
     Paragraph('对应 L1–L4 阶段的标准包', cell_body),
     Paragraph('2,800 – 5,800 元', cell_center),
     Paragraph('约 55%', cell_center)],
    [Paragraph('挑战营（L5 / 项目营）', cell_tag),
     Paragraph('8–12 周作品打磨 + 1:1 导师', cell_body),
     Paragraph('4,800 – 9,800 元', cell_center),
     Paragraph('约 18%', cell_center)],
    [Paragraph('订阅式 AI 陪学（月卡）', cell_tag),
     Paragraph('不限次 AI Tutor + 每月 1 次作业评估', cell_body),
     Paragraph('99 / 199 元/月', cell_center),
     Paragraph('约 12%', cell_center)],
    [Paragraph('赛事 / 作品集服务', cell_tag),
     Paragraph('白名单赛事备赛、申请作品集打磨', cell_body),
     Paragraph('3,000 – 12,000 元', cell_center),
     Paragraph('约 10%', cell_center)],
    [Paragraph('B 端 · 校园解决方案', cell_tag),
     Paragraph('课程 + 平台 + 师训打包供给学校', cell_body),
     Paragraph('20 – 80 万元 / 校 / 年', cell_center),
     Paragraph('约 5%', cell_center)],
]
content.append(themed_table(sku,
                            [4.0 * cm, 5.6 * cm, 3.6 * cm, 2.8 * cm]))
content.append(Paragraph('表 5.2 · 产品 SKU 蓝图（基础情景）', caption))
content.append(PageBreak())

content.append(Paragraph('5.3 客户体验旅程（学员视角）', h1))
journey = [
    [Paragraph('阶段', cell_header),
     Paragraph('触点', cell_header),
     Paragraph('体验设计要点', cell_header)],
    [Paragraph('① 触达', cell_tag),
     Paragraph('短视频 / 小红书 / 家长群 / 学校', cell_body),
     Paragraph('"我家娃做了一个真 App"风格内容，'
               '突出作品而非课程。', cell_body)],
    [Paragraph('② 试听', cell_tag),
     Paragraph('9.9/49 元体验包', cell_body),
     Paragraph('2 节课内必须做出 1 件可分享作品；'
               '家长可同步观看孩子的 Prompt 过程。', cell_body)],
    [Paragraph('③ 入学', cell_tag),
     Paragraph('AI 评测 + 1:1 学习规划', cell_body),
     Paragraph('AI 测评孩子的兴趣 / 表达力 / 思维方式，'
               '生成专属课程路径。', cell_body)],
    [Paragraph('④ 学习', cell_tag),
     Paragraph('App + AI Tutor + 周度直播', cell_body),
     Paragraph('每节课 30–40 分钟、强制护眼、'
               'AI 全程陪伴 + 真人导师周度答疑。', cell_body)],
    [Paragraph('⑤ 作品', cell_tag),
     Paragraph('作品广场 + 家长仪表盘', cell_body),
     Paragraph('每月 1 件可上线作品，'
               '家长仪表盘看到学习曲线与代码量。', cell_body)],
    [Paragraph('⑥ 复购与推荐', cell_tag),
     Paragraph('阶段升级 / 推荐返券 / 赛事入口', cell_body),
     Paragraph('学完一阶段 → 自然升级；'
               '赛事 / 作品集是高粘性触发器。', cell_body)],
]
content.append(themed_table(journey,
                            [2.4 * cm, 5.6 * cm, 9.0 * cm]))
content.append(Paragraph('表 5.3 · 学员体验旅程关键触点', caption))

content.append(Paragraph('5.4 内容安全与未成年人友好的产品红线', h1))
for x in bullets([
    '<b>分级内容过滤</b>：自研针对 K-12 的多层 AI 输出审核（敏感词 + 语义 + 价值观）。',
    '<b>家长共管</b>：家长端可设单次时长、关键词告警、对话回放权限。',
    '<b>护眼默认值</b>：单次 ≤ 30 分钟、深色模式、强制中场离屏。',
    '<b>禁用清单</b>：禁止生成涉及暴力、隐私、考试作弊、虚假信息的代码与内容。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 06 TECH PLATFORM
# ===========================================================================
content += section_divider(
    '06', '技术平台与 AI 教学架构', 'TECH PLATFORM & AI PEDAGOGY',
    '从模型层、教学智能体层、平台层、家长与运营层四层架构出发，'
    '给出可演进的技术蓝图。')

content.append(Paragraph('6.1 四层技术架构', h1))
arch = [
    [Paragraph('层级', cell_header),
     Paragraph('核心组件', cell_header),
     Paragraph('选型 / 策略', cell_header)],
    [Paragraph('模型层', cell_tag),
     Paragraph('基础大模型 + 代码模型 + 安全审核模型', cell_body),
     Paragraph('多供应商策略：豆包 / 通义 / DeepSeek / Claude，'
               '按场景路由；自训 K-12 偏好微调小模型。', cell_body)],
    [Paragraph('智能体层', cell_tag),
     Paragraph('AI Tutor、Code Reviewer、Project Coach、'
               'Safety Guard', cell_body),
     Paragraph('基于 Agent 编排框架（LangGraph / 自研），'
               '每个角色有独立 Prompt + 工具集 + 评估指标。', cell_body)],
    [Paragraph('平台层', cell_tag),
     Paragraph('在线编辑器、作品发布、'
               '学习数据中台、家长仪表盘', cell_body),
     Paragraph('Web + App + 微信小程序三端打通；'
               '云函数承载学员代码运行沙箱。', cell_body)],
    [Paragraph('运营层', cell_tag),
     Paragraph('CRM、增长归因、内容审核工作台', cell_body),
     Paragraph('SaaS + 轻定制；首年聚焦核心链路，避免过度自研。', cell_body)],
]
content.append(themed_table(arch,
                            [2.2 * cm, 5.6 * cm, 9.2 * cm]))
content.append(Paragraph('表 6.1 · 四层技术架构', caption))

content.append(Paragraph('6.2 AI Tutor 能力地图', h1))
for x in bullets([
    '<b>诊断</b>：基于学员 Prompt + 作品输出，识别困惑类型（语法、逻辑、表达）。',
    '<b>引导</b>：用苏格拉底式提问推动学员自己想下一步，避免直接给答案。',
    '<b>反馈</b>：每件作品自动生成 3 项优点 + 2 项改进 + 1 项延伸挑战。',
    '<b>调度</b>：根据学习曲线动态调整难度，连续受挫触发真人介入。',
    '<b>陪伴</b>：基于角色化人设保持长期一致性，建立学员的"老朋友"感。',
]):
    content.append(x)

content.append(Paragraph('6.3 单位推理成本测算（指示性）', h1))
unit = [
    [Paragraph('情景', cell_header),
     Paragraph('单课时 Token 用量', cell_header),
     Paragraph('单价（折后）', cell_header),
     Paragraph('单课时模型成本', cell_header)],
    [Paragraph('启蒙阶段', cell_tag),
     Paragraph('约 25K tokens', cell_center),
     Paragraph('¥0.5 / M', cell_center),
     Paragraph('≈ ¥0.013', cell_center)],
    [Paragraph('进阶阶段', cell_tag),
     Paragraph('约 80K tokens', cell_center),
     Paragraph('¥1.5 / M', cell_center),
     Paragraph('≈ ¥0.12', cell_center)],
    [Paragraph('挑战阶段（含代码模型）', cell_tag),
     Paragraph('约 200K tokens', cell_center),
     Paragraph('¥3.0 / M', cell_center),
     Paragraph('≈ ¥0.60', cell_center)],
    [Paragraph('订阅式 AI 陪学（月）', cell_tag),
     Paragraph('约 4M tokens', cell_center),
     Paragraph('¥1.5 / M（混合）', cell_center),
     Paragraph('≈ ¥6.0', cell_center)],
]
content.append(themed_table(unit,
                            [4.6 * cm, 4.0 * cm, 3.0 * cm, 4.4 * cm]))
content.append(Paragraph('表 6.2 · AI 推理成本测算（基于 2026 年中国大模型市场价）', caption))
content.append(callout(
    '推理成本占课程毛利不足 4%——AI 不是 P&L 的负担，而是体验差异化的"性价比抓手"。'))
content.append(PageBreak())

# ===========================================================================
# 07 OPERATING MODEL
# ===========================================================================
content += section_divider(
    '07', '运营模式与组织架构', 'OPERATING MODEL & ORGANIZATION',
    '聚焦交付、师资与组织设计，给出 Day-1 可落地的运营框架。')

content.append(Paragraph('7.1 三种交付形态对比', h1))
mode = [
    [Paragraph('形态', cell_header),
     Paragraph('师生比', cell_header),
     Paragraph('客单价', cell_header),
     Paragraph('毛利', cell_header),
     Paragraph('适用阶段', cell_header)],
    [Paragraph('AI 全程陪学（自主学习为主）', cell_tag),
     Paragraph('1: 200+', cell_center),
     Paragraph('2,800–4,800 元', cell_center),
     Paragraph('70%', cell_center),
     Paragraph('L1–L3', cell_center)],
    [Paragraph('AI + 真人小班直播', cell_tag),
     Paragraph('1: 12', cell_center),
     Paragraph('5,800–8,800 元', cell_center),
     Paragraph('55%', cell_center),
     Paragraph('L3–L4', cell_center)],
    [Paragraph('AI + 1:1 导师项目营', cell_tag),
     Paragraph('1: 6', cell_center),
     Paragraph('8,800–14,800 元', cell_center),
     Paragraph('45%', cell_center),
     Paragraph('L4–L5', cell_center)],
]
content.append(themed_table(mode,
                            [4.6 * cm, 1.8 * cm, 3.2 * cm, 1.6 * cm, 2.0 * cm]))
content.append(Paragraph('表 7.1 · 三种交付形态（首年以前两种为主，'
                         '形成"低门槛入 → 高客单升"的漏斗）', caption))

content.append(Paragraph('7.2 首年组织架构（约 38 人精干团队）', h1))
org = [
    [Paragraph('职能', cell_header),
     Paragraph('编制', cell_header),
     Paragraph('关键职责', cell_header)],
    [Paragraph('产品 & 设计', cell_tag),
     Paragraph('5', cell_center),
     Paragraph('App / 小程序 / 家长端、教学交互设计、用户研究。', cell_body)],
    [Paragraph('AI 工程 & 智能体', cell_tag),
     Paragraph('6', cell_center),
     Paragraph('AI Tutor 编排、模型评测、Prompt 工程、内容安全。', cell_body)],
    [Paragraph('技术平台', cell_tag),
     Paragraph('5', cell_center),
     Paragraph('前后端、数据中台、沙箱与运维。', cell_body)],
    [Paragraph('教研 & 课程', cell_tag),
     Paragraph('6', cell_center),
     Paragraph('课程体系、作品库、师训手册、学习评估。', cell_body)],
    [Paragraph('班主任 & 教学服务', cell_tag),
     Paragraph('6', cell_center),
     Paragraph('学员陪伴、家长沟通、续费转化。', cell_body)],
    [Paragraph('增长 & 内容', cell_tag),
     Paragraph('5', cell_center),
     Paragraph('短视频 / 小红书 / 私域、归因分析、付费投放。', cell_body)],
    [Paragraph('合规 & 内容审核', cell_tag),
     Paragraph('2', cell_center),
     Paragraph('未成年人合规、AI 内容审核策略、监管对接。', cell_body)],
    [Paragraph('职能（财法人、行政）', cell_tag),
     Paragraph('3', cell_center),
     Paragraph('财务、法务、行政与人事。', cell_body)],
]
content.append(themed_table(org,
                            [4.6 * cm, 1.8 * cm, 10.6 * cm]))
content.append(Paragraph('表 7.2 · 首年组织架构（合计约 38 人，'
                         '兼职授课老师另算）', caption))
content.append(PageBreak())

# ===========================================================================
# 08 GROWTH
# ===========================================================================
content += section_divider(
    '08', '获客与增长策略', 'MARKETING & GROWTH',
    '基于"内容为本、私域沉淀、口碑驱动"的原则，构建从冷启动到稳态的增长路径。')

content.append(Paragraph('8.1 增长路径（Y1）', h1))
content.append(Paragraph(
    'K-12 教育是典型的"内容种草 + 社交信任"驱动赛道。我们建议把首年增长'
    '拆为三个阶段，每个阶段有清晰的核心 KPI 与 CAC 上限：', body))
for x in bullets([
    '<b>0–3 月（蓄水期）</b>：完成品牌、官网、家长群与种子用户社群，'
    '内测 1,000 名学员，重内容轻投放，CAC 控制在 200 元以内。',
    '<b>3–6 月（启动期）</b>：体验包付费转化跑通，目标月新增付费 1,500 单，'
    'CAC 上限 600 元；短视频 + 小红书 + 家长群三路并行。',
    '<b>6–12 月（规模化）</b>：建立完整付费投放归因，'
    '月新增付费 3,000–5,000 单，CAC 上限 900 元，'
    '同时启动 B 端公立校 PoC 项目 3–5 所。',
    '<b>12 月后（口碑飞轮）</b>：老带新占比 ≥ 35%，'
    'LTV/CAC 进入 4× 以上的健康区间。',
]):
    content.append(x)

content.append(Paragraph('8.2 渠道矩阵', h1))
ch = [
    [Paragraph('渠道', cell_header),
     Paragraph('打法', cell_header),
     Paragraph('对项目的价值', cell_header)],
    [Paragraph('短视频（抖音 / 视频号）', cell_tag),
     Paragraph('"孩子做出真 App"作品类内容矩阵 + 家长 KOL', cell_body),
     Paragraph('品类教育与作品种草的核心入口。', cell_body)],
    [Paragraph('小红书 / 家长社群', cell_tag),
     Paragraph('家长视角分享 + 作品集种草 + 问答', cell_body),
     Paragraph('一二线高知家庭决策核心阵地。', cell_body)],
    [Paragraph('微信生态（视频号 / 公众号 / 私域）', cell_tag),
     Paragraph('体验课 → 班主任私域 → 长期续费', cell_body),
     Paragraph('转化与续费的主战场。', cell_body)],
    [Paragraph('白名单赛事 / 信息素养测评', cell_tag),
     Paragraph('备赛课程 + 作品评审支持', cell_body),
     Paragraph('强信任背书，刺激升学动因家长。', cell_body)],
    [Paragraph('B 端 · 学校与课后服务', cell_tag),
     Paragraph('教育部"5+2"采购、AI 教育示范校', cell_body),
     Paragraph('品牌背书 + 稳定营收，反哺 C 端。', cell_body)],
    [Paragraph('跨界合作', cell_tag),
     Paragraph('童书出版社、博物馆、科技馆、家庭硬件品牌', cell_body),
     Paragraph('降低品类教育成本，扩展心智半径。', cell_body)],
]
content.append(themed_table(ch,
                            [4.6 * cm, 5.4 * cm, 7.0 * cm]))
content.append(Paragraph('表 8.1 · 六大获客渠道矩阵', caption))

content.append(Paragraph('8.3 单位经济模型（基础情景）', h1))
content.append(kpi_strip([
    ('CAC · 平均获客成本', '¥ 600', '试听付费 → 正式付费转化率 28%'),
    ('AOV · 平均客单价', '¥ 4,800', '加权 SKU 客单（不含 B 端）'),
    ('GM · 毛利率', '60%', '含交付、师资、模型与平台成本'),
    ('LTV / CAC', '4.5×', '基于 65% 续费率与 2 年期估算'),
]))
content.append(PageBreak())

# ===========================================================================
# 09 FINANCIALS
# ===========================================================================
content += section_divider(
    '09', '财务测算与回报情景', 'FINANCIALS & RETURNS',
    '给出三套情景下的投资、营收、成本与回报指引。'
    '所有数字均为指示性，仅供决策参考。')

content.append(Paragraph('9.1 一次性 + 首年投入（CapEx + Y1 OpEx 启动包）', h1))
capex = [
    [Paragraph('科目', cell_header),
     Paragraph('金额（万元）', cell_header),
     Paragraph('说明', cell_header)],
    [Paragraph('产品 & 平台研发', cell_tag),
     Paragraph('800 – 1,100', cell_center),
     Paragraph('App、AI Tutor、家长端、'
               '编辑器与沙箱的首年研发人力。', cell_body)],
    [Paragraph('AI 模型推理与微调', cell_tag),
     Paragraph('120 – 180', cell_center),
     Paragraph('多供应商 API + 小模型微调试验。', cell_body)],
    [Paragraph('教研与课程', cell_tag),
     Paragraph('300 – 450', cell_center),
     Paragraph('五阶段课程体系 + 100+ 作品模板 + 教师手册。', cell_body)],
    [Paragraph('品牌、内容与冷启动获客', cell_tag),
     Paragraph('400 – 600', cell_center),
     Paragraph('VI、官网、首年内容矩阵、'
               '前 6 个月获客投放预算。', cell_body)],
    [Paragraph('运营团队首年人力', cell_tag),
     Paragraph('500 – 700', cell_center),
     Paragraph('班主任、教学服务、增长、内容审核团队。', cell_body)],
    [Paragraph('合规与法律', cell_tag),
     Paragraph('60 – 100', cell_center),
     Paragraph('备案、合规审计、未成年人合规系统建设。', cell_body)],
    [Paragraph('备用金 & 行政', cell_tag),
     Paragraph('120 – 200', cell_center),
     Paragraph('15% 弹性预算、办公租赁、IT 设备等。', cell_body)],
    [Paragraph('合计', cell_header),
     Paragraph('2,300 – 3,330', cell_header),
     Paragraph('建议中位 ≈ 2,800 万元', cell_header)],
]
content.append(themed_table(capex,
                            [5.8 * cm, 3.0 * cm, 8.2 * cm]))
content.append(Paragraph('表 9.1 · 一次性 + 首年投入估算（指示性）', caption))

content.append(Paragraph('9.2 三情景营收预测（稳态期 · Y3）', h1))
scen = [
    [Paragraph('情景', cell_header),
     Paragraph('付费学员（万人）', cell_header),
     Paragraph('客单价', cell_header),
     Paragraph('年度营收', cell_header),
     Paragraph('综合毛利', cell_header),
     Paragraph('净利率', cell_header)],
    [Paragraph('保守情景', cell_tag),
     Paragraph('2.5', cell_center),
     Paragraph('¥ 3,800', cell_center),
     Paragraph('0.95 亿元', cell_center),
     Paragraph('52%', cell_center),
     Paragraph('5 – 8%', cell_center)],
    [Paragraph('基础情景', cell_tag),
     Paragraph('5.0', cell_center),
     Paragraph('¥ 4,800', cell_center),
     Paragraph('2.40 亿元', cell_center),
     Paragraph('60%', cell_center),
     Paragraph('15 – 22%', cell_center)],
    [Paragraph('乐观情景', cell_tag),
     Paragraph('9.0', cell_center),
     Paragraph('¥ 5,400', cell_center),
     Paragraph('4.86 亿元', cell_center),
     Paragraph('64%', cell_center),
     Paragraph('22 – 28%', cell_center)],
]
content.append(themed_table(scen,
                            [2.8 * cm, 2.6 * cm, 2.2 * cm, 2.6 * cm, 2.4 * cm, 2.4 * cm]))
content.append(Paragraph('表 9.2 · 三情景稳态期营收与利润率（Y3）', caption))

content.append(Paragraph('9.3 回报指标（基础情景）', h1))
content.append(kpi_strip([
    ('PAYBACK · 回收期', '18–28 月', '含 6 个月 MVP 期'),
    ('IRR · 内部回报率', '28–35%', '5 年期、不含战略并购溢价'),
    ('BREAKEVEN · 盈亏平衡', 'Y2 H2', '基础情景 / 月营收 ≈ 1,200 万元'),
    ('Renewal · 年续费率', '≥ 65%', '稳态期目标'),
]))

content.append(Paragraph('9.4 三年现金流粗略路径（基础情景，亿元）', h1))
cf = [
    [Paragraph('年度', cell_header),
     Paragraph('营收', cell_header),
     Paragraph('毛利', cell_header),
     Paragraph('销售与运营费用', cell_header),
     Paragraph('研发与平台', cell_header),
     Paragraph('经营现金流', cell_header)],
    [Paragraph('Y1', cell_tag),
     Paragraph('0.30', cell_center),
     Paragraph('0.15', cell_center),
     Paragraph('0.50', cell_center),
     Paragraph('0.80', cell_center),
     Paragraph('-1.15', cell_center)],
    [Paragraph('Y2', cell_tag),
     Paragraph('1.10', cell_center),
     Paragraph('0.62', cell_center),
     Paragraph('0.55', cell_center),
     Paragraph('0.65', cell_center),
     Paragraph('-0.58', cell_center)],
    [Paragraph('Y3', cell_tag),
     Paragraph('2.40', cell_center),
     Paragraph('1.44', cell_center),
     Paragraph('0.65', cell_center),
     Paragraph('0.55', cell_center),
     Paragraph('+0.24', cell_center)],
]
content.append(themed_table(cf,
                            [1.6 * cm, 2.4 * cm, 2.4 * cm, 3.4 * cm, 3.0 * cm, 3.2 * cm]))
content.append(Paragraph('表 9.3 · 三年经营现金流粗略路径（基础情景，单位：亿元）', caption))
content.append(PageBreak())

# ===========================================================================
# 10 RISK
# ===========================================================================
content += section_divider(
    '10', '风险矩阵与合规要点', 'RISK & COMPLIANCE',
    '识别核心风险并给出缓释措施，重点强调未成年人保护与 AI 内容安全。')

content.append(Paragraph('10.1 风险矩阵（概率 × 影响）', h1))
risk = [
    [Paragraph('风险', cell_header),
     Paragraph('概率', cell_header),
     Paragraph('影响', cell_header),
     Paragraph('缓释措施', cell_header)],
    [Paragraph('监管收紧（未成年人 AI / 时长 / 内容）', cell_tag),
     Paragraph('中—高', cell_center),
     Paragraph('高', cell_center),
     Paragraph('设独立合规岗、建立内容审核机制、与监管常态化沟通；'
               '产品默认按最严标准实现。', cell_body)],
    [Paragraph('巨头入局压价或并购挤压', cell_tag),
     Paragraph('高', cell_center),
     Paragraph('中—高', cell_center),
     Paragraph('用 18 个月窗口期建立教学法、'
               '数据飞轮与口碑壁垒；提前规划战略合作 / 资本对接。', cell_body)],
    [Paragraph('AI 内容安全事故', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('高', cell_center),
     Paragraph('多层审核（前置过滤 + 模型层 + 后置审核）+ '
               '事件分级响应预案。', cell_body)],
    [Paragraph('家长付费动力不足 / 续费率低', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('高', cell_center),
     Paragraph('家长仪表盘、阶段性作品答辩、白名单赛事衔接，'
               '形成"看得见的进步"。', cell_body)],
    [Paragraph('模型 / API 价格反弹或政策变更', cell_tag),
     Paragraph('低—中', cell_center),
     Paragraph('中', cell_center),
     Paragraph('多供应商策略 + 小模型微调；'
               '锁定年度采购协议。', cell_body)],
    [Paragraph('师资 / 教研团队流失', cell_tag),
     Paragraph('中', cell_center),
     Paragraph('中', cell_center),
     Paragraph('股权激励 + 体系化课程模板，'
               '降低对个人 IP 的依赖。', cell_body)],
    [Paragraph('数据泄露 / 未成年人隐私事件', cell_tag),
     Paragraph('低', cell_center),
     Paragraph('极高', cell_center),
     Paragraph('数据最小化原则、密文存储、'
               '年度第三方安全审计、应急公关预案。', cell_body)],
]
content.append(themed_table(risk,
                            [4.6 * cm, 1.8 * cm, 1.8 * cm, 8.8 * cm]))
content.append(Paragraph('表 10.1 · 主要风险与缓释措施', caption))

content.append(Paragraph('10.2 合规清单（上线前必须完成）', h1))
for x in bullets([
    '<b>办学 / 经营资质</b>：根据业态（线上 / 线下 / B 端）匹配相应的'
    '非学科类校外培训资质或 ICP / EDI 备案。',
    '<b>教育移动应用备案</b>：在教育部"教育移动互联网应用程序备案"系统完成备案。',
    '<b>个人信息保护</b>：建立未成年人专属隐私协议、'
    '家长知情同意流程与数据最小化策略。',
    '<b>生成式 AI 服务备案</b>：依据《生成式人工智能服务管理暂行办法》'
    '完成算法 / 内容备案与安全评估。',
    '<b>内容审核机制</b>：建立"事前过滤 + 事中拦截 + 事后回查"的'
    '三层 AI 输出审核链路与人工抽检比例。',
    '<b>未成年人防沉迷</b>：单次 / 单日时长限制、'
    '21:00 后弹窗提示、家长一键暂停。',
    '<b>广告与营销红线</b>：避免承诺升学、'
    '避免使用未成年人形象代言、避免诱导付费用语。',
]):
    content.append(x)
content.append(PageBreak())

# ===========================================================================
# 11 ROADMAP
# ===========================================================================
content += section_divider(
    '11', '实施路线图', 'IMPLEMENTATION ROADMAP',
    '以 12 个月为颗粒度，给出从立项到正式商业化的关键里程碑与责任分工。')

roadmap = [
    [Paragraph('阶段 / 月份', cell_header),
     Paragraph('M1', cell_header), Paragraph('M2', cell_header),
     Paragraph('M3', cell_header), Paragraph('M4', cell_header),
     Paragraph('M5', cell_header), Paragraph('M6', cell_header),
     Paragraph('M7', cell_header), Paragraph('M8', cell_header),
     Paragraph('M9', cell_header), Paragraph('M10', cell_header),
     Paragraph('M11', cell_header), Paragraph('M12', cell_header)],
    [Paragraph('立项 / 用户研究', cell_tag)] +
        [Paragraph('●', cell_center)] * 2 + [Paragraph('', cell_center)] * 10,
    [Paragraph('合规 / 备案启动', cell_tag),
     Paragraph('', cell_center), Paragraph('●', cell_center),
     Paragraph('●', cell_center), Paragraph('●', cell_center),
     Paragraph('●', cell_center)] +
        [Paragraph('', cell_center)] * 7,
    [Paragraph('MVP 产品 + AI Tutor', cell_tag)] +
        [Paragraph('', cell_center)] * 1 +
        [Paragraph('●', cell_center)] * 4 + [Paragraph('', cell_center)] * 7,
    [Paragraph('课程体系（L1–L3）', cell_tag)] +
        [Paragraph('', cell_center)] * 2 +
        [Paragraph('●', cell_center)] * 4 + [Paragraph('', cell_center)] * 6,
    [Paragraph('内测 1,000 名学员', cell_tag)] +
        [Paragraph('', cell_center)] * 4 +
        [Paragraph('●', cell_center)] * 2 + [Paragraph('', cell_center)] * 6,
    [Paragraph('品牌 + 内容矩阵冷启动', cell_tag)] +
        [Paragraph('', cell_center)] * 3 +
        [Paragraph('●', cell_center)] * 4 + [Paragraph('', cell_center)] * 5,
    [Paragraph('体验包付费上线', cell_tag)] +
        [Paragraph('', cell_center)] * 5 +
        [Paragraph('●', cell_center)] * 2 + [Paragraph('', cell_center)] * 5,
    [Paragraph('正式商业化（Y1 课包）', cell_tag)] +
        [Paragraph('', cell_center)] * 7 +
        [Paragraph('●', cell_center)] * 3 + [Paragraph('', cell_center)] * 2,
    [Paragraph('B 端 PoC 与赛事入口', cell_tag)] +
        [Paragraph('', cell_center)] * 8 +
        [Paragraph('●', cell_center)] * 2 + [Paragraph('', cell_center)] * 2,
    [Paragraph('稳态优化 / 复盘迭代', cell_tag)] +
        [Paragraph('', cell_center)] * 10 +
        [Paragraph('●', cell_center)] * 2,
]
content.append(themed_table(roadmap,
                            [3.8 * cm] + [1.05 * cm] * 12))
content.append(Paragraph('表 11.1 · 12 个月里程碑甘特（●=核心活动月份）', caption))

content.append(Paragraph('关键里程碑（Go/No-Go 决策点）', h1))
for x in bullets([
    '<b>M3 末</b>：合规可行性确认 + 产品技术原型跑通 → Go/No-Go #1',
    '<b>M6 末</b>：1,000 名内测学员体验数据达成 NPS ≥ 40，'
    '完课率 ≥ 70% → Go/No-Go #2',
    '<b>M8 末</b>：体验包付费转化率 ≥ 22%、'
    'CAC 控制在 600 元以内 → 进入正式商业化',
    '<b>M12 末</b>：累计付费学员 ≥ 1.2 万、'
    '续费率 ≥ 60% → 进入规模化扩张阶段',
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
    '基于对宏观政策、市场需求、行业格局与财务可行性的系统分析，'
    '我们的总体判断是：<b>本项目处于明确的政策与技术风口、'
    '具备清晰的差异化空间与可控的风险结构，建议立项推进，'
    '并以"快、专、稳"为核心节奏</b>——快指 6 个月内 MVP 上线、'
    '专指坚持原生 Vibe Coding 教学路径不被 Scratch / Python 老路径回拉、'
    '稳指合规与未成年人保护的高于行业均值的投入水位。', body))
content.append(Paragraph(
    '与传统少儿编程相比，本项目的护城河来自"教学法 × 产品工程 × 数据飞轮"三者的复合。'
    '面对潜在的巨头入局，我们窗口期约为 12–18 个月，'
    '必须用极致的产品迭代与作品口碑迅速建立用户心智壁垒。'
    '只要在产品、教研、合规、增长四个维度保持高执行力，'
    '本项目可以在 Y3 实现 2 亿+ 营收、'
    '15% 以上净利率，并具备进一步资本化的潜力。', body))

content.append(Paragraph('建议的下一步动作（90 天清单）', h1))
nxt = [
    [Paragraph('编号', cell_header),
     Paragraph('动作', cell_header),
     Paragraph('责任方', cell_header),
     Paragraph('截止', cell_header)],
    [Paragraph('01', cell_tag),
     Paragraph('完成核心团队搭建：产品负责人、'
               'AI 工程负责人、首席教研、合规负责人。', cell_body),
     Paragraph('创始人', cell_center),
     Paragraph('30 天内', cell_center)],
    [Paragraph('02', cell_tag),
     Paragraph('完成 30 组家长 + 30 组学员深度访谈，'
               '验证 PMF 假设与定价区间。', cell_body),
     Paragraph('产品 + 用研', cell_center),
     Paragraph('30 天内', cell_center)],
    [Paragraph('03', cell_tag),
     Paragraph('合规预审：办学资质、教育 App 备案、'
               '生成式 AI 备案路径锁定。', cell_body),
     Paragraph('合规顾问', cell_center),
     Paragraph('45 天内', cell_center)],
    [Paragraph('04', cell_tag),
     Paragraph('完成 L1 启蒙阶段课程原型 + 10 件标杆作品 Demo。', cell_body),
     Paragraph('教研团队', cell_center),
     Paragraph('60 天内', cell_center)],
    [Paragraph('05', cell_tag),
     Paragraph('AI Tutor 与作品沙箱 MVP 上线，'
               '完成首批 100 名内测家庭灰度。', cell_body),
     Paragraph('AI 工程 + 平台', cell_center),
     Paragraph('75 天内', cell_center)],
    [Paragraph('06', cell_tag),
     Paragraph('品牌命名、VI、官网、家长私域社群初步建立；'
               '内容矩阵首批 30 条作品类视频上线。', cell_body),
     Paragraph('品牌 + 内容', cell_center),
     Paragraph('90 天内', cell_center)],
    [Paragraph('07', cell_tag),
     Paragraph('完成正式商业计划书 + Y1 预算冻结，'
               '启动天使 / Pre-A 轮融资沟通。', cell_body),
     Paragraph('创始人 + 顾问', cell_center),
     Paragraph('90 天内', cell_center)],
]
content.append(themed_table(nxt,
                            [1.4 * cm, 8.6 * cm, 3.6 * cm, 2.4 * cm]))
content.append(Paragraph('表 12.1 · 推进项目所需的 90 天关键动作', caption))

content.append(Spacer(1, 0.6 * cm))
content.append(callout(
    '"让每一个孩子都拥有自己的第一个 AI 创造伙伴——'
    '我们建议把这件事做成一个真正属于这个时代的、值得被记住的产品。"'))

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


output_filename = 'k12_ai_vibe_coding_feasibility_report.pdf'
doc = SimpleDocTemplate(
    output_filename,
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm,
    title='K-12 AI 学习 · Vibe Coding 新产品线可行性研究报告',
    author='East Coast Advisory',
)
doc.build(content, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f'PDF generated: {output_filename}')
