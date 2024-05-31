local var_0_0 = class("PokeMoleView", import("..BaseMiniGameView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = {
	1000,
	230
}
local var_0_5 = {
	300,
	100
}
local var_0_6 = "backyard"
local var_0_7 = "event:/ui/jida"
local var_0_8 = "event:/ui/quanji"
local var_0_9 = "event:/ui/baozhaxiaoshi"
local var_0_10 = ""
local var_0_11 = ""
local var_0_12 = "event:/ui/ddldaoshu2"
local var_0_13 = 0.5
local var_0_14 = 90
local var_0_15 = {
	{
		speed = 60,
		type = 1,
		enable_time = 1,
		life = 1,
		score = 100,
		damage_time = 1
	},
	{
		speed = 65,
		type = 2,
		enable_time = 1,
		life = 1,
		score = 150,
		damage_time = 1
	},
	{
		speed = 50,
		type = 3,
		enable_time = 2,
		life = 2,
		score = 200,
		damage_time = 1
	},
	{
		speed = 55,
		type = 4,
		enable_time = 1,
		life = 1,
		score = 150,
		damage_time = 1
	}
}
local var_0_16 = {
	level_up_time = {
		0,
		20,
		40,
		60,
		80
	},
	enemy_apear_time = {
		2.5,
		2,
		1.5,
		1.5,
		1
	},
	enemy_max = {
		5,
		6,
		7,
		8,
		8
	},
	enemy_amounts = {
		{
			70,
			30
		},
		{
			70,
			30
		},
		{
			70,
			40
		},
		{
			70,
			40,
			20
		},
		{
			70,
			50,
			20
		}
	}
}
local var_0_17 = 3
local var_0_18 = {
	1,
	2,
	3
}
local var_0_19 = 10
local var_0_20 = 10

local function var_0_21(arg_1_0, arg_1_1)
	local var_1_0 = {
		ctor = function(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._callback = arg_1_1
			arg_2_0._animator = GetComponent(arg_2_0._tf, typeof(Animator))
			arg_2_0._attakeCount = 0
			arg_2_0._attakeCd = 0
			arg_2_0._specialTime = 0
			arg_2_0._specialCount = 0
			arg_2_0.atkCollider = GetComponent(findTF(arg_2_0._tf, "atkCollider"), typeof(BoxCollider2D))
			arg_2_0.specialCollider = GetComponent(findTF(arg_2_0._tf, "specialCollider"), typeof(BoxCollider2D))

			local var_2_0 = GetComponent(arg_2_0._tf, typeof(DftAniEvent))

			var_2_0:SetStartEvent(function()
				return
			end)
			var_2_0:SetTriggerEvent(function()
				if arg_2_0._callback then
					local var_4_0 = arg_2_0:getColliderData()

					arg_2_0._callback(var_4_0)

					if arg_2_0:getSpecialState() then
						pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_8)
					end
				end
			end)
			var_2_0:SetEndEvent(function()
				return
			end)
		end,
		getColliderData = function(arg_6_0)
			local var_6_0

			if arg_6_0:getSpecialState() then
				var_6_0 = arg_6_0.specialCollider
			else
				var_6_0 = arg_6_0.atkCollider
			end

			local var_6_1 = var_6_0.bounds.max.x - var_6_0.bounds.min.x
			local var_6_2 = var_6_0.bounds.max.y - var_6_0.bounds.min.y

			return {
				pos = var_6_0.bounds.min,
				boundsLength = {
					width = var_6_1,
					height = var_6_2
				},
				damage = arg_6_0:getDamage()
			}
		end,
		atk = function(arg_7_0)
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_7)
			arg_7_0._animator:SetTrigger("atk")

			arg_7_0._attakeCd = var_0_13
		end,
		specialAtk = function(arg_8_0)
			arg_8_0._animator:SetTrigger("special")

			arg_8_0._attakeCd = var_0_13
		end,
		getDamage = function(arg_9_0)
			if arg_9_0._specialTime > 0 then
				return 3
			end

			return 1
		end,
		reset = function(arg_10_0)
			arg_10_0._animator:SetTrigger("reset")
		end,
		setActive = function(arg_11_0, arg_11_1)
			SetActive(arg_11_0._tf, arg_11_1)
		end,
		setParent = function(arg_12_0, arg_12_1, arg_12_2)
			SetParent(arg_12_0._tf, arg_12_1)
			arg_12_0:setActive(arg_12_2)
		end,
		attakeAble = function(arg_13_0)
			return arg_13_0._attakeCd == 0
		end,
		moveTo = function(arg_14_0, arg_14_1)
			arg_14_1.y = arg_14_1.y + 100
			arg_14_0._tf.anchoredPosition = arg_14_1
		end,
		attakeCount = function(arg_15_0, arg_15_1)
			arg_15_0._attakeCount = arg_15_0._attakeCount + arg_15_1 * 4

			if arg_15_0._attakeCount > 8 then
				arg_15_0._attakeCount = 8
			end

			if arg_15_0._attakeCount > 0 then
				arg_15_0._animator.speed = 0
			end
		end,
		addSpecialCount = function(arg_16_0, arg_16_1)
			if arg_16_0._specialTime == 0 then
				arg_16_0._specialCount = arg_16_0._specialCount + arg_16_1

				if arg_16_0._specialCount >= var_0_20 then
					arg_16_0._specialCount = var_0_20
				end
			end
		end,
		useSpecial = function(arg_17_0)
			if arg_17_0._specialTime and arg_17_0._specialCount >= var_0_20 then
				arg_17_0._specialCount = 0
				arg_17_0._specialTime = var_0_19

				return true
			end

			return false
		end,
		SetSiblingIndex = function(arg_18_0, arg_18_1)
			arg_18_0._tf:SetSiblingIndex(arg_18_1)
		end,
		getSpecialState = function(arg_19_0)
			return arg_19_0._specialTime > 0
		end,
		step = function(arg_20_0)
			if arg_20_0._attakeCount > 0 then
				arg_20_0._attakeCount = arg_20_0._attakeCount - 1

				if arg_20_0._attakeCount == 0 then
					arg_20_0._animator.speed = 1
				end
			end

			if arg_20_0._attakeCd > 0 then
				arg_20_0._attakeCd = arg_20_0._attakeCd - Time.deltaTime
				arg_20_0._attakeCd = arg_20_0._attakeCd < 0 and 0 or arg_20_0._attakeCd
			end

			if arg_20_0._specialTime > 0 then
				arg_20_0._specialTime = arg_20_0._specialTime - Time.deltaTime
				arg_20_0._specialTime = arg_20_0._specialTime < 0 and 0 or arg_20_0._specialTime
			end
		end,
		inSpecial = function(arg_21_0)
			return arg_21_0._specialTime > 0
		end,
		getSpecialData = function(arg_22_0)
			return arg_22_0._specialTime, arg_22_0._specialCount
		end,
		clear = function(arg_23_0)
			arg_23_0._specialTime = 0
			arg_23_0._specialCount = 0

			arg_23_0:reset()
		end,
		useAtk = function(arg_24_0)
			if arg_24_0:inSpecial() then
				arg_24_0:specialAtk()
			else
				arg_24_0:atk()
			end
		end
	}

	var_1_0:ctor()

	return var_1_0
