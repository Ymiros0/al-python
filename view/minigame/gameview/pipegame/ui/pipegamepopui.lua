local var_0_0 = class("PipeGamePopUI")
local var_0_1

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	var_0_1 = PipeGameVo

	arg_1_0:initCountUI()
	arg_1_0:initLeavelUI()
	arg_1_0:initPauseUI()
	arg_1_0:initSettlementUI()
	arg_1_0:initRankUI()
end

function var_0_0.initCountUI(arg_2_0)
	arg_2_0.countUI = findTF(arg_2_0._tf, "pop/CountUI")
	arg_2_0.countAnimator = GetComponent(findTF(arg_2_0.countUI, "count"), typeof(Animator))
	arg_2_0.countDft = GetOrAddComponent(findTF(arg_2_0.countUI, "count"), typeof(DftAniEvent))

	arg_2_0.countDft:SetTriggerEvent(function()
		return
	end)
	arg_2_0.countDft:SetEndEvent(function()
		arg_2_0._event:emit(PipeGameEvent.COUNT_DOWN)
	end)
end

function var_0_0.initLeavelUI(arg_5_0)
	arg_5_0.leaveUI = findTF(arg_5_0._tf, "pop/LeaveUI")

	GetComponent(findTF(arg_5_0.leaveUI, "ad/desc"), typeof(Image)):SetNativeSize()
	setActive(arg_5_0.leaveUI, false)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnOk"), function()
		arg_5_0:resumeGame()
		arg_5_0._event:emit(PipeGameEvent.LEVEL_GAME, true)
	end, SFX_CANCEL)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnCancel"), function()
		arg_5_0:resumeGame()
		arg_5_0._event:emit(PipeGameEvent.LEVEL_GAME, false)
	end, SFX_CANCEL)
end

function var_0_0.initPauseUI(arg_8_0)
	arg_8_0.pauseUI = findTF(arg_8_0._tf, "pop/pauseUI")

	setActive(arg_8_0.pauseUI, false)
	GetComponent(findTF(arg_8_0.pauseUI, "ad/desc"), typeof(Image)):SetNativeSize()
	onButton(arg_8_0._event, findTF(arg_8_0.pauseUI, "ad/btnOk"), function()
		arg_8_0:resumeGame()
		arg_8_0._event:emit(PipeGameEvent.PAUSE_GAME, false)
	end, SFX_CANCEL)
end

function var_0_0.initSettlementUI(arg_10_0)
	arg_10_0.settlementUI = findTF(arg_10_0._tf, "pop/SettleMentUI")

	GetComponent(findTF(arg_10_0.settlementUI, "ad/HighImg"), typeof(Image)):SetNativeSize()
	GetComponent(findTF(arg_10_0.settlementUI, "ad/CurImg"), typeof(Image)):SetNativeSize()
	setActive(arg_10_0.settlementUI, false)
	onButton(arg_10_0._event, findTF(arg_10_0.settlementUI, "ad/btnOver"), function()
		arg_10_0:clearUI()
		arg_10_0._event:emit(PipeGameEvent.BACK_MENU)
	end, SFX_CANCEL)
end

function var_0_0.initRankUI(arg_12_0)
	arg_12_0.rankUI = findTF(arg_12_0._tf, "pop/RankUI")

	arg_12_0:showRank(false)
	GetComponent(findTF(arg_12_0.rankUI, "ad/img/score"), typeof(Image)):SetNativeSize()
	GetComponent(findTF(arg_12_0.rankUI, "ad/img/time"), typeof(Image)):SetNativeSize()

	arg_12_0._rankImg = findTF(arg_12_0.rankUI, "ad/img")
	arg_12_0._rankBtnClose = findTF(arg_12_0.rankUI, "ad/btnClose")
	arg_12_0._rankContent = findTF(arg_12_0.rankUI, "ad/list/content")
	arg_12_0._rankItemTpl = findTF(arg_12_0.rankUI, "ad/list/content/itemTpl")
	arg_12_0._rankEmpty = findTF(arg_12_0.rankUI, "ad/empty")
	arg_12_0._rankDesc = findTF(arg_12_0.rankUI, "ad/desc")
	arg_12_0._rankItems = {}

	setActive(arg_12_0._rankItemTpl, false)
	onButton(arg_12_0._event, findTF(arg_12_0.rankUI, "ad/close"), function()
		arg_12_0:showRank(false)
	end, SFX_CANCEL)
	onButton(arg_12_0._event, arg_12_0._rankBtnClose, function()
		arg_12_0:showRank(false)
	end, SFX_CANCEL)
	setText(arg_12_0._rankDesc, i18n(var_0_1.rank_tip))
	arg_12_0:getRankData()
