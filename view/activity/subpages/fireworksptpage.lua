﻿local var_0_0 = class("FireworksPtPage", import(".TemplatePage.PtTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.fireworkNameText = arg_1_0:findTF("firework_text", arg_1_0.bg)
	arg_1_0.fireworkNumText = arg_1_0:findTF("firework_text/num_text", arg_1_0.bg)
	arg_1_0.ptText = arg_1_0:findTF("pt_text", arg_1_0.bg)
	arg_1_0.fireBtn = arg_1_0:findTF("fire_btn", arg_1_0.bg)
	arg_1_0.fireworkPanel = arg_1_0:findTF("frame", arg_1_0.bg)
	arg_1_0.dots = {
		arg_1_0:findTF("dots/1", arg_1_0.fireworkPanel),
		arg_1_0:findTF("dots/2", arg_1_0.fireworkPanel),
		arg_1_0:findTF("dots/3", arg_1_0.fireworkPanel)
	}
	arg_1_0.fireworkPages = {
		arg_1_0:findTF("content/1", arg_1_0.fireworkPanel),
		arg_1_0:findTF("content/2", arg_1_0.fireworkPanel),
		arg_1_0:findTF("content/3", arg_1_0.fireworkPanel)
	}
	arg_1_0.nextPageBtn = arg_1_0:findTF("right_btn", arg_1_0.fireworkPanel)
	arg_1_0.lastPageBtn = arg_1_0:findTF("left_btn", arg_1_0.fireworkPanel)
end

function var_0_0.OnDataSetting(arg_2_0)
	var_0_0.super.OnDataSetting(arg_2_0)

	arg_2_0.fireworkActID = arg_2_0.activity:getConfig("config_client").fireworkActID

	local var_2_0 = pg.activity_template[arg_2_0.fireworkActID].config_data

	arg_2_0.ptID = var_2_0[2][1]
	arg_2_0.ptConsume = var_2_0[2][2]
	arg_2_0.fireworkIds = var_2_0[3]
end

function var_0_0.OnFirstFlush(arg_3_0)
	var_0_0.super.OnFirstFlush(arg_3_0)
	onButton(arg_3_0, arg_3_0.fireBtn, function()
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SPRING_FESTIVAL_BACKHILL_2023, {
			openFireworkLayer = true
		})
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.nextPageBtn, function()
		arg_3_0:UpdateFrieworkPanel(arg_3_0.pageIndex + 1)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.lastPageBtn, function()
		arg_3_0:UpdateFrieworkPanel(arg_3_0.pageIndex - 1)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0:emit(ActivityMediator.SPECIAL_BATTLE_OPERA)
	end, SFX_PANEL)
	setText(arg_3_0.fireworkNameText, i18n("activity_yanhua_tip1"))
	arg_3_0:UpdataPageIndex()
end

function var_0_0.UpdataPageIndex(arg_8_0)
	arg_8_0.fireworkAct = getProxy(ActivityProxy):getActivityById(arg_8_0.fireworkActID)

	assert(arg_8_0.fireworkAct and not arg_8_0.fireworkAct:isEnd(), "烟花活动(type92)已结束")

	arg_8_0.unlockCount = arg_8_0.fireworkAct:getData1()
	arg_8_0.unlockIds = arg_8_0.fireworkAct:getData1List()

	for iter_8_0 = #arg_8_0.fireworkPages, 1, -1 do
		local var_8_0 = 0

		eachChild(arg_8_0.fireworkPages[iter_8_0], function(arg_9_0)
			local var_9_0 = tonumber(arg_9_0.name)

			if table.contains(arg_8_0.unlockIds, var_9_0) then
				var_8_0 = var_8_0 + 1
			end
		end)

		if var_8_0 ~= arg_8_0.fireworkPages[iter_8_0].childCount then
			arg_8_0.pageIndex = iter_8_0
		end
	end

	if #arg_8_0.unlockIds == #arg_8_0.fireworkIds then
		arg_8_0.pageIndex = 1
	end
end

function var_0_0.OnUpdateFlush(arg_10_0)
	var_0_0.super.OnUpdateFlush(arg_10_0)
	arg_10_0:UpdateFrieworkPanel(arg_10_0.pageIndex)

	if #arg_10_0.unlockIds == 0 then
		local var_10_0 = pg.activity_template[arg_10_0.fireworkActID].config_client.story

		if var_10_0 and type(var_10_0) == "table" then
			for iter_10_0, iter_10_1 in ipairs(var_10_0) do
				if iter_10_1[1] == 0 then
					pg.NewStoryMgr.GetInstance():Play(iter_10_1[2])
				end
			end
		end
	end
end

function var_0_0.UpdateFrieworkPanel(arg_11_0, arg_11_1)
	arg_11_0.fireworkAct = getProxy(ActivityProxy):getActivityById(arg_11_0.fireworkActID)

	assert(arg_11_0.fireworkAct and not arg_11_0.fireworkAct:isEnd(), "烟花活动(type92)已结束")

	arg_11_0.unlockCount = arg_11_0.fireworkAct:getData1()
	arg_11_0.unlockIds = arg_11_0.fireworkAct:getData1List()

	for iter_11_0 = #arg_11_0.fireworkPages, 1, -1 do
		eachChild(arg_11_0.fireworkPages[iter_11_0], function(arg_12_0)
			local var_12_0 = tonumber(arg_12_0.name)

			if table.contains(arg_11_0.unlockIds, var_12_0) then
				setActive(arg_12_0, false)
			else
				setActive(arg_12_0, true)
				onButton(arg_11_0, arg_12_0, function()
					arg_11_0:OnUnlockClick(var_12_0)
				end, SFX_PANEL)
			end
		end)
	end

	local var_11_0 = #arg_11_0.fireworkPages

	if var_11_0 < arg_11_1 or arg_11_1 < 1 then
		return
	end

	arg_11_0.pageIndex = arg_11_1

	for iter_11_1, iter_11_2 in ipairs(arg_11_0.fireworkPages) do
		setActive(iter_11_2, tonumber(iter_11_2.name) == arg_11_1)
	end

	for iter_11_3, iter_11_4 in ipairs(arg_11_0.dots) do
		setActive(iter_11_4, tonumber(iter_11_4.name) == arg_11_1)
	end

	setButtonEnabled(arg_11_0.nextPageBtn, arg_11_1 ~= var_11_0)
	setButtonEnabled(arg_11_0.lastPageBtn, arg_11_1 ~= 1)
	setText(arg_11_0.fireworkNumText, #arg_11_0.unlockIds .. "/" .. #arg_11_0.fireworkIds)

	arg_11_0.ptNum = getProxy(PlayerProxy):getRawData():getResource(arg_11_0.ptID)

	setText(arg_11_0.ptText, arg_11_0.ptNum)
end

function var_0_0.OnUnlockClick(arg_14_0, arg_14_1)
	if arg_14_0.unlockCount <= 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("activity_yanhua_tip6"))

		return
	end

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n("activity_yanhua_tip4", arg_14_0.ptConsume),
		onYes = function()
			if arg_14_0.ptNum < arg_14_0.ptConsume then
				pg.TipsMgr.GetInstance():ShowTips(i18n("activity_yanhua_tip5"))
			else
				arg_14_0:emit(ActivityMediator.EVENT_OPERATION, {
					cmd = 1,
					activity_id = arg_14_0.fireworkActID,
					arg1 = arg_14_1
				})
			end
		end
	})
end

return var_0_0
