from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak

# Register a common Chinese font for reportlab.
pdfmetrics.registerFont(TTFont('SimSun', r'C:\Windows\Fonts\simsun.ttc'))

styles = getSampleStyleSheet()
styles['Title'].fontName = 'SimSun'
styles['Title'].fontSize = 24
styles['Title'].leading = 30
styles['Title'].alignment = TA_CENTER
styles['Title'].spaceAfter = 24
styles['Heading1'].fontName = 'SimSun'
styles['Heading1'].fontSize = 16
styles['Heading1'].leading = 22
styles['Heading1'].spaceBefore = 18
styles['Heading1'].spaceAfter = 12
styles['Heading2'].fontName = 'SimSun'
styles['Heading2'].fontSize = 13
styles['Heading2'].leading = 18
styles['Heading2'].spaceBefore = 12
styles['Heading2'].spaceAfter = 8
styles['BodyText'].fontName = 'SimSun'
styles['BodyText'].fontSize = 11
styles['BodyText'].leading = 18
styles['BodyText'].spaceAfter = 8
styles.add(ParagraphStyle(name='Caption', fontName='SimSun', fontSize=10, leading=14, spaceAfter=6))

content = []

content.append(Paragraph('山东日照雪茄吧可行性分析报告', styles['Title']))
content.append(Paragraph('高端咨询风格方案', styles['Caption']))
content.append(Spacer(1, 2 * cm))

content.append(Paragraph('项目背景', styles['Heading1']))
content.append(Paragraph(
    '本报告面向在山东日照开办高端雪茄吧的项目方，立足日照城市发展、消费升级、游客结构与高端休闲零售市场，提供全面的市场分析、定位建议、运营建议、财务测算和风险管控方案。', 
    styles['BodyText']))
content.append(Paragraph('执行摘要', styles['Heading1']))
content.append(Paragraph(
    '日照作为山东沿海重要港口城市，近年来以“海洋、阳光、沙滩、城市”品牌著称，旅游与商务客流稳定增长。值得关注的是，城市高净值人群与商务出行需求同步提升，但高端雪茄社交空间尚未形成闭环。结合本项目定位，日照具备发展 1-2 家高品质雪茄吧的市场基础，尤其在高端酒店商圈、海景休闲板块和城市核心商务区。', 
    styles['BodyText']))
content.append(Paragraph('关键结论', styles['Heading2']))
content.append(Paragraph('1. 市场机会：日照本地及周边城市高消费人群数量持续增长；高端雪茄文化与私人会所需求存在供给缺口。', styles['BodyText']))
content.append(Paragraph('2. 定位建议：打造“东方海岸雪茄吧”，结合精品雪茄、洋酒、雪茄礼仪与私密会谈空间，强调文化体验与尊享服务。', styles['BodyText']))
content.append(Paragraph('3. 选址建议：首选城市商务中心或高端酒店配套区域，次选高端商业综合体或度假酒店旁。', styles['BodyText']))
content.append(Paragraph('4. 经营模式：会员制+预订制+主题沙龙，配套高端洋酒、雪茄鉴赏、雪茄礼盒定制。', styles['BodyText']))
content.append(Paragraph('5. 风险控制：严控装修成本与烟草合法合规，强化服务体验与会员留存。', styles['BodyText']))

content.append(PageBreak())
content.append(Paragraph('一、日照市场环境与消费画像', styles['Heading1']))
content.append(Paragraph(
    '1. 城市概况：日照市位于山东东南沿海，常住人口约 320 万，2025 年地区生产总值约 3400 亿元。海洋资源、港口物流与旅游度假优势明显。', styles['BodyText']))
content.append(Paragraph(
    '2. 经济与客流：旅游旺季客流超过千万，商务出行和会议活动逐年增加，尤其“港口+新能源+旅游”产业链聚集，为高端社交场景提供客源基础。', styles['BodyText']))
content.append(Paragraph(
    '3. 消费升级：近年来日照居民可支配收入逐年上涨，且青岛、日照等城市高端消费人群扩展，酒吧、精品咖啡与高端餐饮持续增长。', styles['BodyText']))
content.append(Paragraph(
    '4. 目标客群：本地企业主、港口与物流高管、旅游度假人群、城市中高端白领、外地商务访客，以及对雪茄文化感兴趣的社交圈层。', styles['BodyText']))

content.append(Paragraph('二、雪茄吧市场需求分析', styles['Heading1']))
content.append(Paragraph('1. 供给缺口', styles['Heading2']))
content.append(Paragraph(
    '目前日照高端社交空间以酒吧、餐厅、酒店为主，真正提供专业雪茄销售与品鉴空间的同类业态极少。该供给缺口为特色雪茄吧提供市场切入点。', styles['BodyText']))
content.append(Paragraph('2. 消费趋势', styles['Heading2']))
content.append(Paragraph(
    '在高端消费人群中，雪茄已成为商务会晤、私密社交和庆祝仪式的重要符号。随着年轻富裕群体的崛起，体验式消费和“私享空间”更加受欢迎。', styles['BodyText']))
