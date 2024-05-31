local var_0_0 = {}

var_0_0.PaintingGroupName = "PAINTING"
var_0_0.PaintingMgr = None

def var_0_0.GetPaintingMgr():
	if not var_0_0.PaintingMgr:
		var_0_0.PaintingMgr = BundleWizard.Inst.GetGroupMgr(var_0_0.PaintingGroupName)

	return var_0_0.PaintingMgr

var_0_0.NotifyPaintingDownloadFinish = "PaintingGroupConst.NotifyPaintingDownloadFinish"

def var_0_0.VerifyPaintingFileName(arg_2_0):
	return GroupHelper.VerifyFile(var_0_0.PaintingGroupName, arg_2_0)

def var_0_0.CalcPaintingListSize(arg_3_0):
	local var_3_0 = GroupHelper.CreateArrByLuaFileList(var_0_0.PaintingGroupName, arg_3_0)
	local var_3_1 = GroupHelper.CalcSizeWithFileArr(var_0_0.PaintingGroupName, var_3_0)
	local var_3_2 = HashUtil.BytesToString(var_3_1)

	return var_3_1, var_3_2

def var_0_0.IsPaintingNeedCheck():
	if Application.isEditor:
		return False

	if GroupHelper.IsGroupVerLastest(var_0_0.PaintingGroupName):
		return False

	if not GroupHelper.IsGroupWaitToUpdate(var_0_0.PaintingGroupName):
		return False

	return True

def var_0_0.AddPaintingNameWithFilteMap(arg_5_0, arg_5_1):
	arg_5_1 = string.lower(arg_5_1)

	if not pg.painting_filte_map:
		warning("painting_filte_map not exist")

		return

	if not pg.painting_filte_map[arg_5_1]:
		warning("painting_filte_map not exist key. " .. arg_5_1)

		return

	local var_5_0 = pg.painting_filte_map[arg_5_1].res_list

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		if not table.contains(arg_5_0, iter_5_1) and var_0_0.VerifyPaintingFileName(iter_5_1):
			table.insert(arg_5_0, iter_5_1)

def var_0_0.AddPaintingNameByShipGroupID(arg_6_0, arg_6_1):
	if var_0_0.IsPaintingNeedCheck():
		local var_6_0 = ShipGroup.getDefaultSkin(arg_6_1).painting

		var_0_0.AddPaintingNameWithFilteMap(arg_6_0, var_6_0)

def var_0_0.AddPaintingNameByShipConfigID(arg_7_0, arg_7_1):
	if var_0_0.IsPaintingNeedCheck():
		local var_7_0 = {
			configId = arg_7_1
		}
		local var_7_1 = Ship.getGroupId(var_7_0)

		var_0_0.AddPaintingNameByShipGroupID(arg_7_0, var_7_1)

def var_0_0.AddPaintingNameBySkinID(arg_8_0, arg_8_1):
	if var_0_0.IsPaintingNeedCheck():
		local var_8_0 = pg.ship_skin_template[arg_8_1].painting

		if #var_8_0 > 0:
			var_0_0.AddPaintingNameWithFilteMap(arg_8_0, var_8_0)

def var_0_0.GetPaintingNameListInLogin():
	local var_9_0 = {}
	local var_9_1 = var_0_0.GetPaintingMgr()
	local var_9_2 = getProxy(ShipSkinProxy)

	if var_9_2:
		local var_9_3 = var_9_2.GetOwnAndShareSkins()

		for iter_9_0, iter_9_1 in pairs(var_9_3):
			var_0_0.AddPaintingNameBySkinID(var_9_0, iter_9_1.id)

	local var_9_4 = getProxy(CollectionProxy)

	if var_9_4:
		local var_9_5 = var_9_4.getGroups()

		for iter_9_2, iter_9_3 in pairs(var_9_5):
			var_0_0.AddPaintingNameByShipGroupID(var_9_0, iter_9_3.id)

	local var_9_6 = getProxy(BayProxy)

	if var_9_6:
		local var_9_7 = var_9_6.activityNpcShipIds

		for iter_9_4, iter_9_5 in ipairs(var_9_7):
			local var_9_8 = var_9_6.getShipById(iter_9_5)

			var_0_0.AddPaintingNameByShipGroupID(var_9_0, var_9_8.groupId)

	return var_9_0

