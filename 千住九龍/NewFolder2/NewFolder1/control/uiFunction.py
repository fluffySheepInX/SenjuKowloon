from ..model import executeSql
from ..const import sql
from ..const import ui
from ..const import system
from datetime import datetime, timedelta

# map
def createMap():
    
    result = getMap()

    num = 1
    html = "<table class=\"map\" border=\"5\" bordercolor=\"white\" align=\"center\"><tr>"
    
    for x in result:
        html = html + "<td>"
        html = html + "<div class=\"mapImage\">"
        html = html + " <img src=" + str(x[3])
        html = html + " alt=\"" + str(x[1]) + "-" + str(x[2]) + "：" + str(x[4]) + "\""
        html = html + " title=\"" + str(x[1]) + "-" + str(x[2]) + "：" + str(x[4]) + "\""
        html = html + " />"
        html = html + "<p>"
        if x[5] != None:
            html = html + str(x[5])[0]
            pass
        html = html + "</p>"
        html = html + str(x[1]) + "-" + str(x[2])
        html = html + "</div>"
        html = html + "</td>"
        if num != 1 and num % ui.MAPLONGITUDE == 0:
            html = html + "</tr><tr>"
        num += 1

    html = html + "</tr></table>"
    return html

def getMap():
    
    query = ("Select"
             "  map.map_cd"
             "  ,map.latitude_cd"
             "  ,map.longitude_cd"
             "  ,map.image"
             "  ,map.name"
             "  ,mst.name"
             " From"
             "  map"
             " Left join"
             "  mst"
             " On map.camp_group = mst.kind_cd"
             " And mst.class_cd = 2"
             " Order by"
             "  latitude_cd"
             " ,longitude_cd"
             "  ")

    result = executeSql.selectAllQuery(query)

    return result

def createCurrentLocation(args):
    
    result = getCurrentLocation(args)

    html = ""
    html = html + "<table class=\"currentLocation\" border=\"5\" bordercolor=\"white\" align=\"center\">"
    html = html + "<tr>"
    html = html + "    <td rowspan=\"3\">XXXXXXXXXXXXXXX</td>"
    html = html + "    <td>"
    html = html + "貴方は【" + str(result[2]) + "】（座標：" + str(result[0]) + "-" + str(result[1]) + "）に居ます。"
    html = html + "    </td>"
    html = html + "</tr>"
    html = html + "<tr>"
    html = html + "    <td>"
    html = html + "【" + str(result[2]) + "】の最大勢力：" + str(result[4])
    html = html + "    </td>"
    html = html + "</tr>"
    html = html + "<tr>"
    html = html + "    <td>"
    html = html + "【" + str(result[2]) + "】での影響力：" + str(result[3])
    html = html + "    </td>"
    html = html + "</tr>"
    html = html + "</table>"

    return html

def getCurrentLocation(args):

    query = ("Select"
             "  map.latitude_cd"
             "  ,map.longitude_cd"
             "  ,map.name"
             "  ,map.influence"
             "  ,mst.name"
             " From"
             "  system_users"
             " Inner join"
             "  map"
             " On"
             "  system_users.map_cd = map.map_cd"
             " Left join"
             "  mst"
             " On"
             "  mst.kind_cd = map.camp_group"
             " And"
             "  mst.class_cd = %s"
             " WHERE"
             "  system_users_cd = %s")

    var = system.MSTGROUP,(args["system_users_cd"])
    
    return executeSql.selectOneQueryTupple(query,var)

# chat
def createChatGroup(args):
    
    result = getChatGroup(args)

    html = ""
    for x in result:
        html = html + "<table class=\"getChatGroup\" border=\"5\" bordercolor=\"white\" align=\"center\">"
        
        html = html + "<tr>"
        html = html + "<td>" + str(x[2]) + "</td>"
        html = html + "<td>" + str(x[1]) + "</td>"
        html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<td colspan=\"2\">" + str(x[0]) + "</td>"
        html = html + "</tr>"
        
        html = html + "</table>"

    return html

def createChatAll(args):
    
    result = getChatAll(args)

    html = ""
    for x in result:
        html = html + "<table class=\"getChatAll\" border=\"5\" bordercolor=\"white\" align=\"center\">"
        
        html = html + "<tr>"
        html = html + "<td>" + str(x[2]) + "</td>"
        html = html + "<td>" + str(x[1]) + "</td>"
        html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<td colspan=\"2\">" + str(x[0]) + "</td>"
        html = html + "</tr>"
        
        html = html + "</table>"

    return html