content.append(Paragraph('3. 客户偏好', styles['Heading2']))
content.append(Paragraph(
    '- 注重环境私密性与装修质感<br/>'
    '- 希望获得专业建议与定制化服务<br/>'
    '- 对洋酒、雪茄礼盒、配套餐饮有较高接受度<br/>'
    '- 偏好独立包厢、会所式氛围', styles['BodyText']))

content.append(Paragraph('三、竞争分析', styles['Heading1']))
content.append(Paragraph('1. 直接竞争：', styles['Heading2']))
content.append(Paragraph(
    '日照暂无专业雪茄吧，同类业态多为酒吧、酒店大堂吧和茶饮空间，专业性不足。', styles['BodyText']))
content.append(Paragraph('2. 间接竞争：', styles['Heading2']))
content.append(Paragraph(
    '高端酒店、私人会所、洋酒专卖店与商务餐厅构成主要替代品。项目需通过差异化服务和雪茄文化打造独特价值链。', styles['BodyText']))
content.append(Paragraph('3. 市场壁垒：', styles['Heading2']))
content.append(Paragraph(
    '雪茄吧的核心壁垒包括专业选品、雪茄存储环境、服务体验、会员体系与合规审批。早期优势将来自于标准化运营与品牌定位。', styles['BodyText']))

content.append(PageBreak())
content.append(Paragraph('四、定位与产品规划', styles['Heading1']))
content.append(Paragraph('1. 品牌定位', styles['Heading2']))
content.append(Paragraph(
    '建议打造“日照海岸雪茄会”，定位为“东方海岸高端雪茄社交平台”，强调“品味、私享、海岸感”。', styles['BodyText']))
content.append(Paragraph('2. 核心产品线', styles['Heading2']))
content.append(Paragraph(
    '- 雪茄产品：古巴、尼加拉瓜、多米尼加及国产优选雪茄<br/>'
    '- 洋酒搭配：威士忌、白兰地、干邑、白酒单品<br/>'
    '- 轻奢小食：雪茄伴侣、精品巧克力、熟食拼盘<br/>'
    '- 体验服务：雪茄鉴赏、品鉴会、雪茄课程、私人礼盒定制', styles['BodyText']))
content.append(Paragraph('3. 业态模式', styles['Heading2']))
content.append(Paragraph(
    '建议采取会员制+预约制+增值活动模式。会员享受专属包厢、优先预订、定期品鉴活动和主题沙龙。', styles['BodyText']))

content.append(Paragraph('五、选址建议', styles['Heading1']))
content.append(Paragraph('首选位置', styles['Heading2']))
content.append(Paragraph(
    '1. 高端酒店配套：与五星级酒店、特色度假酒店合作，可获得稳定高端客源和品牌背书。<br/>'
    '2. 商务中心：日照市区核心商务区、CBD 邻近写字楼与金融物业，有助于吸引商务洽谈与企事业单位客户。', styles['BodyText']))
content.append(Paragraph('次选位置', styles['Heading2']))
content.append(Paragraph(
    '1. 高端商业综合体：引入咖啡馆、精品店和生活方式品牌同层，形成“品质消费圈”。<br/>'
    '2. 海岸度假区：海景资源可打造差异化体验，但需要更强的运营管理能力。', styles['BodyText']))
content.append(Paragraph('面积建议', styles['Heading2']))
content.append(Paragraph(
    '建议面积 180-260 平方米，包含接待区、雪茄吧台、私密包厢、VIP 房、雪茄存储室及员工备品间。', styles['BodyText']))

content.append(Paragraph('六、运营与服务设计', styles['Heading1']))
content.append(Paragraph('1. 运营组织', styles['Heading2']))
content.append(Paragraph(
    '组建 6-10 人精干团队：店长/总监、雪茄顾问、前台服务、调酒师、食物备餐和仓储管理。强调服务礼仪、产品知识与会员管理。', styles['BodyText']))
content.append(Paragraph('2. 体验环节', styles['Heading2']))
content.append(Paragraph(
    '- 入场：会员预约与礼宾接待<br/>'
    '- 体验：雪茄选购、开盒、点燃、品鉴场景化呈现<br/>'
    '- 情境：定期主题品鉴会、文化沙龙、商务社交晚宴<br/>'
    '- 留存：数据化会员管理、私人礼遇、礼品推荐', styles['BodyText']))
content.append(Paragraph('3. 品质控制', styles['Heading2']))
content.append(Paragraph(
    '严格控制雪茄湿度、温度和存储条件，设立专业雪茄库；建立进货、陈列、销售与退货的全流程标准。', styles['BodyText']))

content.append(PageBreak())
content.append(Paragraph('七、营销与推广策略', styles['Heading1']))
content.append(Paragraph('1. 品牌传播', styles['Heading2']))
content.append(Paragraph(
    '以“海岸+品味+私享”为核心视觉，结合线下高端社交、线上内容与跨业互动，塑造都市尊享生活方式品牌。', styles['BodyText']))
