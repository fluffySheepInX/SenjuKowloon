from ..model import executeSql
from ..const import system
from ..const import systemCommand
from ..const import sql
from ..const import htmlBattle
from datetime import datetime, timedelta
import random

def getUser(args):
    
    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  id = %s"
             " And password = %s")

    var = str(args["id"]),str(args["password"])
    
    return executeSql.selectOneQueryTupple(query,var)

def getNumberOfUser():
    
    query = ("Select"
             "  count(*)"
             " From"
             "  system_users")
    
    return executeSql.selectAllQuery(query)

def getUserBySystemUsersCd(args):
    
    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  system_users_cd = %s")

    var = str(args["system_users_cd"]),
    
    return executeSql.selectOneQueryTupple(query,var)

def getListUser(args):

    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  camp_group = %s")

    var = str(args["camp_group"]),
    
    return executeSql.selectAllQueryTupple(query,var)

def checkUserName(args):
    
    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  name = %s"
             "")

    var = str(args["name"]),
    
    if executeSql.selectOneQueryTupple(query,var) == None:
        return True
    else:
        return False

def checkUserId(args):
    
    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " Where"
             "  id = %s"
             "")

    var = str(args["id"]),
    
    if executeSql.selectOneQueryTupple(query,var) == None:
        return True
    else:
        return False

def insertChat(args):
    
    query = ("INSERT INTO chat_logs ("
             "system_users_cd"
             ",camp_group"
             ",target_cd"
             ",remark"
             ",remark_time"
             ") VALUES ("
             "%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ")")

    var = ((args["system_users_cd"]),
            (args["camp_group"]),
            (args["target_cd"]),
            str(args["remark"]),
            str(args["remark_time"]))

    executeSql.executeQueryTupple(query,var)

def registerAction(args,cur=None):

    time = datetime.now()
    checkAndUpdateTime()
    getRecord = getSystemTime()
    nowTimeInThisWorld = getRecord[0][0]

    for x in range(system.ACTION):

        if x == 0:
            continue

        query = ("INSERT INTO action ("
                 "system_users_cd"
                 ",action_num"
                 ",action"
                 ",option"
                 ",action_time"
                 ",action_time_in_this_world"
                 ") VALUES ("
                 "%s"
                 ",%s"
                 ",%s"
                 ",%s"
                 ",%s"
                 ",%s"
                 ")")

        # xは1から始まる
        var = ((args["system_users_cd"]),
            x,
            system.COMMANDNULL,
            None,
            time + timedelta(hours=system.INTERVAL * x),
            nowTimeInThisWorld + timedelta(hours=system.INTERVALSYSTEM * x),)

        if cur != None:
            cur.execute(query,var)
        else:
            executeSql.executeQueryTupple(query,var)

def registerActionLogs(args,cur=None):
    
    query = ("INSERT INTO action_logs ("
             "system_users_cd"
             ",value"
             ") VALUES ("
             "%s"
             ",%s"
             ")")
    
    var = (args["system_users_cd"]),systemCommand.RESISTER + str(datetime.now()) + ","
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def registerQuest(args,cur=None):
    
    query = ("INSERT INTO manage_quest ("
             "system_users_cd"
             ",patrol_number"
             ",quest_number_001"
             ",call_soldier_number"
             ",quest_number_002"
             ") VALUES ("
             "%s"
             ",0"
             ",0"
             ",0"
             ",0"
             ")")
    
    var = (args["system_users_cd"]),
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def updateAction(args):

    query = ("update action"
             " set"
             "  action = %s"
             " ,option = %s"
             " where"
             "  system_users_cd = %s"
             " and action_num = %s")

    var = ((args["action"]),
            (args["option"]),
            (args["system_users_cd"]),
            (args["action_num"]))

    executeSql.executeQueryTupple(query,var)

def updateActionMultiple(args):

    query = ("update action"
             " set"
             "  action = %s"
             " ,option = %s"
             " where"
             "  system_users_cd = %s"
             " and action_num in %s")

    var = ((args["action"]),
            (args["option"]),
            (args["system_users_cd"]),
            tuple(args["action_num"]))

    executeSql.executeQueryTupple(query,var)

def insertNews(args):

    query = ("INSERT INTO news ("
             "value"
             ") VALUES ("
             "%s"
             ")")

    var = ((args["value"]),)

    executeSql.executeQueryTupple(query,var)