def createChatPrivate(args):
    
    result = getChatPrivate(args)

    html = ""
    for x in result:
        html = html + "<table class=\"getChatPrivate\" border=\"5\" bordercolor=\"white\" align=\"center\">"
        
        html = html + "<tr>"
        html = html + "<td>" + str(x[2]) + "</td>"
        html = html + "<td>" + str(x[1]) + "</td>"
        html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<td colspan=\"2\">" + str(x[0]) + "</td>"
        html = html + "</tr>"
        
        html = html + "</table>"

    return html

def getChatGroup(args):

    query = ("Select"
             "  chat_logs.remark"
             "  ,chat_logs.remark_time"
             "  ,system_users.name"
             " From"
             "  chat_logs"
             " Inner join"
             "  system_users"
             " On"
             "  chat_logs.system_users_cd = system_users.system_users_cd"
             " WHERE"
             "  chat_logs.camp_group = %s"
             " ORDER BY"
             "  chat_logs_cd desc"
             " LIMIT"
             "  %s")

    var = str(args["camp_group"]),sql.CHATLIMIT
    
    return executeSql.selectAllQueryTupple(query,var)

def getChatAll(args):

    query = ("Select"
             "  chat_logs.remark"
             "  ,chat_logs.remark_time"
             "  ,system_users.name"
             " From"
             "  chat_logs"
             " Inner join"
             "  system_users"
             " On"
             "  chat_logs.system_users_cd = system_users.system_users_cd"
             " WHERE"
             "  chat_logs.camp_group is null"
             " AND target_cd is null"
             " ORDER BY"
             "  chat_logs_cd desc"
             " LIMIT"
             "  %s")

    var = sql.CHATLIMIT,
    
    return executeSql.selectAllQueryTupple(query,var)

def getChatPrivate(args):

    query = ("Select"
             "  chat_logs.remark"
             "  ,chat_logs.remark_time"
             "  ,system_users.name"
             " From"
             "  chat_logs"
             " Inner join"
             "  system_users"
             " On"
             "  chat_logs.system_users_cd = system_users.system_users_cd"
             " WHERE"
             "  chat_logs.camp_group is null"
             " AND target_cd is not null"
             " ORDER BY"
             "  chat_logs_cd desc"
             " LIMIT"
             "  %s")

    var = sql.CHATLIMIT,
    
    return executeSql.selectAllQueryTupple(query,var)

# command
def createCommand():

    result = getCommand()

    html = "<select name=\"command\" size=" + ui.LIST + ">"

    for x in result:
        if str(x[1]) == "0":
            html = html + "<option value=" + str(x[1]) + " disabled>" + str(x[2]) + "</option>"
        else:
            html = html + "<option value=" + str(x[1]) + ">" + str(x[2]) + "</option>"

    html = html + "</select>"

    return html

def getCommand():

    query = ("Select"
             "  *"
             " From"
             "  mst"
             " WHERE"
             "  class_cd = %s"
             " ORDER BY"
             "  order_cd")

    var = 1,
    
    return executeSql.selectAllQueryTupple(query,var)

# action
def createAction(args):
    
    result = getAction(args)

    resultGetSystemTime = getSystemTime()

    html = "<select name=\"action\" size=" + ui.LIST + " multiple>"

    count = 0
    for x in result:
        count = count + 1
        calc = resultGetSystemTime[0][0] + timedelta(hours=count * system.INTERVALSYSTEM)

        resultGetSoldier = [None,None]
        if x[4] == system.COMMANDCALLSOLDIER:
            arg = {"system_users_cd":args["system_users_cd"],
                  "action_num":x[0]}
            result = getActionOption(arg)
            resultSplit = result[0][0].split(",")
            arg = {"soldier_cd":resultSplit[0]}
            resultGetSoldier = getSoldierBySoldierCd(arg)
            pass
        elif x[4] == system.COMMANDMOVE:
            arg = {"system_users_cd":args["system_users_cd"],
                  "action_num":x[0]}
            result = getActionOption(arg)
            resultSplit = result[0][0]
            arg = {"map_cd":resultSplit}
            resultMap = getMapByMapCd(arg)
            pass
        elif x[4] == system.COMMANDATTACK:
            arg = {"system_users_cd":args["system_users_cd"],
                  "action_num":x[0]}
            result = getActionOption(arg)
            resultSplit = result[0][0].split(",")
            arg = {"map_cd":resultSplit[0]}
            resultMap = getMapByMapCd(arg)
            pass

        html = html + "<option value=" + str(x[0]) + ">"
        html = html + "No." + str(count).zfill(2) + ":" 

        if x[4] == system.COMMANDCALLSOLDIER:
            html = html + str(x[1]) + "(" + resultGetSoldier[1] + "," + resultSplit[1] + ")" + "："
            pass
        elif x[4] == system.COMMANDMOVE:
            html = html + str(x[1]) + "：" + str(resultMap[sql.MAP_NAME]) + "(" + str(resultMap[sql.MAP_LATITUDE_CD]) + "-" + str(resultMap[sql.MAP_LONGITUDE_CD]) + ")" + "へ"
            pass
        elif x[4] == system.COMMANDATTACK:
            html = html + str(x[1]) + "：" 
            html = html + str(resultMap[sql.MAP_NAME]) + "("
            html = html + str(resultMap[sql.MAP_LATITUDE_CD]) + "-" 
            html = html + str(resultMap[sql.MAP_LONGITUDE_CD]) + ")" + "へ："
            html = html + "No." + resultSplit[1] + "の兵を使う"
            pass
        else:
            html = html + str(x[1]) + "："
            html = html + str(calc.year) + "年"
            html = html + str(calc.month).zfill(2) + "月"
            html = html + str(calc.day).zfill(2) + "日"
            html = html + str(calc.hour).zfill(2) + "時"
            html = html + "（"
            html = html + str(x[2])
            html = html + "）"
            pass
        html = html + "</option>"

    html = html + "</select>"

    return html

