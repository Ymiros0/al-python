local var_0_0 = class("AnniversaryIslandHotSpringScene", import("view.activity.BackHills.NewYearFestival.NewYearHotSpringScene"))

def var_0_0.getUIName(arg_1_0):
	return "AnniversaryIslandHotSpringUI"

local var_0_1 = 0.85

def var_0_0.init(arg_2_0):
	arg_2_0.scrollRect = arg_2_0._tf.Find("ScrollRect")
	arg_2_0.scrollContent = arg_2_0.scrollRect.GetComponent(typeof(ScrollRect)).content
	arg_2_0.slotTFs = _.map(_.range(4, 15), function(arg_3_0)
		return arg_2_0.scrollRect.Find("Pool").GetChild(arg_3_0 - 1))

	local var_2_0 = table.remove(arg_2_0.slotTFs, 12)
	local var_2_1 = table.remove(arg_2_0.slotTFs, 11)

	table.insert(arg_2_0.slotTFs, 1, var_2_1)
	table.insert(arg_2_0.slotTFs, 7, var_2_0)

	arg_2_0.slotOriginalPos = _.map(arg_2_0.slotTFs, function(arg_4_0)
		return arg_4_0.anchoredPosition)
	arg_2_0.slotShipPos = Clone(arg_2_0.slotOriginalPos)

	table.Foreach(arg_2_0.GetRecordPos(), function(arg_5_0, arg_5_1)
		arg_2_0.slotShipPos[arg_5_0] = arg_5_1)

	arg_2_0.poolItems = _.map(_.range(arg_2_0.scrollRect.Find("Pool").childCount), function(arg_6_0)
		return arg_2_0.scrollRect.Find("Pool").GetChild(arg_6_0 - 1))

	Canvas.ForceUpdateCanvases()

	arg_2_0.scrollBGs = _.map({
		{
			"1",
			0.5
		},
		{
			"2",
			0.6
		},
		{
			"3",
			var_0_1
		},
		{
			"Pool",
			var_0_1
		},
		{
			"4",
			1
		},
		{
			"5",
			1
		}
	}, function(arg_7_0)
		local var_7_0 = {
			arg_2_0.scrollRect.Find(arg_7_0[1]),
			arg_7_0[2]
		}

		var_7_0[3] = var_7_0[1].anchoredPosition.x

		arg_2_0.UpdateScrollContent(0, unpack(var_7_0))

		return var_7_0)
	arg_2_0.top = arg_2_0._tf.Find("Top")

	pg.ViewUtils.SetSortingOrder(arg_2_0._tf, -1001)

	arg_2_0.spineRoles = {}
	arg_2_0.washMaterial = Material.New(pg.ShaderMgr.GetInstance().GetShader("M02/Unlit_Colored_Semitransparent"))

	arg_2_0.washMaterial.SetFloat("_Height", 0.5)

def var_0_0.SetActivity(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.activity

	arg_8_0.activity = arg_8_1

	if not var_8_0:
		return

	table.Foreach(var_8_0.data1_list, function(arg_9_0, arg_9_1)
		if arg_9_1 > 0 and (arg_8_1.data1_list[arg_9_0] or 0) == 0:
			arg_8_0.slotShipPos[arg_9_0] = Clone(arg_8_0.slotOriginalPos[arg_9_0]))

def var_0_0.didEnter(arg_10_0):
	var_0_0.super.didEnter(arg_10_0)
	pg.NewStoryMgr.GetInstance().Play(arg_10_0.activity.getConfig("config_client").unlockstory)

def var_0_0.UpdateView(arg_11_0):
	arg_11_0.UpdateSlots()

def var_0_0.GetRecordPos(arg_12_0):
	local var_12_0 = PlayerPrefs.GetString("hotspring_ship_pos_2023", "")
	local var_12_1 = _.map(string.split(var_12_0, ";"), function(arg_13_0)
		return tonumber(arg_13_0))
	local var_12_2 = {}

	for iter_12_0 = 1, #var_12_1, 2:
		table.insert(var_12_2, Vector2.New(var_12_1[iter_12_0], var_12_1[iter_12_0 + 1]))

	return var_12_2

def var_0_0.RecordPos(arg_14_0, arg_14_1):
	if not arg_14_1:
		return

	local var_14_0 = table.concat(_.reduce(arg_14_1, {}, function(arg_15_0, arg_15_1)
		table.insert(arg_15_0, arg_15_1.x)
		table.insert(arg_15_0, arg_15_1.y)

		return arg_15_0), ";")

	PlayerPrefs.SetString("hotspring_ship_pos_2023", var_14_0)

return var_0_0
