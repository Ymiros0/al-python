local var_0_0 = class("Mv1PtPage", import(".TemplatePage.SkinTemplatePage"))
local var_0_1 = 3
local var_0_2

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

def var_0_0.initMv(arg_2_0):
	arg_2_0.showItemNum = var_0_1
	arg_2_0.mvTf = findTF(arg_2_0._tf, "AD/mvPage")

	setActive(arg_2_0.mvTf, False)

	arg_2_0.mvContent = findTF(arg_2_0._tf, "AD/mvPage/movie/view/content")
	arg_2_0.movieWord = findTF(arg_2_0._tf, "AD/mvPage/movie/movieWord")
	arg_2_0.descClose = findTF(arg_2_0._tf, "AD/mvPage/descClose")

	setText(arg_2_0.descClose, i18n("island_act_tips1"))

	arg_2_0.mvIndex = 1

	arg_2_0.pageUpdate()

	arg_2_0.mvBottom = findTF(arg_2_0.mvTf, "bottom")
	arg_2_0.btnPlay = findTF(arg_2_0.mvTf, "movie/btnPlay")
	arg_2_0.btnStop = findTF(arg_2_0.mvTf, "movie/btnStop")
	arg_2_0.btnRepeat = findTF(arg_2_0.mvTf, "movie/btnRepeat")

	onButton(arg_2_0, arg_2_0.btnPlay, function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and not arg_2_0.mvCompleteFlag:
			print("恢复播放")
			arg_2_0.mvManaCpkUI.Pause(False)
			arg_2_0.onPlayerStart())
	onButton(arg_2_0, arg_2_0.btnStop, function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and not arg_2_0.mvCompleteFlag:
			print("暂停播放")
			arg_2_0.mvManaCpkUI.Pause(True)
			arg_2_0.onPlayerStop())
	onButton(arg_2_0, arg_2_0.btnRepeat, function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and arg_2_0.mvCompleteFlag:
			print("重新播放")
			arg_2_0.loadMv())
	onButton(arg_2_0, arg_2_0.mvBottom, function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.isLoading:
			return

		if arg_2_0.playHandle:
			arg_2_0.playHandle()

			arg_2_0.playHandle = None

		arg_2_0.displayWindow(False)
		arg_2_0.clearMovie())
	onButton(arg_2_0, findTF(arg_2_0.mvTf, "left"), function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.mvIndex > 1 and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex - 1

			arg_2_0.pageChange())
	onButton(arg_2_0, findTF(arg_2_0.mvTf, "right"), function()
		if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
			return

		var_0_2 = Time.realtimeSinceStartup

		if arg_2_0.mvIndex < arg_2_0.showItemNum and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex + 1

			arg_2_0.pageChange())
	onButton(arg_2_0, findTF(arg_2_0._tf, "AD/chapter"), function()
		arg_2_0.displayWindow(True), SFX_PANEL)
	onButton(arg_2_0, findTF(arg_2_0._tf, "AD/left"), function()
		if arg_2_0.mvIndex > 1 and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex - 1

			arg_2_0.pageUpdate())
	onButton(arg_2_0, findTF(arg_2_0._tf, "AD/right"), function()
		if arg_2_0.mvIndex < arg_2_0.showItemNum and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex + 1

			arg_2_0.pageUpdate())

	for iter_2_0 = 1, var_0_1:
		local var_2_0 = iter_2_0

		onButton(arg_2_0, findTF(arg_2_0.mvTf, "page/" .. iter_2_0), function()
			if var_0_2 and Time.realtimeSinceStartup - var_0_2 < 1:
				return

			var_0_2 = Time.realtimeSinceStartup

			if arg_2_0.nday < 6:
				return

			if arg_2_0.mvIndex != var_2_0 and not arg_2_0.isLoading:
				arg_2_0.mvIndex = var_2_0

				arg_2_0.pageUpdate())
		setActive(findTF(arg_2_0.mvTf, "page/" .. iter_2_0), iter_2_0 <= arg_2_0.showItemNum)

	setActive(arg_2_0.mvTf, False)

