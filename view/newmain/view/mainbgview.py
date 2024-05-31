local var_0_0 = class("MainBGView", import("..base.MainBaseView"))
local var_0_1 = {
	{
		{
			0,
			5
		},
		"bg_main_night"
	},
	{
		{
			5,
			8
		},
		"bg_main_twilight"
	},
	{
		{
			8,
			16
		},
		"bg_main_day"
	},
	{
		{
			16,
			19
		},
		"bg_main_twilight"
	},
	{
		{
			19,
			24
		},
		"bg_main_night"
	}
}
local var_0_2 = 0

def var_0_0.GetBgAndBgm():
	local var_1_0 = var_0_1
	local var_1_1 = getProxy(ActivityProxy).RawGetActivityById(pg.gameset.dayandnight_bgm.key_value)

	if var_1_1 and not var_1_1.isEnd():
		var_1_0 = pg.gameset.dayandnight_bgm.description

	local var_1_2 = pg.TimeMgr.GetInstance().GetServerHour()

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		local var_1_3 = iter_1_1[1]

		if var_1_2 >= var_1_3[1] and var_1_2 < var_1_3[2]:
			return iter_1_1[2], iter_1_1[3]

def var_0_0.Ctor(arg_2_0, arg_2_1):
	var_0_0.super.Ctor(arg_2_0, arg_2_1, None)

	arg_2_0._tf = arg_2_1
	arg_2_0._go = arg_2_1.gameObject
	arg_2_0.paintingCanvases = {
		arg_2_1.parent.parent.Find("paintBg").GetComponent(typeof(Canvas)),
		arg_2_1.parent.parent.Find("paint").GetComponent(typeof(Canvas))
	}
	arg_2_0.isSpecialBg = False
	arg_2_0.isloading = False

def var_0_0.getUIName(arg_3_0):
	return "MainBGView"

def var_0_0.Init(arg_4_0, arg_4_1):
	arg_4_0.ship = arg_4_1

	arg_4_0.ClearSpecailBg()

	local var_4_0 = arg_4_1.getShipBgPrint()

	arg_4_0.isSpecialBg = var_4_0 != arg_4_1.rarity2bgPrintForGet()

	local var_4_1, var_4_2 = MainPaintingView.GetAssistantStatus(arg_4_1)

	if arg_4_0.isSpecialBg and var_4_2:
		arg_4_0.SetSpecailBg(var_4_0)
		arg_4_0.ClearMapBg()
		arg_4_0.ClearCommonBg()
	elif var_0_2 and var_0_2 != 0:
		local var_4_3 = pg.expedition_data_by_map[var_0_2]

		assert(var_4_3, "expedition_data_by_map >>> " .. var_0_2)

		local var_4_4 = var_4_3.bg .. "_" .. var_4_3.ani_name

		if arg_4_0.mapLoaderKey != var_4_4:
			arg_4_0.ClearMapBg()

			arg_4_0.mapLoaderKey = var_4_4

			arg_4_0.SetMapBg(var_4_3.bg, var_4_3.ani_name)

		arg_4_0.ClearCommonBg()
	else
		local var_4_5 = var_0_0.GetBgAndBgm()

		if arg_4_0.commonBg == var_4_5:
			return

		arg_4_0.SetCommonBg(var_4_5)
		arg_4_0.ClearMapBg()

		arg_4_0.commonBg = var_4_5

def var_0_0.ClearCommonBg(arg_5_0):
	arg_5_0.commonBg = None

def var_0_0.Refresh(arg_6_0, arg_6_1):
	arg_6_0.Init(arg_6_1)

def var_0_0.SetSpecailBg(arg_7_0, arg_7_1):
	arg_7_0.isloading = True

	pg.DynamicBgMgr.GetInstance().LoadBg(arg_7_0, arg_7_1, arg_7_0._tf.parent, arg_7_0._tf, function(arg_8_0)
		arg_7_0.isloading = False
		arg_8_0.transform.localPosition = Vector3(0, 0, 200), function()
		arg_7_0.isloading = False)

def var_0_0.SetMapBg(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.isloading = True
	arg_10_0.effectGo = None

	parallelAsync({
		function(arg_11_0)
			PoolMgr.GetInstance().GetSprite("levelmap/" .. arg_10_1, "", True, function(arg_12_0)
				setImageSprite(arg_10_0._tf, arg_12_0)
				arg_11_0()),
		function(arg_13_0)
			if not arg_10_2 or arg_10_2 == "":
				arg_13_0()

				return

			PoolMgr.GetInstance().GetPrefab("ui/" .. arg_10_2, "", True, function(arg_14_0)
				setParent(arg_14_0, arg_10_0._tf)
				arg_10_0.AdjustMapEffect(arg_14_0)

				arg_10_0.effectGo = arg_14_0

				arg_13_0())
	}, function()
		arg_10_0.isloading = False)

def var_0_0.ClearMapBg(arg_16_0):
	if not IsNil(arg_16_0.effectGo):
		Object.Destroy(arg_16_0.effectGo)

		arg_16_0.effectGo = None

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.paintingCanvases):
		iter_16_1.overrideSorting = False
		iter_16_1.sortingOrder = 0

	arg_16_0.mapLoaderKey = None

def var_0_0.AdjustMapEffect(arg_17_0, arg_17_1):
	local var_17_0 = -math.huge
	local var_17_1 = arg_17_1.GetComponentsInChildren(typeof(Canvas))

	for iter_17_0 = 1, var_17_1.Length:
		local var_17_2 = var_17_1[iter_17_0 - 1]

		if var_17_0 < var_17_2.sortingOrder:
			var_17_0 = var_17_2.sortingOrder

	local var_17_3 = arg_17_1.GetComponentsInChildren(typeof("UnityEngine.ParticleSystemRenderer"))

	for iter_17_1 = 1, var_17_3.Length:
		local var_17_4 = var_17_3[iter_17_1 - 1]
		local var_17_5 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.ParticleSystemRenderer"), "sortingOrder", var_17_4)

		if var_17_0 < var_17_5:
			var_17_0 = var_17_5

	for iter_17_2, iter_17_3 in ipairs(arg_17_0.paintingCanvases):
		iter_17_3.overrideSorting = True
		iter_17_3.sortingOrder = var_17_0 + (iter_17_2 == 3 and 2 or 1)

def var_0_0.SetCommonBg(arg_18_0, arg_18_1):
	setActive(arg_18_0._tf, True)

	local var_18_0 = LoadSprite("commonbg/" .. arg_18_1, "")

	setImageSprite(arg_18_0._tf, var_18_0)

def var_0_0.ClearSpecailBg(arg_19_0):
	if arg_19_0.isSpecialBg:
		pg.DynamicBgMgr.GetInstance().ClearBg(arg_19_0.getUIName())

		arg_19_0.isSpecialBg = False

def var_0_0.IsLoading(arg_20_0):
	return arg_20_0.isloading

def var_0_0.Disable(arg_21_0):
	arg_21_0.ClearSpecailBg()

def var_0_0.Dispose(arg_22_0):
	var_0_0.super.Dispose(arg_22_0)
	arg_22_0.ClearSpecailBg()
	arg_22_0.ClearMapBg()

return var_0_0
