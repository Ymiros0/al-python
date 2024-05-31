pg = pg or {}
pg.RedDotMgr = singletonClass("RedDotMgr")

require("Mgr/RedDot/Include")

local var_0_0 = pg.RedDotMgr
local var_0_1 = True

local function var_0_2(...)
	if var_0_1:
		originalPrint(...)

var_0_0.TYPES = {
	COURTYARD = 1,
	MEMORY_REVIEW = 19,
	ACT_RETURN = 16,
	COMMANDER = 10,
	RYZA_TASK = 21,
	BLUEPRINT = 14,
	BUILD = 4,
	SERVER = 12,
	ISLAND = 22,
	ACT_NEWBIE = 17,
	EVENT = 15,
	ATTIRE = 6,
	FRIEND = 8,
	NEW_SERVER = 20,
	TASK = 2,
	MAIL = 3,
	GUILD = 5,
	SETTTING = 11,
	COMMISSION = 9,
	COLLECTION = 7,
	SCHOOL = 13
}

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0.conditions = {}
	arg_2_0.nodeList = {}

	arg_2_0.BindConditions()

	if arg_2_1:
		arg_2_1()

def var_0_0.BindConditions(arg_3_0):
	arg_3_0.BindCondition(var_0_0.TYPES.COURTYARD, function()
		return getProxy(DormProxy).IsShowRedDot())
	arg_3_0.BindCondition(var_0_0.TYPES.TASK, function()
		return getProxy(TaskProxy).getCanReceiveCount() > 0 or getProxy(AvatarFrameProxy).getCanReceiveCount() > 0)
	arg_3_0.BindCondition(var_0_0.TYPES.MAIL, function()
		return getProxy(MailProxy).GetUnreadCount())
	arg_3_0.BindCondition(var_0_0.TYPES.BUILD, function()
		return getProxy(BuildShipProxy).getFinishCount() > 0 or tobool(getProxy(ActivityProxy).IsShowFreeBuildMark(True)))
	arg_3_0.BindCondition(var_0_0.TYPES.GUILD, function()
		return getProxy(GuildProxy).ShouldShowTip())
	arg_3_0.BindCondition(var_0_0.TYPES.ATTIRE, function()
		return getProxy(AttireProxy).IsShowRedDot() or getProxy(SettingsProxy).ShouldEducateCharTip())
	arg_3_0.BindCondition(var_0_0.TYPES.COLLECTION, function()
		return getProxy(CollectionProxy).hasFinish() or getProxy(AppreciateProxy).isGalleryHaveNewRes() or getProxy(AppreciateProxy).isMusicHaveNewRes() or getProxy(AppreciateProxy).isMangaHaveNewRes())
	arg_3_0.BindCondition(var_0_0.TYPES.FRIEND, function()
		return getProxy(NotificationProxy).getRequestCount() > 0 or getProxy(FriendProxy).getNewMsgCount() > 0)
	arg_3_0.BindCondition(var_0_0.TYPES.COMMISSION, function()
		return getProxy(PlayerProxy).IsShowCommssionTip())
	arg_3_0.BindCondition(var_0_0.TYPES.COMMANDER, function()
		if getProxy(PlayerProxy).getRawData().level < 40:
			return False

		local var_13_0 = getProxy(CommanderProxy).IsFinishAllBox()

		if not LOCK_CATTERY:
			return var_13_0 or getProxy(CommanderProxy).AnyCatteryExistOP() or getProxy(CommanderProxy).AnyCatteryCanUse()
		else
			return var_13_0)
	arg_3_0.BindCondition(var_0_0.TYPES.SETTTING, function()
		return PlayerPrefs.GetFloat("firstIntoOtherPanel") == 0)
	arg_3_0.BindCondition(var_0_0.TYPES.SERVER, function()
		return #getProxy(ServerNoticeProxy).getServerNotices(False) > 0 and getProxy(ServerNoticeProxy).hasNewNotice())
	arg_3_0.BindCondition(var_0_0.TYPES.SCHOOL, function()
		return getProxy(NavalAcademyProxy).IsShowTip())
	arg_3_0.BindCondition(var_0_0.TYPES.BLUEPRINT, function()
		return getProxy(TechnologyProxy).IsShowTip())
	arg_3_0.BindCondition(var_0_0.TYPES.EVENT, function()
		return getProxy(EventProxy).hasFinishState() or LimitChallengeConst.IsShowRedPoint())
	arg_3_0.BindCondition(var_0_0.TYPES.ACT_RETURN, function()
		local var_19_0 = RefluxTaskView.isAnyTaskCanGetAward()
		local var_19_1 = RefluxPTView.isAnyPTCanGetAward()
		local var_19_2 = RefluxShopView.isShowRedPot()

		return var_19_0 or var_19_1 or var_19_2)
	arg_3_0.BindCondition(var_0_0.TYPES.ACT_NEWBIE, function()
		local var_20_0, var_20_1 = TrainingCampScene.isNormalActOn()
		local var_20_2, var_20_3 = TrainingCampScene.isTecActOn()

		return var_20_1 or var_20_3)
	arg_3_0.BindCondition(var_0_0.TYPES.MEMORY_REVIEW, function()
		local var_21_0 = getProxy(PlayerProxy).getRawData()

		if var_21_0:
			local var_21_1 = var_21_0.id

			do return _.any(pg.memory_group.all, function(arg_22_0)
				return PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. var_21_1 .. " " .. arg_22_0, 0) == 1) end
			return

		return False)
	arg_3_0.BindCondition(var_0_0.TYPES.NEW_SERVER, function()
		return NewServerCarnivalScene.isTip())
	arg_3_0.BindCondition(var_0_0.TYPES.RYZA_TASK, function()
		return getProxy(ActivityTaskProxy).getActTaskTip(ActivityConst.RYZA_TASK))
	arg_3_0.BindCondition(var_0_0.TYPES.ISLAND, function()
		local var_25_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

		return Activity.IsActivityReady(var_25_0))