def var_0_0.UpdateTask(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_1 + 1
	local var_13_1 = arg_13_0.findTF("itemMask/item", arg_13_2)
	local var_13_2 = arg_13_0.taskGroup[arg_13_0.nday][var_13_0]
	local var_13_3 = arg_13_0.taskProxy.getTaskById(var_13_2) or arg_13_0.taskProxy.getFinishTaskById(var_13_2)

	assert(var_13_3, "without this task by id. " .. var_13_2)

	local var_13_4 = var_13_3.getConfig("award_display")[1]
	local var_13_5 = {
		type = var_13_4[1],
		id = var_13_4[2],
		count = var_13_4[3]
	}

	updateDrop(var_13_1, var_13_5)
	onButton(arg_13_0, var_13_1, function()
		arg_13_0.emit(BaseUI.ON_DROP, var_13_5), SFX_PANEL)

	local var_13_6 = var_13_3.getProgress()
	local var_13_7 = var_13_3.getConfig("target_num")

	setText(arg_13_0.findTF("description", arg_13_2), var_13_3.getConfig("desc"))

	local var_13_8, var_13_9 = arg_13_0.GetProgressColor()
	local var_13_10

	var_13_10 = var_13_8 and setColorStr(var_13_6, var_13_8) or var_13_6

	local var_13_11

	var_13_11 = var_13_9 and setColorStr("/" .. var_13_7, var_13_9) or "/" .. var_13_7

	setText(arg_13_0.findTF("progressText", arg_13_2), var_13_10 .. var_13_11)
	setSlider(arg_13_0.findTF("progress", arg_13_2), 0, var_13_7, var_13_6)

	local var_13_12 = arg_13_0.findTF("go_btn", arg_13_2)
	local var_13_13 = arg_13_0.findTF("get_btn", arg_13_2)
	local var_13_14 = arg_13_0.findTF("got_btn", arg_13_2)
	local var_13_15 = var_13_3.getTaskStatus()

	setActive(var_13_12, var_13_15 == 0)
	setActive(var_13_13, var_13_15 == 1)
	setActive(var_13_14, var_13_15 == 2)
	onButton(arg_13_0, var_13_12, function()
		arg_13_0.emit(ActivityMediator.ON_TASK_GO, var_13_3), SFX_PANEL)
	onButton(arg_13_0, var_13_13, function()
		arg_13_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_13_3), SFX_PANEL)

	local var_13_16 = arg_13_0.findTF("get_btn", arg_13_2)
	local var_13_17 = arg_13_1 + 1
	local var_13_18 = arg_13_0.taskGroup[arg_13_0.nday][var_13_17]
	local var_13_19 = arg_13_0.taskProxy.getTaskById(var_13_18) or arg_13_0.taskProxy.getFinishTaskById(var_13_18)

	onButton(arg_13_0, var_13_16, function()
		if arg_13_0.nday <= var_0_1:
			arg_13_0.mvIndex = arg_13_0.nday

			arg_13_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_13_19)
		else
			local var_17_0 = arg_13_0.activity.getConfig("config_client").story

			if checkExist(var_17_0, {
				arg_13_0.nday
			}, {
				1
			}):
				pg.NewStoryMgr.GetInstance().Play(var_17_0[arg_13_0.nday][1], function()
					arg_13_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_13_19))
			else
				arg_13_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_13_19), SFX_PANEL)

	local var_13_20 = arg_13_0.findTF("got_btn", arg_13_2)

	onButton(arg_13_0, var_13_20, function()
		arg_13_0.displayWindow(True), SFX_PANEL)

def var_0_0.pageChange(arg_20_0):
	arg_20_0.pageUpdate()
	arg_20_0.loadMv()

def var_0_0.pageUpdate(arg_21_0):
	for iter_21_0 = 1, var_0_1:
		setActive(findTF(arg_21_0.mvTf, "page/" .. iter_21_0 .. "/selected"), arg_21_0.mvIndex == iter_21_0)

	for iter_21_1 = 1, var_0_1:
		setActive(findTF(arg_21_0._tf, "AD/page/" .. iter_21_1 .. "/selected"), arg_21_0.mvIndex == iter_21_1)

	for iter_21_2 = 1, var_0_1:
		setActive(findTF(arg_21_0._tf, "AD/chapter/" .. iter_21_2), arg_21_0.mvIndex == iter_21_2)

	setActive(findTF(arg_21_0._tf, "AD/right"), arg_21_0.mvIndex != arg_21_0.showItemNum)
	setActive(findTF(arg_21_0._tf, "AD/left"), arg_21_0.mvIndex != 1)

def var_0_0.OnFirstFlush(arg_22_0):
	var_0_0.super.OnFirstFlush(arg_22_0)

	arg_22_0.mvIndex = arg_22_0.activity.data3 > var_0_1 and 1 or arg_22_0.activity.data3

	arg_22_0.initMv()

