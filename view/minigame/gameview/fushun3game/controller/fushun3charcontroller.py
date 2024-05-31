local var_0_0 = class("Fushun3CharController")
local var_0_1 = 3

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	arg_1_0._rectCollider = arg_1_1
	arg_1_0._charTf = arg_1_2
	arg_1_0._anim = findTF(arg_1_0._charTf, "anim")
	arg_1_0._pos = findTF(arg_1_0._charTf, "pos")
	arg_1_0._itemPos = findTF(arg_1_0._charTf, "itemPos")
	arg_1_0._dftEvent = GetOrAddComponent(arg_1_0._anim, typeof(DftAniEvent))
	arg_1_0._effectPos = findTF(arg_1_0._charTf, "effectPos")
	arg_1_0._effectFrPos = findTF(arg_1_0._charTf, "effectFrPos")
	arg_1_0._effectBkPos = findTF(arg_1_0._charTf, "effectBkPos")
	arg_1_0._powerSlider = arg_1_4

	arg_1_0._dftEvent.SetTriggerEvent(function()
		local var_2_0
		local var_2_1 = arg_1_0._animator.GetCurrentAnimatorClipInfo(0)

		if var_2_1 and var_2_1.Length > 0:
			var_2_0 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.AnimatorClipInfo"), "clip", var_2_1[0])

		if var_2_0:
			arg_1_0._event.emit(Fushun3GameEvent.add_anim_effect_call, {
				clipName = var_2_0.name,
				targetTf = arg_1_0._effectPos
			}))

	arg_1_0._charItemCatchTf = findTF(arg_1_0._effectPos, "charItem")
	arg_1_0._charItemCatch = GetComponent(findTF(arg_1_0._charItemCatchTf, "catch"), typeof(Animator))
	arg_1_0._charShieldTf = findTF(arg_1_0._effectPos, "shield")
	arg_1_0._collisionInfo = arg_1_3
	arg_1_0._event = arg_1_5
	arg_1_0._animator = GetComponent(arg_1_0._anim, typeof(Animator))
	arg_1_0._powerScript = arg_1_0._rectCollider.getScript(FuShunPowerSpeedScript)
	arg_1_0._jumpScript = arg_1_0._rectCollider.getScript(FuShunJumpScript)
	arg_1_0._damageScript = arg_1_0._rectCollider.getScript(FuShunDamageScript)
	arg_1_0._attackScript = arg_1_0._rectCollider.getScript(FuShunAttakeScript)
	arg_1_0._monsterLayer = LayerMask.NameToLayer("Character")
	arg_1_0._damageTf = findTF(arg_1_0._charTf, "damage")
	arg_1_0._damageCollider = GetComponent(arg_1_0._damageTf, typeof(BoxCollider2D))
	arg_1_0._attackCd = None

	arg_1_0._event.bind(Fushun3GameEvent.script_jump_event, function()
		if arg_1_0._attackCd == 0 and arg_1_0.damageCd == 0 and arg_1_0._animator:
			arg_1_0._animator.SetTrigger("jump")
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_JUMP))
	arg_1_0._event.bind(Fushun3GameEvent.script_attack_event, function()
		if arg_1_0._attackCd == 0 and arg_1_0.damageCd == 0:
			arg_1_0._animator.SetTrigger("attack")

			arg_1_0._attackCd = Fushun3GameConst.attack_cd

			if arg_1_0.getBuff(Fushun3GameConst.buff_weapon):
				local var_4_0 = math.random(1, 30) == 1 and "tamachan" or "rocket"

				arg_1_0._event.emit(Fushun3GameEvent.create_item_call, {
					name = var_4_0,
					pos = arg_1_0._itemPos.position
				})
				arg_1_0._charItemCatch.SetTrigger("attack")
			else
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_ATTACK)

				arg_1_0._attackTime = Fushun3GameConst.attack_time)
	arg_1_0._event.bind(Fushun3GameEvent.script_power_event, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0._animator.SetTrigger("ex")
		arg_1_0._charItemCatch.SetTrigger("ex"))

	arg_1_0.damageCd = 0
	arg_1_0.buffList = {}

	if Application.isEditor:
		if not arg_1_0.handle:
			arg_1_0.handle = UpdateBeat.CreateListener(function()
				if Input.GetKeyDown(KeyCode.Y):
					local var_6_0 = 1

					if arg_1_0.getBuffById(Fushun3GameConst.buff_data[var_6_0].id):
						arg_1_0.removeBuff(Clone(Fushun3GameConst.buff_data[var_6_0]))
					else
						arg_1_0.addBuff(Clone(Fushun3GameConst.buff_data[var_6_0]))
				elif Input.GetKeyDown(KeyCode.U):
					local var_6_1 = 2
					local var_6_2 = Fushun3GameConst.buff_data[var_6_1]

					if arg_1_0.getBuffById(var_6_2.id):
						arg_1_0.removeBuff(Clone(Fushun3GameConst.buff_data[var_6_1]))
					else
						arg_1_0.addBuff(Clone(Fushun3GameConst.buff_data[var_6_1]))
				elif Input.GetKeyDown(KeyCode.I):
					local var_6_3 = 4

					if arg_1_0.getBuffById(Fushun3GameConst.buff_data[var_6_3].id):
						arg_1_0.removeBuff(Clone(Fushun3GameConst.buff_data[var_6_3]))
					else
						arg_1_0.addBuff(Clone(Fushun3GameConst.buff_data[var_6_3]))
				elif Input.GetKeyDown(KeyCode.O):
					local var_6_4 = 5

					arg_1_0.addBuff(Clone(Fushun3GameConst.buff_data[var_6_4])), arg_1_0)

		UpdateBeat.AddListener(arg_1_0.handle, arg_1_0)

