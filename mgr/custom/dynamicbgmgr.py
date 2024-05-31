pg = pg or {}
pg.DynamicBgMgr = singletonClass("DynamicBgMgr")

local var_0_0 = pg.DynamicBgMgr

def var_0_0.Ctor(arg_1_0):
	arg_1_0.cache = {}

def var_0_0.LoadBg(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, arg_2_6):
	local var_2_0 = "bg/star_level_bg_" .. arg_2_2
	local var_2_1 = "ui/star_level_bg_" .. arg_2_2

	if checkABExist(var_2_1):
		arg_2_0.ClearBg(arg_2_1.getUIName())
		PoolMgr.GetInstance().GetPrefab(var_2_1, "", True, function(arg_3_0)
			if not arg_2_1.exited:
				setParent(arg_3_0, arg_2_3, False)

				local var_3_0 = arg_3_0.GetComponent(typeof(CriManaEffectUI))

				if var_3_0:
					var_3_0.renderMode = ReflectionHelp.RefGetField(typeof("CriManaMovieMaterial+RenderMode"), "Always", None)

					var_3_0.Pause(False)

				setActive(arg_2_4, False)

				if arg_2_5 != None:
					arg_2_5(arg_3_0)

				arg_2_0.InsertCache(arg_2_1.getUIName(), arg_2_2, arg_3_0)
			else
				PoolMgr.GetInstance().DestroyPrefab(var_2_1, ""), 1)
	else
		arg_2_0.ClearBg(arg_2_1.getUIName())
		GetSpriteFromAtlasAsync(var_2_0, "", function(arg_4_0)
			if not arg_2_1.exited:
				setImageSprite(arg_2_4, arg_4_0)
				setActive(arg_2_4, True)

				if arg_2_6 != None:
					arg_2_6(arg_4_0)
			else
				PoolMgr.GetInstance().DestroySprite(var_2_0))

def var_0_0.ClearBg(arg_5_0, arg_5_1):
	for iter_5_0 = #arg_5_0.cache, 1, -1:
		local var_5_0 = arg_5_0.cache[iter_5_0]

		if var_5_0.uiName == arg_5_1:
			local var_5_1 = "ui/star_level_bg_" .. var_5_0.bgName
			local var_5_2 = var_5_0.dyBg

			if IsNil(var_5_2):
				table.remove(arg_5_0.cache, iter_5_0)

				return

			local var_5_3 = var_5_2.GetComponent(typeof(CriManaEffectUI))

			if var_5_3:
				var_5_3.Pause(True)

			PoolMgr.GetInstance().ReturnPrefab(var_5_1, "", var_5_2)

			if #arg_5_0.cache > 1:
				PoolMgr.GetInstance().DestroyPrefab(var_5_1, "")

			table.remove(arg_5_0.cache, iter_5_0)

def var_0_0.InsertCache(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.cache):
		if iter_6_1.uiName == arg_6_1 and iter_6_1.bgName == arg_6_2:
			iter_6_1.dyBg = arg_6_3

			return

	table.insert(arg_6_0.cache, {
		uiName = arg_6_1,
		bgName = arg_6_2,
		dyBg = arg_6_3
	})