end

local function var_0_22(arg_25_0, arg_25_1)
	local var_25_0 = {
		ctor = function(arg_26_0)
			arg_26_0.playerTpl = arg_25_0
			arg_26_0.sceneTf = arg_25_1
			arg_26_0._playerPos = findTF(arg_26_0.sceneTf, "playerPos")
			arg_26_0.uiCam = GameObject.Find("UICamera"):GetComponent("Camera")
			arg_26_0.dragDelegate = GetOrAddComponent(findTF(arg_26_0.sceneTf, "clickBounds"), "EventTriggerListener")
			arg_26_0.dragDelegate.enabled = true

			arg_26_0.dragDelegate:AddPointDownFunc(function(arg_27_0, arg_27_1)
				if arg_26_0.player and arg_26_0.player:attakeAble() then
					local var_27_0 = arg_26_0.uiCam:ScreenToWorldPoint(arg_27_1.pressPosition)
					local var_27_1 = arg_26_0._playerPos:InverseTransformPoint(var_27_0)

					arg_26_0.player:moveTo(var_27_1)
					arg_26_0.player:reset()
					arg_26_0.player:useAtk()
				end
			end)
		end,
		createPlayer = function(arg_28_0)
			if arg_28_0.player == nil then
				arg_28_0.player = var_0_21(tf(Instantiate(arg_28_0.playerTpl)), function(arg_29_0)
					arg_28_0:playerActHand(arg_29_0)
				end)

				arg_28_0.player:setParent(arg_28_0._playerPos, true)
			end
		end,
		playerActHand = function(arg_30_0, arg_30_1)
			if arg_30_0.playerHandle then
				arg_30_0.playerHandle(arg_30_1)
			end
		end,
		setPlayerHandle = function(arg_31_0, arg_31_1)
			arg_31_0.playerHandle = arg_31_1
		end,
		step = function(arg_32_0)
			if arg_32_0.player then
				arg_32_0.player:step()
			end
		end,
		getSpecialData = function(arg_33_0)
			if arg_33_0.player then
				return arg_33_0.player:getSpecialData()
			end

			return nil, nil
		end,
		useSpecial = function(arg_34_0)
			if arg_34_0.player then
				return arg_34_0.player:useSpecial()
			end
		end,
		attakeCount = function(arg_35_0, arg_35_1)
			if arg_35_0.player then
				arg_35_0.player:attakeCount(arg_35_1)
			end
		end,
		addSpecialCount = function(arg_36_0, arg_36_1)
			if arg_36_0.player then
				arg_36_0.player:addSpecialCount(arg_36_1)
			end
		end,
		clear = function(arg_37_0)
			if arg_37_0.player then
				arg_37_0.player:clear()
			end
		end
	}

	var_25_0:ctor()

	return var_25_0
end

