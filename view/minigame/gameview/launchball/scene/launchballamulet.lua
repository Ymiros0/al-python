local var_0_0 = class("LaunchBallAmulet")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5
local var_0_6 = 6
local var_0_7 = 7
local var_0_8 = {
	var_0_1,
	var_0_3,
	var_0_4,
	var_0_7,
	var_0_2,
	var_0_5,
	var_0_6
}
local var_0_9 = "amulet s"
local var_0_10 = "amulet l"
local var_0_11 = "amulet ef"
local var_0_12 = 3
local var_0_13 = {
	{
		index = 1,
		anim_name = "EF_A",
		offset = Vector2(0, 20)
	},
	{
		index = 2,
		anim_name = "EF_B",
		offset = Vector2(0, 0)
	},
	{
		index = 3,
		anim_name = "EF_C",
		offset = Vector2(0, -20)
	}
}
local var_0_14 = 50
local var_0_15 = 70
local var_0_16 = -80
local var_0_17 = 1000
local var_0_18 = 90
local var_0_19 = -90
local var_0_20 = 1000
local var_0_21 = 0.05
local var_0_22 = 0.5
local var_0_23 = {
	[var_0_1] = {
		name = "Yellow",
		animator = "Amulet_Yellow_"
	},
	[var_0_3] = {
		name = "White",
		animator = "Amulet_White_"
	},
	[var_0_4] = {
		name = "Red",
		animator = "Amulet_Red_"
	},
	[var_0_7] = {
		name = "Purple",
		animator = "Amulet_Purple_"
	},
	[var_0_2] = {
		name = "Green",
		animator = "Amulet_Green_"
	},
	[var_0_5] = {
		name = "Blue",
		animator = "Amulet_Blue_"
	},
	[var_0_6] = {
		name = "Black",
		animator = "Amulet_Black_"
	}
}

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5)
	arg_1_0.amuletLAnimators = {}
	arg_1_0.amuletSAnimators = {}
	arg_1_0.amuletEFAnimators = {}

	for iter_1_0, iter_1_1 in ipairs(var_0_23) do
		local var_1_0 = iter_1_0
		local var_1_1 = iter_1_1.name
		local var_1_2 = iter_1_1.animator
		local var_1_3 = ResourceMgr.Inst:getAssetSync(LaunchBallGameVo.ui_atlas, var_1_2 .. "L", typeof(RuntimeAnimatorController), false, false)
		local var_1_4 = ResourceMgr.Inst:getAssetSync(LaunchBallGameVo.ui_atlas, var_1_2 .. "S", typeof(RuntimeAnimatorController), false, false)
		local var_1_5 = ResourceMgr.Inst:getAssetSync(LaunchBallGameVo.ui_atlas, var_1_2 .. "EF", typeof(RuntimeAnimatorController), false, false)

		table.insert(arg_1_0.amuletLAnimators, {
			animator = var_1_3,
			type = var_1_0,
			name = var_1_1
		})
		table.insert(arg_1_0.amuletSAnimators, {
			animator = var_1_4,
			type = var_1_0,
			name = var_1_1
		})
		table.insert(arg_1_0.amuletEFAnimators, {
			animator = var_1_5,
			type = var_1_0,
			name = var_1_1
		})
	end

	arg_1_0._content = arg_1_1
	arg_1_0._sContent = arg_1_2
	arg_1_0._lifeContent = arg_1_3
	arg_1_0._tpl = arg_1_4
	arg_1_0._eventCall = arg_1_5
	arg_1_0._amuletLTpl = findTF(arg_1_0._tpl, "amuletL")
	arg_1_0._amuletSTpl = findTF(arg_1_0._tpl, "amuletS")
	arg_1_0._amuletEfTpl = findTF(arg_1_0._tpl, "amuletEF")
	arg_1_0._butterflyTpl = findTF(arg_1_0._tpl, "Butterfly")

	arg_1_0:setAmuletL(nil)

	arg_1_0.amuletS = nil
	arg_1_0.amuletEFs = {}
	arg_1_0.amuletLPool = {}
	arg_1_0.amuletSPool = {}
	arg_1_0.amuletEFPool = {}
	arg_1_0._amuletFires = {}
	arg_1_0.butterflys = {}
