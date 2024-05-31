local var_0_0 = class("AssignedShipForGreetingScene", import(".BaseAssignedShipScene"))
local var_0_1 = {
	select_panel_7 = {
		Vector2(80, -110),
		Vector2(80, -330),
		Vector2(80, -550),
		Vector2(80, -770),
		Vector2(240, -160),
		Vector2(240, -380),
		Vector2(240, -600)
	}
}

def var_0_0.getUIName(arg_1_0):
	return "AssignedShipUI6"

def var_0_0.init(arg_2_0):
	local var_2_0 = arg_2_0._tf.Find("layer")

	arg_2_0.backBtn = var_2_0.Find("top/back")
	arg_2_0.confirmBtn = var_2_0.Find("confirm")
	arg_2_0.print = var_2_0.Find("print")
	arg_2_0.rtName = var_2_0.Find("name")
	arg_2_0.rtTitle = var_2_0.Find("top/title")
	arg_2_0.selectTarget = None
	arg_2_0.count = 1
	arg_2_0.spList = {}
	arg_2_0.afterAnima = {}

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n(arg_3_0.strTip, pg.ship_data_statistics[arg_3_0.selectedShipNumber].name),
			def onYes:()
				arg_3_0.emit(AssignedShipMediator.ON_USE_ITEM, arg_3_0.itemVO.id, arg_3_0.count, {
					arg_3_0.idList[arg_3_0.selectTarget]
				})
		}), SFX_PANEL)
	setActive(arg_3_0.rtTitle, arg_3_0.title)

	if arg_3_0.title:
		GetImageSpriteFromAtlasAsync("extra_page/" .. arg_3_0.style .. "/" .. arg_3_0.title, "", arg_3_0.rtTitle, True)

	local var_3_0 = #arg_3_0.shipIdList
	local var_3_1 = "select_panel_" .. var_3_0

	setActive(arg_3_0._tf.Find("layer/" .. var_3_1), True)

	arg_3_0.selectPanel = arg_3_0._tf.Find("layer/" .. var_3_1 .. "/layout")
	arg_3_0.itemList = UIItemList.New(arg_3_0.selectPanel, arg_3_0.selectPanel.Find("item"))

	arg_3_0.itemList.make(function(arg_7_0, arg_7_1, arg_7_2)
		arg_7_1 = arg_7_1 + 1

		if var_0_1[var_3_1]:
			setAnchoredPosition(arg_7_2, var_0_1[var_3_1][arg_7_1])

		local var_7_0 = arg_3_0.shipIdList[arg_7_1]

		if arg_7_0 == UIItemList.EventUpdate:
			GetImageSpriteFromAtlasAsync("extra_page/" .. arg_3_0.style .. "/i_" .. var_7_0, "", arg_7_2.Find("unselected/icon"))
			GetImageSpriteFromAtlasAsync("extra_page/" .. arg_3_0.style .. "/i_" .. var_7_0, "", arg_7_2.Find("selected/icon"))
			onToggle(arg_3_0, arg_7_2, function(arg_8_0)
				if arg_8_0 and arg_3_0.selectTarget != arg_7_1:
					LeanTween.cancel(arg_3_0.print)

					if arg_3_0.rtName:
						LeanTween.cancel(arg_3_0.rtName)

					arg_3_0.setSelectTarget(arg_7_1), SFX_PANEL))
	arg_3_0.itemList.align(#arg_3_0.idList)
	triggerToggle(arg_3_0.selectPanel.GetChild(0), True)

return var_0_0
