local var_0_0 = {}
local var_0_1 = {
	function()
		local var_1_0 = class("Object")

		var_1_0.colliderSize = None

		function var_1_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
			arg_2_0.rt = arg_2_1
			arg_2_0.pos = arg_2_2

			setAnchoredPosition(arg_2_0.rt, arg_2_0.pos)

			arg_2_0.controller = arg_2_3
			arg_2_0.isTriggered = False

			arg_2_0.Show("base")

		function var_1_0.UpdatePos(arg_3_0, arg_3_1)
			arg_3_0.pos = arg_3_0.pos + arg_3_1

			setAnchoredPosition(arg_3_0.rt, arg_3_0.pos)

		function var_1_0.Show(arg_4_0, arg_4_1)
			arg_4_0.state = arg_4_1

			setActive(arg_4_0.rt, True)

		function var_1_0.Trigger(arg_5_0, arg_5_1)
			arg_5_0.isTriggered = True

			arg_5_0.TriggerEffect(arg_5_1)

		function var_1_0.TriggerEffect(arg_6_0, arg_6_1)
			arg_6_1.TriggerEffect(arg_6_0)

		function var_1_0.Clear(arg_7_0)
			table.removebyvalue(arg_7_0.controller.queue, arg_7_0)
			Destroy(arg_7_0.rt)

		return var_1_0,
	function()
		return (class("StartMark", var_0_0.Object)),
	function()
		local var_9_0 = class("Mire", var_0_0.Object)

		var_9_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}

		function var_9_0.Trigger(arg_10_0, arg_10_1)
			arg_10_0.isTriggered = True

			if arg_10_1.invincibleTime:
				-- block empty
			else
				arg_10_0.TriggerEffect(arg_10_1)

		return var_9_0,
	function()
		local var_11_0 = class("SpeedBumps", var_0_0.Object)

		var_11_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}

		function var_11_0.Trigger(arg_12_0, arg_12_1)
			arg_12_0.isTriggered = True

			if arg_12_1.invincibleTime:
				-- block empty
			else
				arg_12_0.TriggerEffect(arg_12_1)

		return var_11_0,
	function()
		local var_13_0 = class("Obstacle", var_0_0.Object)

		var_13_0.actionDic = {}

		function var_13_0.Ctor(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
			arg_14_0.rt = arg_14_1
			arg_14_0.pos = arg_14_2

			setAnchoredPosition(arg_14_0.rt, arg_14_0.pos)

			arg_14_0.controller = arg_14_3
			arg_14_0.isTriggered = False
			arg_14_0.comSpineAnim = arg_14_1.Find("GameObject").GetComponent("SpineAnimUI")

			arg_14_0.comSpineAnim.SetActionCallBack(function(arg_15_0)
				if arg_15_0 == "finish":
					arg_14_0.ActionCallback())
			arg_14_0.Show("base")

		function var_13_0.ActionCallback(arg_16_0)
			switch(arg_16_0.state, {
				def base:()
					return,
				def trigger:()
					arg_16_0.Clear(),
				def broken:()
					arg_16_0.Clear()
			})

		function var_13_0.Show(arg_20_0, ...)
			var_13_0.super.Show(arg_20_0, ...)

			arg_20_0.action = arg_20_0.actionDic[arg_20_0.state]

			arg_20_0.comSpineAnim.SetAction(arg_20_0.action, 0)

		function var_13_0.Trigger(arg_21_0, arg_21_1)
			arg_21_0.isTriggered = True

			if arg_21_1.invincibleTime:
				arg_21_0.Show("broken")
				pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-crash")
			else
				arg_21_0.Show("trigger")
				arg_21_0.TriggerEffect(arg_21_1)

		return var_13_0,
	function()
		local var_22_0 = class("TrafficCone", var_0_0.Obstacle)

		var_22_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}
		var_22_0.actionDic = {
			trigger = "roadblocks_vanish1",
			broken = "roadblocks_smash1",
			base = "roadblocks_normal1"
		}

		return var_22_0,
	function()
		local var_23_0 = class("Roadblock", var_0_0.Obstacle)

		var_23_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}
		var_23_0.actionDic = {
			trigger = "roadblocks_vanish2",
			broken = "roadblocks_smash2",
			base = "roadblocks_normal2"
		}

		return var_23_0,
	function()
		local var_24_0 = class("Bomb", var_0_0.Obstacle)

		var_24_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}
		var_24_0.actionDic = {
			trigger = "bomb",
			broken = "bombsmash",
			base = "bomb_normal"
		}

		function var_24_0.Trigger(arg_25_0, arg_25_1)
			arg_25_0.isTriggered = True

			if arg_25_1.invincibleTime:
				arg_25_0.Show("broken")
			else
				arg_25_0.Show("trigger")

				arg_25_0.rt.Find("GameObject").GetComponent("SkeletonGraphic").color = Color.New(1, 1, 1, 0)

				setActive(arg_25_0.rt.Find("GameObject/saiche_zhadan"), True)
				arg_25_0.TriggerEffect(arg_25_1)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/baozha1")

		return var_24_0,
	function()
		local var_26_0 = class("Item", var_0_0.Object)

		var_26_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}

		function var_26_0.Trigger(arg_27_0, arg_27_1)
			arg_27_0.isTriggered = True

			arg_27_0.TriggerEffect(arg_27_1)
			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/mini_perfect")
			arg_27_0.Clear()

		return var_26_0,
	function()
		return (class("MoreTime", var_0_0.Item)),
	function()
		return (class("Invincibility", var_0_0.Item)),
	function()
		local var_30_0 = class("Motorcycle", var_0_0.Object)

		var_30_0.colliderSize = {
			{
				-100,
				100
			},
			{
				-114,
				114
			}
		}

		function var_30_0.Ctor(arg_31_0, arg_31_1, arg_31_2, arg_31_3)
			arg_31_0.rt = arg_31_1
			arg_31_0.pos = arg_31_2

			setAnchoredPosition(arg_31_0.rt, arg_31_0.pos)

			arg_31_0.controller = arg_31_3
			arg_31_0.isTriggered = False
			arg_31_0.comSpineAnim = arg_31_1.Find("GameObject").GetComponent(typeof(SpineAnimUI))

			arg_31_0.comSpineAnim.SetActionCallBack(function(arg_32_0)
				if arg_32_0 == "finish":
					arg_31_0.ActionCallback())

			arg_31_0.effectList = {}

			for iter_31_0, iter_31_1 in ipairs({
				"saiche_sudu_01",
				"saiche_sudu_02",
				"saiche_sudu_03",
				"saiche_sudu_04"
			}):
				table.insert(arg_31_0.effectList, arg_31_0.rt.Find("GameObject/" .. iter_31_1))

			arg_31_0.Show("base")

		function var_30_0.UpdatePos(arg_33_0, arg_33_1, arg_33_2)
			arg_33_0.pos = arg_33_0.pos + arg_33_1
			arg_33_0.pos.y = math.clamp(arg_33_0.pos.y, -arg_33_2, arg_33_2)

			setAnchoredPosition(arg_33_0.rt, arg_33_0.pos)

		function var_30_0.ActionCallback(arg_34_0)
			switch(arg_34_0.action, {
				def ride:()
					return,
				def accel:()
					arg_34_0.action = "ride"

					arg_34_0.comSpineAnim.SetAction(arg_34_0.action, 0),
				def fall:()
					arg_34_0.isBlock = False

					arg_34_0.Show("base"),
				def yunxuan:()
					arg_34_0.isVertigo = False

					setActive(arg_34_0.rt.Find("GameObject/saiche_xuanyun"), False)
					setActive(arg_34_0.rt.Find("GameObject/saiche_jiansu"), False)
					arg_34_0.Show("accel")
			})

		function var_30_0.Show(arg_39_0, ...)
			var_30_0.super.Show(arg_39_0, ...)
			switch(arg_39_0.state, {
				def base:()
					arg_39_0.action = "stop",
				def accel:()
					if not arg_39_0.afterFirstAccel:
						arg_39_0.afterFirstAccel = True
						arg_39_0.action = "accel"
					else
						arg_39_0.action = "ride",
				def fall:()
					arg_39_0.action = "fall"
					arg_39_0.isBlock = True,
				def yunxuan:()
					arg_39_0.action = "yunxuan"
					arg_39_0.isVertigo = True

					setActive(arg_39_0.rt.Find("GameObject/saiche_xuanyun"), True)
					setActive(arg_39_0.rt.Find("GameObject/saiche_jiansu"), True)
					pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-yunxuan")
			})
			arg_39_0.comSpineAnim.SetAction(arg_39_0.action, 0)

		function var_30_0.TriggerEffect(arg_44_0, arg_44_1)
			switch(arg_44_1.__cname, {
				def MoreTime:()
					arg_44_0.controller.AddTime(RacingMiniGameConfig.ITEM_ADD_TIME),
				def Invincibility:()
					arg_44_0.invincibleTime = RacingMiniGameConfig.INVINCIBLE_TIME

					setActive(arg_44_0.rt.Find("invincibility"), True),
				def TrafficCone:()
					arg_44_0.controller.SetEnginePower(0)
					arg_44_0.Show("fall")
					pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-fall"),
				def Roadblock:()
					arg_44_0.controller.SetEnginePower(0)
					arg_44_0.Show("fall")
					pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-fall"),
				def Bomb:()
					arg_44_0.controller.SetEnginePower(0)
					arg_44_0.Show("fall"),
				def Mire:()
					arg_44_0.controller.SetEnginePower(math.min(arg_44_0.controller.enginePower, RacingMiniGameConfig.OBSTACLE_POWER_BLOCK))
					arg_44_0.Show("yunxuan"),
				def SpeedBumps:()
					arg_44_0.controller.SetEnginePower(math.min(arg_44_0.controller.enginePower, RacingMiniGameConfig.OBSTACLE_POWER_BLOCK))
					arg_44_0.Show("yunxuan")
			})

		function var_30_0.UpdateInvincibility(arg_52_0, arg_52_1)
			assert(arg_52_0.invincibleTime)

			arg_52_0.invincibleTime = arg_52_0.invincibleTime - arg_52_1

			if arg_52_0.invincibleTime <= 0:
				setActive(arg_52_0.rt.Find("invincibility"), False)

				arg_52_0.invincibleTime = None
			else
				local var_52_0 = arg_52_0.invincibleTime < 2

				setActive(arg_52_0.rt.Find("invincibility/saiche_wudihudun_xiaoshi"), var_52_0)
				setActive(arg_52_0.rt.Find("invincibility/saiche_wudihudun"), not var_52_0)

		return var_30_0
}

for iter_0_0, iter_0_1 in ipairs(var_0_1):
	local var_0_2 = iter_0_1()

	var_0_0[var_0_2.__cname] = var_0_2

return var_0_0
