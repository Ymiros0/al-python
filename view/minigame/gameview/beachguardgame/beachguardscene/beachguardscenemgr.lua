local var_0_0 = class("BeachGuardSceneMgr")

local function var_0_1(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		Ctor = function(arg_2_0)
			arg_2_0._tf = arg_1_0
			arg_2_0._charTpl = arg_1_1
			arg_2_0._event = arg_1_2
			arg_2_0.chars = {}
			arg_2_0.charPool = {}
			arg_2_0.gridChars = {}
			arg_2_0.enemys = {}
			arg_2_0.enemysPool = {}
			arg_2_0.content = findTF(arg_2_0._tf, "sceneContainer/scene/content")
		end,
		changeRecycles = function(arg_3_0, arg_3_1)
			arg_3_0.recycle = arg_3_1

			for iter_3_0 = #arg_3_0.chars, 1, -1 do
				arg_3_0.chars[iter_3_0]:setRecycleFlag(arg_3_1)
			end
		end,
		setGridChar = function(arg_4_0, arg_4_1, arg_4_2)
			local var_4_0 = arg_4_2:getPos()
			local var_4_1 = arg_4_0:createChar(arg_4_1)
			local var_4_2 = arg_4_0.content:InverseTransformPoint(var_4_0.position)

			var_4_1:prepareData()
			var_4_1:setParent(arg_4_0.content, true, var_4_2)
			var_4_1:setLineIndex(arg_4_2:getLineIndex())
			var_4_1:setGridIndex(arg_4_2:getIndex())
			var_4_1:setCamp(1)
			var_4_1:setRaycast(true)
			table.insert(arg_4_0.chars, var_4_1)

			return var_4_1
		end,
		createChar = function(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_0:getCharFromPool(arg_5_1)

			if not var_5_0 then
				local var_5_1 = BeachGuardConst.chars[arg_5_1]

				var_5_0 = BeachGuardChar.New(tf(instantiate(arg_5_0._charTpl)), var_5_1, arg_5_0._event)
			end

			return var_5_0
		end,
		getCharFromPool = function(arg_6_0, arg_6_1)
			for iter_6_0 = #arg_6_0.charPool, 1, -1 do
				if arg_6_0.charPool[iter_6_0]:getId() == arg_6_1 then
					return table.remove(arg_6_0.charPool, iter_6_0)
				end
			end

			return nil
		end,
		removeChar = function(arg_7_0, arg_7_1)
			for iter_7_0 = #arg_7_0.chars, 1, -1 do
				if arg_7_0.chars[iter_7_0] == arg_7_1 then
					local var_7_0 = table.remove(arg_7_0.chars, iter_7_0)

					var_7_0:clear()
					table.insert(arg_7_0.charPool, var_7_0)
				elseif arg_7_0.chars[iter_7_0]:getTarget() == arg_7_1 then
					arg_7_0.chars[iter_7_0]:setTarget(nil)
				end
			end

			for iter_7_1 = #arg_7_0.enemys, 1, -1 do
				if arg_7_0.enemys[iter_7_1] == arg_7_1 then
					local var_7_1 = table.remove(arg_7_0.enemys, iter_7_1)

					var_7_1:clear()
					table.insert(arg_7_0.charPool, var_7_1)
				elseif arg_7_0.enemys[iter_7_1]:getTarget() == arg_7_1 then
					arg_7_0.enemys[iter_7_1]:setTarget(nil)
				end
			end
		end,
		clear = function(arg_8_0)
			for iter_8_0 = #arg_8_0.chars, 1, -1 do
				local var_8_0 = table.remove(arg_8_0.chars, iter_8_0)

				var_8_0:clear()
				table.insert(arg_8_0.charPool, var_8_0)
			end

			for iter_8_1 = #arg_8_0.enemys, 1, -1 do
				local var_8_1 = table.remove(arg_8_0.enemys, iter_8_1)

				var_8_1:clear()
				table.insert(arg_8_0.charPool, var_8_1)
			end
		end,
		start = function(arg_9_0)
			for iter_9_0 = #arg_9_0.chars, 1, -1 do
				arg_9_0.chars[iter_9_0]:start()
			end

			arg_9_0.recycle = false
		end,
		step = function(arg_10_0, arg_10_1)
			for iter_10_0 = #arg_10_0.chars, 1, -1 do
				arg_10_0.chars[iter_10_0]:step(arg_10_1)
			end

			for iter_10_1 = #arg_10_0.enemys, 1, -1 do
				arg_10_0.enemys[iter_10_1]:step(arg_10_1)
			end

			arg_10_0.enemyOver = false

			for iter_10_2 = #arg_10_0.enemys, 1, -1 do
				local var_10_0 = arg_10_0.enemys[iter_10_2]

				if not var_10_0:getTarget() then
					local var_10_1 = var_10_0:getLineIndex()
					local var_10_2 = var_10_0:getPointWorld()
					local var_10_3 = var_10_0:getPos()
					local var_10_4 = arg_10_0:getCharLine(var_10_1)
					local var_10_5 = false

					for iter_10_3, iter_10_4 in ipairs(var_10_4) do
						if iter_10_4:checkCollider(var_10_2, var_10_3) and (not var_10_5 or true) then
							var_10_5 = true

							var_10_0:setTarget(iter_10_4)
						end
					end
				end

				if var_10_0:getPos().x < BeachGuardConst.enemy_over_width then
					arg_10_0.enemyOver = true
				end
			end

			for iter_10_5 = 1, #arg_10_0.chars do
				local var_10_6 = arg_10_0.chars[iter_10_5]
				local var_10_7 = var_10_6:getSkillDistance() * BeachGuardConst.part_width
				local var_10_8 = arg_10_0:getCanHitChar(var_10_6:getLineIndex(), var_10_6:getCamp())

				for iter_10_6, iter_10_7 in ipairs(var_10_8) do
					local var_10_9 = iter_10_7:getPos().x - var_10_6:getPos().x

					if var_10_9 > 0 and var_10_9 < var_10_7 then
						var_10_6:setTarget(iter_10_7)
					end
				end
			end

			arg_10_0:sortChar()
		end,
		stop = function(arg_11_0)
			for iter_11_0 = #arg_11_0.chars, 1, -1 do
				arg_11_0.chars[iter_11_0]:stop()
			end
		end,
		getLineCampChars = function(arg_12_0, arg_12_1, arg_12_2)
			local var_12_0 = {}
			local var_12_1 = {}

			if arg_12_2 == 1 then
				var_12_1 = arg_12_0.chars
			elseif arg_12_2 == 2 then
				var_12_1 = arg_12_0.enemys
			end

			for iter_12_0 = 1, #var_12_1 do
				local var_12_2 = var_12_1[iter_12_0]

				if table.contains(arg_12_1, var_12_2:getLineIndex()) then
					table.insert(var_12_0, var_12_2)
				end
			end

			return var_12_0
		end,
		getCharByCamp = function(arg_13_0, arg_13_1)
			local var_13_0 = {}

			if arg_13_1 == 1 then
				var_13_0 = arg_13_0.chars
			elseif arg_13_1 == 2 then
				var_13_0 = arg_13_0.enemys
			end

			return var_13_0
		end,
		getEnemyOver = function(arg_14_0)
			return arg_14_0.enemyOver
		end,
		getCanHitChar = function(arg_15_0, arg_15_1, arg_15_2)
			local var_15_0 = {}
			local var_15_1 = {}

			if arg_15_2 == 1 then
				var_15_1 = arg_15_0.enemys
			elseif arg_15_2 == 2 then
				var_15_1 = arg_15_0.chars
			end

			for iter_15_0 = 1, #var_15_1 do
				local var_15_2 = var_15_1[iter_15_0]

				if var_15_2:getLineIndex() == arg_15_1 and var_15_2:inBulletBound() then
					table.insert(var_15_0, var_15_2)
				end
			end

			return var_15_0
		end,
		getChars = function(arg_16_0)
			return arg_16_0.chars
		end,
		getEnemys = function(arg_17_0)
			return arg_17_0.enemys
		end,
		getCharLine = function(arg_18_0, arg_18_1)
			local var_18_0 = {}

			for iter_18_0 = 1, #arg_18_0.chars do
				local var_18_1 = arg_18_0.chars[iter_18_0]

				if var_18_1:getLineIndex() == arg_18_1 then
					table.insert(var_18_0, var_18_1)
				end
			end

			return var_18_0
		end,
		addEnemyChar = function(arg_19_0, arg_19_1, arg_19_2)
			local var_19_0 = arg_19_1
			local var_19_1 = arg_19_0:createChar(var_19_0)

			var_19_1:prepareData()
			var_19_1:setLineIndex(arg_19_2.index)

			local var_19_2 = arg_19_0.content:InverseTransformPoint(arg_19_2.position)
			local var_19_3 = math.random(BeachGuardConst.enemy_pos[1], BeachGuardConst.enemy_pos[2])

			var_19_1:setParent(arg_19_0.content, false, Vector2(var_19_3 + var_19_2.x, var_19_2.y + BeachGuardConst.enemy_offset_y))
			var_19_1:setCamp(2)
			var_19_1:setRaycast(false)
			table.insert(arg_19_0.enemys, var_19_1)
		end,
		sortChar = function(arg_20_0)
			local var_20_0 = #arg_20_0.chars + #arg_20_0.enemys

			if not arg_20_0.sorts or #arg_20_0.sorts ~= var_20_0 then
				arg_20_0.sorts = {}

				for iter_20_0 = 1, #arg_20_0.chars do
					table.insert(arg_20_0.sorts, arg_20_0.chars[iter_20_0])
				end

				for iter_20_1 = 1, #arg_20_0.enemys do
					table.insert(arg_20_0.sorts, arg_20_0.enemys[iter_20_1])
				end

				table.sort(arg_20_0.sorts, function(arg_21_0, arg_21_1)
					local var_21_0 = arg_21_0:getPos()
					local var_21_1 = arg_21_1:getPos()

					if var_21_0.y > var_21_1.y then
						return true
					elseif var_21_0.y < var_21_1.y then
						return false
					end

					if var_21_0.x > var_21_1.x then
						return true
					elseif var_21_0.x < var_21_1.x then
						return false
					end
				end)

				for iter_20_2 = 1, #arg_20_0.sorts do
					arg_20_0.sorts[iter_20_2]:SetSiblingIndex(iter_20_2)
				end
			end
		end
	}

	var_1_0:Ctor()

	return var_1_0
end

local function var_0_2(arg_22_0, arg_22_1)
	local var_22_0 = {
		Ctor = function(arg_23_0)
			arg_23_0._tf = arg_22_0
			arg_23_0._event = arg_22_1
			arg_23_0.lineTpl = findTF(arg_23_0._tf, "sceneContainer/scene/classes/lineTpl")
			arg_23_0.gridTpl = findTF(arg_23_0._tf, "sceneContainer/scene/classes/gridTpl")
			arg_23_0.lines = {}
			arg_23_0.content = findTF(arg_23_0._tf, "sceneContainer/scene/content")

			for iter_23_0 = 1, BeachGuardConst.line_num do
				local var_23_0 = findTF(arg_23_0._tf, "sceneContainer/scene/linePos/" .. iter_23_0)
				local var_23_1 = tf(instantiate(arg_23_0.lineTpl))

				var_23_1.anchoredPosition = Vector2(0, 0)

				setParent(var_23_1, var_23_0)

				local var_23_2 = BeachGuardLine.New(var_23_1, arg_23_0.gridTpl, arg_23_0._event)

				var_23_2:setIndex(iter_23_0)
				table.insert(arg_23_0.lines, var_23_2)
			end
		end,
		setMapData = function(arg_24_0, arg_24_1)
			local var_24_0 = arg_24_1.line

			arg_24_0.activeLines = {}

			for iter_24_0 = 1, #arg_24_0.lines do
				local var_24_1 = arg_24_0.lines[iter_24_0]

				if table.contains(var_24_0, var_24_1:getIndex()) then
					var_24_1:active(true)
					table.insert(arg_24_0.activeLines, var_24_1)
				else
					var_24_1:active(false)
				end
			end
		end,
		getGridByIndex = function(arg_25_0, arg_25_1, arg_25_2)
			for iter_25_0 = 1, #arg_25_0.activeLines do
				local var_25_0 = arg_25_0.activeLines[iter_25_0]

				if var_25_0:getIndex() == arg_25_1 then
					return var_25_0:getGridByIndex(arg_25_2)
				end
			end

			return nil
		end,
		setDrag = function(arg_26_0, arg_26_1)
			arg_26_0.dragData = arg_26_1
		end,
		start = function(arg_27_0)
			for iter_27_0 = 1, #arg_27_0.lines do
				local var_27_0 = arg_27_0.lines[iter_27_0]:start()
			end
		end,
		step = function(arg_28_0, arg_28_1)
			for iter_28_0 = 1, #arg_28_0.lines do
				local var_28_0 = arg_28_0.lines[iter_28_0]:step(arg_28_1)
			end
		end,
		clear = function(arg_29_0)
			arg_29_0:clearPre()

			for iter_29_0 = 1, #arg_29_0.lines do
				arg_29_0.lines[iter_29_0]:clear()
			end
		end,
		onTimer = function(arg_30_0)
			if not arg_30_0.dragData then
				return
			end

			if arg_30_0.dragData.flag ~= true or not arg_30_0.dragData.pos then
				if arg_30_0.preCharGrid then
					arg_30_0._event:emit(BeachGuardGameView.PULL_CHAR, {
						card_id = arg_30_0.preCardID,
						line_index = arg_30_0.preCharGrid:getLineIndex(),
						grid_index = arg_30_0.preCharGrid:getIndex()
					})
				end

				arg_30_0:clearPre()

				return
			end

			local var_30_0 = arg_30_0.dragData.pos
			local var_30_1 = arg_30_0:getGridByWorld(var_30_0)

			if var_30_1 and var_30_1:isEmpty() then
				local var_30_2 = arg_30_0.dragData.config
				local var_30_3 = var_30_2.char_id
				local var_30_4 = var_30_2.id

				if arg_30_0.preCharGrid == var_30_1 and arg_30_0.preCardID == var_30_4 then
					return
				end

				arg_30_0:clearPre()

				arg_30_0.preCharGrid = var_30_1
				arg_30_0.preCardID = var_30_4

				arg_30_0.preCharGrid:prechar(var_30_3)

				local var_30_5 = arg_30_0.preCharGrid:getLineIndex()
				local var_30_6 = arg_30_0.preCharGrid:getIndex()

				if var_30_5 and var_30_6 then
					local var_30_7 = BeachGuardConst.chars[var_30_3].distance

					for iter_30_0 = 1, var_30_7 do
						local var_30_8 = arg_30_0:getGridByIndex(var_30_5, var_30_6 + iter_30_0)

						if var_30_8 then
							var_30_8:preDistance()
							table.insert(arg_30_0.preDistanceGrids, var_30_8)
						end
					end
				end
			else
				arg_30_0:clearPre()
			end
		end,
		clearPre = function(arg_31_0)
			if arg_31_0.preCharGrid then
				arg_31_0.preCharGrid:unPreChar()

				arg_31_0.preCharGrid = nil
			end

			if arg_31_0.preDistanceGrids and #arg_31_0.preDistanceGrids > 0 then
				for iter_31_0 = 1, #arg_31_0.preDistanceGrids do
					arg_31_0.preDistanceGrids[iter_31_0]:unPreDistance()
				end
			end

			arg_31_0.preDistanceGrids = {}
		end,
		removeGridChar = function(arg_32_0, arg_32_1)
			local var_32_0 = arg_32_0:getGridByChar(arg_32_1)

			if var_32_0 then
				var_32_0:removeChar()

				return true
			end
		end,
		getGridByWorld = function(arg_33_0, arg_33_1)
			for iter_33_0 = 1, #arg_33_0.activeLines do
				local var_33_0 = arg_33_0.activeLines[iter_33_0]:getGridWorld(arg_33_1)

				if var_33_0 then
					return var_33_0
				end
			end

			return nil
		end,
		getGridByChar = function(arg_34_0, arg_34_1)
			for iter_34_0 = 1, #arg_34_0.lines do
				local var_34_0 = arg_34_0.lines[iter_34_0]:getGrids()

				for iter_34_1, iter_34_2 in ipairs(var_34_0) do
					if iter_34_2:getChar() == arg_34_1 then
						return iter_34_2
					end
				end
			end

			return nil
		end,
		getAbleLinePos = function(arg_35_0, arg_35_1)
			local var_35_0 = {}

			for iter_35_0 = 1, #arg_35_0.activeLines do
				local var_35_1 = arg_35_0.activeLines[iter_35_0]:getIndex()

				if table.contains(arg_35_1, var_35_1) then
					table.insert(var_35_0, {
						position = arg_35_0.activeLines[iter_35_0]:getPosition(),
						index = var_35_1
					})
				end
			end

			return var_35_0[math.random(1, #var_35_0)]
		end
	}

	var_22_0:Ctor()

	return var_22_0
end

local function var_0_3(arg_36_0, arg_36_1)
	local var_36_0 = {
		Ctor = function(arg_37_0)
			arg_37_0._tf = arg_36_0
			arg_37_0._event = arg_36_1
			arg_37_0.content = findTF(arg_37_0._tf, "sceneContainer/scene/content")
			arg_37_0.bullets = {}
			arg_37_0.bulletPool = {}
		end,
		useSkill = function(arg_38_0, arg_38_1)
			local var_38_0 = arg_38_1.skill

			if var_38_0.type == BeachGuardConst.skill_craft then
				arg_38_0._event:emit(BeachGuardGameView.ADD_CRAFT, {
					num = var_38_0.num
				})
			elseif var_38_0.type == BeachGuardConst.skill_bullet then
				local var_38_1 = var_38_0.bullet_id

				for iter_38_0, iter_38_1 in ipairs(var_38_1) do
					arg_38_0:pullBullet(iter_38_1, arg_38_1)
				end
			elseif var_38_0.type == BeachGuardConst.skill_melee then
				local var_38_2 = arg_38_1.damage
				local var_38_3 = arg_38_1.target
				local var_38_4 = arg_38_1.position

				arg_38_0._event:emit(BeachGuardGameView.CREATE_CHAR_DAMAGE, {
					damage = var_38_2,
					position = var_38_4,
					target = var_38_3,
					useData = arg_38_1
				})
			end
		end,
		pullBullet = function(arg_39_0, arg_39_1, arg_39_2)
			local var_39_0 = arg_39_0:getOrCreateBullet(arg_39_1)
			local var_39_1 = arg_39_2.position
			local var_39_2 = arg_39_2.distanceVec
			local var_39_3 = var_39_0.config.offset

			var_39_0.tf.anchoredPosition = arg_39_0.content:InverseTransformPoint(var_39_1)

			if var_39_3 then
				var_39_0.tf.anchoredPosition = Vector2(var_39_0.tf.anchoredPosition.x + var_39_3.x, var_39_0.tf.anchoredPosition.y + var_39_3.y)
			end

			setActive(var_39_0.tf, true)

			var_39_0.distanceVec = var_39_2
			var_39_0.speed = Vector2(var_39_0.config.speed[1], var_39_0.config.speed[2])
			var_39_0.direct = arg_39_2.direct
			var_39_0.hit = false
			var_39_0.useData = arg_39_2

			if var_39_0.config.point_able then
				var_39_0.life = nil
			elseif var_39_0.config.speed_high and var_39_0.config.speed_high ~= 0 then
				local var_39_4 = arg_39_2.target:getPos()
				local var_39_5 = math.random(-10, 5)

				var_39_4.x = var_39_4.x + 5 - math.random() * 15

				local var_39_6 = arg_39_2.useChar:getPos()

				if var_39_4 and var_39_6 then
					var_39_0.life = math.abs(var_39_4.x - var_39_6.x) / math.abs(var_39_0.speed.x)
				else
					var_39_0.life = math.abs(var_39_0.distanceVec.x) / math.abs(var_39_0.speed.x)
				end
			else
				var_39_0.life = math.abs(var_39_0.distanceVec.x) / math.abs(var_39_0.speed.x)
			end

			var_39_0.gravity = 0

			if var_39_0.config.speed_high and var_39_0.config.speed_high ~= 0 then
				local var_39_7 = -(var_39_0.config.speed_high * 2) / math.pow(var_39_0.life / 2, 2)

				var_39_0.speed.y = math.abs(var_39_7) * (var_39_0.life / 2)
				var_39_0.gravity = var_39_7
			end

			table.insert(arg_39_0.bullets, var_39_0)
		end,
		getBullets = function(arg_40_0)
			return arg_40_0.bullets
		end,
		getOrCreateBullet = function(arg_41_0, arg_41_1)
			local var_41_0 = arg_41_0:getBulletFromPool(arg_41_1)

			if not var_41_0 then
				local var_41_1 = BeachGuardConst.bullet[arg_41_1]
				local var_41_2 = BeachGuardAsset.getBullet(var_41_1.name)

				setParent(var_41_2, arg_41_0.content)

				var_41_0 = {
					tf = var_41_2,
					config = var_41_1
				}
			end

			return var_41_0
		end,
		getBulletFromPool = function(arg_42_0, arg_42_1)
			for iter_42_0 = #arg_42_0.bulletPool, 1, -1 do
				if arg_42_0.bulletPool[iter_42_0].config.id == arg_42_1 then
					return table.remove(arg_42_0.bulletPool, iter_42_0)
				end
			end

			return nil
		end,
		finishBullet = function(arg_43_0, arg_43_1)
			local var_43_0 = arg_43_1.config.damage

			setActive(arg_43_1.tf, false)

			local var_43_1 = arg_43_1.tf.anchoredPosition
		end,
		start = function(arg_44_0)
			return
		end,
		step = function(arg_45_0, arg_45_1)
			for iter_45_0 = #arg_45_0.bullets, 1, -1 do
				local var_45_0 = arg_45_0.bullets[iter_45_0]
				local var_45_1 = var_45_0.speed
				local var_45_2 = var_45_0.gravity
				local var_45_3 = var_45_0.direct

				var_45_0.tf.anchoredPosition = Vector2(var_45_0.tf.anchoredPosition.x + var_45_1.x * arg_45_1 * var_45_3, var_45_0.tf.anchoredPosition.y + var_45_1.y * arg_45_1)
				var_45_0.speed.y = var_45_0.speed.y + var_45_0.gravity * arg_45_1

				if var_45_0.life then
					var_45_0.life = var_45_0.life - arg_45_1

					if var_45_0.life <= 0 then
						if var_45_0.config.speed_high and var_45_0.config.speed_high ~= 0 and not var_45_0.hit then
							local var_45_4 = var_45_0.config.damage

							var_45_0.useData.target = nil

							arg_45_0._event:emit(BeachGuardGameView.BULLET_DAMAGE, {
								damage = var_45_4,
								position = var_45_0.tf.position,
								useData = var_45_0.useData
							})
						end

						local var_45_5 = table.remove(arg_45_0.bullets, iter_45_0)

						arg_45_0:finishBullet(var_45_5)
						table.insert(arg_45_0.bulletPool, var_45_5)
					elseif var_45_0.hit then
						local var_45_6 = table.remove(arg_45_0.bullets, iter_45_0)

						arg_45_0:finishBullet(var_45_6)
						table.insert(arg_45_0.bulletPool, var_45_6)
					end
				end
			end
		end,
		stop = function(arg_46_0)
			return
		end,
		clear = function(arg_47_0)
			for iter_47_0 = #arg_47_0.bullets, 1, -1 do
				local var_47_0 = table.remove(arg_47_0.bullets, iter_47_0)

				setActive(var_47_0.tf, false)

				var_47_0.distanceVec = nil

				table.insert(arg_47_0.bulletPool, var_47_0)
			end
		end
	}

	var_36_0:Ctor()

	return var_36_0
end

local function var_0_4(arg_48_0, arg_48_1)
	local var_48_0 = {
		Ctor = function(arg_49_0)
			arg_49_0._tf = arg_48_0
			arg_49_0._event = arg_48_1
		end,
		setData = function(arg_50_0, arg_50_1)
			arg_50_0._data = arg_50_1
			arg_50_0._chapterId = arg_50_0._data.id
		end,
		start = function(arg_51_0)
			arg_51_0:clear()

			arg_51_0._chapterDatas = Clone(arg_51_0._data.data)
		end,
		step = function(arg_52_0, arg_52_1)
			arg_52_0._overTime = arg_52_0._overTime + arg_52_1

			for iter_52_0 = #arg_52_0._chapterDatas, 1, -1 do
				if arg_52_0._chapterDatas[iter_52_0].time < arg_52_0._overTime then
					local var_52_0 = arg_52_0:createData(table.remove(arg_52_0._chapterDatas, iter_52_0))

					table.insert(arg_52_0.enemyDatas, var_52_0)
				end
			end

			for iter_52_1 = #arg_52_0.enemyDatas, 1, -1 do
				local var_52_1 = arg_52_0.enemyDatas[iter_52_1]

				if var_52_1.loop then
					var_52_1.stepTime = var_52_1.stepTime - arg_52_1

					if var_52_1.stepTime <= 0 then
						local var_52_2 = var_52_1.step

						var_52_1.stepTime = math.random() * (var_52_2[2] - var_52_2[1]) + var_52_2[1]

						arg_52_0:addEnemyData(var_52_1)
					end

					if arg_52_0._overTime > var_52_1.stop then
						table.remove(arg_52_0.enemyDatas, iter_52_1)
					end
				else
					arg_52_0:addEnemyData(var_52_1)
					table.remove(arg_52_0.enemyDatas, iter_52_1)
				end
			end

			if not arg_52_0.addEnemyTime then
				arg_52_0.addEnemyTime = 1
			end

			arg_52_0.addEnemyTime = arg_52_0.addEnemyTime - arg_52_1

			if #arg_52_0.enemyList > 0 and arg_52_0.addEnemyTime <= 0 then
				local var_52_3 = table.remove(arg_52_0.enemyList, #arg_52_0.enemyList)

				arg_52_0._event:emit(BeachGuardGameView.ADD_ENEMY, var_52_3)
			end

			if #arg_52_0.enemyDatas == 0 and #arg_52_0._chapterDatas == 0 and #arg_52_0.enemyList == 0 then
				arg_52_0.finishCreate = true
			end
		end,
		getFinishCreate = function(arg_53_0)
			return arg_53_0.finishCreate
		end,
		createData = function(arg_54_0, arg_54_1)
			local var_54_0 = {}
			local var_54_1 = arg_54_1.create
			local var_54_2 = arg_54_1.time
			local var_54_3 = arg_54_1.stop
			local var_54_4 = arg_54_1.step
			local var_54_5 = arg_54_1.comming

			if var_54_4 then
				var_54_0.loop = true
				var_54_0.stepTime = 0
			else
				var_54_0.loop = false
			end

			var_54_0.create = var_54_1
			var_54_0.time = var_54_2
			var_54_0.stop = var_54_3
			var_54_0.step = var_54_4
			var_54_0.comming = var_54_5

			return var_54_0
		end,
		addEnemyData = function(arg_55_0, arg_55_1)
			local var_55_0 = arg_55_1.create

			if arg_55_1.comming or false then
				arg_55_1.comming = false

				arg_55_0._event:emit(BeachGuardGameView.ENEMY_COMMING)
			end

			local var_55_1 = BeachGuardConst.create_enemy[var_55_0]

			for iter_55_0 = 1, var_55_1.num do
				local var_55_2 = var_55_1.enemy[math.random(1, #var_55_1.enemy)]
				local var_55_3 = var_55_1.line

				table.insert(arg_55_0.enemyList, {
					id = var_55_2,
					lines = var_55_3
				})
			end
		end,
		stop = function(arg_56_0)
			return
		end,
		clear = function(arg_57_0)
			arg_57_0._overTime = 0
			arg_57_0._chapterDatas = {}
			arg_57_0.enemyDatas = {}
			arg_57_0.enemyList = {}
			arg_57_0.finishCreate = false
		end
	}

	var_48_0:Ctor()

	return var_48_0
end

local function var_0_5(arg_58_0, arg_58_1)
	local var_58_0 = {
		Ctor = function(arg_59_0)
			arg_59_0._tf = arg_58_0
			arg_59_0._event = arg_58_1
			arg_59_0.effectBackTf = findTF(arg_59_0._tf, "sceneContainer/scene/effect_back")
			arg_59_0.effectFrontTf = findTF(arg_59_0._tf, "sceneContainer/scene/effect_front")
			arg_59_0.content = findTF(arg_59_0._tf, "sceneContainer/scene/content")
			arg_59_0.effects = {}
			arg_59_0.effectPool = {}
		end,
		setCharCtrl = function(arg_60_0, arg_60_1)
			arg_60_0.charCtrl = arg_60_1
		end,
		setSkillCtrl = function(arg_61_0, arg_61_1)
			arg_61_0.skillCtrl = arg_61_1
		end,
		craeteCharDamage = function(arg_62_0, arg_62_1)
			arg_62_0:createDamage(arg_62_1)
		end,
		bulletDamage = function(arg_63_0, arg_63_1)
			arg_63_0:createDamage(arg_63_1)
		end,
		createDamage = function(arg_64_0, arg_64_1)
			local var_64_0 = arg_64_1.damage
			local var_64_1 = arg_64_1.position
			local var_64_2 = arg_64_1.useData
			local var_64_3 = var_64_2.target
			local var_64_4 = var_64_2.line
			local var_64_5 = var_64_2.camp

			if not var_64_0 then
				-- block empty
			end

			local var_64_6 = BeachGuardConst.damage[var_64_0]

			if var_64_3 then
				local var_64_7 = var_64_2.atkRate or 1

				var_64_3:damage(var_64_6.damage * var_64_7)
			end

			if var_64_6.type == BeachGuardConst.bullet_type_range then
				local var_64_8 = var_64_6.config
				local var_64_9 = var_64_8.next
				local var_64_10 = var_64_8.range
				local var_64_11 = var_64_5 == 1 and 2 or 1
				local var_64_12 = arg_64_0.charCtrl:getLineCampChars({
					var_64_4 + 1,
					var_64_4 - 1,
					var_64_4
				}, var_64_11)
				local var_64_13

				if var_64_2.target then
					var_64_13 = var_64_2.target:getPos()
				else
					var_64_13 = arg_64_0.effectFrontTf:InverseTransformPoint(var_64_1)
				end

				if var_64_12 and #var_64_12 > 0 then
					local var_64_14 = var_64_10 * BeachGuardConst.part_width

					for iter_64_0 = 1, #var_64_12 do
						local var_64_15 = var_64_12[iter_64_0]

						if (not var_64_2.target or var_64_2.target ~= var_64_15) and var_64_14 > math.abs(var_64_13.x - var_64_15:getPos().x) then
							local var_64_16 = var_64_15:getWorldPos()
							local var_64_17 = Clone(var_64_2)

							var_64_17.target = var_64_15

							arg_64_0:createDamage({
								damage = var_64_8.next,
								position = var_64_16,
								useData = var_64_17
							})
						end
					end
				end
			elseif var_64_6.type == BeachGuardConst.bullet_type_disperse then
				local var_64_18 = var_64_6.config
				local var_64_19 = var_64_18.up
				local var_64_20 = var_64_18.down
				local var_64_21 = var_64_5 == 1 and 2 or 1

				arg_64_0:addDamageByDisperse({
					var_64_4 - 1
				}, var_64_18.range, var_64_21, var_64_19, var_64_2)
				arg_64_0:addDamageByDisperse({
					var_64_4 + 1
				}, var_64_18.range, var_64_21, var_64_20, var_64_2)
			end

			if var_64_6.buff and #var_64_6.buff > 0 then
				for iter_64_1 = 1, #var_64_6.buff do
					local var_64_22 = var_64_6.buff[iter_64_1]
					local var_64_23 = BeachGuardConst.buff[var_64_22]
					local var_64_24 = var_64_23.type
					local var_64_25 = var_64_23.trigger
					local var_64_26 = var_64_23.bound
					local var_64_27 = var_64_2.useChar
					local var_64_28 = var_64_2.target

					if var_64_25 == BeachGuardConst.buff_trigger_other then
						var_64_28:addBuff(var_64_23)
					elseif var_64_25 == BeachGuardConst.buff_trigger_self then
						var_64_27:addBuff(var_64_23)

						if var_64_26 and var_64_26 ~= nil then
							local var_64_29 = var_64_2.useChar:getCamp()
							local var_64_30 = var_64_2.useChar:getLineIndex()
							local var_64_31 = var_64_2.useChar:getGridIndex()

							if var_64_30 and var_64_31 then
								local var_64_32 = arg_64_0.charCtrl:getCharByCamp(var_64_29)

								for iter_64_2, iter_64_3 in ipairs(var_64_32) do
									if iter_64_3 ~= var_64_27 then
										local var_64_33 = iter_64_3:getGridIndex()
										local var_64_34 = iter_64_3:getLineIndex()

										if math.abs(var_64_33 - var_64_31) <= var_64_26[1] and math.abs(var_64_34 - var_64_30) <= var_64_26[2] then
											iter_64_3:addBuff(var_64_23)
										end
									end
								end
							end
						end
					end
				end
			end

			if var_64_6.effect and #var_64_6.effect > 0 then
				arg_64_0:createEffect(var_64_6.effect, var_64_1)
			end
		end,
		addDamageByDisperse = function(arg_65_0, arg_65_1, arg_65_2, arg_65_3, arg_65_4, arg_65_5)
			local var_65_0 = arg_65_0.charCtrl:getLineCampChars(arg_65_1, arg_65_3)

			if var_65_0 and #var_65_0 > 0 then
				local var_65_1 = arg_65_2 * BeachGuardConst.part_width
				local var_65_2 = arg_65_5.target:getPos()

				for iter_65_0 = 1, #var_65_0 do
					local var_65_3 = var_65_0[iter_65_0]
					local var_65_4 = var_65_3:getPos()

					if var_65_1 > math.abs(var_65_2.x - var_65_4.x) then
						local var_65_5 = var_65_3:getWorldPos()
						local var_65_6 = Clone(arg_65_5)

						var_65_6.target = var_65_3

						arg_65_0:createDamage({
							damage = arg_65_4,
							position = var_65_5,
							useData = var_65_6
						})
					end
				end
			end
		end,
		createEffect = function(arg_66_0, arg_66_1, arg_66_2)
			local var_66_0 = arg_66_0:getEffect(arg_66_1[1])

			if not var_66_0 then
				-- block empty
			end

			if not var_66_0 then
				return
			end

			var_66_0.tf.anchoredPosition = arg_66_0.effectFrontTf:InverseTransformPoint(arg_66_2)

			setActive(var_66_0.tf, true)

			var_66_0.time = var_66_0.config.time

			table.insert(arg_66_0.effects, var_66_0)
		end,
		getEffect = function(arg_67_0, arg_67_1)
			local var_67_0

			if #arg_67_0.effectPool > 0 then
				for iter_67_0 = #arg_67_0.effectPool, 1, -1 do
					if arg_67_0.effectPool[iter_67_0].config.id == arg_67_1 then
						return (table.remove(arg_67_0.effectPool, iter_67_0))
					end
				end
			end

			local var_67_1 = BeachGuardConst.effect[arg_67_1]
			local var_67_2 = BeachGuardAsset.getEffect(var_67_1.name)

			setParent(var_67_2, arg_67_0.effectFrontTf)

			return {
				tf = var_67_2,
				config = var_67_1
			}
		end,
		start = function(arg_68_0)
			return
		end,
		step = function(arg_69_0, arg_69_1)
			local var_69_0 = arg_69_0.skillCtrl:getBullets()

			for iter_69_0 = 1, #var_69_0 do
				local var_69_1 = var_69_0[iter_69_0]
				local var_69_2 = var_69_1.useData
				local var_69_3 = var_69_2.line
				local var_69_4 = var_69_2.camp
				local var_69_5 = var_69_1.tf.position
				local var_69_6 = arg_69_0.charCtrl:getCanHitChar(var_69_3, var_69_4)
				local var_69_7 = false

				for iter_69_1, iter_69_2 in ipairs(var_69_6) do
					if not var_69_7 and iter_69_2:inBulletBound() and iter_69_2:checkBulletCollider(var_69_5) then
						local var_69_8 = var_69_1.config.damage

						var_69_7 = true
						var_69_1.hit = true
						var_69_2.target = iter_69_2

						arg_69_0:createDamage({
							damage = var_69_8,
							position = var_69_2.target:getAnimPos(),
							useData = var_69_1.useData
						})
					end
				end
			end

			for iter_69_3 = #arg_69_0.effects, 1, -1 do
				local var_69_9 = arg_69_0.effects[iter_69_3]

				if var_69_9.time and var_69_9.time > 0 then
					var_69_9.time = var_69_9.time - arg_69_1

					if var_69_9.time <= 0 then
						var_69_9.time = 0

						setActive(var_69_9.tf, false)

						local var_69_10 = table.remove(arg_69_0.effects, iter_69_3)

						table.insert(arg_69_0.effectPool, var_69_10)
					end
				end
			end
		end,
		stop = function(arg_70_0)
			return
		end,
		clear = function(arg_71_0)
			for iter_71_0 = #arg_71_0.effects, 1, -1 do
				setActive(arg_71_0.effects[iter_71_0].tf, false)
				table.insert(arg_71_0.effectPool, table.remove(arg_71_0.effects, iter_71_0))
			end
		end
	}

	var_58_0:Ctor()

	return var_58_0
end

function var_0_0.Ctor(arg_72_0, arg_72_1, arg_72_2, arg_72_3)
	arg_72_0._tf = arg_72_1
	arg_72_0._event = arg_72_3
	arg_72_0._gameData = arg_72_2
	arg_72_0.asset = arg_72_0._gameData.asset
	arg_72_0.timer = Timer.New(function()
		arg_72_0:onTimer()
	end, 0.03333333333333333, -1)

	arg_72_0:init()
end

function var_0_0.init(arg_74_0)
	arg_74_0.charTpl = findTF(arg_74_0._tf, "sceneContainer/scene/classes/charTpl")
	arg_74_0.charCtrl = var_0_1(arg_74_0._tf, arg_74_0.charTpl, arg_74_0._event)
	arg_74_0.lineCtrl = var_0_2(arg_74_0._tf, arg_74_0._event)
	arg_74_0.skillCtrl = var_0_3(arg_74_0._tf, arg_74_0._event)
	arg_74_0.enemyCtrl = var_0_4(arg_74_0._tf, arg_74_0._event)
	arg_74_0.damageCtrl = var_0_5(arg_74_0._tf, arg_74_0._event)

	arg_74_0.damageCtrl:setCharCtrl(arg_74_0.charCtrl)
	arg_74_0.damageCtrl:setSkillCtrl(arg_74_0.skillCtrl)
	arg_74_0.timer:Start()
end

function var_0_0.onTimer(arg_75_0)
	arg_75_0.lineCtrl:onTimer()
end

function var_0_0.setData(arg_76_0, arg_76_1)
	arg_76_0._runningData = arg_76_1

	local var_76_0 = arg_76_0._runningData.chapter
	local var_76_1 = BeachGuardConst.chapter_data[var_76_0]
	local var_76_2 = BeachGuardConst.map_data[var_76_1.map]
	local var_76_3 = BeachGuardConst.chapater_enemy[var_76_0]

	arg_76_0.lineCtrl:setMapData(var_76_2)
	arg_76_0.enemyCtrl:setData(var_76_3)

	if arg_76_1.fog then
		setActive(findTF(arg_76_0._tf, "sceneContainer/scene_front/fog"), true)
	else
		setActive(findTF(arg_76_0._tf, "sceneContainer/scene_front/fog"), false)
	end

	local var_76_4 = GetComponent(findTF(arg_76_0._tf, "sceneBg/map"), typeof(Image))

	var_76_4.sprite = BeachGuardAsset.getBeachMap(var_76_2.pic)

	var_76_4:SetNativeSize()
end

function var_0_0.start(arg_77_0)
	arg_77_0.charCtrl:start()
	arg_77_0.skillCtrl:start()
	arg_77_0.enemyCtrl:start()
	arg_77_0.damageCtrl:start()
	arg_77_0.lineCtrl:start()
end

function var_0_0.step(arg_78_0)
	local var_78_0 = arg_78_0._runningData.deltaTime

	arg_78_0.charCtrl:step(var_78_0)
	arg_78_0.skillCtrl:step(var_78_0)
	arg_78_0.enemyCtrl:step(var_78_0)
	arg_78_0.damageCtrl:step(var_78_0)
	arg_78_0.lineCtrl:step(var_78_0)

	if arg_78_0.charCtrl:getEnemyOver() then
		arg_78_0._event:emit(BeachGuardGameView.GAME_OVER)
	elseif #arg_78_0.charCtrl:getEnemys() == 0 and arg_78_0.enemyCtrl:getFinishCreate() then
		arg_78_0._event:emit(BeachGuardGameView.GAME_OVER)
	end
end

function var_0_0.stop(arg_79_0)
	arg_79_0.charCtrl:stop()
	arg_79_0.skillCtrl:stop()
	arg_79_0.enemyCtrl:stop()
	arg_79_0.damageCtrl:stop()
end

function var_0_0.clear(arg_80_0)
	arg_80_0.charCtrl:clear()
	arg_80_0.lineCtrl:clear()
	arg_80_0.skillCtrl:clear()
	arg_80_0.enemyCtrl:clear()
	arg_80_0.damageCtrl:clear()
end

function var_0_0.changeRecycles(arg_81_0, arg_81_1)
	arg_81_0.charCtrl:changeRecycles(arg_81_1)
end

function var_0_0.pullChar(arg_82_0, arg_82_1, arg_82_2, arg_82_3)
	local var_82_0 = arg_82_0.lineCtrl:getGridByIndex(arg_82_2, arg_82_3)

	if var_82_0 and var_82_0:isEmpty() then
		local var_82_1 = arg_82_0.charCtrl:setGridChar(arg_82_1, var_82_0)

		var_82_0:setChar(var_82_1)

		return true
	end

	return false
end

function var_0_0.setDrag(arg_83_0, arg_83_1)
	arg_83_0.lineCtrl:setDrag(arg_83_1)
end

function var_0_0.useSkill(arg_84_0, arg_84_1)
	arg_84_0.skillCtrl:useSkill(arg_84_1)
end

function var_0_0.addEnemy(arg_85_0, arg_85_1)
	local var_85_0 = arg_85_0.lineCtrl:getAbleLinePos(arg_85_1.lines)

	arg_85_0.charCtrl:addEnemyChar(arg_85_1.id, var_85_0)
end

function var_0_0.craeteCharDamage(arg_86_0, arg_86_1)
	arg_86_0.damageCtrl:craeteCharDamage(arg_86_1)
end

function var_0_0.removeChar(arg_87_0, arg_87_1)
	arg_87_0.charCtrl:removeChar(arg_87_1)
	arg_87_0.lineCtrl:removeGridChar(arg_87_1)
end

function var_0_0.bulletDamage(arg_88_0, arg_88_1)
	arg_88_0.damageCtrl:bulletDamage(arg_88_1)
end

function var_0_0.dispose(arg_89_0)
	if arg_89_0.timer then
		arg_89_0.timer:Stop()

		arg_89_0.timer = nil
	end
end

return var_0_0