def getAction(args):

    query = ("Select"
             "  action.action_num"
             "  ,mst.name"
             "  ,action.action_time"
             "  ,action.action_time_in_this_world"
             "  ,action.action"
             " From"
             "  action"
             " left join"
             "  mst"
             " On"
             "  action.action = mst.kind_cd"
             " And"
             "  mst.class_cd = %s"
             " WHERE"
             "  system_users_cd = %s"
             " ORDER BY"
             "  action_num")

    var = system.MSTCOMMAND,(args["system_users_cd"]),
    
    return executeSql.selectAllQueryTupple(query,var)

def getActionOption(args):

    query = ("Select"
             "  action.option"
             " From"
             "  action"
             " WHERE"
             "  system_users_cd = %s"
             " And action_num = %s")

    var = args["system_users_cd"],(args["action_num"]),
    
    return executeSql.selectAllQueryTupple(query,var)

def getSoldierBySoldierCd(args):

    query = ("Select"
             "  *"
             " From"
             "  soldier"
             " Where"
             "  soldier_cd = %s")

    var = args["soldier_cd"],

    return executeSql.selectOneQueryTupple(query,var)

def getMapByMapCd(args):

    query = ("Select"
             "  *"
             " From"
             "  map"
             " Where"
             "  map_cd = %s")

    var = args["map_cd"],

    return executeSql.selectOneQueryTupple(query,var)

def getSystemTime():

    query = ("Select"
             "  *"
             " From"
             "  System_time")

    return executeSql.selectAllQuery(query)

# news
def createNews():

    result = getNews()

    html = ""
    for x in result:
        html = html + x[1] + "<br />"
        pass

    return html

def getNews():

    query = ("Select"
             "  *"
             " From"
             "  news"
             " Order by"
             "  news_cd desc"
             " LIMIT"
             "  %s")

    var = sql.NEWSLIMIT,
    
    return executeSql.selectAllQueryTupple(query,var)

# status
def createStatus(args):
    
    result = getStatus(args)
    resultCampGroup = getCampGroup(str(result[sql.SYSTEM_USERS_CAMP_GROUP]))

    html = ""

    html = html + "<table class=\"getChatGroup\" border=\"5\" bordercolor=\"white\" align=\"center\">"
    
    html = html + "<tr>"
    html = html + "<td colspan=\"2\">名前:" + str(result[sql.SYSTEM_USERS_NAME]) + "</td>"
    html = html + "</tr>"

    if resultCampGroup == None:
        html = html + "<tr>"
        html = html + "<td colspan=\"2\">所属陣営:無所属</td>"
        html = html + "</tr>"
    else:
        html = html + "<tr>"
        html = html + "<td colspan=\"2\">所属陣営:" + str(resultCampGroup[0]) + "</td>"
        html = html + "</tr>"

    html = html + "<tr>"
    html = html + "<td>武力:" + str(result[sql.SYSTEM_USERS_ATTACK]) + "</td>"
    html = html + "<td>知力:" + str(result[sql.SYSTEM_USERS_INTELLIGENCE]) + "</td>"
    html = html + "</tr>"

    html = html + "<tr>"
    html = html + "<td>統率力:" + str(result[sql.SYSTEM_USERS_LEADERSHIP]) + "</td>"
    html = html + "<td>資産:" + str(result[sql.SYSTEM_USERS_ASSETS]) + "</td>"
    html = html + "</tr>"

    html = html + "<tr>"
    html = html + "<td>武器効果:" + str(result[sql.SYSTEM_USERS_WEAPON]) + "</td>"
    html = html + "<td>武器名:" + str(result[sql.SYSTEM_USERS_WEAPON_NAME]) + "</td>"
    html = html + "</tr>"
    
    html = html + "</table>"

    return html