local function var_0_23(arg_38_0, arg_38_1)
	local var_38_0 = {
		ctor = function(arg_39_0)
			arg_39_0._tf = arg_38_0
			arg_39_0._data = arg_38_1
			arg_39_0._life = 0
			arg_39_0._enable = false
			arg_39_0._attakeAble = false
			arg_39_0._animator = GetComponent(arg_39_0._tf, typeof(Animator))
			arg_39_0._boxCollider = GetComponent(arg_39_0._tf, "BoxCollider2D")

			local var_39_0 = GetComponent(arg_39_0._tf, typeof(DftAniEvent))

			var_39_0:SetStartEvent(function()
				if arg_39_0._callback then
					arg_39_0._callback(var_0_3)
				end
			end)
			var_39_0:SetTriggerEvent(function()
				if arg_39_0._callback then
					arg_39_0._callback(var_0_2)
				end
			end)
			var_39_0:SetEndEvent(function()
				arg_39_0._enable = false

				if arg_39_0._callback then
					arg_39_0._callback(var_0_1)
				end
			end)
		end,
		setHandle = function(arg_43_0, arg_43_1)
			arg_43_0._callback = arg_43_1
		end,
		getSpeed = function(arg_44_0)
			return arg_44_0._data.speed
		end,
		step = function(arg_45_0)
			if arg_45_0._enableTime > 0 then
				arg_45_0._enableTime = arg_45_0._enableTime - Time.deltaTime

				if arg_45_0._enableTime < 0 then
					arg_45_0._enable = true
					arg_45_0._enableTime = 0
				end
			end
		end,
		apear = function(arg_46_0)
			arg_46_0._animator:SetTrigger("pop")

			arg_46_0._enableTime = math.random() * arg_46_0._data.enable_time + 0.5
			arg_46_0._life = arg_46_0._data.life
			arg_46_0._attakeAble = true
		end,
		stop = function(arg_47_0)
			arg_47_0._animator:SetBool("stop", true)
		end,
		damage = function(arg_48_0, arg_48_1)
			arg_48_0._life = arg_48_0._life - arg_48_1

			if arg_48_0._life <= 0 then
				pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_9)
				arg_48_0:dead()
			else
				arg_48_0._animator:SetTrigger("damage")

				arg_48_0._enable = false
				arg_48_0._enableTime = arg_48_0._data.damage_time
			end
		end,
		dead = function(arg_49_0)
			arg_49_0._animator:SetTrigger("dead")

			arg_49_0._enable = false
			arg_49_0._enableTime = 0
			arg_49_0._attakeAble = false
		end,
		steal = function(arg_50_0)
			arg_50_0._animator:SetTrigger("steal")

			arg_50_0._enable = false
			arg_50_0._attakeAble = false
		end,
		move = function(arg_51_0, arg_51_1, arg_51_2)
			local var_51_0 = arg_51_0._tf.anchoredPosition

			var_51_0.x = var_51_0.x + arg_51_1
			var_51_0.y = var_51_0.y + arg_51_2
			arg_51_0._tf.anchoredPosition = var_51_0

			local var_51_1 = arg_51_0._tf.localScale

			var_51_1.x = Mathf.Abs(arg_51_0._tf.localScale.x) * -1 * Mathf.Sign(arg_51_1)
			arg_51_0._tf.localScale = var_51_1
		end,
		moveTo = function(arg_52_0, arg_52_1)
			arg_52_0._tf.anchoredPosition = arg_52_1

			local var_52_0 = arg_52_0._tf.localScale

			var_52_0.x = Mathf.Abs(arg_52_0._tf.localScale.x) * Mathf.Sign(arg_52_0._tf.localPosition.x)
			arg_52_0._tf.localScale = var_52_0
		end,
		setParent = function(arg_53_0, arg_53_1, arg_53_2)
			SetParent(arg_53_0._tf, arg_53_1)
			arg_53_0:setActive(arg_53_2)
		end,
		setActive = function(arg_54_0, arg_54_1)
			SetActive(arg_54_0._tf, arg_54_1)
		end,
		SetSiblingIndex = function(arg_55_0, arg_55_1)
			arg_55_0._tf:SetSiblingIndex(arg_55_1)
		end,
		getPosition = function(arg_56_0)
			return arg_56_0._tf.anchoredPosition
		end,
		getType = function(arg_57_0)
			return arg_57_0._data.type
		end,
		getMoveAble = function(arg_58_0)
			return isActive(arg_58_0._tf) and arg_58_0._enable
		end,
		getAttakeAble = function(arg_59_0)
			return isActive(arg_59_0._tf) and arg_59_0._attakeAble
		end,
		getBounds = function(arg_60_0)
			return arg_60_0._boxCollider.bounds
		end,
		getLife = function(arg_61_0)
			return arg_61_0._life
		end,
		getScore = function(arg_62_0)
			return arg_62_0._data.score
		end,
		getBoundLength = function(arg_63_0)
			if arg_63_0.boundsData == nil then
				local var_63_0 = arg_63_0._boxCollider.bounds.max.x - arg_63_0._boxCollider.bounds.min.x
				local var_63_1 = arg_63_0._boxCollider.bounds.max.y - arg_63_0._boxCollider.bounds.min.y

				arg_63_0.boundsData = {
					width = var_63_0,
					height = var_63_1
				}
			end

			return arg_63_0.boundsData
		end
	}

	var_38_0:ctor()

	return var_38_0
end