def processTimer():
    
    # check and update time
    checkAndUpdateTime()

    result = getTarget()

    if result == [] or result == None:
        return

    getRecord = getSystemTime()
    nowTimeInThisWorld = getRecord[0][0]
    count = 0

    for x in result:
        with executeSql.getConnection() as conn:
            with conn.cursor() as cur:

                userCd = x[sql.ACTION_SYSTEM_USERS_CD]
                strTime = createStrTime(x)
                count = count + system.COUNTBATTLE

                # お給料&ランダムイベント
                if x[sql.ACTION_ACTION_TIME_IN_THIS_WORLD].hour == 0:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]
                    resultStatus = getStatus(userCd)

                    # お給料
                    assets = 0
                    if str(resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]) == system.CAMPGROUPMAGIC:
                        assets = system.GAINFUNDINGMAGIC
                        pass
                    if str(resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]) == system.CAMPGROUPGANG:
                        assets = system.GAINFUNDINGGANG
                        pass
                    if str(resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]) == system.CAMPGROUPPOLICE:
                        assets = system.GAINFUNDINGPOLICE
                        pass

                    arg = assets,userCd
                    gainFunding(arg,cur)
                    
                    # ログ出力
                    setActionLogs(userCd,
                                    systemCommand.FUNDING.format(assets) + strTime,
                                    cur)

                    random.seed(datetime.now().second)
                    ra = random.randint(1,9)
                    if ra == 1:
                        gainAttack(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM001.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 2:
                        gainAttack(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM002.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 3:
                        gainAttack(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM003.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 4:
                        gainLeadership(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM004.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 5:
                        gainIntelligence(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM005.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 6:
                        gainIntelligence(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM006.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 7:
                        gainLeadership(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM007.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 8:
                        gainLeadership(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM008.format("0.1") + strTime,
                                        cur)
                        pass
                    elif ra == 9:
                        gainAttack(userCd,"0.1",cur)
                        setActionLogs(userCd,
                                        systemCommand.RANDOM009.format("0.1") + strTime,
                                        cur)
                        pass

                    pass

                if x[sql.ACTION_ACTION] == system.COMMANDNULL:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    # ログ出力
                    setActionLogs(userCd,
                                    systemCommand.NOACTION + strTime,
                                    cur)
                    pass
                elif x[sql.ACTION_ACTION] == system.COMMANDPATROL:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] == resultMap[sql.MAP_CAMP_GROUP]:
                        # 現在地の所属とユーザの所属が一致していたら
                        gainInfluence(resultMap[0],cur)
                        gainLeadership(userCd,str(systemCommand.PATROL001),cur)
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.PATROL.format(systemCommand.PATROL001,systemCommand.PATROL002) + strTime,
                                      cur)
                        
                        gainNumberPatrol(userCd,cur)

                        pass
                    else:
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.NOBASE + strTime,
                                      cur)
                elif x[sql.ACTION_ACTION] == system.COMMANDCOMMERCE:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] == resultMap[sql.MAP_CAMP_GROUP]:
                        # 現在地の所属とユーザの所属が一致していたら
                        gainInfluence(resultMap[0],cur)
                        gainIntelligence(userCd,str(systemCommand.COMMERCE001),cur)
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.COMMERCE.format(systemCommand.COMMERCE001,systemCommand.COMMERCE002) + strTime,
                                      cur)
                    else:
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.NOBASE + strTime,
                                      cur)
                elif x[sql.ACTION_ACTION] == system.COMMANDTRAINING:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] == resultMap[sql.MAP_CAMP_GROUP]:
                        # 現在地の所属とユーザの所属が一致していたら
                        gainInfluence(resultMap[0],cur)
                        gainAttack(userCd,str(systemCommand.TRAINING001),cur)
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.TRAINING.format(systemCommand.TRAINING001,systemCommand.TRAINING002) + strTime,
                                      cur)
                    else:
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.NOBASE + strTime,
                                      cur)
                elif x[sql.ACTION_ACTION] == system.COMMANDMOVE:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    targetPlace = x[sql.ACTION_OPTION]
                    getNameTargetPlace = getMap(targetPlace)
                    resultStatus = getStatus(userCd)
                    targetSubPlace = getTargetMove(resultStatus[sql.SYSTEM_USERS_MAP_CD])
                    getNameFormerPlace = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    flag = False
                    for y in targetSubPlace:
                        if str(y[sql.MAP_MAP_CD]) == targetPlace:
                            setPlace(userCd,targetPlace,cur)
                            flag = True

                            # ログ出力
                            setActionLogs(userCd,
                                          systemCommand.MOVE.format(getNameFormerPlace[sql.MAP_NAME],getNameTargetPlace[sql.MAP_NAME]) + strTime,
                                          cur)
                        pass

                    if flag == False:
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.NOMOVE.format(getNameTargetPlace[sql.MAP_NAME]) + strTime,
                                      cur)
                        pass
                    pass
                elif x[sql.ACTION_ACTION] == system.COMMANDCALLSOLDIER:

                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    targetData = x[sql.ACTION_OPTION]
                    resultSplit = targetData.split(',')

                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] == resultMap[sql.MAP_CAMP_GROUP]:
                        # 現在地の所属とユーザの所属が一致していたら
                        resultSoldierCost = getSoldierCost(resultSplit[0])
                        cost = int(resultSoldierCost[0])
                        number = int(resultSplit[1])
                        myAssets = int(resultStatus[sql.SYSTEM_USERS_ASSETS])

                        args = {"userCd":userCd,
                                "targetData":targetData,
                                "resultSplit":resultSplit,
                                "resultStatus":resultStatus,
                                "resultSoldierCost":resultSoldierCost,
                                "cost":cost,
                                "number":number,
                                "myAssets":myAssets,
                                "strTime":strTime}

                        processCallSoldier(args,cur)

                        gainNumberCallSoldier(userCd,cur)

                        pass

                    pass
                elif x[sql.ACTION_ACTION] == system.COMMANDATTACK:

                    # 基礎情報取得
                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]
                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] == resultMap[sql.MAP_CAMP_GROUP]:
                        targetData = x[sql.ACTION_OPTION]
                        resultSplit = targetData.split(',')
                        mapCd = resultSplit[0]
                        getNameTargetPlace = getMap(mapCd)

                        args = {"userCd":userCd,
                                "resultStatus":resultStatus,
                                "targetData":targetData,
                                "resultSplit":resultSplit,
                                "mapCd":mapCd,
                                "getNameTargetPlace":getNameTargetPlace,
                                "count":count,
                                "strTime":strTime}

                        processAttack(args,cur)

                        pass
                    else:
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.ATTACKSTAY + strTime,
                                      cur)
                    pass
                elif x[sql.ACTION_ACTION] == system.COMMANDGUARD:

                    # 現在地チェック
                    userCd = x[sql.ACTION_SYSTEM_USERS_CD]

                    resultStatus = getStatus(userCd)
                    resultMap = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])

                    if resultStatus[sql.SYSTEM_USERS_CAMP_GROUP] != resultMap[sql.MAP_CAMP_GROUP]:
                        # 現在地が自陣営でないなら駄目
                        # ログ出力
                        setActionLogs(userCd,
                                      systemCommand.NOBASE + strTime,
                                      cur)
                        pass
                    else:
                        # 順番最大値を取得
                        args = [userCd,resultStatus[sql.SYSTEM_USERS_MAP_CD]]
                        resultGetGuardNumber = getGuardNumber(args)
                        setGuardNumber = 0
                        
                        # 更新前準備
                        if resultGetGuardNumber[0] == None:
                            setGuardNumber = 1
                            pass
                        else:
                            setGuardNumber = resultGetGuardNumber[0] + 1
                            pass
                        
                        targetNumber = x[sql.ACTION_OPTION]
                        if system.GUARDLAST == targetNumber:

                            args = [userCd]
                            targetNumber = getSoldierNumber(args)

                            pass
                        args = [resultStatus[sql.SYSTEM_USERS_MAP_CD],setGuardNumber,targetNumber,userCd]
                        
                        # 更新
                        setGuard(args,cur)

                        # ログ出力
                        getNameFormerPlace = getMap(resultStatus[sql.SYSTEM_USERS_MAP_CD])
                        setActionLogs(userCd,
                                          systemCommand.GUARD.format(getNameFormerPlace[sql.MAP_NAME]) + strTime,
                                          cur)
                        pass
                    pass

                deleteActionTimer(x,cur)
                updateActionTimer(x,cur)
                insertActionTimer(x,cur)

                conn.commit()

    pass