content.append(Paragraph('2. 渠道策略', styles['Heading2']))
content.append(Paragraph(
    '- 私域运营：会员社群、VIP 活动、定向邀约<br/>'
    '- 协作渠道：酒店、会所、商业地产、奢侈品渠道合作<br/>'
    '- 媒体曝光：高端生活方式媒体、社交平台种草、商务关系推荐', styles['BodyText']))
content.append(Paragraph('3. 活动设计', styles['Heading2']))
content.append(Paragraph(
    '策划“雪茄之夜”“海岸品鉴会”“跨界洋酒搭配体验”“老板圈专场”等，强化客户黏性与复购。', styles['BodyText']))

content.append(Paragraph('八、初步财务测算', styles['Heading1']))
content.append(Paragraph('1. 前期投入估算', styles['Heading2']))
content.append(Paragraph(
    '预计装修与设备投入：约 120-180 万元；雪茄与洋酒首批备货：约 60-90 万元；其他开办费用（许可、人员、宣传）：约 30-50 万元。', styles['BodyText']))
content.append(Paragraph('2. 运营成本估算', styles['Heading2']))
content.append(Paragraph(
    '租金与物业：约 25-40 万元/年；人工成本：约 80-120 万元/年；水电与公关推广：约 30-50 万元/年；耗材与折旧：约 20-30 万元/年。', styles['BodyText']))
content.append(Paragraph('3. 收入模型', styles['Heading2']))
content.append(Paragraph(
    '- 雪茄零售与品鉴消费占比 50%<br/>'
    '- 会员费与预订服务占比 25%<br/>'
    '- 洋酒搭配与轻食占比 20%<br/>'
    '- 活动与私属服务占比 5%', styles['BodyText']))
content.append(Paragraph('4. 盈亏平衡', styles['Heading2']))
content.append(Paragraph(
    '若实现月均营业额 70-90 万元，毛利率 55%-60%，则可在 18-24 个月内实现盈亏平衡。重点在于开业首年通过会员拓展和口碑引流迅速提升复购率。', styles['BodyText']))

content.append(Paragraph('九、风险与对策', styles['Heading1']))
content.append(Paragraph('1. 合规风险', styles['Heading2']))
content.append(Paragraph(
    '烟草类经营需遵守《烟草专卖法》与地方政策，必须办理相应许可证，且场所防烟排烟设施符合要求。建议提前咨询当地烟草专卖局与住建部门。', styles['BodyText']))
content.append(Paragraph('2. 市场风险', styles['Heading2']))
content.append(Paragraph(
    '高端雪茄消费本身有一定小众属性，需避免单纯依赖一次性客流，重点打造会员体系与高频体验。', styles['BodyText']))
content.append(Paragraph('3. 运营风险', styles['Heading2']))
content.append(Paragraph(
    '服务与产品体验是雪茄吧核心竞争力。建议引入专业培训、建立标准化流程、并把控环境氛围与细节。', styles['BodyText']))

content.append(PageBreak())
content.append(Paragraph('十、实施路径与建议', styles['Heading1']))
content.append(Paragraph('阶段一：市场定位与选址决策', styles['Heading2']))
content.append(Paragraph(
    '完成项目定位与品牌命名，搜索目标门店，开展可行性调研与成本测算，确定合作酒店或商圈资源。', styles['BodyText']))
content.append(Paragraph('阶段二：设计与筹备', styles['Heading2']))
content.append(Paragraph(
    '委托专业空间设计，明确装修风格与功能分区；制定雪茄选品清单，确定运营团队与供应链伙伴。', styles['BodyText']))
content.append(Paragraph('阶段三：开业与推广', styles['Heading2']))
content.append(Paragraph(
    '实施会员预热、媒体发布、试营业与高端客户邀请方案，快速形成核心用户圈层。', styles['BodyText']))
content.append(Paragraph('阶段四：稳定运营与迭代', styles['Heading2']))
content.append(Paragraph(
    '根据会员反馈调整产品与服务；建立数据化运营分析，每季优化活动、品类与定价。', styles['BodyText']))

content.append(Paragraph('结论', styles['Heading1']))
content.append(Paragraph(
    '综合市场环境、消费趋势与业态缺口分析，日照具备高端雪茄吧项目的可行性。建议以“海岸尊享体验”为核心，优先选择商务/酒店类高端位置，以会员制和主题沙龙为运营引擎，确保首年快速积累稳定客户。', 
    styles['BodyText']))
content.append(Paragraph(
    '本项目若在选址、合规与品牌塑造上保持高度执行力，可成为日照高端社交领域的标杆业态，创造良好的长期回报。', styles['BodyText']))

output_filename = 'cigar_rizhao_feasibility_report.pdf'
doc = SimpleDocTemplate(output_filename, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
doc.build(content)
print(f'PDF generated: {output_filename}')