def var_0_0.BindCondition(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.conditions[arg_26_1] = arg_26_2

def var_0_0.RegisterRedDotNodes(arg_27_0, arg_27_1):
	for iter_27_0, iter_27_1 in ipairs(arg_27_1):
		arg_27_0.RegisterRedDotNode(iter_27_1)

	arg_27_0._NotifyAll()

def var_0_0.RegisterRedDotNode(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_1.GetTypes()

	for iter_28_0, iter_28_1 in ipairs(var_28_0):
		if not arg_28_0.nodeList[iter_28_1]:
			arg_28_0.nodeList[iter_28_1] = {}

		table.insert(arg_28_0.nodeList[iter_28_1], arg_28_1)

	arg_28_1.Init()

def var_0_0.UnRegisterRedDotNodes(arg_29_0, arg_29_1):
	for iter_29_0, iter_29_1 in ipairs(arg_29_1):
		arg_29_0.UnRegisterRedDotNode(iter_29_1)

	var_0_0.cache = {}

def var_0_0.UnRegisterRedDotNode(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_1.GetTypes()

	for iter_30_0, iter_30_1 in ipairs(var_30_0):
		local var_30_1 = arg_30_0.nodeList[iter_30_1] or {}

		for iter_30_2, iter_30_3 in ipairs(var_30_1):
			if iter_30_3 == arg_30_1:
				iter_30_3.Remove()
				table.remove(var_30_1, iter_30_2)

local function var_0_3(arg_31_0, arg_31_1)
	for iter_31_0, iter_31_1 in ipairs(arg_31_1):
		local var_31_0

		if var_0_0.cache[iter_31_1] != None:
			var_31_0 = var_0_0.cache[iter_31_1]
		else
			var_31_0 = arg_31_0.conditions[iter_31_1]()
			var_0_0.cache[iter_31_1] = var_31_0

		if var_31_0:
			return var_31_0

	return False

def var_0_0.NotifyAll(arg_32_0, arg_32_1):
	var_0_0.cache = {}

	for iter_32_0, iter_32_1 in ipairs(arg_32_0.nodeList[arg_32_1] or {}):
		local var_32_0 = iter_32_1.GetTypes()
		local var_32_1 = var_0_3(arg_32_0, var_32_0)

		iter_32_1.SetData(var_32_1)

	var_0_0.cache = {}

def var_0_0._NotifyAll(arg_33_0):
	var_0_0.cache = {}

	local var_33_0 = {}

	local function var_33_1(arg_34_0, arg_34_1)
		local var_34_0 = arg_34_0.GetTypes()
		local var_34_1 = var_0_3(arg_33_0, var_34_0)

		arg_34_0.SetData(var_34_1)
		onNextTick(arg_34_1)

	for iter_33_0, iter_33_1 in pairs(arg_33_0.nodeList):
		for iter_33_2, iter_33_3 in ipairs(iter_33_1):
			table.insert(var_33_0, function(arg_35_0)
				var_33_1(iter_33_3, arg_35_0))

	seriesAsync(var_33_0, function()
		var_0_0.cache = {})

def var_0_0.DebugNodes(arg_37_0):
	for iter_37_0, iter_37_1 in pairs(arg_37_0.nodeList):
		var_0_2("type . ", iter_37_0)

		for iter_37_2, iter_37_3 in ipairs(iter_37_1):
			var_0_2(" ", iter_37_3.GetName())