def getTarget():

    query = ("Select"
             "  *"
             " From"
             "  action"
             " Where"
             "  action_time <= %s"
             " order by"
             "  action_time")

    var = datetime.now(),
    
    return executeSql.selectAllQueryTupple(query,var)

def deleteActionTimer(args,cur=None):

    query = ("Delete From"
             "  action"
             " Where"
             "  system_users_cd = %s"
             " and action_num = 1")

    var = args[sql.ACTION_SYSTEM_USERS_CD],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def updateActionTimer(args,cur=None):

    query = ("Update"
             "  action"
             " Set"
             "  action_num = action_num -1"
             " Where"
             "  system_users_cd = %s")

    var = args[sql.ACTION_SYSTEM_USERS_CD],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def insertActionTimer(args,cur=None):

    query = ("INSERT INTO action ("
             "system_users_cd"
             ",action_num"
             ",action"
             ",option"
             ",action_time"
             ",action_time_in_this_world"
             ")"
             " Select"
             "      %s"
             "      ,%s"
             "      ,%s"
             "      ,%s"
             "      ,action_time + '" + str(system.INTERVAL) + " hours'"
             "      ,action_time_in_this_world + '" + str(system.INTERVALSYSTEM) + " hours'"
             "  From"
             "      action"
             "  Where"
             "      system_users_cd = %s"
             "  And action_num = %s")

    var = (args[sql.ACTION_SYSTEM_USERS_CD],
            system.ACTION - 1,
            system.COMMANDNULL,
            None,
            args[sql.ACTION_SYSTEM_USERS_CD],
            system.ACTION - 2)

    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def getStatus(args):

    query = ("Select"
             "  *"
             " From"
             "  system_users"
             " WHERE"
             "  system_users_cd = %s")

    var = (args),
    
    return executeSql.selectOneQueryTupple(query,var)

def getMap(args):

    query = ("Select"
             "  *"
             " From"
             "  map"
             " WHERE"
             "  map_cd = %s")

    var = (args),
    
    return executeSql.selectOneQueryTupple(query,var)

def gainInfluence(args,cur=None):

    query = ("Update"
             "  map"
             " Set"
             "  influence = influence + 1"
             " Where"
             "  map_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainLeadership(args,amount,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  leadership = leadership + " + amount + ""
             " Where"
             "  system_users_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainAttack(args,amount,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  attack = attack + " + amount + ""
             " Where"
             "  system_users_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainFunding(args,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  assets = assets + %s"
             " Where"
             "  system_users_cd = %s")

    var = args[0],args[1],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainIntelligence(args,amount,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  intelligence = intelligence + " + amount + ""
             " Where"
             "  system_users_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def checkAndUpdateTime():
    
    getRecord = getSystemTime()

    # 現在時刻から前回実行時の時刻を引く
    getCalc1 = datetime.now() - getRecord[0][1]
    # 経過時間を時に直す(1時間更新の場合
    getCalc2 = getCalc1.total_seconds() // (3600 * system.INTERVAL)
    # 劇中時刻に経過時間(時)を足す(刻みがsystem.INTERVALSYSTEM
    getCalc3 = getRecord[0][0] + timedelta(hours=int(getCalc2) * system.INTERVALSYSTEM)
    # 足された劇中時刻を設定する
    setSystemTime(getCalc3,datetime.now())

def getSystemTime():

    query = ("Select"
             "  *"
             " From"
             "  System_time")

    return executeSql.selectAllQuery(query)

def setSystemTime(time,realTime):
    
    query = ("Update System_time"
             " Set"
             "  time = %s"
             "  ,real_time = %s")

    var = time,realTime
    
    executeSql.executeQueryTupple(query,var)

def setActionLogs(userCd,value,cur=None):
    
    query = ("Update action_logs"
             " Set"
             "  value = %s || ',' || value"
             " Where"
             "  system_users_cd = %s")

    var = value,userCd,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)
    pass

def existSoldier(args):

    query = ("Select"
             "  *"
             " From"
             "  Soldier"
             " Where"
             "  soldier_cd = %s")

    var = args,

    result = executeSql.selectAllQueryTupple(query,var)

    if result != None:
        return True
    else:
        return False

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

def setPlace(userCd,maoCd,cur=None):

    query = ("Update system_users"
             " Set"
             "  map_cd = %s"
             " Where"
             "  system_users_cd = %s")

    var = maoCd,userCd,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)
    pass
    
