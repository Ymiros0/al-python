﻿local var_0_0 = class("WSWorldInfo", import("...BaseEntity"))

var_0_0.Fields = {
	powerCount = "userdata",
	stepCount = "userdata",
	achievementTip = "userdata",
	transform = "userdata",
	btnAchievement = "userdata",
	achievementCount = "userdata",
	powerIconTF = "userdata",
	buffListTF = "userdata",
	pressingCount = "userdata"
}
var_0_0.Listeners = {
	onUpdate = "Update"
}

function var_0_0.Build(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)

	local var_1_0 = nowWorld()

	var_1_0:AddListener(World.EventUpdateGlobalBuff, arg_1_0.onUpdate)
	var_1_0:AddListener(World.EventAchieved, arg_1_0.onUpdate)
	var_1_0:GetAtlas():AddListener(WorldAtlas.EventAddPressingMap, arg_1_0.onUpdate)
end

function var_0_0.Dispose(arg_2_0)
	local var_2_0 = nowWorld()

	var_2_0:RemoveListener(World.EventUpdateGlobalBuff, arg_2_0.onUpdate)
	var_2_0:RemoveListener(World.EventAchieved, arg_2_0.onUpdate)
	var_2_0:GetAtlas():RemoveListener(WorldAtlas.EventAddPressingMap, arg_2_0.onUpdate)
	arg_2_0:Clear()
	pg.DelegateInfo.Dispose(arg_2_0)
end

function var_0_0.Setup(arg_3_0)
	arg_3_0:Init()
	arg_3_0:Update()
end

function var_0_0.Init(arg_4_0)
	arg_4_0.powerIconTF = arg_4_0.transform:Find("power/level")

	onToggle(arg_4_0, arg_4_0.powerIconTF, function(arg_5_0)
		if arg_5_0 and isActive(arg_4_0.powerIconTF:Find("effect")) then
			local var_5_0 = getProxy(PlayerProxy):getRawData()

			setActive(arg_4_0.powerIconTF:Find("effect"), false)
			PlayerPrefs.SetInt("world_rank_icon_click_" .. var_5_0.id, 1)
		end
	end)

	arg_4_0.powerCount = arg_4_0.transform:Find("power/bg/Number")
	arg_4_0.buffListTF = arg_4_0.transform:Find("buff")
	arg_4_0.stepCount = arg_4_0.transform:Find("explore/mileage/number")
	arg_4_0.pressingCount = arg_4_0.transform:Find("explore/pressing/number")
	arg_4_0.btnAchievement = arg_4_0.transform:Find("explore/achievement")

	onButton(arg_4_0, arg_4_0.btnAchievement, function()
		pg.m02:sendNotification(WorldMediator.OnNotificationOpenLayer, {
			context = Context.New({
				mediator = WorldCollectionMediator,
				viewComponent = WorldCollectionLayer,
				data = {
					page = WorldCollectionLayer.PAGE_ACHIEVEMENT,
					entranceId = nowWorld():GetActiveEntrance().id
				}
			})
		})
	end, SFX_PANEL)

	arg_4_0.achievementCount = arg_4_0.btnAchievement:Find("number")
	arg_4_0.achievementTip = arg_4_0.btnAchievement:Find("tip")
end

function var_0_0.Update(arg_7_0)
	local var_7_0 = nowWorld()
	local var_7_1 = var_7_0:GetWorldRank()

	LoadImageSpriteAtlasAsync("ui/share/world_info_atlas", "level_phase_" .. var_7_1, arg_7_0.powerIconTF)

	local var_7_2 = getProxy(PlayerProxy):getRawData()

	setActive(arg_7_0.powerIconTF:Find("effect"), not PlayerPrefs.HasKey("world_rank_icon_click_" .. var_7_2.id))
	setText(arg_7_0.powerIconTF:Find("info/Text"), i18n("world_map_level", var_7_1))
	setText(arg_7_0.powerCount, var_7_0:GetWorldPower())

	local var_7_3 = var_7_0:GetWorldMapBuffLevel()

	for iter_7_0 = 1, 3 do
		setText(arg_7_0.buffListTF:GetChild(iter_7_0 - 1):Find("Text"), var_7_3[iter_7_0] or 0)
	end

	setText(arg_7_0.stepCount, var_7_0.stepCount)
	setText(arg_7_0.pressingCount, var_7_0:GetDisplayPressingCount())

	local var_7_4, var_7_5, var_7_6 = var_7_0:CountAchievements()

	setText(arg_7_0.achievementCount, var_7_4 + var_7_5 .. "/" .. var_7_6)

	local var_7_7, var_7_8 = var_7_0:GetFinishAchievements(arg_7_0.achEntranceList)

	setActive(arg_7_0.achievementTip, #var_7_7 > 0)
end

return var_0_0
