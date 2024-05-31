local var_0_0 = class("CatteryDescPage", import("...base.BaseSubView"))

var_0_0.CHANGE_STYLE = "CatteryDescPage.CHANGE_STYLE"
var_0_0.CHANGE_COMMANDER = "CatteryDescPage.CHANGE_COMMANDER"

def var_0_0.getUIName(arg_1_0):
	return "CatteryDescPage"

def var_0_0.OnCatteryUpdate(arg_2_0, arg_2_1):
	arg_2_0.Flush(arg_2_1)

	if arg_2_0.page and arg_2_0.page.GetLoaded() and arg_2_0.page.isShowing():
		arg_2_0.page.OnCatteryUpdate(arg_2_1)

def var_0_0.OnCatteryStyleUpdate(arg_3_0, arg_3_1):
	arg_3_0.cattery = arg_3_1

	arg_3_0.UpdateCatteryStyle()

	if arg_3_0.page and arg_3_0.page.GetLoaded() and arg_3_0.page.isShowing() and isa(arg_3_0.page, CommanderHomeSelCatteryStylePage):
		arg_3_0.page.OnCatteryStyleUpdate(arg_3_1)

def var_0_0.OnLoaded(arg_4_0):
	arg_4_0.closeBtn = arg_4_0.findTF("right/close_btn")
	arg_4_0.styleIcon = arg_4_0.findTF("left/bg/mask/icon").GetComponent(typeof(Image))
	arg_4_0.char = arg_4_0.findTF("left/bg/char")
	arg_4_0.commanderEmpty = arg_4_0.findTF("left/bg/info/empty")
	arg_4_0.styleInfo = arg_4_0.commanderEmpty
	arg_4_0.commanderExp = arg_4_0.findTF("left/bg/info/commander_exp")
	arg_4_0.commanderLevelTxt = arg_4_0.commanderExp.Find("level/Text").GetComponent(typeof(Text))
	arg_4_0.commanderExpTxt = arg_4_0.commanderExp.Find("value_bg/Text").GetComponent(typeof(Text))
	arg_4_0.commanderExpImg = arg_4_0.commanderExp.Find("exp/Image")
	arg_4_0.pageContainer = arg_4_0._tf.Find("")
	arg_4_0.toggleGroup = arg_4_0.findTF("left/tags").GetComponent(typeof(ToggleGroup))
	arg_4_0.pagesTF = arg_4_0.findTF("right/pages")
	arg_4_0.tags = {
		arg_4_0.findTF("left/tags/commander"),
		arg_4_0.findTF("left/tags/home")
	}
	arg_4_0.pages = {
		CommanderHomeSelCommanderPage.New(arg_4_0.pagesTF, arg_4_0.event),
		CommanderHomeSelCatteryStylePage.New(arg_4_0.pagesTF, arg_4_0.event)
	}

def var_0_0.OnInit(arg_5_0):
	arg_5_0.bind(var_0_0.CHANGE_STYLE, function(arg_6_0, arg_6_1)
		arg_5_0.PreviewCatteryStyle(arg_6_1), SFX_PANEL)
	arg_5_0.bind(var_0_0.CHANGE_COMMANDER, function(arg_7_0, arg_7_1)
		arg_5_0.PreviewCatteryCommader(arg_7_1))
	onButton(arg_5_0, arg_5_0._tf, function()
		arg_5_0.Hide(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.closeBtn, function()
		arg_5_0.Hide(), SFX_PANEL)

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.tags):
		onToggle(arg_5_0, iter_5_1, function(arg_10_0)
			if arg_10_0:
				arg_5_0.SwitchPage(iter_5_0), SFX_PANEL)

