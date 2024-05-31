local var_0_0 = class("NewServerMainPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.time = arg_1_0.findTF("time", arg_1_0.bg)
	arg_1_0.shopBtn = arg_1_0.findTF("btn_list/shop", arg_1_0.bg)
	arg_1_0.fightBtn = arg_1_0.findTF("btn_list/fight", arg_1_0.bg)
	arg_1_0.buildBtn = arg_1_0.findTF("btn_list/build", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	onButton(arg_2_0, arg_2_0.shopBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.NEW_SERVER_CARNIVAL, {
			page = NewServerCarnivalScene.SHOP_PAGE
		}))
	onButton(arg_2_0, arg_2_0.buildBtn, function()
		local var_4_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD)

		if var_4_0 and not var_4_0.isEnd():
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
				page = BuildShipScene.PAGE_NEWSERVER
			})
		else
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT))
	onButton(arg_2_0, arg_2_0.fightBtn, function()
		arg_2_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA))
	arg_2_0.updateTime()

def var_0_0.updateTime(arg_6_0):
	local var_6_0 = pg.TimeMgr.GetInstance()
	local var_6_1 = var_6_0.STimeDescS(arg_6_0.activity.getStartTime(), "%m.%d")
	local var_6_2 = var_6_0.STimeDescS(arg_6_0.activity.stopTime, "%m.%d %H.%M")

	setText(arg_6_0.time, var_6_1 .. " - " .. var_6_2)

def var_0_0.OnUpdateFlush(arg_7_0):
	return

return var_0_0
