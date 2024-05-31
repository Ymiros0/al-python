local var_0_0 = class("Apartment", import(".BaseVO"))

var_0_0.TRIGGER_TOUCH = 1001
var_0_0.TRIGGER_TALK = 1002
var_0_0.TRIGGER_OWNER = 1007
var_0_0.TRIGGER_PROPOSE = 1008

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.configId = arg_1_1.ship_group
	arg_1_0.level = arg_1_1.favor_lv
	arg_1_0.favor = arg_1_1.favor_exp
	arg_1_0.daily = arg_1_1.daily_favor
	arg_1_0.skinId = arg_1_1.cur_skin
	arg_1_0.skinList = {}

	table.insert(arg_1_0.skinList, arg_1_0:getConfig("skin_model"))

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.skins) do
		table.insert(arg_1_0.skinList, iter_1_1)
	end

	table.sort(arg_1_0.skinList)

	arg_1_0.triggerCountDic = setmetatable({}, {
		__index = function(arg_2_0, arg_2_1)
			return 0
		end
	})

	for iter_1_2, iter_1_3 in ipairs(arg_1_1.regular_trigger) do
		arg_1_0.triggerCountDic[iter_1_3] = arg_1_0.triggerCountDic[iter_1_3] + 1
	end

	arg_1_0.furnitures = {}

	table.Ipairs(arg_1_1.furnitures, function(arg_3_0, arg_3_1)
		arg_1_0.furnitures[arg_3_0] = Dorm3dFurniture.New({
			configId = arg_3_1.furniture_id,
			slotId = arg_3_1.slot_id
		})
	end)

	arg_1_0.slots = {}

	table.Ipairs(arg_1_0:GetSlotIDList(), function(arg_4_0, arg_4_1)
		local var_4_0 = Dorm3dFurnitureSlot.New({
			configId = arg_4_1
		})

		arg_1_0.slots[arg_4_0] = var_4_0
	end)

	arg_1_0.zones = {}

	table.Ipairs(arg_1_0:GetZoneIDList(), function(arg_5_0, arg_5_1)
		local var_5_0 = Dorm3dZone.New({
			configId = arg_5_1
		})

		arg_1_0.zones[arg_5_0] = var_5_0

		var_5_0:SetSlots(_.map(var_5_0:GetSlotIDList(), function(arg_6_0)
			return _.detect(arg_1_0.slots, function(arg_7_0)
				return arg_7_0:GetConfigID() == arg_6_0
			end)
		end))
	end)

	arg_1_0.globalZones = {}
	arg_1_0.normalZones = {}

	_.each(arg_1_0.zones, function(arg_8_0)
		table.insert(arg_8_0:IsGlobal() and arg_1_0.globalZones or arg_1_0.normalZones, arg_8_0)
	end)

	arg_1_0.cameraZones = _.map(arg_1_0:GetCameraZoneIDList(), function(arg_9_0)
		return Dorm3dCameraZone.New({
			configId = arg_9_0
		})
	end)
	arg_1_0.talkDic = {}

	for iter_1_4, iter_1_5 in ipairs(arg_1_1.dialogues) do
		arg_1_0.talkDic[iter_1_5] = true
	end

	arg_1_0.collectItemDic = {}

	for iter_1_6, iter_1_7 in ipairs(arg_1_1.collections) do
		arg_1_0.collectItemDic[iter_1_7] = true
	end

	arg_1_0.zoneDic = {}

	for iter_1_8, iter_1_9 in ipairs(pg.dorm3d_zone_template.get_id_list_by_char_id[arg_1_0.configId]) do
		local var_1_0 = Dorm3dZone.New({
			configId = iter_1_9
		})
		local var_1_1 = var_1_0:GetWatchCameraName()

		if var_1_1 and var_1_1 ~= "" then
			arg_1_0.zoneDic[var_1_1] = var_1_0
		end
	end
end

function var_0_0.bindConfigTable(arg_10_0)
	return pg.dorm3d_dorm_template
end

function var_0_0.getFavorConfig(arg_11_0, arg_11_1, arg_11_2)
	arg_11_2 = arg_11_2 or arg_11_0.level

	local var_11_0 = pg.dorm3d_favor.get_id_list_by_char_id[arg_11_0.configId]

	return pg.dorm3d_favor[var_11_0[arg_11_2]][arg_11_1]
end

function var_0_0.addFavor(arg_12_0, arg_12_1)
	local var_12_0 = pg.dorm3d_favor_trigger[arg_12_1]
	local var_12_1 = var_12_0.num

	if var_12_0.is_repeat > 0 then
		local var_12_2 = getDorm3dGameset("daily_exp_max")[1]

		var_12_1 = math.min(var_12_1, var_12_2 - arg_12_0.daily)
		arg_12_0.daily = arg_12_0.daily + var_12_1
	end

	arg_12_0.favor = arg_12_0.favor + var_12_1
	arg_12_0.triggerCountDic[arg_12_1] = arg_12_0.triggerCountDic[arg_12_1] + 1

	return var_12_1
