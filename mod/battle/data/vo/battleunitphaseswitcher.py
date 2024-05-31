ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.BossPhaseSwitchType
local var_0_2 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleUnitPhaseSwitcher = class("BattleUnitPhaseSwitcher")
var_0_0.Battle.BattleUnitPhaseSwitcher.__name = "BattleUnitPhaseSwitcher"

local var_0_3 = var_0_0.Battle.BattleUnitPhaseSwitcher

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._client = arg_1_1

	arg_1_0._client.AddPhaseSwitcher(arg_1_0)

	arg_1_0._randomWeaponList = {}

def var_0_3.Update(arg_2_0):
	local var_2_0 = True
	local var_2_1

	for iter_2_0, iter_2_1 in ipairs(arg_2_0._currentPhaseSwitchParam):
		local var_2_2 = iter_2_1.type
		local var_2_3 = iter_2_1.param
		local var_2_4 = iter_2_1.to

		if var_2_2 == var_0_1.DURATION:
			if var_2_3 < pg.TimeMgr.GetInstance().GetCombatTime() - arg_2_0._phaseStartTime:
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = False
		elif var_2_2 == var_0_1.POSITION_X_GREATER:
			if var_2_3 < arg_2_0._client.GetPosition().x:
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = False
		elif var_2_2 == var_0_1.POSITION_X_LESS:
			if var_2_3 > arg_2_0._client.GetPosition().x:
				var_2_1 = iter_2_1.to
				iter_2_1.andFlag = False
		elif var_2_2 == var_0_1.OXYGEN and var_2_3 >= arg_2_0._client.GetCuurentOxygen():
			var_2_1 = iter_2_1.to
			iter_2_1.andFlag = False

		var_2_0 = var_2_0 and not iter_2_1.andFlag

	if var_2_1 and var_2_0:
		arg_2_0.switch(var_2_1)

def var_0_3.UpdateHP(arg_3_0, arg_3_1):
	local var_3_0 = True
	local var_3_1

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._currentPhaseSwitchParam):
		local var_3_2 = iter_3_1.type
		local var_3_3 = iter_3_1.param
		local var_3_4 = iter_3_1.to

		if var_3_2 == var_0_1.HP and arg_3_1 < var_3_3:
			var_3_1 = var_3_4
			iter_3_1.andFlag = False

		var_3_0 = var_3_0 and not iter_3_1.andFlag

	if var_3_1 and var_3_0:
		arg_3_0.switch(var_3_1)

def var_0_3.SetTemplateData(arg_4_0, arg_4_1):
	arg_4_0._phaseList = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_1):
		arg_4_0._phaseList[iter_4_1.index] = iter_4_1

	arg_4_0.switch(0)

def var_0_3.ForceSwitch(arg_5_0, arg_5_1):
	arg_5_0.switch(arg_5_1)

def var_0_3.switch(arg_6_0, arg_6_1):
	if arg_6_1 == -1 or arg_6_0._phaseList[arg_6_1] == None:
		return

	local var_6_0 = arg_6_0._phaseList[arg_6_1]
	local var_6_1 = {}

	if var_6_0.removeWeapon:
		var_6_1 = Clone(var_6_0.removeWeapon)

	if var_6_0.removeRandomWeapon:
		for iter_6_0, iter_6_1 in ipairs(arg_6_0._randomWeaponList):
			table.insert(var_6_1, iter_6_1)

		arg_6_0._randomWeaponList = {}

	local var_6_2 = {}

	if var_6_0.addWeapon:
		var_6_2 = Clone(var_6_0.addWeapon)

	if var_6_0.addRandomWeapon:
		local var_6_3 = var_6_0.addRandomWeapon[math.random(#var_6_0.addRandomWeapon)]

		for iter_6_2, iter_6_3 in ipairs(var_6_3):
			table.insert(var_6_2, iter_6_3)
			table.insert(arg_6_0._randomWeaponList, iter_6_3)

	arg_6_0._currentPhase = var_6_0

	arg_6_0.packagePhaseSwitchParam(var_6_0)
	arg_6_0._client.ShiftWeapon(var_6_1, var_6_2)

	if var_6_0.removeBuff:
		for iter_6_4, iter_6_5 in ipairs(var_6_0.removeBuff):
			arg_6_0._client.RemoveBuff(iter_6_5)

	if var_6_0.addBuff:
		for iter_6_6, iter_6_7 in ipairs(var_6_0.addBuff):
			local var_6_4 = var_0_0.Battle.BattleBuffUnit.New(iter_6_7, 1, arg_6_0._client)

			arg_6_0._client.AddBuff(var_6_4)

	if var_6_0.dive:
		arg_6_0._client.ChangeOxygenState(var_6_0.dive)

	if var_6_0.setAI:
		arg_6_0._client.SetAI(var_6_0.setAI)

	if var_6_0.story:
		pg.NewStoryMgr.GetInstance().Play(var_6_0.story)

	if not var_6_0.guide or var_6_0.guide.type == 1 and pg.SeriesGuideMgr.GetInstance().isEnd():
		-- block empty
	elif var_6_0.guide.event == None:
		pg.NewGuideMgr.GetInstance().Play(var_6_0.guide.step)
	else
		pg.NewGuideMgr.GetInstance().Play(var_6_0.guide.step, {
			var_6_0.guide.event
		})

	arg_6_0._phaseStartTime = pg.TimeMgr.GetInstance().GetCombatTime()

	if var_6_0.retreat == True:
		arg_6_0._client.Retreat()

def var_0_3.packagePhaseSwitchParam(arg_7_0, arg_7_1):
	arg_7_0._currentPhaseSwitchParam = {}

	local var_7_0 = type(arg_7_1.switchType)

	if var_7_0 == "table":
		local var_7_1 = arg_7_1.switchType
		local var_7_2 = arg_7_1.switchParam
		local var_7_3 = arg_7_1.switchTo
		local var_7_4 = type(var_7_3) == "number"
		local var_7_5 = 1
		local var_7_6 = #arg_7_1.switchType

		while var_7_5 <= var_7_6:
			local var_7_7 = {
				type = var_7_1[var_7_5],
				param = var_7_2[var_7_5]
			}

			if var_7_4:
				var_7_7.to = var_7_3
				var_7_7.andFlag = True
			else
				var_7_7.to = var_7_3[var_7_5]

			table.insert(arg_7_0._currentPhaseSwitchParam, var_7_7)

			var_7_5 = var_7_5 + 1
	elif var_7_0 == "number":
		local var_7_8 = {
			type = arg_7_1.switchType
		}

		if arg_7_1.switchParamFunc:
			var_7_8.param = arg_7_1.switchParamFunc()
		else
			var_7_8.param = arg_7_1.switchParam

		var_7_8.to = arg_7_1.switchTo

		table.insert(arg_7_0._currentPhaseSwitchParam, var_7_8)
