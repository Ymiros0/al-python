local var_0_0 = class("BaseAssignedShipScene", import("...base.BaseUI"))

var_0_0.TipWords = {
	login_year = "nine_choose_one",
	login_santa = "five_choose_one",
	shrine_year = "seven_choose_one",
	greeting_year = "spring_invited_2021"
}

def var_0_0.getUIName(arg_1_0):
	assert(False)

def var_0_0.setItemVO(arg_2_0, arg_2_1):
	arg_2_0.itemVO = arg_2_1
	arg_2_0.idList = arg_2_0.itemVO.getConfig("usage_arg")
	arg_2_0.shipIdList = underscore.map(arg_2_0.idList, function(arg_3_0)
		return pg.item_usage_invitation[arg_3_0].ship_id)
	arg_2_0.style, arg_2_0.title = unpack(arg_2_0.itemVO.getConfig("open_ui"))
	arg_2_0.strTip = var_0_0.TipWords[arg_2_0.style]

def var_0_0.init(arg_4_0):
	local var_4_0 = arg_4_0._tf.Find("layer")

	arg_4_0.backBtn = var_4_0.Find("back")
	arg_4_0.confirmBtn = var_4_0.Find("confirm")
	arg_4_0.print = var_4_0.Find("print")
	arg_4_0.rtName = var_4_0.Find("name")
	arg_4_0.rtTitle = var_4_0.Find("title")
	arg_4_0.selectPanel = var_4_0.Find("select_panel/layout")
	arg_4_0.itemList = UIItemList.New(arg_4_0.selectPanel, arg_4_0.selectPanel.Find("item"))

	arg_4_0.itemList.make(function(arg_5_0, arg_5_1, arg_5_2)
		arg_5_1 = arg_5_1 + 1

		local var_5_0 = arg_4_0.shipIdList[arg_5_1]

		if arg_5_0 == UIItemList.EventUpdate:
			GetImageSpriteFromAtlasAsync("extra_page/" .. arg_4_0.style .. "/i_" .. var_5_0, "", arg_5_2)
			GetImageSpriteFromAtlasAsync("extra_page/" .. arg_4_0.style .. "/is_" .. var_5_0, "", arg_5_2.Find("selected"))
			onToggle(arg_4_0, arg_5_2, function(arg_6_0)
				if arg_6_0 and arg_4_0.selectTarget != arg_5_1:
					LeanTween.cancel(arg_4_0.print)

					if arg_4_0.rtName:
						LeanTween.cancel(arg_4_0.rtName)

					arg_4_0.setSelectTarget(arg_5_1), SFX_PANEL))

	arg_4_0.selectTarget = None
	arg_4_0.count = 1
	arg_4_0.spList = {}
	arg_4_0.afterAnima = {}

def var_0_0.didEnter(arg_7_0):
	onButton(arg_7_0, arg_7_0.backBtn, function()
		arg_7_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	onButton(arg_7_0, arg_7_0.confirmBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n(arg_7_0.strTip, pg.ship_data_statistics[arg_7_0.selectedShipNumber].name),
			def onYes:()
				arg_7_0.emit(AssignedShipMediator.ON_USE_ITEM, arg_7_0.itemVO.id, arg_7_0.count, {
					arg_7_0.idList[arg_7_0.selectTarget]
				})
		}), SFX_PANEL)
	arg_7_0.itemList.align(#arg_7_0.idList)
	setActive(arg_7_0.rtTitle, arg_7_0.title)

	if arg_7_0.title:
		GetImageSpriteFromAtlasAsync("extra_page/" .. arg_7_0.style .. "/" .. arg_7_0.title, "", arg_7_0.rtTitle, True)

	triggerToggle(arg_7_0.selectPanel.GetChild(0), True)

def var_0_0.checkAndSetSprite(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_0.spList[arg_11_1] and arg_11_0.afterAnima[arg_11_1]:
		setImageSprite(arg_11_2, arg_11_0.spList[arg_11_1], True)

		arg_11_2.GetComponent(typeof(Image)).enabled = True
		arg_11_0.spList[arg_11_1] = None
		arg_11_0.afterAnima[arg_11_1] = None

		LeanTween.alpha(arg_11_2, 1, 0.3).setFrom(0)

def var_0_0.changeShowCharacter(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	if arg_12_3:
		LeanTween.alpha(rtf(arg_12_2), 0, 0.3).setOnComplete(System.Action(function()
			arg_12_2.GetComponent(typeof(Image)).enabled = False
			arg_12_0.afterAnima[arg_12_1] = True

			arg_12_0.checkAndSetSprite(arg_12_1, arg_12_2)))
	else
		arg_12_2.GetComponent(typeof(Image)).enabled = False
		arg_12_0.afterAnima[arg_12_1] = True

	GetSpriteFromAtlasAsync("extra_page/" .. arg_12_0.style .. "/" .. arg_12_1, "", function(arg_14_0)
		arg_12_0.spList[arg_12_1] = arg_14_0

		arg_12_0.checkAndSetSprite(arg_12_1, arg_12_2))

def var_0_0.setSelectTarget(arg_15_0, arg_15_1):
	arg_15_0.changeShowCharacter("p_" .. arg_15_0.shipIdList[arg_15_1], arg_15_0.print, arg_15_0.selectTarget)

	if arg_15_0.rtName:
		arg_15_0.changeShowCharacter("n_" .. arg_15_0.shipIdList[arg_15_1], arg_15_0.rtName, arg_15_0.selectTarget)

	arg_15_0.selectTarget = arg_15_1
	arg_15_0.selectedShipNumber = arg_15_0.shipIdList[arg_15_1]

def var_0_0.willExit(arg_16_0):
	return

return var_0_0
