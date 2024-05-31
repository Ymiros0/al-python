﻿local var_0_0 = singletonClass("WorldGuider", import("....Mod.Experiment.BaseEntity"))

var_0_0.Fields = {
	tempGridPos = "table",
	tStamina = "number"
}

function var_0_0.Init(arg_1_0)
	arg_1_0.tempGridPos = {}
end

function var_0_0.SetTempGridPos(arg_2_0, arg_2_1, arg_2_2)
	arg_2_2 = arg_2_2 or 1

	local var_2_0 = pg.NewGuideMgr.GetInstance()._tf:InverseTransformPoint(arg_2_1)

	arg_2_0.tempGridPos[arg_2_2] = var_2_0
end

function var_0_0.SetTempGridPos2(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = GameObject.Find("LevelCamera"):GetComponent(typeof(Camera)):WorldToScreenPoint(arg_3_1)
	local var_3_1 = GameObject.Find("OverlayCamera"):GetComponent(typeof(Camera)):ScreenToWorldPoint(var_3_0)

	arg_3_0:SetTempGridPos(var_3_1, arg_3_2)
end

function var_0_0.GetTempGridPos(arg_4_0, arg_4_1)
	arg_4_1 = arg_4_1 or 1

	return arg_4_0.tempGridPos[arg_4_1]
end

function var_0_0.CheckPlayChooseCamp(arg_5_0)
	local var_5_0 = nowWorld():GetRealm()

	if var_5_0 == nil or var_5_0 < 1 then
		arg_5_0:PlayGuide("WorldG001")
	end
end

function var_0_0.CheckIntruduce(arg_6_0)
	local var_6_0 = nowWorld():GetRealm()

	if var_6_0 and var_6_0 > 0 then
		if var_6_0 == 1 then
			arg_6_0:PlayGuide("WorldG002_1")
		elseif var_6_0 == 2 then
			arg_6_0:PlayGuide("WorldG002_2")
		end
	end
end

function var_0_0.CheckUseStaminaItem(arg_7_0)
	local var_7_0 = {
		251,
		252,
		253
	}
	local var_7_1 = nowWorld():GetInventoryProxy()
	local var_7_2 = 0

	for iter_7_0, iter_7_1 in ipairs(var_7_0) do
		var_7_2 = var_7_2 + var_7_1:GetItemCount(iter_7_1)
	end

	if var_7_2 > 0 then
		arg_7_0:PlayGuide("WorldG020")
	end
end

function var_0_0.CheckMapLimit(arg_8_0)
	pg.NewGuideMgr.GetInstance():Play("WorldG012")
end

function var_0_0.SpecialCheck(arg_9_0, arg_9_1)
	if arg_9_1 == "WorldG008" then
		local var_9_0 = nowWorld():GetActiveMap()

		if var_9_0 ~= nil and var_9_0.findex == 2 then
			return "WorldG008_2"
		end
	end

	return arg_9_1
end

var_0_0.interruptReplayList = {
	"WorldG007",
	"WorldG021",
	"WorldG100",
	"WorldG121",
	"WorldG141",
	"WorldG151"
}

function var_0_0.PlayGuide(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = pg.NewGuideMgr.GetInstance()

	if not GUIDE_WROLD or not arg_10_2 and pg.NewStoryMgr.GetInstance():IsPlayed(arg_10_1) or not var_10_0:CanPlay() then
		existCall(arg_10_3)

		return false
	end

	if not _.any(var_0_0.interruptReplayList, function(arg_11_0)
		return arg_10_1 == arg_11_0
	end) then
		pg.m02:sendNotification(GAME.STORY_UPDATE, {
			storyId = arg_10_1
		})
	end

	var_10_0:Play(arg_10_1, nil, function()
		return existCall(arg_10_3)
	end)

	return true
end

var_0_0.WORLD_HIDE_UI = "world hide ui"
var_0_0.WORLD_OPEN_MAP_OVERVIEW = "world open map overview"
var_0_0.WORLD_SHOW_MARGIN = "world show margin"
var_0_0.WORLD_SCANNER_DISPLAY = "world scanner display"
var_0_0.WORLD_GET_COMPASS_POS = "world get compass pos"
var_0_0.WORLD_GET_COMPASS_MAP_POS = "world get compass map pos"
var_0_0.WORLD_GET_SLG_TILE_POS = "world get slg tile pos"
var_0_0.WORLD_GET_SCANNER_POS = "world get scanner pos"
var_0_0.WORLD_OPEN_TRANSPORT_POS = "world open transport pos"
var_0_0.WORLD_SELECT_MODEL_MAP = "world select model map"
var_0_0.WORLD_FOCUS_EDGE = "world focus edge"
var_0_0.WORLD_FOCUS_EVENT = "world focus event"
var_0_0.WORLD_SCANNER_EVENT = "world scanner event"
var_0_0.WORLD_HELP_EVENT = "world help event"
var_0_0.WORLD_RECALL = "world recall"

local var_0_1 = {
	[var_0_0.WORLD_HIDE_UI] = function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_1.type == 1 then
			arg_13_2:HideMapRightCompass()
		elseif arg_13_1.type == 2 then
			arg_13_2:HideMapRightMemo()
		elseif arg_13_1.type == 3 then
			-- block empty
		elseif arg_13_1.type == 4 then
			arg_13_2:HideOverall()
		end
	end,
	[var_0_0.WORLD_GET_COMPASS_POS] = function(arg_14_0, arg_14_1, arg_14_2)
		arg_14_2:GetCompassGridPos(arg_14_1.row, arg_14_1.column, arg_14_1.cachedIndex)
	end,
	[var_0_0.WORLD_GET_COMPASS_MAP_POS] = function(arg_15_0, arg_15_1, arg_15_2)
		arg_15_2:GetEntranceTrackMark(arg_15_1.mapId, arg_15_1.cachedIndex)
	end,
	[var_0_0.WORLD_GET_SLG_TILE_POS] = function(arg_16_0, arg_16_1, arg_16_2)
		arg_16_2:GetSlgTilePos(arg_16_1.row, arg_16_1.column, arg_16_1.cachedIndex)
	end,
	[var_0_0.WORLD_GET_SCANNER_POS] = function(arg_17_0, arg_17_1, arg_17_2)
		arg_17_2:GetScannerPos(arg_17_1 and arg_17_1.cachedIndex or 1)
	end,
	[var_0_0.WORLD_OPEN_MAP_OVERVIEW] = function(arg_18_0, arg_18_1, arg_18_2)
		arg_18_2:Op("OpShowMarkOverview", {
			ids = arg_18_1.mapIds
		})
	end,
	[var_0_0.WORLD_SHOW_MARGIN] = function(arg_19_0, arg_19_1, arg_19_2)
		arg_19_2:ShowMargin(arg_19_1.tdType)
	end,
	[var_0_0.WORLD_SCANNER_DISPLAY] = function(arg_20_0, arg_20_1, arg_20_2)
		if arg_20_1.open == 1 then
			arg_20_2:OnLongPressMap(arg_20_1.row, arg_20_1.column)
		else
			arg_20_2:HideScannerPanel()
		end
	end,
	[var_0_0.WORLD_OPEN_TRANSPORT_POS] = function(arg_21_0, arg_21_1, arg_21_2)
		arg_21_2:EnterTransportWorld()
	end,
	[var_0_0.WORLD_SELECT_MODEL_MAP] = function(arg_22_0, arg_22_1, arg_22_2)
		arg_22_2:GuideSelectModelMap(arg_22_1.mapId)
	end,
	[var_0_0.WORLD_FOCUS_EDGE] = function(arg_23_0, arg_23_1, arg_23_2)
		arg_23_2:Op("OpMoveCameraTarget", arg_23_1.line, arg_23_1.stayTime)
	end,
	[var_0_0.WORLD_FOCUS_EVENT] = function(arg_24_0, arg_24_1, arg_24_2)
		arg_24_2:Op("OpMoveCamera", arg_24_1.eventId, arg_24_1.stayTime)
	end,
	[var_0_0.WORLD_SCANNER_EVENT] = function(arg_25_0, arg_25_1, arg_25_2)
		arg_25_2:GuideShowScannerEvent(arg_25_1.eventId)
	end,
	[var_0_0.WORLD_HELP_EVENT] = function(arg_26_0, arg_26_1, arg_26_2)
		arg_26_2:emit(WorldMediator.OnOpenLayer, Context.New({
			mediator = WorldHelpMediator,
			viewComponent = WorldHelpLayer,
			data = {
				titleId = arg_26_1.titleId,
				pageId = arg_26_1.pageId
			}
		}))
	end,
	[var_0_0.WORLD_RECALL] = function(arg_27_0, arg_27_1, arg_27_2)
		arg_27_2:Op("OpInteractive")
	end
}

function var_0_0.GetWorldGuiderNotifies(arg_28_0)
	return underscore.keys(var_0_1)
end

function var_0_0.WorldGuiderNotifyHandler(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	switch(arg_29_1, var_0_1, nil, arg_29_1, arg_29_2, arg_29_3)
end

return var_0_0
