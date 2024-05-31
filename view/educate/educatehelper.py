local var_0_0 = class("EducateHelper")

def var_0_0.GetItemAddDrops(arg_1_0):
	local var_1_0 = pg.child_item[arg_1_0.id].display
	local var_1_1 = {}

	underscore.each(var_1_0, function(arg_2_0)
		assert(arg_2_0[1] == EducateConst.DROP_TYPE_ATTR or arg_2_0[1] == EducateConst.DROP_TYPE_RES, "非法道具增益, item id." .. arg_1_0.id)
		table.insert(var_1_1, {
			type = arg_2_0[1],
			id = arg_2_0[2],
			number = arg_2_0[3] * arg_1_0.number
		}))

	return var_1_1

def var_0_0.UpdateDropsData(arg_3_0):
	local var_3_0 = getProxy(EducateProxy)

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		switch(iter_3_1.type, {
			[EducateConst.DROP_TYPE_ATTR] = function()
				var_3_0.UpdateAttr(iter_3_1.id, iter_3_1.number),
			[EducateConst.DROP_TYPE_RES] = function()
				var_3_0.UpdateRes(iter_3_1.id, iter_3_1.number),
			[EducateConst.DROP_TYPE_ITEM] = function()
				var_3_0.AddItem(iter_3_1.id, iter_3_1.number)

				local var_6_0 = var_0_0.GetItemAddDrops(iter_3_1)

				var_0_0.UpdateDropsData(var_6_0),
			[EducateConst.DROP_TYPE_MEMORY] = function()
				var_3_0.AddMemory(iter_3_1.id, iter_3_1.number),
			[EducateConst.DROP_TYPE_POLAROID] = function()
				var_3_0.AddPolaroid(iter_3_1.id),
			[EducateConst.DROP_TYPE_BUFF] = function()
				var_3_0.AddBuff(iter_3_1.id)
		})

def var_0_0.UpdateDropShow(arg_10_0, arg_10_1):
	if arg_10_1.type == EducateConst.DROP_TYPE_MEMORY or arg_10_1.type == EducateConst.DROP_TYPE_POLAROID:
		pg.TipsMgr.GetInstance().ShowTips(string.format("不支持的掉落展示for Item,请检查配置！type.%d, id.%d", arg_10_1.type, arg_10_1.id))

		return

	local var_10_0 = var_0_0.GetDropConfig(arg_10_1)

	LoadImageSpriteAsync("educateprops/" .. var_10_0.icon, findTF(arg_10_0, "frame/icon"))
	setText(findTF(arg_10_0, "frame/count_bg/count"), "x" .. arg_10_1.number)
	setText(findTF(arg_10_0, "name_bg/name"), shortenString(var_10_0.name, 5))

	if arg_10_1.type == EducateConst.DROP_TYPE_ITEM:
		local var_10_1 = EducateItem.RARITY2FRAME[var_10_0.rarity]

		GetImageSpriteFromAtlasAsync("ui/educatecommonui_atlas", var_10_1, findTF(arg_10_0, "frame"))

def var_0_0.GetDropConfig(arg_11_0):
	return switch(arg_11_0.type, {
		[EducateConst.DROP_TYPE_ATTR] = function()
			local var_12_0 = pg.child_attr[arg_11_0.id]

			assert(var_12_0, "找不到child_attr配置, id. " .. arg_11_0.id)

			return var_12_0,
		[EducateConst.DROP_TYPE_RES] = function()
			local var_13_0 = pg.child_resource[arg_11_0.id]

			assert(var_13_0, "找不到child_resource配置, id. " .. arg_11_0.id)

			return var_13_0,
		[EducateConst.DROP_TYPE_ITEM] = function()
			local var_14_0 = pg.child_item[arg_11_0.id]

			assert(var_14_0, "找不到child_item配置, id. " .. arg_11_0.id)

			return var_14_0,
		[EducateConst.DROP_TYPE_MEMORY] = function()
			local var_15_0 = pg.child_memory[arg_11_0.id]

			assert(var_15_0, "找不到child_memory配置, id. " .. arg_11_0.id)

			return var_15_0,
		[EducateConst.DROP_TYPE_POLAROID] = function()
			local var_16_0 = pg.child_polaroid[arg_11_0.id]

			assert(var_16_0, "找不到child_polaroid配置, id. " .. arg_11_0.id)

			return var_16_0,
		[EducateConst.DROP_TYPE_BUFF] = function()
			local var_17_0 = pg.child_buff[arg_11_0.id]

			assert(var_17_0, "找不到child_buff配置, id. " .. arg_11_0.id)

			return var_17_0
	})

