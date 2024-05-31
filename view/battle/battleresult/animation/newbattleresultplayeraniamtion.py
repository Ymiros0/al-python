local var_0_0 = class("NewBattleResultPlayerAniamtion")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	arg_1_0.playerLv = arg_1_1
	arg_1_0.playerExp = arg_1_2
	arg_1_0.playerExpBar = arg_1_3
	arg_1_0.newPlayer = arg_1_4
	arg_1_0.oldPlayer = arg_1_5

def var_0_0.SetUp(arg_2_0, arg_2_1):
	parallelAsync({
		function(arg_3_0)
			arg_2_0.LevelAnimation(arg_3_0),
		function(arg_4_0)
			arg_2_0.ExpAnimation(arg_4_0),
		function(arg_5_0)
			arg_2_0.ExpBarAnimation(arg_5_0)
	}, arg_2_1)

def var_0_0.LevelAnimation(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.oldPlayer.level
	local var_6_1 = arg_6_0.newPlayer.level

	if var_6_0 == var_6_1:
		arg_6_0.playerLv.text = "Lv." .. var_6_1

		arg_6_1()

		return

	LeanTween.value(arg_6_0.playerLv.gameObject, var_6_0, var_6_1, 1.5).setOnUpdate(System.Action_float(function(arg_7_0)
		arg_6_0.playerLv.text = "Lv." .. math.ceil(arg_7_0))).setOnComplete(System.Action(arg_6_1))

def var_0_0.ExpAnimation(arg_8_0, arg_8_1):
	local var_8_0 = NewBattleResultUtil.GetPlayerExpOffset(arg_8_0.oldPlayer, arg_8_0.newPlayer)

	LeanTween.value(arg_8_0.playerExp.gameObject, 0, var_8_0, 1.5).setOnUpdate(System.Action_float(function(arg_9_0)
		arg_8_0.playerExp.text = "+" .. math.ceil(arg_9_0))).setOnComplete(System.Action(arg_8_1))

local function var_0_1(arg_10_0, arg_10_1)
	local var_10_0 = arg_10_0.oldPlayer.exp
	local var_10_1 = arg_10_0.newPlayer.exp
	local var_10_2 = getConfigFromLevel1(pg.user_level, arg_10_0.newPlayer.level).exp_interval

	LeanTween.value(arg_10_0.playerExpBar.gameObject, var_10_0, var_10_1, 1.5).setOnUpdate(System.Action_float(function(arg_11_0)
		arg_10_0.playerExpBar.fillAmount = arg_11_0 / var_10_2)).setOnComplete(System.Action(arg_10_1))

local function var_0_2(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_0.oldPlayer.exp
	local var_12_1 = getConfigFromLevel1(pg.user_level, arg_12_0.oldPlayer.level).exp_interval

	LeanTween.value(arg_12_0.playerExpBar.gameObject, var_12_0 / var_12_1, 1, 1).setOnUpdate(System.Action_float(function(arg_13_0)
		arg_12_0.playerExpBar.fillAmount = arg_13_0)).setOnComplete(System.Action(arg_12_1))

local function var_0_3(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0.newPlayer.exp
	local var_14_1 = getConfigFromLevel1(pg.user_level, arg_14_0.newPlayer.level).exp_interval

	LeanTween.value(arg_14_0.playerExpBar.gameObject, 0, var_14_0 / var_14_1, 1).setOnUpdate(System.Action_float(function(arg_15_0)
		arg_14_0.playerExpBar.fillAmount = arg_15_0)).setOnComplete(System.Action(arg_14_1))

local function var_0_4(arg_16_0, arg_16_1)
	local var_16_0 = arg_16_0.oldPlayer.level
	local var_16_1 = arg_16_0.newPlayer.level - (var_16_0 + 1)

	LeanTween.value(arg_16_0.playerExpBar.gameObject, 0, 1, 1).setOnUpdate(System.Action_float(function(arg_17_0)
		arg_16_0.playerExpBar.fillAmount = arg_17_0)).setRepeat(var_16_1).setOnComplete(System.Action(arg_16_1))

local function var_0_5(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_0.oldPlayer.level
	local var_18_1 = arg_18_0.newPlayer.level
	local var_18_2 = {}

	table.insert(var_18_2, function(arg_19_0)
		var_0_2(arg_18_0, arg_19_0))

	if var_18_0 + 1 != var_18_1:
		table.insert(var_18_2, function(arg_20_0)
			var_0_4(arg_18_0, arg_20_0))

	table.insert(var_18_2, function(arg_21_0)
		var_0_3(arg_18_0, arg_21_0))
	seriesAsync(var_18_2, arg_18_1)

def var_0_0.ExpBarAnimation(arg_22_0, arg_22_1):
	if arg_22_0.oldPlayer.level == arg_22_0.newPlayer.level:
		var_0_1(arg_22_0, arg_22_1)
	else
		var_0_5(arg_22_0, arg_22_1)

def var_0_0.Dispose(arg_23_0):
	for iter_23_0, iter_23_1 in ipairs({
		"playerLv",
		"playerExp",
		"playerExpBar"
	}):
		local var_23_0 = arg_23_0[iter_23_1].gameObject

		if LeanTween.isTweening(var_23_0):
			LeanTween.cancel(var_23_0)

return var_0_0
