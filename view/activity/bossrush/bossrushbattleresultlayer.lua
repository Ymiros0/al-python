local var_0_0 = class("BossRushBattleResultLayer", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "BattleResultBossRushUI"
end

function var_0_0.Ctor(arg_2_0, ...)
	var_0_0.super.Ctor(arg_2_0, ...)

	arg_2_0.loader = AutoLoader.New()
end

function var_0_0.GetAtalsName(arg_3_0)
	return "ui/battleresult_atlas"
end

function var_0_0.preload(arg_4_0, arg_4_1)
	arg_4_0.loader:LoadBundle(arg_4_0:GetAtalsName())
	existCall(arg_4_1)
end

function var_0_0.init(arg_5_0)
	local var_5_0 = arg_5_0._tf:Find("main/Series")

	arg_5_0.resultScroll = var_5_0:Find("Scroll")
	arg_5_0.resultList = var_5_0:Find("Scroll/List")
	arg_5_0.playerExp = var_5_0:Find("playerExp")
	arg_5_0.rightBottomPanel = var_5_0:Find("rightBottomPanel")

	setText(arg_5_0.rightBottomPanel:Find("confirmBtn/Text"), i18n("text_confirm"))
	setText(arg_5_0.resultList:Find("Result/BG/Ships/resulttpl/result/Statistics/kill_count_label"), i18n("battle_result_kill_count"))
	setText(arg_5_0.resultList:Find("Result/BG/Ships/resulttpl/result/Statistics/dmg_count_label"), i18n("battle_result_dmg"))
	setText(arg_5_0.resultList:Find("Result/BG/commanderExp/commander_container"):GetChild(0):Find("empty/add/Text"), i18n("series_enemy_empty_commander_main"))
	setText(arg_5_0.resultList:Find("Result/BG/commanderExp/commander_container"):GetChild(1):Find("empty/add/Text"), i18n("series_enemy_empty_commander_assistant"))
end

local var_0_1 = {
	"sucess_title_bg",
	"fail_title_bg",
	"none_title_bg"
}
local var_0_2 = {
	"1216207f",
	"48160d7f",
	"3c3c3c7f"
}

function var_0_0.didEnter(arg_6_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_6_0._tf, true, {
		lockGlobalBlur = true,
		groupName = LayerWeightConst.GROUP_COMBAT
	})

	local var_6_0 = arg_6_0.contextData.seriesData
	local var_6_1 = var_6_0:GetBattleStatistics()
	local var_6_2 = var_6_0:GetFinalResults()
	local var_6_3 = var_6_0:GetFleets()
	local var_6_4 = var_6_0:GetExpeditionIds()
	local var_6_5 = var_6_3[#var_6_3]
	local var_6_6 = var_6_5:getTeamByName(TeamType.Submarine)
	local var_6_7 = var_6_5:GetRawCommanderIds()
	local var_6_8 = {}
	local var_6_9 = {}

	for iter_6_0 = 1, #var_6_4 do
		local var_6_10 = var_6_3[iter_6_0]

		if var_6_0:GetMode() == BossRushSeriesData.MODE.SINGLE then
			var_6_10 = var_6_3[1]
		end

		local var_6_11 = var_6_2[iter_6_0]
		local var_6_12 = {
			index = iter_6_0,
			oldShips = {},
			ships = {},
			oldCmds = {},
			cmds = {},
			mvp = var_6_11 and var_6_11.mvp or 0
		}
		local var_6_13 = Clone(var_6_12)

		table.Foreach(var_6_10:getShipIds(), function(arg_7_0, arg_7_1)
			if iter_6_0 <= #var_6_2 then
				local var_7_0 = var_6_11.newShips[arg_7_1]

				if var_7_0 then
					table.insert(var_6_12.ships, var_7_0)

					var_6_12.oldShips[arg_7_1] = var_6_11.oldShips[arg_7_1]
				end
			else
				local var_7_1 = getProxy(BayProxy):getShipById(arg_7_1)

				table.insert(var_6_12.ships, var_7_1)

				var_6_12.oldShips[arg_7_1] = var_7_1
			end
		end)
		table.Foreach(var_6_6, function(arg_8_0, arg_8_1)
			if iter_6_0 <= #var_6_2 then
				local var_8_0 = var_6_11.newShips[arg_8_1]

				if var_8_0 then
					table.insert(var_6_13.ships, var_8_0)

					var_6_13.oldShips[arg_8_1] = var_6_11.oldShips[arg_8_1]
				end
			end
		end)

		local var_6_14 = var_6_10:GetRawCommanderIds()

		_.each({
			1,
			2
		}, function(arg_9_0)
			local var_9_0 = var_6_14[arg_9_0] or false

			if var_9_0 then
				if iter_6_0 <= #var_6_2 then
					local var_9_1 = var_6_11.newCmds[var_9_0]

					if var_9_1 then
						table.insert(var_6_12.cmds, var_9_1)

						var_6_12.oldCmds[var_9_0] = var_6_11.oldCmds[var_9_0]
					end
				else
					local var_9_2 = getProxy(CommanderProxy):getCommanderById(var_9_0)

					table.insert(var_6_12.cmds, var_9_2)

					var_6_12.oldCmds[var_9_0] = var_9_2
				end
			else
				table.insert(var_6_12.cmds, false)
			end
		end)
		_.each({
			1,
			2
		}, function(arg_10_0)
			local var_10_0 = var_6_7[arg_10_0] or false

			if iter_6_0 <= #var_6_2 then
				if var_10_0 then
					local var_10_1 = var_6_11.newCmds[var_10_0]

					if var_10_1 then
						table.insert(var_6_13.cmds, var_10_1)

						var_6_13.oldCmds[var_10_1.id] = var_6_11.oldCmds[var_10_0]
					else
						table.insert(var_6_13.cmds, false)
					end
				else
					table.insert(var_6_13.cmds, false)
				end
			end
		end)

		var_6_8[iter_6_0] = var_6_12

		if next(var_6_13.ships) then
			table.insert(var_6_9, var_6_13)
		end
	end

	local var_6_15 = 0
	local var_6_16 = 0

	local function var_6_17(arg_11_0, arg_11_1, arg_11_2)
		UIItemList.StaticAlign(arg_11_0, arg_11_0:GetChild(0), 2, function(arg_12_0, arg_12_1, arg_12_2)
			if arg_12_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_12_0 = arg_11_2[arg_12_1 + 1]
			local var_12_1 = not var_12_0

			setActive(arg_12_2:Find("empty"), var_12_1)
			setActive(arg_12_2:Find("exp"), not var_12_1)

			if var_12_1 then
				return
			end

			local var_12_2 = arg_11_1[var_12_0.id]
			local var_12_3 = var_12_0.exp

			GetImageSpriteFromAtlasAsync("commandericon/" .. var_12_0:getPainting(), "", arg_12_2:Find("exp/icon"))
			setText(arg_12_2:Find("exp/name_text"), var_12_0:getName())
			setText(arg_12_2:Find("exp/lv_text"), "Lv." .. var_12_0.level)

			local var_12_4 = math.max(0, var_12_2.expAdd or 0)

			setText(arg_12_2:Find("exp/exp_text"), "+" .. var_12_4)

			local var_12_5
			local var_12_6 = var_12_0:isMaxLevel() and 1 or var_12_3 / var_12_0:getNextLevelExp()

			arg_12_2:Find("exp/exp_progress"):GetComponent(typeof(Image)).fillAmount = var_12_6
		end)
	end

	local function var_6_18(arg_13_0, arg_13_1, arg_13_2)
		setActive(arg_13_0:Find("result/mvpBG"), arg_13_1 == arg_13_2)
	end

	local function var_6_19(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
		UIItemList.StaticAlign(arg_14_0, arg_14_0:GetChild(0), #arg_14_1, function(arg_15_0, arg_15_1, arg_15_2)
			if arg_15_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_15_0 = arg_14_1[arg_15_1 + 1]
			local var_15_1 = arg_14_2[var_15_0.id]

			setActive(arg_15_2:Find("result/Exp"), true)
			setActive(arg_15_2:Find("result/Statistics"), false)
			var_6_18(arg_15_2, var_15_0.id, arg_14_3)

			local var_15_2 = arg_6_0:findTF("result/mask/icon", arg_15_2)
			local var_15_3 = arg_6_0:findTF("result/type", arg_15_2)
			local var_15_4 = GetSpriteFromAtlas("shiptype", shipType2print(var_15_1:getShipType()))

			setImageSprite(var_15_3, var_15_4, true)
			setImageSprite(var_15_2, LoadSprite("herohrzicon/" .. var_15_1:getPainting()))

			local var_15_5 = findTF(arg_15_2, "result/stars")
			local var_15_6 = findTF(arg_15_2, "result/stars/star_tpl")
			local var_15_7 = var_15_1:getStar()
			local var_15_8 = var_15_1:getMaxStar()

			UIItemList.StaticAlign(var_15_5, var_15_6, var_15_8, function(arg_16_0, arg_16_1, arg_16_2)
				if arg_16_0 ~= UIItemList.EventUpdate then
					return
				end

				local var_16_0 = var_15_8 - arg_16_1

				SetActive(arg_16_2:Find("empty"), var_16_0 > var_15_7)
				SetActive(arg_16_2:Find("star"), var_16_0 <= var_15_7)
			end)
			setText(arg_15_2:Find("result/Exp/Level"), "Lv." .. var_15_0.level)
			setText(arg_15_2:Find("result/Exp/name"), var_15_0:getName())

			local var_15_9 = arg_15_2:Find("result/Exp/exp_text")
			local var_15_10 = var_15_1:getConfig("rarity")

			if var_15_1.level < var_15_0.level then
				local var_15_11 = 0

				for iter_15_0 = var_15_1.level, var_15_0.level - 1 do
					var_15_11 = var_15_11 + getExpByRarityFromLv1(var_15_10, iter_15_0)
				end

				setText(var_15_9, "+" .. var_15_11 + var_15_0:getExp() - var_15_1:getExp())
			else
				setText(var_15_9, "+" .. (var_15_1.expAdd or 0))
			end

			local var_15_12 = arg_6_0:findTF("result/Progress/progress_bar", arg_15_2)
			local var_15_13 = var_15_0:getExp() / getExpByRarityFromLv1(var_15_10, var_15_0.level)

			var_15_12:GetComponent(typeof(Image)).fillAmount = var_15_13
		end)
	end

	local function var_6_20(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4)
		arg_17_4 = arg_17_4 and arg_17_4.statistics

		local var_17_0 = 0

		if not arg_17_4 then
			var_17_0 = 10000
		elseif arg_17_3 == 0 then
			var_17_0 = 0

			for iter_17_0, iter_17_1 in pairs(arg_17_2) do
				var_17_0 = math.max(arg_17_4[iter_17_1.id].output, var_17_0)
			end
		elseif arg_17_3 > 0 then
			var_17_0 = arg_17_4[arg_17_3].output
		end

		UIItemList.StaticAlign(arg_17_0, arg_17_0:GetChild(0), #arg_17_1, function(arg_18_0, arg_18_1, arg_18_2)
			if arg_18_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_18_0 = arg_17_1[arg_18_1 + 1]
			local var_18_1 = arg_17_2[var_18_0.id]

			setActive(arg_18_2:Find("result/Statistics"), true)
			setActive(arg_18_2:Find("result/Exp"), false)
			var_6_18(arg_18_2, var_18_0.id, arg_17_3)

			local var_18_2 = arg_6_0:findTF("result/mask/icon", arg_18_2)
			local var_18_3 = arg_6_0:findTF("result/type", arg_18_2)
			local var_18_4 = GetSpriteFromAtlas("shiptype", shipType2print(var_18_1:getShipType()))

			setImageSprite(var_18_3, var_18_4, true)
			setImageSprite(var_18_2, LoadSprite("herohrzicon/" .. var_18_1:getPainting()))

			local var_18_5 = findTF(arg_18_2, "result/stars")
			local var_18_6 = findTF(arg_18_2, "result/stars/star_tpl")
			local var_18_7 = var_18_1:getStar()
			local var_18_8 = var_18_1:getMaxStar()

			UIItemList.StaticAlign(var_18_5, var_18_6, var_18_8, function(arg_19_0, arg_19_1, arg_19_2)
				if arg_19_0 ~= UIItemList.EventUpdate then
					return
				end

				local var_19_0 = var_18_8 - arg_19_1

				SetActive(arg_19_2:Find("empty"), var_19_0 > var_18_7)
				SetActive(arg_19_2:Find("star"), var_19_0 <= var_18_7)
			end)

			local var_18_9 = arg_17_4 and arg_17_4[var_18_1.id].output or 0
			local var_18_10 = arg_17_4 and arg_17_4[var_18_1.id].kill_count or 0
			local var_18_11 = arg_6_0:findTF("result/Statistics/atk", arg_18_2)

			setText(var_18_11, 0)
			setText(var_18_11, var_18_9)

			local var_18_12 = arg_6_0:findTF("result/Statistics/killCount", arg_18_2)

			setText(var_18_12, 0)
			setText(var_18_12, var_18_10)

			local var_18_13 = arg_6_0:findTF("result/Progress/progress_bar", arg_18_2)

			var_18_13:GetComponent(typeof(Image)).fillAmount = 0

			local var_18_14 = var_18_9 / var_17_0

			var_18_13:GetComponent(typeof(Image)).fillAmount = var_18_14
		end)
	end

	local function var_6_21(arg_20_0, arg_20_1, arg_20_2, arg_20_3)
		arg_20_2 = arg_20_2 and arg_20_2.statistics

		local var_20_0 = arg_20_0:Find("Title/Label")
		local var_20_1 = arg_20_0:Find("Title/Letter")
		local var_20_2 = {
			"d",
			"c",
			"b",
			"a",
			"s"
		}
		local var_20_3
		local var_20_4
		local var_20_5
		local var_20_6
		local var_20_7

		if arg_20_2 then
			local var_20_8 = var_20_2[arg_20_2._battleScore + 1]

			var_20_6 = "letter_" .. var_20_8
			var_20_4 = "battlescore/battle_score_" .. var_20_8 .. "/letter_" .. var_20_8
			var_20_7 = "label_" .. var_20_8
			var_20_5 = "battlescore/battle_score_" .. var_20_8 .. "/label_" .. var_20_8

			if arg_20_2._scoreMark == ys.Battle.BattleConst.DEAD_FLAG then
				var_20_7 = "label_flag_destroy"
				var_20_5 = "battlescore/battle_score_c/label_flag_destroy"
			end
		else
			var_20_6 = ""
			var_20_7 = "label_none"
			var_20_5 = "battlescore/grade_label_none"
		end

		eachChild(var_20_0, function(arg_21_0)
			setActive(arg_21_0, arg_21_0.name == var_20_7)

			if arg_21_0.name == var_20_7 then
				arg_6_0.loader:GetSprite(var_20_5, "", arg_21_0)
			end
		end)
		eachChild(var_20_1, function(arg_22_0)
			setActive(arg_22_0, arg_22_0.name == var_20_6)

			if arg_22_0.name == var_20_6 then
				arg_6_0.loader:GetSprite(var_20_4, "", arg_22_0)
			end
		end)

		local var_20_9 = 0
		local var_20_10 = not arg_20_2 and 3 or arg_20_2._battleScore > ys.Battle.BattleConst.BattleScore.C and 1 or 2
		local var_20_11 = var_0_1[var_20_10]

		arg_6_0.loader:GetSprite(arg_6_0:GetAtalsName(), var_20_11, arg_20_0:Find("Title"))

		local var_20_12 = var_0_2[var_20_10]

		setImageColor(arg_20_0:Find("BG"), SummerFeastScene.TransformColor(var_20_12))

		local var_20_13 = pg.expedition_data_template[var_6_4[arg_20_3]]

		setText(arg_20_0:Find("Title/Name"), var_20_13.name)
		setText(arg_20_0:Find("BG/FleetName/Text"), i18n("series_enemy_fleet_prefix", GetRomanDigit(arg_20_1.index)))
		var_6_17(arg_20_0:Find("BG/commanderExp/commander_container"), arg_20_1.oldCmds, arg_20_1.cmds)
	end

	local function var_6_22()
		local var_23_0 = var_6_16 == 1 and var_6_9 or var_6_8

		UIItemList.StaticAlign(arg_6_0.resultList, arg_6_0.resultList:GetChild(0), #var_23_0, function(arg_24_0, arg_24_1, arg_24_2)
			if arg_24_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_24_0 = var_23_0[arg_24_1 + 1]
			local var_24_1 = var_6_1[var_24_0.index]

			var_6_21(arg_24_2, var_24_0, var_24_1, var_24_0.index)
			var_6_19(arg_24_2:Find("BG/Ships"), var_24_0.ships, var_24_0.oldShips, var_24_0.mvp)
		end)
	end

	local function var_6_23()
		local var_25_0 = var_6_16 == 1 and var_6_9 or var_6_8

		UIItemList.StaticAlign(arg_6_0.resultList, arg_6_0.resultList:GetChild(0), #var_25_0, function(arg_26_0, arg_26_1, arg_26_2)
			if arg_26_0 ~= UIItemList.EventUpdate then
				return
			end

			local var_26_0 = var_25_0[arg_26_1 + 1]
			local var_26_1 = var_6_1[var_26_0.index]

			var_6_21(arg_26_2, var_26_0, var_26_1, var_26_0.index)
			var_6_20(arg_26_2:Find("BG/Ships"), var_26_0.ships, var_26_0.oldShips, var_26_0.mvp, var_26_1)
		end)
	end

	local var_6_24 = arg_6_0.rightBottomPanel:Find("submarine")
	local var_6_25 = arg_6_0.rightBottomPanel:Find("main")

	setActive(var_6_24, #var_6_9 > 0)

	local function var_6_26()
		setActive(var_6_25, var_6_16 == 1)
		setActive(var_6_24, var_6_16 == 0 and #var_6_9 > 0)

		if var_6_15 == 0 then
			var_6_22()
		elseif var_6_15 == 1 then
			var_6_23()
		end
	end

	var_6_26()
	;(function()
		local var_28_0 = getProxy(PlayerProxy):getRawData()
		local var_28_1 = _.reduce(var_6_2, 0, function(arg_29_0, arg_29_1)
			return arg_29_0 + arg_29_1.playerExp.addExp
		end)

		setText(arg_6_0._tf:Find("main/Series/playerExp/name_text"), var_28_0.name)
		setText(arg_6_0._tf:Find("main/Series/playerExp/lv_text"), "Lv." .. var_28_0.level)
		setText(arg_6_0._tf:Find("main/Series/playerExp/exp_text"), "+" .. var_28_1)

		local var_28_2 = arg_6_0._tf:Find("main/Series/playerExp/exp_progress")
		local var_28_3 = getConfigFromLevel1(pg.user_level, var_28_0.level)

		var_28_2:GetComponent(typeof(Image)).fillAmount = var_28_0.exp / var_28_3.exp_interval
	end)()
	onButton(arg_6_0, arg_6_0.rightBottomPanel:Find("statisticsBtn"), function()
		var_6_15 = 1 - var_6_15

		var_6_26()
	end, SFX_PANEL)
	onButton(arg_6_0, var_6_24, function()
		var_6_16 = 1

		var_6_26()
	end, SFX_PANEL)
	onButton(arg_6_0, var_6_25, function()
		var_6_16 = 0

		var_6_26()
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rightBottomPanel:Find("confirmBtn"), function()
		arg_6_0:emit(BossRushBattleResultMediator.ON_SETTLE)
	end, SFX_PANEL)

	local var_6_27 = arg_6_0._tf:Find("main/Series/ArrowLeft")
	local var_6_28 = arg_6_0._tf:Find("main/Series/ArrowRight")

	Canvas.ForceUpdateCanvases()

	if arg_6_0.resultScroll.rect.width >= arg_6_0.resultList.rect.width then
		setActive(var_6_27, false)
		setActive(var_6_28, false)
	else
		setActive(var_6_27, false)
		setActive(var_6_28, true)
		onScroll(arg_6_0, arg_6_0.resultScroll, function(arg_34_0)
			setActive(var_6_27, arg_34_0.x > 0.01)
			setActive(var_6_28, arg_34_0.x < 0.99)
		end)
	end
end

function var_0_0.HideConfirmPanel(arg_35_0)
	setActive(arg_35_0.rightBottomPanel:Find("confirmBtn"), false)
end

function var_0_0.onBackPressed(arg_36_0)
	triggerButton(arg_36_0.rightBottomPanel:Find("confirmBtn"))
end

function var_0_0.willExit(arg_37_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_37_0._tf)
	arg_37_0.loader:Clear()
end

return var_0_0
