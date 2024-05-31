local var_0_0 = class("SailBoatChar")
local var_0_1

var_0_0.fire_cd = 0.1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._eventCallback = arg_1_2
	arg_1_0._collider = GetComponent(findTF(arg_1_0._tf, "bound"), typeof(BoxCollider2D))
	arg_1_0.imgTf = findTF(arg_1_0._tf, "img")
	arg_1_0._animator = GetComponent(arg_1_0.imgTf, typeof(Animator))
	arg_1_0._leftWeapons, arg_1_0._rightWeapons = {}, {}
	arg_1_0._hpTf = findTF(arg_1_0._tf, "hp")
	arg_1_0._hpSlider = GetComponent(findTF(arg_1_0._tf, "hp"), typeof(Slider))

	setActive(arg_1_0._tf, False)

	arg_1_0._playerAnimator = GetComponent(arg_1_0._tf, typeof(Animator))

def var_0_0.setData(arg_2_0, arg_2_1):
	arg_2_0._data = arg_2_1
	arg_2_0._baseSpeed = arg_2_0.getConfig("speed")
	arg_2_0._baseHp = arg_2_0.getConfig("hp")

def var_0_0.setWeapon(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0._leftWeapons and #arg_3_0._leftWeapons > 0:
		for iter_3_0 = 1, #arg_3_0._leftWeapons:
			arg_3_0._leftWeapons[iter_3_0].clear()

	if arg_3_0._rightWeapons and #arg_3_0._rightWeapons > 0:
		for iter_3_1 = 1, #arg_3_0._rightWeapons:
			arg_3_0._rightWeapons[iter_3_1].clear()

	arg_3_0._leftWeapons = arg_3_1
	arg_3_0._rightWeapons = arg_3_2
	arg_3_0._weaponMaxDistance = None

def var_0_0.setContent(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._content = arg_4_1

	SetParent(arg_4_0._tf, arg_4_1)

	arg_4_0._tf.anchoredPosition = arg_4_2

def var_0_0.changeDirect(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0._directX = arg_5_1
	arg_5_0._directY = arg_5_2

	if arg_5_0._directX < 0:
		arg_5_0.imgTf.localEulerAngles = Vector3(0, 0, 3)
	elif arg_5_0._directX > 0:
		arg_5_0.imgTf.localEulerAngles = Vector3(0, 0, -3)
	else
		arg_5_0.imgTf.localEulerAngles = Vector3(0, 0, 0)

def var_0_0.getWorld(arg_6_0):
	return arg_6_0._tf.position

def var_0_0.start(arg_7_0):
	arg_7_0._directX = 0
	arg_7_0._directY = 0

	setActive(arg_7_0._tf, True)

	arg_7_0._tf.anchoredPosition = Vector2(0, 0)

	for iter_7_0 = 1, #arg_7_0._leftWeapons:
		arg_7_0._leftWeapons[iter_7_0].start()

	for iter_7_1 = 1, #arg_7_0._rightWeapons:
		arg_7_0._rightWeapons[iter_7_1].start()

	arg_7_0._speed = Vector2(0, 0)
	arg_7_0._speed.x = arg_7_0._baseSpeed.x + arg_7_0.getEquipAttr("speed")
	arg_7_0._speed.y = arg_7_0._baseSpeed.y + arg_7_0.getEquipAttr("speed")
	arg_7_0._hp = arg_7_0._baseHp + arg_7_0.getEquipAttr("hp")
	arg_7_0._hpSlider.minValue = 0
	arg_7_0._hpSlider.maxValue = arg_7_0._hp
	arg_7_0._timeForDead = None
	arg_7_0._fireLeftCd = 0
	arg_7_0._fireRightCd = 0
	arg_7_0._skillTime = 0
	arg_7_0.colliderDamageCd = 0
	arg_7_0._hpSlider.value = arg_7_0._hp

def var_0_0.step(arg_8_0, arg_8_1):
	if arg_8_0.getLife():
		local var_8_0 = arg_8_0.getNextPosition(arg_8_0._directX, arg_8_0._directY)

		if math.abs(var_8_0.x) > var_0_1.scene_width / 2 + 50 or math.abs(var_8_0.y) > var_0_1.scene_height / 2 + 50:
			-- block empty
		else
			arg_8_0._tf.anchoredPosition = var_8_0

		for iter_8_0 = #arg_8_0._leftWeapons, 1, -1:
			arg_8_0._leftWeapons[iter_8_0].step(arg_8_1)

			if arg_8_0._skillTime and arg_8_0._skillTime > 0:
				arg_8_0._leftWeapons[iter_8_0].skillStep(arg_8_1)

		for iter_8_1 = #arg_8_0._rightWeapons, 1, -1:
			arg_8_0._rightWeapons[iter_8_1].step(arg_8_1)

			if arg_8_0._skillTime and arg_8_0._skillTime > 0:
				arg_8_0._rightWeapons[iter_8_1].skillStep(arg_8_1)

	if arg_8_0._skillTime and arg_8_0._skillTime > 0:
		arg_8_0._skillTime = arg_8_0._skillTime - arg_8_1

	if arg_8_0.colliderDamageCd and arg_8_0.colliderDamageCd > 0:
		arg_8_0.colliderDamageCd = arg_8_0.colliderDamageCd - arg_8_1

	if arg_8_0._timeForDead and arg_8_0._timeForDead > 0:
		arg_8_0._timeForDead = arg_8_0._timeForDead - arg_8_1

		if arg_8_0._timeForDead <= 0:
			arg_8_0._timeForDead = None

			arg_8_0._eventCallback(SailBoatGameEvent.PLAYER_DEAD)

	if arg_8_0._fireLeftCd and arg_8_0._fireLeftCd > 0:
		arg_8_0._fireLeftCd = arg_8_0._fireLeftCd - arg_8_1

		if arg_8_0._fireLeftCd <= 0:
			arg_8_0._fireLeftCd = 0

	if arg_8_0._fireRightCd and arg_8_0._fireRightCd > 0:
		arg_8_0._fireRightCd = arg_8_0._fireRightCd - arg_8_1

		if arg_8_0._fireRightCd <= 0:
			arg_8_0._fireRightCd = 0

	if math.abs(arg_8_0._tf.anchoredPosition.x) > var_0_1.scene_width / 2 + 50 or math.abs(arg_8_0._tf.anchoredPosition.y) > var_0_1.scene_height / 2 + 50:
		arg_8_0.damage({
			num = 999,
			position = Vector2(0, 0)
		})

def var_0_0.getHp(arg_9_0):
	return arg_9_0._hp

def var_0_0.getHpPos(arg_10_0):
	return arg_10_0._hpTf.position

def var_0_0.useSkill(arg_11_0):
	arg_11_0._skillTime = SailBoatGameVo.skillTime

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1.SFX_SOUND_SKILL)

def var_0_0.getNextPosition(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = 0

	if arg_12_1 != 0:
		var_12_0 = arg_12_0._speed.x * arg_12_1 * var_0_1.deltaTime

	local var_12_1 = 0

	if arg_12_2 != 0:
		var_12_1 = arg_12_0._speed.y * arg_12_2 * var_0_1.deltaTime

	local var_12_2 = arg_12_0._tf.anchoredPosition

	if var_12_0 != 0 or var_12_1 != 0:
		var_12_2.x = var_12_2.x + var_12_0
		var_12_2.y = var_12_2.y + var_12_1

		return var_12_2

	return var_12_2

def var_0_0.getWeapons(arg_13_0):
	return arg_13_0._leftWeapons, arg_13_0._rightWeapons

def var_0_0.getFirePos(arg_14_0):
	if not arg_14_0._leftFireTf:
		arg_14_0._leftFireTf = findTF(arg_14_0._tf, "leftFire")

	if not arg_14_0._rightFireTf:
		arg_14_0._rightFireTf = findTF(arg_14_0._tf, "rightFire")

	return arg_14_0._content.InverseTransformPoint(arg_14_0._leftFireTf.position), arg_14_0._content.InverseTransformPoint(arg_14_0._rightFireTf.position)

def var_0_0.getFireContent(arg_15_0):
	return arg_15_0._leftFireTf, arg_15_0._rightFireTf

def var_0_0.getWeaponMaxDistance(arg_16_0):
	if not arg_16_0._weaponMaxDistance:
		arg_16_0._weaponMaxDistance = 0

		for iter_16_0 = 1, #arg_16_0._leftWeapons:
			local var_16_0 = arg_16_0._leftWeapons[iter_16_0]

			if var_16_0.getDistance() > arg_16_0._weaponMaxDistance:
				arg_16_0._weaponMaxDistance = var_16_0.getDistance()

		for iter_16_1 = 1, #arg_16_0._rightWeapons:
			local var_16_1 = arg_16_0._rightWeapons[iter_16_1]

			if var_16_1.getDistance() > arg_16_0._weaponMaxDistance:
				arg_16_0._weaponMaxDistance = var_16_1.getDistance()

	return arg_16_0._weaponMaxDistance

def var_0_0.flash(arg_17_0):
	arg_17_0.colliderDamageCd = var_0_1.collider_time

	arg_17_0._playerAnimator.SetTrigger("flash")

def var_0_0.move(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0 = arg_18_0._tf.anchoredPosition

	var_18_0.x = var_18_0.x + arg_18_1
	var_18_0.y = var_18_0.y + arg_18_2
	arg_18_0._tf.anchoredPosition = var_18_0

def var_0_0.getMaxHp(arg_19_0):
	return arg_19_0._baseHp + arg_19_0.getEquipAttr("hp")

def var_0_0.getTf(arg_20_0):
	return arg_20_0._tf

def var_0_0.clearEquipData(arg_21_0):
	arg_21_0._equipData = {}

def var_0_0.setEquipData(arg_22_0, arg_22_1):
	table.insert(arg_22_0._equipData, arg_22_1)

def var_0_0.getEquipAttr(arg_23_0, arg_23_1):
	local var_23_0 = 0

	for iter_23_0 = 1, #arg_23_0._equipData:
		var_23_0 = var_23_0 + arg_23_0._equipData[iter_23_0][arg_23_1]

	return var_23_0

def var_0_0.getColliderData(arg_24_0):
	local var_24_0 = arg_24_0._content.InverseTransformPoint(arg_24_0._collider.bounds.min)

	if not arg_24_0._boundData:
		local var_24_1 = arg_24_0._content.InverseTransformPoint(arg_24_0._collider.bounds.max)

		arg_24_0._boundData = {
			width = math.floor(var_24_1.x - var_24_0.x),
			height = math.floor(var_24_1.y - var_24_0.y)
		}

	return var_24_0, arg_24_0._boundData

def var_0_0.getWorldColliderData(arg_25_0):
	local var_25_0 = arg_25_0._collider.bounds.min

	if not arg_25_0._worldBoundData:
		local var_25_1 = arg_25_0._collider.bounds.max

		arg_25_0._worldBoundData = {
			width = var_25_1.x - var_25_0.x,
			height = var_25_1.y - var_25_0.y
		}

	return var_25_0, arg_25_0._worldBoundData

def var_0_0.addHp(arg_26_0, arg_26_1):
	if arg_26_0.getLife():
		arg_26_0._hp = arg_26_0._hp + arg_26_1

		local var_26_0 = arg_26_0.getMaxHp()

		if var_26_0 < arg_26_0._hp:
			arg_26_0._hp = var_26_0

def var_0_0.getLife(arg_27_0):
	return arg_27_0._hp > 0

def var_0_0.getColliderMinPosition(arg_28_0):
	if not arg_28_0._minPosition:
		arg_28_0._minPosition = arg_28_0._tf.InverseTransformPoint(arg_28_0._collider.bounds.min)

	return arg_28_0._minPosition

def var_0_0.getBoundData(arg_29_0):
	local var_29_0 = arg_29_0._content.InverseTransformPoint(arg_29_0._collider.bounds.min)

	if not arg_29_0._boundData:
		local var_29_1 = arg_29_0._content.InverseTransformPoint(arg_29_0._collider.bounds.max)

		arg_29_0._boundData = {
			width = math.floor(var_29_1.x - var_29_0.x),
			height = math.floor(var_29_1.y - var_29_0.y)
		}

	return arg_29_0._boundData

def var_0_0.getPosition(arg_30_0):
	return arg_30_0._tf.anchoredPosition

def var_0_0.getGroup(arg_31_0):
	return arg_31_0.getConfig("group")

def var_0_0.getHitGroup(arg_32_0):
	return arg_32_0.getConfig("hit_group")

def var_0_0.inFireCd(arg_33_0, arg_33_1):
	if arg_33_1 > 0:
		return arg_33_0._fireRightCd > 0
	else
		return arg_33_0._fireLeftCd > 0

def var_0_0.fire(arg_34_0, arg_34_1):
	if arg_34_1 > 0:
		if arg_34_0._fireRightCd <= 0:
			arg_34_0._fireRightCd = var_0_0.fire_cd

			return True

		return False
	else
		if arg_34_0._fireLeftCd <= 0:
			arg_34_0._fireLeftCd = var_0_0.fire_cd

			return True

		return False

def var_0_0.clear(arg_35_0):
	return

def var_0_0.stop(arg_36_0):
	return

def var_0_0.checkColliderDamage(arg_37_0):
	return arg_37_0.colliderDamageCd <= 0

def var_0_0.damage(arg_38_0, arg_38_1):
	if not arg_38_0.getLife():
		return

	local var_38_0 = arg_38_1.position

	if var_38_0:
		if var_38_0.x > arg_38_0._tf.position.x:
			arg_38_0.setInteger("damage_direct", 1)
		else
			arg_38_0.setInteger("damage_direct", -1)

	arg_38_0._hp = arg_38_0._hp - arg_38_1.num

	if arg_38_0._hp <= 0:
		arg_38_0._hp = 0

		arg_38_0.setTrigger("dead", True)

		arg_38_0._timeForDead = 1
	elif var_38_0:
		arg_38_0.setTrigger("damage")

def var_0_0.setTrigger(arg_39_0, arg_39_1, arg_39_2):
	if arg_39_0.getLife():
		arg_39_0._animator.SetTrigger(arg_39_1)
	elif arg_39_2:
		arg_39_0._animator.SetTrigger(arg_39_1)

def var_0_0.setInteger(arg_40_0, arg_40_1, arg_40_2):
	arg_40_0._animator.SetInteger(arg_40_1, arg_40_2)

def var_0_0.getMinMaxPosition(arg_41_0):
	return arg_41_0._collider.bounds.min, arg_41_0._collider.bounds.max

def var_0_0.getConfig(arg_42_0, arg_42_1):
	return arg_42_0._data[arg_42_1]

def var_0_0.checkPositionInRange(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_0._tf.anchoredPosition
	local var_43_1 = math.abs(var_43_0.x - arg_43_1.x)
	local var_43_2 = math.abs(var_43_0.y - arg_43_1.y)

	if var_43_1 < 250 and var_43_2 < 300:
		return True

	return False

def var_0_0.dispose(arg_44_0):
	return

return var_0_0
