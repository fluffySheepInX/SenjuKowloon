from ..const import debug

REDIRECTMAIN = ""
REDIRECTMEETINGROOM = ""
REDIRECTTOP = ""
REDIRECTMOVE = ""
REDIRECTCALLSOLDIER = ""
REDIRECTATTACK = ""
REDIRECTGUARD = ""
if debug.debug:
    REDIRECTMAIN = "/main"
    REDIRECTMEETINGROOM = "/meetingRoom"
    REDIRECTTOP = "/top"
    REDIRECTMOVE = "/commandMove"
    REDIRECTCALLSOLDIER = "/commandCallSoldier"
    REDIRECTATTACK = "/commandAttack"
    REDIRECTGUARD = "/commandGuard"
else:
    REDIRECTMAIN = "/base.py/main"
    REDIRECTMEETINGROOM = "/base.py/meetingRoom"
    REDIRECTTOP = "/base.py/top"
    REDIRECTMOVE = "/base.py/commandMove"
    REDIRECTCALLSOLDIER = "/base.py/commandCallSoldier"
    REDIRECTATTACK = "/base.py/commandAttack"
    REDIRECTGUARD = "/base.py/commandGuard"

# ゲーム開始時刻
STARTDATE = "2019/10/10"

# 戦争開始時刻
STARTWARDATE = "2019/10/26"

# 士官制限
NumberOfRegister = 150

# 入力アクション数
ACTION = 24 * 5

# 削除条件
DELETE = 24 * 7

# 更新間隔
INTERVAL = 0.5

# ゲーム内更新間隔
INTERVALSYSTEM = 8

# 一回の戦闘可能数
COUNTBATTLE = 100

# 統率コスト
COSTLEADERSHIP = 4

NEWSCATEGORY001 = "【連絡】"
NEWSCATEGORY002 = "【戦闘】"
NEWSCATEGORY003 = "【噂話】"
NEWSCATEGORY004 = "【支配】"
NEWSCATEGORY005 = "【撤退】"
NEWSCATEGORY006 = "【統一】"
NEWSRESET = "ゲームデータが初期化されました"
NEWSBATTLE = "{0}が{1}と戦闘、{2}が勝利したようです。詳細は<a href=\"{3}\" target=\"_blank\">こちら</a>"
NEWSREGISTOR = "......という者が千住入りを果たしたようです"
NEWSDOMINATION = "{0}が{1}を掌握したと、噂が街を駆けたようです"
NEWSWITHDRAWAL = "勢力としての{0}は勝負に敗れ、ただ在るだけの存在になったようです......"
NEWSWUNIFICATION = "ついに{0}はこの地での勢力争いに勝利しました。この先何が起こるのかは......神のみぞ知ることでしょう"

# 初期影響数
INFLUENCE = 100

# 所属
CAMPGROUPMAGIC = "1"
CAMPGROUPGANG = "2"
CAMPGROUPPOLICE = "3"

# コマンド
COMMANDPATROL = 2
COMMANDCOMMERCE = 3
COMMANDTRAINING = 4
COMMANDCALLSOLDIER = 5
COMMANDGUARD = 6
COMMANDATTACK = 7
COMMANDNULL = 11
COMMANDMOVE = 12

# マスタ種別
MSTCOMMAND = 1
MSTGROUP = 2

# 資金
GAINFUNDINGMAGIC = 300000
GAINFUNDINGGANG = 1000000
GAINFUNDINGPOLICE = 600000

# 招集のシステム上の上限
LIMITCALLSOLDIER = 999999

GUARDLAST = "LAST"