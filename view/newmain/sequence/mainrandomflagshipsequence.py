local var_0_0 = class("MainRandomFlagShipSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(SettingsProxy).GetRandomFlagShipList()

	if #var_1_0 > 0 and _.all(var_1_0, function(arg_2_0)
		return getProxy(BayProxy).RawGetShipById(arg_2_0) == None):
		pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_off_0"))
		getProxy(SettingsProxy).UpdateRandomFlagShipList({})
		arg_1_1()

		return

	local var_1_1, var_1_2 = arg_1_0.ShouldRandom()

	if var_1_1:
		local var_1_3 = arg_1_0.Random()

		if not var_1_3 or #var_1_3 == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_off_0"))
			arg_1_0.SynToCache({}, var_1_2)
		else
			arg_1_0.SynToCache(var_1_3, var_1_2)

	arg_1_1()

local function var_0_1(arg_3_0)
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_3_1 = GetZeroTime() - 18000
	local var_3_2 = var_3_1 - 39600
	local var_3_3 = var_3_2 - 46800

	if var_3_0 < var_3_2 and arg_3_0 < var_3_3:
		return True, var_3_3

	if var_3_2 <= var_3_0 and var_3_0 < var_3_1 and arg_3_0 < var_3_2:
		return True, var_3_2

	if var_3_1 <= var_3_0 and arg_3_0 < var_3_1:
		return True, var_3_1

	return False

def var_0_0.ShouldRandom(arg_4_0):
	if not getProxy(SettingsProxy).IsOpenRandomFlagShip():
		return False

	local var_4_0 = getProxy(SettingsProxy).GetPrevRandomFlagShipTime()

	return var_0_1(var_4_0)

local function var_0_2(arg_5_0, arg_5_1)
	if arg_5_1.isActivityNpc():
		return False

	if arg_5_0 == SettingsRandomFlagShipAndSkinPanel.SHIP_FREQUENTLYUSED:
		return arg_5_1.GetPreferenceTag() != 0
	elif arg_5_0 == SettingsRandomFlagShipAndSkinPanel.SHIP_LOCKED:
		return arg_5_1.GetLockState() != 0
	elif arg_5_0 == SettingsRandomFlagShipAndSkinPanel.COUSTOM:
		-- block empty

	return True

local function var_0_3(arg_6_0, arg_6_1)
	local function var_6_0(arg_7_0, arg_7_1, arg_7_2)
		if not arg_7_0[arg_7_2.groupId]:
			arg_7_0[arg_7_2.groupId] = {}

			table.insert(arg_7_1, arg_7_2.groupId)

		table.insert(arg_7_0[arg_7_2.groupId], arg_7_2.id)

	local var_6_1 = {}

	if arg_6_0 == SettingsRandomFlagShipAndSkinPanel.COUSTOM:
		for iter_6_0, iter_6_1 in ipairs(getProxy(PlayerProxy).getRawData().GetCustomRandomShipList()):
			local var_6_2 = getProxy(BayProxy).RawGetShipById(iter_6_1)

			if var_6_2:
				table.insert(var_6_1, var_6_2)
	else
		var_6_1 = getProxy(BayProxy).getRawData()

	local var_6_3 = {}
	local var_6_4 = {}
	local var_6_5 = {}
	local var_6_6 = {}

	for iter_6_2, iter_6_3 in pairs(var_6_1):
		if var_0_2(arg_6_0, iter_6_3):
			if arg_6_1[iter_6_3.groupId]:
				var_6_0(var_6_5, var_6_6, iter_6_3)
			else
				var_6_0(var_6_3, var_6_4, iter_6_3)

	return var_6_3, var_6_4, var_6_5, var_6_6

local function var_0_4(arg_8_0)
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in ipairs(arg_8_0):
		local var_8_1 = getProxy(BayProxy).RawGetShipById(iter_8_1)

		if var_8_1:
			var_8_0[var_8_1.groupId] = True

	return var_8_0

def var_0_0.Random(arg_9_0):
	local var_9_0 = getProxy(PlayerProxy).getRawData().GetRandomFlagShipMode()
	local var_9_1, var_9_2 = PlayerVitaeShipsPage.GetSlotMaxCnt()
	local var_9_3 = var_0_4(getProxy(SettingsProxy).GetRandomFlagShipList())
	local var_9_4, var_9_5, var_9_6, var_9_7 = var_0_3(var_9_0, var_9_3)

	return (arg_9_0.RandomShips(var_9_2, var_9_4, var_9_5, var_9_6, var_9_7))

def var_0_0.RandomShips(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5):
	local var_10_0 = {}

	for iter_10_0 = 1, arg_10_1:
		if #arg_10_3 == 0 and #arg_10_5 == 0:
			return var_10_0

		local var_10_1 = #arg_10_3 == 0
		local var_10_2 = var_10_1 and arg_10_5 or arg_10_3
		local var_10_3 = var_10_1 and arg_10_4 or arg_10_2
		local var_10_4 = var_10_2[math.random(1, #var_10_2)]
		local var_10_5 = var_10_3[var_10_4] or {}

		if #var_10_5 > 0:
			local var_10_6 = var_10_5[math.random(1, #var_10_5)]

			table.insert(var_10_0, var_10_6)
			table.removebyvalue(var_10_5, var_10_6)

		if #var_10_5 == 0:
			table.removebyvalue(var_10_2, var_10_4)

	return var_10_0

def var_0_0.SynToCache(arg_11_0, arg_11_1, arg_11_2):
	getProxy(SettingsProxy).UpdateRandomFlagShipList(arg_11_1)
	getProxy(SettingsProxy).SetPrevRandomFlagShipTime(arg_11_2)

return var_0_0