def getStatus(args):

    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " WHERE"
             "  system_users_cd = %s")

    var = (args["system_users_cd"]),
    
    return executeSql.selectOneQueryTupple(query,var)

def getCampGroup(args):

    query = ("Select"
             "  name"
             " From"
             "  mst"
             " WHERE"
             "  class_cd = 2"
             " And kind_cd = %s")

    var = (args),
    
    return executeSql.selectOneQueryTupple(query,var)


# move
def createSelectBoxMove(args):

    result = getTargetMove(args)

    html = "<select name=\"target\" size=" + ui.LIST + ">"
    html = html + "<option value=999 disabled>===隣接地ここから===</option>"
    
    for x in result:
        html = html + "<option value=" + str(x[sql.MAP_MAP_CD]) + ">"
        html = html + str(x[sql.MAP_NAME]) + "(" + str(x[sql.MAP_LATITUDE_CD]) + "-" + str(x[sql.MAP_LONGITUDE_CD]) + ")"
        html = html + "</option>"

    html = html + "<option value=999 disabled>===ここまで===</option>"

    resultGetmap = getMap()

    for x in resultGetmap:
        html = html + "<option value=" + str(x[sql.MAP_MAP_CD]) + ">"
        html = html + str(x[sql.MAP_NAME]) + "(" + str(x[sql.MAP_LATITUDE_CD]) + "-" + str(x[sql.MAP_LONGITUDE_CD]) + ")"
        html = html + "</option>"

    html = html + "</select>"

    return html

def getTargetMove(args):
    
    query = ("Select"
                " 	*"
                " From"
                " 	map"
                " Where"
                " 	latitude_cd = (select latitude_cd from map where map_cd = %s)"
                " And longitude_cd = (select longitude_cd + 1 from map where map_cd = %s)"
                " Union all"
                " Select"
                " 	*"
                " From"
                " 	map"
                " Where"
                " 	latitude_cd = (select latitude_cd from map where map_cd = %s)"
                " And longitude_cd = (select longitude_cd - 1 from map where map_cd = %s)"
                " Union all"
                " Select"
                " 	*"
                " From"
                " 	map"
                " Where"
                " 	latitude_cd = (select latitude_cd + 1 from map where map_cd = %s)"
                " And longitude_cd = (select longitude_cd from map where map_cd = %s)"
                " Union all"
                " Select"
                " 	*"
                " From"
                " 	map"
                " Where"
                " 	latitude_cd = (select latitude_cd - 1 from map where map_cd = %s)"
                " And longitude_cd = (select longitude_cd from map where map_cd = %s)")


    var = args,args,args,args,args,args,args,args,
    
    return executeSql.selectAllQueryTupple(query,var)

# History
def createHistoryAction(args):
    
    result = getTarHistoryAction(args)

    resultSplit = result[0][1].split(',')

    html = ""
    html = html + "<table border=\"5\" bordercolor=\"white\" >"
    html = html + " <thead>"
    html = html + "     <tr><th>時間</th><th>行動内容</th></tr>"
    html = html + " </thead>"
    html = html + " <tbody>"

    count = 0
    for x in resultSplit:

        if x == "":
            continue

        if count == ui.HISTORY:
            html = html + " </tbody>"
            html = html + "</table>"
            return html
        
        y = x.split(ui.HISTORYCOMMA)
        html = html + "<tr>"
        html = html + "<th>"
        html = html + y[1]
        html = html + "</th>"
        html = html + "<th>"
        html = html + y[0]
        html = html + "</th>"
        html = html + "</tr>"
        count = count + 1

    html = html + " </tbody>"
    html = html + "</table>"

    return html

def getTarHistoryAction(args):
    
    query = ("select"
                "	*"
                " from"
                "	action_logs"
                " where"
                "	system_users_cd = %s")

    var = args,
    
    return executeSql.selectAllQueryTupple(query,var)

