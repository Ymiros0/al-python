local var_0_0 = class("CookGameJudgesController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._sceneTf = findTF(arg_1_1, "scene")
	arg_1_0._sceneBackground = findTF(arg_1_1, "scene_background")
	arg_1_0._sceneFrontTf = findTF(arg_1_1, "scene_front")
	arg_1_0._tpl = findTF(arg_1_0._sceneBackground, "judgeTpl")
	arg_1_0._gameData = arg_1_2
	arg_1_0._event = arg_1_3
	arg_1_0.initFlag = False
	arg_1_0.jiujiuTf = findTF(arg_1_0._sceneBackground, "jiujiuTime")
	arg_1_0.jiujiuAnim = GetComponent(findTF(arg_1_0.jiujiuTf, "anim"), typeof(Animator))

	setActive(arg_1_0._tpl, False)

def var_0_0.init(arg_2_0):
	arg_2_0.initFlag = True
	arg_2_0._judgeDatas = {}

	for iter_2_0 = 1, #CookGameConst.judge_data:
		local var_2_0 = CookGameConst.judge_data[iter_2_0]
		local var_2_1 = ResourceMgr.Inst.getAssetSync(arg_2_0._gameData.path, var_2_0.name, typeof(RuntimeAnimatorController), False, False)

		table.insert(arg_2_0._judgeDatas, {
			data = Clone(var_2_0),
			runtimeAnimator = var_2_1
		})

	arg_2_0.judges = {}

	for iter_2_1 = 1, CookGameConst.judge_num:
		local var_2_2 = iter_2_1
		local var_2_3 = tf(instantiate(arg_2_0._tpl))
		local var_2_4 = findTF(arg_2_0._sceneBackground, "judgesPos" .. iter_2_1).anchoredPosition

		setParent(var_2_3, arg_2_0._sceneTf)
		setActive(var_2_3, True)

		var_2_3.anchoredPosition = var_2_4

		local var_2_5 = CookGameJudge.New(var_2_3, var_2_2, arg_2_0._judgeDatas, arg_2_0._gameData, arg_2_0._event)

		var_2_5.setFrontContainer(arg_2_0._sceneFrontTf)
		var_2_5.setClickCallback(function()
			arg_2_0.onJudgeClick(var_2_2))
		table.insert(arg_2_0.judges, var_2_5)

	arg_2_0._gameData.judges = arg_2_0.judges

def var_0_0.changeSpeed(arg_4_0, arg_4_1):
	for iter_4_0 = 1, #arg_4_0.judges:
		arg_4_0.judges[iter_4_0].changeSpeed(arg_4_1)

def var_0_0.serverIndex(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if arg_5_1 and arg_5_1 < #arg_5_0.judges:
		arg_5_0.judges[arg_5_1].server(arg_5_2, arg_5_3)
	else
		arg_5_3(False)

def var_0_0.onJudgeClick(arg_6_0, arg_6_1):
	for iter_6_0 = 1, #arg_6_0.judges:
		if iter_6_0 == arg_6_1:
			arg_6_0.judges[iter_6_0].select(True)
			arg_6_0._event.emit(CookGameView.CLICK_JUDGE_EVENT, arg_6_0.judges[arg_6_1], function(arg_7_0)
				if not arg_7_0:
					arg_6_0.judges[iter_6_0].select(False))
		else
			arg_6_0.judges[iter_6_0].select(False)

def var_0_0.start(arg_8_0):
	if not arg_8_0.initFlag:
		arg_8_0.init()

	for iter_8_0 = 1, #arg_8_0.judges:
		arg_8_0.judges[iter_8_0].start()

def var_0_0.step(arg_9_0, arg_9_1):
	for iter_9_0 = 1, #arg_9_0.judges:
		arg_9_0.judges[iter_9_0].step(arg_9_1)

def var_0_0.clear(arg_10_0):
	for iter_10_0 = 1, #arg_10_0.judges:
		arg_10_0.judges[iter_10_0].clear()

def var_0_0.extend(arg_11_0):
	if arg_11_0.jiujiuAnim:
		arg_11_0.jiujiuAnim.SetTrigger("extend")

def var_0_0.timeUp(arg_12_0):
	if arg_12_0.jiujiuAnim:
		arg_12_0.jiujiuAnim.SetTrigger("time_up")

return var_0_0
