from bottle import route, view, request, template, redirect
from datetime import datetime
from NewFolder2.NewFolder1.control import adminFunction as adminFunction
from NewFolder2.NewFolder1.control import normalFunction as normalFunction
from NewFolder2.NewFolder1.const import system

@route('/admin' , method=["POST"])
@view('admin')
def admin():
    id = request.forms.user_id
    password = request.forms.user_password

    if id == "" and password == "":
        return dict(year=datetime.now().year)

    redirect(system.REDIRECTTOP)

@route('/allCreate' , method=["POST"])
@view('admin')
def allCreate():

    adminFunction.createTableUser()
    adminFunction.createTableChatLogs()
    adminFunction.createTableMap()
    adminFunction.insertTableMap()
    adminFunction.createTableMST()
    adminFunction.insertTableMST()
    adminFunction.createTableNews()
    adminFunction.createTableAction()
    adminFunction.createTableActionLogs()
    adminFunction.createTableTime()
    adminFunction.insertTableTime()
    adminFunction.createSoldier()
    adminFunction.insertSoldier()
    adminFunction.createSoldierPersonal()
    adminFunction.createManageQuest()
    adminFunction.createMeetingRoom()

    arg = {"value":system.NEWSCATEGORY001 + system.NEWSRESET}
    normalFunction.insertNews(arg)

    return dict(year=datetime.now().year)

@route('/allDrop' , method=["POST"])
@view('admin')
def allDrop():

    try:
        adminFunction.dropTableUser()
    except :
        pass
    try:
        adminFunction.dropTableChatLogs()
    except :
        pass
    try:
        adminFunction.dropTableMap()
    except :
        pass
    try:
        adminFunction.dropTableMST()
    except :
        pass
    try:
        adminFunction.dropTableNews()
    except :
        pass
    try:
        adminFunction.dropTableAction()
    except :
        pass
    try:
        adminFunction.dropTableActionLogs()
    except :
        pass
    try:
        adminFunction.dropTableTime()
    except :
        pass
    try:
        adminFunction.dropSoldier()
    except :
        pass
    try:
        adminFunction.dropSoldierPersonal()
    except :
        pass
    try:
        adminFunction.dropManageQuest()
    except :
        pass
    try:
        adminFunction.dropMeetingRoom()
    except :
        pass

    return dict(year=datetime.now().year)

@route('/createCharaAndSpeedUp' , method=["POST"])
@view('admin')
def createCharaAndSpeedUp():

    id = request.forms.user_id
    password = request.forms.user_password
    name = "test"
    group = 1
    arg = {"name":name,"id":id,"password":password,"camp_group":group}
    adminFunction.registerUser(arg)

    arg = {"id":id,"password":password}
    user = normalFunction.getUser(arg)

    arg = {"system_users_cd":user[0]}
    normalFunction.registerAction(arg)

    normalFunction.registerActionLogs(arg)

    return dict(year=datetime.now().year)

@route('/createTableUser' , method=["POST"])
@view('admin')
def createTableUser():
    adminFunction.createTableUser()
    return dict(year=datetime.now().year)

@route('/dropTableUser' , method=["POST"])
@view('admin')
def dropTableUser():
    adminFunction.dropTableUser()
    return dict(year=datetime.now().year)

@route('/createTableChatLogs' , method=["POST"])
@view('admin')
def createTableUser():
    adminFunction.createTableChatLogs()
    return dict(year=datetime.now().year)

@route('/dropTableChatLogs' , method=["POST"])
@view('admin')
def dropTableUser():
    adminFunction.dropTableChatLogs()
    return dict(year=datetime.now().year)

@route('/createTableMap' , method=["POST"])
@view('admin')
def createTableMap():
    adminFunction.createTableMap()
    return dict(year=datetime.now().year)

@route('/dropTableMap' , method=["POST"])
@view('admin')
def dropTableMap():
    adminFunction.dropTableMap()
    return dict(year=datetime.now().year)