# SoldierList
def createSoldierList(args):

    result = getSoldierData(args)

    html = ""
    for x in result:
        html = html + "<table border=\"5\" bordercolor=\"white\" >"
        html = html + " <thead>"
        html = html + "     <tr><th>名前</th><th>速さ</th><th>力</th><th>根気強さ</th><th>コスト</th></tr>"
        html = html + " </thead>"
        html = html + " <tbody>"
        html = html + " <tr>"
        html = html + ("<th>" + str(x[sql.SOLDIER_NAME]).replace("\n","<br />") + "</th>"
                       "<th>" + str(x[sql.SOLDIER_SPEED]) + "</th>"
                       "<th>" + str(x[sql.SOLDIER_STRENGTH]) + "</th>"
                        "<th>" + str(x[sql.SOLDIER_HARDNESS]) + "</th>"
                        "<th>" + str(x[sql.SOLDIER_COST]) + "</th>")
        html = html + " <form action=\"./inputSoldier\" method=\"post\">"
        html = html + " <th>"
        html = html + "     <input type=\"hidden\" name=\"soldier_cd\" value=" + str(x[sql.SOLDIER_CD]) + ">"
        html = html + "     <input type=\"text\" name=\"number\" maxlength=\"6\" style=\"width:45px;\">"
        html = html + " </th>"
        html = html + " <th>"
        html = html + "     ⇒<button type=\"submit\">招集</button>"
        html = html + " </th>"
        html = html + " </form>"
        html = html + " <form action=\"./inputSoldier\" method=\"post\">"
        html = html + " <th>"
        html = html + "     <input type=\"hidden\" name=\"soldier_cd\" value=" + str(x[sql.SOLDIER_CD]) + ">"
        html = html + "     <input type=\"text\" name=\"number\" value=\"100\" maxlength=\"6\" style=\"width:45px;\">"
        html = html + " </th>"
        html = html + " <th>"
        html = html + "     ⇒<button type=\"submit\">招集</button>"
        html = html + " </th>"
        html = html + " </form>"
        html = html + " <form action=\"./inputSoldier\" method=\"post\">"
        html = html + " <th>"
        html = html + "     <input type=\"hidden\" name=\"soldier_cd\" value=" + str(x[sql.SOLDIER_CD]) + ">"
        html = html + "     <input type=\"text\" name=\"number\" value=\"1000\" maxlength=\"6\" style=\"width:45px;\">"
        html = html + " </th>"
        html = html + " <th>"
        html = html + "     ⇒<button type=\"submit\">招集</button>"
        html = html + " </th>"
        html = html + " </form>"
        html = html + " </tr>"
        html = html + " <tr>"
        html = html + " <th colspan=\"11\">"
        html = html + str(x[sql.SOLDIER_FLAVOR])
        html = html + " </th>"
        html = html + " </tr>"
        html = html + " </tbody>"
        html = html + " </table>"
        html = html + "<br />"

    return html
    
def getSoldierData(args):

    query = ("Select"
             "  *"
             " From"
             "  soldier"
             " Where"
             "  camp_group = %s"
             " Order by"
             "  soldier_cd")

    var = args,

    return executeSql.selectAllQueryTupple(query,var)

def createSoldierListPersonal(args):

    result = getSoldierDataPersonal(args)

    if result == [] or result == None:
        html = "現在、貴方は兵を所有していません"
        return html

    html = ""
    for x in result:
        html = html + "<table border=\"5\" bordercolor=\"white\" >"
        html = html + "<thead>"
        html = html + "<tr>"
        html = html + " <th></th>"
        html = html + " <th>No</th>"
        html = html + " <th>名前</th>"
        html = html + " <th>兵数</th>"
        html = html + " <th>訓練度</th>"
        html = html + " <th>速さ</th>"
        html = html + " <th>力</th>"
        html = html + " <th>コスト</th>"
        html = html + " <th>道徳</th>"
        html = html + " <th>粘り強さ</th>"
        html = html + " <th>招集時の陣営</th>"
        #html = html + " <th>必要影響力</th>"
        html = html + " <th>防衛場所</th>"
        html = html + "</tr>"
        html = html + "</thead>"
        html = html + "<tbody>"
        html = html + "<tr>"
        html = html + "<th><input type=\"radio\" name=\"soldier\" value=" + str(x[0]) + "></th>"
        html = html + "<th>" + str(x[0]) + "</th>"
        html = html + "<th>" + str(x[1]) + "</th>"
        html = html + "<th>" + str(x[2]) + "</th>"
        html = html + "<th>" + str(x[3]) + "</th>"
        html = html + "<th>" + str(x[4]) + "</th>"
        html = html + "<th>" + str(x[5]) + "</th>"
        html = html + "<th>" + str(x[6]) + "</th>"
        html = html + "<th>" + str(x[7]) + "</th>"
        html = html + "<th>" + str(x[8]) + "</th>"
        html = html + "<th>" + str(x[9]) + "</th>"
        #html = html + "<th>" + str(x[10]) + "</th>"
        html = html + "<th>" + str(x[11]) + "(" + str(x[12]) + "-" + str(x[13]) + ")" + "</th>"

        if False:
            html = html + "<form action=\"./inputSoldier\" method=\"post\">"
            html = html + " <th>"
            html = html + "     <input type=\"hidden\" name=\"soldier_cd\" value=" + str(x[sql.SOLDIER_CD]) + ">"
            html = html + "     <input type=\"text\" name=\"number\">"
            html = html + " </th>"
            html = html + " <th>"
            html = html + "     <button type=\"submit\">招集</button>"
            html = html + " </th>"
            html = html + "</form>"
            pass

        html = html + "</tr>"
        html = html + "</tbody>"
        html = html + "</table>"
        html = html + "<br />"

    return html
    