end

function var_0_0.getRankData(arg_15_0)
	pg.m02:sendNotification(GAME.MINI_GAME_FRIEND_RANK, {
		id = var_0_1.game_id,
		callback = function(arg_16_0)
			local var_16_0 = {}

			for iter_16_0 = 1, #arg_16_0 do
				local var_16_1 = {}

				for iter_16_1, iter_16_2 in pairs(arg_16_0[iter_16_0]) do
					var_16_1[iter_16_1] = iter_16_2
				end

				table.insert(var_16_0, var_16_1)
			end

			table.sort(var_16_0, function(arg_17_0, arg_17_1)
				if arg_17_0.score ~= arg_17_1.score then
					return arg_17_0.score > arg_17_1.score
				elseif arg_17_0.time_data ~= arg_17_1.time_data then
					return arg_17_0.time_data > arg_17_1.time_data
				else
					return arg_17_0.player_id < arg_17_1.player_id
				end
			end)
			arg_15_0:updateRankData(var_16_0)
		end
	})
end

function var_0_0.updateRankData(arg_18_0, arg_18_1)
	for iter_18_0 = 1, #arg_18_1 do
		local var_18_0

		if iter_18_0 > #arg_18_0._rankItems then
			local var_18_1 = tf(instantiate(arg_18_0._rankItemTpl))

			setActive(var_18_1, false)
			setParent(var_18_1, arg_18_0._rankContent)
			table.insert(arg_18_0._rankItems, var_18_1)
		end

		local var_18_2 = arg_18_0._rankItems[iter_18_0]

		arg_18_0:setRankItemData(var_18_2, arg_18_1[iter_18_0], iter_18_0)
		setActive(var_18_2, true)
	end

	for iter_18_1 = #arg_18_1 + 1, #arg_18_0._rankItems do
		setActive(arg_18_0._rankItems, false)
	end

	setActive(arg_18_0._rankEmpty, #arg_18_1 == 0)
	setActive(arg_18_0._rankImg, #arg_18_1 > 0)
end

function var_0_0.setRankItemData(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	local var_19_0 = arg_19_2.name
	local var_19_1 = arg_19_2.player_id
	local var_19_2 = arg_19_2.position
	local var_19_3 = arg_19_2.score
	local var_19_4 = arg_19_2.time_data
	local var_19_5 = getProxy(PlayerProxy):isSelf(var_19_1)

	setText(findTF(arg_19_1, "nameText"), var_19_0)
	arg_19_0:setChildVisible(findTF(arg_19_1, "bg"), false)
	arg_19_0:setChildVisible(findTF(arg_19_1, "rank"), false)

	if arg_19_3 <= 3 then
		setActive(findTF(arg_19_1, "bg/" .. arg_19_3), true)
		setActive(findTF(arg_19_1, "rank/" .. arg_19_3), true)
	elseif var_19_5 then
		setActive(findTF(arg_19_1, "bg/me"), true)
		setActive(findTF(arg_19_1, "rank/count"), true)
	else
		setActive(findTF(arg_19_1, "bg/other"), true)
		setActive(findTF(arg_19_1, "rank/count"), true)
	end

	setText(findTF(arg_19_1, "rank/count"), tostring(arg_19_3))
	setText(findTF(arg_19_1, "score"), tostring(var_19_3))
	setText(findTF(arg_19_1, "time"), tostring(var_19_4))
	setActive(findTF(arg_19_1, "imgMy"), var_19_5)
end

function var_0_0.setChildVisible(arg_20_0, arg_20_1, arg_20_2)
	for iter_20_0 = 1, arg_20_1.childCount do
		local var_20_0 = arg_20_1:GetChild(iter_20_0 - 1)

		setActive(var_20_0, arg_20_2)
	end
end

function var_0_0.showRank(arg_21_0, arg_21_1)
	if arg_21_1 then
		arg_21_0:getRankData()
	end

	setActive(arg_21_0.rankUI, arg_21_1)
end

function var_0_0.updateSettlementUI(arg_22_0)
	GetComponent(findTF(arg_22_0.settlementUI, "ad"), typeof(Animator)):Play("settlement", -1, 0)

	local var_22_0 = var_0_1.scoreNum
	local var_22_1 = math.floor(var_0_1.gameDragTime)
	local var_22_2 = getProxy(MiniGameProxy):GetHighScore(var_0_1.game_id)
	local var_22_3 = var_22_2 and #var_22_2 > 0 and var_22_2[1] or 0
	local var_22_4 = var_22_2 and #var_22_2 > 1 and var_22_2[2] or 0

	setActive(findTF(arg_22_0.settlementUI, "ad/new"), var_22_3 < var_22_0)

	if var_22_0 > 0 and var_22_3 < var_22_0 then
		arg_22_0._event:emit(PipeGameEvent.STORE_SERVER, {
			var_22_0,
			var_22_1
		})
	elseif var_22_0 > 0 and var_22_0 == var_22_3 and var_22_4 < var_22_1 then
		arg_22_0._event:emit(PipeGameEvent.STORE_SERVER, {
			var_22_0,
			var_22_1
		})
	end

	local var_22_5 = findTF(arg_22_0.settlementUI, "ad/highText")
	local var_22_6 = findTF(arg_22_0.settlementUI, "ad/currentText")

	setText(var_22_6, var_22_0)
	setText(var_22_5, var_22_1)
	arg_22_0._event:emit(PipeGameEvent.SUBMIT_GAME_SUCCESS)
end

function var_0_0.backPressed(arg_23_0)
	if isActive(arg_23_0.pauseUI) then
		arg_23_0:resumeGame()
		arg_23_0._event:emit(PipeGameEvent.PAUSE_GAME, false)
	elseif isActive(arg_23_0.leaveUI) then
		arg_23_0:resumeGame()
		arg_23_0._event:emit(PipeGameEvent.LEVEL_GAME, false)
	elseif not isActive(arg_23_0.pauseUI) and not isActive(arg_23_0.pauseUI) then
		if not var_0_1.startSettlement then
			arg_23_0:popPauseUI()
			arg_23_0._event:emit(PipeGameEvent.PAUSE_GAME, true)
		end
	else
		arg_23_0:resumeGame()
	end
end

function var_0_0.resumeGame(arg_24_0)
	setActive(arg_24_0.leaveUI, false)
	setActive(arg_24_0.pauseUI, false)
end

function var_0_0.popLeaveUI(arg_25_0)
	if isActive(arg_25_0.pauseUI) then
		setActive(arg_25_0.pauseUI, false)
	end

	setActive(arg_25_0.leaveUI, true)
end

function var_0_0.popPauseUI(arg_26_0)
	if isActive(arg_26_0.leaveUI) then
		setActive(arg_26_0.leaveUI, false)
	end

	setActive(arg_26_0.pauseUI, true)
end

function var_0_0.updateGameUI(arg_27_0, arg_27_1)
	setText(arg_27_0.scoreTf, arg_27_1.scoreNum)
	setText(arg_27_0.gameTimeS, math.ceil(arg_27_1.gameTime))
end

function var_0_0.readyStart(arg_28_0)
	arg_28_0:popCountUI(true)
	arg_28_0.countAnimator:Play("count")
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_1.SFX_COUNT_DOWN)
end

function var_0_0.popCountUI(arg_29_0, arg_29_1)
	setActive(arg_29_0.countUI, arg_29_1)
end

function var_0_0.popSettlementUI(arg_30_0, arg_30_1)
	setActive(arg_30_0.settlementUI, arg_30_1)
end

function var_0_0.clearUI(arg_31_0)
	setActive(arg_31_0.settlementUI, false)
	setActive(arg_31_0.countUI, false)
end

return var_0_0
