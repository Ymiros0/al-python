local var_0_0 = class("SailBoatEnemyControllua")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._bgContent = arg_1_1
	arg_1_0._eventCall = arg_1_2
	arg_1_0._content = findTF(arg_1_0._bgContent, "scene/content")
	arg_1_0._enemys = {}
	arg_1_0._enemyPool = {}
	arg_1_0._rules = {}

def var_0_0.start(arg_2_0):
	for iter_2_0 = #arg_2_0._enemys, 1, -1:
		arg_2_0.returnEnemy(table.remove(arg_2_0._enemys, iter_2_0))

	arg_2_0._rules = {}

	var_0_1.SetGameEnemys(arg_2_0._enemys)

	local var_2_0 = var_0_1.GetRoundData()

	if var_2_0:
		for iter_2_1 = 1, #var_2_0.enemy_rule:
			local var_2_1 = SailBoatGameConst.enemy_rule[var_2_0.enemy_rule[iter_2_1]]

			if not var_2_1:
				print("不存在 rule id " .. var_2_0.enemy_rule[iter_2_1])

			local var_2_2 = 0

			table.insert(arg_2_0._rules, {
				data = var_2_1,
				time = var_2_2
			})

	arg_2_0._fireIndex = var_0_1.fire_step

def var_0_0.step(arg_3_0, arg_3_1):
	arg_3_0._fireIndex = arg_3_0._fireIndex - 1

	if arg_3_0._fireIndex <= 0:
		arg_3_0._fireIndex = var_0_1.fire_step

		local var_3_0 = var_0_1.GetGameChar()
		local var_3_1 = var_3_0.getPosition()
		local var_3_2 = var_0_1.GetGameEnemys()

		for iter_3_0 = 1, #var_3_2:
			local var_3_3 = var_3_2[iter_3_0]

			if var_3_3.canFire():
				arg_3_0.checkEnemyFire(var_3_0, var_3_3)

	local var_3_4 = var_0_1.GetGameItems()

	for iter_3_1 = #arg_3_0._enemys, 1, -1:
		local var_3_5 = arg_3_0._enemys[iter_3_1]

		var_3_5.step(arg_3_1)

		if var_3_5.getRemoveFlag():
			table.remove(arg_3_0._enemys, iter_3_1)
			arg_3_0.returnEnemy(var_3_5)
		elif not var_3_5.getStop():
			for iter_3_2, iter_3_3 in ipairs(var_3_4):
				if arg_3_0.checkEnemyCollider(var_3_5, iter_3_3):
					var_3_5.stopTarget(Vector2(0, 0))

					if var_3_5.getConfig("boom") and var_3_5.damage({
						num = 99999
					}):
						arg_3_0._eventCall(SailBoatGameEvent.DESTROY_ENEMY, var_3_5.getDestroyData())

	local var_3_6 = var_0_1.gameTime

	for iter_3_4 = 1, #arg_3_0._rules:
		local var_3_7 = arg_3_0._rules[iter_3_4]
		local var_3_8 = var_3_7.data.create_time

		if var_3_6 > var_3_8[1] and var_3_6 < var_3_8[2] and var_3_7.time and var_3_7.time >= 0:
			var_3_7.time = var_3_7.time - arg_3_1

			if var_3_7.time <= 0:
				var_3_7.time = math.random(1, var_3_7.data.time[2] - var_3_7.data.time[1]) + var_3_7.data.time[1]

				arg_3_0.applyRule(var_3_7)