def var_0_0.SwitchPage(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.pages[arg_11_1]

	if arg_11_0.page == var_11_0:
		return

	if arg_11_0.page:
		arg_11_0.page.Hide()

	var_11_0.ExecuteAction("Update", arg_11_0.home, arg_11_0.cattery)

	arg_11_0.page = var_11_0

	local var_11_1 = isa(var_11_0, CommanderHomeSelCatteryStylePage)

	setActive(arg_11_0.commanderEmpty, var_11_1)
	setActive(arg_11_0.commanderExp, not var_11_1)
	arg_11_0.FlushCatteryInfo()

def var_0_0.Update(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0.Show()

	arg_12_0.home = arg_12_1
	arg_12_0.cattery = arg_12_2
	arg_12_0.page = None

	triggerToggle(arg_12_0.tags[1], True)

	if arg_12_2:
		arg_12_0.Flush(arg_12_2)

def var_0_0.Show(arg_13_0):
	var_0_0.super.Show(arg_13_0)
	arg_13_0.emit(CommanderHomeLayer.DESC_PAGE_OPEN)

def var_0_0.Flush(arg_14_0, arg_14_1):
	arg_14_0.cattery = arg_14_1

	arg_14_0.FlushCatteryInfo()
	arg_14_0.UpdateCatteryStyle()

def var_0_0.FlushCatteryInfo(arg_15_0):
	local var_15_0 = False

	if isa(arg_15_0.page, CommanderHomeSelCommanderPage):
		local var_15_1 = arg_15_0.cattery.ExistCommander()

	arg_15_0.UpdateCommander(arg_15_0.cattery.GetCommander())

	local var_15_2 = arg_15_0.home

def var_0_0.UpdateCommander(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_1 != None

	arg_16_0.ReturnChar()

	if var_16_0:
		arg_16_0.LoadChar(arg_16_1)

		arg_16_0.commanderLevelTxt.text = "LV." .. arg_16_1.getLevel()

		if arg_16_1.isMaxLevel():
			arg_16_0.commanderExpTxt.text = "MAX"

			setFillAmount(arg_16_0.commanderExpImg, 1)
		else
			arg_16_0.commanderExpTxt.text = "<color=#92FC63FF>" .. arg_16_1.exp .. "</color>/" .. arg_16_1.getNextLevelExp()

			setFillAmount(arg_16_0.commanderExpImg, arg_16_1.exp / arg_16_1.getNextLevelExp())

	setActive(arg_16_0.commanderExp, var_16_0)
	setActive(arg_16_0.commanderEmpty, not var_16_0)

def var_0_0.PreviewCatteryCommader(arg_17_0, arg_17_1):
	arg_17_0.UpdateCommander(arg_17_1)

def var_0_0.UpdateCatteryStyle(arg_18_0):
	local var_18_0 = arg_18_0.cattery
	local var_18_1 = var_18_0._GetStyle_()

	if var_18_0.ExistCommander():
		arg_18_0.styleIcon.sprite = GetSpriteFromAtlas("CatteryStyle/" .. var_18_1.GetName(var_18_0.IsDirty()), "")
	else
		arg_18_0.styleIcon.sprite = GetSpriteFromAtlas("CatteryStyle/" .. var_18_1.GetName(False), "")

def var_0_0.PreviewCatteryStyle(arg_19_0, arg_19_1):
	local var_19_0 = pg.commander_home_style[arg_19_1].name

	arg_19_0.styleIcon.sprite = GetSpriteFromAtlas("CatteryStyle/" .. var_19_0, "")

def var_0_0.LoadChar(arg_20_0, arg_20_1):
	arg_20_0.painting = arg_20_1.getPainting()

	setCommanderPaintingPrefab(arg_20_0.char, arg_20_0.painting, "info")

def var_0_0.ReturnChar(arg_21_0):
	if arg_21_0.painting:
		retCommanderPaintingPrefab(arg_21_0.char, arg_21_0.painting)

		arg_21_0.painting = None

def var_0_0.Hide(arg_22_0):
	arg_22_0.emit(CommanderHomeLayer.DESC_PAGE_CLOSE)
	arg_22_0.toggleGroup.SetAllTogglesOff()
	var_0_0.super.Hide(arg_22_0)

	for iter_22_0, iter_22_1 in pairs(arg_22_0.pages):
		if iter_22_1.GetLoaded() and iter_22_1.isShowing():
			iter_22_1.Hide()

def var_0_0.OnDestroy(arg_23_0):
	arg_23_0.ReturnChar()

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.pages):
		iter_23_1.Destroy()

return var_0_0
