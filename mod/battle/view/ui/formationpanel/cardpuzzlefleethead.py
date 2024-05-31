ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleFleetHead = class("CardPuzzleFleetHead")

local var_0_3 = var_0_0.Battle.CardPuzzleFleetHead

var_0_3.__name = "CardPuzzleFleetHead"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_0._go.transform
	arg_1_0._mainIcon = arg_1_0._tf.Find("main/icon")
	arg_1_0._scoutIcon = arg_1_0._tf.Find("scout/icon")
	arg_1_0._testAttrContainer = arg_1_0._tf.Find("test_attr_list")
	arg_1_0._testAttrTpl = arg_1_0._tf.Find("test_attr_tpl")
	arg_1_0._testAttrList = {}
	arg_1_0._loader = AutoLoader.New()

def var_0_3.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	var_0_0.EventListener.AttachEventListener(arg_2_0)

	arg_2_0._info = arg_2_1

	if TEST_ATTR_PANEL:
		arg_2_0._info.RegisterEventListener(arg_2_0, var_0_2.UPDATE_FLEET_ATTR, arg_2_0.onUpdateFleetAttr)
		arg_2_0.onUpdateFleetAttr()

def var_0_3.Update(arg_3_0):
	return

def var_0_3.UpdateShipIcon(arg_4_0, arg_4_1):
	local var_4_0
	local var_4_1

	if arg_4_1 == TeamType.TeamPos.FLAG_SHIP:
		var_4_0 = arg_4_0._info.GetMainUnit()
		var_4_1 = arg_4_0._mainIcon
	elif arg_4_1 == TeamType.TeamPos.LEADER:
		var_4_0 = arg_4_0._info.GetScoutUnit()
		var_4_1 = arg_4_0._scoutIcon

	local var_4_2 = CardPuzzleShip.getPaintingName(var_4_0.GetTemplate().id)

	arg_4_0._loader.GetSprite("cardtowerselectships/" .. var_4_2 .. "_select", "", var_4_1)

def var_0_3.UpdateShipBuff(arg_5_0):
	return

def var_0_3.onUpdateFleetAttr(arg_6_0):
	local var_6_0 = arg_6_0._info.GetAttrManager()._attrList

	for iter_6_0, iter_6_1 in pairs(var_6_0):
		if arg_6_0._testAttrList[iter_6_0] == None:
			local var_6_1 = cloneTplTo(arg_6_0._testAttrTpl, arg_6_0._testAttrContainer)

			arg_6_0._testAttrList[iter_6_0] = var_6_1

			setText(var_6_1.Find("name"), iter_6_0)

		local var_6_2 = arg_6_0._testAttrList[iter_6_0]
		local var_6_3 = arg_6_0._info.GetAttrManager().GetCurrent(iter_6_0)

		setText(var_6_2.Find("value"), var_6_3)

def var_0_3.updateHPBar(arg_7_0):
	return

def var_0_3.Dispose(arg_8_0):
	arg_8_0._mainIcon = None
	arg_8_0._scoutIcon = None
	arg_8_0._testAttrContainer = None
	arg_8_0._testAttrTpl = None
	arg_8_0._testAttrList = None

	arg_8_0._loader.Clear()