def setSoldier(userCd,kind,number,cur=None):
    
    #query = ("Update system_users"
    #         " Set"
    #         " filibusters = filibusters || %s || ':' || %s || ':' || '0' ||
    #         ','"
    #         " Where"
    #         " system_users_cd = %s")

    query = ("INSERT INTO soldier_personal ("
             "soldier_personal_cd"
             ",system_users_cd"
             ",soldier_cd"
             ",number"
             ",training"
             ") select "
             " Case When MAX(soldier_personal_cd) IS NULL THEN 1"
             "      ELSE MAX(soldier_personal_cd) + 1"
             " END"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             " From"
             " soldier_personal"
             " where"
             " system_users_cd = %s")

    var = userCd,kind,number,0,userCd,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)
    pass

def getSoldierName(args):

    query = ("Select"
             "  name"
             " From"
             "  Soldier"
             " Where"
             "  soldier_cd = %s")

    var = (args),

    return executeSql.selectOneQueryTupple(query,var)

def getSoldierCost(args):

    query = ("Select"
             "  cost"
             " From"
             "  Soldier"
             " Where"
             "  soldier_cd = %s")

    var = (args),

    return executeSql.selectOneQueryTupple(query,var)

def setGroupForMap(args,cur=None):

    query = ("Update"
             "  map"
             " Set"
             "  camp_group = %s"
             " Where"
             "  map_cd = %s")

    var = args[0],args[1],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def getGuardNumber(args):

    query = ("Select"
             "  MAX(guard_number)"
             " From"
             "  soldier_personal"
             " Where"
             "  system_users_cd = %s"
             " And map_cd = %s")

    var = args[0],args[1],

    return executeSql.selectOneQueryTupple(query,var)

def getSoldierNumber(args):

    query = ("Select"
             "  MAX(soldier_personal_cd)"
             " From"
             "  soldier_personal"
             " Where"
             "  system_users_cd = %s")

    var = args[0],

    return executeSql.selectOneQueryTupple(query,var)

def getSoldierBySoldierPersonalCd(args):

    query = ("Select"
             "  *"
             " From"
             "  soldier_personal"
             " Where"
             "  soldier_personal_cd = %s"
             " And system_users_cd = %s")

    var = args[0],args[1]

    return executeSql.selectOneQueryTupple(query,var)

def getSoldierBySoldierCd(args):

    query = ("Select"
             "  *"
             " From"
             "  soldier"
             " Where"
             "  soldier_cd = %s")

    var = args[0],

    return executeSql.selectOneQueryTupple(query,var)

def getGuardList(args,cur=None):

    query = ("Select"
             "  *"
             " From"
             "  soldier_personal"
             " Where"
             "  map_cd = %s")

    var = args,

    if cur != None:
        cur.execute(query,var)
        return cur.fetchall()
    else:
        return executeSql.selectAllQueryTupple(query,var)

