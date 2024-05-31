local var_0_0 = class("SailBoatCharControl")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._bgContent = arg_1_1
	arg_1_0._eventCall = arg_1_2
	arg_1_0._charContent = findTF(arg_1_0._bgContent, "scene/content")

	local var_1_0 = SailBoatGameConst.game_char[var_0_1.char_id]
	local var_1_1 = var_0_1.GetGameCharTf(var_1_0.tpl)

	arg_1_0._char = SailBoatChar.New(var_1_1, arg_1_0._eventCall)

	arg_1_0._char.setData(var_1_0)
	arg_1_0._char.setContent(arg_1_0._charContent, var_0_1.char_start_pos)

def var_0_0.start(arg_2_0):
	var_0_1.SetGameChar(arg_2_0._char)

	arg_2_0._fireIndex = var_0_1.fire_step

	local var_2_0 = {}
	local var_2_1 = {}

	arg_2_0._char.clearEquipData()

	for iter_2_0 = 1, #var_0_1.equips:
		if var_0_1.equips[iter_2_0] and var_0_1.equips[iter_2_0] > 0:
			local var_2_2 = SailBoatGameConst.equip_data[var_0_1.equips[iter_2_0]]

			arg_2_0._char.setEquipData(var_2_2)

			if var_2_2.weapon_id and var_2_2.weapon_id != 0:
				local var_2_3 = SailBoatGameConst.game_weapon[var_2_2.weapon_id]
				local var_2_4 = SailBoatWeapon.New(var_2_3)
				local var_2_5 = SailBoatWeapon.New(var_2_3)

				table.insert(var_2_0, var_2_4)
				table.insert(var_2_1, var_2_5)

	local var_2_6 = var_0_1.char_weapons

	for iter_2_1 = 1, #var_2_6[1]:
		local var_2_7 = var_2_6[1][iter_2_1]
		local var_2_8 = SailBoatGameConst.game_weapon[var_2_7]
		local var_2_9 = SailBoatWeapon.New(Clone(var_2_8))

		table.insert(var_2_0, var_2_9)

	for iter_2_2 = 1, #var_2_6[2]:
		local var_2_10 = var_2_6[2][iter_2_2]
		local var_2_11 = SailBoatGameConst.game_weapon[var_2_10]
		local var_2_12 = SailBoatWeapon.New(Clone(var_2_11))

		table.insert(var_2_1, var_2_12)

	arg_2_0._char.setWeapon(var_2_0, var_2_1)
	arg_2_0._char.start()

	arg_2_0._ableFire = True

