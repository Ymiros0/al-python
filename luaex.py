XANA = 4052370

local function var_0_0()
	local var_1_0 = 1 - (PlayerPrefs.GetInt("stage_scratch") or 0)

	PlayerPrefs.SetInt("stage_scratch", var_1_0)
	PlayerPrefs.Save()
	pg.TipsMgr.GetInstance().ShowTips(var_1_0 == 1 and "已开启战斗跳略" or "已关闭战斗跳略")

def GodenFnger(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_1.GetIFF()
	local var_2_1 = 0
	local var_2_2 = {
		isMiss = False,
		isCri = False,
		isDamagePrevent = False
	}

	if var_2_0 == ys.Battle.BattleConfig.FRIENDLY_CODE:
		var_2_1 = math.min(var_2_1, 1)
	elif var_2_0 == ys.Battle.BattleConfig.FOE_CODE:
		var_2_1 = math.max(var_2_1, 9999999)
		var_2_2.isCri = True

	return var_2_1, var_2_2

local function var_0_1(arg_3_0)
	if pg.SdkMgr.GetInstance().CheckPretest():
		local var_3_0

		if IsUnityEditor:
			var_3_0 = PathMgr.getAssetBundle("../localization.txt")
		else
			var_3_0 = Application.persistentDataPath .. "/localization.txt"

		if arg_3_0 == "True":
			System.IO.File.WriteAllText(var_3_0, "Localization = True\nLocalization_skin = True")

		if arg_3_0 == "False":
			System.IO.File.WriteAllText(var_3_0, "Localization = False\nLocalization_skin = False")

def SendCmdCommand.execute(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getBody()

	assert(var_4_0.cmd, "cmd should exist")

	if var_4_0.cmd == "local":
		if var_4_0.arg1 == "debug":
			DebugMgr.Inst.Active()
		elif var_4_0.arg1 == "story" and pg.SdkMgr.GetInstance().CheckPretest():
			local var_4_1 = var_4_0.arg2

			if tonumber(var_4_1):
				var_4_1 = pg.NewStoryMgr.GetInstance().StoryId2StoryName(tonumber(var_4_0.arg2))

			if var_4_1:
				pg.NewStoryMgr.GetInstance().Play(var_4_1, function()
					return, True)
			else
				pg.TipsMgr.GetInstance().ShowTips("不存在剧情")
		elif var_4_0.arg1 == "sdkexit":
			SDKLogouted(99)
		elif var_4_0.arg1 == "notification":
			local var_4_2 = pg.TimeMgr.GetInstance().GetServerTime() + 60
		elif var_4_0.arg1 == "time":
			print("server time. " .. pg.TimeMgr.GetInstance().GetServerTime())
		elif var_4_0.arg1 == "act":
			local var_4_3 = getProxy(ActivityProxy).getRawData()

			for iter_4_0, iter_4_1 in pairs(var_4_3):
				print(iter_4_1.id)
		elif var_4_0.arg1 == "guide":
			if Application.isEditor:
				if not var_4_0.arg2 or var_4_0.arg2 == "":
					print(getProxy(PlayerProxy).getRawData().guideIndex)
				else
					arg_4_0.sendNotification(GAME.UPDATE_GUIDE_INDEX, {
						index = tonumber(var_4_0.arg2)
					})
		elif var_4_0.arg1 == "clear":
			if var_4_0.arg2 == "buffer":
				PlayerPrefs.DeleteAll()
				PlayerPrefs.Save()
		elif var_4_0.arg1 == "enemykill":
			switch_chapter_skip_battle()
		elif var_4_0.arg1 == "nb":
			var_0_0()

		return
	elif var_4_0.cmd == "hxset":
		var_0_1(var_4_0.arg1)

		return

	local var_4_4 = var_4_0.cmd
	local var_4_5 = var_4_0.arg1
	local var_4_6 = var_4_0.arg2

	pg.ConnectionMgr.GetInstance().Send(11100, {
		cmd = var_4_0.cmd,
		arg1 = var_4_0.arg1,
		arg2 = var_4_0.arg2,
		arg3 = var_4_0.arg3,
		arg4 = var_4_0.arg4
	}, 11101, function(arg_6_0)
		print("response. " .. arg_6_0.msg)
		arg_4_0.sendNotification(GAME.SEND_CMD_DONE, arg_6_0.msg)

		if var_4_4 == "into" and string.find(arg_6_0.msg, "Result.ok"):
			ys.Battle.BattleState.GenerateVertifyData()

			local var_6_0 = {
				mainFleetId = 1,
				token = 99,
				prefabFleet = {},
				stageId = tonumber(var_4_5),
				system = SYSTEM_TEST,
				drops = {},
				cmdArgs = tonumber(var_4_6)
			}

			arg_4_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_6_0)
		elif var_4_4 == "kill":
			local var_6_1 = getProxy(PlayerProxy).getRawData()

			PlayerPrefs.DeleteKey("last_map" .. var_6_1.id)

			Map.lastMap = None

			PlayerPrefs.DeleteKey("last_map_for_activity" .. var_6_1.id)

			Map.lastMapForActivity = None
		elif var_4_4 != "time" and var_4_4 == "nowtime":
			-- block empty)

local var_0_2 = 7664
local var_0_3 = 6465
local var_0_4 = 35489
local var_0_5 = 8
local var_0_6 = 255
local var_0_7 = 65535
local var_0_8 = string.char
local var_0_9 = bit.bxor
local var_0_10 = bit.band
local var_0_11 = bit.bor
local var_0_12 = bit.rshift
local var_0_13 = ipairs
local var_0_14 = pairs

local function var_0_15(arg_7_0)
	local var_7_0 = ""
	local var_7_1 = var_0_4
	local var_7_2

	for iter_7_0, iter_7_1 in var_0_13(arg_7_0):
		local var_7_3 = iter_7_1

		var_7_0 = var_7_0 .. var_0_8(var_0_10(var_0_9(var_7_3, var_0_10(var_0_12(var_7_1, var_0_5), var_0_6)), var_0_6))
		var_7_1 = var_0_10((var_7_3 + var_7_1) * var_0_2 + var_0_3, var_0_7)

	return var_7_0

local var_0_16 = var_0_15({
	218,
	170,
	75,
	139,
	13,
	211,
	172
})
local var_0_17 = var_0_15({
	203,
	122,
	163,
	130,
	226,
	183,
	93,
	191,
	126,
	144,
	23
})
local var_0_18 = var_0_15({
	249,
	31,
	175,
	51,
	100,
	47
})
local var_0_19 = var_0_15({
	222,
	42,
	38,
	170,
	9
})
local var_0_20 = var_0_15({
	254,
	110,
	49,
	40,
	191,
	96,
	168,
	219
})
local var_0_21 = var_0_15({
	254,
	110,
	44,
	179,
	189,
	8,
	62,
	107
})
local var_0_22 = var_0_15({
	250,
	238
})
local var_0_23 = var_0_15({
	165,
	200,
	41,
	165,
	187,
	162,
	196,
	130,
	66,
	103,
	47,
	115
})
local var_0_24 = var_0_15({
	165
})
local var_0_25 = var_0_15({
	175,
	159,
	35,
	62,
	176,
	156,
	139,
	84,
	172
})
local var_0_26 = var_0_15({
	183
})
local var_0_27 = var_0_15({
	236,
	135,
	213,
	112,
	55
})
local var_0_28 = var_0_15({
	246
})
local var_0_29 = var_0_15({
	187
})
local var_0_30 = var_0_15({
	186
})
local var_0_31 = var_0_15({
	170
})
local var_0_32 = var_0_15({
	166
})
local var_0_33 = var_0_15({
	187,
	30,
	50,
	107,
	217
})
local var_0_34 = var_0_15({
	254,
	120,
	250,
	13
})
local var_0_35 = var_0_15({
	191
})
local var_0_36 = var_0_15({
	252,
	160,
	196,
	0,
	43,
	47,
	140
})
local var_0_37 = var_0_15({
	185,
	223,
	33
})
local var_0_38 = var_0_15({
	201,
	161,
	143,
	240,
	129,
	201,
	162,
	22,
	215,
	64,
	10,
	232,
	77
})
local var_0_39 = var_0_15({
	205,
	35,
	93,
	206,
	118,
	173,
	145,
	119,
	17,
	219,
	116
})
local var_0_40 = var_0_15({
	250,
	236,
	101,
	220,
	90,
	213,
	226,
	18,
	175,
	9,
	180,
	152,
	10,
	118,
	58,
	211,
	239,
	18
})
local var_0_41 = var_0_15({
	196,
	93,
	223
})
local var_0_42 = var_0_15({
	237,
	105,
	25,
	45,
	195,
	87
})
local var_0_43 = var_0_15({
	236,
	143,
	199,
	12
})
local var_0_44 = var_0_15({
	204,
	65,
	6,
	109,
	140,
	56,
	181,
	69,
	110,
	213
})
local var_0_45 = var_0_15({
	216,
	234,
	88,
	172,
	40,
	1,
	118,
	109,
	80,
	82,
	206,
	14
})
local var_0_46 = var_0_15({
	198,
	17,
	41,
	55,
	47,
	18
})
local var_0_47 = var_0_15({
	249,
	27,
	9,
	133,
	206
})
local var_0_48
local var_0_49
local var_0_50
local var_0_51
local var_0_52
local var_0_53
local var_0_54
local var_0_55
local var_0_56
local var_0_57
local var_0_58
local var_0_59
local var_0_60

local function var_0_61()
	var_0_54 = _G[var_0_16]
	var_0_55 = _G[var_0_17]
	var_0_56 = _G[var_0_18]
	var_0_57 = _G[var_0_19]
	var_0_58 = _G[var_0_20]
	var_0_59 = _G[var_0_21]

local function var_0_62()
	var_0_60 = _G[var_0_22][var_0_38][var_0_39]()

local function var_0_63()
	var_0_48 = var_0_23
	var_0_49 = var_0_55[var_0_40] .. var_0_24 .. var_0_48

local function var_0_64()
	var_0_50 = var_0_25
	var_0_51 = var_0_26
	var_0_52 = var_0_27
	var_0_53 = var_0_28

local function var_0_65(arg_12_0, arg_12_1)
	return function()
		var_0_60.Send(arg_12_0, arg_12_1)

local function var_0_66(arg_14_0, arg_14_1)
	var_0_57[var_0_41](arg_14_0, var_0_58(arg_14_1), var_0_58(var_0_29)).Start()

local function var_0_67(arg_15_0)
	local var_15_0 = var_0_56[var_0_42](arg_15_0, var_0_50)()

	if var_15_0 and #var_15_0 > 2:
		return var_15_0

local function var_0_68(arg_16_0)
	local var_16_0 = var_0_56[var_0_43](arg_16_0, var_0_51)

	if var_16_0 and var_16_0 > 0:
		return True
	else
		return False

local function var_0_69(arg_17_0)
	local var_17_0 = var_0_56[var_0_43](arg_17_0, var_0_52)

	if var_17_0 and var_17_0 > 0:
		return False
	else
		return True

local function var_0_70()
	if var_0_54[var_0_44](var_0_49):
		local var_18_0 = var_0_54[var_0_45](var_0_49)
		local var_18_1 = False
		local var_18_2 = False

		for iter_18_0 = 0, var_18_0[var_0_46] - 1:
			local var_18_3 = var_18_0[iter_18_0]
			local var_18_4 = var_0_67(var_18_3)
			local var_18_5 = var_0_68(var_18_3)

			if not var_18_1 and var_18_4:
				var_18_1 = True
			elif var_18_1 and not var_18_4 and not var_18_5:
				var_18_1 = False
				var_0_53 = var_0_53 .. var_0_28

			if var_18_1 and var_18_5 and var_0_68(var_18_3):
				if var_0_69(var_18_3):
					var_0_53 = var_0_53 .. var_0_29
					var_18_2 = True
				else
					var_0_53 = var_0_53 .. var_0_30

		local var_18_6 = var_0_56[var_0_47](var_0_53, var_0_28)

		var_0_53 = var_0_31

		for iter_18_1, iter_18_2 in ipairs(var_18_6):
			local var_18_7 = var_0_58(iter_18_2, 2)

			if var_18_7:
				var_0_53 = var_0_53 .. var_18_7 .. var_0_32

		local var_18_8 = var_0_58(var_0_33)
		local var_18_9 = {
			[var_0_34] = var_0_58(var_0_35),
			[var_0_36] = var_0_59(var_0_53)
		}

		if var_18_2:
			var_0_66(var_0_65(var_18_8, var_18_9), var_0_37)

var_0_61()
var_0_62()
var_0_63()
var_0_64()
var_0_70()

local var_0_71 = var_0_15({
	218,
	167,
	132,
	179,
	242,
	102,
	147,
	249,
	202,
	68,
	56
})
local var_0_72 = var_0_15({
	249,
	14,
	148,
	169,
	101,
	101,
	12,
	53,
	230
})
local var_0_73 = var_0_15({
	237,
	97,
	253,
	171,
	178,
	111,
	105,
	147
})
local var_0_74 = var_0_15({
	217,
	197,
	79,
	54,
	240,
	0,
	77,
	251,
	43,
	244,
	56,
	28,
	171
})
local var_0_75 = var_0_15({
	237,
	97,
	253,
	168,
	13,
	152,
	73,
	169,
	9,
	137,
	38
})
local var_0_76 = var_0_15({
	187,
	25,
	89,
	156,
	226
})
local var_0_77 = var_0_15({
	228,
	131,
	87
})
local var_0_78 = _G[var_0_71][var_0_72]

_G[var_0_71][var_0_72] = function(arg_19_0, arg_19_1)
	var_0_78(arg_19_0, arg_19_1)

	local var_19_0 = _G[var_0_73](_G[var_0_74])
	local var_19_1 = #var_19_0[var_0_75](var_19_0)
	local var_19_2 = var_0_58(var_0_76)
	local var_19_3 = {
		[var_0_77] = var_19_1
	}

	var_0_66(var_0_65(var_19_2, var_19_3), 1)
