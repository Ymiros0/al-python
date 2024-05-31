local var_0_0 = class("TagTipHelper")

def var_0_0.FuDaiTagTip(arg_1_0):
	triggerToggle(arg_1_0, False)

	local var_1_0 = {}
	local var_1_1 = pg.pay_data_display

	for iter_1_0, iter_1_1 in ipairs(var_1_1.all):
		if var_1_1[iter_1_1].type == 1 and pg.TimeMgr.GetInstance().inTime(var_1_1[iter_1_1].time) and type(var_1_1[iter_1_1].time) == "table":
			table.insert(var_1_0, var_1_1[iter_1_1])

	if #var_1_0 > 0:
		local function var_1_2(arg_2_0)
			table.sort(var_1_0, function(arg_3_0, arg_3_1)
				return pg.TimeMgr.GetInstance().parseTimeFromConfig(arg_3_0.time[1]) > pg.TimeMgr.GetInstance().parseTimeFromConfig(arg_3_1.time[1]))

			local var_2_0 = var_1_0[1]
			local var_2_1 = arg_2_0[var_2_0.id] != None
			local var_2_2 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_2_0.time[1])
			local var_2_3 = PlayerPrefs.GetInt("Ever_Enter_Mall_", 0)

			if not var_2_1 and var_2_3 < var_2_2:
				var_0_0.FudaiTime = var_2_2

				triggerToggle(arg_1_0, True)

		local var_1_3 = getProxy(ShopsProxy)
		local var_1_4 = var_1_3.getChargedList()

		if not var_1_4:
			pg.m02.sendNotification(GAME.GET_CHARGE_LIST, {
				def callback:()
					var_1_4 = var_1_3.getChargedList()

					var_1_2(var_1_4)
			})
		else
			var_1_2(var_1_4)

def var_0_0.SetFuDaiTagMark():
	if var_0_0.FudaiTime:
		PlayerPrefs.SetInt("Ever_Enter_Mall_", var_0_0.FudaiTime)
		PlayerPrefs.Save()

		var_0_0.FudaiTime = None

def var_0_0.SkinTagTip(arg_6_0):
	triggerToggle(arg_6_0, False)

	local var_6_0 = getProxy(ShipSkinProxy).GetAllSkins()
	local var_6_1 = {}

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		if iter_6_1.type == Goods.TYPE_SKIN and type(iter_6_1.getConfig("time")) == "table" and iter_6_1.genre != ShopArgs.SkinShopTimeLimit:
			table.insert(var_6_1, pg.TimeMgr.GetInstance().parseTimeFromConfig(iter_6_1.getConfig("time")[1]))

	if #var_6_1 > 0:
		table.sort(var_6_1, function(arg_7_0, arg_7_1)
			return arg_7_1 < arg_7_0)

		local var_6_2 = var_6_1[1]
		local var_6_3 = var_6_2 > PlayerPrefs.GetInt("Ever_Enter_Skin_Shop_", 0)

		if var_6_3:
			var_0_0.SkinTime = var_6_2

		triggerToggle(arg_6_0, var_6_3)

def var_0_0.SetSkinTagMark():
	if var_0_0.SkinTime:
		PlayerPrefs.SetInt("Ever_Enter_Skin_Shop_", var_0_0.SkinTime)
		PlayerPrefs.Save()

		var_0_0.SkinTime = None

def var_0_0.MonthCardTagTip(arg_9_0):
	local var_9_0 = MonthCardOutDateTipPanel.GetShowMonthCardTag()

	triggerToggle(arg_9_0, var_9_0)

def var_0_0.FreeGiftTag(arg_10_0):
	local var_10_0 = getProxy(ShopsProxy)

	if not var_10_0.getChargedList():
		pg.m02.sendNotification(GAME.GET_CHARGE_LIST, {
			def callback:()
				if _.all(arg_10_0, function(arg_12_0)
					return not IsNil(arg_12_0)):
					for iter_11_0, iter_11_1 in ipairs(arg_10_0):
						setActive(iter_11_1, var_10_0.checkHasFreeNormal())
		})
	else
		for iter_10_0, iter_10_1 in ipairs(arg_10_0):
			setActive(iter_10_1, var_10_0.checkHasFreeNormal())

def var_0_0.FreeBuildTicketTip(arg_13_0, arg_13_1):
	local var_13_0 = getProxy(ActivityProxy).IsShowFreeBuildMark(False)

	if var_13_0:
		setActive(arg_13_0, True)
		LoadImageSpriteAtlasAsync(Drop.New({
			type = DROP_TYPE_VITEM,
			id = var_13_0.getConfig("config_client")[1]
		}).getIcon(), "", arg_13_0.Find("Image"))

		local var_13_1 = tostring(var_13_0.data1)

		if var_13_0.data1 < 10:
			var_13_1 = var_13_1 .. " "

		setText(arg_13_0.Find("Text"), i18n("build_ticket_expire_warning", var_13_1))

		var_0_0.BuildMark = True
	else
		setActive(arg_13_0, False)

def var_0_0.TecShipGiftTip(arg_14_0):
	local var_14_0 = {
		2001,
		2002,
		2003,
		2004,
		2005,
		2006,
		2007,
		2008
	}
	local var_14_1 = 30 <= getProxy(PlayerProxy).getData().level
	local var_14_2 = PlayerPrefs.GetInt("Tec_Ship_Gift_Enter_Tag", 0) > 0
	local var_14_3 = False

	for iter_14_0, iter_14_1 in ipairs(pg.pay_data_display.all):
		if table.contains(var_14_0, iter_14_1):
			var_14_3 = True

			break

	if var_14_3 and var_14_1 and not var_14_2:
		triggerToggle(arg_14_0, True)
	else
		triggerToggle(arg_14_0, False)

def var_0_0.SetFreeBuildMark():
	if var_0_0.BuildMark:
		local var_15_0 = getProxy(ActivityProxy).IsShowFreeBuildMark(False)

		if var_15_0:
			PlayerPrefs.SetString("Free_Build_Ticket_" .. var_15_0.id, pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d"))
			PlayerPrefs.Save()

		var_0_0.BuildMark = None

return var_0_0
