local var_0_0 = class("MakeTeaPtPage", import(".TemplatePage.SkinTemplatePage"))
local var_0_1 = 5
local var_0_2 = {
	"caizhai",
	"tanfang",
	"shaqing",
	"huichao",
	"huiguo",
	"yincha"
}
local var_0_3 = "ui/activityuipage/maketeaptpage_atlas"
local var_0_4

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

def var_0_0.initMv(arg_2_0):
	arg_2_0.showItemNum = arg_2_0.activity.data3 < var_0_1 and arg_2_0.activity.data3 or var_0_1
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
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and not arg_2_0.mvCompleteFlag:
			print("恢复播放")
			arg_2_0.mvManaCpkUI.Pause(False)
			arg_2_0.onPlayerStart())
	onButton(arg_2_0, arg_2_0.btnStop, function()
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and not arg_2_0.mvCompleteFlag:
			print("暂停播放")
			arg_2_0.mvManaCpkUI.Pause(True)
			arg_2_0.onPlayerStop())
	onButton(arg_2_0, arg_2_0.btnRepeat, function()
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.mvManaCpkUI and arg_2_0.mvCompleteFlag:
			print("重新播放")
			arg_2_0.loadMv())
	onButton(arg_2_0, arg_2_0.mvBottom, function()
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.isLoading:
			return

		if arg_2_0.playHandle:
			arg_2_0.playHandle()

			arg_2_0.playHandle = None

		arg_2_0.displayWindow(False)
		arg_2_0.clearMovie())
	onButton(arg_2_0, findTF(arg_2_0.mvTf, "left"), function()
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.mvIndex > 1 and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex - 1

			arg_2_0.pageChange())
	onButton(arg_2_0, findTF(arg_2_0.mvTf, "right"), function()
		if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
			return

		var_0_4 = Time.realtimeSinceStartup

		if arg_2_0.mvIndex < arg_2_0.showItemNum and not arg_2_0.isLoading:
			arg_2_0.mvIndex = arg_2_0.mvIndex + 1

			arg_2_0.pageChange())

	for iter_2_0 = 1, var_0_1:
		local var_2_0 = iter_2_0

		onButton(arg_2_0, findTF(arg_2_0.mvTf, "page/" .. iter_2_0), function()
			if var_0_4 and Time.realtimeSinceStartup - var_0_4 < 1:
				return

			var_0_4 = Time.realtimeSinceStartup

			if arg_2_0.nday < 6:
				return

			if arg_2_0.mvIndex != var_2_0 and not arg_2_0.isLoading:
				arg_2_0.mvIndex = var_2_0

				arg_2_0.pageChange())
		setActive(findTF(arg_2_0.mvTf, "page/" .. iter_2_0), iter_2_0 <= arg_2_0.showItemNum)

	setActive(arg_2_0.mvTf, False)

def var_0_0.UpdateTask(arg_10_0, arg_10_1, arg_10_2):
	var_0_0.super.UpdateTask(arg_10_0, arg_10_1, arg_10_2)

	local var_10_0 = arg_10_0.findTF("get_btn", arg_10_2)
	local var_10_1 = arg_10_1 + 1
	local var_10_2 = arg_10_0.taskGroup[arg_10_0.nday][var_10_1]
	local var_10_3 = arg_10_0.taskProxy.getTaskById(var_10_2) or arg_10_0.taskProxy.getFinishTaskById(var_10_2)

	onButton(arg_10_0, var_10_0, function()
		if arg_10_0.nday <= var_0_1:
			arg_10_0.mvIndex = arg_10_0.nday

			function arg_10_0.playHandle()
				arg_10_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_10_3)

			arg_10_0.displayWindow(True)
		else
			local var_11_0 = arg_10_0.activity.getConfig("config_client").story

			if checkExist(var_11_0, {
				arg_10_0.nday
			}, {
				1
			}):
				pg.NewStoryMgr.GetInstance().Play(var_11_0[arg_10_0.nday][1], function()
					arg_10_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_10_3))
			else
				arg_10_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_10_3), SFX_PANEL)

	local var_10_4 = arg_10_0.findTF("got_btn", arg_10_2)

	onButton(arg_10_0, var_10_4, function()
		arg_10_0.displayWindow(True), SFX_PANEL)

def var_0_0.pageChange(arg_15_0):
	arg_15_0.pageUpdate()
	arg_15_0.loadMv()

def var_0_0.pageUpdate(arg_16_0):
	for iter_16_0 = 1, var_0_1:
		setActive(findTF(arg_16_0.mvTf, "page/" .. iter_16_0 .. "/selected"), arg_16_0.mvIndex == iter_16_0)

	for iter_16_1 = 1, #var_0_2:
		setActive(findTF(arg_16_0.mvTf, "title_word/" .. iter_16_1), iter_16_1 == arg_16_0.mvIndex)

def var_0_0.OnFirstFlush(arg_17_0):
	var_0_0.super.OnFirstFlush(arg_17_0)

	arg_17_0.mvIndex = arg_17_0.activity.data3 > var_0_1 and 1 or arg_17_0.activity.data3

	arg_17_0.initMv()

