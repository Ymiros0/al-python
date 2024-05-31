local var_0_0 = class("CpkPerformPlayer", import(".BasePerformPlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.bgTF = arg_1_0.findTF("bg", arg_1_0._tf)
	arg_1_0.nameTF = arg_1_0.findTF("name", arg_1_0.bgTF)
	arg_1_0.sliderTF = arg_1_0.findTF("slider", arg_1_0.bgTF)
	arg_1_0.cpkParentTF = arg_1_0.findTF("cpk", arg_1_0.bgTF)
	arg_1_0.cpkCoverTF = arg_1_0.findTF("cpk_cover", arg_1_0.bgTF)
	arg_1_0.frameRate = Application.targetFrameRate or 60

	local var_1_0 = pg.child_data[1]

	arg_1_0.maxStage = #var_1_0.stage
	arg_1_0.personalityIds = var_1_0.attr_2_list

def var_0_0.getCpkName(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(EducateProxy).GetCharData().GetStage()

	if var_2_0 < arg_2_0.maxStage:
		return arg_2_1[var_2_0]
	elif var_2_0 == arg_2_0.maxStage:
		local var_2_1 = getProxy(EducateProxy).GetPersonalityId()
		local var_2_2 = table.indexof(arg_2_0.personalityIds, var_2_1)

		return arg_2_1[var_2_0][var_2_2]

	return ""

def var_0_0.Play(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	arg_3_0.Show()

	if arg_3_3:
		setText(arg_3_0.nameTF, arg_3_3)

	setActive(arg_3_0.bgTF, not IsNil(arg_3_0.cpkTF))

	local var_3_0 = arg_3_0.getCpkName(arg_3_1.param[1]) or ""
	local var_3_1 = arg_3_1.param[2] or 3

	if checkABExist("educateanim/" .. var_3_0):
		ResourceMgr.Inst.getAssetAsync("educateanim/" .. var_3_0, var_3_0, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_4_0)
			local var_4_0 = Object.Instantiate(arg_4_0, arg_3_0.cpkParentTF)

			setActive(arg_3_0.bgTF, True)

			arg_3_0.player = var_4_0.transform.Find("usm").GetComponent(typeof(CriManaCpkUI))
			arg_3_0.time = var_3_1

			local var_4_1 = arg_3_0.cpkTF

			arg_3_0.cpkTF = var_4_0

			arg_3_0.player.SetPlayEndHandler(function()
				if arg_3_2:
					arg_3_2()

				arg_3_0.onCpkEnd())

			if arg_3_0._anim:
				arg_3_0._anim.Play()

			arg_3_0.player.SetMaxFrameDrop(CriManaMovieMaterial.MaxFrameDrop.Infinite)
			arg_3_0.player.SetCpkTotalTimeCallback(function(arg_6_0)
				arg_3_0.time = arg_6_0

				arg_3_0.onCpkStart(arg_6_0))
			arg_3_0.player.PlayerManualUpdate()
			arg_3_0.player.PlayCpk()

			if not IsNil(var_4_1):
				Destroy(var_4_1)), True, True)
	elif arg_3_2:
		arg_3_2()

def var_0_0.onCpkStart(arg_7_0, arg_7_1):
	setSlider(arg_7_0.sliderTF, 0, 1, 0)

	arg_7_0.playingTime = 0
	arg_7_0.timer = Timer.New(function()
		arg_7_0.playingTime = arg_7_0.playingTime + 1 / arg_7_0.frameRate

		setSlider(arg_7_0.sliderTF, 0, 1, arg_7_0.playingTime / arg_7_1), 1 / arg_7_0.frameRate, -1)

	arg_7_0.timer.Start()

def var_0_0.onCpkEnd(arg_9_0):
	setSlider(arg_9_0.sliderTF, 0, 1, 1)

	if arg_9_0.timer != None:
		arg_9_0.timer.Stop()

		arg_9_0.timer = None

def var_0_0.SetUIParam(arg_10_0, arg_10_1):
	setAnchoredPosition(arg_10_0.sliderTF, arg_10_1.sliderPos)
	setAnchoredPosition(arg_10_0.cpkParentTF, arg_10_1.cpkPos)
	setAnchoredPosition(arg_10_0.cpkCoverTF, arg_10_1.cpkCoverPos)

	GetComponent(arg_10_0.bgTF, typeof(Image)).enabled = arg_10_1.showCpkBg

def var_0_0.Clear(arg_11_0):
	if not IsNil(arg_11_0.cpkTF):
		Destroy(arg_11_0.cpkTF)

	if arg_11_0.timer != None:
		arg_11_0.timer.Stop()

		arg_11_0.timer = None

	arg_11_0.player = None

	setText(arg_11_0.nameTF, "")
	arg_11_0.Hide()
	gcAll()

return var_0_0
