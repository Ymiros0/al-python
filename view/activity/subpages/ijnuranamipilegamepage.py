local var_0_0 = class("IJNUranamiPileGamePage", import("view.base.BaseActivityPage"))

var_0_0.MINIGAME_HUB_ID = 39
var_0_0.MINIGAME_ID = 47

def var_0_0.OnInit(arg_1_0):
	arg_1_0.goBtn = arg_1_0.findTF("AD/go")
	arg_1_0.indexTpl = arg_1_0.findTF("AD/index")
	arg_1_0.markContainer = arg_1_0.findTF("AD/marks")
	arg_1_0.markTpl = arg_1_0.findTF("AD/marks/1")
	arg_1_0.markTrs = {}

	for iter_1_0 = 1, 7:
		local var_1_0 = cloneTplTo(arg_1_0.markTpl, arg_1_0.markContainer, iter_1_0)

		table.insert(arg_1_0.markTrs, var_1_0)

def var_0_0.OnDataSetting(arg_2_0):
	return

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.goBtn, function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, var_0_0.MINIGAME_ID), SFX_PANEL)

	local var_3_0 = getProxy(MiniGameProxy).GetHubByHubId(var_0_0.MINIGAME_HUB_ID)

	arg_3_0.FlushMarks(var_3_0)
	Canvas.ForceUpdateCanvases()
	arg_3_0.FlushIndex(var_3_0)

def var_0_0.FlushMarks(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.usedtime
	local var_5_1 = var_5_0 + arg_5_1.count

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.markTrs):
		setActive(iter_5_1, iter_5_0 <= var_5_1)
		setActive(iter_5_1.Find("finish"), iter_5_0 <= var_5_0)

def var_0_0.FlushIndex(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.usedtime

	setActive(arg_6_0.indexTpl, var_6_0 > 0)

	if var_6_0 > 0:
		local var_6_1 = arg_6_0.markTrs[math.min(var_6_0, #arg_6_0.markTrs)]
		local var_6_2 = arg_6_0.indexTpl.parent.InverseTransformPoint(var_6_1.position)

		arg_6_0.indexTpl.localPosition = Vector3(var_6_2.x, var_6_2.y, 0)

def var_0_0.OnUpdateFlush(arg_7_0):
	return

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
