HXSet = {}

local var_0_0 = HXSet

var_0_0.codeModeKey = "hx_code_mode"

if PLATFORM_CODE == PLATFORM_CH:
	var_0_0.codeMode = False
	var_0_0.antiSkinMode = True
else
	var_0_0.codeMode = True
	var_0_0.antiSkinMode = True

var_0_0.nameCodeMap = {}
var_0_0.nameEquipCodeMap = {}
var_0_0.nameCodeMap_EN = {
	IJN = "IJN"
}

def var_0_0.init():
	for iter_1_0, iter_1_1 in pairs(pg.name_code):
		local var_1_0

		if iter_1_1.type == 1:
			var_1_0 = var_0_0.nameCodeMap
		elif iter_1_1.type == 2:
			var_1_0 = var_0_0.nameEquipCodeMap
		else
			assert(False)

		var_1_0[iter_1_1.name] = iter_1_1.code

	if pg.gameset.code_switch.key_value == 1 and PlayerPrefs.HasKey(var_0_0.codeModeKey):
		var_0_0.codeMode = PlayerPrefs.GetInt(var_0_0.codeModeKey) == 1

	if PLATFORM_CODE == PLATFORM_CH:
		local var_1_1

		if IsUnityEditor:
			var_1_1 = PathMgr.getAssetBundle("../localization.txt")
		else
			var_1_1 = Application.persistentDataPath .. "/localization.txt"

		if PathMgr.FileExists(var_1_1):
			local var_1_2 = PathMgr.ReadAllLines(var_1_1)

			if string.gsub(var_1_2[0], "%w+%s*=%s*", "") == "True":
				var_0_0.codeMode = True

			local var_1_3 = "Localization_skin = False"

			if var_1_2.Length <= 1:
				local var_1_4 = {
					var_1_2[0],
					var_1_3
				}
			else
				var_1_3 = var_1_2[1]

			if string.gsub(var_1_3, "[_%w]+%s*=%s*", "") == "True":
				var_0_0.antiSkinMode = True
		else
			System.IO.File.WriteAllText(var_1_1, "Localization = False\nLocalization_skin = False")

	var_0_0.update()

def var_0_0.calcLocalizationUse():
	if PLATFORM_CODE == PLATFORM_CH:
		local var_2_0 = "localization_use"

		if PlayerPrefs.HasKey(var_2_0):
			PlayerPrefs.DeleteKey(var_2_0)

		local var_2_1 = pg.TimeMgr.GetInstance()
		local var_2_2 = getProxy(PlayerProxy).getData().id
		local var_2_3 = "localization_time_1_" .. var_2_2
		local var_2_4 = PlayerPrefs.GetInt(var_2_3, 0)

		if var_0_0.codeMode and not var_2_1.IsSameDay(var_2_4, var_2_1.GetServerTime()):
			pg.m02.sendNotification(GAME.CHEATER_MARK, {
				reason = CC_TYPE_99
			})
			PlayerPrefs.SetInt(var_2_3, var_2_1.GetServerTime())

		local var_2_5 = "localization_time_2_" .. var_2_2
		local var_2_6 = PlayerPrefs.GetInt(var_2_5, 0)

		if var_0_0.antiSkinMode and not var_2_1.IsSameDay(var_2_6, var_2_1.GetServerTime()):
			pg.m02.sendNotification(GAME.CHEATER_MARK, {
				reason = CC_TYPE_100
			})
			PlayerPrefs.SetInt(var_2_5, var_2_1.GetServerTime())

def var_0_0.switchCodeMode():
	if pg.gameset.code_switch.key_value == 1 or var_0_0.codeMode:
		var_0_0.codeMode = not var_0_0.codeMode

		PlayerPrefs.SetInt(var_0_0.codeModeKey, var_0_0.codeMode and 1 or 0)
		PlayerPrefs.Save()
		var_0_0.update()
		originalPrint("anti hx mode. " .. (var_0_0.codeMode and "on" or "off"))

def var_0_0.isHXNation(arg_4_0):
	var_0_0.nationHX = var_0_0.nationHX or {
		[Nation.US] = True,
		[Nation.JP] = True,
		[Nation.DE] = True,
		[Nation.CN] = True,
		[Nation.ITA] = True,
		[Nation.SN] = True,
		[Nation.MNF] = True,
		[Nation.META] = True
	}

	return var_0_0.nationHX[arg_4_0]

