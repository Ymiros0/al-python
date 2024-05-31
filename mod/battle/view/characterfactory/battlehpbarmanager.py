ys = ys or {}

local var_0_0 = ys
local var_0_1 = require("Mgr/Pool/PoolUtil")
local var_0_2 = singletonClass("BattleHPBarManager")

var_0_0.Battle.BattleHPBarManager = var_0_2
var_0_2.__name = "BattleHPBarManager"
var_0_2.ROOT_NAME = "HPBarContainer"
var_0_2.HP_BAR_FRIENDLY = "heroBlood"
var_0_2.HP_BAR_FOE = "enemyBlood"
var_0_2.ORIGIN_BAR_WIDTH = {
	heroBlood = 70,
	enemyBlood = 154
}
var_0_2.ORIGIN_PROGRESS_WIDTH = {
	heroBlood = 66,
	enemyBlood = 153
}

def var_0_2.Ctor(arg_1_0):
	return

def var_0_2.Init(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._allPool = {}
	arg_2_0._ob2Pool = {}
	arg_2_0._allPool[var_0_2.HP_BAR_FRIENDLY] = var_0_2.generateTempPool(var_0_2.HP_BAR_FRIENDLY, arg_2_2, arg_2_1, 3, 10)
	arg_2_0._allPool[var_0_2.HP_BAR_FOE] = var_0_2.generateTempPool(var_0_2.HP_BAR_FOE, arg_2_2, arg_2_1, 8, 10)

def var_0_2.InitialPoolRoot(arg_3_0, arg_3_1):
	arg_3_0._allPool[var_0_2.HP_BAR_FRIENDLY].ResetParent(arg_3_1)
	arg_3_0._allPool[var_0_2.HP_BAR_FOE].ResetParent(arg_3_1)

def var_0_2.Clear(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0._allPool):
		iter_4_1.Dispose()

	arg_4_0._ob2Pool = {}
	arg_4_0._allPool = {}

def var_0_2.GetHPBar(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0._allPool[arg_5_1]
	local var_5_1 = var_5_0.GetObject()

	arg_5_0._ob2Pool[var_5_1] = var_5_0

	local var_5_2 = var_5_1.transform

	var_5_2.Find("blood").GetComponent(typeof(Image)).fillAmount = 1

	local var_5_3 = var_5_2.Find("type")

	if var_5_3:
		SetActive(var_5_3, False)

	local var_5_4 = var_5_2.Find("torpedoIcons")

	if var_5_4:
		SetActive(var_5_4, False)

	local var_5_5 = var_5_2.Find("biasBar")

	if var_5_5:
		SetActive(var_5_5, False)

	return var_5_1

def var_0_2.DestroyObj(arg_6_0, arg_6_1):
	if arg_6_1 == None:
		return

	local var_6_0 = arg_6_0._ob2Pool[arg_6_1]

	if var_6_0:
		var_6_0.Recycle(arg_6_1)
	else
		Object.Destroy(arg_6_1)

local var_0_3 = Vector3(0, 10000, 0)

def var_0_2.HideBullet(arg_7_0):
	arg_7_0.transform.position = var_0_3

def var_0_2.generateTempPool(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	local var_8_0 = arg_8_2.transform.Find(arg_8_0).gameObject

	var_8_0.transform.position = var_0_3

	var_8_0.SetActive(True)

	local var_8_1 = pg.Pool.New(arg_8_1, var_8_0, arg_8_3, arg_8_4, True, True)

	var_8_1.SetRecycleFuncs(var_0_2.HideBullet)
	var_8_1.InitSize()

	return var_8_1