end

function var_0_0.start(arg_2_0)
	local var_2_0 = LaunchBallGameVo.gameRoundData.amulet_life

	arg_2_0.lifeBound = GetComponent(findTF(arg_2_0._lifeContent, tostring(var_2_0)), typeof(BoxCollider2D))
	arg_2_0.min = arg_2_0._lifeContent:InverseTransformPoint(arg_2_0.lifeBound.bounds.min)
	arg_2_0.max = arg_2_0._lifeContent:InverseTransformPoint(arg_2_0.lifeBound.bounds.max)
	arg_2_0.amuletType = arg_2_0:getRandomAmuletType()
	arg_2_0.amuletNextType = arg_2_0:getRandomAmuletType()

	arg_2_0:setAmuletL(arg_2_0:getAmulete(var_0_10, arg_2_0.amuletType))

	arg_2_0.amuletS = arg_2_0:getAmulete(var_0_9, arg_2_0.amuletNextType)
	arg_2_0.amuletPos = Vector2(0, 0)
	arg_2_0.angle = var_0_19
	arg_2_0.rad = var_0_19 * math.deg2Rad
	arg_2_0.amuletPos.x = math.cos(arg_2_0.rad) * var_0_15
	arg_2_0.amuletPos.y = math.sin(arg_2_0.rad) * var_0_15
	arg_2_0.isPlaying = false
end

