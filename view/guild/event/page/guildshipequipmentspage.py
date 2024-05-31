local var_0_0 = class("GuildShipEquipmentsPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "GuildShipEquipmentsPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.shipNameTxt = arg_2_0.findTF("frame/ship_info/shipname").GetComponent(typeof(Text))
	arg_2_0.userNameTxt = arg_2_0.findTF("frame/ship_info/username").GetComponent(typeof(Text))
	arg_2_0.shipTypeIcon = arg_2_0.findTF("frame/ship_info/ship_type").GetComponent(typeof(Image))
	arg_2_0.shipStarList = UIItemList.New(arg_2_0.findTF("frame/ship_info/stars"), arg_2_0.findTF("frame/ship_info/stars/star_tpl"))
	arg_2_0.shipLvTxt = arg_2_0.findTF("frame/ship_info/lv/Text").GetComponent(typeof(Text))
	arg_2_0.equipmentList = UIItemList.New(arg_2_0.findTF("frame/equipemtns"), arg_2_0.findTF("frame/equipemtns/equipment_tpl"))
	arg_2_0.playerId = getProxy(PlayerProxy).getRawData().id
	arg_2_0.nextBtn = arg_2_0.findTF("frame/next")
	arg_2_0.prevBtn = arg_2_0.findTF("frame/prev")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.nextBtn, function()
		if arg_3_0.onNext:
			arg_3_0.onNext(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.prevBtn, function()
		if arg_3_0.onPrev:
			arg_3_0.onPrev(), SFX_PANEL)

def var_0_0.SetCallBack(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.onPrev = arg_7_1
	arg_7_0.onNext = arg_7_2

def var_0_0.Show(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	var_0_0.super.Show(arg_8_0)

	arg_8_0.OnHide = arg_8_3

	if arg_8_4:
		arg_8_4()

	arg_8_0.Flush(arg_8_1, arg_8_2)
	pg.UIMgr.GetInstance().BlurPanel(arg_8_0._tf)
	setActive(arg_8_0.nextBtn, arg_8_0.onNext != None)
	SetActive(arg_8_0.prevBtn, arg_8_0.onPrev != None)

def var_0_0.Flush(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.ship = arg_9_1
	arg_9_0.member = arg_9_2

	arg_9_0.UpdateShipInfo()
	arg_9_0.UpdateEquipments()

def var_0_0.Refresh(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.Flush(arg_10_1, arg_10_2)

def var_0_0.UpdateShipInfo(arg_11_0):
	local var_11_0 = arg_11_0.ship
	local var_11_1 = arg_11_0.member

	arg_11_0.shipNameTxt.text = var_11_0.getName()

	local var_11_2 = arg_11_0.playerId == var_11_1.id and "" or i18n("guild_ship_from") .. var_11_1.name

	arg_11_0.userNameTxt.text = var_11_2

	local var_11_3 = pg.ship_data_statistics[var_11_0.configId]

	arg_11_0.shipTypeIcon.sprite = GetSpriteFromAtlas("shiptype", shipType2print(var_11_3.type))

	local var_11_4 = var_11_0.getMaxStar()
	local var_11_5 = var_11_0.getStar()

	arg_11_0.shipStarList.make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate:
			setActive(arg_12_2.Find("star_tpl"), arg_12_1 <= var_11_5))
	arg_11_0.shipStarList.align(var_11_4)

	arg_11_0.shipLvTxt.text = var_11_0.level

def var_0_0.UpdateEquipments(arg_13_0):
	local var_13_0 = arg_13_0.ship.getActiveEquipments()

	arg_13_0.equipmentList.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate:
			local var_14_0 = var_13_0[arg_14_1 + 1]

			setActive(arg_14_2.Find("info"), var_14_0)
			setActive(arg_14_2.Find("empty"), not var_14_0)

			if var_14_0:
				updateEquipment(arg_14_2.Find("info"), var_14_0)
				setText(arg_14_2.Find("info/name_bg/Text"), shortenString(var_14_0.getConfig("name"), 5)))
	arg_13_0.equipmentList.align(5)

def var_0_0.Hide(arg_15_0):
	var_0_0.super.Hide(arg_15_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_15_0._tf, arg_15_0._parentTf)

	if arg_15_0.OnHide:
		arg_15_0.OnHide()

		arg_15_0.OnHide = None

def var_0_0.OnDestroy(arg_16_0):
	arg_16_0.Hide()

return var_0_0