@route('/insertTableMap' , method=["POST"])
@view('admin')
def insertTableMap():
    adminFunction.insertTableMap()
    return dict(year=datetime.now().year)

@route('/createTableMST' , method=["POST"])
@view('admin')
def createTableMST():
    adminFunction.createTableMST()
    return dict(year=datetime.now().year)

@route('/dropTableMST' , method=["POST"])
@view('admin')
def dropTableMST():
    adminFunction.dropTableMST()
    return dict(year=datetime.now().year)

@route('/insertTableMST' , method=["POST"])
@view('admin')
def insertTableMST():
    adminFunction.insertTableMST()
    return dict(year=datetime.now().year)

@route('/createTableNews' , method=["POST"])
@view('admin')
def createTableNews():
    adminFunction.createTableNews()
    return dict(year=datetime.now().year)

@route('/dropTableNews' , method=["POST"])
@view('admin')
def dropTableNews():
    adminFunction.dropTableNews()
    return dict(year=datetime.now().year)

@route('/createTableAction' , method=["POST"])
@view('admin')
def createTableAction():
    adminFunction.createTableAction()
    return dict(year=datetime.now().year)

@route('/dropTableAction' , method=["POST"])
@view('admin')
def dropTableAction():
    adminFunction.dropTableAction()
    return dict(year=datetime.now().year)

@route('/createTableActionLogs' , method=["POST"])
@view('admin')
def createTableActionLogs():
    adminFunction.createTableActionLogs()
    return dict(year=datetime.now().year)

@route('/dropTableActionLogs' , method=["POST"])
@view('admin')
def dropTableActionLogs():
    adminFunction.dropTableActionLogs()
    return dict(year=datetime.now().year)

@route('/createTableTime' , method=["POST"])
@view('admin')
def createTableTime():
    adminFunction.createTableTime()
    return dict(year=datetime.now().year)

@route('/dropTableTime' , method=["POST"])
@view('admin')
def dropTableTime():
    adminFunction.dropTableTime()
    return dict(year=datetime.now().year)

@route('/insertTableTime' , method=["POST"])
@view('admin')
def insertTableTime():
    adminFunction.insertTableTime()
    return dict(year=datetime.now().year)

@route('/createSoldier' , method=["POST"])
@view('admin')
def createSoldier():
    adminFunction.createSoldier()
    return dict(year=datetime.now().year)

@route('/dropSoldier' , method=["POST"])
@view('admin')
def dropSoldier():
    adminFunction.dropSoldier()
    return dict(year=datetime.now().year)

@route('/insertSoldier' , method=["POST"])
@view('admin')
def insertSoldier():
    adminFunction.insertSoldier()
    return dict(year=datetime.now().year)

@route('/createSoldierPersonal' , method=["POST"])
@view('admin')
def createSoldierPersonal():
    adminFunction.createSoldierPersonal()
    return dict(year=datetime.now().year)

@route('/dropSoldierPersonal' , method=["POST"])
@view('admin')
def dropSoldierPersonal():
    adminFunction.dropSoldierPersonal()
    return dict(year=datetime.now().year)

@route('/createManageQuest' , method=["POST"])
@view('admin')
def createManageQuest():
    adminFunction.createManageQuest()
    return dict(year=datetime.now().year)

@route('/dropManageQuest' , method=["POST"])
@view('admin')
def dropManageQuest():
    adminFunction.dropManageQuest()
    return dict(year=datetime.now().year)

@route('/createMeetingRoom' , method=["POST"])
@view('admin')
def createMeetingRoom():
    adminFunction.createMeetingRoom()
    return dict(year=datetime.now().year)

@route('/dropMeetingRoom' , method=["POST"])
@view('admin')
def dropMeetingRoom():
    adminFunction.dropMeetingRoom()
    return dict(year=datetime.now().year)
