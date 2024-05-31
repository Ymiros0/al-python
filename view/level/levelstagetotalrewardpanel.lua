﻿local var_0_0 = class("LevelStageTotalRewardPanel", import("view.level.BaseTotalRewardPanel"))

function var_0_0.getUIName(arg_1_0)
	return "LevelStageTotalRewardPanel"
end

local var_0_1 = 0.15

function var_0_0.init(arg_2_0)
	var_0_0.super.init(arg_2_0)

	arg_2_0.itemList = arg_2_0.boxView:Find("Content/ItemGrid")

	local var_2_0 = Instantiate(arg_2_0.itemList:GetComponent(typeof(ItemList)).prefabItem[0])

	var_2_0.name = "Icon"

	setParent(var_2_0, arg_2_0.itemList:Find("GridItem/Shell"))

	arg_2_0.itemListSub = arg_2_0.boxView:Find("Content/ItemGridSub")

	cloneTplTo(var_2_0, arg_2_0.itemListSub:Find("GridItem/Shell"), var_2_0.name)

	arg_2_0.spList = arg_2_0.window:Find("Fixed/SpList")

	arg_2_0.CloneIconTpl(arg_2_0.spList:Find("Item/Active/Item"), "Icon")
	setText(arg_2_0.boxView:Find("Content/Title/Text"), i18n("battle_end_subtitle1"))
	setText(arg_2_0.boxView:Find("Content/TitleSub/Text"), i18n("settle_rewards_text"))
end

function var_0_0.didEnter(arg_3_0)
	var_0_0.super.didEnter(arg_3_0)

	local var_3_0 = arg_3_0.contextData.isAutoFight
	local var_3_1 = PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0) > 0

	if var_3_0 and var_3_1 then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_AUTO_BATTLE)
		LuaHelper.Vibrate()
	end

	local var_3_2 = getProxy(MetaCharacterProxy):getMetaTacticsInfoOnEnd()

	if var_3_2 and #var_3_2 > 0 then
		arg_3_0.metaExpView = MetaExpView.New(arg_3_0.window:Find("Layout"), arg_3_0.event, arg_3_0.contextData)

		local var_3_3 = arg_3_0.metaExpView

		var_3_3:Reset()
		var_3_3:Load()
		var_3_3:setData(var_3_2)
		var_3_3:ActionInvoke("Show")
	end
end

function var_0_0.willExit(arg_4_0)
	arg_4_0:SkipAnim()

	if arg_4_0.metaExpView then
		arg_4_0.metaExpView:Destroy()
	end

	var_0_0.super.willExit(arg_4_0)
end

