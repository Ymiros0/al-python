local var_0_0 = class("ChangeShipSkinPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ChangeShipSkinPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.confirmBtn = arg_2_0.findTF("window/exchange_btn")
	arg_2_0.closeBtn = arg_2_0.findTF("window/top/btnBack")
	arg_2_0.shipCardTpl = arg_2_0._tf.GetComponent("ItemList").prefabItem[0]
	arg_2_0.shipContent = arg_2_0.findTF("window/sliders/scroll_rect/content")
	arg_2_0.flagShipToggle = arg_2_0.findTF("window/flag_ship")

	setText(arg_2_0.findTF("window/top/title_list/infomation/title"), i18n("chang_ship_skin_window_title"))
	setText(arg_2_0.findTF("window/please"), i18n("choose_ship_to_wear_this_skin"))
	setText(arg_2_0.findTF("window/exchange_btn/Image"), i18n("change"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0.OnConfirm(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.flagShipToggle, function(arg_7_0)
		arg_3_0.flagShipMark = arg_7_0, SFX_PANEL)

def var_0_0.OnConfirm(arg_8_0):
	if not arg_8_0.selectIds or #arg_8_0.selectIds <= 0:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("new_skin_no_choose"),
			def onYes:()
				arg_8_0.Hide()
		})

		return

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.selectIds):
		pg.m02.sendNotification(GAME.SET_SHIP_SKIN, {
			shipId = iter_8_1,
			skinId = arg_8_0.skin.id
		})

	local var_8_0 = arg_8_0.flagShipMark

	arg_8_0.SetFlagShip(var_8_0)

	if var_8_0:
		local var_8_1 = arg_8_0.selectIds[1]

		pg.m02.sendNotification(GAME.CHANGE_PLAYER_ICON, {
			skinPage = True,
			characterId = var_8_1
		})

	arg_8_0.Hide()

def var_0_0.Show(arg_10_0, arg_10_1):
	var_0_0.super.Show(arg_10_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_10_0._tf)

	arg_10_0.selectIds = {}
	arg_10_0.skin = arg_10_1
	arg_10_0.ships = arg_10_0.GetShips(arg_10_1)

	local var_10_0 = arg_10_0.GetSetFlagShip()

	triggerToggle(arg_10_0.flagShipToggle, var_10_0)
	arg_10_0.FlushShips()

def var_0_0.GetSetFlagShip(arg_11_0):
	return getProxy(SettingsProxy).GetSetFlagShipForSkinAtlas()

def var_0_0.SetFlagShip(arg_12_0, arg_12_1):
	getProxy(SettingsProxy).SetFlagShipForSkinAtlas(arg_12_1)

def var_0_0.Sort(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_1.skinId == arg_13_0.skin.id and 0 or 1
	local var_13_1 = arg_13_2.skinId == arg_13_0.skin.id and 0 or 1

	if var_13_0 == var_13_1:
		if arg_13_1.level == arg_13_2.level:
			local var_13_2 = arg_13_1.getStar()
			local var_13_3 = arg_13_2.getStar()

			if var_13_2 == var_13_3:
				local var_13_4 = arg_13_1.inFleet and 1 or 0
				local var_13_5 = arg_13_2.inFleet and 1 or 0

				if var_13_4 == var_13_5:
					return arg_13_1.createTime < arg_13_2.createTime
				else
					return var_13_5 < var_13_4
			else
				return var_13_3 < var_13_2
		else
			return arg_13_1.level > arg_13_2.level
	else
		return var_13_1 < var_13_0

def var_0_0.GetShips(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.IsTransSkin()
	local var_14_1 = arg_14_1.IsProposeSkin()
	local var_14_2 = getProxy(BayProxy)._findShipsByGroup(arg_14_0.skin.getConfig("ship_group"), var_14_0, var_14_1)

	table.sort(var_14_2, function(arg_15_0, arg_15_1)
		return arg_14_0.Sort(arg_15_0, arg_15_1))

	return var_14_2

def var_0_0.FlushShips(arg_16_0):
	local var_16_0 = arg_16_0.ships

	local function var_16_1(arg_17_0)
		for iter_17_0, iter_17_1 in pairs(arg_16_0.selectIds):
			if iter_17_1 == arg_17_0.shipVO.id:
				table.remove(arg_16_0.selectIds, iter_17_0)

				break

	removeAllChildren(arg_16_0.shipContent)

	for iter_16_0, iter_16_1 in ipairs(var_16_0):
		local var_16_2 = Object.Instantiate(arg_16_0.shipCardTpl, arg_16_0.shipContent)
		local var_16_3 = ShipDetailCard.New(var_16_2.gameObject)

		var_16_3.update(iter_16_1, arg_16_0.skin.id)

		local var_16_4 = iter_16_1.skinId == arg_16_0.skin.id

		setActive(var_16_3.maskStatusOb, var_16_4)
		setText(var_16_3.maskStatusOb.Find("Text"), "-  " .. i18n("index_CANTUSE") .. "  -")
		onToggle(arg_16_0, var_16_3.tr, function(arg_18_0)
			if iter_16_1.skinId == arg_16_0.skin.id:
				return

			var_16_3.updateSelected(arg_18_0)

			if arg_18_0:
				table.insert(arg_16_0.selectIds, var_16_3.shipVO.id)
			else
				var_16_1(var_16_3), SFX_PANEL)

def var_0_0.Hide(arg_19_0):
	var_0_0.super.Hide(arg_19_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_19_0._tf, arg_19_0._parentTf)

	arg_19_0.selectIds = {}

def var_0_0.OnDestroy(arg_20_0):
	if arg_20_0.isShowing():
		arg_20_0.Hide()

	arg_20_0.shipCards = None
	arg_20_0.selectIds = None

return var_0_0