def var_0_0.GetColorForAttrDrop(arg_18_0):
	if arg_18_0.type == EducateConst.DROP_TYPE_RES:
		return Color.NewHex("6FD9C4")
	elif arg_18_0.type == EducateConst.DROP_TYPE_ATTR:
		local var_18_0 = getProxy(EducateProxy).GetCharData().GetAttrTypeById(arg_18_0.id)

		if var_18_0 == EducateChar.ATTR_TYPE_MAJOR:
			return Color.NewHex("5DC9FD")
		elif var_18_0 == EducateChar.ATTR_TYPE_PERSONALITY:
			return Color.NewHex("6FD9C4")
		elif var_18_0 == EducateChar.ATTR_TYPE_MINOR:
			return Color.NewHex("8CA1EE")

	return Color.NewHex("39BFFF")

def var_0_0.UpdateDropShowForAttr(arg_19_0, arg_19_1):
	if arg_19_1.type != EducateConst.DROP_TYPE_ATTR and arg_19_1.type != EducateConst.DROP_TYPE_RES:
		pg.TipsMgr.GetInstance().ShowTips(string.format("不支持的掉落展示for Attr,请检查配置！type.%d, id.%d", arg_19_1.type, arg_19_1.id))

		return

	setImageColor(arg_19_0, var_0_0.GetColorForAttrDrop(arg_19_1))

	local var_19_0 = arg_19_1.type == EducateConst.DROP_TYPE_ATTR and "attr_" or "res_"
	local var_19_1 = arg_19_1.number > 0 and "+" or ""
	local var_19_2 = var_0_0.GetDropConfig(arg_19_1)

	setActive(findTF(arg_19_0, "icon"), True)
	GetImageSpriteFromAtlasAsync("ui/educatecommonui_atlas", var_19_0 .. arg_19_1.id, findTF(arg_19_0, "icon"))
	setText(findTF(arg_19_0, "name"), var_19_2.name)
	setText(findTF(arg_19_0, "value"), var_19_1 .. arg_19_1.number)

def var_0_0.FilterDropByTypes(arg_20_0, arg_20_1):
	return underscore.select(arg_20_0, function(arg_21_0)
		return table.contains(arg_20_1, arg_21_0.type))

def var_0_0.GetDialogueShowDrops(arg_22_0):
	return var_0_0.FilterDropByTypes(arg_22_0, {
		EducateConst.DROP_TYPE_ATTR,
		EducateConst.DROP_TYPE_RES,
		EducateConst.DROP_TYPE_BUFF
	})

def var_0_0.GetCommonShowDrops(arg_23_0):
	return var_0_0.FilterDropByTypes(arg_23_0, {
		EducateConst.DROP_TYPE_ITEM,
		EducateConst.DROP_TYPE_POLAROID
	})

def var_0_0.UpdateAvatarShow(arg_24_0, arg_24_1, arg_24_2):
	setImageSprite(findTF(arg_24_0, "mask/Image"), LoadSprite("squareicon/" .. arg_24_2), True)

	local var_24_0 = 0

	for iter_24_0, iter_24_1 in ipairs(arg_24_1):
		local var_24_1 = findTF(arg_24_0, "progress/" .. iter_24_1[1])
		local var_24_2 = iter_24_1[2] - 0.005

		setFillAmount(var_24_1, var_24_2)
		setLocalEulerAngles(var_24_1, Vector3(0, 0, -360 * var_24_0))

		var_24_0 = var_24_0 + var_24_2 + 0.005

def var_0_0.GetTimeFromCfg(arg_25_0):
	return {
		month = arg_25_0[1],
		week = arg_25_0[2],
		day = arg_25_0[3]
	}

def var_0_0.IsSameDay(arg_26_0, arg_26_1):
	return arg_26_0.month == arg_26_1.month and arg_26_0.week == arg_26_1.week and arg_26_0.day == arg_26_1.day

def var_0_0.CfgTime2Time(arg_27_0):
	return {
		month = arg_27_0[1][1],
		week = arg_27_0[1][2] or 1,
		day = arg_27_0[1][3] or 1
	}, {
		month = arg_27_0[2][1],
		week = arg_27_0[2][2] or 4,
		day = arg_27_0[2][3] or 7
	}

def var_0_0.IsBeforeTime(arg_28_0, arg_28_1):
	if arg_28_0.month < arg_28_1.month:
		return True

	if arg_28_0.month == arg_28_1.month and arg_28_0.week < arg_28_1.week:
		return True

	if arg_28_0.month == arg_28_1.month and arg_28_0.week == arg_28_1.week and arg_28_0.day < arg_28_1.day:
		return True

	return False

def var_0_0.IsAfterTime(arg_29_0, arg_29_1):
	if arg_29_0.month > arg_29_1.month:
		return True

	if arg_29_0.month == arg_29_1.month and arg_29_0.week > arg_29_1.week:
		return True

	if arg_29_0.month == arg_29_1.month and arg_29_0.week == arg_29_1.week and arg_29_0.day > arg_29_1.day:
		return True

	return False

