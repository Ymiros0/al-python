local var_0_0 = class("Cryptolalia", import("model.vo.BaseVO"))

var_0_0.STATE_LOCK = 1
var_0_0.STATE_DOWNLOADABLE = 2
var_0_0.STATE_PLAYABLE = 3
var_0_0.STATE_DOWNLOADING = 4
var_0_0.COST_TYPE_GEM = 1
var_0_0.COST_TYPE_TICKET = 2
var_0_0.LANG_TYPE_JP = 0
var_0_0.LANG_TYPE_CH = 1

def var_0_0.GetAssetBundlePath(arg_1_0):
	local var_1_0 = var_0_0.BuildCpkPath(arg_1_0)

	return PathMgr.getAssetBundle(var_1_0)

def var_0_0.GetSubtitleAssetBundlePath(arg_2_0):
	local var_2_0 = var_0_0.BuildSubtitlePath(arg_2_0)

	return PathMgr.getAssetBundle(var_2_0)

def var_0_0.BuildCpkPath(arg_3_0):
	return "originsource/cipher/" .. string.lower(arg_3_0) .. ".cpk"

def var_0_0.BuildSubtitlePath(arg_4_0):
	return "originsource/cipher/" .. string.lower(arg_4_0) .. ".txt"

def var_0_0.Ctor(arg_5_0, arg_5_1):
	arg_5_0.id = arg_5_1.id
	arg_5_0.configId = arg_5_1.id
	arg_5_0.lock = True
	arg_5_0.sizes = {}

def var_0_0.GetState(arg_6_0, arg_6_1):
	if not arg_6_0.IsLock():
		if arg_6_0.IsDownloadRes(arg_6_1):
			return var_0_0.STATE_PLAYABLE
		else
			return var_0_0.STATE_DOWNLOADABLE
	else
		return var_0_0.STATE_LOCK

def var_0_0.IsEmpty(arg_7_0):
	return arg_7_0 == None or arg_7_0 == ""

def var_0_0.GetDefaultLangType(arg_8_0):
	if not var_0_0.IsEmpty(arg_8_0.GetJpCpkName()):
		return var_0_0.LANG_TYPE_JP

	if not var_0_0.IsEmpty(arg_8_0.GetCnCpkName()):
		return var_0_0.LANG_TYPE_CH

def var_0_0.IsDownloadableState(arg_9_0, arg_9_1):
	return arg_9_0.GetState(arg_9_1) == var_0_0.STATE_DOWNLOADABLE

def var_0_0.IsPlayableState(arg_10_0, arg_10_1):
	return arg_10_0.GetState(arg_10_1) == var_0_0.STATE_PLAYABLE