local function var_0_24(arg_64_0, arg_64_1, arg_64_2, arg_64_3)
	local var_64_0 = {
		ctor = function(arg_65_0)
			arg_65_0.enemysTpl = arg_64_0
			arg_65_0.sceneTf = arg_64_1
			arg_65_0.enemyPos = findTF(arg_65_0.sceneTf, "enemyPos")
			arg_65_0.createPos = findTF(arg_65_0.sceneTf, "createPos")
			arg_65_0.countsWeight = {}

			for iter_65_0 = 1, #var_0_16.enemy_amounts do
				local var_65_0 = {}
				local var_65_1 = 0
				local var_65_2 = var_0_16.enemy_amounts[iter_65_0]

				for iter_65_1 = 1, #var_65_2 do
					var_65_1 = var_65_1 + var_65_2[iter_65_1]

					table.insert(var_65_0, var_65_1)
				end

				table.insert(arg_65_0.countsWeight, var_65_0)
			end

			arg_65_0.callback = arg_64_2
			arg_65_0.callback2 = arg_64_3
			arg_65_0.enemys = {}
			arg_65_0.enemysPool = {}
			arg_65_0.apearTime = 0
			arg_65_0.stepTime = 0
			arg_65_0.level = 1
			arg_65_0.cakeLife = var_0_17
			arg_65_0.cakeTf = findTF(arg_65_0.sceneTf, "enemyPos/cake")
			arg_65_0.cakeAniamtor = GetComponent(findTF(arg_65_0.cakeTf, "image"), typeof(Animator))

			arg_65_0.cakeAniamtor:SetInteger("life", arg_65_0:getCakeLifeIndex())

			arg_65_0.cakeBox = GetComponent(arg_65_0.cakeTf, "BoxCollider2D")
			arg_65_0.cakeBoundsLength = {
				width = arg_65_0.cakeBox.bounds.max.x - arg_65_0.cakeBox.bounds.min.x,
				height = arg_65_0.cakeBox.bounds.max.y - arg_65_0.cakeBox.bounds.min.y
			}
			arg_65_0.gameScore = 0
			arg_65_0.createBounds = {}

			for iter_65_2 = 0, arg_65_0.createPos.childCount - 1 do
				table.insert(arg_65_0.createBounds, arg_65_0.createPos:GetChild(iter_65_2))
			end
		end,
		step = function(arg_66_0)
			for iter_66_0 = #var_0_16.level_up_time, 1, -1 do
				if iter_66_0 > arg_66_0.level and arg_66_0.stepTime > var_0_16.level_up_time[iter_66_0] and arg_66_0.level ~= iter_66_0 then
					arg_66_0.level = iter_66_0

					print("level up :" .. arg_66_0.level)

					break
				end
			end

			if arg_66_0.apearTime == 0 then
				local var_66_0 = arg_66_0:getCreateCounts()

				for iter_66_1 = 1, var_66_0 do
					if #arg_66_0.enemys < var_0_16.enemy_max[arg_66_0.level] then
						local var_66_1 = var_0_15[math.random(1, #var_0_15)]
						local var_66_2 = arg_66_0:getEnemyFromPool(var_66_1.type) or arg_66_0:createEnemy(var_66_1)

						table.insert(arg_66_0.enemys, var_66_2)
						var_66_2:setActive(true)
						var_66_2:moveTo(arg_66_0:getRandApearPosition())
						var_66_2:apear()
					end
				end

				arg_66_0.apearTime = var_0_16.enemy_apear_time[arg_66_0.level]
			end

			table.sort(arg_66_0.enemys, function(arg_67_0, arg_67_1)
				return arg_67_0:getPosition().y > arg_67_1:getPosition().y
			end)

			local var_66_3 = 0

			for iter_66_2 = #arg_66_0.enemys, 1, -1 do
				local var_66_4 = arg_66_0.enemys[iter_66_2]

				if arg_66_0.cakeTf.localPosition.y <= var_66_4:getPosition().y then
					var_66_3 = var_66_3 + 1
				end

				var_66_4:SetSiblingIndex(iter_66_2)
				var_66_4:step()

				if var_66_4:getMoveAble() then
					local var_66_5 = var_66_4:getPosition()

					if arg_66_0:checkEnemySteal(var_66_4) then
						var_66_4:steal()
					else
						local var_66_6 = Mathf.Atan2(Mathf.Abs(var_66_5.y), Mathf.Abs(var_66_5.x))
						local var_66_7 = var_66_4:getSpeed() * Mathf.Cos(var_66_6) * -Mathf.Sign(var_66_5.x)
						local var_66_8 = var_66_4:getSpeed() * Mathf.Sin(var_66_6) * -Mathf.Sign(var_66_5.y)

						var_66_4:move(var_66_7 * Time.deltaTime, var_66_8 * Time.deltaTime)
					end
				end
			end

			arg_66_0.cakeTf:SetSiblingIndex(var_66_3)

			arg_66_0.apearTime = arg_66_0.apearTime - Time.deltaTime

			if arg_66_0.apearTime < 0 then
				arg_66_0.apearTime = 0
			end

			arg_66_0.stepTime = arg_66_0.stepTime + Time.deltaTime

			arg_66_0.cakeAniamtor:SetInteger("life", arg_66_0:getCakeLifeIndex())
		end,
		getCreateCounts = function(arg_68_0)
			local var_68_0 = arg_68_0.countsWeight[arg_68_0.level]
			local var_68_1 = math.random(1, var_68_0[#var_68_0])

			for iter_68_0 = 1, #var_68_0 do
				if var_68_1 <= var_68_0[iter_68_0] then
					return iter_68_0
				end
			end

			return 1
		end,
		checkEnemySteal = function(arg_69_0, arg_69_1)
			local var_69_0 = arg_69_1:getBounds().min
			local var_69_1 = arg_69_1:getBoundLength()
			local var_69_2 = arg_69_0.cakeBox.bounds.min
			local var_69_3 = arg_69_0.cakeBoundsLength

			return arg_69_0:checkRectCollider(var_69_0, var_69_2, var_69_1, var_69_3)
		end,
		checkRectCollider = function(arg_70_0, arg_70_1, arg_70_2, arg_70_3, arg_70_4)
			local var_70_0 = arg_70_1.x
			local var_70_1 = arg_70_1.y
			local var_70_2 = arg_70_3.width
			local var_70_3 = arg_70_3.height
			local var_70_4 = arg_70_2.x
			local var_70_5 = arg_70_2.y
			local var_70_6 = arg_70_4.width
			local var_70_7 = arg_70_4.height

			if var_70_4 <= var_70_0 and var_70_0 >= var_70_4 + var_70_6 then
				return false
			elseif var_70_0 <= var_70_4 and var_70_4 >= var_70_0 + var_70_2 then
				return false
			elseif var_70_5 <= var_70_1 and var_70_1 >= var_70_5 + var_70_7 then
				return false
			elseif var_70_1 <= var_70_5 and var_70_5 >= var_70_1 + var_70_3 then
				return false
			else
				return true
			end
		end,
		createEnemy = function(arg_71_0, arg_71_1)
			local var_71_0 = tf(Instantiate(arg_71_0.enemysTpl[arg_71_1.type]))
			local var_71_1 = var_0_23(var_71_0, arg_71_1)

			var_71_1:setHandle(function(arg_72_0)
				arg_71_0:enemyEventHandle(arg_72_0, var_71_1)
			end)
			var_71_1:setParent(arg_71_0.enemyPos, true)

			return var_71_1
		end,
		getEnemyFromPool = function(arg_73_0, arg_73_1)
			for iter_73_0 = 1, #arg_73_0.enemysPool do
				local var_73_0 = arg_73_0.enemysPool[iter_73_0]

				if var_73_0:getType() == arg_73_1 then
					table.remove(arg_73_0.enemysPool, iter_73_0)

					return var_73_0
				end
			end

			return nil
		end,
		removeEnemy = function(arg_74_0, arg_74_1)
			for iter_74_0 = #arg_74_0.enemys, 1, -1 do
				if arg_74_0.enemys[iter_74_0] == arg_74_1 then
					table.remove(arg_74_0.enemys, iter_74_0)
				end
			end

			arg_74_1:setActive(false)
			table.insert(arg_74_0.enemysPool, arg_74_1)
		end,
		getRandApearPosition = function(arg_75_0)
			local var_75_0 = math.random(1, #arg_75_0.createBounds)
			local var_75_1 = arg_75_0.createBounds[var_75_0]
			local var_75_2 = math.random() * (var_75_1.sizeDelta.x / 2) * (math.random() < 0.5 and 1 or -1)
			local var_75_3 = math.random() * (var_75_1.sizeDelta.y / 2) * (math.random() < 0.5 and 1 or -1)
			local var_75_4 = var_75_1:TransformPoint(var_75_2, var_75_3, 0)

			return (arg_75_0.enemyPos:InverseTransformPoint(var_75_4.x, var_75_4.y, var_75_4.z))
		end,
		enemyEventHandle = function(arg_76_0, arg_76_1, arg_76_2)
			if arg_76_1 == var_0_2 then
				arg_76_0.cakeLife = arg_76_0.cakeLife - 1

				if arg_76_0.callback2 then
					arg_76_0.callback2()
				end

				if arg_76_0.cakeLife <= 0 and arg_76_0.callback then
					arg_76_0.callback()
				end

				arg_76_0.cakeAniamtor:SetInteger("life", arg_76_0:getCakeLifeIndex())
			elseif arg_76_1 == var_0_1 then
				arg_76_0.gameScore = arg_76_0.gameScore + arg_76_2:getScore()

				arg_76_0:removeEnemy(arg_76_2)
			else
				arg_76_0:removeEnemy(arg_76_2)
			end
		end,
		playerActAttake = function(arg_77_0, arg_77_1)
			local var_77_0 = arg_77_1.pos
			local var_77_1 = arg_77_1.boundsLength
			local var_77_2 = arg_77_1.damage
			local var_77_3 = 0
			local var_77_4 = 0

			for iter_77_0 = 1, #arg_77_0.enemys do
				local var_77_5 = arg_77_0.enemys[iter_77_0]

				if var_77_5:getAttakeAble() then
					local var_77_6 = var_77_5:getBounds().min
					local var_77_7 = var_77_5:getBoundLength()

					if arg_77_0:checkRectCollider(var_77_6, var_77_0, var_77_7, var_77_1) then
						var_77_5:damage(var_77_2)

						var_77_3 = var_77_3 + 1

						if var_77_5:getLife() == 0 then
							var_77_4 = var_77_4 + 1
						end
					end
				end
			end

			return var_77_3, var_77_4
		end,
		clear = function(arg_78_0)
			arg_78_0.stepTime = 0

			for iter_78_0 = #arg_78_0.enemys, 1, -1 do
				local var_78_0 = table.remove(arg_78_0.enemys, iter_78_0)

				var_78_0:setActive(false)
				table.insert(arg_78_0.enemysPool, var_78_0)
			end

			arg_78_0.cakeLife = var_0_17
			arg_78_0.gameScore = 0
			arg_78_0.level = 1
		end,
		getCakeLife = function(arg_79_0)
			return arg_79_0.cakeLife
		end,
		getCakeLifeIndex = function(arg_80_0)
			for iter_80_0 = #var_0_18, 1, -1 do
				if arg_80_0.cakeLife >= var_0_18[iter_80_0] then
					return iter_80_0
				end
			end

			return 0
		end,
		getScore = function(arg_81_0)
			return arg_81_0.gameScore
		end
	}

	var_64_0:ctor()

	return var_64_0
end

local function var_0_25(arg_82_0, arg_82_1, arg_82_2)
	local var_82_0 = {
		ctor = function(arg_83_0)
			arg_83_0.playerController = arg_82_0
			arg_83_0.enemyController = arg_82_1
			arg_83_0.callback = arg_82_2

			arg_83_0.playerController:setPlayerHandle(function(arg_84_0)
				local var_84_0, var_84_1 = arg_83_0.enemyController:playerActAttake(arg_84_0)

				if var_84_0 > 0 then
					arg_83_0.playerController:attakeCount(var_84_0)
				end

				if var_84_1 > 0 then
					arg_83_0.playerController:addSpecialCount(var_84_1)

					if arg_83_0.callback then
						arg_83_0.callback()
					end
				end
			end)
		end
	}

	var_82_0:ctor()

	return var_82_0
end

local var_0_26 = "role type loop"
local var_0_27 = "role type normal"

local function var_0_28(arg_85_0, arg_85_1)
	local var_85_0 = {
		ctor = function(arg_86_0)
			arg_86_0.playerController = arg_85_1
			arg_86_0.roleTfs = arg_85_0
			arg_86_0.roleDatas = {}

			for iter_86_0 = 1, #arg_86_0.roleTfs do
				local var_86_0 = {
					animator = GetComponent(arg_86_0.roleTfs[iter_86_0], typeof(Animator))
				}

				if iter_86_0 == 2 or iter_86_0 == 3 then
					var_86_0.type = var_0_26
					var_86_0.loop_time = {
						3,
						3
					}
					var_86_0.time = 0
				else
					var_86_0.type = var_0_27
				end

				table.insert(arg_86_0.roleDatas, var_86_0)
			end
		end,
		step = function(arg_87_0)
			local var_87_0 = arg_87_0.playerController:getSpecialData()

			for iter_87_0 = 1, #arg_87_0.roleDatas do
				local var_87_1 = arg_87_0.roleDatas[iter_87_0]

				if var_87_1.type == var_0_26 then
					if var_87_1.time == 0 then
						var_87_1.animator:SetTrigger("loop")

						var_87_1.time = math.random() * var_87_1.loop_time[1] + var_87_1.loop_time[2]
					else
						var_87_1.time = var_87_1.time - Time.deltaTime

						if var_87_1.time < 0 then
							var_87_1.time = 0
						end
					end
				end

				if var_87_1.special and var_87_0 == 0 then
					var_87_1.animator:SetTrigger("reset")

					var_87_1.special = false
				end
			end
		end,
		special = function(arg_88_0)
			for iter_88_0 = 1, #arg_88_0.roleDatas do
				local var_88_0 = arg_88_0.roleDatas[iter_88_0]

				var_88_0.animator:SetTrigger("special")

				var_88_0.special = true
			end
		end,
		fail = function(arg_89_0)
			for iter_89_0 = 1, #arg_89_0.roleDatas do
				arg_89_0.roleDatas[iter_89_0].animator:SetTrigger("fail")
			end
		end,
		reset = function(arg_90_0)
			for iter_90_0 = 1, #arg_90_0.roleDatas do
				arg_90_0.roleDatas[iter_90_0].animator:SetTrigger("reset")
			end
		end
	}

	var_85_0:ctor()

	return var_85_0
end

function var_0_0.getUIName(arg_91_0)
	return "PokeMoleGameUI"
end

function var_0_0.getBGM(arg_92_0)
	return var_0_6
end

function var_0_0.didEnter(arg_93_0)
	arg_93_0:initData()
	arg_93_0:initUI()
end

function var_0_0.initData(arg_94_0)
	arg_94_0.settlementFlag = false
	arg_94_0.gameStartFlag = false

	local var_94_0 = Application.targetFrameRate or 60

	arg_94_0.timer = Timer.New(function()
		arg_94_0:onTimer()
	end, 1 / var_94_0, -1, true)
end

function var_0_0.initUI(arg_96_0)
	arg_96_0.clickMask = findTF(arg_96_0._tf, "clickMask")
	arg_96_0.countUI = findTF(arg_96_0._tf, "pop/CountUI")
	arg_96_0.countAnimator = GetComponent(findTF(arg_96_0.countUI, "count"), typeof(Animator))
	arg_96_0.countDft = GetComponent(findTF(arg_96_0.countUI, "count"), typeof(DftAniEvent))

	arg_96_0.countDft:SetTriggerEvent(function()
		return
	end)
	arg_96_0.countDft:SetEndEvent(function()
		setActive(arg_96_0.countUI, false)
		arg_96_0:gameStart()
	end)

	arg_96_0.leaveUI = findTF(arg_96_0._tf, "pop/LeaveUI")

	onButton(arg_96_0, findTF(arg_96_0.leaveUI, "ad/btnOk"), function()
		arg_96_0:resumeGame()
		arg_96_0:onGameOver()
	end, SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.leaveUI, "ad/btnCancel"), function()
		arg_96_0:resumeGame()
	end, SFX_CANCEL)

	arg_96_0.pauseUI = findTF(arg_96_0._tf, "pop/pauseUI")

	onButton(arg_96_0, findTF(arg_96_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_96_0.pauseUI, false)
		arg_96_0:resumeGame()
	end, SFX_CANCEL)

	arg_96_0.settlementUI = findTF(arg_96_0._tf, "pop/SettleMentUI")

	onButton(arg_96_0, findTF(arg_96_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_96_0.settlementUI, false)
		arg_96_0:openMenuUI()
	end, SFX_CANCEL)

	arg_96_0.menuUI = findTF(arg_96_0._tf, "pop/menuUI")

	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnBack"), function()
		arg_96_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.securitycake_help.tip
		})
	end, SFX_CANCEL)
	onButton(arg_96_0, findTF(arg_96_0.menuUI, "btnStart"), function()
		setActive(arg_96_0.menuUI, false)
		arg_96_0:readyStart()
	end, SFX_CANCEL)

	arg_96_0.gameUI = findTF(arg_96_0._tf, "ui/gameUI")
	arg_96_0.textTime = findTF(arg_96_0.gameUI, "time")
	arg_96_0.textScore = findTF(arg_96_0.gameUI, "score")
	arg_96_0.hearts = {}

	local var_96_0 = 3

	for iter_96_0 = 1, var_96_0 do
		local var_96_1 = findTF(arg_96_0.gameUI, "heart" .. iter_96_0 .. "/img")

		table.insert(arg_96_0.hearts, var_96_1)
	end

	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnStop"), function()
		arg_96_0:stopGame()
		setActive(arg_96_0.pauseUI, true)
	end)
	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnLeave"), function()
		arg_96_0:stopGame()
		setActive(arg_96_0.leaveUI, true)
	end)

	arg_96_0.specialSlider = GetComponent(findTF(arg_96_0.gameUI, "btnSpecial/Slider"), typeof(Slider))
	arg_96_0.touchSlider = findTF(arg_96_0.specialSlider, "touch")
	arg_96_0.specialEffect = findTF(arg_96_0.gameUI, "btnSpecial/baoweidangao_extiao")
	arg_96_0.arrowTf = findTF(arg_96_0.gameUI, "btnSpecial/arrow")

	onButton(arg_96_0, findTF(arg_96_0.gameUI, "btnSpecial"), function()
		if arg_96_0.playerController and arg_96_0.playerController:useSpecial() then
			arg_96_0.bgRoleController:special()
		end
	end)

	arg_96_0.sceneTf = findTF(arg_96_0._tf, "scene")
	arg_96_0.playerTpl = findTF(arg_96_0._tf, "playerTpl")
	arg_96_0.playerController = var_0_22(arg_96_0.playerTpl, arg_96_0.sceneTf)
	arg_96_0.enemyTpls = {}

	for iter_96_1 = 1, 4 do
		table.insert(arg_96_0.enemyTpls, findTF(arg_96_0._tf, "enemy" .. iter_96_1 .. "Tpl"))
	end

	arg_96_0.enemyController = var_0_24(arg_96_0.enemyTpls, arg_96_0.sceneTf, function()
		arg_96_0.bgRoleController:fail()
		arg_96_0:onGameOver()
	end, function()
		arg_96_0:gameUIUpdate()
	end)
	arg_96_0.attakeController = var_0_25(arg_96_0.playerController, arg_96_0.enemyController, function()
		arg_96_0:gameUIUpdate()
	end)

	local var_96_2 = {}
	local var_96_3 = 4

	for iter_96_2 = 1, var_96_3 do
		table.insert(var_96_2, findTF(arg_96_0._tf, "bg_background/role/role" .. iter_96_2))
	end

	arg_96_0.bgRoleController = var_0_28(var_96_2, arg_96_0.playerController)

	arg_96_0:updateMenuUI()
	arg_96_0:openMenuUI()

	if not arg_96_0.handle then
		arg_96_0.handle = UpdateBeat:CreateListener(arg_96_0.Update, arg_96_0)
	end

	UpdateBeat:AddListener(arg_96_0.handle)