def getSoldierDataPersonal(args):

    query = ("Select"
             "  soldier_personal.soldier_personal_cd"
             "  ,soldier.name"
             "  ,soldier_personal.number"
             "  ,soldier_personal.training"
             "  ,soldier.speed"
             "  ,soldier.strength"
             "  ,soldier.cost"
             "  ,soldier.morals"
             "  ,soldier.hardness"
             "  ,soldier.camp_group"
             "  ,soldier.influence"
             "  ,map.name"
             "  ,map.latitude_cd"
             "  ,map.longitude_cd"
             " From"
             "  soldier_personal"
             " inner join soldier"
             "  on soldier_personal.soldier_cd = soldier.soldier_cd"
             " left join map"
             "  on soldier_personal.map_cd = map.map_cd"
             " Where"
             "  soldier_personal.system_users_cd = %s")
    
    var = args,

    return executeSql.selectAllQueryTupple(query,var)

# Config
def createConfigBackGroundColor():

    html = ""
    html = html + "<div class=\"centeringInlineBlock\">"
    html = html + "<table border=\"5\" bordercolor=\"white\" >"
    #html = html + " <thead>"
    #html = html + " <tr><th>Color</th></tr>"
    #html = html + " </thead>"
    html = html + " <tbody>"
    html = html + " <tr>"
    html = html + "     <th>"
    html = html + "オリジナル"
    html = html + "     </th>"
    html = html + "     <form action=\"./configChangeColor\" method=\"post\">"
    html = html + "         <th>"
    html = html + "             <input type=\"hidden\" name=\"color_cd\" value=" + ui.ConfigBackGroundColorOne + ">"
    html = html + "             <button type=\"submit\">決定</button>"
    html = html + "         </th>"
    html = html + "     </form>"
    html = html + " </tr>"
    html = html + " <tr>"
    html = html + "     <th>"
    html = html + "煉瓦レッド"
    html = html + "     </th>"
    html = html + "     <form action=\"./configChangeColor\" method=\"post\">"
    html = html + "         <th>"
    html = html + "             <input type=\"hidden\" name=\"color_cd\" value=" + ui.ConfigBackGroundColorTwo + ">"
    html = html + "             <button type=\"submit\">決定</button>"
    html = html + "         </th>"
    html = html + "     </form>"
    html = html + " </tr>"
    html = html + " <tr>"
    html = html + "     <th>"
    html = html + "煉瓦ブルー"
    html = html + "     </th>"
    html = html + "     <form action=\"./configChangeColor\" method=\"post\">"
    html = html + "         <th>"
    html = html + "             <input type=\"hidden\" name=\"color_cd\" value=" + ui.ConfigBackGroundColorThree + ">"
    html = html + "             <button type=\"submit\">決定</button>"
    html = html + "         </th>"
    html = html + "     </form>"
    html = html + " </tr>"
    html = html + " </tbody>"
    html = html + " </table>"
    html = html + "</div>"

    return html

# UserList
def createListUser(args):

    args = {"camp_group":args}
    magicList = getListUser(args)
    magic = "<br />"
    magic = magic + "   <table class=\"magic\" border=\"5\" bordercolor=\"white\" align=\"center\">"
    magic = magic + "       <thead>"
    magic = magic + "           <tr><th>名前</th><th>武力</th><th>知力</th><th>統率力</th></tr>"
    magic = magic + "       </thead>"
    magic = magic + "       <tbody>"
    for x in magicList:
        comp = "<tr>"
        comp = comp + "<td>" + str(x[sql.SYSTEM_USERS_NAME]) + "</td>"
        comp = comp + "<td>" + str(x[sql.SYSTEM_USERS_ATTACK]) + "</td>"
        comp = comp + "<td>" + str(x[sql.SYSTEM_USERS_INTELLIGENCE]) + "</td>"
        comp = comp + "<td>" + str(x[sql.SYSTEM_USERS_LEADERSHIP]) + "</td>"
        comp = comp + "</tr>"
        magic = magic + comp + "<br />"
        pass
    magic = magic + "       </tbody>"
    magic = magic + "   </table>"
    
    return magic