def setGuard(args,cur=None):

    query = ("Update"
             "  soldier_personal"
             " Set"
             "  map_cd = %s"
             "  ,guard_number = %s"
             " Where"
             "  soldier_personal_cd = %s"
             " And system_users_cd = %s")

    var = args[0],args[1],args[2],args[3],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def setWinner(args,cur=None):

    query = ("Update"
             "  soldier_personal"
             " Set"
             "  number = %s"
             " Where"
             "  soldier_personal_cd = %s"
             " And system_users_cd = %s")

    var = args[0],args[1],args[2],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def setAssets(args,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  assets = %s"
             " Where"
             "  system_users_cd = %s")

    var = args[0],args[1],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def processAttack(args,cur=None):

    userCd = args["userCd"]
    resultStatus = args["resultStatus"]
    targetData = args["targetData"]
    resultSplit = args["resultSplit"]
    mapCd = args["mapCd"]
    getNameTargetPlace = args["getNameTargetPlace"]
    strTime = args["strTime"]
    count = args["count"]

    # 戦闘開始年月チェック
    resultSystemTime = getSystemTime()
    resultStartTime = datetime.strptime(system.STARTWARDATE, '%Y/%m/%d')
    if resultSystemTime[0][0] < resultStartTime:
        # ログ出力
        setActionLogs(userCd,
                      systemCommand.ATTACKDATE + strTime,
                      cur)
        return

    # 他陣営かチェックを行う
    if getNameTargetPlace[sql.MAP_CAMP_GROUP] == resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]:
        
        # 同じ陣営の場合は移動+防衛

        # ログ出力
        setActionLogs(userCd,
                      systemCommand.ATTACKSOMEGROUP + strTime,
                      cur)

        setPlace(userCd,mapCd,cur)
    
        # 順番最大値を取得
        args = [userCd,resultStatus[sql.SYSTEM_USERS_MAP_CD]]
        resultGetGuardNumber = getGuardNumber(args)
        setGuardNumber = 0
        
        # 更新前準備
        if resultGetGuardNumber[0] == None:
            setGuardNumber = 1
            pass
        else:
            setGuardNumber = resultGetGuardNumber[0] + 1
            pass
                
        args = [mapCd,setGuardNumber,resultSplit[1],userCd]
        
        # 更新
        setGuard(args,cur)

        # ログ出力
        setActionLogs(userCd,
                          systemCommand.GUARD.format(getNameTargetPlace[sql.MAP_NAME]) + strTime,
                          cur)
        return 
    
    # ログ出力
    setActionLogs(userCd,
                  systemCommand.ATTACK.format(getNameTargetPlace[sql.MAP_NAME]) + strTime,
                  cur)
    
    # 守備情報取得
    resultGetGuardList = getGuardList(mapCd)

    if (resultGetGuardList == [] or resultGetGuardList == None):
        # 守備がいない場合
        # 実質的に無所属地域支配処理

        # 支配処理
    
        args = [resultStatus[sql.SYSTEM_USERS_CAMP_GROUP],mapCd]
        
        setGroupForMap(args,cur)
        setPlace(userCd,mapCd,cur)
    
        # 更新前準備
        setGuardNumber = 1
        args = [mapCd,setGuardNumber,resultSplit[1],userCd]
        
        # 更新
        setGuard(args,cur)
    
        # ログ出力
        setActionLogs(userCd,
                      systemCommand.ATTACKNOGUARD.format(getNameTargetPlace[sql.MAP_NAME]) + strTime,
                      cur)
        
        # ニュース出力
        arg = {"value":system.NEWSCATEGORY004 + system.NEWSDOMINATION.format(resultStatus[sql.SYSTEM_USERS_NAME],getNameTargetPlace[sql.MAP_NAME])}
        insertNews(arg)
    
        # 無所属の場合、ここで処理を終了
        if getNameTargetPlace[sql.MAP_CAMP_GROUP] == None:
            return

        # 上書きされた陣営cdで領土をチェック、一つも無ければ滅亡
        resultGetCountCampGroup = getCountCampGroup(getNameTargetPlace[sql.MAP_CAMP_GROUP],cur)
        if int(resultGetCountCampGroup[0][0]) > 0:
            # 一つ以上ある
            return
        
        # 滅亡処理
        resultCampGroupTarget = getCampGroup(str(getNameTargetPlace[sql.MAP_CAMP_GROUP]))
        arg = {"value":system.NEWSCATEGORY005 + system.NEWSWITHDRAWAL.format(resultCampGroupTarget[0])}
        insertNews(arg)
        
        # 勢力が一つのみか
        resultGetExistCampGroup = getExistCampGroup(cur)
        if len(resultGetExistCampGroup) != 1:
            return
        
        # 統一処理
        resultCampGroup = getCampGroup(str(resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]))
        arg = {"value":system.NEWSCATEGORY006 + system.NEWSWUNIFICATION.format(resultCampGroup[0])}
        insertNews(arg)

        return

    # 守備がいる場合
    for x in resultGetGuardList:
        count = count + 1

        if (count != 0 and 0 == (count % system.COUNTBATTLE)):
            # ログ出力
            setActionLogs(userCd,
                          systemCommand.ATTACKCOUNT + strTime,
                          cur)
            return


        # 戦闘処理準備
        args = {"attackUserCd":userCd,
                "attackUserSoldierPersonalCd":resultSplit[1],
                "resultGetGuardListX":x,
                "cur":cur,
                "count":count,
                "strTime":strTime,}
        # 戦闘処理
        resultBattle = startBattle(args)

        if resultBattle == True:
            # 勝利時

            # ログ出力
            setActionLogs(userCd,
                  systemCommand.ATTACKSUCCESESS + strTime,
                  cur)
    
            # 防衛剥がし
            # map_cdで抽出し、-1する
            # 0となったものをdeleteする
            argsSetGuardLose = [mapCd]
            setGuardLose(argsSetGuardLose,cur)
            deleteGuardLose(argsSetGuardLose,cur)

            resultGetGuardList = getGuardList(mapCd,cur)
            if len(resultGetGuardList) == 0:
                # 防衛がいなくなった場合
                
                # 支配処理
    
                args = [resultStatus[sql.SYSTEM_USERS_CAMP_GROUP],mapCd]
                
                setGroupForMap(args,cur)
                setPlace(userCd,mapCd,cur)
                
                # 更新前準備
                setGuardNumber = 1
                args = [mapCd,setGuardNumber,resultSplit[1],userCd]
                
                # 更新
                setGuard(args,cur)
                
                # ログ出力
                setActionLogs(userCd,
                              systemCommand.ATTACKNOGUARD.format(getNameTargetPlace[sql.MAP_NAME]) + strTime,
                              cur)
                
                # ニュース出力
                arg = {"value":system.NEWSCATEGORY004 + system.NEWSDOMINATION.format(resultStatus[sql.SYSTEM_USERS_NAME],getNameTargetPlace[sql.MAP_NAME])}
                insertNews(arg)
                
                # 上書きされた陣営cdで領土をチェック、一つも無ければ滅亡
                resultGetCountCampGroup = getCountCampGroup(getNameTargetPlace[sql.MAP_CAMP_GROUP],cur)
                if int(resultGetCountCampGroup[0][0]) > 0:
                    # 一つ以上ある
                    continue

                # 滅亡処理
                resultCampGroupTarget = getCampGroup(str(getNameTargetPlace[sql.MAP_CAMP_GROUP]))
                arg = {"value":system.NEWSCATEGORY005 + system.NEWSWITHDRAWAL.format(resultCampGroupTarget[0])}
                insertNews(arg)

                # 勢力が一つのみか
                resultGetExistCampGroup = getExistCampGroup(cur)
                if len(resultGetExistCampGroup) != 1:
                    continue

                # 統一処理
                resultCampGroup = getCampGroup(str(resultStatus[sql.SYSTEM_USERS_CAMP_GROUP]))
                arg = {"value":system.NEWSCATEGORY006 + system.NEWSWUNIFICATION.format(resultCampGroup[0])}
                insertNews(arg)

                pass
    
            pass
        else:
            # 敗北時
    
            # ログ出力
            setActionLogs(userCd,
                  systemCommand.ATTACKFAILURE + strTime,
                  cur)
            return
        pass

    return