end

function var_0_0.updateMenuUI(arg_112_0)
	local var_112_0 = arg_112_0:getGameUsedTimes()
	local var_112_1 = arg_112_0:getGameTimes()

	setActive(findTF(arg_112_0.menuUI, "btnStart/tip"), var_112_1 > 0)
	arg_112_0:CheckGet()
end

function var_0_0.openMenuUI(arg_113_0)
	setActive(findTF(arg_113_0._tf, "scene_front"), false)
	setActive(findTF(arg_113_0._tf, "scene_background"), false)
	setActive(findTF(arg_113_0._tf, "scene"), false)
	setActive(arg_113_0.gameUI, false)
	setActive(arg_113_0.menuUI, true)
	arg_113_0:updateMenuUI()
end

function var_0_0.showSettlement(arg_114_0)
	setActive(arg_114_0.settlementUI, true)
	GetComponent(findTF(arg_114_0.settlementUI, "ad"), typeof(Animator)):Play("settlement", -1, 0)

	local var_114_0 = arg_114_0:GetMGData():GetRuntimeData("elements")
	local var_114_1 = arg_114_0.enemyController:getScore()
	local var_114_2 = var_114_0 and #var_114_0 > 0 and var_114_0[1] or 0

	if var_114_2 <= var_114_1 then
		var_114_2 = var_114_1

		arg_114_0:StoreDataToServer({
			var_114_2
		})
	end

	local var_114_3 = findTF(arg_114_0.settlementUI, "ad/highText")
	local var_114_4 = findTF(arg_114_0.settlementUI, "ad/currentText")

	setText(var_114_3, var_114_2)
	setText(var_114_4, var_114_1)

	if arg_114_0:getGameTimes() and arg_114_0:getGameTimes() > 0 then
		arg_114_0:SendSuccess(0)
	end
