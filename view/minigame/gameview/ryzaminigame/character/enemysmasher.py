local var_0_0 = class("EnemySmasher", import("view.miniGame.gameView.RyzaMiniGame.character.MoveEnemy"))

var_0_0.ConfigSkillCD = 10
var_0_0.ConfigSkillCount = 3
var_0_0.ImpackRange = 20

def var_0_0.InitUI(arg_1_0, arg_1_1):
	var_0_0.super.InitUI(arg_1_0, arg_1_1)

	arg_1_0.hp = arg_1_1.hp or 2
	arg_1_0.hpMax = arg_1_0.hp
	arg_1_0.speed = arg_1_1.speed or 2

	eachChild(arg_1_0.rtScale.Find("front"), function(arg_2_0)
		arg_2_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_2_0, False)))
	arg_1_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function()
		arg_1_0.triggerCount = defaultValue(arg_1_0.triggerCount, 0) + 1

		switch(arg_1_0.triggerCount, {
			function()
				setActive(arg_1_0.rtScale.Find("front/EF_Bullet_UP"), True),
			function()
				setActive(arg_1_0.rtScale.Find("front/EF_Bullet_UP_High"), True)
		})

		arg_1_0.triggerCount = arg_1_0.triggerCount % 2)
	arg_1_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		switch(arg_1_0.status, {
			def Attack_S:()
				arg_1_0.impackCD = 0
				arg_1_0.impackCount = arg_1_0.ConfigSkillCount
		})

		arg_1_0.lock = False

		if arg_1_0.hp <= 0:
			arg_1_0.Destroy())

	arg_1_0.skillCD = 0
	arg_1_0.impackCount = 0

def var_0_0.TimeTrigger(arg_9_0, arg_9_1):
	var_0_0.super.TimeTrigger(arg_9_0, arg_9_1)

	arg_9_0.skillCD = arg_9_0.skillCD - arg_9_1

	if not arg_9_0.lock and arg_9_0.skillCD <= 0 and arg_9_0.responder.SearchRyza(arg_9_0, arg_9_0.search) and (arg_9_0.responder.reactorRyza.pos - arg_9_0.pos).SqrMagnitude() >= 4:
		arg_9_0.PlayAnim("Attack_S")

		arg_9_0.skillCD = arg_9_0.ConfigSkillCD
		arg_9_0.skillCenterPos = arg_9_0.responder.reactorRyza.realPos

	local function var_9_0()
		if arg_9_0.responder.reactorRyza.hide:
			return False
		else
			local var_10_0 = arg_9_0.responder.reactorRyza.realPos - arg_9_0.skillCenterPos

			return var_10_0.x * var_10_0.x < arg_9_0.ImpackRange * arg_9_0.ImpackRange / 4 and var_10_0.y * var_10_0.y < arg_9_0.ImpackRange * arg_9_0.ImpackRange / 4

	if arg_9_0.impackCount > 0:
		if var_9_0():
			arg_9_0.impackCD = arg_9_0.impackCD - arg_9_1

			if arg_9_0.impackCD <= 0:
				arg_9_0.impackCount = arg_9_0.impackCount - 1
				arg_9_0.impackCD = 0.5

				local var_9_1 = arg_9_0.responder.reactorRyza.pos
				local var_9_2 = arg_9_0.responder.reactorRyza.realPos

				arg_9_0.responder.Create({
					name = "Impack",
					pos = {
						var_9_1.x,
						var_9_1.y
					},
					realPos = {
						var_9_2.x,
						var_9_2.y
					}
				})
		else
			arg_9_0.impackCount = 0
			arg_9_0.impackCD = None

return var_0_0
