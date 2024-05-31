ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.BossPhaseSwitchType
local var_0_2 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleUnitPhaseSwitcher = class("BattleUnitPhaseSwitcher")
var_0_0.Battle.BattleUnitPhaseSwitcher.__name = "BattleUnitPhaseSwitcher"

local var_0_3 = var_0_0.Battle.BattleUnitPhaseSwitcher

function var_0_3.Ctor(arg_1_0, arg_1_1)
	arg_1_0._client = arg_1_1

	arg_1_0._client:AddPhaseSwitcher(arg_1_0)

	arg_1_0._randomWeaponList = {}
end

function var_0_3.Update(arg_2_0)
	local var_2_0 = true
	local var_2_1

	for iter_2_0, iter_2_1 in ipairs(arg_2_0._currentPhaseSwitchParam) do
		local var_2_2 = iter_2_1.type
		local var_2_3 = iter_2_1.param
		local var_2_4 = iter_2_1.to

		if var_2_2 == var_0_1.DURATION then
			if var_2_3 < pg.TimeMgr.GetInstance():GetCombatTime() - arg_2_0._phaseStartTime then
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = false
			end
		elseif var_2_2 == var_0_1.POSITION_X_GREATER then
			if var_2_3 < arg_2_0._client:GetPosition().x then
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = false
			end
		elseif var_2_2 == var_0_1.POSITION_X_LESS then
			if var_2_3 > arg_2_0._client:GetPosition().x then
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = false
			end
		elseif var_2_2 == var_0_1.OXYGEN and var_2_3 >= arg_2_0._client:GetCuurentOxygen() then
			var_2_1 = iter_2_1.to
			iter_2_1.andFlag = false
		end

		var_2_0 = var_2_0 and not iter_2_1.andFlag
	end

	if var_2_1 and var_2_0 then
		arg_2_0:switch(var_2_1)
	end
end

function var_0_3.UpdateHP(arg_3_0, arg_3_1)
	local var_3_0 = true
	local var_3_1

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._currentPhaseSwitchParam) do
		local var_3_2 = iter_3_1.type
		local var_3_3 = iter_3_1.param
		local var_3_4 = iter_3_1.to

		if var_3_2 == var_0_1.HP and arg_3_1 < var_3_3 then
			var_3_1 = var_3_4
			iter_3_1.andFlag = false
		end

		var_3_0 = var_3_0 and not iter_3_1.andFlag
	end

	if var_3_1 and var_3_0 then
		arg_3_0:switch(var_3_1)
	end
end

function var_0_3.SetTemplateData(arg_4_0, arg_4_1)
	arg_4_0._phaseList = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_1) do
		arg_4_0._phaseList[iter_4_1.index] = iter_4_1
	end

	arg_4_0:switch(0)
end

function var_0_3.ForceSwitch(arg_5_0, arg_5_1)
	arg_5_0:switch(arg_5_1)
end

function var_0_3.switch(arg_6_0, arg_6_1)
	if arg_6_1 == -1 or arg_6_0._phaseList[arg_6_1] == nil then
		return
	end

	local var_6_0 = arg_6_0._phaseList[arg_6_1]
	local var_6_1 = {}

	if var_6_0.removeWeapon then
		var_6_1 = Clone(var_6_0.removeWeapon)
	end

	if var_6_0.removeRandomWeapon then
		for iter_6_0, iter_6_1 in ipairs(arg_6_0._randomWeaponList) do
			table.insert(var_6_1, iter_6_1)
		end

		arg_6_0._randomWeaponList = {}
	end

	local var_6_2 = {}

	if var_6_0.addWeapon then
		var_6_2 = Clone(var_6_0.addWeapon)
	end

	if var_6_0.addRandomWeapon then
		local var_6_3 = var_6_0.addRandomWeapon[math.random(#var_6_0.addRandomWeapon)]

		for iter_6_2, iter_6_3 in ipairs(var_6_3) do
			table.insert(var_6_2, iter_6_3)
			table.insert(arg_6_0._randomWeaponList, iter_6_3)
		end
	end

	arg_6_0._currentPhase = var_6_0

	arg_6_0:packagePhaseSwitchParam(var_6_0)
	arg_6_0._client:ShiftWeapon(var_6_1, var_6_2)

	if var_6_0.removeBuff then
		for iter_6_4, iter_6_5 in ipairs(var_6_0.removeBuff) do
			arg_6_0._client:RemoveBuff(iter_6_5)
		end
	end

	if var_6_0.addBuff then
		for iter_6_6, iter_6_7 in ipairs(var_6_0.addBuff) do
			local var_6_4 = var_0_0.Battle.BattleBuffUnit.New(iter_6_7, 1, arg_6_0._client)

			arg_6_0._client:AddBuff(var_6_4)
		end
	end

	if var_6_0.dive then
		arg_6_0._client:ChangeOxygenState(var_6_0.dive)
	end

	if var_6_0.setAI then
		arg_6_0._client:SetAI(var_6_0.setAI)
	end

	if var_6_0.story then
		pg.NewStoryMgr.GetInstance():Play(var_6_0.story)
	end

	if not var_6_0.guide or var_6_0.guide.type == 1 and pg.SeriesGuideMgr.GetInstance():isEnd() then
		-- block empty
	elseif var_6_0.guide.event == nil then
		pg.NewGuideMgr.GetInstance():Play(var_6_0.guide.step)
	else
		pg.NewGuideMgr.GetInstance():Play(var_6_0.guide.step, {
			var_6_0.guide.event
		})
	end

	arg_6_0._phaseStartTime = pg.TimeMgr.GetInstance():GetCombatTime()

	if var_6_0.retreat == true then
		arg_6_0._client:Retreat()
	end
end

function var_0_3.packagePhaseSwitchParam(arg_7_0, arg_7_1)
	arg_7_0._currentPhaseSwitchParam = {}

	local var_7_0 = type(arg_7_1.switchType)

	if var_7_0 == "table" then
		local var_7_1 = arg_7_1.switchType
		local var_7_2 = arg_7_1.switchParam
		local var_7_3 = arg_7_1.switchTo
		local var_7_4 = type(var_7_3) == "number"
		local var_7_5 = 1
		local var_7_6 = #arg_7_1.switchType

		while var_7_5 <= var_7_6 do
			local var_7_7 = {
				type = var_7_1[var_7_5],
				param = var_7_2[var_7_5]
			}

			if var_7_4 then
				var_7_7.to = var_7_3
				var_7_7.andFlag = true
			else
				var_7_7.to = var_7_3[var_7_5]
			end

			table.insert(arg_7_0._currentPhaseSwitchParam, var_7_7)

			var_7_5 = var_7_5 + 1
		end
	elseif var_7_0 == "number" then
		local var_7_8 = {
			type = arg_7_1.switchType
		}

		if arg_7_1.switchParamFunc then
			var_7_8.param = arg_7_1.switchParamFunc()
		else
			var_7_8.param = arg_7_1.switchParam
		end

		var_7_8.to = arg_7_1.switchTo

		table.insert(arg_7_0._currentPhaseSwitchParam, var_7_8)
	end
end
