from ..model import executeSql
from ..const import system,debug
from datetime import datetime

def createTableUser():

    query = ("CREATE TABLE system_users ("
             "system_users_cd serial PRIMARY KEY"
             ",name varchar(30)"
             ",id varchar(30)"
             ",password varchar(30)"
             ",camp_group int"
             ",mail_address char(300)"
             ",introduce_main char(60)"
             ",introduce_sub char(60)"
             ",attack numeric"
             ",Intelligence numeric"
             ",leadership numeric"
             ",assets int"
             ",weapon numeric"
             ",weapon_name text"
             ",filibusters text"
             ",filibusters_kind text"
             ",map_cd int"
             ",config_color varchar(1)"
             ",tab_left varchar(1)"
             ",tab_right varchar(1)"
             ",tab_right_all timestamp"
             ",tab_right_group timestamp"
             ",tab_right_personal timestamp"
             ",time_regist timestamp"
             ",time_update timestamp"
             ");")

    executeSql.executeQuery(query)

def dropTableUser():

    query = ("drop TABLE system_users;")

    executeSql.executeQuery(query)

def createTableChatLogs():

    query = ("CREATE TABLE chat_logs ("
             "chat_logs_cd serial PRIMARY KEY"
             ",system_users_cd serial"
             ",camp_group char(1)"
             ",target_cd int"
             ",remark text"
             ",remark_time timestamp"
             ");")

    executeSql.executeQuery(query)

def dropTableChatLogs():

    query = ("drop TABLE chat_logs;")

    executeSql.executeQuery(query)

def createTableMap():

    query = ("CREATE TABLE Map ("
             "map_cd serial PRIMARY KEY"
             ",latitude_cd int"
             ",longitude_cd int"
             ",image text"
             ",name text"
             ",influence int"
             ",camp_group int"
             ");")

    executeSql.executeQuery(query)

def dropTableMap():

    query = ("drop TABLE Map;")

    executeSql.executeQuery(query)

def insertTableMap():

    query = ("INSERT INTO Map ("
             "latitude_cd"
             ",longitude_cd"
             ",image"
             ",name"
             ",influence"
             ",camp_group"
             ") VALUES ("
             "%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ")")

    strImage1 = ""
    strImage2 = ""
    swi = False
    #swi = True
    if debug.debug:
        strImage1 = "/static/element/map1.png"
        strImage2 = "/static/element/map2.png"
    else:
        strImage1 = "../base.py/static/element/map1.png"
        strImage2 = "../base.py/static/element/map2.png"

    var = 0,0,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,1,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,2,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,3,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,4,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,5,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 0,6,strImage2,"東京拘置所",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

    var = 1,0,strImage2,"千住桜木",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 1,1,strImage2,"元宿さくら公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 1,2,strImage2,"千住箭弓稲荷神社",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 1,3,strImage2,"千住大川町",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 1,4,strImage2,"足立区生涯学習センター",system.INFLUENCE,system.CAMPGROUPMAGIC
    executeSql.executeQueryTupple(query,var)
    var = 1,5,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 1,6,strImage2,"小菅西公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

    var = 2,0,strImage1,"隅田川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,1,strImage2,"千住宮元町",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,2,strImage2,"千住中居町",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,3,strImage2,"北千住駅前通り",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,4,strImage2,"北千住駅",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,5,strImage2,"千住旭公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 2,6,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

    var = 3,0,strImage2,"千住緑町",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 3,1,strImage2,"千住神社",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 3,2,strImage2,"千住警察署",system.INFLUENCE,system.CAMPGROUPPOLICE
    executeSql.executeQueryTupple(query,var)
    var = 3,3,strImage2,"千住東",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 3,4,strImage2,"柳原千草園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 3,5,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 3,6,strImage2,"堀切菖蒲園駅",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

    var = 4,0,strImage2,"千住スポーツ公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 4,1,strImage2,"千住大橋駅",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 4,2,strImage2,"千住仲町公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 4,3,strImage2,"千住関屋町",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 4,4,strImage2,"千住大川端公園",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 4,5,strImage2,"堀切駅",system.INFLUENCE,system.CAMPGROUPGANG
    executeSql.executeQueryTupple(query,var)
    var = 4,6,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

    var = 5,0,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,1,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,2,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,3,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,4,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,5,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)
    var = 5,6,strImage1,"荒川",system.INFLUENCE,None
    executeSql.executeQueryTupple(query,var)

def createTableMST():

    query = ("CREATE TABLE MST ("
             "class_cd int"
             ",kind_cd int"
             ",name text"
             ",order_cd int"
             ");")

    executeSql.executeQuery(query)

def dropTableMST():

    query = ("drop TABLE MST;")

    executeSql.executeQuery(query)