def var_0_0.OnUpdateFlush(arg_18_0):
	arg_18_0.nday = arg_18_0.activity.data3

	if arg_18_0.dayTF:
		setText(arg_18_0.dayTF, tostring(arg_18_0.nday))

	arg_18_0.uilist.align(#arg_18_0.taskGroup[arg_18_0.nday])

	for iter_18_0 = 1, #var_0_2:
		setActive(findTF(arg_18_0._tf, "AD/word/" .. iter_18_0), iter_18_0 == arg_18_0.nday)

def var_0_0.updateMvUI(arg_19_0):
	arg_19_0.showItemNum = arg_19_0.activity.data3 < var_0_1 and arg_19_0.activity.data3 or var_0_1

	if arg_19_0.playHandle:
		setActive(findTF(arg_19_0.mvTf, "left"), False)
		setActive(findTF(arg_19_0.mvTf, "right"), False)
	else
		setActive(findTF(arg_19_0.mvTf, "left"), arg_19_0.showItemNum > 1)
		setActive(findTF(arg_19_0.mvTf, "right"), arg_19_0.showItemNum > 1)

	for iter_19_0 = 1, var_0_1:
		setActive(findTF(arg_19_0.mvTf, "page/" .. iter_19_0 .. "/selected"), arg_19_0.mvIndex == iter_19_0)
		setActive(findTF(arg_19_0.mvTf, "page/" .. iter_19_0), iter_19_0 <= arg_19_0.showItemNum)
		setActive(findTF(arg_19_0.mvTf, "title_word/" .. iter_19_0), iter_19_0 == arg_19_0.mvIndex)

def var_0_0.displayWindow(arg_20_0, arg_20_1):
	if not arg_20_1 and not arg_20_0.blurFlag:
		return

	if arg_20_0.isLoading:
		return

	if arg_20_0.blurFlag == arg_20_1:
		return

	if arg_20_1:
		setActive(arg_20_0.mvTf, True)

		local var_20_0 = Screen.width
		local var_20_1 = Screen.height

		setSizeDelta(findTF(arg_20_0.mvTf, "bottom"), Vector2(Screen.width, Screen.height))
		pg.UIMgr.GetInstance().BlurPanel(arg_20_0.mvTf, True)
		arg_20_0.updateMvUI()
		arg_20_0.loadMv()
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_20_0.mvTf)
		setActive(arg_20_0.mvTf, False)

	arg_20_0.blurFlag = arg_20_1

def var_0_0.OnDestroy(arg_21_0):
	var_0_0.super.OnDestroy(arg_21_0)

	arg_21_0.isLoading = False

	arg_21_0.displayWindow(False)
	arg_21_0.clearMovie()

def var_0_0.clearMovie(arg_22_0):
	if arg_22_0.mvGo:
		arg_22_0.mvManaCpkUI.SetPlayEndHandler(None)
		arg_22_0.mvManaCpkUI.StopCpk()
		destroy(arg_22_0.mvGo)

		arg_22_0.mvManaCpkUI = None
		arg_22_0.mvGo = None
		arg_22_0.mvName = None

def var_0_0.GetProgressColor(arg_23_0):
	return "#57896D", "#A1AAA1"

def var_0_0.loadMv(arg_24_0):
	arg_24_0.clearMovie()

	if arg_24_0.isLoading:
		return

	local var_24_0 = "paocha" .. arg_24_0.mvIndex

	arg_24_0.isLoading = True

	PoolMgr.GetInstance().GetUI(var_24_0, True, function(arg_25_0)
		arg_24_0.mvGo = arg_25_0
		arg_24_0.mvName = var_24_0
		arg_24_0.mvManaCpkUI = GetComponent(findTF(arg_24_0.mvGo, "video/cpk"), typeof(CriManaCpkUI))

		arg_24_0.mvManaCpkUI.SetPlayEndHandler(System.Action(function()
			arg_24_0.mvComplete()

			if arg_24_0.playHandle:
				arg_24_0.playHandle()

				arg_24_0.playHandle = None))
		setActive(arg_24_0.btnPlay, False)
		setActive(arg_24_0.btnStop, True)
		setActive(arg_24_0.btnRepeat, False)
		setText(arg_24_0.movieWord, i18n("mktea_" .. arg_24_0.mvIndex))

		if arg_24_0.isLoading == False:
			arg_24_0.clearMovie()
		else
			arg_24_0.isLoading = False

			setParent(arg_24_0.mvGo, arg_24_0.mvContent)
			setActive(arg_24_0.mvGo, True)

		arg_24_0.mvCompleteFlag = False

		arg_24_0.mvManaCpkUI.PlayCpk())

def var_0_0.mvComplete(arg_27_0):
	print("播放完成")

	arg_27_0.mvCompleteFlag = True

	arg_27_0.onPlayerEnd()

	if arg_27_0.mvIndex == arg_27_0.nday:
		-- block empty

def var_0_0.onPlayerEnd(arg_28_0):
	setActive(arg_28_0.btnPlay, False)
	setActive(arg_28_0.btnStop, False)
	setActive(arg_28_0.btnRepeat, True)

def var_0_0.onPlayerStop(arg_29_0):
	setActive(arg_29_0.btnPlay, True)
	setActive(arg_29_0.btnStop, False)
	setActive(arg_29_0.btnRepeat, False)

def var_0_0.onPlayerStart(arg_30_0):
	setActive(arg_30_0.btnPlay, False)
	setActive(arg_30_0.btnStop, True)
	setActive(arg_30_0.btnRepeat, False)

return var_0_0
