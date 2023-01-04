from bottle import route, view, request, template, response, redirect
from datetime import datetime
from NewFolder2.NewFolder1.control import adminFunction as adminFunction
from NewFolder2.NewFolder1.control import normalFunction as normalFunction
from NewFolder2.NewFolder1.control import uiFunction as uiFunction
from NewFolder2.NewFolder1.model import executeSql as executeSql
from NewFolder2.NewFolder1.const import cookie as cookie
from NewFolder2.NewFolder1.const import system as system
from NewFolder2.NewFolder1.const import sql as sql
from NewFolder2.NewFolder1.const import debug as debug

@route('/')
@route('/top')
@view('top')
def top():
    try:
        normalFunction.processTimer()

        resultCreateMap = uiFunction.createMap()
        resultNews = uiFunction.createNews()

        return dict(year=datetime.now().year,
                    news = resultNews,
                    map = resultCreateMap,
                    message = "")
    except :
        return dict(year=datetime.now().year,
                    news = "",
                    map="",
                    message = "")
    pass

@route('/story')
@view('story')
def story():
    return  dict(year=datetime.now().year)

@route('/notice')
@view('notice')
def notice():
    return  dict(year=datetime.now().year)

@route('/manual')
@view('manual')
def manual():
    return  dict(year=datetime.now().year)

@route('/listUser')
@view('listUser')
def listUser():

    magic = uiFunction.createListUser(system.CAMPGROUPMAGIC)
    outlaw = uiFunction.createListUser(system.CAMPGROUPGANG)
    police = uiFunction.createListUser(system.CAMPGROUPPOLICE)

    return  dict(year=datetime.now().year,magic=magic,outlaw=outlaw,police=police)

@route('/changeGroup', method=["POST"])
@view('changeGroup')
def changeGroup():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    resultButton = uiFunction.createButtonChangingGroup(userTwo[sql.SYSTEM_USERS_CAMP_GROUP])

    return  dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                 button=resultButton)

@route('/executeChangeGroup', method=["POST"])
def executeChangeGroup():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)
    
    userTwo = normalFunction.getUser(user)

    arg = {"camp_group":request.forms.group,"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    normalFunction.setGroup(arg)

    redirect(system.REDIRECTMAIN)

@route('/listSoldier', method=["POST"])
@view('listSoldier')
def listSoldier():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    soldier = uiFunction.createSoldierListPersonal(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                soldier = soldier)

@route('/config', method=["POST"])
@view('config')
def config():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    resultBackGroundColor = uiFunction.createConfigBackGroundColor()

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                backGroundColor = resultBackGroundColor)

@route('/questCommon', method=["POST"])
@view('questCommon')
def questCommon():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor)

@route('/configChangeColor', method=["POST"])
@view('config')
def configChangeColor():

    action = request.get_cookie(cookie.COOKIECALLSOLDIER, secret=cookie.SECRET)
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    color_cd = request.forms.color_cd

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD],"config_color":color_cd}
    normalFunction.setColor(arg)

    resultBackGroundColor = uiFunction.createConfigBackGroundColor()

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                backGroundColor = resultBackGroundColor)

@route('/main' , method=["POST"])
def main():

    normalFunction.processTimer()
    
    id = request.forms.user_id
    password = request.forms.user_password

    if (id == None or id == '') or (password == None or password == ''):
        id = request.forms.getunicode('user_id')
        password = request.forms.getunicode('user_password')

    if (id == None or id == '') or (password == None or password == ''):
        return template('top',
                        year=datetime.now().year,
                        news = "",
                        map="",
                        message = "idもしくはpasswordが未入力です")

    arg = {"id":id,"password":password}

    user = normalFunction.getUser(arg)

    if user == None:
        return template('top',
                        year=datetime.now().year,
                        news = "",
                        map="",
                        message = "キャラクターが存在しませんでした。貴方が入力したidは【" + id + "】です")

    #if request.get_cookie(cookie.COOKIE) == None:
    #response.set_cookie(cookie.COOKIE, user, max_age=60 * 60 * 24,
    #secret=cookie.SECRET)
    response.set_cookie(cookie.COOKIE, arg, max_age=60 * 60 * 24, secret=cookie.SECRET)

    redirect(system.REDIRECTMAIN)