def startBattle(args):

    # 攻撃者に関連する情報
    attackUserCd = args["attackUserCd"]
    arg = {"system_users_cd":attackUserCd}
    attackUser = getUserBySystemUsersCd(arg)
    arg = None

    attackInfluence = getInfluenceThePlace(attackUser[sql.SYSTEM_USERS_MAP_CD])

    attackUserSoldier = args["attackUserSoldierPersonalCd"]
    arg = [attackUserSoldier,attackUserCd]
    attackSoldier = getSoldierBySoldierPersonalCd(arg)
    arg = None

    argsGetSoldierBySoldierCd = [attackSoldier[sql.SOLDIER_PERSONAL_SOLDIER_CD]]
    attackUserSoldierBase = getSoldierBySoldierCd(argsGetSoldierBySoldierCd)
    argsGetSoldierBySoldierCd = None

    # 防衛に関連する情報
    resultGetGuardListX = args["resultGetGuardListX"]
    arg = {"system_users_cd":resultGetGuardListX[1]}
    guardUser = getUserBySystemUsersCd(arg)
    arg = None
    guardInfluence = getInfluenceThePlace(guardUser[sql.SYSTEM_USERS_MAP_CD])
    argsGetSoldierBySoldierCd = [resultGetGuardListX[sql.SOLDIER_PERSONAL_SOLDIER_CD]]
    guardUserSoldierBase = getSoldierBySoldierCd(argsGetSoldierBySoldierCd)
    argsGetSoldierBySoldierCd = None

    # システム情報
    strTime = args["strTime"]
    count = args["count"]
    cur = args["cur"]

    attackWin = False
    guardWin = False
    numberAttack = attackSoldier[3]
    numberGuard = resultGetGuardListX[3]
    
    html = ""
    html = html + "<table border=\"5\" bordercolor=\"white\" >"
    html = html + " <thead>"
    html = html + "     <tr><th>攻撃</th><th>守備</th></tr>"
    html = html + " </thead>"
    html = html + " <tbody>"
    html = html + "<tr>"
    html = html + " <th>"
    html = html + attackUser[sql.SYSTEM_USERS_NAME]
    html = html + " </th>"
    html = html + " <th>"
    html = html + guardUser[sql.SYSTEM_USERS_NAME]
    html = html + " </th>"
    html = html + "</tr>"
    html = html + "<tr>"
    html = html + " <th>"
    html = html + attackUserSoldierBase[sql.SOLDIER_NAME]
    html = html + " </th>"
    html = html + " <th>"
    html = html + guardUserSoldierBase[sql.SOLDIER_NAME]
    html = html + " </th>"
    html = html + "</tr>"

    for x in range(1,50):

        random.seed(datetime.now().second)
        raAttack = random.randint(1,9)
        raGuard = random.randint(1,9)

        turnOfSp = 10
        damageGuard = 0
        damageAttack = 0

        if x % turnOfSp == 0:
            # ((影響力*0.01) ** (知力*0.01)) *11
            # (6.5**1.5)*11 = 182.289947611
            damageAttack = ((attackInfluence[0] * 0.01) ** (int(attackUser[sql.SYSTEM_USERS_INTELLIGENCE]) * 0.01)) * 11 + raAttack
            numberGuard = numberGuard - damageAttack
        else:
            # (((武力(固定値)+兵の力) / 10 ) * 速さ)
            # ((150 + 40) /10) * 0.8 = 15.2
            damageAttack = ((int(attackUser[sql.SYSTEM_USERS_ATTACK]) + attackUserSoldierBase[sql.SOLDIER_STRENGTH]) / 10) * int(attackUserSoldierBase[sql.SOLDIER_SPEED]) + raAttack
            numberGuard = numberGuard - damageAttack

        if x % turnOfSp == 0:
            damageGuard = ((guardInfluence[0] * 0.01) ** (int(guardUser[sql.SYSTEM_USERS_INTELLIGENCE]) * 0.01)) * 11 + raGuard
            numberAttack = numberAttack - damageGuard
        else:
            damageGuard = ((int(guardUser[sql.SYSTEM_USERS_ATTACK]) + guardUserSoldierBase[sql.SOLDIER_STRENGTH]) / 10) * int(guardUserSoldierBase[sql.SOLDIER_SPEED]) + raGuard
            numberAttack = numberAttack - damageGuard

        if x % turnOfSp == 0:
            html = html + "<tr>"
            html = html + "<th>"
            html = html + "攻め手は策を以て仕掛けるようだ......"
            html = html + "</th>"
            html = html + "<th>"
            html = html + "受け手も策で対抗するようだ......"
            html = html + "</th>"
            html = html + "</tr>"

        html = html + "<tr>"
        html = html + "<th>"
        html = html + "攻撃：" + str(numberAttack) + "(" + "-" + str(damageGuard) + ")"
        html = html + "</th>"
        html = html + "<th>"
        html = html + "守備：" + str(numberGuard) + "(" + "-" + str(damageAttack) + ")"
        html = html + "</th>"
        html = html + "</tr>"

        if numberAttack <= 0:
            guardWin = True

        if numberGuard <= 0:
            attackWin = True

        if (numberAttack <= 0 or numberGuard <= 0):
            break

        pass

    html = html + " </tbody>"
    html = html + "</table>"

    resultHtml = htmlBattle.html.format(html)

    path_w_base = "NewFolder2/NewFolder1/"
    path_w = "battleLog/"
    path_w = path_w + str(datetime.now().year) 
    path_w = path_w + str(datetime.now().month)
    path_w = path_w + str(datetime.now().day)
    path_w = path_w + str(datetime.now().hour)
    path_w = path_w + str(attackUserCd) + str(count) + ".html"
    with open(path_w_base + path_w, mode='w',encoding="utf-8") as f:
        f.write(resultHtml)

    # ログ出力
    setActionLogs(attackUserCd,
                    systemCommand.INTOATTACK.format(guardUser[sql.SYSTEM_USERS_NAME],path_w) + strTime,
                    cur)
    setActionLogs(guardUser[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
                    systemCommand.INTOATTACK.format(attackUser[sql.SYSTEM_USERS_NAME],path_w) + strTime,
                    cur)

    if (attackWin == True and guardWin == True):
        # お互い0の引き分け
        # 攻撃者勝利で進行

        # ニュース出力
        arg = {"value":system.NEWSCATEGORY002 + system.NEWSBATTLE.format(attackUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],attackUser[sql.SYSTEM_USERS_NAME],path_w)}
        insertNews(arg)

        # 兵更新
        arg = [numberAttack,attackSoldier[sql.SOLDIER_PERSONAL_SOLDIER_PERSONAL_CD],attackUserCd]
        setWinner(arg,cur)
        return True
        
    if (attackWin == False and guardWin == False):
        # お互い0以上の引き分け
        # 攻撃者敗北で進行

        # ニュース出力
        arg = {"value":system.NEWSCATEGORY002 + system.NEWSBATTLE.format(attackUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],path_w)}
        insertNews(arg)

        # 兵更新
        arg = [numberGuard,resultGetGuardListX[0],resultGetGuardListX[1]]
        setWinner(arg,cur)
        arg = [numberAttack,attackSoldier[sql.SOLDIER_PERSONAL_SOLDIER_PERSONAL_CD],attackUserCd]
        setWinner(arg,cur)
        return False
        
    if (attackWin == True and guardWin == False):
        # 攻撃者勝利

        # ニュース出力
        arg = {"value":system.NEWSCATEGORY002 + system.NEWSBATTLE.format(attackUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],attackUser[sql.SYSTEM_USERS_NAME],path_w)}
        insertNews(arg)

        # 兵更新
        arg = [numberAttack,attackUserCd,attackUserSoldier]
        setWinner(arg,cur)
        return True

    # 攻撃者敗北

    # ニュース出力
    arg = {"value":system.NEWSCATEGORY002 + system.NEWSBATTLE.format(attackUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],guardUser[sql.SYSTEM_USERS_NAME],path_w)}
    insertNews(arg)

    # 兵更新
    arg = [numberGuard,resultGetGuardListX[0],resultGetGuardListX[1]]
    setWinner(arg,cur)
    arg2 = [attackUserSoldier,attackUserCd]
    deletesSoldierPersonal(arg2)

    return False