function var_0_0.UpdateView(arg_5_0)
	local var_5_0 = arg_5_0.contextData

	onButton(arg_5_0, arg_5_0._tf:Find("BG"), function()
		if arg_5_0.isRewardAnimating then
			arg_5_0:SkipAnim()

			return
		end

		existCall(var_5_0.onClose)
		arg_5_0:closeView()
	end)
	onButton(arg_5_0, arg_5_0.window:Find("Fixed/ButtonGO"), function()
		if arg_5_0.contextData.spItemID and not (PlayerPrefs.GetInt("autoFight_firstUse_sp", 0) == 1) then
			PlayerPrefs.SetInt("autoFight_firstUse_sp", 1)
			PlayerPrefs.Save()

			local function var_7_0()
				arg_5_0.contextData.spItemID = nil

				arg_5_0:UpdateSPItem()
			end

			arg_5_0:HandleShowMsgBox({
				hideNo = true,
				content = i18n("autofight_special_operation_tip"),
				onYes = var_7_0,
				onNo = var_7_0
			})

			return
		end

		local var_7_1 = Chapter.GetSPOperationItemCacheKey(arg_5_0.contextData.chapter.id)

		PlayerPrefs.SetInt(var_7_1, arg_5_0.contextData.spItemID or 0)

		local var_7_2 = true

		arg_5_0:emit(LevelMediator2.ON_RETRACKING, arg_5_0.contextData.chapter, var_7_2)
		arg_5_0:closeView()
	end, SFX_CONFIRM)
	onButton(arg_5_0, arg_5_0.window:Find("Fixed/ButtonExit"), function()
		existCall(var_5_0.onClose)
		arg_5_0:closeView()
	end, SFX_CANCEL)
	arg_5_0:UpdateSPItem()

	local var_5_1 = var_5_0.rewards
	local var_5_2 = var_5_0.resultRewards
	local var_5_3 = var_5_0.events
	local var_5_4 = var_5_0.guildTasks
	local var_5_5 = var_5_0.guildAutoReceives
	local var_5_6 = var_5_1 and #var_5_1 > 0
	local var_5_7 = var_5_2 and #var_5_2 > 0
	local var_5_8 = var_5_3 and #var_5_3 > 0
	local var_5_9 = var_5_4 and table.getCount(var_5_4) > 0
	local var_5_10 = var_5_5 and table.getCount(var_5_5) > 0
	local var_5_11 = true
	local var_5_12 = {}

	setActive(arg_5_0.boxView:Find("Content/Title"), false)
	setActive(arg_5_0.itemList, false)

	if var_5_6 then
		var_5_11 = false
		arg_5_0.hasRewards = true

		table.insert(var_5_12, function(arg_10_0)
			setActive(arg_5_0.boxView:Find("Content/Title"), true)
			setActive(arg_5_0.itemList, true)
			arg_10_0()
		end)

		local var_5_13 = CustomIndexLayer.Clone2Full(arg_5_0.itemList, #var_5_1)

		for iter_5_0, iter_5_1 in ipairs(var_5_13) do
			local var_5_14 = var_5_1[iter_5_0]
			local var_5_15 = var_5_13[iter_5_0]

			updateDrop(var_5_15:Find("Shell/Icon"), var_5_14)
			onButton(arg_5_0, var_5_15:Find("Shell/Icon"), function()
				arg_5_0:emit(BaseUI.ON_DROP, var_5_14)
			end, SFX_PANEL)
		end

		arg_5_0.isRewardAnimating = true

		for iter_5_2 = 1, #var_5_1 do
			local var_5_16 = var_5_13[iter_5_2]

			setActive(var_5_16, false)
			table.insert(var_5_12, function(arg_12_0)
				if arg_5_0.exited then
					return
				end

				setActive(var_5_16, true)
				scrollTo(arg_5_0.boxView:Find("Content"), {
					y = 0
				})

				arg_5_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_12_0)).uniqueId
			end)
		end
	end

	setActive(arg_5_0.boxView:Find("Content/TitleSub"), false)
	setActive(arg_5_0.itemListSub, false)

	if var_5_7 then
		var_5_11 = false
		arg_5_0.hasResultRewards = true

		table.insert(var_5_12, function(arg_13_0)
			setActive(arg_5_0.boxView:Find("Content/TitleSub"), true)
			setActive(arg_5_0.itemListSub, true)
			arg_13_0()
		end)

		local var_5_17 = CustomIndexLayer.Clone2Full(arg_5_0.itemListSub, #var_5_2)

		for iter_5_3, iter_5_4 in ipairs(var_5_17) do
			local var_5_18 = var_5_2[iter_5_3]
			local var_5_19 = var_5_17[iter_5_3]

			updateDrop(var_5_19:Find("Shell/Icon"), var_5_18)
			onButton(arg_5_0, var_5_19:Find("Shell/Icon"), function()
				arg_5_0:emit(BaseUI.ON_DROP, var_5_18)
			end, SFX_PANEL)
		end

		arg_5_0.isRewardAnimating = true

		local var_5_20 = {}

		for iter_5_5 = 1, #var_5_2 do
			local var_5_21 = var_5_17[iter_5_5]

			setActive(var_5_21, false)
			table.insert(var_5_12, function(arg_15_0)
				if arg_5_0.exited then
					return
				end

				setActive(var_5_21, true)
				scrollTo(arg_5_0.boxView:Find("Content"), {
					y = 0
				})

				arg_5_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_15_0)).uniqueId
			end)
		end
	end

	setActive(arg_5_0.boxView:Find("Content/TextArea"), false)

	local var_5_22 = {}

	if var_5_8 then
		for iter_5_6, iter_5_7 in ipairs(var_5_3) do
			local var_5_23 = pg.collection_template[iter_5_7] and pg.collection_template[iter_5_7].title or ""

			table.insert(var_5_22, i18n("autofight_entrust", var_5_23))
		end
	end

	if var_5_9 then
		for iter_5_8, iter_5_9 in pairs(var_5_4) do
			table.insert(var_5_22, i18n("autofight_task", iter_5_9))
		end
	end

	if var_5_10 then
		for iter_5_10, iter_5_11 in pairs(var_5_5) do
			table.insert(var_5_22, i18n("guild_task_autoaccept_1", iter_5_11))
		end
	end

	if #var_5_22 > 0 then
		var_5_11 = false
		arg_5_0.hasEventMsg = true

		setText(arg_5_0.boxView:Find("Content/TextArea/Text"), table.concat(var_5_22, "\n"))
		table.insert(var_5_12, function(arg_16_0)
			setActive(arg_5_0.boxView:Find("Content/TextArea"), true)
			arg_16_0()
		end)
	end

	setActive(arg_5_0.boxView, not var_5_11)
	setActive(arg_5_0.emptyTip, var_5_11)
	seriesAsync(var_5_12, function()
		arg_5_0:SkipAnim()
	end)
