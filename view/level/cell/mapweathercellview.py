local var_0_0 = class("MapWeatherCellView", import(".StaticCellView"))

def var_0_0.Ctor(arg_1_0, ...):
	var_0_0.super.Ctor(arg_1_0, ...)

	arg_1_0.weatherPrefabs = {}

def var_0_0.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityUpperEffect

def var_0_0.Update(arg_3_0, arg_3_1):
	if IsNil(arg_3_0.go):
		arg_3_0.PrepareBase("weathers" .. arg_3_0.line.row .. "_" .. arg_3_0.line.column)

	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		if not arg_3_0.weatherPrefabs[iter_3_1]:
			arg_3_0.weatherPrefabs[iter_3_1] = True

			local var_3_0 = pg.weather_data_template[iter_3_1].icon

			if var_3_0 and #var_3_0 > 0:
				arg_3_0.GetLoader().GetPrefab("ui/" .. var_3_0, var_3_0, function(arg_4_0)
					setParent(arg_4_0, arg_3_0.tf)
					setActive(arg_4_0, True)
					arg_3_0.OnLoadedPrefab(arg_4_0, iter_3_1), "Weather" .. iter_3_1)
			elif IsUnityEditor:
				local var_3_1 = GameObject("weatherID_" .. iter_3_1)

				arg_3_0.GetLoader().RegisterLoaded("Weather" .. iter_3_1, var_3_1)
				setParent(var_3_1, arg_3_0.tf)
				setActive(var_3_1, True)

	for iter_3_2, iter_3_3 in pairs(arg_3_0.weatherPrefabs):
		if not table.contains(arg_3_1, iter_3_2):
			arg_3_0.GetLoader().ClearRequest("Weather" .. iter_3_2)

			arg_3_0.weatherPrefabs[iter_3_2] = None

def var_0_0.OnLoadedPrefab(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_2 == ChapterConst.FlagWeatherFog:
		local var_5_0 = tf(arg_5_1).childCount
		local var_5_1 = math.random(1, var_5_0)

		for iter_5_0 = 1, var_5_0:
			setActive(tf(arg_5_1).GetChild(iter_5_0 - 1), iter_5_0 == var_5_1)

return var_0_0
