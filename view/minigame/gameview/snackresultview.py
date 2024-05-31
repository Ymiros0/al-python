local var_0_0 = class("SnackResultView", import("...base.BaseSubView"))

var_0_0.EXTable = {
	[0] = 0,
	1,
	2,
	5
}

def var_0_0.getUIName(arg_1_0):
	return "SnackResult"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initUI()
	arg_2_0.updateView()
	arg_2_0.Show()
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.lockBackPress = False

	pg.UIMgr.GetInstance().UnblurPanel(arg_3_0._tf)

def var_0_0.initUI(arg_4_0):
	local var_4_0 = arg_4_0.findTF("Content")

	arg_4_0.timeText = arg_4_0.findTF("Tip/Time/TimeText", var_4_0)
	arg_4_0.scoreText = arg_4_0.findTF("Tip/Score/ScoreText", var_4_0)
	arg_4_0.snackTpl = arg_4_0.findTF("SnackTpl", var_4_0)
	arg_4_0.orderListContainer = arg_4_0.findTF("Order/OrderList", var_4_0)
	arg_4_0.orderList = UIItemList.New(arg_4_0.orderListContainer, arg_4_0.snackTpl)
	arg_4_0.selectedListContainer = arg_4_0.findTF("Select/SelectList", var_4_0)
	arg_4_0.selectedList = UIItemList.New(arg_4_0.selectedListContainer, arg_4_0.snackTpl)
	arg_4_0.submitBtn = arg_4_0.findTF("Buttons/SubmitBtn", var_4_0)
	arg_4_0.continueBtn = arg_4_0.findTF("Buttons/ContinueBtn", var_4_0)

	onButton(arg_4_0, arg_4_0.submitBtn, function()
		local var_5_0 = arg_4_0.calculateLevel()

		arg_4_0.contextData.onSubmit(var_5_0)
		arg_4_0.Destroy(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.continueBtn, function()
		arg_4_0.contextData.onContinue()
		arg_4_0.Destroy())

def var_0_0.updateView(arg_7_0):
	local var_7_0 = arg_7_0.calculateEXValue()

	if arg_7_0.contextData.countTime > 0:
		setText(arg_7_0.timeText, arg_7_0.contextData.countTime .. "s   + " .. setColorStr(var_7_0 .. "s", "#3068E6FF"))
	else
		setText(arg_7_0.timeText, arg_7_0.contextData.countTime .. "s")

	setText(arg_7_0.scoreText, arg_7_0.contextData.score .. "   + " .. setColorStr(var_7_0, "#3068E6FF"))
	arg_7_0.orderList.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = arg_7_0.contextData.orderIDList[arg_8_1 + 1]
			local var_8_1 = arg_7_0.findTF("SnackImg", arg_8_2)

			setImageSprite(var_8_1, GetSpriteFromAtlas("ui/snackui_atlas", "snack_" .. var_8_0)))
	arg_7_0.orderList.align(#arg_7_0.contextData.orderIDList)
	arg_7_0.selectedList.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = arg_7_0.contextData.selectedIDList[arg_9_1 + 1]
			local var_9_1 = arg_7_0.findTF("SnackImg", arg_9_2)

			setImageSprite(var_9_1, GetSpriteFromAtlas("ui/snackui_atlas", "snack_" .. var_9_0))

			local var_9_2 = arg_7_0.contextData.orderIDList[arg_9_1 + 1]
			local var_9_3 = arg_7_0.findTF("ErrorImg", arg_9_2)
			local var_9_4 = arg_7_0.findTF("CorrectImg", arg_9_2)

			setActive(var_9_4, var_9_0 == var_9_2)
			setActive(var_9_3, var_9_0 != var_9_2))
	arg_7_0.selectedList.align(#arg_7_0.contextData.selectedIDList)

	if arg_7_0.contextData.countTime == 0:
		setActive(arg_7_0.continueBtn, False)

	arg_7_0.contextData.countTime = arg_7_0.contextData.countTime + var_7_0
	arg_7_0.contextData.score = arg_7_0.contextData.score + var_7_0

def var_0_0.calculateEXValue(arg_10_0):
	local var_10_0 = 0

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.contextData.selectedIDList):
		if arg_10_0.contextData.orderIDList[iter_10_0] == iter_10_1:
			var_10_0 = var_10_0 + 1

	return arg_10_0.contextData.correctNumToEXValue[var_10_0]

def var_0_0.calculateLevel(arg_11_0):
	if arg_11_0.contextData.score >= arg_11_0.contextData.scoreLevel[4]:
		return 1
	elif arg_11_0.contextData.score >= arg_11_0.contextData.scoreLevel[3]:
		return 2
	elif arg_11_0.contextData.score >= arg_11_0.contextData.scoreLevel[2]:
		return 3
	elif arg_11_0.contextData.score >= arg_11_0.contextData.scoreLevel[1]:
		return 4

return var_0_0
