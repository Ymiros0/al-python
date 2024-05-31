local var_0_0 = class("GuildMemberCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.go = arg_1_1
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.iconTF = arg_1_0.tf.Find("shipicon/icon").GetComponent(typeof(Image))
	arg_1_0.starsTF = arg_1_0.tf.Find("shipicon/stars")
	arg_1_0.starTF = arg_1_0.tf.Find("shipicon/stars/star")
	arg_1_0.levelTF = arg_1_0.tf.Find("level/Text").GetComponent(typeof(Text))
	arg_1_0.nameTF = arg_1_0.tf.Find("name_bg/Text").GetComponent(typeof(Text))
	arg_1_0.dutyTF = arg_1_0.tf.Find("duty").GetComponent(typeof(Image))
	arg_1_0.livenessTF = arg_1_0.tf.Find("liveness/Text").GetComponent(typeof(Text))
	arg_1_0.onLine = arg_1_0.tf.Find("online_tag")
	arg_1_0.offLine = arg_1_0.tf.Find("last_time")
	arg_1_0.onLineLabel = arg_1_0.tf.Find("online")
	arg_1_0.offLineLabel = arg_1_0.tf.Find("offline")
	arg_1_0.offLineText = arg_1_0.tf.Find("last_time/Text").GetComponent(typeof(Text))
	arg_1_0.maskTF = arg_1_0.tf.Find("mask")
	arg_1_0.timerTF = arg_1_0.tf.Find("mask/Text").GetComponent(typeof(Text))
	arg_1_0.borderTF = arg_1_0.tf.Find("selected")
	arg_1_0.bg = arg_1_0.tf.Find("bg")
	arg_1_0.circle = arg_1_0.tf.Find("shipicon/frame")

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.memberVO = arg_2_1

	arg_2_0.Clear()

	local var_2_0 = pg.ship_data_statistics[arg_2_1.icon]
	local var_2_1 = Ship.New({
		configId = arg_2_1.icon,
		skin_id = arg_2_1.skinId,
		propose = arg_2_1.proposeTime
	})

	LoadSpriteAsync("qicon/" .. var_2_1.getPainting(), function(arg_3_0)
		if not IsNil(arg_2_0.iconTF):
			arg_2_0.iconTF.sprite = arg_3_0)

	local var_2_2 = AttireFrame.attireFrameRes(arg_2_1, arg_2_1.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, arg_2_1.propose)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_2_2, var_2_2, True, function(arg_4_0)
		if arg_2_0.circle and not arg_2_0.exited:
			arg_4_0.name = var_2_2
			findTF(arg_4_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_4_0, arg_2_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_2_2, var_2_2, arg_4_0))

	local var_2_3 = GetSpriteFromAtlas("dutyicon", arg_2_1.duty)

	arg_2_0.dutyTF.sprite = var_2_3

	local var_2_4 = arg_2_0.starsTF.childCount

	for iter_2_0 = var_2_4, var_2_0.star - 1:
		cloneTplTo(arg_2_0.starTF, arg_2_0.starsTF)

	for iter_2_1 = 1, var_2_4:
		local var_2_5 = arg_2_0.starsTF.GetChild(iter_2_1 - 1)

		setActive(var_2_5, iter_2_1 <= var_2_0.star)

	arg_2_0.levelTF.text = arg_2_1.level
	arg_2_0.nameTF.text = arg_2_1.name
	arg_2_0.livenessTF.text = arg_2_1.liveness

	setActive(arg_2_0.onLine, arg_2_1.isOnline())
	setActive(arg_2_0.offLine, not arg_2_1.isOnline())
	setActive(arg_2_0.onLineLabel, arg_2_1.isOnline())
	setActive(arg_2_0.offLineLabel, not arg_2_1.isOnline())

	if not arg_2_1.isOnline():
		arg_2_0.offLineText.text = getOfflineTimeStamp(arg_2_1.preOnLineTime)

	local var_2_6 = arg_2_1.duty == GuildConst.DUTY_COMMANDER and arg_2_2.inKickTime()

	setActive(arg_2_0.maskTF, var_2_6)

	if var_2_6:
		arg_2_0.AddTimer(function()
			local var_5_0 = arg_2_2.getKickLeftTime()

			if var_5_0 > 0:
				arg_2_0.timerTF.text = pg.TimeMgr.GetInstance().DescCDTime(var_5_0)
			else
				arg_2_0.timerTF.text = ""

				setActive(arg_2_0.maskTF, False))

def var_0_0.AddTimer(arg_6_0, arg_6_1):
	if arg_6_0.timer:
		arg_6_0.timer.Stop()

		arg_6_0.timer = None

	arg_6_0.timer = Timer.New(arg_6_1, 1, -1)

	arg_6_0.timer.Start()
	arg_6_0.timer.func()

def var_0_0.Clear(arg_7_0):
	if arg_7_0.circle.childCount > 0:
		local var_7_0 = arg_7_0.circle.GetChild(0)
		local var_7_1 = var_7_0.gameObject.name

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_7_1, var_7_1, var_7_0.gameObject)

	if arg_7_0.timer:
		arg_7_0.timer.Stop()

		arg_7_0.timer = None

def var_0_0.SetSelected(arg_8_0, arg_8_1):
	setActive(arg_8_0.borderTF, arg_8_1)
	setActive(arg_8_0.bg, not arg_8_1)

def var_0_0.Dispose(arg_9_0):
	arg_9_0.exited = True

	arg_9_0.Clear()

return var_0_0
