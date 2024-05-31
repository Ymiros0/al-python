ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleConfig
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleFleetIconList = class("CardPuzzleFleetIconList")

local var_0_4 = var_0_0.Battle.CardPuzzleFleetIconList

var_0_4.__name = "CardPuzzleFleetIconList"

def var_0_4.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.init()

def var_0_4.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	var_0_0.EventListener.AttachEventListener(arg_2_0)

	arg_2_0._info = arg_2_1
	arg_2_0._attrManager = arg_2_0._info.GetAttrManager()
	arg_2_0._buffManager = arg_2_0._info.GetBuffManager()

	arg_2_0._info.RegisterEventListener(arg_2_0, var_0_3.UPDATE_FLEET_ATTR, arg_2_0.onUpdateFleetAttr)

def var_0_4.init(arg_3_0):
	arg_3_0._buffIconList = {}
	arg_3_0._attrIconList = {}
	arg_3_0._tf = arg_3_0._go.transform
	arg_3_0._iconTpl = arg_3_0._tf.Find("icon_tpl")
	arg_3_0._iconContainer = arg_3_0._tf.Find("icon_list")

def var_0_4.AddBuffIcon(arg_4_0, arg_4_1):
	local var_4_0 = cloneTplTo(arg_4_0._iconTpl, arg_4_0._iconContainer)
	local var_4_1 = var_4_0.Find("count_bg/count_label")
	local var_4_2 = var_4_0.Find("icon")
	local var_4_3 = var_4_0.Find("buff_duration").GetComponent(typeof(Image))
	local var_4_4 = {
		tf = var_4_0,
		count = var_4_1,
		durationIMG = var_4_3,
		buffID = arg_4_1
	}

	arg_4_0._buffIconList[arg_4_1] = var_4_4

	arg_4_0.updateBuffIcon(var_4_4)

def var_0_4.AddAttrIcon(arg_5_0, arg_5_1):
	local var_5_0 = cloneTplTo(arg_5_0._iconTpl, arg_5_0._iconContainer)
	local var_5_1 = var_5_0.Find("count_bg/count_label")
	local var_5_2 = var_5_0.Find("icon")
	local var_5_3 = {
		tf = var_5_0,
		count = var_5_1,
		attr = arg_5_1
	}

	arg_5_0._attrIconList[arg_5_1] = var_5_3

	arg_5_0.updateAttrIcon(var_5_3)

def var_0_4.onUpdateFleetAttr(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.Data.attrName

	if var_0_2.FleetIconRegisterAttr[var_6_0]:
		local var_6_1 = arg_6_0._attrIconList[var_6_0]

		if var_6_1:
			arg_6_0.updateAttrIcon(var_6_1)
		else
			arg_6_0.AddAttrIcon(var_6_0)

def var_0_4.updateAttrIcon(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.count
	local var_7_1 = arg_7_1.attr
	local var_7_2 = arg_7_0._attrManager.GetCurrent(var_7_1)

	setText(var_7_0, var_7_2)

def var_0_4.updateBuffIcon(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.buffID
	local var_8_1 = arg_8_0._buffManager.GetCardPuzzleBuff(var_8_0)
	local var_8_2 = arg_8_1.count
	local var_8_3 = var_8_1.GetStack()

	setText(var_8_2, var_8_3)

	arg_8_1.durationIMG.fillAmount = var_8_1.GetDurationRate()

def var_0_4.Update(arg_9_0):
	local var_9_0 = arg_9_0._buffManager.GetCardPuzzleBuffList()

	for iter_9_0, iter_9_1 in pairs(var_9_0):
		if var_0_2.FleetIconRegisterBuff[iter_9_0]:
			local var_9_1 = arg_9_0._buffIconList[iter_9_0]

			if var_9_1 == None:
				arg_9_0.AddBuffIcon(iter_9_0)
			else
				arg_9_0.updateBuffIcon(var_9_1)

def var_0_4.Dispose(arg_10_0):
	arg_10_0._buffIconList = None
	arg_10_0._attrIconList = None
	arg_10_0._tf = None
	arg_10_0._iconTpl = None
	arg_10_0._iconContainer = None