@route('/main')
def main():

    normalFunction.processTimer()

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],"camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP]}

    resultCreateMap = uiFunction.createMap()
    resultCurrentLocation = uiFunction.createCurrentLocation(arg)
    resultCreateChatGroup = uiFunction.createChatGroup(arg)
    resultCreateChatAll = uiFunction.createChatAll(arg)
    resultCreateChatPrivate = uiFunction.createChatPrivate(arg)
    resultCommand = uiFunction.createCommand()
    resultAction = uiFunction.createAction(arg)
    resultNews = uiFunction.createNews()
    resultStatus = uiFunction.createStatus(arg)

    resultGetStatus = normalFunction.getStatus(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])
    resultMapCd = resultGetStatus[sql.SYSTEM_USERS_MAP_CD]
    resultGuard = uiFunction.createListGuard(resultMapCd)

    arg = {"targetGroup":userTwo[sql.SYSTEM_USERS_CAMP_GROUP]}
    resultAppointment = uiFunction.createButtonGroup(arg)

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    resultCheckedRight1 = "checked"
    resultCheckedRight2 = ""
    resultCheckedRight3 = ""
    resultCountAll = ""
    resultCountGroup = ""
    resultCountPersonal = ""
    if resultGetStatus[sql.SYSTEM_USERS_TAB_RIGHT] == "1":
        resultCheckedRight1 = "checked"
        resultCheckedRight2 = ""
        resultCheckedRight3 = ""
        arg = {"camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP]
               ,"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD]}
        resultCount = normalFunction.getCountChat(arg,2)
        if resultCount[0] != 0:
            resultCountGroup = "("+str(resultCount[0])+")"
            pass
        #resultCountPersonal = ""
    elif resultGetStatus[sql.SYSTEM_USERS_TAB_RIGHT] == "2":
        resultCheckedRight1 = ""
        resultCheckedRight2 = "checked"
        resultCheckedRight3 = ""
        arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD]}
        resultCount = normalFunction.getCountChat(arg,1)
        if resultCount[0] != 0:
            resultCountAll = "("+str(resultCount[0])+")"
            pass
        #resultCountPersonal = ""
    elif resultGetStatus[sql.SYSTEM_USERS_TAB_RIGHT] == "3":
        resultCheckedRight1 = ""
        resultCheckedRight2 = ""
        resultCheckedRight3 = "checked"
        arg = {"camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP]
               ,"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD]}
        resultCount1 = normalFunction.getCountChat(arg,1)
        resultCount2 = normalFunction.getCountChat(arg,2)
        if resultCount1[0] != 0:
            resultCountAll = "("+str(resultCount1[0])+")"
            pass
        if resultCount2[0] != 0:
            resultCountGroup = "("+str(resultCount2[0])+")"
            pass

    resultAjaxUrlLeft = ""
    resultAjaxUrlRight = ""
    if debug.debug:
        resultAjaxUrlLeft = "/ajaxTabLeft"
        resultAjaxUrlRight = "/ajaxTabRight"
    else:
        resultAjaxUrlLeft = "http://lockedroom.s16.valueserver.jp/base.py/ajaxTabLeft"
        resultAjaxUrlRight = "http://lockedroom.s16.valueserver.jp/base.py/ajaxTabRight"

    return template('views/main',
                    year = datetime.now().year,
                    divBaseColor = resultCreateDivBaseColor,
                    chatGroup = resultCreateChatGroup,
                    chatAll = resultCreateChatAll,
                    chatPrivate = resultCreateChatPrivate,
                    command = resultCommand,
                    action = resultAction,
                    news = resultNews,
                    status = resultStatus,
                    currentLocation = resultCurrentLocation,
                    guard = resultGuard,
                    appointment = resultAppointment,
                    checkedRight1 = resultCheckedRight1,
                    checkedRight2 = resultCheckedRight2,
                    checkedRight3 = resultCheckedRight3,
                    checkedLeft1 = "checked",
                    checkedLeft2 = "",
                    checkedLeft3 = "",
                    countAll = resultCountAll,
                    countGroup = resultCountGroup,
                    countPersonal = resultCountPersonal,
                    ajaxUrlLeft = resultAjaxUrlLeft,
                    ajaxUrlRight = resultAjaxUrlRight,
                    id = userTwo[sql.SYSTEM_USERS_ID],
                    password = userTwo[sql.SYSTEM_USERS_PASSWORD],
                    map = resultCreateMap)

@route('/inputAction' , method=["POST"])
def inputAction():

    resultKey = request.forms.dict.get('action',None)
    if resultKey == None:
        redirect(system.REDIRECTMAIN)

    action = request.forms.dict['action']
    command = request.forms.command

    if command == str(system.COMMANDMOVE):
        user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
        if user == None:
            redirect(system.REDIRECTTOP)
        response.set_cookie(cookie.COOKIE, user, max_age=60 * 60 * 24, secret=cookie.SECRET)
        response.set_cookie(cookie.COOKIEMOVE, action, max_age=60 * 60 * 24, secret=cookie.SECRET)
        redirect(system.REDIRECTMOVE)
    if command == str(system.COMMANDCALLSOLDIER):
        response.set_cookie(cookie.COOKIECALLSOLDIER, action, max_age=60 * 60 * 24, secret=cookie.SECRET)
        redirect(system.REDIRECTCALLSOLDIER)
    if command == str(system.COMMANDATTACK):
        user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
        if user == None:
            redirect(system.REDIRECTTOP)
        response.set_cookie(cookie.COOKIE, user, max_age=60 * 60 * 24, secret=cookie.SECRET)
        response.set_cookie(cookie.COOKIEMOVE, action, max_age=60 * 60 * 24, secret=cookie.SECRET)
        redirect(system.REDIRECTATTACK)
    if command == str(system.COMMANDGUARD):
        response.set_cookie(cookie.COOKIEMOVE, action, max_age=60 * 60 * 24, secret=cookie.SECRET)
        redirect(system.REDIRECTGUARD)

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
    userTwo = normalFunction.getUser(user)

    if len(action) == 1:

        arg = {"action":command,
               "option":None,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action[0]}

        normalFunction.updateAction(arg)
    
    else:
        arg = {"action":command,
               "option":None,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action}

        normalFunction.updateActionMultiple(arg)    

    redirect(system.REDIRECTMAIN)

@route('/register')
@view('register')
def register():
    return dict(year=datetime.now().year,message = "")

@route('/commandMove')
@view('commandMove')
def commandMove():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    getSelectBoxMove = uiFunction.createSelectBoxMove(userTwo[sql.SYSTEM_USERS_MAP_CD])
    getMap = uiFunction.createMap()

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                getSelectBoxMove = getSelectBoxMove,
                getMap = getMap)