end

function var_0_0.Update(arg_115_0)
	arg_115_0:AddDebugInput()
end

function var_0_0.AddDebugInput(arg_116_0)
	if arg_116_0.gameStop or arg_116_0.settlementFlag then
		return
	end

	if IsUnityEditor and Input.GetKeyDown(KeyCode.Space) and arg_116_0.playerController then
		local var_116_0 = arg_116_0.playerController:useSpecial()
	end
end

function var_0_0.CheckGet(arg_117_0)
	setActive(findTF(arg_117_0.menuUI, "got"), false)

	if arg_117_0:getUltimate() and arg_117_0:getUltimate() ~= 0 then
		setActive(findTF(arg_117_0.menuUI, "got"), true)
	end

	if arg_117_0:getUltimate() == 0 then
		if arg_117_0:getGameTotalTime() > arg_117_0:getGameUsedTimes() then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_117_0:GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_117_0.menuUI, "got"), true)
	end
end

function var_0_0.clearUI(arg_118_0)
	return
end

function var_0_0.readyStart(arg_119_0)
	setActive(arg_119_0.countUI, true)
	arg_119_0.countAnimator:Play("count")
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_12)
	arg_119_0.bgRoleController:reset()
end

function var_0_0.gameStart(arg_120_0)
	arg_120_0.gameStartFlag = true
	arg_120_0.gameStepTime = 0
	arg_120_0.gameLastTime = var_0_14

	setActive(findTF(arg_120_0._tf, "scene_front"), true)
	setActive(findTF(arg_120_0._tf, "scene_background"), true)
	setActive(findTF(arg_120_0._tf, "scene"), true)
	setActive(arg_120_0.gameUI, true)
	arg_120_0.playerController:createPlayer()
	arg_120_0:timerStart()
	arg_120_0:gameUIUpdate()
