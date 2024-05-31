local var_0_0 = class("BuildShipRegularExchangeLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "BuildShipRegularExchangeUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	arg_2_0.cfg = pg.ship_data_create_exchange[REGULAR_BUILD_POOL_EXCHANGE_ID]
	arg_2_0.ids = arg_2_0.cfg.exchange_ship_id
	arg_2_0.iconSprites = {}

	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.ids):
		table.insert(var_2_0, function(arg_3_0)
			GetSpriteFromAtlasAsync("RegularExchangeIcon", tostring(iter_2_1), function(arg_4_0)
				arg_2_0.iconSprites[iter_2_1] = arg_4_0

				arg_3_0()))

	seriesAsync(var_2_0, arg_2_1)

def var_0_0.setCount(arg_5_0, arg_5_1):
	arg_5_0.count = arg_5_1

	setText(arg_5_0.textCount, arg_5_0.count .. "/" .. arg_5_0.cfg.exchange_request)
	setGray(arg_5_0.btnConfirm, arg_5_0.count < arg_5_0.cfg.exchange_request)

def var_0_0.init(arg_6_0):
	arg_6_0.btnBack = arg_6_0._tf.Find("top/bg/btn_back")

	onButton(arg_6_0, arg_6_0.btnBack, function()
		arg_6_0.closeView(), SFX_CANCEL)

	local var_6_0 = arg_6_0._tf.Find("select/container")

	arg_6_0.iconList = UIItemList.New(var_6_0, var_6_0.Find("tpl"))

	arg_6_0.iconList.make(function(arg_8_0, arg_8_1, arg_8_2)
		arg_8_1 = arg_8_1 + 1

		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = Ship.New({
				configId = arg_6_0.ids[arg_8_1]
			})

			setImageSprite(arg_8_2.Find("Image"), arg_6_0.iconSprites[var_8_0.configId], True)
			setActive(arg_8_2.Find("noget"), not getProxy(CollectionProxy).getShipGroup(var_8_0.getGroupId()))
			onToggle(arg_6_0, arg_8_2, function(arg_9_0)
				if arg_9_0:
					arg_6_0.setSelectedShip(var_8_0), SFX_PANEL)
			triggerToggle(arg_8_2, arg_8_1 == 1))
	onButton(arg_6_0, arg_6_0._tf.Find("select/operation/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("Normalbuild_URexchange_help")
		}), SFX_PANEL)
	setText(arg_6_0._tf.Find("select/operation/count/Text"), i18n("Normalbuild_URexchange_text2") .. ".")

	arg_6_0.textCount = arg_6_0._tf.Find("select/operation/count/num")
	arg_6_0.btnConfirm = arg_6_0._tf.Find("select/operation/confirm")

	onButton(arg_6_0, arg_6_0.btnConfirm, function()
		if arg_6_0.count < arg_6_0.cfg.exchange_request:
			pg.TipsMgr.GetInstance().ShowTips(i18n("Normalbuild_URexchange_warning1"))
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("Normalbuild_URexchange_confirm", arg_6_0.shipVO.getName()),
				def onYes:()
					arg_6_0.emit(BuildShipRegularExchangeMediator.EXCHAGNE_SHIP, arg_6_0.shipVO.configId)
					arg_6_0.closeView()
			}), SFX_CONFIRM)

	arg_6_0.rtName = arg_6_0._tf.Find("select/name_bg")
	arg_6_0.rtPaint = arg_6_0._tf.Find("main/paint")

def var_0_0.setSelectedShip(arg_13_0, arg_13_1):
	if arg_13_0.shipVO:
		retPaintingPrefab(arg_13_0.rtPaint, arg_13_0.shipVO.getPainting())

	arg_13_0.shipVO = arg_13_1

	local var_13_0 = ShipType.Type2BattlePrint(arg_13_1.getShipType())

	eachChild(arg_13_0.rtName.Find("shiptype"), function(arg_14_0)
		setActive(arg_14_0, arg_14_0.name == var_13_0))
	setText(arg_13_0.rtName.Find("name"), arg_13_1.getName())
	setText(arg_13_0.rtName.Find("english"), string.upper(arg_13_1.getConfig("english_name")))
	setPaintingPrefabAsync(arg_13_0.rtPaint, arg_13_1.getPainting(), "huode")

def var_0_0.didEnter(arg_15_0):
	arg_15_0.iconList.align(#arg_15_0.ids)

def var_0_0.willExit(arg_16_0):
	arg_16_0.iconSprites = None

	if arg_16_0.shipVO:
		retPaintingPrefab(arg_16_0.rtPaint, arg_16_0.shipVO.getPainting())

return var_0_0