end

function var_0_0.getDailyFavor(arg_13_0)
	return arg_13_0.daily, getDorm3dGameset("daily_exp_max")[1]
end

function var_0_0.addLevel(arg_14_0)
	arg_14_0.favor = arg_14_0.favor - arg_14_0:getNextExp()
	arg_14_0.level = arg_14_0.level + 1
end

function var_0_0.addSkin(arg_15_0, arg_15_1)
	table.insert(arg_15_0.skinList, arg_15_1)
	table.sort(arg_15_0.skinList)
end

function var_0_0.getSkinId(arg_16_0)
	if arg_16_0.skinId == 0 then
		return arg_16_0:getConfig("skin_model")
	else
		return arg_16_0.skinId
	end
end

function var_0_0.getStageRank(arg_17_0)
	if not var_0_0.stageDic then
		var_0_0.stageDic = {}

		for iter_17_0, iter_17_1 in ipairs(getDorm3dGameset("stage_level")[2]) do
			for iter_17_2, iter_17_3 in ipairs(iter_17_1) do
				var_0_0.stageDic[iter_17_3] = iter_17_0
			end
		end
	end

	return var_0_0.stageDic[arg_17_0.level]
end

function var_0_0.getStageText(arg_18_0)
	return getDorm3dGameset("stage_name")[2][arg_18_0:getStageRank()][1]
end

function var_0_0.getNextExp(arg_19_0)
	if arg_19_0.level < getDorm3dGameset("favor_level")[1] then
		return arg_19_0:getFavorConfig("favor_exp", arg_19_0.level + 1)
	else
		return 0
	end
end

function var_0_0.GetScene(arg_20_0)
	return arg_20_0:getConfig("scene")
end

function var_0_0.GetBaseScene(arg_21_0)
	return arg_21_0:getConfig("scene_base")
end

function var_0_0.GetSceneRootName(arg_22_0)
	return arg_22_0:getConfig("scene_parent")
end

function var_0_0.GetAssetName(arg_23_0)
	return arg_23_0:getConfig("asset_name")
end

function var_0_0.GetBaseModelName(arg_24_0)
	return arg_24_0:getConfig("base_model")
end

function var_0_0.GetSceneData(arg_25_0, arg_25_1)
	return {
		sceneName = arg_25_0:getConfig("scene")[arg_25_1],
		baseSceneName = arg_25_0:getConfig("scene_base")[arg_25_1],
		modelName = arg_25_0:GetSkinModelName()
	}
end

function var_0_0.GetSkinModelName(arg_26_0)
	local var_26_0 = arg_26_0.skinId

	if var_26_0 == 0 then
		var_26_0 = arg_26_0:getConfig("skin_model")
	end

	assert(underscore.any(pg.dorm3d_resource.get_id_list_by_ship_group[arg_26_0.configId], function(arg_27_0)
		return var_26_0 == arg_27_0
	end))

	return pg.dorm3d_resource[var_26_0].model_id
end

function var_0_0.GetZoneIDList(arg_28_0)
	return pg.dorm3d_zone_template.get_id_list_by_char_id[arg_28_0.configId]
end

function var_0_0.GetSlotIDList(arg_29_0)
	return pg.dorm3d_furniture_slot_template.get_id_list_by_char_id[arg_29_0.configId]
end

function var_0_0.GetCameraZoneIDList(arg_30_0)
	return pg.dorm3d_camera_zone_template.get_id_list_by_char_id[arg_30_0.configId]
end

function var_0_0.GetZones(arg_31_0)
	return arg_31_0.zones
end

function var_0_0.GetGlobalZones(arg_32_0)
	return arg_32_0.globalZones
end

function var_0_0.GetNormalZones(arg_33_0)
	return arg_33_0.normalZones
end

function var_0_0.GetCameraZones(arg_34_0)
	return arg_34_0.cameraZones
end

function var_0_0.GetSlots(arg_35_0)
	return arg_35_0.slots
end

function var_0_0.GetFurnitures(arg_36_0)
	return arg_36_0.furnitures
end

function var_0_0.ReplaceFurnitures(arg_37_0, arg_37_1)
	_.each(arg_37_1, function(arg_38_0)
		arg_37_0:ReplaceFurniture(arg_38_0.slotId, arg_38_0.furnitureId)
	end)
end

function var_0_0.ReplaceFurniture(arg_39_0, arg_39_1, arg_39_2)
	local var_39_0 = _.detect(arg_39_0.furnitures, function(arg_40_0)
		return arg_40_0:GetSlotID() == arg_39_1
	end)

	if var_39_0 then
		var_39_0:SetSlotID(0)
	end

	local var_39_1 = _.detect(arg_39_0.furnitures, function(arg_41_0)
		return arg_41_0:GetConfigID() == arg_39_2 and arg_41_0:GetSlotID() == 0
	end)

	if var_39_1 then
		var_39_1:SetSlotID(arg_39_1)
	end
