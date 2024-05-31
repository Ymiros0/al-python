﻿local var_0_0 = class("SSSSPtPage", import(".TemplatePage.PtTemplatePage"))
local var_0_1 = {
	{
		11,
		1.5
	},
	{
		19,
		2
	},
	{
		25,
		3
	},
	{
		28,
		4
	}
}
local var_0_2 = 0.25
local var_0_3 = 20
local var_0_4 = 20
local var_0_5 = 0.75
local var_0_6 = 3
local var_0_7 = 0.75
local var_0_8 = 5
local var_0_9 = "he"

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.maskNode = arg_1_0:findTF("mask", arg_1_0.bg)
	arg_1_0.role = arg_1_0:findTF("role", arg_1_0.maskNode)
	arg_1_0.food = arg_1_0:findTF("food", arg_1_0.maskNode)
	arg_1_0.monster = arg_1_0:findTF("monster", arg_1_0.maskNode)
	arg_1_0.reflectNode = arg_1_0:findTF("reflection", arg_1_0.maskNode)
	arg_1_0.monsterReflect = arg_1_0:findTF("monster_reflection", arg_1_0.reflectNode)
	arg_1_0.roleReflect = arg_1_0:findTF("role_reflection", arg_1_0.reflectNode)
	arg_1_0.feedBtn = arg_1_0:findTF("feed_btn", arg_1_0.bg)
	arg_1_0.window = arg_1_0:findTF("window")
	arg_1_0.monsterAni = GetComponent(arg_1_0:findTF("panel/monster", arg_1_0.window), typeof(Animator))
	arg_1_0.spineRole = arg_1_0:findTF("panel/spinechar", arg_1_0.window)
	arg_1_0.spriteRole = arg_1_0:findTF("panel/spritechar", arg_1_0.window)
	arg_1_0.isPlaying = false
	arg_1_0.coutinuePlay = {}
end

function var_0_0.OnFirstFlush(arg_2_0)
	var_0_0.super.OnFirstFlush(arg_2_0)
	setActive(arg_2_0.window, false)
	onButton(arg_2_0, arg_2_0.monster, function()
		if arg_2_0.monster.localScale.x == var_0_1[#var_0_1][2] then
			arg_2_0:OpenMonsterWin()
		end
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0:findTF("close", arg_2_0.window), function()
		setActive(arg_2_0.window, false)
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0:findTF("close_btn", arg_2_0.window), function()
		setActive(arg_2_0.window, false)
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.feedBtn, function()
		local var_6_0 = {}
		local var_6_1 = arg_2_0.ptData:GetAward()
		local var_6_2 = getProxy(PlayerProxy):getRawData()
		local var_6_3 = pg.gameset.urpt_chapter_max.description[1]
		local var_6_4 = LOCK_UR_SHIP and 0 or getProxy(BagProxy):GetLimitCntById(var_6_3)
		local var_6_5, var_6_6 = Task.StaticJudgeOverflow(var_6_2.gold, var_6_2.oil, var_6_4, true, true, {
			{
				var_6_1.type,
				var_6_1.id,
				var_6_1.count
			}
		})

		if var_6_5 then
			table.insert(var_6_0, function(arg_7_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					type = MSGBOX_TYPE_ITEM_BOX,
					content = i18n("award_max_warning"),
					items = var_6_6,
					onYes = arg_7_0
				})
			end)
		end

		seriesAsync(var_6_0, function()
			local function var_8_0()
				arg_2_0:PlayFeedAni()
			end

			local var_8_1, var_8_2 = arg_2_0.ptData:GetResProgress()

			arg_2_0:emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_2_0.ptData:GetId(),
				arg1 = var_8_2,
				callback = var_8_0
			})
		end)
	end, SFX_PANEL)
	setActive(arg_2_0:findTF("blink_effect", arg_2_0.bg), true)
	arg_2_0:UpdateMonster()
end

function var_0_0.OnUpdateFlush(arg_10_0)
	var_0_0.super.OnUpdateFlush(arg_10_0)

	local var_10_0, var_10_1, var_10_2 = arg_10_0.ptData:GetLevelProgress()
	local var_10_3, var_10_4, var_10_5 = arg_10_0.ptData:GetResProgress()

	setText(arg_10_0.step, setColorStr(var_10_0, "#f0dbff") .. "/" .. var_10_1)
	setText(arg_10_0.progress, (var_10_5 >= 1 and setColorStr(var_10_3, "#f0dbff") or var_10_3) .. "/" .. var_10_4)

	if isActive(arg_10_0.getBtn) and arg_10_0:IsSpecialPhase() then
		setActive(arg_10_0.getBtn, false)
		setActive(arg_10_0.feedBtn, true)
	else
		setActive(arg_10_0.feedBtn, false)
	end
end

function var_0_0.IsSpecialPhase(arg_11_0)
	local var_11_0 = arg_11_0.ptData:GetLevelProgress()
	local var_11_1 = false

	for iter_11_0, iter_11_1 in ipairs(var_0_1) do
		if var_11_0 == iter_11_1[1] then
			var_11_1 = true
		end
	end

	return var_11_1
end

function var_0_0.GetMonsterScale(arg_12_0, arg_12_1)
	local var_12_0 = 1

	for iter_12_0, iter_12_1 in ipairs(var_0_1) do
		if arg_12_1 > iter_12_1[1] then
			var_12_0 = iter_12_1[2]
		end
	end

	return var_12_0