def var_0_0.update():
	local var_5_0 = var_0_0.codeMode and {} or var_0_0.nameCodeMap
	local var_5_1 = var_0_0.codeMode and {} or var_0_0.nameEquipCodeMap
	local var_5_2 = var_0_0.codeMode and {} or var_0_0.nameCodeMap_EN
	local var_5_3 = pg.ship_data_statistics

	pg.ship_data_statistics = setmetatable({}, {
		def __index:(arg_6_0, arg_6_1)
			local var_6_0 = var_5_3[arg_6_1]

			if var_6_0 == None:
				return var_6_0
			elif var_6_0.name == None:
				arg_6_0[arg_6_1] = var_6_0

				return arg_6_0[arg_6_1]

			arg_6_0[arg_6_1] = {}

			if var_0_0.isHXNation(var_6_0.nationality) and var_5_0[var_6_0.name]:
				arg_6_0[arg_6_1].name = var_5_0[var_6_0.name]

			if var_6_0.english_name and #var_6_0.english_name > 0:
				arg_6_0[arg_6_1].english_name = var_6_0.english_name

				for iter_6_0, iter_6_1 in pairs(var_5_2):
					arg_6_0[arg_6_1].english_name = string.gsub(arg_6_0[arg_6_1].english_name or "", iter_6_0, iter_6_1)

			setmetatable(arg_6_0[arg_6_1], {
				__index = var_6_0
			})

			return arg_6_0[arg_6_1]
	})

	local var_5_4 = pg.fleet_tech_ship_class

	pg.fleet_tech_ship_class = setmetatable({}, {
		def __index:(arg_7_0, arg_7_1)
			local var_7_0 = var_5_4[arg_7_1]

			if var_7_0 == None:
				return var_7_0
			elif var_7_0.name == None:
				arg_7_0[arg_7_1] = var_7_0

				return arg_7_0[arg_7_1]

			local var_7_1, var_7_2 = string.gsub(var_7_0.name, "级", "")

			if var_0_0.isHXNation(var_7_0.nation) and var_5_0[var_7_1]:
				arg_7_0[arg_7_1] = setmetatable({
					name = var_5_0[var_7_1] .. (var_7_2 > 0 and "级" or "")
				}, {
					__index = var_7_0
				})
			else
				arg_7_0[arg_7_1] = var_7_0

			return arg_7_0[arg_7_1]
	})

	local var_5_5 = pg.enemy_data_statistics

	pg.enemy_data_statistics = setmetatable({}, {
		def __index:(arg_8_0, arg_8_1)
			local var_8_0 = var_5_5[arg_8_1]

			if var_8_0 == None:
				return var_8_0
			elif var_8_0.name == None:
				arg_8_0[arg_8_1] = var_8_0

				return arg_8_0[arg_8_1]

			if var_0_0.isHXNation(var_8_0.nationality) and var_5_0[var_8_0.name]:
				arg_8_0[arg_8_1] = setmetatable({
					name = var_5_0[var_8_0.name]
				}, {
					__index = var_8_0
				})
			else
				arg_8_0[arg_8_1] = var_8_0

			return arg_8_0[arg_8_1]
	})

	local var_5_6 = pg.equip_data_statistics

	pg.equip_data_statistics = setmetatable({}, {
		def __index:(arg_9_0, arg_9_1)
			local var_9_0 = var_5_6[arg_9_1]

			if var_9_0 == None:
				return var_9_0
			elif var_9_0.name == None:
				arg_9_0[arg_9_1] = var_9_0

				return arg_9_0[arg_9_1]

			if var_5_1[var_9_0.name]:
				arg_9_0[arg_9_1] = setmetatable({
					name = var_5_1[var_9_0.name]
				}, {
					__index = var_9_0
				})
			else
				arg_9_0[arg_9_1] = var_9_0

			return arg_9_0[arg_9_1]
	})

def var_0_0.hxLan(arg_10_0, arg_10_1):
	return string.gsub(arg_10_0 or "", "{namecode.(%d+).-}", function(arg_11_0)
		local var_11_0 = pg.name_code[tonumber(arg_11_0)]

		return var_11_0 and ((var_0_0.codeMode or arg_10_1) and var_11_0.name or var_11_0.code))

def var_0_0.isHx():
	return not var_0_0.codeMode

def var_0_0.isHxSkin():
	return not var_0_0.antiSkinMode

def var_0_0.isHxPropose():
	return not var_0_0.codeMode and PLATFORM_CODE == PLATFORM_CH and LOCK_PROPOSE_SHIP

var_0_0.hxPathList = {
	"live2d",
	"painting",
	"shipYardIcon",
	"paintingface",
	"char",
	"shipmodels",
	"technologycard",
	"shipdesignicon",
	"herohrzicon",
	"skinunlockanim"
}
var_0_0.folderBundle = {
	"paintingface"
}

def var_0_0.needShift(arg_15_0):
	for iter_15_0, iter_15_1 in ipairs(var_0_0.hxPathList):
		if string.find(arg_15_0, iter_15_1):
			return True

	return False

def var_0_0.isFolderBundle(arg_16_0):
	for iter_16_0, iter_16_1 in ipairs(var_0_0.folderBundle):
		if string.find(arg_16_0, iter_16_1):
			return True

	return False

def var_0_0.autoHxShift(arg_17_0, arg_17_1):
	if var_0_0.isHx():
		if string.find(arg_17_0, "live2d"):
			if checkABExist(arg_17_0 .. arg_17_1 .. "_hx"):
				return arg_17_0, arg_17_1 .. "_hx"
			elif pg.l2dhx[arg_17_1]:
				return arg_17_0, arg_17_1 .. "_hx"

		if var_0_0.needShift(arg_17_0):
			local var_17_0 = arg_17_0 .. arg_17_1

			if checkABExist(var_17_0 .. "_hx"):
				return arg_17_0, arg_17_1 .. "_hx"

	return arg_17_0, arg_17_1

def var_0_0.autoHxShiftPath(arg_18_0, arg_18_1, arg_18_2):
	if var_0_0.isHx():
		if string.find(arg_18_0, "live2d"):
			if arg_18_2:
				local var_18_0 = string.gsub(arg_18_0, "live2d/", "")

				if pg.l2dhx[var_18_0]:
					return arg_18_0 .. "_hx"
			elif checkABExist(arg_18_0 .. "_hx"):
				return arg_18_0 .. "_hx"
			else
				local var_18_1 = string.gsub(arg_18_0, "live2d/", "")

				if pg.l2dhx[var_18_1]:
					return arg_18_0 .. "_hx"

		if var_0_0.needShift(arg_18_0) and checkABExist(arg_18_0 .. "_hx"):
			if var_0_0.isFolderBundle(arg_18_0):
				return arg_18_0 .. "_hx", arg_18_1
			elif arg_18_1 and #arg_18_1 > 0:
				return arg_18_0 .. "_hx", arg_18_1 .. "_hx"
			else
				return arg_18_0 .. "_hx", arg_18_1

	return arg_18_0, arg_18_1

var_0_0.init()
