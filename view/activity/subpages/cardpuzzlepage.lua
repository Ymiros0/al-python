﻿local var_0_0 = class("CardPuzzlePage", import("view.base.BaseActivityPage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.titleTF = arg_1_0:findTF("title", arg_1_0.bg)
	arg_1_0.progressTF = arg_1_0:findTF("progress", arg_1_0.bg)
	arg_1_0.descTF = arg_1_0:findTF("desc", arg_1_0.bg)
	arg_1_0.startBtn = arg_1_0:findTF("start_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0:findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0:findTF("got_btn", arg_1_0.bg)
	arg_1_0.item = arg_1_0:findTF("levels/tpl", arg_1_0.bg)
	arg_1_0.items = arg_1_0:findTF("levels", arg_1_0.bg)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0.item)
end

function var_0_0.OnDataSetting(arg_2_0)
	arg_2_0.levelList = arg_2_0.activity:getConfig("config_data")[1]
	arg_2_0.awardList = arg_2_0.activity:getConfig("config_data")[2]
end

function var_0_0.OnFirstFlush(arg_3_0)
	arg_3_0.uilist:make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventInit then
			arg_3_0:InitItem(arg_4_1, arg_4_2)
		elseif arg_4_0 == UIItemList.EventUpdate then
			arg_3_0:UpdateItem(arg_4_1, arg_4_2)
		end
	end)
	onButton(arg_3_0, arg_3_0.startBtn, function()
		if not arg_3_0.selectedId then
			return
		end

		arg_3_0:emit(ActivityMediator.GO_CARDPUZZLE_COMBAT, arg_3_0.selectedId)
	end, SFX_PANEL)

	arg_3_0.selectedId = arg_3_0:GetCurLevel()

	arg_3_0:UpdateLevelInfo()
end

function var_0_0.InitItem(arg_6_0, arg_6_1, arg_6_2)
	GetImageSpriteFromAtlasAsync("ui/activityuipage/cardpuzzlepage_atlas", arg_6_1 + 1, arg_6_0:findTF("normal/num", arg_6_2), true)
	GetImageSpriteFromAtlasAsync("ui/activityuipage/cardpuzzlepage_atlas", arg_6_1 + 1, arg_6_0:findTF("selected/num", arg_6_2), true)
end

function var_0_0.UpdateItem(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = arg_7_1 + 1
	local var_7_1 = arg_7_0.levelList[var_7_0]

	setActive(arg_7_0:findTF("selected", arg_7_2), arg_7_0.selectedId == var_7_1)

	local var_7_2 = table.contains(arg_7_0.finishList, var_7_1)

	setActive(arg_7_0:findTF("finish", arg_7_2), var_7_2)
	setActive(arg_7_0:findTF("normal", arg_7_2), not var_7_2 and arg_7_0.selectedId ~= var_7_1)
	onButton(arg_7_0, arg_7_2, function()
		arg_7_0.selectedId = var_7_1

		arg_7_0.uilist:align(#arg_7_0.levelList)
		arg_7_0:UpdateLevelInfo()
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_9_0)
	arg_9_0.gotList = arg_9_0.activity:getData1List()
	arg_9_0.finishList = arg_9_0.activity.data2_list

	arg_9_0.uilist:align(#arg_9_0.levelList)

	if arg_9_0:CheckAward() then
		setActive(arg_9_0.getBtn, true)
		onButton(arg_9_0, arg_9_0.getBtn, function()
			arg_9_0:emit(ActivityMediator.EVENT_OPERATION, {
				cmd = 2,
				activity_id = arg_9_0.activity.id,
				arg1 = arg_9_0:CheckAward()
			})
		end, SFX_PANEL)
	else
		setActive(arg_9_0.getBtn, false)
	end

	setActive(arg_9_0.gotBtn, #arg_9_0.gotList == #arg_9_0.awardList)
	setText(arg_9_0.progressTF, setColorStr(#arg_9_0.finishList, "#C2FFF3") .. "/" .. #arg_9_0.levelList)
	arg_9_0:UpdateEveryDayTip()
end

function var_0_0.CheckAward(arg_11_0)
	if #arg_11_0.gotList == #arg_11_0.awardList then
		return nil
	end

	local var_11_0 = #arg_11_0.finishList

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.awardList) do
		if not table.contains(arg_11_0.gotList, iter_11_1[1]) and var_11_0 >= iter_11_1[1] then
			return iter_11_1[1]
		end
	end

	return nil
end

function var_0_0.UpdateLevelInfo(arg_12_0)
	local var_12_0 = pg.puzzle_combat_template[arg_12_0.selectedId]

	setText(arg_12_0.titleTF, "·" .. var_12_0.name)
	setText(arg_12_0.descTF, var_12_0.description)
end

function var_0_0.GetCurLevel(arg_13_0)
	arg_13_0.finishList = arg_13_0.activity.data2_list

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.levelList) do
		if not table.contains(arg_13_0.finishList, iter_13_1) then
			return iter_13_1, iter_13_0
		end
	end

	return arg_13_0.levelList[#arg_13_0.levelList], #arg_13_0.levelList
end

function var_0_0.UpdateEveryDayTip(arg_14_0)
	if #arg_14_0.gotList == #arg_14_0.awardList then
		return
	end

	if arg_14_0:CheckAward() then
		return
	end

	local var_14_0, var_14_1 = arg_14_0:GetCurLevel()
	local var_14_2 = arg_14_0:findTF("tip", arg_14_0.items:GetChild(var_14_1 - 1))
	local var_14_3 = getProxy(PlayerProxy):getData().id
	local var_14_4 = "DAY_TIP_" .. arg_14_0.activity.id .. "_" .. var_14_3 .. "_" .. arg_14_0.activity:getDayIndex()

	if PlayerPrefs.GetInt(var_14_4) == 0 then
		setActive(var_14_2, true)
		PlayerPrefs.SetInt(var_14_4, 1)
	else
		setActive(var_14_2, false)
	end
end

return var_0_0