def getListUser(args):

    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  camp_group = %s")

    var = str(args["camp_group"]),
    
    return executeSql.selectAllQueryTupple(query,var)

# GuardList
def createListGuard(args):

    result = getListGuard(args)

    html = "【名前:部隊No】"
    html = html + "<br />"
    html = html + "～"
    for x in result:
        html = html + "【" + str(x[0]) + ":" + str(x[1]) + "】～"
        pass

    return html

def getListGuard(args):

    query = ("Select"
             "  name"
             "  ,soldier_personal_cd"
             " From"
             "  soldier_personal"
             " inner join system_users"
             "  on soldier_personal.system_users_cd = system_users.system_users_cd"
             " Where"
             "  soldier_personal.map_cd = %s"
             " Order by"
             "  guard_number")

    var = args,
    
    return executeSql.selectAllQueryTupple(query,var)

def createButtonGroup(args):

    # ユーザのグループを取得
    targetGroup = args["targetGroup"]

    # マップをグループで検索
    resultGetGroupListByCampGroup = getGroupListByCampGroup(targetGroup)

    # 存在しない場合はボタンを表示する
    if len(resultGetGroupListByCampGroup) != 0:
        return ""

    html = ""
    html = html + "<br />" + "足音が聞こえる。"
    html = html + "<br />" + "この寂れた事務所に、誰が来たのだろう。"
    html = html + "<br />" + "足音の主が事務所の扉を開ける。"
    html = html + "<br />" + "同時に貴方は構える。"
    html = html + "<br />" + "「おー。早まるな、早まるな」"
    html = html + "<br />" + "声の主は笑う。そしてのたまう。"
    html = html + "<br />" + "「アンタの為に良い話を持ってきた。陣営を変えてみないか」"
    html = html + "<br />" + "貴方は構えを解く。"
    html = html + "<br />" + ""
    html = html + "<br />" + "****貴方の所属している陣営は勢力争いで負けてしまいました。"
    html = html + "<br />" + "別陣営に所属して続きを楽しみましょう****"
    html = html + "<br />" + ""
    html = html + "<form action=\"./changeGroup\" method=\"post\">"
    html = html + "<button type=\"submit\">陣営替え</button>"
    html = html + "</form>"
    return html

def createButtonChangingGroup(args):
    
    html = ""
    if str(args) == system.CAMPGROUPMAGIC:
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPGANG + ">"
        html = html + "<button type=\"submit\">半グレに陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPPOLICE + ">"
        html = html + "<button type=\"submit\">警察に陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"
    elif str(args) == system.CAMPGROUPGANG:
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPMAGIC + ">"
        html = html + "<button type=\"submit\">魔法使いに陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPPOLICE + ">"
        html = html + "<button type=\"submit\">警察に陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"
    elif str(args) == system.CAMPGROUPPOLICE:
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPGANG + ">"
        html = html + "<button type=\"submit\">半グレに陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"
        html = html + "</ br>"
        html = html + "<form action=\"./executeChangeGroup\" method=\"post\">"
        html = html + "<input type=\"hidden\" name=\"group\" value=" + system.CAMPGROUPMAGIC + ">"
        html = html + "<button type=\"submit\">魔法使いに陣営替えする</button>"
        html = html + "</form>"
        html = html + "</ br>"

    return html

def getGroupListByCampGroup(args):

    query = ("Select"
             "  *"
             " From"
             "  map"
             " Where"
             "  camp_group = %s")

    var = args,
    
    return executeSql.selectAllQueryTupple(query,var)

# Div
def createDivBaseColor(args):

    result = getConfigColor(args)

    html = ""
    if result[0] == ui.ConfigBackGroundColorOne:
        html = html + "<div class=\"normalOne\">"
    elif result[0] == ui.ConfigBackGroundColorTwo:
        html = html + "<div class=\"normalTwo\">"
    elif result[0] == ui.ConfigBackGroundColorThree:
        html = html + "<div class=\"normalThree\">"
    else:
        html = html + "<div class=\"normalOne\">"

    return html

def getConfigColor(args):

    query = ("Select"
             "  config_color"
             " From"
             "  system_users"
             " WHERE"
             "  id = %s"
             " And password = %s")

    var = str(args["id"]),str(args["password"]),
    
    return executeSql.selectOneQueryTupple(query,var)