end

function var_0_0.UpdateSPItem(arg_18_0)
	local var_18_0 = getProxy(BagProxy):getItemsByType(Item.SPECIAL_OPERATION_TICKET)
	local var_18_1 = arg_18_0.contextData.chapter:getConfig("special_operation_list")

	var_18_1 = var_18_1 == "" and {} or var_18_1

	local var_18_2 = {}

	for iter_18_0, iter_18_1 in ipairs(pg.benefit_buff_template.all) do
		local var_18_3 = pg.benefit_buff_template[iter_18_1]

		if var_18_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and table.contains(var_18_1, iter_18_1) then
			table.insert(var_18_2, var_18_3)
		end
	end

	local var_18_4 = 1

	setActive(arg_18_0.spList, #var_18_2 ~= 0 and arg_18_0.contextData.chapter:GetRestDailyBonus() == 0)

	if #var_18_2 == 0 then
		return
	end

	UIItemList.StaticAlign(arg_18_0.spList, arg_18_0.spList:GetChild(0), var_18_4, function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 ~= UIItemList.EventUpdate then
			return
		end

		local var_19_0 = var_18_2[arg_19_1 + 1]
		local var_19_1 = tonumber(var_19_0.benefit_condition)

		setText(arg_19_2:Find("Active/Desc"), var_19_0.desc)

		local var_19_2 = _.detect(var_18_0, function(arg_20_0)
			return arg_20_0.configId == var_19_1
		end)
		local var_19_3 = var_19_2 and var_19_2.count > 0

		setActive(arg_19_2:Find("Active"), var_19_3)
		setActive(arg_19_2:Find("Block"), not var_19_3)

		if not var_19_3 then
			setText(arg_19_2:Find("Block"):Find("Desc"), i18n("levelScene_select_noitem"))

			return
		end

		setActive(arg_19_2:Find("Active/Item"), true)
		updateDrop(arg_19_2:Find("Active/Item/Icon"), Drop.New({
			id = var_19_1,
			type = DROP_TYPE_ITEM,
			count = var_19_2 and var_19_2.count or 0
		}))
		onButton(arg_18_0, arg_19_2, function()
			arg_18_0.contextData.spItemID = not arg_18_0.contextData.spItemID and var_19_1 or nil

			if arg_18_0.contextData.spItemID then
				pg.TipsMgr.GetInstance():ShowTips(i18n("levelScene_select_sp"))
			end

			arg_18_0:UpdateSPItem()
		end, SFX_PANEL)
		onButton(arg_18_0, arg_19_2:Find("Active/Item/Icon"), function()
			arg_18_0:emit(BaseUI.ON_ITEM, var_19_1)
		end)
		setActive(arg_19_2:Find("Active/Checkbox/Mark"), tobool(arg_18_0.contextData.spItemID))
	end)
end

function var_0_0.SkipAnim(arg_23_0)
	if not arg_23_0.isRewardAnimating then
		return
	end

	arg_23_0.isRewardAnimating = nil

	if arg_23_0.LTid then
		LeanTween.cancel(arg_23_0.LTid)

		arg_23_0.LTid = nil
	end

	eachChild(arg_23_0.itemList, function(arg_24_0)
		setActive(arg_24_0, true)
	end)
	eachChild(arg_23_0.itemListSub, function(arg_25_0)
		setActive(arg_25_0, true)
	end)
	setActive(arg_23_0.boxView:Find("Content/Title"), arg_23_0.hasRewards)
	setActive(arg_23_0.itemList, arg_23_0.hasRewards)
	setActive(arg_23_0.boxView:Find("Content/TitleSub"), arg_23_0.hasResultRewards)
	setActive(arg_23_0.itemListSub, arg_23_0.hasResultRewards)
	setActive(arg_23_0.boxView:Find("Content/TextArea"), arg_23_0.hasEventMsg)
end

return var_0_0