end

function var_0_0.onTimer(arg_121_0)
	arg_121_0:gameStep()
end

function var_0_0.gameStep(arg_122_0)
	arg_122_0.playerController:step()
	arg_122_0.enemyController:step()
	arg_122_0.bgRoleController:step()

	arg_122_0.gameLastTime = arg_122_0.gameLastTime - Time.deltaTime

	setText(arg_122_0.textScore, arg_122_0.enemyController:getScore())

	if arg_122_0.gameLastTime <= 0 then
		arg_122_0.gameLastTime = 0

		arg_122_0:onGameOver()
	end

	setText(arg_122_0.textTime, math.ceil(arg_122_0.gameLastTime) .. "")

	local var_122_0, var_122_1 = arg_122_0.playerController:getSpecialData()

	var_122_1 = var_122_1 or 0

	if var_122_0 > 0 then
		setSlider(arg_122_0.specialSlider, 0, 1, var_122_0 / var_0_19)
	else
		setSlider(arg_122_0.specialSlider, 0, 1, var_122_1 / var_0_20)
	end

	if var_122_1 == var_0_20 or var_122_0 > 0 then
		SetActive(arg_122_0.touchSlider, false)
		SetActive(arg_122_0.specialEffect, true)
	else
		SetActive(arg_122_0.touchSlider, true)
		SetActive(arg_122_0.specialEffect, false)
	end

	if arg_122_0.settlementFlag then
		SetActive(arg_122_0.specialEffect, false)
	end

	SetActive(arg_122_0.arrowTf, var_122_1 == var_0_20 and var_122_0 == 0)