# Quest
def createExecuteQuestButton(args):
    
    from NewFolder2.NewFolder1.const import quest

    resultGetSystemUsersCd = getSystemUsersCd(args)

    argsGetFlagQuest = {}
    if str(args["questCommonCd"]) == quest.CODEOFQUEST001:
        argsGetFlagQuest = {"query":"quest_number_001","system_users_cd":resultGetSystemUsersCd[0]}
    elif str(args["questCommonCd"]) == quest.CODEOFQUEST002:
        argsGetFlagQuest = {"query":"quest_number_002","system_users_cd":resultGetSystemUsersCd[0]}
    else:
        return html

    flag = False
    resultGetFlagQuest = getFlagQuest(argsGetFlagQuest)
    if resultGetFlagQuest[0] == 0:
        flag = True

    html = ""
    if flag == True:

        html = html + "<form action=\"./questCheck\" method=\"post\">"
        html = html + "	<input type=\"hidden\" name=\"quest_common_cd\" value=" + str(args["questCommonCd"]) + " />"
        html = html + "	<button type=\"submit\">"
        html = html + "		check!"
        html = html + "	</button>"
        html = html + "</form>"

        return html
    else:
        return html

def getFlagQuest(args):
    
    query = ("Select"
             "  " + str(args["query"]) + " From"
             "  manage_quest"
             " WHERE"
             "  system_users_cd = %s")

    var = (args["system_users_cd"]),
    
    return executeSql.selectOneQueryTupple(query,var)

def getSystemUsersCd(args):
    
    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  id = %s"
             " And password = %s")

    var = str(args["id"]),str(args["password"])
    
    return executeSql.selectOneQueryTupple(query,var)

def createQuestAfter(args):
    
    from NewFolder2.NewFolder1.const import quest

    resultGetSystemUsersCd = getSystemUsersCd(args)

    html = ""
    argsGetFlagQuest = {}
    if str(args["questCommonCd"]) == quest.CODEOFQUEST001:
        argsGetFlagQuest = {"query":"quest_number_001","system_users_cd":resultGetSystemUsersCd[0]}
        html = quest.RESULTQUEST001
    elif str(args["questCommonCd"]) == quest.CODEOFQUEST002:
        argsGetFlagQuest = {"query":"quest_number_002","system_users_cd":resultGetSystemUsersCd[0]}
        html = quest.RESULTQUEST002
    else:
        return html

    flag = True
    resultGetFlagQuest = getFlagQuest(argsGetFlagQuest)
    if resultGetFlagQuest[0] == 0:
        flag = False

    if flag == False:

        html = ""

        return html
    else:
        return html

def createBodyMeetingRoom(args):

    result = getBodyMeetingRoom(args)

    html = ""

    if result == []:
        return ""

    thread = result[0][1]
    for x in result:

        if thread != x[1]:
            #html = html + "<form action=\"./inputMeetingRoom\" method=\"post\">"
            #html = html + "<br />"
            #html = html + "本文"
            #html = html + "<br />"
            #html = html + "<textarea cols=\"30\" rows=\"10\" name=\"body\"></textarea>"
            #html = html + "<br />"
            #html = html + "<button type=\"submit\">送信</button>"
            html = html + "～～～"
            pass

        html = html + "<table class=\"getChatGroup\" border=\"5\" bordercolor=\"white\" align=\"center\">"
        
        html = html + "<tr>"
        html = html + "<td colspan=\"2\">" + str(x[3]) + "</td>"
        html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<td>" + str(x[5]) + "</td>"
        html = html + "<td>" + str(x[6]) + "</td>"
        html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<td colspan=\"2\">" + str(x[4]).replace("\n","<br />") + "</td>"
        html = html + "</tr>"
        
        html = html + "</table>"

    return html

def getBodyMeetingRoom(args):

    query = ("Select"
             "  MeetingRoom.camp_group"
             "  ,MeetingRoom.thread"
             "  ,MeetingRoom.childNumber"
             "  ,MeetingRoom.title"
             "  ,MeetingRoom.body"
             "  ,system_users.name"
             "  ,MeetingRoom.body_time"
             " From"
             "  MeetingRoom"
             " Left join"
             "  system_users"
             " On MeetingRoom.system_users_cd = system_users.system_users_cd"
             " WHERE"
             "  MeetingRoom.camp_group = %s"
             " ORDER BY"
             "  MeetingRoom.thread desc")

    var = str(args["camp_group"]),
    
    return executeSql.selectAllQueryTupple(query,var)
