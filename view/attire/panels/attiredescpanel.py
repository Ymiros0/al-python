local var_0_0 = class("AttireDescPanel")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0.icon = findTF(arg_1_0._tf, "icon")
	arg_1_0.frame = findTF(arg_1_0._tf, "frame")
	arg_1_0.chatContainer = findTF(arg_1_0._tf, "chatContainer")
	arg_1_0.conditionTF = findTF(arg_1_0._tf, "condition")
	arg_1_0.nameTxt = findTF(arg_1_0._tf, "name/Text").GetComponent(typeof(Text))
	arg_1_0.stateTxt = findTF(arg_1_0._tf, "get_info/lock").GetComponent(typeof(Text))
	arg_1_0.timeTxt = findTF(arg_1_0._tf, "get_info/time").GetComponent(typeof(Text))
	arg_1_0.conditionTxt = findTF(arg_1_0._tf, "condition/Text").GetComponent(typeof(Text))
	arg_1_0.applyBtn = findTF(arg_1_0._tf, "apply_btn")
	arg_1_0.applyingBtn = findTF(arg_1_0._tf, "applying_btn")
	arg_1_0.getBtn = findTF(arg_1_0._tf, "get_btn")

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.UpdateIconDesc(arg_2_1, arg_2_2)

	arg_2_0.nameTxt.text = HXSet.hxLan(arg_2_1.getConfig("name"))

	local var_2_0 = arg_2_1.isOwned()
	local var_2_1 = var_2_0 and i18n("word_got") or i18n("word_not_get")

	arg_2_0.stateTxt.text = setColorStr(var_2_1, var_2_0 and "#3DC6FFFF" or "#a5afdf")

	local var_2_2 = arg_2_1.expiredType()

	arg_2_0.RemoveTimer()

	if var_2_0 and var_2_2:
		arg_2_0.AddTimer(arg_2_1, arg_2_2)
	elif var_2_0 and not var_2_2:
		arg_2_0.timeTxt.text = ""
	elif not var_2_0:
		arg_2_0.timeTxt.text = ""

	arg_2_0.conditionTxt.text = HXSet.hxLan(arg_2_1.getConfig("desc"))

	local var_2_3 = arg_2_1.getState()
	local var_2_4 = arg_2_2.getAttireByType(arg_2_1.getType()) == arg_2_1.id

	setActive(arg_2_0.applyBtn, var_2_3 == AttireFrame.STATE_UNLOCK and not var_2_4)
	setActive(arg_2_0.applyingBtn, var_2_3 == AttireFrame.STATE_UNLOCK and var_2_4)
	setActive(arg_2_0.getBtn, var_2_3 == AttireFrame.STATE_LOCK)

def var_0_0.UpdateIconDesc(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_1.getType() == AttireConst.TYPE_ICON_FRAME
	local var_3_1 = arg_3_1.getType() == AttireConst.TYPE_CHAT_FRAME

	if arg_3_0.loadedIcon and arg_3_0.loadedIconTF:
		local var_3_2 = arg_3_0.loadedIcon.getIcon()

		if var_3_1:
			arg_3_0.loadedIconTF.transform.Find("Text").GetComponent(typeof(Text)).supportRichText = False

		PoolMgr.GetInstance().ReturnPrefab(var_3_2, arg_3_0.loadedIcon.id, arg_3_0.loadedIconTF)

	if var_3_0:
		if not arg_3_0.startList:
			arg_3_0.startList = UIItemList.New(findTF(arg_3_0._tf, "stars"), findTF(arg_3_0._tf, "stars/tpl"))

		local var_3_3 = arg_3_1.getIcon()

		PoolMgr.GetInstance().GetPrefab(var_3_3, arg_3_1.getConfig("id"), True, function(arg_4_0)
			arg_3_0.loadedIcon = arg_3_1
			arg_3_0.loadedIconTF = arg_4_0

			setParent(arg_4_0, arg_3_0.frame, False))

		local var_3_4 = arg_3_2.GetFlagShip()

		LoadSpriteAsync("qicon/" .. var_3_4.getPrefab(), function(arg_5_0)
			arg_3_0.icon.GetComponent(typeof(Image)).sprite = arg_5_0)
		arg_3_0.startList.align(var_3_4.getStar())
	elif var_3_1:
		local var_3_5 = arg_3_1.getIcon()

		PoolMgr.GetInstance().GetPrefab(var_3_5, arg_3_1.getConfig("id") .. "_self", True, function(arg_6_0)
			arg_3_0.loadedIcon = arg_3_1
			arg_3_0.loadedIconTF = arg_6_0

			setParent(arg_6_0, arg_3_0.chatContainer, False)

			tf(arg_6_0).localPosition = Vector3(0, 0, 0)
			findTF(arg_6_0, "Text").GetComponent(typeof(Text)).supportRichText = True

			setText(findTF(arg_6_0, "Text"), arg_3_1.getConfig("desc")))

	setActive(arg_3_0.conditionTF, not var_3_1)

def var_0_0.AddTimer(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_1.getExpiredTime()

	arg_7_0.timer = Timer.New(function()
		local var_8_0 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_8_1 = var_7_0 - var_8_0

		if var_8_1 > 0:
			arg_7_0.timeTxt.text = "/ " .. attireTimeStamp(var_8_1)
		else
			arg_7_0.Update(arg_7_1, arg_7_2)
			arg_7_0.RemoveTimer(), 1, -1)

	arg_7_0.timer.Start()
	arg_7_0.timer.func()

def var_0_0.RemoveTimer(arg_9_0):
	if arg_9_0.timer:
		arg_9_0.timer.Stop()

		arg_9_0.timer = None

def var_0_0.Dispose(arg_10_0):
	arg_10_0.RemoveTimer()

return var_0_0
