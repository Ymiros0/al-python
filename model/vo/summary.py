local var_0_0 = class("Summary", import(".BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	local var_1_0 = pg.TimeMgr.GetInstance()

	arg_1_0.name = getProxy(PlayerProxy).getData().name
	arg_1_0.registerTime = var_1_0.STimeDescC(arg_1_1.register_date, "%Y.%m.%d")

	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY).getStartTime()

	arg_1_0.days = math.max(math.ceil((var_1_1 - arg_1_1.register_date) / 86400), 0) + 1

	local var_1_2 = getProxy(UserProxy).getRawData()
	local var_1_3 = getProxy(ServerProxy).getRawData()[var_1_2 and var_1_2.server or 0]

	arg_1_0.serverName = var_1_3 and var_1_3.name or ""

	local var_1_4 = math.max(arg_1_1.chapter_id, 101)
	local var_1_5 = pg.chapter_template[var_1_4]

	if PLATFORM_CODE == PLATFORM_US and var_1_5.model == ChapterConst.TypeMainSub:
		arg_1_0.chapterName = pg.chapter_template[var_1_4 - 1].chapter_name .. " " .. var_1_5.name
	else
		arg_1_0.chapterName = var_1_5.chapter_name .. " " .. var_1_5.name

	arg_1_0.guildName = arg_1_1.guild_name
	arg_1_0.proposeCount = arg_1_1.marry_number
	arg_1_0.medalCount = arg_1_1.medal_number
	arg_1_0.furnitureCount = arg_1_1.furniture_number
	arg_1_0.furnitureWorth = arg_1_1.furniture_worth
	arg_1_0.flagShipId = arg_1_1.character_id
	arg_1_0.firstLadyId = arg_1_1.first_lady_id
	arg_1_0.isProPose = arg_1_0.proposeCount > 0
	arg_1_0.firstProposeName = ""

	if arg_1_0.firstLadyId > 0:
		arg_1_0.firstProposeName = Ship.New({
			configId = arg_1_0.firstLadyId
		}).getConfig("name")

	if arg_1_1.first_lady_name != "":
		arg_1_0.firstProposeName = arg_1_1.first_lady_name

	arg_1_0.proposeTime = math.ceil((var_1_1 - arg_1_1.first_lady_time) / 86400) + 1
	arg_1_0.firstLadyTime = var_1_0.STimeDescC(arg_1_1.first_lady_time, "%Y-%m-%d %H.%M")
	arg_1_0.unMarryShipId = 100001

	local var_1_6 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

	arg_1_0.furnitures = {}

	for iter_1_0, iter_1_1 in pairs(getProxy(DormProxy).getRawData().furnitures):
		arg_1_0.furnitures[iter_1_1.id] = iter_1_1

	arg_1_0.medalList = underscore.filter(var_1_6.getConfig("config_data"), function(arg_2_0)
		return tobool(arg_1_0.furnitures[arg_2_0]))

	local var_1_7 = getProxy(AttireProxy)

	arg_1_0.iconFrameList = underscore.filter(var_1_6.getConfig("config_client")[1], function(arg_3_0)
		return var_1_7.getAttireFrame(AttireConst.TYPE_ICON_FRAME, arg_3_0[1]).isOwned())
	arg_1_0.worldProgressTask = arg_1_1.world_max_task
	arg_1_0.collectionNum = string.format("%0.1f", arg_1_1.collect_num / var_1_6.getConfig("config_client")[2] * 100)
	arg_1_0.powerRaw = math.floor(arg_1_1.combat^0.667)
	arg_1_0.totalShipNum = arg_1_1.ship_num_total
	arg_1_0.topShipNum = arg_1_1.ship_num_120
	arg_1_0.bestShipNum = arg_1_1.ship_num_125
	arg_1_0.maxIntimacyNum = arg_1_1.love200_num
	arg_1_0.skinNum = arg_1_1.skin_num
	arg_1_0.skinShipNum = arg_1_1.skin_ship_num
	arg_1_0.skinId = 0

	local var_1_8 = {}

	for iter_1_2, iter_1_3 in ipairs(getProxy(ShipSkinProxy).GetShopShowingSkins()):
		if iter_1_3.buyCount > 0:
			var_1_8[iter_1_3.getSkinId()] = True

	local var_1_9 = getProxy(BayProxy)

	for iter_1_4, iter_1_5 in ipairs(getProxy(PlayerProxy).getRawData().characters):
		local var_1_10 = var_1_9.getShipById(iter_1_5)

		if var_1_10 and var_1_8[var_1_10.skinId]:
			arg_1_0.skinId = var_1_10.skinId

			break

	if arg_1_0.skinId == 0:
		local var_1_11 = underscore.keys(var_1_8)

		if #var_1_11 > 0:
			arg_1_0.skinId = var_1_11[math.max(1, math.ceil(math.random() * #var_1_11))]

def var_0_0.hasGuild(arg_4_0):
	return arg_4_0.guildName and arg_4_0.guildName != ""

def var_0_0.hasMedal(arg_5_0):
	return arg_5_0.medalCount > 0

return var_0_0