def insertTableMST():

    query = ("INSERT INTO mst ("
             "class_cd"
             ",kind_cd"
             ",name"
             ",order_cd"
             ") VALUES ("
             "%s"
             ",%s"
             ",%s"
             ",%s"
             ")")

    var = 1,0,"====コマンド====",1
    executeSql.executeQueryTupple(query,var)
    var = 1,0,"【通常業務】",2
    executeSql.executeQueryTupple(query,var)
    #var = 1,1,"休暇",2
    #executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDPATROL,"パトロール",3
    executeSql.executeQueryTupple(query,var)
    #var = 1,3,"偵察",4
    #executeSql.executeQueryTupple(query,var)
    #var = 1,5,"接待",6
    #executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDCOMMERCE,"商取引",4
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDTRAINING,"格闘訓練",5
    executeSql.executeQueryTupple(query,var)
    #var = 1,7,"営業",8
    #executeSql.executeQueryTupple(query,var)
    var = 1,0,"【戦闘】",6
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDCALLSOLDIER,"招集",8
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDGUARD,"防衛",9
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDATTACK,"襲撃",10
    executeSql.executeQueryTupple(query,var)
    #var = 1,10,"兵士訓練",11
    #executeSql.executeQueryTupple(query,var)
    var = 1,0,"【その他】",15
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDNULL,"未入力",17
    executeSql.executeQueryTupple(query,var)
    var = 1,system.COMMANDMOVE,"移動",19
    executeSql.executeQueryTupple(query,var)

    var = 2,0,"勢力",1

    executeSql.executeQueryTupple(query,var)

    var = 2,1,"魔法使い",2

    executeSql.executeQueryTupple(query,var)

    var = 2,2,"半グレ",3

    executeSql.executeQueryTupple(query,var)

    var = 2,3,"警察",4

    executeSql.executeQueryTupple(query,var)

    var = 2,None,"無所属",5

    executeSql.executeQueryTupple(query,var)

def createTableNews():

    query = ("CREATE TABLE News ("
             "news_cd serial PRIMARY KEY"
             ",value text"
             ");")

    executeSql.executeQuery(query)

def dropTableNews():

    query = ("drop TABLE News;")

    executeSql.executeQuery(query)

def registerUser(arg,cur=None):

    query = ("INSERT INTO system_users ("
             "name"
             ",id"
             ",password"
             ",camp_group"
             ",attack"
             ",Intelligence"
             ",leadership"
             ",assets"
             ",weapon"
             ",weapon_name"
             ",filibusters"
             ",filibusters_kind"
             ",map_cd"
             ",config_color"
             ",tab_right"
             ",tab_right_all"
             ",tab_right_group"
             ",tab_right_personal"
             ")"
             " Select"
             "  %s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,%s"
             "  ,map_cd"
             "  ,%s"
             "  ,1"
             "  ,now()"
             "  ,'1971-07-13'"
             "  ,'1971-07-13'"
             " From"
             "  Map"
             " Where"
             "  camp_group = %s"
             " Order by"
             "  random() LIMIT 1"
             "")

    # ,系カラムは仕様変更に弱いので、""とする
    var = (str(arg["name"]),
            str(arg["id"]),
            str(arg["password"]),
            str(arg["camp_group"]),
            100,
            100,
            100,
            10000,
            1,
            "警棒",
            "",
            "",
            "1",
            str(arg["camp_group"]))

    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def getUser(arg):
    
    query = ("Select"
             "  Count(1)"
             " From"
             "  system_users"
             " Where"
             "  id = %s"
             " And password = %s")

    var = str(arg["id"]),str(arg["password"])
    
    return executeSql.selectOneQueryTupple(query,var)

def createTableAction():

    query = ("CREATE TABLE action ("
             "system_users_cd serial"
             ",action_num int"
             ",action int"
             ",option varchar(300)"
             ",action_time timestamp"
             ",action_time_in_this_world timestamp"
             ");")

    executeSql.executeQuery(query)

def dropTableAction():

    query = ("drop TABLE action;")

    executeSql.executeQuery(query)

def createTableActionLogs():

    query = ("CREATE TABLE action_logs ("
             "system_users_cd serial PRIMARY KEY"
             ",value text"
             ");")

    executeSql.executeQuery(query)

def dropTableActionLogs():

    query = ("drop TABLE action_logs;")

    executeSql.executeQuery(query)

def createTableTime():

    query = ("CREATE TABLE System_time ("
             " time timestamp"
             ",real_time timestamp"
             ");")

    executeSql.executeQuery(query)

def dropTableTime():

    query = ("drop TABLE System_time;")

    executeSql.executeQuery(query)

def insertTableTime():

    query = ("INSERT INTO System_time ("
             " time"
             ",real_time"
             ") VALUES ("
             "%s"
             ",%s"
             ")")

    var = system.STARTDATE,datetime.now()

    executeSql.executeQueryTupple(query,var)

def createSoldier():

    query = ("CREATE TABLE Soldier ("
             " soldier_cd serial"
             ",name varchar(300)"
             ",speed real"
             ",strength int"
             ",cost int"
             ",morals int"
             ",hardness int"
             ",camp_group int"
             ",Influence int"
             ",flavor char(300)"
             ");")

    executeSql.executeQuery(query)

def dropSoldier():

    query = ("drop TABLE Soldier;")

    executeSql.executeQuery(query)

