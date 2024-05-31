local var_0_0 = class("SailBoatBulletsControl")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._bullets = {}
	arg_1_0._bulletPool = {}
	arg_1_0._content = findTF(arg_1_0._tf, "scene_front/content")

def var_0_0.start(arg_2_0):
	for iter_2_0 = #arg_2_0._bullets, 1, -1:
		local var_2_0 = table.remove(arg_2_0._bullets, iter_2_0)

		var_2_0.clear()
		table.insert(arg_2_0._bulletPool, var_2_0)

	arg_2_0._bulletStep = var_0_1.bullet_step

def var_0_0.step(arg_3_0, arg_3_1):
	for iter_3_0 = #arg_3_0._bullets, 1, -1:
		arg_3_0._bullets[iter_3_0].step(arg_3_1)

	arg_3_0._bulletStep = arg_3_0._bulletStep - 1

	if arg_3_0._bulletStep > 0:
		return

	arg_3_0._bulletStep = var_0_1.bullet_step

	local var_3_0 = var_0_1.GetGameEnemys()
	local var_3_1 = var_0_1.GetGameChar()
	local var_3_2 = var_3_1.getGroup()
	local var_3_3 = 0

	for iter_3_1 = #arg_3_0._bullets, 1, -1:
		local var_3_4 = arg_3_0._bullets[iter_3_1]
		local var_3_5 = var_3_4.getHitGroup()
		local var_3_6 = var_3_4.getWorld()

		if not var_3_4.getRemoveFlag():
			for iter_3_2, iter_3_3 in ipairs(var_3_0):
				if iter_3_3.getLife():
					local var_3_7 = iter_3_3.getGroup()

					if iter_3_3.getLife():
						local var_3_8, var_3_9 = iter_3_3.getMinMaxPosition()

						if var_0_1.PointInRect2(var_3_6, var_3_8, var_3_9) and table.contains(var_3_5, var_3_7):
							var_3_4.hit()

							local var_3_10 = var_3_4.getDamage()

							if iter_3_3.damage(var_3_10):
								arg_3_0._event(SailBoatGameEvent.DESTROY_ENEMY, iter_3_3.getDestroyData())

							return

		if not var_3_4.getRemoveFlag() and var_3_1.getLife() and table.contains(var_3_5, var_3_2):
			local var_3_11, var_3_12 = var_3_1.getMinMaxPosition()

			if var_0_1.PointInRect2(var_3_6, var_3_11, var_3_12):
				var_3_4.hit()

				local var_3_13 = var_3_4.getDamage()

				var_3_1.damage(var_3_13)

				return

		if var_3_4.getRemoveFlag():
			local var_3_14 = table.remove(arg_3_0._bullets, iter_3_1)

			var_3_14.clear()
			arg_3_0.returnBullet(var_3_14)

def var_0_0.returnBullet(arg_4_0, arg_4_1):
	table.insert(arg_4_0._bulletPool, arg_4_1)

def var_0_0.createBullet(arg_5_0, arg_5_1):
	local var_5_0

	if #arg_5_0._bulletPool > 0:
		var_5_0 = table.remove(arg_5_0._bulletPool, 1)

	if not var_5_0:
		local var_5_1 = var_0_1.GetGameBullet()

		var_5_0 = SailBoatBullet.New(var_5_1, arg_5_0._event)

		var_5_0.setContent(arg_5_0._content)

	local var_5_2 = SailBoatGameConst.game_bullet[arg_5_1]

	var_5_0.setData(var_5_2)
	table.insert(arg_5_0._bullets, var_5_0)

	return var_5_0

def var_0_0.onEventCall(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_1 == SailBoatGameEvent.BOAT_EVENT_FIRE:
		local var_6_0 = arg_6_0.createBullet(arg_6_2.bullet_id)

		var_6_0.setFireData(arg_6_2.fire_data)
		var_6_0.setWeapon(arg_6_2.weapon_data)
		var_6_0.start()

def var_0_0.dispose(arg_7_0):
	return

def var_0_0.clear(arg_8_0):
	return

return var_0_0