def setGuardLose(args,cur=None):

    query = ("Update"
             "  soldier_personal"
             " Set"
             "  guard_number = guard_number -1"
             " Where"
             "  map_cd = %s")

    var = args[0],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def deleteGuardLose(args,cur=None):

    query = ("Delete From"
             "  soldier_personal"
             " Where"
             "  map_cd = %s"
             " And guard_number = 0")

    var = args[0],
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def deletesSoldierPersonal(args,cur=None):

    query = ("Delete From"
             "  soldier_personal"
             " Where"
             "  soldier_personal_cd = %s"
             " And system_users_cd = %s")

    var = args[0],args[1]
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def processCallSoldier(args,cur=None):
    
    userCd = args["userCd"]
    
    targetData = args["targetData"]
    resultSplit = args["resultSplit"]
    
    resultStatus = args["resultStatus"]
    resultSoldierCost = args["resultSoldierCost"]
    cost = args["cost"]
    number = args["number"]
    myAssets = args["myAssets"]
    strTime = args["strTime"]

    # 上限チェック
    if number > system.LIMITCALLSOLDIER:
        # ログ出力
        setActionLogs(userCd,
                      systemCommand.CALLSOLDIERLIMIT.format(system.LIMITCALLSOLDIER) + strTime,
                      cur)
        return
    
    # 所持金チェック
    normalCost = 0
    if (number - resultStatus[sql.SYSTEM_USERS_LEADERSHIP]) > 0:
        normalCost = (number - resultStatus[sql.SYSTEM_USERS_LEADERSHIP]) * cost
        normalCost = normalCost + ((resultStatus[sql.SYSTEM_USERS_LEADERSHIP] * cost) / system.COSTLEADERSHIP)
    else:
        normalCost = ((resultStatus[sql.SYSTEM_USERS_LEADERSHIP] / system.COSTLEADERSHIP) * cost)
    
    if normalCost > myAssets:
        # ログ出力
        setActionLogs(userCd,
                      systemCommand.NOASSETS + strTime,
                      cur)
        return
    
    # 所持金処理
    assets = myAssets - normalCost
    args = [assets,userCd]
    setAssets(args,cur)
    
    setSoldier(userCd,resultSplit[0],resultSplit[1],cur)
    name = getSoldierName(resultSplit[0])
    
    # ログ出力
    setActionLogs(userCd,
                  systemCommand.CALLSOLDIER.format(name[0],resultSplit[1]) + strTime,
                  cur)
    pass
    
def getCountCampGroup(args,cur=None):

    query = ("Select"
             "  count(*)"
             " From"
             "  map"
             " Where"
             "  camp_group = %s")

    var = args,

    if cur != None:
        cur.execute(query,var)
        return cur.fetchall()
    else:
        return executeSql.selectAllQueryTupple(query,var)

def getExistCampGroup(cur=None):

    query = ("Select"
             "  camp_group"
             " From"
             "  map"
             " Where"
             "  camp_group Is Not Null"
             " Group by"

             "  camp_group")

    if cur != None:
        cur.execute(query)
        return cur.fetchall()
    else:
        return executeSql.selectAllQuery(query)

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

def getInfluenceThePlace(args):

    query = ("Select"
             "  influence"
             " From"
             "  map"
             " WHERE"
             "  map_cd = %s")

    var = (args),
    
    return executeSql.selectOneQueryTupple(query,var)

def createStrTime(args):
    x = args
    strTime = str(x[sql.ACTION_ACTION_TIME_IN_THIS_WORLD].year) + "年"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME_IN_THIS_WORLD].month).zfill(2) + "月"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME_IN_THIS_WORLD].day).zfill(2) + "日"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME_IN_THIS_WORLD].hour).zfill(2) + "時"
    strTime = strTime + "(現実時間:"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].year) + "年"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].month).zfill(2) + "月"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].day).zfill(2) + "日"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].hour).zfill(2) + "時"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].minute).zfill(2) + "分"
    strTime = strTime + str(x[sql.ACTION_ACTION_TIME].second).zfill(2) + "秒"
    strTime = strTime + ")"
    return strTime