def insertSoldier():

    query = ("INSERT INTO Soldier ("
             " name"
             ",speed"
             ",strength"
             ",cost"
             ",morals"
             ",hardness"
             ",camp_group"
             ",Influence"
             ",flavor"
             ") VALUES ("
             "%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ")")

    var = "魔獣【桜】",0.8,10,500,5,5,1,100,"近寄りがたい、背中の豪炎"
    executeSql.executeQueryTupple(query,var)
    #var = "魔獣【梅】",0.8,20,5,5,5,1,200,"俺が波を引き起こしたら、どう泳ぐ？見せてみろ"
    #executeSql.executeQueryTupple(query,var)
    var = "魔獣【梅】",0.8,20,700,5,5,1,200,"夜に出歩きたくない理由の一つ"
    executeSql.executeQueryTupple(query,var)
    var = "魔獣【桃】",0.8,50,900,5,5,1,300,"警官隊の一人「なんか空にデカイ豆腐が浮かんでて、しかもビーム撃ってきた」"
    executeSql.executeQueryTupple(query,var)
    var = "魔法少女隊",0.8,70,1100,5,5,1,400,"目が輝いている。力を持った人間は皆そう"
    executeSql.executeQueryTupple(query,var)
    var = "魔女【クシナダヒメ】",1,90,1500,5,5,1,500,"女王は臣下に心を打たれた"
    executeSql.executeQueryTupple(query,var)
    var = "魔女【カムヤタテヒメ】",1.3,140,2000,5,5,1,600,"嘆きはいよいよ耐え切れず泣き始めた。あるべきものが失われ、保つべきものが崩壊し始めたからだ"
    executeSql.executeQueryTupple(query,var)

    var = "私兵【プロテクター装備】",0.8,10,2200,5,5,2,100,"最初は遊びのつもりだった"
    executeSql.executeQueryTupple(query,var)
    var = "私兵【密輸入クロスボウ装備】",0.9,30,2500,5,5,2,200,"撃った後は、ステゴロで突貫！"
    executeSql.executeQueryTupple(query,var)
    var = "私兵【短機関銃装備】",0.9,90,2800,5,5,2,300,"いつまでもあると思うなよ、金金金！"
    executeSql.executeQueryTupple(query,var)
    var = "私兵【突撃銃装備】",0.8,140,3000,5,5,2,400,"心地よい安心感"
    executeSql.executeQueryTupple(query,var)
    var = "PMC",0.9,200,3200,5,5,2,500,"とある魔女「遠くがぴかっと光ったと思ったら、皆が死んだ」"
    executeSql.executeQueryTupple(query,var)
    var = "遊撃特化私兵\n【随伴魔術師による不可視障壁装備】",1.8,100,4000,5,5,2,600,"目的を達する為の、王の右手"
    executeSql.executeQueryTupple(query,var)

    var = "警官隊【White】",0.8,30,700,5,5,3,100,"素晴らしい統率力、素晴らしい忠誠"
    executeSql.executeQueryTupple(query,var)
    var = "警官隊【Red】",0.8,50,1000,5,5,3,200,"腕立て100！背筋100！突撃100！"
    executeSql.executeQueryTupple(query,var)
    var = "警官隊【Blue】",0.8,80,1300,5,5,3,300,"一日の半分を過ぎた。彼らの訓練は続く"
    executeSql.executeQueryTupple(query,var)
    var = "警官隊【Yellow】",0.9,100,1500,5,5,3,400,"妻子ある者のみで構成された、士気の高い警官隊"
    executeSql.executeQueryTupple(query,var)
    var = "SAT",1,200,2000,5,5,3,500,"精鋭というのは、こうあるべき"
    executeSql.executeQueryTupple(query,var)
    var = "戦術遂行室機械化魔道班",2.25,180,3000,5,5,3,600,"公務員魔女を現代テクノロジーで強力サポート！とっても手強いぞ！"
    executeSql.executeQueryTupple(query,var)

def createSoldierPersonal():

    query = ("CREATE TABLE soldier_personal ("
             " soldier_personal_cd int"
             " ,system_users_cd int"
             " ,soldier_cd int"
             " ,number int"
             " ,training int"
             " ,map_cd int"
             " ,guard_number int"
             ");")

    executeSql.executeQuery(query)

def dropSoldierPersonal():

    query = ("drop TABLE soldier_personal;")

    executeSql.executeQuery(query)

def createManageQuest():

    query = ("CREATE TABLE manage_quest ("
             "system_users_cd serial PRIMARY KEY"
             " ,patrol_number int"
             " ,quest_number_001 int"
             " ,call_soldier_number int"
             " ,quest_number_002 int"
             ");")

    executeSql.executeQuery(query)

def dropManageQuest():

    query = ("drop TABLE manage_quest;")

    executeSql.executeQuery(query)

def createMeetingRoom():

    query = ("CREATE TABLE MeetingRoom ("
             "camp_group int"
             ",thread serial"
             ",childNumber int"
             ",title text"
             ",body text"
             ",system_users_cd serial"
             ",body_time timestamp"
             ");")

    executeSql.executeQuery(query)

def dropMeetingRoom():

    query = ("drop TABLE MeetingRoom;")

    executeSql.executeQuery(query)