def var_0_0.step(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1.joyStickData
	local var_3_1 = 0
	local var_3_2 = 0
	local var_3_3 = 0
	local var_3_4 = 0

	if var_3_0 and var_3_0.active:
		var_3_1, var_3_2 = var_3_0.x, var_3_0.y
		var_3_3, var_3_4 = var_3_0.directX, var_3_0.directY

		if math.abs(var_3_3) < 0.1:
			var_3_3 = 0

		if math.abs(var_3_4) < 0.1:
			var_3_4 = 0

	if arg_3_0.getCharNextTouchFlag(var_3_1, var_3_2, var_3_3, var_3_4):
		var_3_1, var_3_2 = 0, 0

	arg_3_0._char.changeDirect(var_3_1, var_3_2)
	arg_3_0._char.step(arg_3_1)

	arg_3_0._fireIndex = arg_3_0._fireIndex - 1

	if arg_3_0._fireIndex <= 0:
		arg_3_0._fireIndex = var_0_1.fire_step

	if arg_3_0._ableFire:
		local var_3_5 = arg_3_0._char.getPosition()
		local var_3_6 = var_0_1.GetGameEnemys()

		for iter_3_0 = 1, #var_3_6:
			local var_3_7 = var_3_6[iter_3_0]

			arg_3_0.checkCharEnemyFire(arg_3_0._char, var_3_7)

def var_0_0.checkCharEnemyFire(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.getPosition()
	local var_4_1 = arg_4_1.getWeaponMaxDistance()
	local var_4_2 = arg_4_2.getPosition()
	local var_4_3 = var_4_2.x > var_4_0.x and 1 or -1

	if arg_4_1.getLife() and arg_4_2.getLife() and not arg_4_1.inFireCd(var_4_3):
		local var_4_4, var_4_5 = arg_4_0._char.getWeapons()
		local var_4_6, var_4_7 = arg_4_0._char.getFirePos()
		local var_4_8, var_4_9 = arg_4_0._char.getFireContent()
		local var_4_10 = var_4_2.x > var_4_0.x and var_4_5 or var_4_4
		local var_4_11 = var_4_2.x > var_4_0.x and var_4_7 or var_4_6

		var_4_11.y = var_4_11.y + math.random(-10, 10)

		local var_4_12 = var_4_2.x > var_4_0.x and var_4_9 or var_4_8

		if math.sqrt(math.pow(var_4_2.x - var_4_0.x, 2) + math.pow(var_4_2.y - var_4_0.y, 2)) < arg_4_0._char.getWeaponMaxDistance():
			local var_4_13 = math.atan2(var_4_2.y - var_4_0.y + math.random(-20, 20), var_4_2.x - var_4_0.x + math.random(-20, 20))
			local var_4_14 = var_4_13 * math.rad2Deg

			for iter_4_0 = 1, #var_4_10:
				local var_4_15 = var_4_10[iter_4_0]

				if var_4_15.getFireAble():
					local var_4_16 = var_4_15.getAngel()
					local var_4_17 = False

					if var_4_16 > math.abs(var_4_14) and var_4_3 == 1:
						var_4_17 = True
					elif var_4_16 > math.abs(180 - math.abs(var_4_14)) and var_4_3 == -1:
						var_4_17 = True

					if var_4_17:
						local var_4_18 = var_4_15.fire()

						if var_4_18:
							arg_4_1.fire(var_4_3)
							pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1.SFX_SOUND_FIRE)

							local var_4_19 = {
								pos = var_4_11,
								move = Vector2(math.cos(var_4_13), math.sin(var_4_13)),
								hit = arg_4_0._char.getHitGroup(),
								effect_pos = Vector2(0, 0),
								effect_content = var_4_12
							}

							arg_4_0._eventCall(SailBoatGameEvent.BOAT_EVENT_FIRE, {
								bullet_id = var_4_18.bullet_id,
								weapon_data = var_4_18,
								fire_data = var_4_19
							})

							return
	elif not arg_4_1.inFireCd(var_4_3):
		-- block empty

def var_0_0.getCharNextTouchFlag(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	local var_5_0 = arg_5_0._char.getNextPosition(arg_5_1, arg_5_2)
	local var_5_1 = arg_5_0._char.getBoundData()
	local var_5_2 = arg_5_0._char.getColliderMinPosition()
	local var_5_3 = Vector2(0, 0)

	var_5_3.x = var_5_0.x + var_5_2.x
	var_5_3.y = var_5_0.y + var_5_2.y

	local var_5_4 = var_0_1.GetGameItems()

	for iter_5_0 = 1, #var_5_4:
		local var_5_5 = var_5_4[iter_5_0]

		if var_5_5.getConfig("type") == SailBoatGameConst.item_static:
			local var_5_6 = var_5_5.getPosition()

			if math.abs(var_5_6.x - var_5_0.x) < 500 and math.abs(var_5_6.y - var_5_0.y) < 500:
				local var_5_7, var_5_8 = var_5_5.getColliderData()

				if not arg_5_0.checkLeave(arg_5_3, arg_5_4, var_5_0, var_5_6) and var_0_1.CheckRectCollider(var_5_3, var_5_7, var_5_1, var_5_8):
					return True

	return False

def var_0_0.checkLeave(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	local var_6_0
	local var_6_1
	local var_6_2 = False
	local var_6_3
	local var_6_4

	if arg_6_1 != 0:
		var_6_3 = arg_6_3.x > arg_6_4.x and arg_6_1 == 1 and True or arg_6_3.x <= arg_6_4.x and arg_6_1 == -1 and True or False

	if arg_6_2 != 0:
		var_6_4 = arg_6_3.y > arg_6_4.y and arg_6_2 == 1 and True or arg_6_3.y <= arg_6_4.y and arg_6_2 == -1 and True or False

	if arg_6_1 != 0 and arg_6_2 != 0:
		-- block empty
	elif arg_6_1 != 0 and arg_6_2 == 0:
		var_6_2 = var_6_3
	elif arg_6_1 == 0 and arg_6_2 != 0:
		var_6_2 = var_6_4

	return var_6_2

def var_0_0.ableFire(arg_7_0):
	return

def var_0_0.clear(arg_8_0):
	return

def var_0_0.stop(arg_9_0):
	return

def var_0_0.dispose(arg_10_0):
	return

def var_0_0.useSkill(arg_11_0):
	arg_11_0._char.useSkill()

def var_0_0.onEventCall(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_1 == SailBoatGameEvent.PLAYER_EVENT_DAMAGE:
		arg_12_0._char.damage(arg_12_2)
	elif arg_12_1 == SailBoatGameEvent.USE_ITEM:
		local var_12_0 = arg_12_2.hp

		arg_12_0._char.addHp(var_12_0)

return var_0_0