def var_0_0.OnUpdateFlush(arg_23_0):
	arg_23_0.nday = arg_23_0.activity.data3

	if arg_23_0.dayTF:
		setText(arg_23_0.dayTF, tostring(arg_23_0.nday))

	arg_23_0.uilist.align(#arg_23_0.taskGroup[arg_23_0.nday])

def var_0_0.updateMvUI(arg_24_0):
	arg_24_0.showItemNum = var_0_1

	if arg_24_0.playHandle:
		setActive(findTF(arg_24_0.mvTf, "left"), False)
		setActive(findTF(arg_24_0.mvTf, "right"), False)
	else
		setActive(findTF(arg_24_0.mvTf, "left"), arg_24_0.showItemNum > 1)
		setActive(findTF(arg_24_0.mvTf, "right"), arg_24_0.showItemNum > 1)

	for iter_24_0 = 1, var_0_1:
		setActive(findTF(arg_24_0.mvTf, "page/" .. iter_24_0 .. "/selected"), arg_24_0.mvIndex == iter_24_0)
		setActive(findTF(arg_24_0.mvTf, "page/" .. iter_24_0), iter_24_0 <= arg_24_0.showItemNum)

def var_0_0.displayWindow(arg_25_0, arg_25_1):
	if not arg_25_1 and not arg_25_0.blurFlag:
		return

	if arg_25_0.isLoading:
		return

	if arg_25_0.blurFlag == arg_25_1:
		return

	if arg_25_1:
		setActive(arg_25_0.mvTf, True)

		local var_25_0 = Screen.width
		local var_25_1 = Screen.height

		setSizeDelta(findTF(arg_25_0.mvTf, "bottom"), Vector2(Screen.width, Screen.height))
		pg.UIMgr.GetInstance().BlurPanel(arg_25_0.mvTf, True)
		arg_25_0.updateMvUI()
		arg_25_0.loadMv()
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_25_0.mvTf)
		setActive(arg_25_0.mvTf, False)

	arg_25_0.blurFlag = arg_25_1

def var_0_0.OnDestroy(arg_26_0):
	var_0_0.super.OnDestroy(arg_26_0)

	arg_26_0.isLoading = False

	arg_26_0.displayWindow(False)
	arg_26_0.clearMovie()

def var_0_0.clearMovie(arg_27_0):
	if arg_27_0.mvGo:
		arg_27_0.mvManaCpkUI.SetPlayEndHandler(None)
		arg_27_0.mvManaCpkUI.StopCpk()
		destroy(arg_27_0.mvGo)

		arg_27_0.mvManaCpkUI = None
		arg_27_0.mvGo = None
		arg_27_0.mvName = None

def var_0_0.GetProgressColor(arg_28_0):
	return "#FF6868", "#604D49"

def var_0_0.loadMv(arg_29_0):
	arg_29_0.clearMovie()

	if arg_29_0.isLoading:
		return

	local var_29_0 = "psplive_" .. arg_29_0.mvIndex

	arg_29_0.isLoading = True

	PoolMgr.GetInstance().GetUI(var_29_0, True, function(arg_30_0)
		arg_29_0.mvGo = arg_30_0
		arg_29_0.mvName = var_29_0
		arg_29_0.mvManaCpkUI = GetComponent(findTF(arg_29_0.mvGo, "video/cpk"), typeof(CriManaCpkUI))

		arg_29_0.mvManaCpkUI.SetPlayEndHandler(System.Action(function()
			arg_29_0.mvComplete()

			if arg_29_0.playHandle:
				arg_29_0.playHandle()

				arg_29_0.playHandle = None))
		setActive(arg_29_0.btnPlay, False)
		setActive(arg_29_0.btnStop, True)
		setActive(arg_29_0.btnRepeat, False)

		if arg_29_0.isLoading == False:
			arg_29_0.clearMovie()
		else
			arg_29_0.isLoading = False

			setParent(arg_29_0.mvGo, arg_29_0.mvContent)
			setActive(arg_29_0.mvGo, True)

		arg_29_0.mvCompleteFlag = False

		arg_29_0.mvManaCpkUI.PlayCpk())

def var_0_0.mvComplete(arg_32_0):
	print("播放完成")

	arg_32_0.mvCompleteFlag = True

	arg_32_0.onPlayerEnd()

	if arg_32_0.mvIndex == arg_32_0.nday:
		-- block empty

def var_0_0.onPlayerEnd(arg_33_0):
	setActive(arg_33_0.btnPlay, False)
	setActive(arg_33_0.btnStop, False)
	setActive(arg_33_0.btnRepeat, True)

def var_0_0.onPlayerStop(arg_34_0):
	setActive(arg_34_0.btnPlay, True)
	setActive(arg_34_0.btnStop, False)
	setActive(arg_34_0.btnRepeat, False)

def var_0_0.onPlayerStart(arg_35_0):
	setActive(arg_35_0.btnPlay, False)
	setActive(arg_35_0.btnStop, True)
	setActive(arg_35_0.btnRepeat, False)

return var_0_0