@route('/commandCallSoldier')
@view('commandCallSoldier')
def commandCallSoldier():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    getSoldier = uiFunction.createSoldierList(userTwo[sql.SYSTEM_USERS_CAMP_GROUP])

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                getSoldier = getSoldier,
                message="",
                cost = system.COSTLEADERSHIP)

@route('/commandAttack')
@view('commandAttack')
def commandAttack():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    getSelectBoxMove = uiFunction.createSelectBoxMove(userTwo[sql.SYSTEM_USERS_MAP_CD])
    getMap = uiFunction.createMap()
    getSoldier = uiFunction.createSoldierListPersonal(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                getSelectBoxMove = getSelectBoxMove,
                getMap = getMap,
                getSoldier = getSoldier)

@route('/commandGuard')
@view('commandGuard')
def commandGuard():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    getSoldier = uiFunction.createSoldierListPersonal(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                getSoldier = getSoldier)

@route('/inputSoldier' , method=["POST"])
def inputSoldier():

    action = request.get_cookie(cookie.COOKIECALLSOLDIER, secret=cookie.SECRET)
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    soldier_cd = request.forms.soldier_cd
    number = request.forms.number

    if soldier_cd == "":
        getSoldier = uiFunction.createSoldierList()
        return template('commandCallSoldier',year=datetime.now().year,getSoldier=getSoldier,message = "兵種が未入力です")
    if number == "":
        getSoldier = uiFunction.createSoldierList()
        return template('commandCallSoldier',year=datetime.now().year,getSoldier=getSoldier,message = "兵数が未入力です")

    if normalFunction.existSoldier(soldier_cd) == False:
        getSoldier = uiFunction.createSoldierList()
        return template('commandCallSoldier',year=datetime.now().year,getSoldier=getSoldier,message = "兵種が存在しません")

    if len(action) == 1:
        arg = {"action":system.COMMANDCALLSOLDIER,
               "option":soldier_cd + "," + number,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action[0]}

        normalFunction.updateAction(arg)
    
    else:
        arg = {"action":system.COMMANDCALLSOLDIER,
               "option":soldier_cd + "," + number,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action}

        normalFunction.updateActionMultiple(arg)    

    redirect(system.REDIRECTMAIN)

