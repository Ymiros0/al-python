local var_0_0 = class("FushunBeastChar")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.index = arg_1_2
	arg_1_0.template_id = arg_1_3.id
	arg_1_0.name = arg_1_3.name
	arg_1_0.dir = -1
	arg_1_0.maxHp = arg_1_3.hp
	arg_1_0.hp = arg_1_3.hp
	arg_1_0.attackDistance = arg_1_3.attackDistance
	arg_1_0.score = arg_1_3.score
	arg_1_0.energyScore = arg_1_3.energyScore
	arg_1_0.escape = False
	arg_1_0.freeze = False
	arg_1_0.attacking = False
	arg_1_0.animator = arg_1_0._go.GetComponent(typeof(Animator))
	arg_1_0.animatorEvent = arg_1_0._go.GetComponent(typeof(DftAniEvent))
	arg_1_0.collider2D = arg_1_0._tf.GetComponent(typeof(UnityEngine.Collider2D))
	arg_1_0.effectCollider2D = arg_1_0._tf.Find("effect").GetComponent(typeof(UnityEngine.Collider2D))
	arg_1_0.hpBar = UIItemList.New(arg_1_1.transform.Find("hp"), arg_1_1.transform.Find("hp/tpl"))
	arg_1_0.fushunLoader = arg_1_4

	arg_1_0.MakeHpBar()

def var_0_0.MakeHpBar(arg_2_0):
	setActive(arg_2_0.hpBar.container, True)
	arg_2_0.hpBar.make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventUpdate:
			setActive(arg_3_2.Find("mark"), arg_3_1 < arg_2_0.hp))
	arg_2_0.hpBar.align(arg_2_0.maxHp)

def var_0_0.SetSpeed(arg_4_0, arg_4_1):
	arg_4_0.speed = arg_4_1

def var_0_0.SetPosition(arg_5_0, arg_5_1):
	arg_5_0._tf.localPosition = arg_5_1

def var_0_0.GetPosition(arg_6_0):
	return arg_6_0._tf.localPosition

def var_0_0.GetAttackPosition(arg_7_0):
	return arg_7_0._tf.localPosition - Vector3(arg_7_0.attackDistance, 0, 0)

def var_0_0.Move(arg_8_0):
	if arg_8_0.attacking:
		return

	arg_8_0._tf.Translate(Vector3(-1 * arg_8_0.speed * Time.deltaTime, 0, 0))
	arg_8_0.animator.SetFloat("speed", arg_8_0.speed)

def var_0_0.Attack(arg_9_0):
	arg_9_0.animatorEvent.SetEndEvent(None)
	arg_9_0.animatorEvent.SetEndEvent(function()
		arg_9_0.attacking = False

		arg_9_0.Unfreeze()
		arg_9_0.Die())
	arg_9_0.animatorEvent.SetTriggerEvent(None)
	arg_9_0.animatorEvent.SetTriggerEvent(function()
		setActive(arg_9_0.hpBar.container, False))

	arg_9_0.attacking = True

	arg_9_0.animator.SetTrigger("attack")

def var_0_0.OnHit(arg_12_0):
	arg_12_0.escape = True

	arg_12_0.Freeze()

def var_0_0.IsEscape(arg_13_0):
	return arg_13_0.escape

def var_0_0.Die(arg_14_0):
	arg_14_0.UpdateHp(0)

def var_0_0.Hurt(arg_15_0, arg_15_1):
	if arg_15_0.IsDeath() or arg_15_0.IsEscape():
		return

	arg_15_0.UpdateHp(arg_15_0.hp - arg_15_1)

def var_0_0.UpdateHp(arg_16_0, arg_16_1):
	arg_16_0.hp = math.max(arg_16_1, 0)

	arg_16_0.hpBar.align(arg_16_0.maxHp)

def var_0_0.IsFreeze(arg_17_0):
	return arg_17_0.freeze

def var_0_0.Freeze(arg_18_0):
	arg_18_0.freeze = True

def var_0_0.Unfreeze(arg_19_0):
	arg_19_0.freeze = False

def var_0_0.IsDeath(arg_20_0):
	return arg_20_0.hp <= 0

def var_0_0.WillDeath(arg_21_0):
	return arg_21_0.IsDeath() or arg_21_0.IsEscape()

def var_0_0.GetHp(arg_22_0):
	return arg_22_0.hp

def var_0_0.Vanish(arg_23_0):
	if arg_23_0.vanish:
		return

	if arg_23_0.IsEscape():
		arg_23_0.Dispose()
	else
		arg_23_0.vanish = True

		arg_23_0.animatorEvent.SetEndEvent(None)
		arg_23_0.animatorEvent.SetEndEvent(function()
			arg_23_0.Dispose())
		arg_23_0.animator.SetTrigger("vanish")

	setActive(arg_23_0.hpBar.container, False)

def var_0_0.GetScore(arg_25_0):
	return arg_25_0.score

def var_0_0.GetEnergyScore(arg_26_0):
	return arg_26_0.energyScore

def var_0_0.GetMaxHp(arg_27_0):
	return arg_27_0.maxHp

def var_0_0.Dispose(arg_28_0):
	arg_28_0.animatorEvent.SetTriggerEvent(None)
	arg_28_0.animatorEvent.SetEndEvent(None)
	arg_28_0.fushunLoader.ReturnPrefab("FushunAdventure/" .. arg_28_0.name, "", arg_28_0._go, False)

	arg_28_0._go = None
	arg_28_0._tf = None
	arg_28_0.animator = None

return var_0_0