end

function var_0_0.getTalkingList(arg_42_0)
	return pg.dorm3d_dialogue_group.get_id_list_by_char_id[arg_42_0.configId]
end

var_0_0.ENTER_TALK_TYPE = {
	[103] = true,
	[102] = true,
	[104] = true,
	[101] = true,
	[105] = true
}

function var_0_0.getEnterTalking(arg_43_0)
	return underscore.filter(arg_43_0:getTalkingList(), function(arg_44_0)
		local var_44_0 = pg.dorm3d_dialogue_group[arg_44_0]

		return var_0_0.ENTER_TALK_TYPE[var_44_0.type] and arg_43_0:checkUnlockConfig(var_44_0.unlock)
	end)
end

function var_0_0.getFurnitureTalking(arg_45_0, arg_45_1)
	return underscore.filter(arg_45_0:getTalkingList(), function(arg_46_0)
		local var_46_0 = pg.dorm3d_dialogue_group[arg_46_0]

		return var_46_0.type == 200 and var_46_0.trigger_config == arg_45_1 and arg_45_0:checkUnlockConfig(var_46_0.unlock)
	end)
end

function var_0_0.getTouchConfig(arg_47_0, arg_47_1)
	local var_47_0
	local var_47_1 = {}

	for iter_47_0, iter_47_1 in ipairs(pg.dorm3d_touch_data.get_id_list_by_char_id[arg_47_0.configId]) do
		if arg_47_1 == pg.dorm3d_touch_data[iter_47_1].trigger_area then
			var_47_0 = pg.dorm3d_touch_data[iter_47_1]

			break
		end
	end

	local var_47_2 = arg_47_0:getStageRank()

	if not var_47_0 then
		return
	end

	for iter_47_2, iter_47_3 in ipairs(var_47_0.stage_unlock) do
		if var_47_2 < iter_47_2 then
			break
		else
			var_47_1 = table.mergeArray(var_47_1, iter_47_3)
		end
	end

	local var_47_3 = {
		[0] = envFunc(function()
			up, donw, left, right, zoom_in, zoom_out = unpack(var_47_0.camera_trigger[var_47_2])
		end, {})
	}

	for iter_47_4, iter_47_5 in ipairs(var_47_1) do
		local var_47_4 = pg.dorm3d_touch_trigger[iter_47_5]

		var_47_3[var_47_4.touch_type] = var_47_3[var_47_4.touch_type] or {}
		var_47_3[var_47_4.touch_type][var_47_4.body_area] = iter_47_5
	end

	return var_47_0, var_47_3
end

function var_0_0.getGiftIds(arg_49_0)
	local var_49_0 = pg.dorm3d_gift.get_id_list_by_ship_group_id

	return table.mergeArray(var_49_0[0], var_49_0[arg_49_0.configId])
end

function var_0_0.getCollectConfig(arg_50_0, arg_50_1)
	local var_50_0 = pg.dorm3D_collect[arg_50_0.configId]

	return var_50_0 and var_50_0[arg_50_1] or nil
end

function var_0_0.getTriggerableCollectItems(arg_51_0)
	local var_51_0 = {}

	for iter_51_0, iter_51_1 in ipairs(arg_51_0:getCollectConfig("collection_template_list")) do
		local var_51_1 = pg.dorm3d_collection_template[iter_51_1]

		if not arg_51_0.collectItemDic[iter_51_1] and arg_51_0:checkUnlockConfig(var_51_1.unlock) then
			table.insert(var_51_0, iter_51_1)
		end
	end

	return var_51_0
end

function var_0_0.checkUnlockConfig(arg_52_0, arg_52_1)
	local var_52_0, var_52_1 = unpack(arg_52_1)

	return switch(var_52_0, {
		function()
			if arg_52_0.level >= var_52_1 then
				return true
			else
				return false, string.format("apartment level unenough:%d", var_52_1)
			end
		end,
		function()
			if underscore.any(arg_52_0.furnitures, function(arg_55_0)
				return arg_55_0.configId == var_52_1
			end) then
				return true
			else
				return false, string.format("without dorm furniture:%d", var_52_1)
			end
		end,
		function()
			if getProxy(ApartmentProxy):isGiveGiftDone(var_52_1) then
				return true
			else
				return false, string.format("gift:%d didn't had given", var_52_1)
			end
		end
	}, function()
		return false, string.format("without unlock type:%d", var_52_0)
	end)
end

function var_0_0.getZone(arg_58_0, arg_58_1)
	return arg_58_0.zoneDic[arg_58_1]
end

function var_0_0.getZoneNames(arg_59_0)
	return underscore.keys(arg_59_0.zoneDic)
end

return var_0_0