@route('/historyAction' , method=["POST"])
@view('historyAction')
def historyAction():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    getHistoryAction = uiFunction.createHistoryAction(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    return dict(year=datetime.now().year,
                divBaseColor = resultCreateDivBaseColor,
                getHistoryAction = getHistoryAction)

@route('/commandMoveInput' , method=["POST"])
def commandMoveInput():

    action = request.get_cookie(cookie.COOKIEMOVE, secret=cookie.SECRET)
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    if request.forms.target == "":
        getSelectBoxMove = uiFunction.createSelectBoxMove(userTwo[sql.SYSTEM_USERS_MAP_CD])
        getMap = uiFunction.createMap()
        arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
        resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)
        return template('commandMove',
                        year=datetime.now().year,
                        divBaseColor = resultCreateDivBaseColor,
                        getSelectBoxMove = getSelectBoxMove,
                        getMap = getMap)

    if len(action) == 1:
        arg = {"action":system.COMMANDMOVE,
               "option":request.forms.target,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action[0]}

        normalFunction.updateAction(arg)
    
    else:
        arg = {"action":system.COMMANDMOVE,
               "option":request.forms.target,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action}

        normalFunction.updateActionMultiple(arg)    

    redirect(system.REDIRECTMAIN)

@route('/commandAttackInput' , method=["POST"])
def commandAttackInput():

    action = request.get_cookie(cookie.COOKIEMOVE, secret=cookie.SECRET)
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    if (request.forms.target == "" or request.forms.soldier == ""):
        getSelectBoxMove = uiFunction.createSelectBoxMove(userTwo[sql.SYSTEM_USERS_MAP_CD])
        getMap = uiFunction.createMap()
        getSoldier = uiFunction.createSoldierListPersonal(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])
        arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
        resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)
        return template('commandAttack'
                        ,year=datetime.now().year
                        ,divBaseColor = resultCreateDivBaseColor
                        ,getSelectBoxMove = getSelectBoxMove
                        ,getMap = getMap
                        ,getSoldier = getSoldier)

    if len(action) == 1:
        arg = {"action":system.COMMANDATTACK,
               "option":request.forms.target + "," + request.forms.soldier,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action[0]}

        normalFunction.updateAction(arg)
    
    else:
        arg = {"action":system.COMMANDATTACK,
               "option":request.forms.target + "," + request.forms.soldier,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action}

        normalFunction.updateActionMultiple(arg)    

    redirect(system.REDIRECTMAIN)

@route('/commandGuardInput' , method=["POST"])
def commandGuardInput():

    action = request.get_cookie(cookie.COOKIEMOVE, secret=cookie.SECRET)
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)

    if (request.forms.soldier == ""):
        getSoldier = uiFunction.createSoldierListPersonal(userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD])
        return template('commandGuard'
                        ,year=datetime.now().year
                        ,getSoldier = getSoldier)

    if len(action) == 1:
        arg = {"action":system.COMMANDGUARD,
               "option":request.forms.soldier,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action[0]}

        normalFunction.updateAction(arg)
    
    else:
        arg = {"action":system.COMMANDGUARD,
               "option":request.forms.soldier,
               "system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
               "action_num":action}

        normalFunction.updateActionMultiple(arg)    

    redirect(system.REDIRECTMAIN)

