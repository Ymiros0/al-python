local var_0_0 = class("EducateCharGroup")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1

	local var_1_0 = pg.secretary_special_ship.get_id_list_by_group[arg_1_1]

	arg_1_0.charIdList = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		if pg.secretary_special_ship[iter_1_1].secrerary_show == 1:
			table.insert(arg_1_0.charIdList, iter_1_1)

def var_0_0.GetSortWeight(arg_2_0):
	local var_2_0 = arg_2_0.GetShowId()

	return pg.secretary_special_ship[var_2_0].type

def var_0_0.GetCharIdList(arg_3_0):
	return arg_3_0.charIdList

def var_0_0.GetTitle(arg_4_0):
	local var_4_0 = arg_4_0.GetShowId()

	if pg.secretary_special_ship[var_4_0].type == 1:
		return i18n("secretary_special_title_age")
	else
		return i18n("secretary_special_title_physiognomy")

def var_0_0.GetUnlockDesc(arg_5_0):
	local var_5_0 = arg_5_0.GetShowId()

	return pg.secretary_special_ship[var_5_0].unlock_desc

def var_0_0.GetSpriteName(arg_6_0):
	local var_6_0 = arg_6_0.GetShowId()
	local var_6_1 = pg.secretary_special_ship[var_6_0].type

	return "label_" .. var_6_1

def var_0_0.GetShowId(arg_7_0):
	return (_.detect(arg_7_0.charIdList, function(arg_8_0)
		return pg.secretary_special_ship[arg_8_0].type != 0))

def var_0_0.GetShowPainting(arg_9_0):
	local var_9_0 = arg_9_0.GetShowId()

	assert(var_9_0)

	return pg.secretary_special_ship[var_9_0].prefab

def var_0_0.IsSelected(arg_10_0, arg_10_1):
	return _.any(arg_10_0.charIdList, function(arg_11_0)
		return arg_10_1 == arg_11_0)

def var_0_0.IsLock(arg_12_0):
	local var_12_0 = getProxy(EducateProxy).GetSecretaryIDs()
	local var_12_1 = {}

	for iter_12_0, iter_12_1 in ipairs(var_12_0):
		var_12_1[iter_12_1] = True

	return _.all(arg_12_0.charIdList, function(arg_13_0)
		return not var_12_1[arg_13_0])

def var_0_0.ShouldTip(arg_14_0):
	local var_14_0 = getProxy(SettingsProxy)

	return _.any(arg_14_0.charIdList, function(arg_15_0)
		return var_14_0._ShouldEducateCharTip(arg_15_0))

return var_0_0