function var_0_0.step(arg_3_0)
	if not arg_3_0.isPlaying then
		if LaunchBallGameVo.joyStickData and LaunchBallGameVo.joyStickData.angle then
			arg_3_0.rad = LaunchBallGameVo.joyStickData.rad
			arg_3_0.angle = LaunchBallGameVo.joyStickData.angle
			arg_3_0.amuletPos.x = math.cos(arg_3_0.rad) * var_0_15
			arg_3_0.amuletPos.y = math.sin(arg_3_0.rad) * var_0_15
		end

		if arg_3_0.amuletL then
			arg_3_0.amuletL.tf.anchoredPosition = arg_3_0.amuletPos
			arg_3_0.amuletL.rad = arg_3_0.rad
		else
			arg_3_0:setAmuletL(arg_3_0:getAmulete(var_0_10, arg_3_0.amuletNextType))
			arg_3_0:returnAmulete(arg_3_0.amuletS, arg_3_0.amuletSPool)

			arg_3_0.amuletNextType = arg_3_0:getRandomAmuletType()
			arg_3_0.amuletS = nil
			arg_3_0.amuletS = arg_3_0:getAmulete(var_0_9, arg_3_0.amuletNextType)
		end

		if arg_3_0.amuletS then
			arg_3_0.amuletS.tf.anchoredPosition = Vector2(math.cos(arg_3_0.rad) * var_0_16, math.sin(arg_3_0.rad) * var_0_16)
		end
	end

	if arg_3_0._amuletFires and #arg_3_0._amuletFires > 0 then
		for iter_3_0 = #arg_3_0._amuletFires, 1, -1 do
			local var_3_0 = arg_3_0._amuletFires[iter_3_0]
			local var_3_1 = var_3_0.tf.anchoredPosition

			var_3_1.x = var_3_1.x + var_3_0.speed.x * LaunchBallGameVo.deltaTime
			var_3_1.y = var_3_1.y + var_3_0.speed.y * LaunchBallGameVo.deltaTime
			var_3_0.tf.anchoredPosition = var_3_1

			if var_3_0.effectTime and var_3_0.effectTime > 0 then
				var_3_0.effectTime = var_3_0.effectTime - LaunchBallGameVo.deltaTime

				if var_3_0.effectTime <= 0 then
					var_3_0.effectTime = var_0_21

					arg_3_0:createEF(var_3_0)
				end
			end

			if math.abs(var_3_1.x) > var_0_20 or math.abs(var_3_1.y) > var_0_20 then
				table.remove(arg_3_0._amuletFires, iter_3_0)
				arg_3_0:returnAmulete(var_3_0, arg_3_0.amuletLPool)
			elseif var_3_0.removeFlag then
				table.remove(arg_3_0._amuletFires, iter_3_0)
				arg_3_0:returnAmulete(var_3_0, arg_3_0.amuletLPool)
			elseif arg_3_0.lifeBound then
				if var_3_1.x >= arg_3_0.max.x or var_3_1.x <= arg_3_0.min.x then
					table.remove(arg_3_0._amuletFires, iter_3_0)
					arg_3_0:returnAmulete(var_3_0, arg_3_0.amuletLPool)
				elseif var_3_1.y >= arg_3_0.max.y or var_3_1.y <= arg_3_0.min.y then
					table.remove(arg_3_0._amuletFires, iter_3_0)
					arg_3_0:returnAmulete(var_3_0, arg_3_0.amuletLPool)
				end
			end
		end
	end

	if arg_3_0.butterflys and #arg_3_0.butterflys > 0 then
		for iter_3_1 = #arg_3_0.butterflys, 1, -1 do
			local var_3_2 = arg_3_0.butterflys[iter_3_1]
			local var_3_3 = var_3_2.tf.anchoredPosition

			var_3_3.x = var_3_3.x + var_3_2.speed.x * LaunchBallGameVo.deltaTime
			var_3_3.y = var_3_3.y + var_3_2.speed.y * LaunchBallGameVo.deltaTime
			var_3_2.tf.anchoredPosition = var_3_3

			if math.abs(var_3_3.x) > var_0_20 or math.abs(var_3_3.y) > var_0_20 then
				var_3_2.anim = nil

				Destroy(var_3_2.tf)
				table.remove(arg_3_0.butterflys, iter_3_1)
			elseif var_3_2.removeFlag then
				var_3_2.anim = nil

				Destroy(var_3_2.tf)
				table.remove(arg_3_0.butterflys, iter_3_1)
			elseif var_3_3.x >= arg_3_0.max.x or var_3_3.x <= arg_3_0.min.x then
				var_3_2.anim = nil

				Destroy(var_3_2.tf)
				table.remove(arg_3_0.butterflys, iter_3_1)
			elseif var_3_3.y >= arg_3_0.max.y or var_3_3.y <= arg_3_0.min.y then
				var_3_2.anim = nil

				Destroy(var_3_2.tf)
				table.remove(arg_3_0.butterflys, iter_3_1)
			elseif var_3_2.removeTime and var_3_2.removeTime > 0 then
				var_3_2.removeTime = var_3_2.removeTime - LaunchBallGameVo.deltaTime

				if var_3_2.removeTime < 0 then
					var_3_2.removeTime = nil
					var_3_2.removeFlag = true
				end
			end
		end
	end

	if arg_3_0.amuletEFs and #arg_3_0.amuletEFs > 0 then
		for iter_3_2 = #arg_3_0.amuletEFs, 1, -1 do
			local var_3_4 = arg_3_0.amuletEFs[iter_3_2]

			if var_3_4.removeTime and var_3_4.removeTime > 0 then
				var_3_4.removeTime = var_3_4.removeTime - LaunchBallGameVo.deltaTime

				if var_3_4.removeTime <= 0 then
					table.remove(arg_3_0.amuletEFs, iter_3_2)
					arg_3_0:returnAmulete(var_3_4, arg_3_0.amuletEFPool)
				end
			end
		end
	end
end

function var_0_0.getFireAmulet(arg_4_0)
	return arg_4_0._amuletFires
end

function var_0_0.removeFireAmulet(arg_5_0, arg_5_1)
	if arg_5_0._amuletFires and #arg_5_0._amuletFires > 0 then
		for iter_5_0 = #arg_5_0._amuletFires, 1, -1 do
			local var_5_0 = arg_5_0._amuletFires[iter_5_0]

			if var_5_0 then
				table.remove(arg_5_0._amuletFires, iter_5_0)
				arg_5_0:returnAmulete(var_5_0, arg_5_0.amuletLPool)
			end
		end
	end