def var_0_0.IsDownloadRes(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.GetCpkName(arg_11_1)
	local var_11_1 = var_0_0.BuildCpkPath(var_11_0)

	return pg.CipherGroupMgr.GetInstance().isCipherExist(var_11_1)

def var_0_0.IsDownloadAllRes(arg_12_0):
	if arg_12_0.IsMultiVersion():
		return arg_12_0.IsDownloadRes(var_0_0.LANG_TYPE_CH) and arg_12_0.IsDownloadRes(var_0_0.LANG_TYPE_JP)
	elif arg_12_0.OnlyChVersion():
		return arg_12_0.IsDownloadRes(var_0_0.LANG_TYPE_CH)
	elif arg_12_0.OnlyJpVersion():
		return arg_12_0.IsDownloadRes(var_0_0.LANG_TYPE_JP)

def var_0_0.IsLockState(arg_13_0, arg_13_1):
	return arg_13_0.GetState(arg_13_1) == var_0_0.STATE_LOCK

def var_0_0.Unlock(arg_14_0):
	arg_14_0.lock = False

def var_0_0.IsLock(arg_15_0):
	return arg_15_0.lock

def var_0_0.bindConfigTable(arg_16_0):
	return pg.soundstory_template

def var_0_0.GetName(arg_17_0):
	return arg_17_0.getConfig("name")

def var_0_0.GetDescription(arg_18_0):
	return arg_18_0.getConfig("overview")

def var_0_0.GetCnCvAuthor(arg_19_0):
	return arg_19_0.getConfig("CV_CN")

def var_0_0.GetJpCvAuthor(arg_20_0):
	return arg_20_0.getConfig("CV_JP")

def var_0_0.GetCvAuthor(arg_21_0, arg_21_1):
	if arg_21_1 == var_0_0.LANG_TYPE_CH:
		return arg_21_0.GetCnCvAuthor()
	elif arg_21_1 == var_0_0.LANG_TYPE_JP:
		return arg_21_0.GetJpCvAuthor()

def var_0_0.GetShipGroupId(arg_22_0):
	return arg_22_0.getConfig("ship_id")

def var_0_0.IsSameGroup(arg_23_0, arg_23_1):
	return arg_23_0.GetShipGroupId() == arg_23_1

def var_0_0.GetShipName(arg_24_0):
	local var_24_0 = arg_24_0.GetShipGroupId()
	local var_24_1 = ShipGroup.getDefaultShipConfig(var_24_0)

	return (HXSet.hxLan(var_24_1.name))

def var_0_0.ShipIcon(arg_25_0):
	local var_25_0 = arg_25_0.GetShipGroupId()
	local var_25_1 = ShipGroup.getDefaultShipConfig(var_25_0)

	return pg.ship_skin_template[var_25_1.skin_id].prefab

def var_0_0.GetCnAudition(arg_26_0):
	return arg_26_0.getConfig("audition_resource_CN")

def var_0_0.GetJpAudition(arg_27_0):
	return arg_27_0.getConfig("audition_resource_JP")

def var_0_0.GetAudition(arg_28_0, arg_28_1):
	if arg_28_1 == var_0_0.LANG_TYPE_CH:
		return arg_28_0.GetCnAudition()
	elif arg_28_1 == var_0_0.LANG_TYPE_JP:
		return arg_28_0.GetJpAudition()

def var_0_0.GetAuditionVoice(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_0.GetAudition(arg_29_1)

	if arg_29_1 == var_0_0.LANG_TYPE_CH:
		return var_29_0 .. "-CN"
	elif arg_29_1 == var_0_0.LANG_TYPE_JP:
		return var_29_0 .. "-JP"

def var_0_0.GetAuditionTitle(arg_30_0):
	return arg_30_0.getConfig("audition_text")

def var_0_0.GetCnCpkName(arg_31_0):
	return arg_31_0.getConfig("story_resource_CN")

def var_0_0.GetJpCpkName(arg_32_0):
	return arg_32_0.getConfig("story_resource_JP")

def var_0_0.GetCpkName(arg_33_0, arg_33_1):
	if arg_33_1 == var_0_0.LANG_TYPE_CH:
		return arg_33_0.GetCnCpkName()
	elif arg_33_1 == var_0_0.LANG_TYPE_JP:
		return arg_33_0.GetJpCpkName()

def var_0_0.IsMultiVersion(arg_34_0):
	return not var_0_0.IsEmpty(arg_34_0.GetCnCpkName()) and not var_0_0.IsEmpty(arg_34_0.GetJpCpkName())

def var_0_0.OnlyChVersion(arg_35_0):
	return not var_0_0.IsEmpty(arg_35_0.GetCnCpkName()) and var_0_0.IsEmpty(arg_35_0.GetJpCpkName())

def var_0_0.OnlyJpVersion(arg_36_0):
	return not var_0_0.IsEmpty(arg_36_0.GetJpCpkName()) and var_0_0.IsEmpty(arg_36_0.GetCnCpkName())

def var_0_0.ExistLang(arg_37_0, arg_37_1):
	local var_37_0 = arg_37_0.GetCpkName(arg_37_1)

	return not var_0_0.IsEmpty(var_37_0)

def var_0_0.GetIcon(arg_38_0):
	return arg_38_0.getConfig("story_pic")

def var_0_0.GetCost(arg_39_0, arg_39_1):
	return arg_39_0.GetCostList()[arg_39_1]

def var_0_0.GetCostList(arg_40_0):
	local var_40_0 = arg_40_0.getConfig("cost" .. var_0_0.COST_TYPE_GEM)
	local var_40_1 = arg_40_0.getConfig("cost" .. var_0_0.COST_TYPE_TICKET)

	return {
		[var_0_0.COST_TYPE_GEM] = {
			type = var_40_0[1],
			id = var_40_0[2],
			count = var_40_0[3]
		},
		[var_0_0.COST_TYPE_TICKET] = {
			type = var_40_1[1],
			id = var_40_1[2],
			count = var_40_1[3]
		}
	}

def var_0_0.InTime(arg_41_0):
	local var_41_0 = arg_41_0.getConfig("time")

	return pg.TimeMgr.GetInstance().inTime(var_41_0)

def var_0_0.IsExpired(arg_42_0):
	return not arg_42_0.InTime()

def var_0_0.GetSortIndex(arg_43_0):
	return arg_43_0.getConfig("order")

def var_0_0.IsForever(arg_44_0):
	local var_44_0 = arg_44_0.getConfig("time")

	return type(var_44_0) == "string" and var_44_0 == "always"

def var_0_0.GetExpiredTimeStr(arg_45_0):
	if arg_45_0.InTime() and not arg_45_0.IsForever():
		local var_45_0 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_45_1 = arg_45_0.getConfig("time")[3]
		local var_45_2 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_45_1) - var_45_0

		return var_45_2 <= 0 and "" or skinTimeStamp(var_45_2)
	else
		return ""

local function var_0_1(arg_46_0)
	local var_46_0 = io.open(arg_46_0, "rb")

	if var_46_0:
		local var_46_1 = var_46_0.seek("end")

		var_46_0.close()

		return var_46_1
	else
		return None

def var_0_0.ExistLocalFile(arg_47_0, arg_47_1):
	local var_47_0 = arg_47_0.GetCpkName(arg_47_1)
	local var_47_1 = var_0_0.GetAssetBundlePath(var_47_0)

	return PathMgr.FileExists(var_47_1)

def var_0_0.ExistLocalSubtitleFile(arg_48_0, arg_48_1):
	local var_48_0 = arg_48_0.GetCpkName(arg_48_1)
	local var_48_1 = var_0_0.GetSubtitleAssetBundlePath(var_48_0)

	return PathMgr.FileExists(var_48_1)

def var_0_0.GetResSize(arg_49_0, arg_49_1):
	if not arg_49_0.IsDownloadRes(arg_49_1):
		return ""

	if not arg_49_0.sizes[arg_49_1] and arg_49_0.ExistLocalFile(arg_49_1):
		local var_49_0 = arg_49_0.GetCpkName(arg_49_1)
		local var_49_1 = var_0_0.GetAssetBundlePath(var_49_0)
		local var_49_2 = var_0_1(var_49_1)
		local var_49_3 = 0

		if arg_49_0.ExistLocalSubtitleFile(arg_49_1):
			local var_49_4 = var_0_0.GetSubtitleAssetBundlePath(var_49_0)

			var_49_3 = var_0_1(var_49_4)

		arg_49_0.sizes[arg_49_1] = HashUtil.BytesToString(var_49_2 + var_49_3)

	return arg_49_0.sizes[arg_49_1] or 0

return var_0_0
