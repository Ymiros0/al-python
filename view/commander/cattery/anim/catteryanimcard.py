local var_0_0 = class("CatteryAnimCard", import("..CatterySettlementCard"))
local var_0_1 = 1

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.emptyTF = findTF(arg_1_0._tf, "empty")
	arg_1_0.commanderTF = findTF(arg_1_0._tf, "commander")
	arg_1_0.char = arg_1_0.commanderTF.Find("mask/char")
	arg_1_0.slider = arg_1_0.commanderTF.Find("slider").GetComponent(typeof(Slider))
	arg_1_0.nameTxt = arg_1_0.commanderTF.Find("name/Text").GetComponent(typeof(Text))
	arg_1_0.levelTxt = arg_1_0.commanderTF.Find("name/level").GetComponent(typeof(Text))
	arg_1_0.expTxt = arg_1_0.commanderTF.Find("exp").GetComponent(typeof(Text))
	arg_1_0.addition = arg_1_0.commanderTF.Find("addition")
	arg_1_0.additionTxt = arg_1_0.addition.Find("Text").GetComponent(typeof(Text))
	arg_1_0.additionY = arg_1_0.addition.localPosition.y

def var_0_0.UpdateCommander(arg_2_0):
	var_0_0.super.UpdateCommander(arg_2_0)

	arg_2_0.additionTxt.text = arg_2_0.exp .. "<size=40>EXP</size>"

def var_0_0.Action(arg_3_0, arg_3_1):
	setActive(arg_3_0.addition, False)

	if not arg_3_0.commander or arg_3_0.exp <= 0:
		arg_3_1()

		return

	local var_3_0 = {}

	arg_3_0.InitAnim(var_3_0)
	table.insert(var_3_0, function(arg_4_0)
		arg_3_0.AdditionAnim(var_0_1, arg_4_0))
	parallelAsync(var_3_0, arg_3_1)

def var_0_0.Clear(arg_5_0):
	var_0_0.super.Clear(arg_5_0)

	if LeanTween.isTweening(go(arg_5_0.addition)):
		LeanTween.cancel(go(arg_5_0.addition))

def var_0_0.LoadCommander(arg_6_0, arg_6_1):
	arg_6_0.ReturnCommander()

	arg_6_0.painting = arg_6_1.getPainting()

	setCommanderPaintingPrefab(arg_6_0.char, arg_6_0.painting, "result1")

def var_0_0.AdditionAnim(arg_7_0, arg_7_1, arg_7_2):
	setActive(arg_7_0.addition, True)

	local var_7_0 = arg_7_0.additionY

	LeanTween.value(go(arg_7_0.addition), var_7_0, var_7_0 + 25, arg_7_1).setOnUpdate(System.Action_float(function(arg_8_0)
		arg_7_0.addition.localPosition = Vector3(arg_7_0.addition.localPosition.x, arg_8_0, 0))).setOnComplete(System.Action(function()
		setActive(arg_7_0.addition, False)
		arg_7_2()

		arg_7_0.addition.localPosition = Vector3(arg_7_0.addition.localPosition.x, var_7_0, 0)))

def var_0_0.GetColor(arg_10_0):
	return "#ffffff"

return var_0_0