@route('/registerUser' , method=["POST"])
def registerUser():

    name = request.forms.user_name
    id = request.forms.user_id
    password = request.forms.user_password
    group = request.forms.user_camp_group

    # check
    number = normalFunction.getNumberOfUser()
    if number[0][0] >= system.NumberOfRegister:
        return template('register',year=datetime.now().year,message = "ゲームの登録人数が制限に達しています")
    
    if name == "":
        return template('register',year=datetime.now().year,message = "nameが未入力です")
    if id == "":
        return template('register',year=datetime.now().year,message = "idが未入力です")
    if password == "":
        return template('register',year=datetime.now().year,message = "passwordが未入力です")
    if group == "":
        return template('register',year=datetime.now().year,message = "groupが未入力です")

    list = [system.CAMPGROUPMAGIC,system.CAMPGROUPGANG,system.CAMPGROUPPOLICE]
    if group in list :
        arg = {"name":name,"id":id,"password":password,"camp_group":group}
    else:
        return template('register',year=datetime.now().year,message = "不正な入力です")

    if normalFunction.checkUserName(arg) == False:
        return template('register',year=datetime.now().year,message = "Nameが重複しています。別のNameを設定して下さい")
    if normalFunction.checkUserId(arg) == False:
        return template('register',year=datetime.now().year,message = "Idが重複しています。別のIdを設定して下さい")
    
    # register execute
    adminFunction.registerUser(arg)
    arg = {"id":id,"password":password}
    user = normalFunction.getUser(arg)
    
    with executeSql.getConnection() as conn:
        with conn.cursor() as cur:
            argTwo = {"system_users_cd":user[sql.SYSTEM_USERS_SYSTEM_USERS_CD]}

            normalFunction.registerAction(argTwo,cur)

            normalFunction.registerActionLogs(argTwo,cur)

            normalFunction.registerQuest(argTwo,cur)

    if user == None:
        redirect(system.REDIRECTTOP)

    response.set_cookie(cookie.COOKIE, arg, max_age=60 * 60 * 24, secret=cookie.SECRET)

    if True:

        arg = {"value":system.NEWSCATEGORY003 + name + system.NEWSREGISTOR}
        normalFunction.insertNews(arg)

        redirect(system.REDIRECTMAIN)
    else:
        return template('register')

@route('/chatAll' , method=["POST"])
def chatAll():
    remark = request.forms.remark
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
    userTwo = normalFunction.getUser(user)

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
           "camp_group":None,
           "target_cd":None,
           "remark":remark,
           "remark_time":datetime.now()}

    normalFunction.insertChat(arg)

    redirect(system.REDIRECTMAIN)

@route('/chatGroup' , method=["POST"])
def chatGroup():
    remark = request.forms.remark
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
    userTwo = normalFunction.getUser(user)

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
           "camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP],
           "target_cd":None,
           "remark":remark,
           "remark_time":datetime.now()}

    normalFunction.insertChat(arg)

    redirect(system.REDIRECTMAIN)

@route('/chatPrivate' , method=["POST"])
def chatPrivate():
    remark = request.forms.remark
    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)
    userTwo = normalFunction.getUser(user)

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
           "camp_group":None,
           "target_cd":"12345",
           "remark":remark,
           "remark_time":datetime.now()}

    normalFunction.insertChat(arg)

    redirect(system.REDIRECTMAIN)