end

var_0_0.fireIndex = 0

function var_0_0.getAmulete(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0
	local var_6_1
	local var_6_2
	local var_6_3
	local var_6_4 = arg_6_0._content

	if arg_6_1 == var_0_10 then
		var_6_1 = arg_6_0.amuletLPool
		var_6_2 = arg_6_0._amuletLTpl
		var_6_3 = Vector2(0, var_0_15)
	elseif arg_6_1 == var_0_9 then
		var_6_1 = arg_6_0.amuletSPool
		var_6_2 = arg_6_0._amuletSTpl
		var_6_3 = Vector2(0, var_0_16)
		var_6_4 = arg_6_0._sContent
	elseif arg_6_1 == var_0_11 then
		var_6_1 = arg_6_0.amuletEFPool
		var_6_2 = arg_6_0._amuletEfTpl
		var_6_3 = Vector2(0, 0)
	end

	if not var_6_1 then
		return
	end

	for iter_6_0 = 1, #var_6_1 do
		var_6_0 = var_6_0 or table.remove(var_6_1, iter_6_0)
	end

	if not var_6_0 then
		local var_6_5 = tf(instantiate(var_6_2))
		local var_6_6 = findTF(var_6_5, "ad/anim")
		local var_6_7 = GetComponent(findTF(var_6_5, "ad/anim"), typeof(Animator))

		setParent(var_6_5, var_6_4)

		var_6_0 = {
			tf = var_6_5,
			type = arg_6_1,
			anim = var_6_7,
			animTf = var_6_6
		}
	end

	var_6_0.angle = nil
	var_6_0.fire = nil

	setActive(var_6_0.tf, true)

	var_6_0.tf.anchoredPosition = var_6_3
	var_6_0.anim.runtimeAnimatorController = arg_6_0:getAnimator(arg_6_1, arg_6_2)
	var_6_0.tf.name = arg_6_1 .. "_" .. var_0_23[arg_6_2].name
	var_6_0.color = arg_6_2
	findTF(var_6_0.tf, "ad").localRotation = Quaternion.Euler(0, 0, 0)
	var_6_0.removeFlag = false

	if arg_6_1 == var_0_10 then
		var_6_0.effectTime = var_0_21
		var_6_0.effectIndex = 1
		var_6_0[LaunchBallGameConst.amulet_buff_back] = false
		var_6_0.concentrate = false
		var_6_0.fireIndex = var_0_0.fireIndex
		var_6_0.overFlag = false
		var_6_0.overCount = 0
		var_0_0.fireIndex = var_0_0.fireIndex + 1
	elseif arg_6_1 == var_0_9 then
		-- block empty
	elseif arg_6_1 == var_0_11 then
		var_6_0.removeTime = var_0_22
	end

	return var_6_0
end

function var_0_0.returnAmulete(arg_7_0, arg_7_1, arg_7_2)
	setActive(arg_7_1.tf, false)
	table.insert(arg_7_2, arg_7_1)
end

function var_0_0.getColor(arg_8_0)
	return arg_8_0.amuletL.color
end

function var_0_0.fireAmulet(arg_9_0)
	if arg_9_0.amuletL then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(LaunchBallGameVo.SFX_FIRE)

		arg_9_0.amuletPos.x = math.cos(arg_9_0.rad) * var_0_15
		arg_9_0.amuletPos.y = math.sin(arg_9_0.rad) * var_0_15
		arg_9_0.amuletL.tf.anchoredPosition = arg_9_0.amuletPos
		arg_9_0.amuletL.angle = arg_9_0.angle
		arg_9_0.amuletL.rad = arg_9_0.rad
		arg_9_0.amuletL.speed = Vector2(math.cos(arg_9_0.amuletL.rad) * var_0_17, math.sin(arg_9_0.amuletL.rad) * var_0_17)

		arg_9_0.amuletL.anim:Play("L_Fire")

		findTF(arg_9_0.amuletL.tf, "ad").localEulerAngles = Vector3(0, 0, arg_9_0.angle + var_0_18)

		if arg_9_0.concentrateTime then
			arg_9_0.amuletL.concentrate = true
			arg_9_0.concentrateTime = arg_9_0.concentrateTime - 1

			if arg_9_0.concentrateTime <= 0 then
				arg_9_0.concentrateTime = nil
			end
		end

		table.insert(arg_9_0._amuletFires, arg_9_0.amuletL)
		arg_9_0:setAmuletL(nil)
	end
end

function var_0_0.randomFireAmulet(arg_10_0, arg_10_1)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(LaunchBallGameVo.SFX_FIRE)

	local var_10_0 = arg_10_0:getAmulete(var_0_10, arg_10_0:getRandomAmuletType())

	for iter_10_0, iter_10_1 in pairs(arg_10_1) do
		var_10_0[iter_10_0] = iter_10_1
	end

	local var_10_1 = math.random(1, 360)
	local var_10_2 = math.deg2Rad * var_10_1

	var_10_0.tf.anchoredPosition = Vector2(0, 0)
	var_10_0.rad = arg_10_0.rad
	var_10_0.speed = Vector2(math.cos(var_10_2) * var_0_17, math.sin(var_10_2) * var_0_17)

	var_10_0.anim:Play("L_Fire")

	findTF(var_10_0.tf, "ad").localEulerAngles = Vector3(0, 0, var_10_1 + var_0_18)

	table.insert(arg_10_0._amuletFires, var_10_0)
end

function var_0_0.setAmuletL(arg_11_0, arg_11_1)
	arg_11_0.amuletL = arg_11_1
	LaunchBallGameVo.amulet = arg_11_0.amuletL
end

function var_0_0.createEF(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_0:getAmulete(var_0_11, arg_12_1.color)

	arg_12_1.effectIndex = arg_12_1.effectIndex + 1

	local var_12_1 = arg_12_1.effectIndex % var_0_12 + 1
	local var_12_2 = var_0_13[var_12_1].anim_name
	local var_12_3 = arg_12_1.tf.anchoredPosition

	var_12_0.tf.anchoredPosition = var_12_3

	local var_12_4 = math.cos(arg_12_1.rad)
	local var_12_5 = math.sin(arg_12_1.rad)
	local var_12_6 = var_0_13[var_12_1].offset.x
	local var_12_7 = var_0_13[var_12_1].offset.y
	local var_12_8 = var_12_4 * var_12_6 - var_12_5 * var_12_7
	local var_12_9 = var_12_4 * var_12_7 + var_12_5 * var_12_6

	findTF(var_12_0.tf, "ad").anchoredPosition = Vector2(var_12_8, var_12_9)

	var_12_0.anim:Play(var_12_2)
	table.insert(arg_12_0.amuletEFs, var_12_0)
end

function var_0_0.getRandomAmuletType(arg_13_0)
	if not LaunchBallGameVo.enemyColors or #LaunchBallGameVo.enemyColors == 0 then
		return var_0_8[math.random(1, #var_0_8)]
	else
		return LaunchBallGameVo.enemyColors[math.random(1, #LaunchBallGameVo.enemyColors)]
	end
end

function var_0_0.getAnimator(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0

	if arg_14_1 == var_0_10 then
		var_14_0 = arg_14_0.amuletLAnimators
	elseif arg_14_1 == var_0_9 then
		var_14_0 = arg_14_0.amuletSAnimators
	elseif arg_14_1 == var_0_11 then
		var_14_0 = arg_14_0.amuletEFAnimators
	end

	for iter_14_0 = 1, #var_14_0 do
		if var_14_0[iter_14_0].type == arg_14_2 then
			return var_14_0[iter_14_0].animator
		end
	end
end

function var_0_0.getAmuletPos(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = math.cos(arg_15_2)
	local var_15_1 = math.sin(arg_15_2)
	local var_15_2 = var_15_0 * arg_15_1
	local var_15_3 = var_15_1 * arg_15_1

	return Vector2(var_15_2, var_15_3)
end

function var_0_0.getAngle(arg_16_0)
	return arg_16_0.angle
end

function var_0_0.eventCall(arg_17_0, arg_17_1, arg_17_2)
	if arg_17_1 == LaunchBallGameScene.PLAYING_CHANGE then
		arg_17_0.isPlaying = arg_17_2
	elseif arg_17_1 == LaunchBallGameScene.FIRE_AMULET then
		arg_17_0:fireAmulet()
	elseif arg_17_1 == LaunchBallGameScene.RANDOM_FIRE then
		local var_17_0 = arg_17_2.num
		local var_17_1 = arg_17_2.data

		for iter_17_0 = 1, var_17_0 do
			arg_17_0:randomFireAmulet(var_17_1)
		end
	elseif arg_17_1 == LaunchBallGameScene.CHANGE_AMULET then
		if arg_17_0.changeTime and LaunchBallGameVo.gameStepTime - arg_17_0.changeTime < 1 then
			return
		end

		if arg_17_0.amuletL then
			arg_17_0.changeTime = LaunchBallGameVo.gameStepTime

			arg_17_0:returnAmulete(arg_17_0.amuletL, arg_17_0.amuletLPool)
			arg_17_0:setAmuletL(nil)
		end
	elseif arg_17_1 == LaunchBallGameScene.CONCENTRATE_TRIGGER then
		arg_17_0.concentrateTime = arg_17_2.time
	elseif arg_17_1 == LaunchBallGameScene.SLEEP_TIME_TRIGGER then
		print("创建一个小蝴蝶")

		local var_17_2 = arg_17_0:createButterfly()
	end
end

function var_0_0.getButterfly(arg_18_0)
	return arg_18_0.butterflys
end

function var_0_0.createButterfly(arg_19_0)
	local var_19_0 = tf(instantiate(arg_19_0._butterflyTpl))
	local var_19_1 = GetComponent(findTF(var_19_0, "ad/anim"), typeof(Animator))

	var_19_0.anchoredPosition = Vector2(math.random(1, 20), math.random(1, 20))

	local var_19_2 = math.random(1, 360)
	local var_19_3 = math.deg2Rad * var_19_2
	local var_19_4 = Vector2(math.cos(var_19_3) * var_0_14, math.sin(var_19_3) * var_0_14)
	local var_19_5 = 3
	local var_19_6 = var_19_4.x > 0 and -1 * var_19_5 or 1 * var_19_5

	findTF(var_19_0, "ad/anim").localScale = Vector3(var_19_6, var_19_5, var_19_5)

	table.insert(arg_19_0.butterflys, {
		tf = var_19_0,
		anim = var_19_1,
		speed = var_19_4
	})
	setParent(var_19_0, arg_19_0._content)
	setActive(var_19_0, true)
end

function var_0_0.clear(arg_20_0)
	arg_20_0:clearAmulet()
end

function var_0_0.clearAmulet(arg_21_0)
	if arg_21_0.amuletL then
		arg_21_0:returnAmulete(arg_21_0.amuletL, arg_21_0.amuletLPool)
		arg_21_0:setAmuletL(nil)
	end

	if arg_21_0.amuletS then
		arg_21_0:returnAmulete(arg_21_0.amuletS, arg_21_0.amuletSPool)

		arg_21_0.amuletS = nil
	end

	if #arg_21_0.amuletEFs > 0 then
		for iter_21_0 = #arg_21_0.amuletEFs, 1, -1 do
			local var_21_0 = table.remove(arg_21_0.amuletEFs, iter_21_0)

			arg_21_0:returnAmulete(var_21_0, arg_21_0.amuletEFPool)
		end
	end

	if arg_21_0.butterflys and #arg_21_0.butterflys > 0 then
		for iter_21_1 = #arg_21_0.butterflys, 1, -1 do
			local var_21_1 = arg_21_0.butterflys[iter_21_1].tf

			Destroy(arg_21_0.butterflys[iter_21_1].tf)
		end

		arg_21_0.butterflys = {}
	end
end

return var_0_0