end

function var_0_0.UpdateMonster(arg_13_0)
	local var_13_0 = arg_13_0.ptData:GetLevelProgress()
	local var_13_1 = arg_13_0:GetMonsterScale(var_13_0)

	setLocalScale(arg_13_0.monster, Vector2(var_13_1, var_13_1))
	setLocalScale(arg_13_0.monsterReflect, Vector2(var_13_1, var_13_1))
end

function var_0_0.PlayFeedAni(arg_14_0)
	if arg_14_0.isPlaying then
		local var_14_0 = arg_14_0.ptData:GetLevelProgress() - 1

		table.insert(arg_14_0.coutinuePlay, var_14_0)

		return
	end

	arg_14_0.isPlaying = true

	arg_14_0:managedTween(LeanTween.moveX, function()
		arg_14_0:PlayThrowFoodAni(function()
			arg_14_0:PlayMonsterAni()
		end)
	end, arg_14_0.role, arg_14_0.role.localPosition.x + var_0_3, var_0_2):setLoopPingPong(1)
end

function var_0_0.PlayThrowFoodAni(arg_17_0, arg_17_1)
	local var_17_0 = Vector2(280, -70)
	local var_17_1 = Vector2(500, -70)
	local var_17_2 = 1
	local var_17_3 = (var_17_1.x - var_17_0.x) / var_0_6
	local var_17_4 = (var_17_1.y - var_17_0.y) / var_0_6

	setLocalPosition(arg_17_0.food, var_17_0)
	setActive(arg_17_0.food, true)

	arg_17_0.foodTimer = Timer.New(function()
		local var_18_0 = Vector2(var_17_0.x + var_17_3 * var_17_2, var_17_0.y + var_17_4 * var_17_2)

		setLocalPosition(arg_17_0.food, var_18_0)

		if var_17_2 == var_0_6 then
			arg_17_0.foodTimer:Stop()
			setActive(arg_17_0.food, false)

			if arg_17_1 then
				arg_17_1()
			end
		else
			var_17_2 = var_17_2 + 1
		end
	end, var_0_5 / var_0_6, var_0_6)

	arg_17_0.foodTimer:Start()
end

function var_0_0.PlayMonsterAni(arg_19_0)
	local var_19_0 = arg_19_0.monster.localScale.x
	local var_19_1 = arg_19_0.coutinuePlay[1] and arg_19_0.coutinuePlay[1] or arg_19_0.ptData:GetLevelProgress()
	local var_19_2 = arg_19_0:GetMonsterScale(var_19_1)
	local var_19_3 = 1
	local var_19_4 = (var_19_2 - var_19_0) / var_0_8

	setLocalScale(arg_19_0.monster, Vector2(var_19_0, var_19_0))
	setLocalScale(arg_19_0.monsterReflect, Vector2(var_19_0, var_19_0))

	arg_19_0.monsterTimer = Timer.New(function()
		local var_20_0 = Vector2(var_19_0 + var_19_4 * var_19_3, var_19_0 + var_19_4 * var_19_3)

		setLocalScale(arg_19_0.monster, var_20_0)
		setLocalScale(arg_19_0.monsterReflect, var_20_0)

		if var_19_3 == var_0_8 then
			arg_19_0.monsterTimer:Stop()

			arg_19_0.monsterTimer = nil
			arg_19_0.isPlaying = false

			if #arg_19_0.coutinuePlay > 0 then
				table.remove(arg_19_0.coutinuePlay, 1)
				arg_19_0:PlayFeedAni()
			end
		else
			var_19_3 = var_19_3 + 1
		end
	end, var_0_7 / var_0_8, var_0_8)

	arg_19_0:managedTween(LeanTween.moveX, function()
		arg_19_0:managedTween(LeanTween.moveY, function()
			arg_19_0.monsterTimer:Start()
		end, arg_19_0.monster, arg_19_0.monster.localPosition.y + var_0_4, var_0_2):setLoopPingPong(2)
	end, arg_19_0.monster, arg_19_0.monster.localPosition.x + var_0_3, var_0_2):setLoopPingPong(2)
end

function var_0_0.OpenMonsterWin(arg_23_0)
	setActive(arg_23_0.window, true)
	arg_23_0.monsterAni:Play("ATK")
	setLocalPosition(arg_23_0.spriteRole, Vector2(-180, -115))

	if LeanTween.isTweening(go(arg_23_0.spriteRole)) then
		LeanTween.cancel(go(arg_23_0.spriteRole))
	end

	arg_23_0:managedTween(LeanTween.moveX, nil, arg_23_0.spriteRole, arg_23_0.spriteRole.localPosition.x + 20, 0.8):setLoopPingPong()
end

function var_0_0.OnHideFlush(arg_24_0)
	setActive(arg_24_0.window, false)
end

function var_0_0.OnDestroy(arg_25_0)
	arg_25_0:cleanManagedTween()

	if arg_25_0.foodTimer then
		arg_25_0.foodTimer:Stop()

		arg_25_0.foodTimer = nil
	end

	if arg_25_0.monsterTimer then
		arg_25_0.monsterTimer:Stop()

		arg_25_0.monsterTimer = nil
	end

	if arg_25_0.model then
		PoolMgr.GetInstance():ReturnSpineChar(var_0_9, arg_25_0.model)

		arg_25_0.model = nil
	end
end

return var_0_0
