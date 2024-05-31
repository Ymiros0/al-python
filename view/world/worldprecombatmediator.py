local var_0_0 = class("WorldPreCombatMediator", import("..base.ContextMediator"))

var_0_0.OnSwitchShip = "WorldPreCombatMediator.OnSwitchShip"
var_0_0.OnMapOp = "WorldPreCombatMediator.OnMapOp"
var_0_0.OnAuto = "WorldPreCombatMediator.OnAuto"
var_0_0.OnSubAuto = "WorldPreCombatMediator.OnSubAuto"
var_0_0.OnStartBattle = "WorldPreCombatMediator.OnStartBattle"
var_0_0.OnOpenSublayer = "OpenSublayer"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OnSwitchShip, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		nowWorld().GetFleet(arg_2_1).SwitchShip(arg_2_2, arg_2_3))
	arg_1_0.bind(var_0_0.OnAuto, function(arg_3_0, arg_3_1)
		arg_1_0.onAutoBtn(arg_3_1))
	arg_1_0.bind(var_0_0.OnSubAuto, function(arg_4_0, arg_4_1)
		arg_1_0.onSubAuto(arg_4_1))
	arg_1_0.bind(var_0_0.OnMapOp, function(arg_5_0, arg_5_1)
		arg_1_0.sendNotification(GAME.WORLD_MAP_OP, arg_5_1))
	arg_1_0.bind(var_0_0.OnStartBattle, function(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
		if arg_6_2.damageLevel > arg_6_3.GetLimitDamageLevel():
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideYes = True,
				content = i18n("world_low_morale")
			})
		else
			arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
				system = SYSTEM_WORLD,
				stageId = arg_6_1
			}))
	arg_1_0.bind(var_0_0.OnOpenSublayer, function(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
		arg_1_0.addSubLayers(arg_7_1, arg_7_2, arg_7_3))
	arg_1_0.viewComponent.setPlayerInfo(getProxy(PlayerProxy).getRawData())

def var_0_0.onAutoBtn(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.isOn
	local var_8_1 = arg_8_1.toggle

	arg_8_0.sendNotification(GAME.AUTO_BOT, {
		isActiveBot = var_8_0,
		toggle = var_8_1,
		system = SYSTEM_WORLD
	})

def var_0_0.onSubAuto(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.isOn
	local var_9_1 = arg_9_1.toggle
	local var_9_2 = arg_9_1.system

	arg_9_0.sendNotification(GAME.AUTO_SUB, {
		isActiveSub = var_9_0,
		toggle = var_9_1,
		system = SYSTEM_WORLD
	})

def var_0_0.listNotificationInterests(arg_10_0):
	return {
		PlayerProxy.UPDATED,
		GAME.WORLD_MAP_OP_DONE
	}

def var_0_0.handleNotification(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.getName()
	local var_11_1 = arg_11_1.getBody()

	if var_11_0 == PlayerProxy.UPDATED:
		arg_11_0.viewComponent.setPlayerInfo(getProxy(PlayerProxy).getRawData())
	elif var_11_0 == GAME.WORLD_MAP_OP_DONE:
		-- block empty

return var_0_0