def var_0_0.InTime(arg_30_0, arg_30_1, arg_30_2):
	return not var_0_0.IsBeforeTime(arg_30_0, arg_30_1) and not var_0_0.IsAfterTime(arg_30_0, arg_30_2)

def var_0_0.GetTimeAfterDays(arg_31_0, arg_31_1):
	local var_31_0 = {
		month = arg_31_0.month,
		week = arg_31_0.week,
		day = arg_31_0.day,
		day = arg_31_0.day + arg_31_1
	}

	while var_31_0.day > 7 or var_31_0.week > 4:
		if var_31_0.day > 7:
			var_31_0.day = var_31_0.day - 7
			var_31_0.week = var_31_0.week + 1

		if var_31_0.week > 4:
			var_31_0.week = var_31_0.week - 4
			var_31_0.month = var_31_0.month + 1

	return var_31_0

def var_0_0.GetTimeAfterWeeks(arg_32_0, arg_32_1):
	local var_32_0 = {
		month = arg_32_0.month,
		week = arg_32_0.week,
		day = arg_32_0.day
	}

	var_32_0.week = var_32_0.week + arg_32_1

	while var_32_0.week > 4:
		var_32_0.week = var_32_0.week - 4
		var_32_0.month = var_32_0.month + 1

	return var_32_0

def var_0_0.GetDaysBetweenTimes(arg_33_0, arg_33_1):
	return (arg_33_1.month - arg_33_0.month) * 28 + (arg_33_1.week - arg_33_0.week) * 7 + (arg_33_1.day - arg_33_0.day)

def var_0_0.GetWeekIdxWithTime(arg_34_0):
	return (arg_34_0.month - 1) * 4 + arg_34_0.week

def var_0_0.GetShowMonthNumber(arg_35_0):
	return arg_35_0 > 12 and arg_35_0 - 12 or arg_35_0

def var_0_0.GetWeekByNumber(arg_36_0):
	if arg_36_0 == 7:
		return i18n("word_day")
	else
		return i18n("number_" .. arg_36_0)

def var_0_0.GetWeekStrByNumber(arg_37_0):
	return i18n("word_week_day" .. arg_37_0)

def var_0_0.InUnlockTime(arg_38_0, arg_38_1):
	if arg_38_0.month > arg_38_1[1]:
		return True

	if arg_38_0.month == arg_38_1[1] and arg_38_0.week > arg_38_1[2]:
		return True

	if arg_38_0.month == arg_38_1[1] and arg_38_0.week == arg_38_1[2] and arg_38_0.day >= arg_38_1[3]:
		return True

	return False

def var_0_0.IsSystemUnlock(arg_39_0):
	local var_39_0 = getProxy(EducateProxy).IsFirstGame()
	local var_39_1 = EducateConst.SYSTEM_UNLOCK_CONFIG[arg_39_0]

	if not var_39_0 and var_39_1[2]:
		return True

	local var_39_2 = getProxy(EducateProxy).GetCurTime()
	local var_39_3 = pg.gameset[var_39_1[1]].description

	return var_0_0.InUnlockTime(var_39_2, var_39_3)

def var_0_0.IsShowNature():
	local var_40_0, var_40_1 = var_0_0.CfgTime2Time(pg.gameset.child_charactor_time.description)

	return var_0_0.InTime(getProxy(EducateProxy).GetCurTime(), var_40_0, var_40_1)

def var_0_0.IsSiteUnlock(arg_41_0, arg_41_1):
	local var_41_0 = pg.child_site[arg_41_0]
	local var_41_1 = getProxy(EducateProxy).GetCurTime()
	local var_41_2 = arg_41_1 and var_41_0.unlock_time_1 or var_41_0.unlock_time_2

	return var_0_0.InUnlockTime(var_41_1, var_41_2)

def var_0_0.IsMatchSubType(arg_42_0, arg_42_1):
	if arg_42_0 == "":
		return False

	if type(arg_42_0) == "table":
		return table.contains(arg_42_0, arg_42_1)
	elif type(arg_42_0) == "string":
		return arg_42_1 == tonumber(arg_42_0)

	return False

def var_0_0.ReqEducateDataCheck(arg_43_0):
	if LOCK_EDUCATE_SYSTEM:
		arg_43_0()

		return

	local var_43_0 = {}

	if not getProxy(EducateProxy).CheckDataRequestEnd():
		table.insert(var_43_0, function(arg_44_0)
			pg.m02.sendNotification(GAME.EDUCATE_REQUEST, {
				callback = arg_44_0
			}))

	seriesAsync(var_43_0, arg_43_0)

return var_0_0