def var_0_0.start(arg_7_0):
	arg_7_0._animator.SetBool("la", False)
	arg_7_0._animator.SetBool("s", False)
	arg_7_0._animator.SetBool("below", arg_7_0._collisionInfo.below)

	arg_7_0._attackCd = Fushun3GameConst.attack_cd
	arg_7_0._charTf.anchoredPosition = Fushun3GameConst.char_init_pos
	arg_7_0.buffList = {}
	arg_7_0._attackTime = 0
	arg_7_0.power = 0
	arg_7_0._powerTime = 0
	arg_7_0.powerFlag = False
	arg_7_0.shieldNum = 0

	arg_7_0.updateBuffShow(Fushun3GameConst.buff_shield)

	arg_7_0.heart = Fushun3GameConst.heart_num

	setActive(arg_7_0._charItemCatchTf, False)

def var_0_0.step(arg_8_0):
	if arg_8_0._charTf.anchoredPosition.y >= 1200 or arg_8_0._charTf.anchoredPosition.y <= -200:
		if arg_8_0._powerTime > 0:
			arg_8_0._charTf.anchoredPosition = Vector2(arg_8_0._charTf.anchoredPosition.x + 100, 1000)
		else
			arg_8_0._event.emit(Fushun3GameEvent.game_over_call)

		return

	arg_8_0._powerSlider.value = arg_8_0.power / Fushun3GameConst.power_max_num

	arg_8_0._animator.SetBool("below", arg_8_0._collisionInfo.below)

	local var_8_0 = arg_8_0._collisionInfo.getVelocity()

	arg_8_0._animator.SetFloat("moveAmountX", var_8_0.x)
	arg_8_0._animator.SetFloat("moveAmountY", var_8_0.y)

	if arg_8_0._attackCd > 0:
		arg_8_0._attackCd = arg_8_0._attackCd - Time.deltaTime
		arg_8_0._attackCd = arg_8_0._attackCd < 0 and 0 or arg_8_0._attackCd

	if arg_8_0._powerTime > 0:
		arg_8_0._powerTime = arg_8_0._powerTime - Time.deltaTime

		if arg_8_0._powerTime < 0:
			arg_8_0._powerTime = 0

	for iter_8_0 = #arg_8_0.buffList, 1, -1:
		local var_8_1 = arg_8_0.buffList[iter_8_0]

		if var_8_1.time:
			var_8_1.time = var_8_1.time - Time.deltaTime

			if var_8_1.time <= 0:
				arg_8_0.removeBuff(var_8_1)

	local var_8_2 = {}

	for iter_8_1, iter_8_2 in pairs(arg_8_0._collisionInfo.horizontalLeftTfs):
		table.insert(var_8_2, iter_8_2)

	for iter_8_3, iter_8_4 in pairs(arg_8_0._collisionInfo.horizontalRightTfs):
		table.insert(var_8_2, iter_8_4)

	local var_8_3 = {}

	for iter_8_5, iter_8_6 in pairs(arg_8_0._collisionInfo.verticalBottomTfs):
		table.insert(var_8_3, iter_8_6)

	if #var_8_2 > 0:
		if arg_8_0.getBuff(Fushun3GameConst.buff_power_speed):
			for iter_8_7 = 1, #var_8_2:
				if go(var_8_2[iter_8_7]).layer == arg_8_0._monsterLayer:
					arg_8_0._event.emit(Fushun3GameEvent.power_damage_monster_call, {
						tf = var_8_2[iter_8_7]
					})
		else
			for iter_8_8 = 1, #var_8_2:
				if arg_8_0._powerTime == 0 and go(var_8_2[iter_8_8]).layer == arg_8_0._monsterLayer and arg_8_0.damageCd == 0:
					arg_8_0._event.emit(Fushun3GameEvent.check_player_damage, {
						tf = var_8_2[iter_8_8],
						def callback:(arg_9_0)
							if not arg_9_0:
								arg_8_0.damageChar()
					})
				elif findTF(var_8_2[iter_8_8], "high_roof"):
					setActive(findTF(var_8_2[iter_8_8], "high_roof"), False)
					arg_8_0._collisionInfo.changeVelocity(0, arg_8_0._collisionInfo.config.minJumpVelocity, None)

					if arg_8_0._powerTime == 0 and arg_8_0.damageCd == 0:
						arg_8_0.damageChar()
	elif var_8_3 and #var_8_3 > 0:
		for iter_8_9 = 1, #var_8_3:
			if go(var_8_3[iter_8_9]).layer == arg_8_0._monsterLayer:
				if arg_8_0.getBuff(Fushun3GameConst.buff_speed):
					arg_8_0._event.emit(Fushun3GameEvent.kick_damage_monster_call, {
						tf = var_8_3[iter_8_9],
						def callback:(arg_10_0)
							if arg_10_0:
								arg_8_0._collisionInfo.changeVelocity(None, arg_8_0._collisionInfo.config.minJumpVelocity, None)
					})
				else
					arg_8_0._event.emit(Fushun3GameEvent.check_player_damage, {
						tf = var_8_2[iter_8_9],
						def callback:(arg_11_0)
							if not arg_11_0:
								arg_8_0.damageChar()
					})

	arg_8_0.flushBuff()

	if arg_8_0.damageCd > 0:
		arg_8_0.damageCd = arg_8_0.damageCd - Time.deltaTime
		arg_8_0.damageCd = arg_8_0.damageCd <= 0 and 0 or arg_8_0.damageCd

	if arg_8_0._attackTime > 0:
		arg_8_0._event.emit(Fushun3GameEvent.player_attack_call, {
			collider = arg_8_0._damageCollider,
			def callback:(arg_12_0)
				if arg_12_0:
					arg_8_0._event.emit(Fushun3GameEvent.add_effect_call, {
						effectName = "EF_fr_Attack",
						targetTf = arg_8_0._effectPos
					})
		})

		arg_8_0._attackTime = arg_8_0._attackTime - Time.deltaTime
		arg_8_0._attackTime = arg_8_0._attackTime <= 0 and 0 or arg_8_0._attackTime

	if arg_8_0.power == Fushun3GameConst.power_max_num and not arg_8_0.powerFlag and arg_8_0._charTf.anchoredPosition.y >= 200:
		arg_8_0.powerFlag = True

		arg_8_0._event.emit(Fushun3GameEvent.power_speed_call)

		if not arg_8_0.powerBuff:
			for iter_8_10 = 1, #Fushun3GameConst.buff_data:
				if Fushun3GameConst.buff_data[iter_8_10].buff == Fushun3GameConst.buff_power_speed:
					arg_8_0.powerBuff = Clone(Fushun3GameConst.buff_data[iter_8_10])

		arg_8_0.addBuff(Clone(arg_8_0.powerBuff))

	if arg_8_0.powerFlag:
		arg_8_0.power = arg_8_0.power - Fushun3GameConst.power_sub_time * Time.deltaTime

		if arg_8_0.power <= 0:
			arg_8_0.power = 0
			arg_8_0.powerFlag = False

			arg_8_0.removeBuff(Clone(arg_8_0.powerBuff))
	elif arg_8_0.power >= Fushun3GameConst.power_max_num:
		arg_8_0.power = Fushun3GameConst.power_max_num

