local var_0_0 = class("NewNavalTacticsStudentsPage", import("....base.BaseSubView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3

def var_0_0.getUIName(arg_1_0):
	return "NewNavalTacticsStudentsPage"

def var_0_0.OnUnlockSlot(arg_2_0):
	arg_2_0.Flush()

def var_0_0.OnAddStudent(arg_3_0):
	arg_3_0.Flush()

def var_0_0.OnExitStudent(arg_4_0):
	arg_4_0.Flush()

def var_0_0.OnLoaded(arg_5_0):
	arg_5_0.helpBtn = arg_5_0.findTF("help_btn")

	local var_5_0 = arg_5_0.findTF("info")
	local var_5_1 = arg_5_0.findTF("add")
	local var_5_2 = arg_5_0.findTF("lock")

	arg_5_0.cards = {
		{},
		{},
		{}
	}

	table.insert(arg_5_0.cards[var_0_1], NewNavalTacticsShipCard.New(var_5_0, arg_5_0.event))
	table.insert(arg_5_0.cards[var_0_2], NewNavalTacticsEmptyCard.New(var_5_1, arg_5_0.event))
	table.insert(arg_5_0.cards[var_0_3], NewNavalTacticsLockCard.New(var_5_2, arg_5_0.event))

def var_0_0.OnInit(arg_6_0):
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.tactics_lesson_system_introduce.tip
		}), SFX_PANEL)

def var_0_0.Show(arg_8_0, arg_8_1):
	var_0_0.super.Show(arg_8_0)

	arg_8_0.students = arg_8_1

	arg_8_0.Flush()

def var_0_0.Flush(arg_9_0):
	local var_9_0 = {
		0,
		0,
		0
	}
	local var_9_1 = getProxy(NavalAcademyProxy).getSkillClassNum()

	for iter_9_0 = 1, NavalAcademyProxy.MAX_SKILL_CLASS_NUM:
		local var_9_2 = arg_9_0.GetCardType(iter_9_0, var_9_1)

		var_9_0[var_9_2] = var_9_0[var_9_2] + 1

		arg_9_0.UpdateTypeCard(var_9_2, var_9_0[var_9_2], iter_9_0)

	for iter_9_1, iter_9_2 in ipairs(var_9_0):
		arg_9_0.ClearDisableCards(iter_9_1, iter_9_2)

def var_0_0.GetCardType(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_2 < arg_10_1:
		return var_0_3
	else
		return arg_10_0.students[arg_10_1] and var_0_1 or var_0_2

def var_0_0.UpdateTypeCard(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0 = arg_11_0.cards[arg_11_1]
	local var_11_1 = var_11_0[arg_11_2]

	if not var_11_1:
		var_11_1 = var_11_0[1].Clone()
		var_11_0[arg_11_2] = var_11_1

	var_11_1.Enable()

	local var_11_2 = arg_11_0.students[arg_11_3]

	var_11_1.Update(arg_11_3, var_11_2)

def var_0_0.ClearDisableCards(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_0.cards[arg_12_1]

	for iter_12_0 = #var_12_0, arg_12_2 + 1, -1:
		var_12_0[iter_12_0].Disable()

def var_0_0.GetCard(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.cards[var_0_1]

	return underscore.detect(var_13_0, function(arg_14_0)
		return arg_14_0.index == arg_13_1)

def var_0_0.OnDestroy(arg_15_0):
	for iter_15_0, iter_15_1 in ipairs(arg_15_0.cards):
		for iter_15_2, iter_15_3 in ipairs(iter_15_1):
			iter_15_3.Dispose()

	arg_15_0.cards = None

return var_0_0
