local var_0_0 = class("SailBoatColliderControl")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._eventCall = arg_1_2

def var_0_0.start(arg_2_0):
	arg_2_0._itemMoveSpeed = var_0_1.item_move_speed

def var_0_0.step(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1.GetGameChar()
	local var_3_1 = var_0_1.GetGameItems()
	local var_3_2 = var_0_1.GetGameEnemys()
	local var_3_3, var_3_4 = var_3_0.getWorldColliderData()
	local var_3_5 = var_3_0.getPosition()
	local var_3_6 = False

	for iter_3_0 = 1, #var_3_1:
		local var_3_7 = var_3_1[iter_3_0]
		local var_3_8, var_3_9 = var_3_7.getWorldColliderData()

		if var_0_1.CheckRectCollider(var_3_3, var_3_8, var_3_4, var_3_9):
			if var_3_7.getConfig("type") == SailBoatGameConst.item_static:
				local var_3_10 = var_3_7.getSpeed()

				var_3_0.move(var_3_10.x, var_3_10.y)
			elif var_3_7.getConfig("type") == SailBoatGameConst.item_used:
				arg_3_0._eventCall(SailBoatGameEvent.USE_ITEM, var_3_7.getUseData())
				var_3_7.setRemoveFlag(True)
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1.SFX_SOUND_ITEM)

	for iter_3_1 = 1, #var_3_2:
		local var_3_11 = var_3_2[iter_3_1]

		if var_3_11.getLife():
			local var_3_12, var_3_13 = var_3_11.getWorldColliderData()

			if var_0_1.CheckRectCollider(var_3_3, var_3_12, var_3_4, var_3_13):
				if var_3_11.getConfig("boom") and var_3_11.getConfig("boom") > 0:
					if var_3_11.damage({
						num = 999
					}):
						arg_3_0._eventCall(SailBoatGameEvent.DESTROY_ENEMY, var_3_11.getDestroyData())
				elif var_3_0.checkColliderDamage():
					var_3_0.flash()
					var_3_0.damage({
						num = var_0_1.colliderDamage
					})

def var_0_0.dispose(arg_4_0):
	return

def var_0_0.clear(arg_5_0):
	return

return var_0_0