def var_0_0.jump(arg_13_0):
	if arg_13_0._jumpScript.checkScirptApply():
		arg_13_0._jumpScript.active(True)

def var_0_0.attack(arg_14_0):
	if arg_14_0._attackScript.checkScirptApply():
		arg_14_0._attackScript.active(True)

def var_0_0.damageChar(arg_15_0):
	if arg_15_0._damageScript.checkScirptApply():
		arg_15_0._damageScript.active(True)

		if arg_15_0.damageCd == 0:
			if arg_15_0.shieldNum > 0:
				arg_15_0.shieldNum = arg_15_0.shieldNum - 1

				arg_15_0._animator.SetTrigger("damage")
				arg_15_0.updateBuffShow(Fushun3GameConst.buff_shield)
				arg_15_0._event.emit(Fushun3GameEvent.add_effect_call, {
					effectName = "EF_Barrier_Break",
					targetTf = arg_15_0._effectPos
				})
			else
				arg_15_0.heart = arg_15_0.heart - 1

				if arg_15_0.heart <= 0:
					arg_15_0.heart = 0

				if arg_15_0.heart == 0:
					arg_15_0._animator.SetTrigger("down")
				elif #arg_15_0.buffList > 0:
					arg_15_0.removeBuff(arg_15_0.buffList[math.random(1, #arg_15_0.buffList)], True)
					arg_15_0._animator.SetTrigger("respawn")
				else
					arg_15_0._animator.SetTrigger("damage")

			arg_15_0.damageCd = Fushun3GameConst.damage_cd

			if arg_15_0._attackTime > 0:
				arg_15_0._attackTime = 0

			arg_15_0._event.emit(Fushun3GameEvent.char_damaged_call)

def var_0_0.addPower(arg_16_0, arg_16_1):
	if not arg_16_0.powerFlag:
		arg_16_0.power = arg_16_0.power + arg_16_1

def var_0_0.getBuff(arg_17_0, arg_17_1):
	for iter_17_0 = 1, #arg_17_0.buffList:
		if arg_17_0.buffList[iter_17_0].buff == arg_17_1:
			return arg_17_0.buffList[iter_17_0]

	return None

def var_0_0.getBuffById(arg_18_0, arg_18_1):
	for iter_18_0 = 1, #arg_18_0.buffList:
		if arg_18_0.buffList[iter_18_0].id == arg_18_1:
			return arg_18_0.buffList[iter_18_0]

	return None

def var_0_0.setBuff(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_1.buff_id
	local var_19_1

	for iter_19_0 = 1, #Fushun3GameConst.buff_data:
		if Fushun3GameConst.buff_data[iter_19_0].id == var_19_0:
			var_19_1 = Fushun3GameConst.buff_data[iter_19_0]

	if var_19_1:
		arg_19_0.addBuff(Clone(var_19_1))

def var_0_0.addBuff(arg_20_0, arg_20_1):
	for iter_20_0 = 1, #arg_20_0.buffList:
		if arg_20_0.buffList[iter_20_0].id == arg_20_1.id:
			if arg_20_1.buff == Fushun3GameConst.buff_shield:
				if arg_20_0.shieldNum == var_0_1:
					return
			else
				return

	local var_20_0 = arg_20_0.getItemTriggerFlag()

	if arg_20_1.buff == Fushun3GameConst.buff_speed:
		arg_20_0._animator.SetBool("s", True)

		arg_20_0._collisionInfo.config.moveSpeed = Fushun3GameConst.move_speed_shoose

		if not var_20_0:
			arg_20_0._animator.SetTrigger("item")
	elif arg_20_1.buff == Fushun3GameConst.buff_power_speed:
		if arg_20_0._powerScript.checkScirptApply():
			arg_20_0._powerScript.active(True)
			arg_20_0._animator.SetTrigger("ex_on")
			arg_20_0._charItemCatch.SetTrigger("ex_on")
	elif arg_20_1.buff == Fushun3GameConst.buff_weapon:
		arg_20_0._animator.SetBool("la", True)

		if not var_20_0:
			arg_20_0._animator.SetTrigger("item")
	elif arg_20_1.buff == Fushun3GameConst.buff_catch:
		setActive(arg_20_0._charItemCatchTf, True)
		arg_20_0._charItemCatch.SetTrigger("ride")
	elif arg_20_1.buff == Fushun3GameConst.buff_shield:
		arg_20_0.shieldNum = arg_20_0.shieldNum + 1

		if arg_20_0.shieldNum > var_0_1:
			arg_20_0.shieldNum = var_0_1

		arg_20_0.updateBuffShow(Fushun3GameConst.buff_shield)
		arg_20_0._event.emit(Fushun3GameEvent.add_effect_call, {
			effectName = "EF_Barrier_Get",
			targetTf = arg_20_0._effectPos
		})

	table.insert(arg_20_0.buffList, arg_20_1)

def var_0_0.updateBuffShow(arg_21_0, arg_21_1):
	if arg_21_1 == Fushun3GameConst.buff_shield:
		for iter_21_0 = 1, var_0_1:
			local var_21_0 = iter_21_0
			local var_21_1 = findTF(arg_21_0._charShieldTf, tostring(var_21_0))

			setActive(var_21_1, var_21_0 <= arg_21_0.shieldNum)
			setActive(findTF(arg_21_0._effectFrPos, "Barrier/" .. tostring(var_21_0)), arg_21_0.shieldNum == var_21_0)
			setActive(findTF(arg_21_0._effectBkPos, "Barrier/" .. tostring(var_21_0)), arg_21_0.shieldNum == var_21_0)

		setActive(arg_21_0._charShieldTf, False)
		setActive(arg_21_0._charShieldTf, True)

def var_0_0.removeBuff(arg_22_0, arg_22_1, arg_22_2):
	for iter_22_0 = 1, #arg_22_0.buffList:
		local var_22_0 = arg_22_0.buffList[iter_22_0]

		if var_22_0.buff == arg_22_1.buff:
			local var_22_1 = arg_22_0.getItemTriggerFlag()

			if var_22_0.buff == Fushun3GameConst.buff_speed:
				arg_22_0._animator.SetBool("s", False)

				arg_22_0._collisionInfo.config.moveSpeed = Fushun3GameConst.move_speed

				if not var_22_1 and not arg_22_2:
					arg_22_0._animator.SetTrigger("item")
			elif var_22_0.buff == Fushun3GameConst.buff_power_speed:
				arg_22_0._powerScript.active(False)
				arg_22_0._animator.SetTrigger("ex_off")
				arg_22_0._charItemCatch.SetTrigger("ex_off")

				arg_22_0._powerTime = Fushun3GameConst.power_time
			elif var_22_0.buff == Fushun3GameConst.buff_weapon:
				arg_22_0._animator.SetBool("la", False)

				if not var_22_1 and not arg_22_2:
					arg_22_0._animator.SetTrigger("item")
			elif var_22_0.buff == Fushun3GameConst.buff_catch:
				setActive(arg_22_0._charItemCatchTf, False)

			table.remove(arg_22_0.buffList, iter_22_0)

			return

def var_0_0.flushBuff(arg_23_0):
	for iter_23_0 = 1, #arg_23_0.buffList:
		local var_23_0 = arg_23_0.buffList[iter_23_0]

		if var_23_0.buff == Fushun3GameConst.buff_speed:
			-- block empty
		elif var_23_0.buff == Fushun3GameConst.buff_power_speed:
			-- block empty
		elif var_23_0.buff == Fushun3GameConst.buff_weapon:
			-- block empty
		elif var_23_0.buff == Fushun3GameConst.buff_catch:
			local var_23_1 = arg_23_0._charTf.anchoredPosition

			var_23_1.y = var_23_1.y + arg_23_0._itemPos.anchoredPosition.y

			arg_23_0._event.emit(Fushun3GameEvent.item_follow_call, {
				anchoredPos = var_23_1
			})

def var_0_0.getHeart(arg_24_0):
	return arg_24_0.heart

def var_0_0.getItemTriggerFlag(arg_25_0):
	for iter_25_0 = 1, #arg_25_0.buffList:
		if arg_25_0.buffList[iter_25_0].lock_item:
			return True

	return False

def var_0_0.dispose(arg_26_0):
	if Application.isEditor:
		UpdateBeat.RemoveListener(arg_26_0.handle)

		arg_26_0.handle = None

return var_0_0
