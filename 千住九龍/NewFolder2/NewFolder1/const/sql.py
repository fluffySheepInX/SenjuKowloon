from ..const import debug

SQLCONNECT = ""
if debug.debug:
    SQLCONNECT = ""
else:
    SQLCONNECT = "host=/tmp/"
CHATLIMIT = 100
NEWSLIMIT = 15


SYSTEM_USERS_SYSTEM_USERS_CD = 0
SYSTEM_USERS_NAME = 1
SYSTEM_USERS_ID = 2
SYSTEM_USERS_PASSWORD = 3
SYSTEM_USERS_CAMP_GROUP = 4
SYSTEM_USERS_MAIL_ADDRESS = 5
SYSTEM_USERS_INTRODUCE_MAIN = 6
SYSTEM_USERS_INTRODUCE_SUB = 7
SYSTEM_USERS_ATTACK = 8
SYSTEM_USERS_INTELLIGENCE = 9
SYSTEM_USERS_LEADERSHIP = 10
SYSTEM_USERS_ASSETS = 11
SYSTEM_USERS_WEAPON = 12
SYSTEM_USERS_WEAPON_NAME = 13
SYSTEM_USERS_FILIBUSTERS = 14
SYSTEM_USERS_FILIBUSTERS_KIND = 15
SYSTEM_USERS_MAP_CD = 16
SYSTEM_USERS_CONFIG_COLOR = 17
SYSTEM_USERS_TAB_LEFT = 18
SYSTEM_USERS_TAB_RIGHT = 19
SYSTEM_USERS_TAB_RIGHT_ALL = 20
SYSTEM_USERS_TAB_RIGHT_GROUP = 21
SYSTEM_USERS_TAB_RIGHT_PERSONAL = 22
SYSTEM_USERS_TIME_REGIST = 23
SYSTEM_USERS_TIME_UPDATE = 24

ACTION_SYSTEM_USERS_CD = 0
ACTION_ACTION_NUM = 1
ACTION_ACTION = 2
ACTION_OPTION = 3
ACTION_ACTION_TIME = 4
ACTION_ACTION_TIME_IN_THIS_WORLD = 5

MAP_MAP_CD = 0
MAP_LATITUDE_CD = 1
MAP_LONGITUDE_CD = 2
MAP_NAME = 4
MAP_CAMP_GROUP = 6

SOLDIER_CD = 0
SOLDIER_NAME = 1
SOLDIER_SPEED = 2
SOLDIER_STRENGTH = 3
SOLDIER_COST = 4
SOLDIER_HARDNESS = 6
SOLDIER_FLAVOR = 9

SOLDIER_PERSONAL_SOLDIER_PERSONAL_CD = 0
SOLDIER_PERSONAL_SYSTEM_USERS_CD = 1
SOLDIER_PERSONAL_SOLDIER_CD = 2

MANAGE_QUEST_SYSTEM_USERS_CD = 0
MANAGE_QUEST_PATROL_NUMBER = 1
MANAGE_QUEST_QUEST_NUMBER_001 = 2
MANAGE_QUEST_CALL_SOLDIER_NUMBER = 3
MANAGE_QUEST_QUEST_NUMBER_002 = 4