def var_0_0.GetPaintingNameListForTec():
	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(pg.ship_data_blueprint.all):
		var_0_0.AddPaintingNameByShipGroupID(var_10_0, iter_10_1)

	return var_10_0

def var_0_0.GetPaintingNameListForAwardList(arg_11_0):
	local var_11_0 = {}

	for iter_11_0 = 1, #arg_11_0:
		local var_11_1 = arg_11_0[iter_11_0]
		local var_11_2 = var_11_1.type

		if var_11_2 == DROP_TYPE_SHIP:
			local var_11_3 = var_11_1.id

			var_0_0.AddPaintingNameByShipConfigID(var_11_0, var_11_3)
		elif var_11_2 == DROP_TYPE_NPC_SHIP:
			local var_11_4 = getProxy(BayProxy).getShipById(var_11_1.id)

			var_0_0.AddPaintingNameByShipConfigID(var_11_0, var_11_4.configId)
		elif var_11_2 == DROP_TYPE_SKIN:
			local var_11_5 = var_11_1.id

			var_0_0.AddPaintingNameBySkinID(var_11_0, var_11_5)

	return var_11_0

def var_0_0.GetPaintingNameListByShipVO(arg_12_0):
	local var_12_0 = {}
	local var_12_1 = getProxy(ShipSkinProxy)
	local var_12_2 = var_12_1.GetAllSkinForShip(arg_12_0)

	for iter_12_0, iter_12_1 in ipairs(var_12_2):
		var_0_0.AddPaintingNameBySkinID(var_12_0, iter_12_1.id)

	local var_12_3 = var_12_1.GetShareSkinsForShip(arg_12_0)

	for iter_12_2, iter_12_3 in ipairs(var_12_3):
		var_0_0.AddPaintingNameBySkinID(var_12_0, iter_12_3.id)

	return var_12_0

def var_0_0.PaintingDownload(arg_13_0):
	local var_13_0 = {}

	if var_0_0.IsPaintingNeedCheck():
		local var_13_1 = arg_13_0.isShowBox
		local var_13_2 = pg.FileDownloadMgr.GetInstance().IsNeedRemind()
		local var_13_3 = IsUsingWifi()
		local var_13_4 = var_13_1 and var_13_2
		local var_13_5 = arg_13_0.paintingNameList

		if #var_13_5 > 0:
			if not var_13_3 and var_13_4:
				local var_13_6, var_13_7 = var_0_0.CalcPaintingListSize(var_13_5)

				if var_13_6 > 0:
					table.insert(var_13_0, function(arg_14_0)
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							modal = True,
							locked = True,
							type = MSGBOX_TYPE_FILE_DOWNLOAD,
							content = string.format(i18n("file_down_msgbox", var_13_7)),
							onYes = arg_14_0,
							onNo = arg_13_0.onNo,
							onClose = arg_13_0.onClose
						}))

			table.insert(var_13_0, function(arg_15_0)
				local var_15_0 = {
					groupName = var_0_0.PaintingGroupName,
					fileNameList = var_13_5
				}
				local var_15_1 = {
					dataList = {
						var_15_0
					},
					onFinish = arg_15_0
				}

				pg.FileDownloadMgr.GetInstance().Main(var_15_1))
			table.insert(var_13_0, function(arg_16_0)
				pg.m02.sendNotification(var_0_0.NotifyPaintingDownloadFinish)
				arg_16_0())

	seriesAsync(var_13_0, arg_13_0.finishFunc)

return var_0_0