def var_0_0.checkEnemyFire(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.getPosition()

	if arg_4_1.getLife() and arg_4_2.getLife() and not arg_4_2.inFireCd():
		local var_4_1 = arg_4_2.getPosition()
		local var_4_2, var_4_3 = arg_4_2.getWeapons()
		local var_4_4, var_4_5 = arg_4_2.getFirePos()
		local var_4_6, var_4_7 = arg_4_2.getFireContent()
		local var_4_8 = var_4_0.x > var_4_1.x and var_4_3 or var_4_2
		local var_4_9 = var_4_0.x > var_4_1.x and var_4_5 or var_4_4

		var_4_9.y = var_4_9.y + math.random(-15, 15)

		local var_4_10 = var_4_0.x > var_4_1.x and var_4_7 or var_4_6

		if math.sqrt(math.pow(var_4_0.x - var_4_1.x, 2) + math.pow(var_4_0.y - var_4_1.y, 2)) < arg_4_2.getWeaponMaxDistance():
			local var_4_11 = math.atan2(var_4_0.y - var_4_1.y + math.random(-50, 50), var_4_0.x - var_4_1.x + math.random(-50, 50))
			local var_4_12 = var_4_11 * math.rad2Deg

			for iter_4_0 = 1, #var_4_8:
				local var_4_13 = var_4_8[iter_4_0]

				if var_4_13.getFireAble():
					local var_4_14 = var_4_13.getAngel()

					if var_4_14 > math.abs(var_4_12) or var_4_14 > math.abs(180 - math.abs(var_4_12)):
						local var_4_15 = var_4_13.fire()

						if var_4_15:
							arg_4_2.fire()

							local var_4_16 = {
								pos = var_4_9,
								move = Vector2(math.cos(var_4_11), math.sin(var_4_11)),
								hit = arg_4_2.getHitGroup(),
								effect_pos = Vector2(0, 0),
								effect_content = var_4_10
							}

							arg_4_0._eventCall(SailBoatGameEvent.BOAT_EVENT_FIRE, {
								bullet_id = var_4_15.bullet_id,
								weapon_data = var_4_15,
								fire_data = var_4_16
							})

							return

def var_0_0.returnEnemy(arg_5_0, arg_5_1):
	arg_5_1.clear()
	table.insert(arg_5_0._enemyPool, arg_5_1)

def var_0_0.checkEnemyCollider(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_2.getConfig("type") == SailBoatGameConst.item_static:
		local var_6_0 = arg_6_2.getPosition()
		local var_6_1 = arg_6_1.getPosition()

		if math.abs(var_6_0.x - var_6_1.x) < 500 and math.abs(var_6_0.y - var_6_1.y) < 500:
			local var_6_2, var_6_3 = arg_6_2.getWorldColliderData()
			local var_6_4, var_6_5 = arg_6_1.getWorldColliderData()

			if var_0_1.CheckRectCollider(var_6_4, var_6_2, var_6_5, var_6_3):
				return True

	return False

def var_0_0.applyRule(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.data
	local var_7_1 = var_7_0.enemys
	local var_7_2 = var_7_0.screen_pos_x
	local var_7_3 = var_7_0.screen_pos_y

	if not var_7_2 or not var_7_3:
		print("rule id = " .. var_7_0 .. " 异常，没有范围参数")

	local var_7_4 = var_7_1[math.random(1, #var_7_1)]
	local var_7_5 = var_0_1.GetRangePos(var_7_2, var_7_3)

	if not var_7_5:
		return

	local var_7_6 = arg_7_0.getOrCreateEnemy(var_7_4)

	var_7_6.setPosition(var_7_5)
	table.insert(arg_7_0._enemys, var_7_6)

	local var_7_7 = arg_7_1.data.target_x
	local var_7_8 = arg_7_1.data.target_y
	local var_7_9 = arg_7_1.data.target_speed

	var_7_6.setTarget(var_7_7, var_7_8, var_7_9)
	var_7_6.start()

def var_0_0.getOrCreateEnemy(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0

	if #arg_8_0._enemyPool > 0:
		for iter_8_0 = #arg_8_0._enemyPool, 1, -1:
			if not var_8_0 and arg_8_0._enemyPool[iter_8_0].getId() == arg_8_1:
				var_8_0 = table.remove(arg_8_0._enemyPool, iter_8_0)

				break

	if not var_8_0:
		if not SailBoatGameConst.game_enemy[arg_8_1]:
			print("id = " .. arg_8_1 .. " 的敌人不存在")

		local var_8_1 = Clone(SailBoatGameConst.game_enemy[arg_8_1])
		local var_8_2 = var_0_1.GetGameEnemyTf(var_8_1.tpl)

		var_8_0 = SailBoatEnemy.New(var_8_2, arg_8_0._event)

		var_8_0.setData(var_8_1)
		arg_8_0.initWeapon(var_8_0, var_8_1.weapons)
		var_8_0.setContent(arg_8_0._content)

	return var_8_0

def var_0_0.initWeapon(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = {}
	local var_9_1 = {}

	for iter_9_0 = 1, #arg_9_2[1]:
		local var_9_2 = arg_9_2[1][iter_9_0]
		local var_9_3 = SailBoatGameConst.game_weapon[var_9_2]
		local var_9_4 = SailBoatWeapon.New(var_9_3)

		table.insert(var_9_0, var_9_4)

	for iter_9_1 = 1, #arg_9_2[2]:
		local var_9_5 = arg_9_2[2][iter_9_1]
		local var_9_6 = SailBoatGameConst.game_weapon[var_9_5]
		local var_9_7 = SailBoatWeapon.New(var_9_6)

		table.insert(var_9_1, var_9_7)

	arg_9_1.setWeapon(var_9_0, var_9_1)

def var_0_0.clear(arg_10_0):
	return

def var_0_0.stop(arg_11_0):
	return

def var_0_0.dispose(arg_12_0):
	return

return var_0_0