def setColor(args,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  config_color = %s"
             " Where"
             "  id = %s"
             " And password = %s")

    var = str(args["config_color"]),str(args["id"]),str(args["password"]),
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainNumberPatrol(args,cur=None):

    query = ("Update"
             "  manage_quest"
             " Set"
             "  patrol_number = patrol_number + 1"
             " Where"
             "  system_users_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def gainNumberCallSoldier(args,cur=None):

    query = ("Update"
             "  manage_quest"
             " Set"
             "  call_soldier_number = call_soldier_number + 1"
             " Where"
             "  system_users_cd = %s")

    var = args,
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def getManageQuest(args):
    
    query = ("Select"
             "  *"
             " From"
             "  manage_quest"
             " Where"
             "  system_users_cd = %s")

    var = str(args["system_users_cd"]),
    
    return executeSql.selectOneQueryTupple(query,var)

def switchToOnManageQuest(args,cur=None):

    query = ("Update"
             "  manage_quest"
             " Set"
             "  " + str(args["target"]) + " = 1"
             " Where"
             "  system_users_cd = %s")

    var = str(args["system_users_cd"]),
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def questCheck(args):
    
    from NewFolder2.NewFolder1.const import quest

    argsGetManageQuest = {"system_users_cd":args["system_users_cd"]}
    resultGetManageQuest = getManageQuest(argsGetManageQuest)

    if str(args["questCommonCd"]) == quest.CODEOFQUEST001:

        if resultGetManageQuest[sql.MANAGE_QUEST_PATROL_NUMBER] > 0:
            
            with executeSql.getConnection() as conn:
                with conn.cursor() as cur:
                    args = {"target":"quest_number_001","system_users_cd":args["system_users_cd"]}
                    switchToOnManageQuest(args,cur)
                    gainLeadership(args["system_users_cd"],"10",cur)
                    gainAttack(args["system_users_cd"],"10",cur)
                    gainIntelligence(args["system_users_cd"],"10",cur)
            result = {"successFlag":1}
            return result
        else:
            result = {"successFlag":0}
            return result

        return
    elif str(args["questCommonCd"]) == quest.CODEOFQUEST002:

        if resultGetManageQuest[sql.MANAGE_QUEST_CALL_SOLDIER_NUMBER] > 0:
            with executeSql.getConnection() as conn:
                with conn.cursor() as cur:
                    args = {"target":"quest_number_002","system_users_cd":args["system_users_cd"]}
                    switchToOnManageQuest(args,cur)
                    gainLeadership(args["system_users_cd"],"10",cur)
                    gainAttack(args["system_users_cd"],"10",cur)
                    gainIntelligence(args["system_users_cd"],"10",cur)
            result = {"successFlag":1}
            return result
        else:
            result = {"successFlag":0}
            return result

        return
    else:
        return

    return

def saveTabRight(args,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  tab_right = %s")
    
    if str(args["tab_right"]) == "1":
        query = query + " ,tab_right_all = now()"
    elif str(args["tab_right"]) == "2":
        query = query + " ,tab_right_group = now()"
    elif str(args["tab_right"]) == "3":
        query = query + " ,tab_right_personal = now()"

    query = query + (" Where"
             "  system_users_cd = %s")

    var = str(args["tab_right"]),str(args["system_users_cd"])
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def getCountChat(args,kind):
    
    var = "",

    if kind == 1:
        query = (""
                "select "
                "	count(*)"
                " from"
                "	chat_logs"
                " where "
                "	camp_group is null"
                " and	system_users_cd <> %s"
                " and	remark_time > ("
                "		select "
                "			tab_right_all "
                "		from "
                "			system_users "
                "		where "
                "			system_users_cd = %s)")
        var = str(args["system_users_cd"]),str(args["system_users_cd"]),

    elif kind == 2:
        query = (""
                "select "
                "	count(*)"
                " from"
                "	chat_logs"
                " where "
                "	camp_group = %s"
                " and	system_users_cd <> %s"
                " and	remark_time > ("
                "		select "
                "			tab_right_group "
                "		from "
                "			system_users "
                "		where "
                "			system_users_cd = %s)")
        var = str(args["camp_group"]),str(args["system_users_cd"]),str(args["system_users_cd"]),

    elif kind == 3:
        query = (""
                "select "
                "	count(*)"
                " from"
                "	chat_logs"
                " where "
                "	target_cd = %s"
                " and	system_users_cd <> %s"
                " and	remark_time > ("
                "		select "
                "			tab_right_personal "
                "		from "
                "			system_users "
                "		where "
                "			system_users_cd = %s)")
        var = str(args["system_users_cd"]),str(args["system_users_cd"]),str(args["system_users_cd"]),
    
    return executeSql.selectOneQueryTupple(query,var)

def setGroup(args,cur=None):

    query = ("Update"
             "  system_users"
             " Set"
             "  camp_group = %s"
             " Where"
             "  id = %s"
             " And password = %s")

    var = str(args["camp_group"]),str(args["id"]),str(args["password"]),
    
    if cur != None:
        cur.execute(query,var)
    else:
        executeSql.executeQueryTupple(query,var)

def writeMeetingRoom(args):
    
    query = ("INSERT INTO MeetingRoom ("
             "camp_group"
             ",childNumber"
             ",title"
             ",body"
             ",system_users_cd"
             ",body_time"
             ") VALUES ("
             "%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ",%s"
             ")")

    var = ((args["camp_group"]),
           0,
            (args["title"]),
            (args["body"]),
           (args["system_users_cd"]),
            str(args["body_time"]))

    executeSql.executeQueryTupple(query,var)
