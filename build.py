from pathlib import Path
from html import escape
import re
p=Path(__file__).parent
parts=[]
def table(headers,rows):
 return '<div class="scroll"><table><thead><tr>'+''.join('<th>'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td'+(' class="nowrap"' if re.fullmatch(r'[\d,，.＋×＝—%]+(?:美元|美金|个|条|张)?(?:定制主片|品牌共创主片)?',x) else '')+'>'+x+'</td>' for x in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def section(i,title,body):
 parts.append(f'<section id="s{i}"><div class="num">{i:02d}</div><h2>{title}</h2>{body}</section>')
def todo(items):
 return '<ul class="todo">'+''.join('<li>'+escape(x)+'</li>' for x in items)+'</ul>'
section(1,'2026年总结', '<h3>主要靠产品置换，积累网红资源与素材</h3><p>2026年主要做OutfitR、Young两站，几乎都用免费产品置换。视频大多按“安装→推车上架→细节讲解→路测”拍摄。现在已有一批愿意长期合作的网红和产品视频素材，2027年要在此基础上区分OutfitR、Young、Young Pro的内容，丰富拍法，并增加付费品牌合作。</p>'+table(['维度','数据（截至2026年11月2日）','2027年怎么用'],[
 ['合作规模','640次合作，335位网红（已去重）','优先找车型适合、配合度高、审美好的网红再次合作'],
 ['已收到素材','513条独立视频，2,760张照片','总结广告效果好的素材片段和网红，2027年复用并拓展'],
 ['视频播放','758,528次播放，477条可统计视频；单条播放中位数664次','拓展腰部、头部网红，增加品牌曝光与话题度']]))
annual_targets=table(['合作类型','全年名额','品牌分配','主要任务','全年预算'],[
 ['置换','222个','OutfitR、Young、Young Pro各74个，各占置换名额的三分之一','日常广告素材；生活方式、产品解释、真实测试；发布视频并提供可剪辑原片与照片','0美金'],
 ['腰部付费','12个','三品牌合计每月1个，轮流安排；每品牌全年4个','共创定制脚本，解答选型及使用疑问','30,000美元'],
 ['头部付费','6个','每品牌2个；提前联系，配合春夏及黑五发布','品牌主题与人物故事，结合定制评测','48,000美元'],
 ['全年合计','240个','每月合计20个；每品牌全年80个，各占三分之一','按当月广告需求和品牌安排确定合作产品','78,000美元']])+table(['年度交付与评价','计划'],[
 ['计划交付','240条主视频；每个合作名额交付1条。独立照片共1,266张：置换222×5＋腰部12×8＋头部6×10。其他交付内容另外约定'],
 ['照片品牌分配','三个品牌各422张，各占三分之一。每品牌按74个置换×5张＋4个腰部×8张＋2个头部×10张计算'],
 ['可用素材测算','预计置换合作按约定交齐且审核合格的比例为80%，付费为90%；后续争取提高至置换90%、付费95%。按前期逐步提升至全年稳定达到较高比例估算，全年约211—217套可用素材'],
 ['主要评价','内容质量、广告或商品页采用、到站访问、扣除退款后的订单、每套可用素材成本'],
 ['辅助评价','发布满7天、30天及约3个月后的播放与互动']])
annual_targets=annual_targets.replace('<table>','<table class="annual-targets">',1)
section(2,'2027年规划', '<p>2027要让每次合作更有用：拿到能投广告的素材，把产品讲清楚，也让更多目标用户记住品牌。</p><h3>重点改这六件事</h3>'+table(['规划方向','具体安排'],[
 ['三品牌定位','OutfitR围绕户外生活；Young讲清产品选法；Young Pro突出品质、高端体验与产品科普'],
 ['三类脚本','生活方式、产品解释、真实测试；按网红擅长的内容安排，三个品牌各有侧重'],
 ['三类网红分工','置换持续提供日常广告素材；腰部解答购买疑问；头部与品牌共同策划、发布主题视频。全年置换222个、腰部12个、头部6个'],
 ['平台安排','YouTube可拍有氛围感的出行影片、人物与品牌故事，也可做深入讲解和评测；Instagram和TikTok可用短片展示场景、功能与品牌故事。按内容和网红擅长的拍法选择平台'],
 ['市场安排','美国为主，加拿大和澳洲少量试做'],
 ['跟进与调整','每月跟进，每季决定是否继续投入；重点看素材返回数量、质量、实际广告采用、可追踪订单，再辅助看曝光与互动；按实际表现调整预算和续约名单']])+ '<p><b>全年要做到：</b>日常有素材可用，用户看完更容易选对产品，品牌合作让更多目标用户记住品牌。</p><h3>全年合作、任务与预算</h3>'+annual_targets+'<p class="caption">三个品牌作为独立品牌平均分配合作名额，各有内容侧重。全年每品牌80个＝置换74个＋腰部4个＋头部2个。每月合计20个，按7、7、6个轮换，全年各80个；品牌内容定位保持各自侧重。</p>')
section(3,'三个品牌，找谁、拍什么',table(['品牌','合作名额','找什么网红','内容方向'],[
 ['<b>OutfitR</b>','全年80个<br>每月6—7个','骑行、露营、自驾、家庭或伴侣出游作者','置换：装车、营地、骑行场景<br>腰部：结合出行讲功能<br>头部：旅程与人物故事'],
 ['<b>Young</b>','全年80个<br>每月6—7个','电动自行车评测、家庭多车和电动三轮车真实用户','置换：适配、装卸和收纳<br>腰部：型号选择与真实测试<br>头部：围绕用户的出行需求拍完整故事'],
 ['<b>Young Pro</b>','全年80个<br>每月6—7个','双车出行、专业装备评测和注重使用体验的作者','置换：细节与操作<br>腰部：深入评测与体验比较<br>头部：用完整出行故事体现品质和配置价值'],
 ['<b>选人标准</b>','适用范围','筛选要求','补充说明'],
 ['腰部','三个品牌','粉丝10万—25万','三个品牌合计每月1个，轮流安排；每品牌全年4个'],['头部','三个品牌','粉丝25万以上','每品牌全年2个，提前联系并配合发布档期'],
 ['共同要求','所有合作','最近同类视频的通常播放量、目标国家观众、产品适配、拍摄能力和报价','能够拍出自然可信的出行场景、人物互动或完整测试'],
 ['合作产品','所有合作','根据当月广告需求及品牌方安排确定','合作前核实车型与产品适配']]))
import json
selected_videos=json.loads((p/'site_selected_videos.json').read_text())['videos']
reference_html=''
brand_titles={'OutfitR':'户外旅程、家庭出游与露营空间','Young':'重车操作、车型适配与专门选型','Young Pro':'品牌质感、配置细节与便利性证明'}
reference_groups=[]
for brand in ['OutfitR','Young','Young Pro']:
 rows=[]
 for video in selected_videos:
  if video['brand']!=brand:continue
  clips=[]
  for clip in video['clips']:
   url=video['url']+('&t='+str(clip['start']) if 'start' in clip and 'youtube.com/watch?' in video['url'] else '')
   clips.append('<a target="_blank" rel="noopener noreferrer" href="'+escape(url,quote=True)+'">'+escape(clip['time'])+' '+escape(clip['description'])+'</a>')
  original='<a class="video-title" target="_blank" rel="noopener noreferrer" href="'+escape(video['url'],quote=True)+'">'+escape(video['competitor']+'｜'+video['title'])+'</a><div class="video-duration">'+escape(video['duration'])+'</div><div class="video-summary">'+escape(video['original_content'])+'</div><div class="video-clips">'+'<br>'.join(clips)+'</div>'
  rows.append([escape(video['category']),escape(video['tier']),original,escape(video['adaptation'])])
 reference_groups.append((brand,rows))
 reference_html+='<h3>'+brand+'｜'+brand_titles[brand]+'</h3>'+table(['内容类别','合作类型','原视频内容与参考片段','本品牌怎么拍'],rows)
section(4,'内容参考与合作交付',reference_html+'<h3>每次合作交付</h3>'+table(['合作类别','主视频','其他视频素材','独立照片','主要任务'],[
 ['置换','1条','可剪辑原片','5张','日常场景、产品解释、真实使用'],
 ['腰部','1条定制主片','另外约定','8张','共创脚本，讲清购买疑问和操作体验'],
 ['头部','1条品牌共创主片','另外约定','10张','完整故事与品牌主题']]))
section(5,'内容评价', '<h3>交付审核：内容质量</h3>'+table(['检查项目','具体看什么'],[
 ['核心问题','是否讲清适合谁、解决什么问题、怎样操作；是否完成确认脚本的重点'],
 ['产品准确性','车型、装载、安装和功能演示是否准确；是否展示实际操作和使用限制'],
 ['场景与故事','是否拍出自然可信的出行场景，交代去哪、做什么，并有同行者互动或完整测试；是否比通用安装视频更有内容'],
 ['品牌表达','OutfitR是否体现户外生活；Young是否帮助选型；Young Pro是否讲清品质与配置价值'],
 ['画面与声音','主体和操作细节是否清晰；收音、字幕是否准确；场景、功能近景与照片是否充足'],
 ['素材完整性','主视频、原片、照片及另外约定的素材是否交齐；是否有可独立使用的功能片段'],
 ['素材使用条件','交付素材是否具备用于约定广告或商品页的使用许可'],
 ['修改与可用性','反馈是否落实；最终内容可直接用、需修改还是需补拍；与置换内容相比是否减少返工、提高可用性']])+ '<h3>使用评价：实际价值</h3>'+table(['评价项目','具体怎么做'],[
 ['实际采用','统计合格素材中，实际用于广告、商品页或品牌账号的套数及占比；列出采用位置、上线时间和未采用原因'],
 ['到站访问','按网红专属链接统计到站访问；网红发布与品牌广告分别统计'],
 ['有效订单','统计可追踪订单，去重并扣除取消、退款订单；按实际退款情况更新'],
 ['每套可用素材成本','已结算网红费用除以通过审核的素材套数；分别比较置换、腰部和头部，一次合作计一套'],
 ['持续使用','检查素材后续是否仍在使用，是否持续回答购买疑问、带来到站和有效订单'],
 ['合作价值','在同品牌、相近产品和相同使用渠道下，对比内容质量、实际采用、有效订单与成本，判断是否值得续约']])+ '<h3>辅助评价：播放与互动</h3>'+table(['评价项目','具体怎么做'],[
 ['观察时间','发布满7天、30天分别记录，持续跟踪约3个月'],
 ['播放与观看','按平台和长短视频查看播放、观看时长或停留情况'],
 ['互动与评论','查看分享、收藏及评论；整理真实购买疑问、产品误解与使用反馈']]))
brands=['OutfitR','Young','Young Pro']
monthly_quota=[dict(zip(brands, pattern)) for pattern in [(7,7,6),(6,7,7),(7,6,7)]*4]
waist_brands=brands*4
head_brands={1:'OutfitR',2:'Young',4:'Young Pro',5:'OutfitR',8:'Young',9:'Young Pro'}
annual_rows=[]
for brand in brands:
 total=sum(q[brand] for q in monthly_quota)
 annual_rows.append([brand,str(total-6),str(4),str(2),str(total),'10,000美元','16,000美元','26,000美元'])
annual_rows.append(['全年合计','222','12','6','240','30,000美元','48,000美元','78,000美元'])
section(6,'按品牌分配合作与预算',table(['品牌','置换（个）','腰部（个）','头部（个）','全年名额（个）','腰部预算','头部预算','品牌总预算'],annual_rows)+ '<h3>单个预算与合作安排</h3>'+table(['合作类别','单个预算','全年名额','新增合作安排'],[
 ['置换','0美金','222个','每品牌当月名额扣除腰部、头部后，其余全部用于置换'],
 ['腰部','2,500美元','12个','每月1个；三个品牌轮流安排，每品牌全年4个'],
 ['头部','8,000美元','6个','1月OutfitR、2月Young、4月Young Pro、5月OutfitR、8月Young、9月Young Pro；每品牌2个']])+ '<p class="caption">每月合计20个，三个品牌按7、7、6个轮换；全年各80个，置换各74个。合作预算仅含网红合作费，不设备用预算，不含产品、运费和广告投放。</p>')
head_release={1:'2月底—3月发布',2:'3—4月发布',4:'5—6月发布',5:'6—7月发布',8:'9月底—10月上旬发布，黑五复用',9:'10月发布，黑五前完成另外约定的素材'}
publish_plan=[
 '春季内容准备：本月确认的置换及腰部合作，目标2—3月交付发布；OutfitR头部目标2月底—3月发布。',
 '春季内容上线：推动1月项目发布；本月合作目标3—4月发布，Young头部覆盖3—4月。',
 '3月开始放量：推动前期视频按期上线；本月新增合作目标4—5月发布，补充春夏素材。',
 '暑期内容前置：本月新增合作目标5—6月发布，Young Pro头部覆盖暑期前段。',
 '暑期主内容制作：本月新增合作目标6—7月发布；OutfitR头部在暑期上线。',
 '暑期持续发布：跟进4—5月合作上线；本月新增合作目标7—8月发布。',
 '暑期补充内容：推进本月合作在8—9月发布，优先复用已验证有效的网红与拍法。',
 '黑五内容开始准备：Young头部目标9月底—10月上旬发布；另行约定黑五需要的补充素材。',
 '黑五主内容制作：Young Pro头部目标10月发布；9月合作在10—11月前完成，避免黑五临时开拍。',
 '旺季收尾、黑五备片：前期合作完成成片与另外约定的素材；本月新增以低预算合作为主，目标11—12月发布。',
 '黑五发布与复用：集中推进已完成内容发布、转发和广告使用；本月新增腰部不承担黑五主内容制作。',
 '淡季复盘与次年准备：完成跨年项目沟通，本月新增合作用于次年春季储备。']
work=[
 ['与优化师确认3月起量需要的场景、卖点和脚本优先级','筛选三品牌网红，完成询价、适配核实及合作确认','与OutfitR头部打磨脚本、镜头和交付时间，锁定2月底—3月发布','逐位确认寄样进度与拍摄排期，准备后续腰部及头部候选名单'],
 ['逐位推进1月项目收稿、修改和发布，确认春季可用素材','与Young头部确认选型方向、脚本和3—4月发布时间','与优化师检查首批素材的广告采用及测试反馈，调整新一轮拍摄说明','核对专属链接，补齐已发布视频的7天、30天数据'],
 ['推动春季视频按期发布，跟进未交稿、修改与补拍项目','与优化师复盘首批广告素材，确认4—5月需要强化的卖点和拍法','推进当月网红邀约、脚本及拍摄，提前联系暑期头部候选','统计素材采用、专属链接到站及扣除退款后的订单，比较置换与付费内容'],
 ['与Young Pro头部打磨配置价值和真实使用脚本，锁定5—6月发布','推进暑期置换、腰部合作，明确主视频、另外约定的素材和返稿时间','与优化师筛选可继续放大的内容，统一反馈给网红修改','跟踪已发布内容的采用、广告效果与有效订单'],
 ['与OutfitR头部确认暑期出行故事、拍摄镜头和6—7月发布时间','逐位催收暑期首批素材，集中完成审片、修改和发布确认','与优化师复盘功能片段表现，把有效要求带入后续脚本','跟进专属链接到站、有效订单和每套可用素材成本'],
 ['确保4—5月合作按暑期档期发布，处理收稿和修改延期','推进7—8月补充合作，优先联系配合度好、素材被采用的网红','与优化师复盘上半年网红广告表现，确定续约和脚本优化方向','汇总三品牌、三类合作的素材质量、采用、到站、有效订单和费用'],
 ['持续跟进暑期网红返稿、修改和发布，补充有效内容','与优化师确认暑期仍需要的场景和卖点，指导下一批脚本','筛选8—9月黑五项目人选，提前询价和锁定拍摄档期','监测已发布合作的播放、广告采用、到站和有效订单'],
 ['与优化师及品牌方确认黑五内容需求和发布时间','完成Young头部邀约与脚本，约定9月底—10月上旬发布，另行确认黑五所需素材','提前沟通Young Pro头部的9月合作，锁定返稿和10月发布时间','跟进暑期合作收尾，复盘网红素材的广告表现和续约价值'],
 ['与Young Pro头部确认脚本、镜头和10月发布排期','催收黑五主视频及另外约定的素材，逐项确认修改和最终交付时间','与优化师检查已回收素材，按广告反馈与网红沟通修改','跟进Young头部发布及数据，确认黑五期间内容使用安排'],
 ['推动8—9月付费项目完成发布、修改及另外约定的素材交付','与优化师逐条确认黑五实际采用的网红素材，及时协调补充或修改','逐位确认网红黑五发布、转发时间及专属链接','推进当月置换与腰部合作，避免临时新增高预算头部项目'],
 ['按已确认时间推进黑五内容发布、转发与网红沟通','与优化师跟踪网红素材广告表现，及时沟通必要的内容调整','监测专属链接到站、有效订单及退款更新，汇总合作表现','完成当月置换和腰部邀约，沟通次年春季内容储备'],
 ['完成年度未交稿、修改和跨年发布项目的逐位跟进','与优化师复盘三品牌网红内容的质量、采用、广告表现和成本','确定次年续约人选与需优化的脚本方向，提前沟通春季档期','汇总全年网红费用、到站及扣除退款后的订单，更新跨年项目状态']]
monthly=[]
monthly_html=''
for month in range(1,13):
 wb=waist_brands[month-1];hb=head_brands.get(month);brand_quota=monthly_quota[month-1]
 rows=[]
 for brand in brands:
  waist=int(wb==brand);head=int(hb==brand);swap=brand_quota[brand]-waist-head
  waist_fee=waist*2500;head_fee=head*8000
  rows.append([brand,str(swap),str(waist),str(head),str(brand_quota[brand]),f'{waist_fee:,}美元',f'{head_fee:,}美元',f'{waist_fee+head_fee:,}美元'])
 head_count=int(hb is not None);fee=2500+head_count*8000
 rows.append(['当月合计',str(19-head_count),'1',str(head_count),'20','2,500美元',f'{head_count*8000:,}美元',f'{fee:,}美元'])
 monthly.append(rows)
 monthly_html+='<article class="month"><div class="month-heading"><h3>'+str(month)+'月</h3><span>20个名额 · 新增合作预算 '+f'{fee:,}'+'美元</span></div>'+'<p class="release-plan">'+publish_plan[month-1]+'</p>'+table(['品牌','置换（个）','腰部（个）','头部（个）','总名额（个）','腰部预算','头部预算','品牌预算合计'],rows)+'<div class="month-tasks"><h4>网红运营待办</h4>'+todo(work[month-1])+'</div></article>'
section(7,'2027年逐月安排','<p>3月开始起量，暑期集中销售，10月后逐渐转淡，11月配合黑五。合作提前推进，春夏及黑五所需内容先完成脚本、拍摄和交付，再按档期发布。</p><p class="caption">下表名额与预算按新增合作安排；发布时间另列。费用按合作项目预估，实际付款按合同节点执行。</p>'+monthly_html)
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f3f2ed;color:#243c38;font:15px/1.85 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}header{background:#163e37;color:#fff;padding:64px max(6vw,24px) 48px}header small{letter-spacing:3px;color:#b5c6b9}h1{font-size:44px;line-height:1.25;font-weight:650;margin:18px 0}header p{color:#cfdbd5;max-width:800px}.status{display:inline-block;border:1px solid #9db1a0;padding:5px 12px;border-radius:4px;font-size:12px}nav{position:sticky;top:0;background:#fffef9ed;backdrop-filter:blur(10px);padding:12px 5vw;display:flex;gap:20px;flex-wrap:wrap;border-bottom:1px solid #dce2db;z-index:2}nav a{font-size:13px}a{color:#246b59;text-underline-offset:4px}nav a{text-decoration:none}main{max-width:1540px;padding:32px 36px 70px;margin:auto}section{position:relative;padding:40px;background:#fffefa;border:1px solid #e1e5dc;border-radius:12px;margin-bottom:24px;scroll-margin-top:100px}.num{font-size:12px;color:#8e7844;letter-spacing:2px}h2{font-size:27px;margin:5px 0 10px}h3{font-size:18px;margin:26px 0 8px}.intro{font-size:16px;color:#687a70;margin:0 0 24px}.scroll{overflow-x:auto;margin:16px 0}table{border-collapse:separate;border-spacing:0;width:100%;min-width:680px;font-size:15px;line-height:1.8;border:1px solid #dfe6dc;border-radius:8px;overflow:hidden}th{text-align:left;background:#eaf0e8;color:#284b3f;font-weight:600}td,th{padding:18px 20px;border-bottom:1px solid #e4e9df;vertical-align:top}tbody tr:last-child td{border-bottom:0}td:first-child{min-width:125px}tbody tr:nth-child(even){background:#f8faf5}.note{background:#f5f0df;border-left:3px solid #aa9154;padding:15px 18px;margin:20px 0;font-size:13px;color:#655c40}details{border-top:1px solid #dfe5db;padding:16px 0;margin-top:22px}summary{font-weight:600;cursor:pointer}li{padding:5px 0}.todo{list-style:none;padding:0;margin:0;min-width:0}.todo li{position:relative;padding:4px 0 4px 20px;line-height:1.7}.todo li:before{content:"☐";position:absolute;left:0;color:#7a8b77}.scroll table th{white-space:nowrap}button{border:0;background:#294e41;color:#fff;padding:8px 14px;border-radius:4px;cursor:pointer}footer{text-align:center;color:#718278;font-size:12px;padding:0 20px 35px}.caption{font-size:13px;color:#6e7f73;margin:14px 0}.month{margin:30px 0 42px;padding:24px;border:1px solid #dce5d7;border-radius:12px;background:#fff}.month-heading{display:flex;align-items:center;justify-content:space-between;gap:15px;border-bottom:1px solid #e2e8dd;padding-bottom:14px;margin-bottom:20px}.month-heading h3{font-size:24px;margin:0}.month-heading span{color:#527461;font-size:14px}.month .scroll{margin:0 0 20px}.month table,#s6>.scroll:first-of-type table{table-layout:fixed;min-width:960px}.month th,.month td,#s6>.scroll:first-of-type th,#s6>.scroll:first-of-type td{text-align:right;white-space:nowrap;padding:16px 12px;font-variant-numeric:tabular-nums}.month th:first-child,.month td:first-child,#s6>.scroll:first-of-type th:first-child,#s6>.scroll:first-of-type td:first-child{text-align:left;width:15%;min-width:0}.month th:nth-child(n+2):nth-child(-n+5),.month td:nth-child(n+2):nth-child(-n+5),#s6>.scroll:first-of-type th:nth-child(n+2):nth-child(-n+5),#s6>.scroll:first-of-type td:nth-child(n+2):nth-child(-n+5){width:8%}.month tbody tr:last-child,#s6>.scroll:first-of-type tbody tr:last-child{font-weight:650;background:#eaf1e5}.release-plan{padding:14px 18px;margin:0 0 20px;border-left:3px solid #9cae82;background:#f5f7ee;color:#486044}.month-tasks{background:#f6f8f1;padding:18px 22px;border-radius:8px}.month-tasks h4{font-size:14px;margin:0 0 7px;color:#3e624d}.month .todo li{padding-top:5px;padding-bottom:5px}#s4 th:first-child{width:15%}#s4 th:nth-child(2){width:9%}#s4 th:nth-child(3){width:40%}#s4 th:nth-child(4){width:36%}#s4>.scroll:last-child th{width:auto}#s4 a{display:inline-block;margin:2px 0}#s4 .video-title{font-weight:600}#s4 .video-duration{font-size:12px;color:#738274;margin:2px 0 8px}#s4 .video-summary{margin:0 0 10px}#s4 .video-clips{border-top:1px solid #e2e8dc;padding-top:8px;font-size:13px;line-height:1.7}#s4 table{min-width:900px}#s4>.scroll:last-child table{min-width:680px}#s2 table.annual-targets{min-width:1000px;table-layout:fixed}#s2 table.annual-targets th:nth-child(1){width:13%}#s2 table.annual-targets th:nth-child(2){width:10%}#s2 table.annual-targets th:nth-child(3){width:25%}#s2 table.annual-targets th:nth-child(4){width:34%}#s2 table.annual-targets th:nth-child(5){width:18%}#s2 table.annual-targets td:nth-child(1),#s2 table.annual-targets td:nth-child(2),#s2 table.annual-targets td:nth-child(5){white-space:nowrap;word-break:keep-all;overflow-wrap:normal}#s2 table.annual-targets td:nth-child(5){font-variant-numeric:tabular-nums;padding-left:14px;padding-right:14px}#s3 table{table-layout:fixed;min-width:1000px}#s3 th:nth-child(1){width:14%}#s3 th:nth-child(2){width:14%}#s3 th:nth-child(3){width:32%}#s3 th:nth-child(4){width:40%}#s3 td:first-child,#s4 td:nth-child(-n+2),#s6 td:first-child{white-space:nowrap}#s4 th:nth-child(1){width:13%}#s4 th:nth-child(2){width:12%}#s4 th:nth-child(3){width:39%}#s4 th:nth-child(4){width:36%}#s4>.scroll:last-child th{width:auto} @media(max-width:700px){header{padding:35px 24px}h1{font-size:32px}main{padding:16px 12px}section{padding:22px 18px}h2{font-size:23px}nav{position:static;gap:13px}.month{padding:14px;margin:24px 0}.month-heading{align-items:flex-start}.month-heading h3{font-size:22px}.month-heading span{font-size:12px}.month-tasks{padding:14px}table{font-size:13px}td,th{padding:12px}}@media print{@page{size:A4 landscape;margin:14mm}body{background:white;font-size:10pt}header{padding:20px;color:#163e37;background:white}header p,header small{color:#456154}h1{font-size:27pt}nav,button{display:none}main{padding:0;max-width:none}section{padding:14px 0;border:0;border-radius:0;margin:0 0 15px}h2{font-size:18pt;break-after:avoid}.scroll{overflow:visible}table{min-width:0;font-size:9pt}.month{padding:14px;margin:15px 0;break-inside:avoid}.month table,#s6>.scroll:first-of-type table,#s4 table,#s4>.scroll:last-child table{min-width:0}.month th,.month td,#s6>.scroll:first-of-type th,#s6>.scroll:first-of-type td{padding:8px;font-size:9pt}.month-heading{padding-bottom:8px;margin-bottom:10px}.month-heading h3{font-size:16pt}.month-tasks{padding:10px 15px}td,th{padding:8px}tr,.note{break-inside:avoid}thead{display:table-header-group}a{color:inherit}footer{display:none}}'''
css+='''
/* Keep complete labels, headings and numeric values on one line throughout. */
th,td:first-child,td.nowrap{white-space:nowrap!important;word-break:keep-all!important;overflow-wrap:normal!important}
table:not(.annual-targets){table-layout:auto}td:first-child{min-width:max-content}
#s2>.scroll:not(:has(.annual-targets)) td:first-child{width:180px;min-width:180px}
#s1 td:first-child,#s5 td:first-child{min-width:155px}
@media(max-width:700px){#s2>.scroll:not(:has(.annual-targets)) td:first-child{min-width:150px;width:150px}}
'''
nav=''.join(f'<a href="#s{i}">{name}</a>' for i,name in enumerate(['今年成果','年度目标','品牌方向','参考与交付','内容评价','预算','逐月安排'],1))
html='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Forcome｜2026成果与2027年度网红规划</title><style>'+css+'</style></head><body><header><small>FORCOME · 2027 ANNUAL PLAN</small><h1>2026成果与2027年度网红规划</h1><span class="status">全年240个合作名额 · 腰部12个 · 头部6个 · 合作预算78,000美元</span></header><nav>'+nav+'<button onclick="window.print()">打印 / 保存PDF</button></nav><main>'+''.join(parts)+'</main></body></html>'
(p/'index.html').write_text(html)
print('Written',len(html),'characters')