@route('/ajaxTabRight' , method=["POST"])
def ajaxTabRight():
    resultTarget = request.params.dict["target"][0]
    resultId = request.params.dict["id"][0]
    resultPassword = request.params.dict["password"][0]

    user = {"id":resultId,"password":resultPassword}
    userTwo = normalFunction.getUser(user)

    args = {"tab_right":resultTarget,"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD]}
    normalFunction.saveTabRight(args)

    pass

@route('/questCommonDetail' , method=["POST"])
@view('questCommonDetail')
def questCommonDetail():

    questCommonCd = request.forms.quest_common_cd

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    from NewFolder2.NewFolder1.const import quest

    paramQuest = ""
    paramConditions = ""
    if str(questCommonCd) == quest.CODEOFQUEST001:
        paramQuest = quest.QUEST001
        paramConditions = quest.CONDITIONS001
        paramQuestCommonCd = quest.CODEOFQUEST001
    elif str(questCommonCd) == quest.CODEOFQUEST002:
        paramQuest = quest.QUEST002
        paramConditions = quest.CONDITIONS002
        paramQuestCommonCd = quest.CODEOFQUEST002
    else:
        return dict(year=datetime.now().year,
                    divBaseColor=resultCreateDivBaseColor,
                    quest = "",
                    conditions = "",
                    executeQuestButton = "",
                    resultCheck = "",
                    resultQuest = "",
                    questCommonCd = "")

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],
           "password":userTwo[sql.SYSTEM_USERS_PASSWORD],
           "questCommonCd":questCommonCd}

    paramExecuteQuestButton = uiFunction.createExecuteQuestButton(arg)

    paramResultCheck = ""
    resultQuest = uiFunction.createQuestAfter(arg)
    return dict(year=datetime.now().year,
                divBaseColor=resultCreateDivBaseColor,
                quest = paramQuest,
                conditions = paramConditions,
                executeQuestButton = paramExecuteQuestButton ,
                resultCheck = paramResultCheck,
                resultQuest = resultQuest,
                questCommonCd = paramQuestCommonCd)

@route('/questCheck' , method=["POST"])
@view('questCommonDetail')
def questCheck():
    
    questCommonCd = request.forms.quest_common_cd

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
           "questCommonCd":questCommonCd}

    result = normalFunction.questCheck(arg)

    paramResultCheck = ""
    if result == None or result["successFlag"] == 0:
        paramResultCheck = "失敗"
    else:
        paramResultCheck = "成功。各ステータスが10、上昇しました。"

    from NewFolder2.NewFolder1.const import quest

    paramQuest = ""
    paramConditions = ""
    if str(questCommonCd) == quest.CODEOFQUEST001:
        paramQuest = quest.QUEST001
        paramConditions = quest.CONDITIONS001
        paramQuestCommonCd = quest.CODEOFQUEST001
    elif str(questCommonCd) == quest.CODEOFQUEST002:
        paramQuest = quest.QUEST002
        paramConditions = quest.CONDITIONS002
        paramQuestCommonCd = quest.CODEOFQUEST002
    else:
        return dict(year=datetime.now().year,
                    divBaseColor=resultCreateDivBaseColor,
                    quest = "",
                    conditions = "",
                    executeQuestButton = "",
                    resultCheck = "",
                    resultQuest = "",
                    questCommonCd = "")

    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],
           "password":userTwo[sql.SYSTEM_USERS_PASSWORD],
           "questCommonCd":questCommonCd}

    paramExecuteQuestButton = uiFunction.createExecuteQuestButton(arg)

    resultQuest = uiFunction.createQuestAfter(arg)
    return dict(year=datetime.now().year,
                divBaseColor=resultCreateDivBaseColor,
                quest = paramQuest,
                conditions = paramConditions,
                executeQuestButton = paramExecuteQuestButton,
                resultCheck = paramResultCheck,
                resultQuest = resultQuest,
                questCommonCd = paramQuestCommonCd)

@route('/meetingRoom')
@view('meetingRoom')
def meetingRoom():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}
    resultCreateDivBaseColor = uiFunction.createDivBaseColor(arg)

    arg = {"camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP]}
    resultBody = uiFunction.createBodyMeetingRoom(arg)

    return dict(year=datetime.now().year,
                body=resultBody,
                divBaseColor=resultCreateDivBaseColor)

@route('/inputMeetingRoom' , method=["POST"])
def inputMeetingRoom():

    user = request.get_cookie(cookie.COOKIE, secret=cookie.SECRET)

    if user == None:
        redirect(system.REDIRECTTOP)

    userTwo = normalFunction.getUser(user)
    arg = {"id":userTwo[sql.SYSTEM_USERS_ID],"password":userTwo[sql.SYSTEM_USERS_PASSWORD]}

    title = request.forms.title
    body = request.forms.body

    arg = {"system_users_cd":userTwo[sql.SYSTEM_USERS_SYSTEM_USERS_CD],
           "camp_group":userTwo[sql.SYSTEM_USERS_CAMP_GROUP],
           "title":title,
           "body":body,
           "body_time":datetime.now()}

    normalFunction.writeMeetingRoom(arg)

    redirect(system.REDIRECTMEETINGROOM)
