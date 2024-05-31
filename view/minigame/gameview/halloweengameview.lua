﻿local var_0_0 = class("HalloweenGameView", import("..BaseMiniGameView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = 1
local var_0_6 = 2
local var_0_7 = 1
local var_0_8 = 2
local var_0_9 = {
	{
		3,
		5
	},
	{
		2,
		3
	},
	{
		1.5,
		3
	},
	{
		1,
		2.5
	},
	{
		1,
		2
	},
	{
		0.8,
		1.4
	}
}
local var_0_10 = {
	30,
	80,
	120,
	160,
	180
}
local var_0_11 = {
	4,
	6
}
local var_0_12 = {
	0,
	30
}
local var_0_13 = 0.5
local var_0_14 = {
	{
		10,
		13
	},
	{
		7,
		10
	}
}
local var_0_15 = {
	30
}
local var_0_16 = {
	0,
	3
}
local var_0_17 = {
	1,
	2
}
local var_0_18 = {
	100,
	100,
	100,
	100
}
local var_0_19 = {
	0,
	0,
	0,
	0,
	0,
	0,
	0
}
local var_0_20 = {
	3,
	3.5,
	4,
	4.8,
	5.6,
	6.6,
	8.4
}
local var_0_21 = {
	30,
	80,
	120,
	140,
	160,
	180
}
local var_0_22 = {
	3,
	3.5,
	4,
	4.5,
	4.7,
	5
}
local var_0_23 = {
	30,
	80,
	120,
	160,
	180
}
local var_0_24 = 3
local var_0_25 = {
	110,
	193,
	1170,
	193
}
local var_0_26 = {
	117,
	848,
	1167,
	848
}
local var_0_27 = Vector2(90, 244)
local var_0_28 = 200
local var_0_29 = 5
local var_0_30 = 0
local var_0_31 = 1000000
local var_0_32 = 50000
local var_0_33 = "event:/ui/getcandy"
local var_0_34 = "event:/ui/jackboom"

local function var_0_35(arg_1_0)
	return
end

function var_0_0.getUIName(arg_2_0)
	return "HalloweenGameUI"
end

function var_0_0.getBGM(arg_3_0)
	return "backyard"
end

local function var_0_36(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = {}
	local var_4_1 = {
		{
			0,
			4
		},
		{
			4,
			6
		}
	}
	local var_4_2 = 1
	local var_4_3 = -1

	var_4_0.charactorTf = arg_4_0
	var_4_0.moveRanges = arg_4_1
	var_4_0.scene = arg_4_2
	var_4_0.speedX = 0
	var_4_0.direct = 0
	var_4_0.moveRightFlag = false
	var_4_0.moveLeftFlag = false
	var_4_0.charactorIdleCallback = false

	function var_4_0.ctor(arg_5_0)
		arg_5_0.collider = findTF(arg_5_0.charactorTf, "collider")
		arg_5_0.follow = findTF(arg_5_0.charactorTf, "follow")
		arg_5_0.charAnimator = GetComponent(findTF(arg_5_0.charactorTf, "char"), typeof(Animator))
		arg_5_0.posLight = findTF(arg_5_0.charactorTf, "posLight")
		arg_5_0.lightCharAnimator = GetComponent(findTF(arg_5_0.posLight, "char"), typeof(Animator))
		arg_5_0.lightCharDft = GetComponent(findTF(arg_5_0.posLight, "char"), typeof(DftAniEvent))
		arg_5_0.lightEffectAnimator = GetComponent(findTF(arg_5_0.posLight, "light"), typeof(Animator))
		arg_5_0.charactorDft = GetComponent(findTF(arg_5_0.charactorTf, "char"), typeof(DftAniEvent))

		arg_5_0.charactorDft:SetEndEvent(function(arg_6_0)
			arg_5_0:onAnimationEnd()
		end)
		arg_5_0:clearData()
	end

	function var_4_0.clearData(arg_7_0)
		arg_7_0.inAction = false
		arg_7_0.direct = 0
		arg_7_0.directType = var_4_2
		arg_7_0.currentDirectType = nil
		arg_7_0.ghostFlag = false
		arg_7_0.ghostPlayFlag = false
		arg_7_0.speedRangeIndex = 1
		arg_7_0.maxSpeed = var_0_11[arg_7_0.speedRangeIndex]
		arg_7_0.playLightFlag = false
		arg_7_0.moveLeftFlag = false
		arg_7_0.moveRightFlag = false
		arg_7_0.speedX = 0
	end

	function var_4_0.setGhostFlag(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_1 and (arg_8_0.ghostFlag or arg_8_0.ghostPlayFlag) then
			return
		end

		arg_8_0:ghostAniCallback(true)

		function arg_8_0.aniCallback(arg_9_0)
			if not arg_9_0 then
				arg_8_0.ghostFlag = arg_8_1
			else
				arg_8_0.ghostFlag = false
			end

			if arg_8_2 then
				arg_8_2()
			end
		end

		if arg_8_1 then
			arg_8_0:playGhostDrump()
		else
			arg_8_0:hideDrumpGhost()

			arg_8_0.ghostPlayFlag = false
			arg_8_0.ghostFlag = false
		end
	end

	function var_4_0.playLight(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0.playLightFlag or arg_10_0.inAction then
			if arg_10_1 then
				arg_10_1(false)
			end

			return
		end

		arg_10_0.playLightFlag = true

		setActive(arg_10_0.posLight, true)
		arg_10_0.lightCharDft:SetEndEvent(function()
			arg_10_0.playLightFlag = false
		end)
		arg_10_0.lightCharDft:SetTriggerEvent(function()
			if arg_10_1 then
				arg_10_1(true)
			end
		end)

		if arg_10_2 == var_0_3 then
			arg_10_0.lightCharAnimator:Play("charLight", -1, 0)
			arg_10_0.lightEffectAnimator:Play("lightOn", -1, 0)
		elseif arg_10_2 == var_0_4 then
			arg_10_0.lightCharAnimator:Play("charUnLight", -1, 0)
			arg_10_0.lightEffectAnimator:Play("lightOff", -1, 0)
		end
	end

	function var_4_0.ghostAniCallback(arg_13_0, arg_13_1)
		if arg_13_0.aniCallback then
			arg_13_0.aniCallback(arg_13_1)

			arg_13_0.aniCallback = nil
		end
	end

	function var_4_0.hideDrumpGhost(arg_14_0)
		local var_14_0 = findTF(arg_14_0.charactorTf, "ghostContainer/posGhost")

		setActive(var_14_0, false)
	end

	function var_4_0.getGhostFlag(arg_15_0)
		return arg_15_0.ghostFlag or arg_15_0.ghostPlayFlag
	end

	function var_4_0.getActionFlag(arg_16_0)
		return arg_16_0.inAction
	end

	function var_4_0.playGhostDrump(arg_17_0)
		arg_17_0.ghostPlayFlag = true

		local var_17_0 = findTF(arg_17_0.charactorTf, "ghostContainer/posGhost")

		setActive(var_17_0, true)

		local var_17_1 = GetComponent(var_17_0, typeof(Animator))

		GetComponent(var_17_0, typeof(DftAniEvent)):SetEndEvent(function()
			arg_17_0:ghostAniCallback()
			setActive(var_17_0, false)

			arg_17_0.ghostPlayFlag = false

			if arg_17_0.inSpecial then
				arg_17_0.currentDirectType = nil

				arg_17_0:checkPlayerAnimation(true)

				arg_17_0.inSpecial = false
			end
		end)
		var_17_1:Play("drump", -1, 0)

		local var_17_2 = findTF(var_17_0, "drumpGhost/char")
		local var_17_3 = GetComponent(var_17_2, typeof(Animator))

		var_17_3:SetInteger("state_type", 0)
		var_17_3:SetInteger("state_type", 3)
	end

	function var_4_0.boom(arg_19_0)
		if arg_19_0.inAction then
			return
		end

		local var_19_0 = "boom"

		if arg_19_0.currentDirectType == var_0_1 then
			var_19_0 = var_19_0 .. "_left"
		else
			var_19_0 = var_19_0 .. "_right"
		end

		if arg_19_0.ghostFlag then
			var_19_0 = var_19_0 .. "_ghost"
		end

		arg_19_0:PlayAniamtion(var_19_0, function()
			arg_19_0:checkPlayerAnimation(true)

			arg_19_0.inAction = false
		end)

		arg_19_0.inAction = true
	end

	function var_4_0.fail(arg_21_0, arg_21_1)
		if arg_21_0.inAction then
			return
		end

		local var_21_0 = "fail"

		if arg_21_0.currentDirectType == var_0_1 then
			var_21_0 = var_21_0 .. "_left"
		else
			var_21_0 = var_21_0 .. "_right"
		end

		if arg_21_1 == var_0_7 then
			var_21_0 = var_21_0 .. "_miss"
		elseif arg_21_1 == var_0_8 then
			var_21_0 = var_21_0 .. "_boom"
		end

		if arg_21_0.ghostFlag then
			var_21_0 = var_21_0 .. "_ghost"
		end

		arg_21_0:PlayAniamtion(var_21_0, function()
			arg_21_0.inAction = false
		end)

		arg_21_0.inAction = true
	end

	function var_4_0.gameOver(arg_23_0)
		arg_23_0.moveFlag = false

		if arg_23_0.charactorIdleCallback then
			arg_23_0.charactorIdleCallback(false)
		end
	end

	function var_4_0.start(arg_24_0)
		arg_24_0.moveFlag = true
		arg_24_0.startTime = var_0_30

		arg_24_0:clearData()
	end

	function var_4_0.step(arg_25_0)
		if not arg_25_0.moveFlag then
			return
		end

		if not arg_25_0.inAction then
			if arg_25_0.direct ~= 0 then
				if arg_25_0.maxSpeed - math.abs(arg_25_0.speedX) < var_0_13 then
					arg_25_0.speedX = arg_25_0.maxSpeed * arg_25_0.direct
				elseif math.abs(arg_25_0.speedX) ~= arg_25_0.maxSpeed then
					arg_25_0.speedX = (math.abs(arg_25_0.speedX) + var_0_13) * arg_25_0.direct
				end

				local var_25_0 = arg_25_0.ghostFlag and 0.5 or 1
				local var_25_1 = arg_25_0.charactorTf.localPosition.x + arg_25_0.speedX * var_25_0

				if var_25_1 < arg_25_0.moveRanges[1] then
					var_25_1 = arg_25_0.moveRanges[1]
				end

				if var_25_1 > arg_25_0.moveRanges[3] then
					var_25_1 = arg_25_0.moveRanges[3]
				end

				arg_25_0.charactorTf.localPosition = Vector3(var_25_1, arg_25_0.charactorTf.localPosition.y, arg_25_0.charactorTf.localPosition.z)
			end

			arg_25_0:checkPlayerAnimation()
		end

		if arg_25_0.speedRangeIndex < #var_0_12 then
			for iter_25_0 = #var_0_12, 1, -1 do
				if var_0_30 - arg_25_0.startTime > var_0_12[iter_25_0] and arg_25_0.speedRangeIndex ~= iter_25_0 then
					var_0_35("角色速度提升")

					arg_25_0.speedRangeIndex = iter_25_0
					arg_25_0.maxSpeed = var_0_11[arg_25_0.speedRangeIndex]

					break
				end
			end
		end

		if arg_25_0.speedX == 0 and not arg_25_0.ghostFlag and not arg_25_0.inAction then
			if arg_25_0.specialTime then
				if var_0_30 - arg_25_0.specialTime >= 7 then
					arg_25_0.specialTime = nil
					arg_25_0.inSpecial = true

					arg_25_0:PlayAniamtion("special", function()
						arg_25_0.currentDirectType = nil

						arg_25_0:checkPlayerAnimation(true)

						arg_25_0.inSpecial = false
					end)
				end
			else
				arg_25_0.specialTime = var_0_30
			end
		else
			arg_25_0.specialTime = nil
		end

		if arg_25_0.speedX == 0 and not arg_25_0.inAction then
			if arg_25_0.idleTime then
				if var_0_30 - arg_25_0.idleTime >= 5 then
					arg_25_0.idleTime = nil

					if arg_25_0.charactorIdleCallback then
						arg_25_0.charactorIdleCallback(true)
					end
				end
			else
				arg_25_0.idleTime = var_0_30
			end
		else
			arg_25_0.idleTime = nil

			if arg_25_0.charactorIdleCallback then
				arg_25_0.charactorIdleCallback(false)
			end
		end
	end

	function var_4_0.checkPlayerAnimation(arg_27_0, arg_27_1)
		if arg_27_0.currentDirectType ~= arg_27_0.directType or arg_27_1 then
			arg_27_0.currentDirectType = arg_27_0.directType

			if arg_27_0.currentDirectType == var_0_2 then
				arg_27_0:PlayAniamtion("idle_right")
			else
				arg_27_0:PlayAniamtion("idle_left")
			end
		end

		local var_27_0

		if arg_27_0.speedX == 0 then
			var_27_0 = 0
		else
			for iter_27_0 = 1, #var_4_1 do
				local var_27_1 = var_4_1[iter_27_0]

				if math.abs(arg_27_0.speedX) ~= 0 and arg_27_0.maxSpeed > var_27_1[1] and arg_27_0.maxSpeed <= var_27_1[2] then
					var_27_0 = iter_27_0
				end
			end
		end

		if arg_27_0.charAnimator:GetInteger("speed_type") ~= var_27_0 then
			arg_27_0.charAnimator:SetInteger("speed_type", var_27_0)
		end

		if arg_27_0.charAnimator:GetBool("ghost") ~= arg_27_0.ghostFlag then
			arg_27_0.charAnimator:SetBool("ghost", arg_27_0.ghostFlag)
		end
	end

	function var_4_0.PlayAniamtion(arg_28_0, arg_28_1, arg_28_2)
		var_0_35("开始播放动作:" .. arg_28_1)
		arg_28_0.charAnimator:Play(arg_28_1, -1, 0)

		if arg_28_0.onAniCallback then
			var_0_35(arg_28_0.onAniamtionName .. "的animation被" .. arg_28_1 .. "中断")
		end

		arg_28_0.onAniamtionName = arg_28_1
		arg_28_0.onAniCallback = arg_28_2
	end

	function var_4_0.onAnimationEnd(arg_29_0)
		var_0_35("动作播放结束:" .. arg_29_0.onAniamtionName)

		if arg_29_0.onAniCallback then
			local var_29_0 = arg_29_0.onAniCallback

			arg_29_0.onAniCallback = nil

			var_29_0()
		end
	end

	function var_4_0.onDirectChange(arg_30_0, arg_30_1, arg_30_2)
		if not arg_30_0.moveFlag then
			return
		end

		if arg_30_0.inSpecial then
			arg_30_0.currentDirectType = nil

			arg_30_0:checkPlayerAnimation(true)

			arg_30_0.inSpecial = false
		end

		if arg_30_1 == var_0_1 then
			arg_30_0.moveLeftFlag = arg_30_2
		elseif arg_30_1 == var_0_2 then
			arg_30_0.moveRightFlag = arg_30_2
		end

		local var_30_0

		if arg_30_2 then
			var_30_0 = arg_30_1 == var_0_1 and var_4_3 or var_4_2
		else
			var_30_0 = arg_30_0.moveRightFlag and 1 or arg_30_0.moveLeftFlag and -1 or 0
		end

		if arg_30_0.direct ~= var_30_0 or var_30_0 == 0 then
			arg_30_0.speedX = 0
		end

		arg_30_0.direct = var_30_0

		if arg_30_0.direct ~= 0 then
			arg_30_0.directType = arg_30_0.direct == var_4_3 and var_0_1 or var_0_2
		end
	end

	function var_4_0.getCollider(arg_31_0)
		if not arg_31_0.collider then
			-- block empty
		end

		local var_31_0 = arg_31_0.collider.sizeDelta.x
		local var_31_1 = arg_31_0.collider.sizeDelta.y
		local var_31_2 = arg_31_0.collider.position
		local var_31_3 = arg_31_0.scene:InverseTransformPoint(var_31_2.x, var_31_2.y, 0)

		var_31_3.x = var_31_3.x - var_31_0 / 2

		return {
			pos = var_31_3,
			width = var_31_0,
			height = var_31_1
		}
	end

	function var_4_0.getFollowPos(arg_32_0)
		return arg_32_0.follow.position
	end

	function var_4_0.getLeavePos(arg_33_0)
		local var_33_0

		if arg_33_0.ghostPlayFlag then
			var_33_0 = findTF(arg_33_0.charactorTf, "ghostContainer/posGhost").position

			var_0_35("播放动画中，获取幽灵当前位置")
		else
			if not arg_33_0.leavePos then
				arg_33_0.leavePos = findTF(arg_33_0.charactorTf, "posGhostLeave")
			end

			var_33_0 = arg_33_0.leavePos.position

			var_0_35("播放动画结束，获取头顶位置")
		end

		return var_33_0
	end

	function var_4_0.clearDirect(arg_34_0)
		arg_34_0.direct = 0
		arg_34_0.speedX = 0
	end

	var_4_0:ctor()

	return var_4_0
end

local function var_0_37(arg_35_0, arg_35_1)
	local var_35_0 = {
		moveTf = arg_35_0,
		useLightTf = arg_35_1
	}

	var_35_0.initFlag = false
	var_35_0.direct = 0
	var_35_0.pointChangeCallback = nil
	var_35_0.pointUpCallback = nil
	var_35_0.pointLightCallback = nil
	var_35_0.lightTime = nil

	function var_35_0.Ctor(arg_36_0)
		arg_36_0.buttonDelegate = GetOrAddComponent(arg_36_0.useLightTf, "EventTriggerListener")

		arg_36_0.buttonDelegate:AddPointDownFunc(function(arg_37_0, arg_37_1)
			local var_37_0

			if not arg_36_0.lightTime or var_0_30 - arg_36_0.lightTime > var_0_29 then
				var_37_0 = var_0_3
				arg_36_0.lightTime = var_0_30
			else
				var_37_0 = var_0_4
			end

			if arg_36_0.pointLightCallback then
				arg_36_0.pointLightCallback(var_37_0)
			end
		end)

		arg_36_0.delegateLeft = GetOrAddComponent(findTF(arg_36_0.moveTf, "left"), "EventTriggerListener")
		arg_36_0.delegateRight = GetOrAddComponent(findTF(arg_36_0.moveTf, "right"), "EventTriggerListener")

		arg_36_0.delegateLeft:AddPointDownFunc(function(arg_38_0, arg_38_1)
			if arg_36_0.pointChangeCallback then
				arg_36_0.pointChangeCallback(var_0_1)
			end
		end)
		arg_36_0.delegateRight:AddPointDownFunc(function(arg_39_0, arg_39_1)
			if arg_36_0.pointChangeCallback then
				arg_36_0.pointChangeCallback(var_0_2)
			end
		end)
		arg_36_0.delegateLeft:AddPointUpFunc(function(arg_40_0, arg_40_1)
			if arg_36_0.pointUpCallback then
				arg_36_0.pointUpCallback(var_0_1)
			end
		end)
		arg_36_0.delegateRight:AddPointUpFunc(function(arg_41_0, arg_41_1)
			if arg_36_0.pointUpCallback then
				arg_36_0.pointUpCallback(var_0_2)
			end
		end)

		arg_36_0.initFlag = true
	end

	function var_35_0.callbackDirect(arg_42_0, arg_42_1, arg_42_2)
		if not arg_42_2 then
			return
		end

		local var_42_0 = arg_42_0:getPointFromEventData(arg_42_1)

		var_0_35(var_42_0.x .. "  " .. var_42_0.y)

		local var_42_1 = arg_42_0:getDirect(var_42_0)

		arg_42_2(var_42_1)
	end

	function var_35_0.getPointFromEventData(arg_43_0, arg_43_1)
		if not arg_43_0.uiCam then
			arg_43_0.uiCam = GameObject.Find("UICamera"):GetComponent("Camera")
		end

		local var_43_0 = arg_43_0.uiCam:ScreenToWorldPoint(arg_43_1.position)

		return (arg_43_0.moveTf:InverseTransformPoint(var_43_0))
	end

	function var_35_0.getDirect(arg_44_0, arg_44_1)
		local var_44_0 = arg_44_0.moveTf.sizeDelta.x
		local var_44_1 = arg_44_0.moveTf.sizeDelta.y

		if arg_44_1.x >= 0 then
			return var_0_2
		else
			return var_0_1
		end
	end

	function var_35_0.changeRemind(arg_45_0, arg_45_1)
		arg_45_0.remindFlag = arg_45_1

		local var_45_0 = GetComponent(arg_45_0.useLightTf, typeof(Animator))

		if arg_45_1 and isActive(findTF(arg_45_0.useLightTf, "light")) then
			var_45_0:Play("useLightRemind", -1, 0)
		else
			var_45_0:Play("useLightIdle", -1, 0)
		end
	end

	function var_35_0.start(arg_46_0)
		setActive(findTF(arg_46_0.useLightTf, "light"), true)

		arg_46_0.lightTime = nil
	end

	function var_35_0.step(arg_47_0)
		if not arg_47_0.lightTime or var_0_30 - arg_47_0.lightTime > var_0_29 then
			if not isActive(findTF(arg_47_0.useLightTf, "light")) then
				setActive(findTF(arg_47_0.useLightTf, "light"), true)
				arg_47_0:changeRemind(arg_47_0.remindFlag)
			end
		elseif isActive(findTF(arg_47_0.useLightTf, "light")) then
			setActive(findTF(arg_47_0.useLightTf, "light"), false)
		end
	end

	function var_35_0.gameOver(arg_48_0)
		setActive(findTF(arg_48_0.useLightTf, "light"), false)
	end

	function var_35_0.destroy(arg_49_0)
		if arg_49_0.delegateLeft then
			ClearEventTrigger(arg_49_0.delegateLeft)
		end

		if arg_49_0.delegateRight then
			ClearEventTrigger(arg_49_0.delegateRight)
		end
	end

	var_35_0:Ctor()

	return var_35_0
end

local function var_0_38(arg_50_0, arg_50_1)
	local var_50_0 = {
		_tf = arg_50_0,
		moveRange = arg_50_1
	}

	var_50_0.targetX = nil
	var_50_0.speedX = 1
	var_50_0.dropCallback = nil
	var_50_0.dropNum = 0

	function var_50_0.Ctor(arg_51_0)
		arg_51_0.bodyAnimator = GetComponent(findTF(arg_51_0._tf, "char/body"), typeof(Animator))
		arg_51_0.bodyDft = GetComponent(findTF(arg_51_0._tf, "char/body"), typeof(DftAniEvent))

		arg_51_0.bodyDft:SetEndEvent(function()
			arg_51_0:dropEnd()
		end)
		arg_51_0.bodyDft:SetTriggerEvent(function()
			arg_51_0:dropItem()
		end)
	end

	function var_50_0.start(arg_54_0)
		arg_54_0.moveFlag = true
		arg_54_0.speedLevel = 1
	end

	function var_50_0.gameOver(arg_55_0)
		arg_55_0.moveFlag = false
	end

	function var_50_0.step(arg_56_0)
		if not arg_56_0.moveFlag then
			return
		end

		if arg_56_0.targetX then
			if arg_56_0.targetX ~= arg_56_0._tf.localPosition.x then
				if arg_56_0.targetX > arg_56_0._tf.localPosition.x then
					arg_56_0._tf.localPosition = Vector3(arg_56_0._tf.localPosition.x + arg_56_0:getSpeed(), arg_56_0._tf.localPosition.y, arg_56_0._tf.localPosition.z)
				else
					arg_56_0._tf.localPosition = Vector3(arg_56_0._tf.localPosition.x - arg_56_0:getSpeed(), arg_56_0._tf.localPosition.y, arg_56_0._tf.localPosition.z)
				end
			end

			if math.abs(arg_56_0.targetX - arg_56_0._tf.localPosition.x) <= arg_56_0:getSpeed() then
				arg_56_0.targetX = nil
			end
		end

		if not arg_56_0.targetX then
			arg_56_0:setNextTarget()
		end

		if arg_56_0.speedLevel < #var_0_22 and var_0_23[arg_56_0.speedLevel] < var_0_30 then
			arg_56_0.speedLevel = arg_56_0.speedLevel + 1
		end
	end

	function var_50_0.getSpeed(arg_57_0)
		return var_0_22[arg_57_0.speedLevel]
	end

	function var_50_0.dropItem(arg_58_0)
		if arg_58_0.dropCallback then
			arg_58_0.dropCallback()
		end
	end

	function var_50_0.dropEnd(arg_59_0)
		if arg_59_0.dropNum > 0 then
			arg_59_0.dropNum = arg_59_0.dropNum - 1
		end

		arg_59_0.bodyAnimator:SetInteger("dropNums", arg_59_0.dropNum)
	end

	function var_50_0.addDropNum(arg_60_0)
		arg_60_0.dropNum = arg_60_0.dropNum + 1

		arg_60_0.bodyAnimator:SetInteger("dropNums", arg_60_0.dropNum)
	end

	function var_50_0.setNextTarget(arg_61_0)
		if not arg_61_0.targetX then
			if arg_61_0._tf.localPosition.x < arg_61_0.moveRange[3] / 3 then
				arg_61_0.targetX = math.random(arg_61_0.moveRange[3] * 2 / 3, arg_61_0.moveRange[3])
			else
				arg_61_0.targetX = math.random(arg_61_0.moveRange[1], arg_61_0.moveRange[3] / 3)
			end
		end

		if arg_61_0._tf.localPosition.x > arg_61_0.targetX then
			arg_61_0._tf.localScale = Vector3(-1, 1, 1)
		else
			arg_61_0._tf.localScale = Vector3(1, 1, 1)
		end
	end

	function var_50_0.getDropWorldPos(arg_62_0)
		if not arg_62_0.posDrop then
			arg_62_0.posDrop = findTF(arg_62_0._tf, "char/posDrop")
		end

		return arg_62_0.posDrop.position
	end

	function var_50_0.clear(arg_63_0)
		arg_63_0.dropNum = 0
		arg_63_0.dropCallback = nil
	end

	var_50_0:Ctor()

	return var_50_0
end

local function var_0_39()
	local var_64_0 = {}

	var_64_0.speedLevel = 1
	var_64_0.dropRequestCallback = nil

	function var_64_0.start(arg_65_0)
		arg_65_0.startFlag = true
		arg_65_0.speedLevel = 1
		arg_65_0.startTime = var_0_30
	end

	function var_64_0.gameOver(arg_66_0)
		arg_66_0.startFlag = false
		arg_66_0.stepTime = nil
		arg_66_0.speedLevel = nil
	end

	function var_64_0.step(arg_67_0)
		if not arg_67_0.startFlag then
			return
		end

		if not arg_67_0.stepTime then
			arg_67_0.stepTime = arg_67_0.startTime + math.random() * (var_0_9[arg_67_0.speedLevel][1] - var_0_9[arg_67_0.speedLevel][2]) + var_0_9[arg_67_0.speedLevel][1]
		elseif var_0_30 >= arg_67_0.stepTime then
			arg_67_0.stepTime = var_0_30 + math.random(var_0_9[arg_67_0.speedLevel][1], var_0_9[arg_67_0.speedLevel][2])

			if arg_67_0.dropRequestCallback then
				arg_67_0.dropRequestCallback()
			end
		end

		if arg_67_0.speedLevel <= #var_0_10 then
			if not arg_67_0.nextSpeedUpTime then
				arg_67_0.nextSpeedUpTime = arg_67_0.startTime + var_0_10[arg_67_0.speedLevel]
			end

			if var_0_30 >= arg_67_0.nextSpeedUpTime then
				arg_67_0.speedLevel = arg_67_0.speedLevel + 1
				arg_67_0.nextSpeedUpTime = arg_67_0.speedLevel <= #var_0_10 and var_0_30 + var_0_10[arg_67_0.speedLevel] or nil
			end
		end
	end

	return var_64_0
end

local function var_0_40(arg_68_0, arg_68_1)
	local var_68_0 = {
		flyer = arg_68_0,
		scene = arg_68_1,
		dropItems = {}
	}

	var_68_0.lostCallback = nil
	var_68_0.boomCallback = nil
	var_68_0.dropSpeedUpCallback = nil

	function var_68_0.start(arg_69_0)
		arg_69_0.startFlag = true
		arg_69_0.speedLevel = 1
		arg_69_0.nextSpeedUpTime = nil
		arg_69_0.startTime = var_0_30
	end

	function var_68_0.gameOver(arg_70_0)
		arg_70_0.startFlag = false

		for iter_70_0 = #arg_70_0.dropItems, 1, -1 do
			local var_70_0 = arg_70_0.dropItems[iter_70_0].tf
			local var_70_1 = table.remove(arg_70_0.dropItems, iter_70_0)

			arg_70_0:returnDropItem(var_70_1)
		end
	end

	function var_68_0.createDropItem(arg_71_0)
		local var_71_0 = arg_71_0:getDropItem()
		local var_71_1 = arg_71_0.flyer:getDropWorldPos()
		local var_71_2 = arg_71_0.scene:InverseTransformPoint(var_71_1)

		var_71_0.tf.localPosition = var_71_2

		if not arg_71_0.dropItems then
			arg_71_0.dropItems = {}
		end

		table.insert(arg_71_0.dropItems, var_71_0)
	end

	function var_68_0.getDropItem(arg_72_0)
		if not arg_72_0.dropItemPool then
			arg_72_0.dropItemPool = {}
		end

		local var_72_0

		if #arg_72_0.dropItemPool > 0 then
			var_72_0 = table.remove(arg_72_0.dropItemPool, 1)
		else
			local var_72_1 = tf(instantiate(findTF(arg_72_0.scene, "tplItem")))

			SetParent(var_72_1, arg_72_0.scene, false)

			var_72_0 = {
				tf = var_72_1
			}
		end

		local var_72_2 = math.random(var_0_17[1], var_0_17[2]) <= var_0_17[1] and var_0_6 or var_0_5

		var_72_0.type = var_72_2
		var_72_0.speed = var_0_20[arg_72_0.speedLevel]

		setActive(var_72_0.tf, true)
		arg_72_0:setItemData(var_72_0, var_72_2)

		return var_72_0
	end

	function var_68_0.setItemData(arg_73_0, arg_73_1, arg_73_2)
		local var_73_0 = arg_73_1.tf
		local var_73_1 = findTF(var_73_0, "candy")
		local var_73_2 = findTF(var_73_0, "boom")

		arg_73_1.score = 0

		if arg_73_2 == var_0_5 then
			setActive(var_73_1, true)
			setActive(var_73_2, false)

			local var_73_3 = math.random(var_0_16[1], var_0_16[2])
			local var_73_4 = GetComponent(findTF(var_73_1, "img"), typeof(Animator))

			var_73_4:SetInteger("type", var_73_3)
			var_73_4:Play("candyIdle", -1, 0)

			arg_73_1.score = var_0_18[var_73_3 + 1]
		else
			setActive(var_73_1, false)
			setActive(var_73_2, true)
		end
	end

	function var_68_0.returnDropItem(arg_74_0, arg_74_1)
		setActive(arg_74_1.tf, false)
		table.insert(arg_74_0.dropItemPool, arg_74_1)
	end

	function var_68_0.step(arg_75_0)
		if not arg_75_0.startFlag then
			return
		end

		if arg_75_0.speedLevel <= #var_0_21 then
			if not arg_75_0.nextSpeedUpTime then
				arg_75_0.nextSpeedUpTime = arg_75_0.startTime + var_0_21[arg_75_0.speedLevel]
			end

			if var_0_30 >= arg_75_0.nextSpeedUpTime then
				arg_75_0.speedLevel = arg_75_0.speedLevel + 1
				arg_75_0.nextSpeedUpTime = arg_75_0.speedLevel <= #var_0_21 and arg_75_0.startTime + var_0_21[arg_75_0.speedLevel] or nil

				if arg_75_0.dropSpeedUpCallback then
					arg_75_0.dropSpeedUpCallback()
				end
			end
		end

		if arg_75_0.dropItems and #arg_75_0.dropItems > 0 then
			for iter_75_0 = #arg_75_0.dropItems, 1, -1 do
				local var_75_0 = arg_75_0.dropItems[iter_75_0].tf
				local var_75_1 = arg_75_0.dropItems[iter_75_0].speed + var_0_19[arg_75_0.speedLevel]

				arg_75_0.dropItems[iter_75_0].speed = var_75_1

				if var_75_0.localPosition.y <= var_0_28 then
					local var_75_2 = table.remove(arg_75_0.dropItems, iter_75_0)

					if var_75_2.type == var_0_5 and arg_75_0.lostCallback then
						arg_75_0:playItemLost(var_75_2)
						arg_75_0.lostCallback()
					else
						arg_75_0:returnDropItem(var_75_2)
					end
				else
					var_75_0.localPosition = Vector3(var_75_0.localPosition.x, var_75_0.localPosition.y - var_75_1, var_75_0.localPosition.z)
				end
			end
		end
	end

	function var_68_0.dropItemCollider(arg_76_0, arg_76_1)
		for iter_76_0 = #arg_76_0.dropItems, 1, -1 do
			if table.contains(arg_76_1, iter_76_0) then
				local var_76_0 = table.remove(arg_76_0.dropItems, iter_76_0)

				arg_76_0:playItemEffect(var_76_0)
			end
		end
	end

	function var_68_0.playItemEffect(arg_77_0, arg_77_1)
		local var_77_0 = arg_77_1.type

		if var_77_0 == var_0_5 then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_33)

			local var_77_1 = GetComponent(findTF(arg_77_1.tf, "candy/img"), typeof(Animator))

			GetComponent(findTF(arg_77_1.tf, "candy/img"), typeof(DftAniEvent)):SetEndEvent(function()
				arg_77_0:returnDropItem(arg_77_1)
			end)
			var_77_1:SetTrigger("effect")
		elseif var_77_0 == var_0_6 then
			local var_77_2 = GetComponent(findTF(arg_77_1.tf, "boom/img"), typeof(Animator))
			local var_77_3 = GetComponent(findTF(arg_77_1.tf, "boom/img"), typeof(DftAniEvent))

			var_77_3:SetEndEvent(function()
				arg_77_0:returnDropItem(arg_77_1)
			end)
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_34)
			var_77_3:SetTriggerEvent(function()
				if arg_77_0.boomCallback then
					arg_77_0.boomCallback()
				end
			end)
			var_77_2:SetTrigger("effect")
		end
	end

	function var_68_0.playItemLost(arg_81_0, arg_81_1)
		if arg_81_1.type == var_0_5 then
			local var_81_0 = GetComponent(findTF(arg_81_1.tf, "candy/img"), typeof(Animator))
			local var_81_1 = findTF(arg_81_1.tf, "candy/candy_glow")
			local var_81_2 = GetComponent(findTF(arg_81_1.tf, "candy/img"), typeof(DftAniEvent))
			local var_81_3 = var_81_0:GetLayerIndex("newLayer")

			var_81_2:SetEndEvent(function()
				setActive(var_81_1, false)
				arg_81_0:returnDropItem(arg_81_1)
			end)
			var_81_2:SetTriggerEvent(function()
				setActive(var_81_1, true)
			end)
			var_81_0:Play("candyLost", var_81_3, 0)
		end
	end

	function var_68_0.getDropItemsCollider(arg_84_0)
		if not arg_84_0.dropItems then
			return
		end

		local var_84_0 = {}

		for iter_84_0 = 1, #arg_84_0.dropItems do
			local var_84_1 = findTF(arg_84_0.dropItems[iter_84_0].tf, "collider")
			local var_84_2 = var_84_1.sizeDelta.x
			local var_84_3 = var_84_1.sizeDelta.y
			local var_84_4 = var_84_1.position

			table.insert(var_84_0, {
				x = var_84_4.x,
				y = var_84_4.y,
				width = var_84_2,
				height = var_84_3,
				index = iter_84_0,
				type = arg_84_0.dropItems[iter_84_0].type,
				score = arg_84_0.dropItems[iter_84_0].score
			})
		end

		return var_84_0
	end

	return var_68_0
end

local function var_0_41(arg_85_0, arg_85_1, arg_85_2)
	local var_85_0 = {
		charactor = arg_85_0,
		dropItemController = arg_85_1,
		scene = arg_85_2
	}

	var_85_0.colliderDropItemCallback = nil

	function var_85_0.start(arg_86_0)
		arg_86_0.startFlag = true
	end

	function var_85_0.gameOver(arg_87_0)
		arg_87_0.startFlag = false
	end

	function var_85_0.step(arg_88_0)
		if not arg_88_0.startFlag then
			return
		end

		arg_88_0:checkCollider()
	end

	function var_85_0.checkCollider(arg_89_0)
		local var_89_0 = {}
		local var_89_1 = arg_89_0.dropItemController:getDropItemsCollider()
		local var_89_2 = arg_89_0.charactor:getCollider()
		local var_89_3 = var_89_2.pos

		if var_89_1 and #var_89_1 > 0 then
			for iter_89_0 = 1, #var_89_1 do
				local var_89_4 = var_89_1[iter_89_0]
				local var_89_5 = arg_89_0.scene:InverseTransformPoint(var_89_4.x, var_89_4.y, 0)

				if arg_89_0:checkRectCollider(var_89_3, var_89_5, var_89_2, var_89_4) then
					table.insert(var_89_0, var_89_4.index)

					if arg_89_0.colliderDropItemCallback then
						arg_89_0.colliderDropItemCallback(var_89_4)
					end
				end
			end
		end

		if #var_89_0 > 0 then
			arg_89_0.dropItemController:dropItemCollider(var_89_0)
		end
	end

	function var_85_0.checkRectCollider(arg_90_0, arg_90_1, arg_90_2, arg_90_3, arg_90_4)
		local var_90_0 = arg_90_1.x
		local var_90_1 = arg_90_1.y
		local var_90_2 = arg_90_3.width
		local var_90_3 = arg_90_3.height
		local var_90_4 = arg_90_2.x
		local var_90_5 = arg_90_2.y
		local var_90_6 = arg_90_4.width
		local var_90_7 = arg_90_4.height

		if var_90_4 <= var_90_0 and var_90_0 >= var_90_4 + var_90_6 then
			return false
		elseif var_90_0 <= var_90_4 and var_90_4 >= var_90_0 + var_90_2 then
			return false
		elseif var_90_5 <= var_90_1 and var_90_1 >= var_90_5 + var_90_7 then
			return false
		elseif var_90_1 <= var_90_5 and var_90_5 >= var_90_1 + var_90_3 then
			return false
		else
			return true
		end
	end

	return var_85_0
end

local function var_0_42(arg_91_0)
	local var_91_0 = {
		_tf = arg_91_0
	}

	var_91_0.speedLevel = 1
	var_91_0.createGhostCallback = nil
	var_91_0.ghostSpeedUpCallback = nil

	function var_91_0.start(arg_92_0)
		arg_92_0.startFlag = true
		arg_92_0.speedLevel = 1
		arg_92_0.startTime = var_0_30
		arg_92_0.bossAnimator = GetComponent(findTF(arg_92_0._tf, "char"), typeof(Animator))
		arg_92_0.tip = findTF(arg_92_0._tf, "tip")
	end

	function var_91_0.gameOver(arg_93_0)
		arg_93_0.startFlag = false
		arg_93_0.stepTime = nil

		setActive(arg_93_0.tip, false)
		arg_93_0.bossAnimator:SetInteger("state_type", 0)
	end

	function var_91_0.step(arg_94_0)
		if not arg_94_0.startFlag then
			return
		end

		if not arg_94_0.stepTime then
			arg_94_0.stepTime = arg_94_0.startTime + math.random(var_0_14[arg_94_0.speedLevel][1], var_0_14[arg_94_0.speedLevel][2])
		elseif var_0_30 >= arg_94_0.stepTime then
			arg_94_0.stepTime = var_0_30 + math.random(var_0_14[arg_94_0.speedLevel][1], var_0_14[arg_94_0.speedLevel][2])

			if arg_94_0.createGhostCallback then
				arg_94_0.createGhostCallback()
			end
		end

		if arg_94_0.speedLevel <= #var_0_15 then
			if not arg_94_0.nextSpeedUpTime then
				arg_94_0.nextSpeedUpTime = arg_94_0.startTime + var_0_15[arg_94_0.speedLevel]
			end

			if var_0_30 >= arg_94_0.nextSpeedUpTime then
				arg_94_0.speedLevel = arg_94_0.speedLevel + 1
				arg_94_0.nextSpeedUpTime = arg_94_0.speedLevel <= #var_0_15 and arg_94_0.nextSpeedUpTime + var_0_15[arg_94_0.speedLevel] or nil

				if arg_94_0.ghostSpeedUpCallback then
					arg_94_0.ghostSpeedUpCallback()
				end

				var_0_35("幽灵生成速度提升" .. (arg_94_0.nextSpeedUpTime or "(已经达到最高速度)"))
			end
		end
	end

	function var_91_0.showTip(arg_95_0, arg_95_1)
		if LeanTween.isTweening(go(arg_95_0.tip)) then
			LeanTween.cancel(go(arg_95_0.tip))
		end

		setActive(findTF(arg_95_0.tip, "img1"), false)
		setActive(findTF(arg_95_0.tip, "img2"), false)
		setActive(findTF(arg_95_0.tip, "img" .. arg_95_1), true)
		setActive(arg_95_0.tip, true)
		LeanTween.delayedCall(go(arg_95_0.tip), 10, System.Action(function()
			setActive(arg_95_0.tip, false)
		end))
	end

	function var_91_0.onCreate(arg_97_0)
		arg_97_0.bossAnimator:SetInteger("state_type", 3)
	end

	function var_91_0.onCatch(arg_98_0)
		arg_98_0.bossAnimator:SetInteger("state_type", 2)
	end

	function var_91_0.onGhostDestroy(arg_99_0)
		arg_99_0.bossAnimator:SetInteger("state_type", 1)

		arg_99_0.stepTime = var_0_30 + math.random(var_0_14[arg_99_0.speedLevel][1], var_0_14[arg_99_0.speedLevel][2])
	end

	function var_91_0.destory(arg_100_0)
		if LeanTween.isTweening(go(arg_100_0.tip)) then
			LeanTween.cancel(go(arg_100_0.tip))
		end
	end

	return var_91_0
end

local function var_0_43(arg_101_0, arg_101_1, arg_101_2)
	local var_101_0 = {}
	local var_101_1 = 4

	var_101_0.tplGhost = arg_101_0
	var_101_0.charactor = arg_101_1
	var_101_0.scene = arg_101_2
	var_101_0.catchCharactorCallback = nil

	function var_101_0.start(arg_102_0)
		arg_102_0.startFlag = true
	end

	function var_101_0.gameOver(arg_103_0)
		arg_103_0.startFlag = false

		if not arg_103_0.ghostChilds then
			return
		end

		for iter_103_0 = #arg_103_0.ghostChilds, 1, -1 do
			local var_103_0 = arg_103_0.ghostChilds[iter_103_0]

			arg_103_0:removeChild(var_103_0)
		end
	end

	function var_101_0.step(arg_104_0)
		if not arg_104_0.startFlag or not arg_104_0.ghostChilds then
			return
		end

		local var_104_0 = arg_104_0.charactor:getFollowPos()
		local var_104_1 = arg_104_0.scene:InverseTransformPoint(var_104_0)

		for iter_104_0 = #arg_104_0.ghostChilds, 1, -1 do
			local var_104_2 = arg_104_0.ghostChilds[iter_104_0]

			if isActive(var_104_2) then
				local var_104_3 = var_104_2.anchoredPosition
				local var_104_4 = 0
				local var_104_5 = 0
				local var_104_6 = false
				local var_104_7 = false

				if math.abs(var_104_1.x - var_104_3.x) > 10 then
					var_104_4 = var_101_1 * (var_104_1.x > var_104_3.x and 1 or -1)
				else
					var_104_6 = true
				end

				if math.abs(var_104_1.y - var_104_3.y) > 10 then
					var_104_5 = var_101_1 * (var_104_1.y > var_104_3.y and 1 or -1)
				else
					var_104_7 = true
				end

				if not arg_104_0.charactor:getGhostFlag() and not arg_104_0.charactor:getActionFlag() and var_104_7 and var_104_6 then
					setActive(var_104_2, false)

					if arg_104_0.catchCharactorCallback then
						arg_104_0.catchCharactorCallback(var_104_2)
					end

					return
				end

				var_104_3.x = var_104_3.x + var_104_4
				var_104_3.y = var_104_3.y + var_104_5
				arg_104_0.ghostChilds[iter_104_0].anchoredPosition = var_104_3
			end
		end
	end

	function var_101_0.removeChild(arg_105_0, arg_105_1)
		for iter_105_0 = 1, #arg_105_0.ghostChilds do
			if arg_105_1 == arg_105_0.ghostChilds[iter_105_0] then
				local var_105_0 = table.remove(arg_105_0.ghostChilds, iter_105_0)

				arg_105_0:returnGhost(var_105_0)

				return
			end
		end
	end

	function var_101_0.createGhost(arg_106_0)
		if not arg_106_0.ghostChilds then
			arg_106_0.ghostChilds = {}
		end

		if #arg_106_0.ghostChilds > 0 or arg_101_1:getGhostFlag() then
			return false
		end

		local var_106_0 = arg_106_0:getGhostChild()

		var_106_0.anchoredPosition = var_0_27

		GetComponent(findTF(var_106_0, "char"), typeof(Animator)):SetInteger("state_type", 1)
		table.insert(arg_106_0.ghostChilds, var_106_0)

		return true
	end

	function var_101_0.getGhostChild(arg_107_0)
		if not arg_107_0.ghostPool then
			arg_107_0.ghostPool = {}
		end

		local var_107_0

		if #arg_107_0.ghostPool > 0 then
			var_107_0 = table.remove(arg_107_0.ghostPool, #arg_107_0.ghostPool)
		else
			var_107_0 = tf(instantiate(arg_107_0.tplGhost))

			SetParent(var_107_0, arg_107_0.scene, false)
		end

		setActive(var_107_0, true)

		return var_107_0
	end

	function var_101_0.returnGhost(arg_108_0, arg_108_1)
		setActive(arg_108_1, false)
		table.insert(arg_108_0.ghostPool, arg_108_1)
	end

	function var_101_0.createGhostLight(arg_109_0, arg_109_1)
		if not arg_109_0.lightGhost then
			arg_109_0.lightGhost = tf(instantiate(arg_109_0.tplGhost))
			arg_109_0.lightGhost.name = "lightGhost"
			arg_109_0.lightAnimator = GetComponent(findTF(arg_109_0.lightGhost, "char"), typeof(Animator))

			GetComponent(findTF(arg_109_0.lightGhost, "char"), typeof(DftAniEvent)):SetEndEvent(function()
				setActive(arg_109_0.lightGhost, false)
			end)
			setParent(arg_109_0.lightGhost, arg_109_0.scene)
		end

		if arg_109_0.charactor:getGhostFlag() then
			arg_109_0.lightGhost.anchoredPosition = arg_109_0.scene:InverseTransformPoint(arg_109_0.charactor:getLeavePos())

			setActive(arg_109_0.lightGhost, true)
			arg_109_0.lightAnimator:SetInteger("state_type", 0)
			arg_109_0.lightAnimator:SetInteger("state_type", 2)
			arg_109_1(true)
		else
			arg_109_1(false)
		end
	end

	return var_101_0
end

local function var_0_44(arg_111_0, arg_111_1)
	local var_111_0 = {
		eyeTf = arg_111_0
	}
	local var_111_1 = 3

	function var_111_0.changeEyeShow(arg_112_0, arg_112_1)
		return
	end

	function var_111_0.start(arg_113_0)
		if not arg_113_0.eyes then
			arg_113_0.eyes = {}

			for iter_113_0 = 1, 3 do
				table.insert(arg_113_0.eyes, findTF(arg_113_0.eyeTf, "eye" .. iter_113_0))
			end
		end

		arg_113_0.centerX = (var_0_25[3] - var_0_25[1]) / 2
		arg_113_0.halfRnage = (var_0_25[3] - var_0_25[1]) / 2

		arg_113_0:changeEyeShow(true)
	end

	function var_111_0.step(arg_114_0)
		local var_114_0 = (arg_111_1.anchoredPosition.x - var_0_25[1] - arg_114_0.centerX) / arg_114_0.halfRnage * var_111_1

		for iter_114_0 = 1, #arg_114_0.eyes do
			setAnchoredPosition(findTF(arg_114_0.eyes[iter_114_0], "img"), Vector3(var_114_0, 0, 0))
		end
	end

	function var_111_0.gameOver(arg_115_0)
		return
	end

	return var_111_0
end

function var_0_0.init(arg_116_0)
	arg_116_0:initUI()
	arg_116_0:initData()
	arg_116_0:gameReadyStart()
end

function var_0_0.initUI(arg_117_0)
	onButton(arg_117_0, findTF(arg_117_0._tf, "conLeft/btnClose"), function()
		if not arg_117_0.gameStartFlag then
			arg_117_0:closeView()
		else
			setActive(arg_117_0.leaveUI, true)
			arg_117_0:timerStop()

			arg_117_0.gameStartFlag = false
		end
	end, SFX_CANCEL)

	arg_117_0.playerIdleTip = findTF(arg_117_0._tf, "idleTip")

	setActive(arg_117_0.playerIdleTip, false)

	arg_117_0.hearts = {}

	for iter_117_0 = 1, var_0_24 do
		table.insert(arg_117_0.hearts, findTF(arg_117_0._tf, "conRight/heart/heart" .. iter_117_0))
	end

	arg_117_0.wanshengjie = findTF(arg_117_0._tf, "wanshengjie")

	setActive(arg_117_0.wanshengjie, false)

	arg_117_0.scoreText = findTF(arg_117_0._tf, "conRight/score/text")
	arg_117_0.scene = findTF(arg_117_0._tf, "scene")
	arg_117_0.countUI = findTF(arg_117_0._tf, "pop/CountUI")
	arg_117_0.settlementUI = findTF(arg_117_0._tf, "pop/SettleMentUI")

	onButton(arg_117_0, findTF(arg_117_0.settlementUI, "ad/btnOver"), function()
		arg_117_0:clearUI()
		arg_117_0:closeView()
	end, SFX_CANCEL)

	arg_117_0.leaveUI = findTF(arg_117_0._tf, "pop/LeaveUI")

	onButton(arg_117_0, findTF(arg_117_0.leaveUI, "ad/btnOk"), function()
		setActive(arg_117_0.leaveUI, false)
		arg_117_0:gameOver()
	end, SFX_CANCEL)
	onButton(arg_117_0, findTF(arg_117_0.leaveUI, "ad/btnCancel"), function()
		setActive(arg_117_0.leaveUI, false)
		arg_117_0:timerStart()

		arg_117_0.gameStartFlag = true
	end, SFX_CANCEL)
end

function var_0_0.initData(arg_122_0)
	arg_122_0.timer = Timer.New(function()
		arg_122_0:onTimer()
	end, 0.016666666666666666, -1)
	arg_122_0.charactor = var_0_36(findTF(arg_122_0.scene, "charactor"), var_0_25, arg_122_0.scene)

	function arg_122_0.charactor.charactorIdleCallback(arg_124_0)
		setActive(arg_122_0.playerIdleTip, arg_124_0)
	end

	arg_122_0.flyer = var_0_38(findTF(arg_122_0.scene, "flyCharactor"), var_0_26)

	function arg_122_0.flyer.dropCallback()
		arg_122_0:onCreateDropItem()
	end

	arg_122_0.controllerUI = var_0_37(findTF(arg_122_0._tf, "controller"), findTF(arg_122_0._tf, "conRight/useLight"))

	function arg_122_0.controllerUI.pointChangeCallback(arg_126_0)
		arg_122_0:onControllerDirectChange(arg_126_0)
	end

	function arg_122_0.controllerUI.pointUpCallback(arg_127_0)
		arg_122_0:onControllerDirectUp(arg_127_0)
	end

	function arg_122_0.controllerUI.pointLightCallback(arg_128_0)
		arg_122_0:onUseLight(arg_128_0)
	end

	arg_122_0.dropControl = var_0_39()

	function arg_122_0.dropControl.dropRequestCallback()
		arg_122_0:onRequestDrop()
	end

	arg_122_0.dropItemController = var_0_40(arg_122_0.flyer, arg_122_0.scene)

	function arg_122_0.dropItemController.lostCallback()
		arg_122_0:lostCandy()
	end

	function arg_122_0.dropItemController.boomCallback()
		arg_122_0:touchBoom()
	end

	function arg_122_0.dropItemController.dropSpeedUpCallback()
		arg_122_0:dropSpeedUp()
	end

	arg_122_0.dropColliderControll = var_0_41(arg_122_0.charactor, arg_122_0.dropItemController, arg_122_0.scene)

	function arg_122_0.dropColliderControll.colliderDropItemCallback(arg_133_0)
		arg_122_0:addScore(arg_133_0.score)
	end

	arg_122_0.ghostBossController = var_0_42(findTF(arg_122_0._tf, "ghostBoss"))

	function arg_122_0.ghostBossController.createGhostCallback()
		arg_122_0:createGhost()
	end

	function arg_122_0.ghostBossController.ghostSpeedUpCallback()
		if arg_122_0.eyesController then
			arg_122_0.eyesController:changeEyeShow(false)
		end
	end

	arg_122_0.ghostChildController = var_0_43(findTF(arg_122_0.scene, "tplGhost"), arg_122_0.charactor, arg_122_0.scene)

	function arg_122_0.ghostChildController.catchCharactorCallback(arg_136_0)
		arg_122_0:onGhostCatch(arg_136_0)
	end

	arg_122_0.eyesController = var_0_44(findTF(arg_122_0._tf, "bg/eyes"), findTF(arg_122_0.scene, "charactor"))

	if not arg_122_0.handle then
		arg_122_0.handle = UpdateBeat:CreateListener(arg_122_0.Update, arg_122_0)
	end

	UpdateBeat:AddListener(arg_122_0.handle)

	arg_122_0.countAnimator = GetComponent(findTF(arg_122_0.countUI, "count"), typeof(Animator))
	arg_122_0.countDft = GetComponent(findTF(arg_122_0.countUI, "count"), typeof(DftAniEvent))

	arg_122_0.countDft:SetTriggerEvent(function()
		return
	end)
	arg_122_0.countDft:SetEndEvent(function()
		setActive(arg_122_0.countUI, false)
		arg_122_0:gameStart()
	end)
end

function var_0_0.gameReadyStart(arg_139_0)
	setActive(arg_139_0.countUI, true)
	arg_139_0.countAnimator:Play("count")
end

function var_0_0.gameStart(arg_140_0)
	arg_140_0.heartNum = var_0_24
	arg_140_0.scoreNum = 0
	arg_140_0.gameStartFlag = true
	var_0_30 = 0

	setActive(arg_140_0.scene, true)
	arg_140_0:updateUI()
	arg_140_0.charactor:start()
	arg_140_0.flyer:start()
	arg_140_0.dropControl:start()
	arg_140_0.dropItemController:start()
	arg_140_0.dropColliderControll:start()
	arg_140_0.ghostBossController:start()
	arg_140_0.ghostChildController:start()
	arg_140_0.controllerUI:start()
	arg_140_0.eyesController:start()
	arg_140_0:timerStart()
end

function var_0_0.timerStart(arg_141_0)
	if not arg_141_0.timer.running then
		arg_141_0.timer:Start()
	end

	setActive(arg_141_0.wanshengjie, true)
end

function var_0_0.timerStop(arg_142_0)
	if arg_142_0.timer.running then
		arg_142_0.timer:Stop()
	end

	setActive(arg_142_0.wanshengjie, false)
end

function var_0_0.getGameTimes(arg_143_0)
	return arg_143_0:GetMGHubData().count
end

function var_0_0.getSoundData(arg_144_0, arg_144_1)
	CueData.GetCueData().channelName = pg.CriMgr.C_GALLERY_MUSIC
	arg_144_0.cueData.cueSheetName = arg_144_1
	arg_144_0.cueData.cueName = ""
end

function var_0_0.onTimer(arg_145_0)
	var_0_30 = var_0_30 + arg_145_0.timer.duration

	arg_145_0.charactor:step()
	arg_145_0.flyer:step()
	arg_145_0.dropControl:step()
	arg_145_0.dropItemController:step()
	arg_145_0.dropColliderControll:step()
	arg_145_0.ghostBossController:step()
	arg_145_0.ghostChildController:step()
	arg_145_0.controllerUI:step()
	arg_145_0.eyesController:step()
end

function var_0_0.updateUI(arg_146_0)
	for iter_146_0 = 1, #arg_146_0.hearts do
		if iter_146_0 <= arg_146_0.heartNum then
			setActive(findTF(arg_146_0.hearts[iter_146_0], "img"), true)
		else
			setActive(findTF(arg_146_0.hearts[iter_146_0], "img"), false)
		end
	end

	if not arg_146_0.showOverTip and (arg_146_0.scoreNum >= var_0_31 or var_0_30 * 1000 >= var_0_32) and arg_146_0.ghostBossController then
		arg_146_0.showOverTip = true

		arg_146_0.ghostBossController:showTip(2)
	end

	setText(arg_146_0.scoreText, arg_146_0.scoreNum)
end

function var_0_0.dropSpeedUp(arg_147_0)
	if arg_147_0.ghostBossController then
		arg_147_0.ghostBossController:showTip(1)
	end
end

function var_0_0.loseHeart(arg_148_0, arg_148_1)
	if arg_148_0.heartNum and arg_148_0.heartNum > 0 then
		arg_148_0.heartNum = arg_148_0.heartNum - 1

		arg_148_0:updateUI()

		if arg_148_0.heartNum == 0 then
			local var_148_0 = arg_148_1 == var_0_5 and var_0_7 or var_0_8

			arg_148_0.charactor:fail(var_148_0)

			if var_148_0 == var_0_8 then
				arg_148_0.ghostChildController:createGhostLight(function(arg_149_0)
					if arg_149_0 then
						arg_148_0.ghostBossController:onGhostDestroy()
					end
				end)
				arg_148_0.charactor:setGhostFlag(false)
			end

			arg_148_0.gameStartFlag = false

			arg_148_0:timerStop()
			LeanTween.delayedCall(go(arg_148_0._tf), 3, System.Action(function()
				arg_148_0:gameOver()
			end))
		elseif arg_148_1 == var_0_6 then
			arg_148_0.charactor:boom()
		end
	end
end

function var_0_0.addScore(arg_151_0, arg_151_1)
	arg_151_0.scoreNum = arg_151_0.scoreNum + arg_151_1

	arg_151_0:updateUI()
end

function var_0_0.gameOver(arg_152_0)
	arg_152_0.charactor:gameOver()
	arg_152_0.flyer:gameOver()
	arg_152_0.dropControl:gameOver()
	arg_152_0.dropItemController:gameOver()
	arg_152_0.dropColliderControll:gameOver()
	arg_152_0.ghostBossController:gameOver()
	arg_152_0.ghostChildController:gameOver()
	arg_152_0.controllerUI:gameOver()
	arg_152_0.eyesController:gameOver()

	if arg_152_0:getGameTimes() and arg_152_0:getGameTimes() > 0 then
		arg_152_0:SendSuccess(0)
	end

	arg_152_0:showSettlement()
end

function var_0_0.showSettlement(arg_153_0)
	setActive(arg_153_0.settlementUI, true)
	GetComponent(findTF(arg_153_0.settlementUI, "ad"), typeof(Animator)):Play("settlement", -1, 0)

	local var_153_0 = arg_153_0:GetMGData():GetRuntimeData("elements")
	local var_153_1 = arg_153_0.scoreNum
	local var_153_2 = var_153_0 and #var_153_0 > 0 and var_153_0[1] or 0

	if var_153_2 <= var_153_1 then
		var_153_2 = var_153_1

		arg_153_0:StoreDataToServer({
			var_153_2
		})
	end

	local var_153_3 = findTF(arg_153_0.settlementUI, "ad/highText")
	local var_153_4 = findTF(arg_153_0.settlementUI, "ad/currentText")

	setText(var_153_3, var_153_2)
	setText(var_153_4, var_153_1)
end

function var_0_0.lostCandy(arg_154_0)
	arg_154_0:loseHeart(var_0_5)
end

function var_0_0.touchBoom(arg_155_0)
	arg_155_0:loseHeart(var_0_6)
end

function var_0_0.createGhost(arg_156_0)
	if arg_156_0.ghostChildController and arg_156_0.ghostChildController:createGhost() then
		arg_156_0.ghostBossController:onCreate()
	end
end

function var_0_0.onCreateDropItem(arg_157_0)
	if arg_157_0.dropItemController then
		arg_157_0.dropItemController:createDropItem()
	end
end

function var_0_0.onRequestDrop(arg_158_0)
	if arg_158_0.flyer then
		arg_158_0.flyer:addDropNum()
	end
end

function var_0_0.onGhostCatch(arg_159_0, arg_159_1)
	if not arg_159_0.charactor:getGhostFlag() then
		arg_159_0.charactor:setGhostFlag(true, function()
			arg_159_0.ghostChildController:removeChild(arg_159_1)
		end)
		arg_159_0.controllerUI:changeRemind(true)
		arg_159_0.ghostBossController:onCatch()
	end
end

function var_0_0.onUseLight(arg_161_0, arg_161_1)
	if not arg_161_0.gameStartFlag then
		return
	end

	arg_161_0.charactor:playLight(function(arg_162_0)
		if arg_162_0 and arg_161_1 == var_0_3 then
			arg_161_0.ghostChildController:createGhostLight(function(arg_163_0)
				if arg_163_0 then
					arg_161_0.ghostBossController:onGhostDestroy()
					arg_161_0.controllerUI:changeRemind(false)
				end
			end)
			arg_161_0.charactor:setGhostFlag(false)
		end
	end, arg_161_1)
end

function var_0_0.onColliderItem(arg_164_0, arg_164_1)
	var_0_35("碰撞到了物品，数量:" .. #arg_164_1)
end

function var_0_0.onControllerDirectChange(arg_165_0, arg_165_1)
	arg_165_0:changeDirect(arg_165_1, true)
end

function var_0_0.onControllerDirectUp(arg_166_0, arg_166_1)
	arg_166_0:changeDirect(arg_166_1, false)
end

function var_0_0.changeDirect(arg_167_0, arg_167_1, arg_167_2)
	if arg_167_0.gameStartFlag then
		arg_167_0.charactor:onDirectChange(arg_167_1, arg_167_2)
	end
end

function var_0_0.Update(arg_168_0)
	arg_168_0:AddDebugInput()
end

function var_0_0.AddDebugInput(arg_169_0)
	if IsUnityEditor then
		if Input.GetKeyDown(KeyCode.A) then
			arg_169_0:changeDirect(var_0_1, true)
		end

		if Input.GetKeyUp(KeyCode.A) then
			arg_169_0:changeDirect(var_0_1, false)
		end

		if Input.GetKeyDown(KeyCode.D) then
			arg_169_0:changeDirect(var_0_2, true)
		end

		if Input.GetKeyUp(KeyCode.D) then
			arg_169_0:changeDirect(var_0_2, false)
		end
	end
end

function var_0_0.clearUI(arg_170_0)
	setActive(arg_170_0.scene, false)
	setActive(arg_170_0.settlementUI, false)
	setActive(arg_170_0.countUI, false)
end

function var_0_0.onBackPressed(arg_171_0)
	if not arg_171_0.gameStartFlag then
		arg_171_0:emit(var_0_0.ON_BACK_PRESSED)
	else
		setActive(arg_171_0.leaveUI, true)
		arg_171_0:timerStop()

		arg_171_0.gameStartFlag = false
	end
end

function var_0_0.willExit(arg_172_0)
	if arg_172_0.timer and arg_172_0.timer.running then
		arg_172_0.timer:Stop()
	end

	if LeanTween.isTweening(go(arg_172_0._tf)) then
		LeanTween.cancel(go(arg_172_0._tf))
	end
end

return var_0_0