end

function var_0_0.gameUIUpdate(arg_123_0)
	for iter_123_0 = 1, #arg_123_0.hearts do
		if iter_123_0 <= arg_123_0.enemyController:getCakeLifeIndex() then
			SetActive(arg_123_0.hearts[iter_123_0], true)
		else
			SetActive(arg_123_0.hearts[iter_123_0], false)
		end
	end

	setText(arg_123_0.textScore, arg_123_0.enemyController:getScore())
end

function var_0_0.resumeGame(arg_124_0)
	arg_124_0.gameStop = false

	setActive(arg_124_0.leaveUI, false)
	arg_124_0:timerStart()
end

function var_0_0.stopGame(arg_125_0)
	arg_125_0.gameStop = true

	arg_125_0:timerStop()
end

function var_0_0.onGameOver(arg_126_0)
	if arg_126_0.settlementFlag then
		return
	end

	arg_126_0:timerStop()

	arg_126_0.settlementFlag = true

	SetActive(arg_126_0.specialEffect, false)
	setActive(arg_126_0.clickMask, true)
	LeanTween.delayedCall(go(arg_126_0._tf), 1, System.Action(function()
		arg_126_0:showSettlement()
		arg_126_0.enemyController:clear()
		arg_126_0.playerController:clear()
		arg_126_0.bgRoleController:reset()

		arg_126_0.settlementFlag = false
		arg_126_0.gameStartFlag = false

		setActive(arg_126_0.clickMask, false)
	end))
end

function var_0_0.timerStop(arg_128_0)
	if arg_128_0.timer.running then
		arg_128_0.timer:Stop()
	end
end

function var_0_0.timerStart(arg_129_0)
	if not arg_129_0.timer.running then
		arg_129_0.timer:Start()
	end
end

function var_0_0.getGameTimes(arg_130_0)
	return arg_130_0:GetMGHubData().count
end

function var_0_0.getGameUsedTimes(arg_131_0)
	return arg_131_0:GetMGHubData().usedtime
end

function var_0_0.getUltimate(arg_132_0)
	return arg_132_0:GetMGHubData().ultimate
end

function var_0_0.getGameTotalTime(arg_133_0)
	return (arg_133_0:GetMGHubData():getConfig("reward_need"))
end

function var_0_0.onBackPressed(arg_134_0)
	return
end

function var_0_0.willExit(arg_135_0)
	if arg_135_0.handle then
		UpdateBeat:RemoveListener(arg_135_0.handle)
	end

	if arg_135_0.timer and arg_135_0.timer.running then
		arg_135_0.timer:Stop()
	end

	arg_135_0.timer = nil
end

return var_0_0
