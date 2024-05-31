local var_0_0 = class("TowerClimbingController")

function var_0_0.Ctor(arg_1_0)
	arg_1_0.view = TowerClimbingView.New(arg_1_0)
end

function var_0_0.SetCallBack(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.OnGameEndCallBack = arg_2_1
	arg_2_0.OnOverMapScore = arg_2_2
end

function var_0_0.SetUp(arg_3_0, arg_3_1)
	arg_3_0:NetUpdateData(arg_3_1)
	arg_3_0.view:OnEnter()
end

function var_0_0.NetUpdateData(arg_4_0, arg_4_1)
	arg_4_0.data = arg_4_1
end

function var_0_0.StartGame(arg_5_0, arg_5_1)
	if arg_5_0.enterGame then
		return
	end

	arg_5_0.enterGame = true

	seriesAsync({
		function(arg_6_0)
			arg_5_0.map = TowerClimbingMapVO.New(arg_5_1, arg_5_0.view)

			arg_5_0.view:OnCreateMap(arg_5_0.map, arg_6_0)
		end,
		function(arg_7_0)
			arg_5_0.map:Init(arg_5_0.data, arg_7_0)
		end,
		function(arg_8_0)
			arg_5_0.view:DoEnter(arg_8_0)
		end
	}, function()
		arg_5_0.IsStarting = true

		arg_5_0:MainLoop()
		arg_5_0.view:OnStartGame()
	end)
end

function var_0_0.EnterBlock(arg_10_0, arg_10_1, arg_10_2)
	if arg_10_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_10_0.map:GetPlayer():IsDeath() then
		return
	end

	if arg_10_1.normal == Vector2.up then
		arg_10_0.map:GetPlayer():UpdateStand(true)

		arg_10_0.level = arg_10_2

		arg_10_0.map:SetCurrentLevel(arg_10_2)
	end
end

function var_0_0.StayBlock(arg_11_0, arg_11_1, arg_11_2)
	if arg_11_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_11_0.map:GetPlayer():IsDeath() then
		return
	end

	if _.any(arg_11_1, function(arg_12_0)
		return arg_12_0.normal == Vector2.up
	end) and not arg_11_0.map:GetPlayer():IsIdle() and arg_11_2 == Vector2(0, 0) then
		arg_11_0.map:GetPlayer():Idle()
	end
end

function var_0_0.ExitBlock(arg_13_0, arg_13_1)
	if arg_13_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_13_0.map:GetPlayer():IsDeath() then
		return
	end

	if arg_13_0.level == arg_13_1 then
		arg_13_0.map:GetPlayer():UpdateStand(false)
	end
end

function var_0_0.EnterAttacker(arg_14_0)
	if arg_14_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_14_0.map:GetPlayer():IsDeath() then
		return
	end

	arg_14_0.map:GetPlayer():BeInjured()
	arg_14_0.map:GetPlayer():AddInvincibleEffect(TowerClimbingGameSettings.INVINCEIBLE_TIME)
end

function var_0_0.EnterGround(arg_15_0)
	if arg_15_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_15_0.map:GetPlayer():IsDeath() then
		return
	end

	arg_15_0.map:GetPlayer():BeFatalInjured(function()
		if not arg_15_0.map:GetPlayer():IsDeath() then
			arg_15_0.map:GetPlayer():AddInvincibleEffect(TowerClimbingGameSettings.INVINCEIBLE_TIME)
			arg_15_0.map:GetPlayer():UpdateStand(true)
			arg_15_0.map:ReBornPlayer()
			arg_15_0.map:GetPlayer():Idle()
		end
	end)

	if not arg_15_0.map:GetPlayer():IsDeath() then
		arg_15_0.map:SetGroundSleep(TowerClimbingGameSettings.GROUND_SLEEP_TIME)
	end
end

function var_0_0.OnStickChange(arg_17_0, arg_17_1)
	if arg_17_0.map:GetPlayer():IsFatalInjured() then
		return
	end

	if arg_17_1 > 0.05 then
		arg_17_0.map:GetPlayer():MoveRight()
	elseif arg_17_1 < -0.05 then
		arg_17_0.map:GetPlayer():MoveLeft()
	end
end

function var_0_0.MainLoop(arg_18_0)
	if not arg_18_0.handle then
		arg_18_0.handle = UpdateBeat:CreateListener(arg_18_0.Update, arg_18_0)
	end

	UpdateBeat:AddListener(arg_18_0.handle)
end

function var_0_0.Update(arg_19_0)
	arg_19_0.view:Update()
	arg_19_0.map:Update()

	if arg_19_0.IsStarting and arg_19_0.map:GetPlayer():IsDeath() then
		arg_19_0:EndGame()
	end
end

function var_0_0.PlayerJump(arg_20_0)
	arg_20_0.map:GetPlayer():Jump()
end

function var_0_0.PlayerIdle(arg_21_0)
	arg_21_0.map:GetPlayer():Idle()
end

local function var_0_1(arg_22_0)
	arg_22_0.IsStarting = false

	if arg_22_0.handle then
		UpdateBeat:RemoveListener(arg_22_0.handle)
	end
end

function var_0_0.EndGame(arg_23_0)
	var_0_1(arg_23_0)

	local var_23_0 = arg_23_0.map:GetPlayer()

	arg_23_0.view:OnEndGame(var_23_0.score, var_23_0.mapScore, arg_23_0.map.id)

	if arg_23_0.OnGameEndCallBack then
		arg_23_0.OnGameEndCallBack(var_23_0.score, var_23_0.higestscore, var_23_0.pageIndex, arg_23_0.map.id)
	end

	if arg_23_0.OnOverMapScore and var_23_0:IsOverMapScore() then
		arg_23_0.OnOverMapScore(arg_23_0.map.id, var_23_0.score)
	end
end

function var_0_0.updateHighScore(arg_24_0, arg_24_1)
	arg_24_0.highScores = arg_24_1

	arg_24_0.view:SetHighScore(arg_24_1)
end

function var_0_0.ExitGame(arg_25_0)
	var_0_1(arg_25_0)
	arg_25_0.view:OnExitGame()

	if arg_25_0.map then
		arg_25_0.map:Dispose()

		arg_25_0.map = nil
	end

	arg_25_0.enterGame = nil
end

function var_0_0.onBackPressed(arg_26_0)
	return arg_26_0.view:onBackPressed()
end

function var_0_0.Dispose(arg_27_0)
	arg_27_0:ExitGame()
	arg_27_0.view:Dispose()
end

return var_0_0
