pg = pg or {}
pg.CpkPlayMgr = singletonClass("CpkPlayMgr")

local var_0_0 = pg.CpkPlayMgr

def var_0_0.Ctor(arg_1_0):
	arg_1_0._onPlaying = False
	arg_1_0._mainTF = None
	arg_1_0._closeLimit = None
	arg_1_0._animator = None
	arg_1_0._timer = None
	arg_1_0._criUsm = None
	arg_1_0._criCpk = None
	arg_1_0._stopGameBGM = False

def var_0_0.Reset(arg_2_0):
	arg_2_0._onPlaying = False
	arg_2_0._mainTF = None
	arg_2_0._closeLimit = None
	arg_2_0._animator = None
	arg_2_0._criUsm = None
	arg_2_0._criCpk = None
	arg_2_0._stopGameBGM = False
	arg_2_0._timer = None

def var_0_0.OnPlaying(arg_3_0):
	return arg_3_0._onPlaying

def var_0_0.PlayCpkMovie(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5, arg_4_6, arg_4_7, arg_4_8, arg_4_9):
	pg.DelegateInfo.New(arg_4_0)

	arg_4_0._onPlaying = True
	arg_4_0._stopGameBGM = arg_4_6

	pg.UIMgr.GetInstance().LoadingOn()

	local function var_4_0()
		if arg_4_0.debugTimer:
			arg_4_0.debugTimer.Stop()

		if not arg_4_0._mainTF:
			return

		if not arg_4_9 and Time.realtimeSinceStartup < arg_4_0._closeLimit:
			return

		setActive(arg_4_0._mainTF, False)
		arg_4_0.DisposeCpkMovie()

		if arg_4_2:
			arg_4_2()

	local function var_4_1()
		onButton(arg_4_0, arg_4_0._mainTF, function()
			if arg_4_5:
				var_4_0())

		if arg_4_0._criUsm:
			arg_4_0._criUsm.player.SetVolume(PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME))
			arg_4_0._criUsm.player.SetShaderDispatchCallback(function(arg_8_0, arg_8_1)
				arg_4_0.checkBgmStop(arg_8_0)

				return None)

		if arg_4_0._criCpk:
			arg_4_0._criCpk.player.SetVolume(PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME))
			arg_4_0._criCpk.player.SetShaderDispatchCallback(function(arg_9_0, arg_9_1)
				arg_4_0.CpkDebug("ShaderDispatchCallback")
				arg_4_0.checkBgmStop(arg_9_0)

				return None)

		if arg_4_0._animator != None:
			arg_4_0._animator.enabled = True

			local var_6_0 = arg_4_0._mainTF.GetComponent("DftAniEvent")

			var_6_0.SetStartEvent(function(arg_10_0)
				if arg_4_0._criUsm:
					arg_4_0._criUsm.Play())
			var_6_0.SetEndEvent(function(arg_11_0)
				var_4_0())
		else
			arg_4_0._timer = Timer.New(var_4_0, arg_4_8)

			arg_4_0._timer.Start()

		setActive(arg_4_0._mainTF, True)

		if arg_4_0._stopGameBGM:
			pg.BgmMgr.GetInstance().StopPlay()

		if arg_4_1:
			arg_4_1()

	if IsNil(arg_4_0._mainTF):
		LoadAndInstantiateAsync(arg_4_3, arg_4_4, function(arg_12_0)
			pg.UIMgr.GetInstance().LoadingOff()

			arg_4_0._closeLimit = Time.realtimeSinceStartup + 1

			if not arg_4_0._onPlaying:
				Destroy(arg_12_0)

				return

			arg_4_0._parentTF = arg_4_0._parentTF or GameObject.Find("UICamera/Canvas")

			setParent(arg_12_0, arg_4_0._parentTF)

			arg_4_0._mainTF = arg_12_0

			pg.UIMgr.GetInstance().OverlayPanel(arg_4_0._mainTF.transform, arg_4_7)

			arg_4_0._criUsm = tf(arg_4_0._mainTF).Find("usm").GetComponent("CriManaEffectUI")
			arg_4_0._criCpk = tf(arg_4_0._mainTF).Find("usm").GetComponent("CriManaCpkUI")
			arg_4_0._usmImg = tf(arg_4_0._mainTF).Find("usm").GetComponent("Image")
			arg_4_0._animator = arg_4_0._mainTF.GetComponent("Animator")

			if arg_4_0._criUsm:
				arg_4_0._criUsm.renderMode = ReflectionHelp.RefGetField(typeof("CriManaMovieMaterial+RenderMode"), "Always", None)

			if arg_4_0._usmImg:
				arg_4_0._usmImg.color = Color.New(1, 1, 1, 1)

			arg_4_0.CpkDebug("Instantiate")

			arg_4_0.debugTimer = Timer.New(function()
				arg_4_0.CpkDebug("After 1s"), 1)

			arg_4_0.debugTimer.Start()
			var_4_1())
	else
		var_4_1()

def var_0_0.CpkDebug(arg_14_0, arg_14_1):
	warning(arg_14_1)

	if arg_14_0._criCpk:
		warning("CriManaMovieController.target ", arg_14_0._criCpk.target)
		warning("CriManaMovieController.useOriginalMaterial ", arg_14_0._criCpk.useOriginalMaterial)
		warning("CriManaMovieController.applyMask ", arg_14_0._criCpk.applyMask)
		warning("CriManaMovieMaterial.isMaterialAvailable ", arg_14_0._criCpk.isMaterialAvailable)
		warning("CriManaMovieMaterial.player ", arg_14_0._criCpk.player)
		warning("CriManaMovieMaterial.material ", arg_14_0._criCpk.material)

		if arg_14_0._criCpk.material:
			warning("Material.Shader", arg_14_0._criCpk.material.shader)
			warning("Material.mainTexture", arg_14_0._criCpk.material.mainTexture)

	if arg_14_0._usmImg:
		warning("usmImage", arg_14_0._usmImg.enabled)

	local var_14_0 = tf(arg_14_0._mainTF).Find("usm")

	if var_14_0:
		warning("usmEnable", isActive(var_14_0))
		warning("UsmPositon", var_14_0.transform.position)
		warning("UsmScale", var_14_0.transform.localScale)
		warning("UsmRotation", var_14_0.transform.localRotation)

	local var_14_1 = var_14_0.GetComponent("AspectRatioFitter")

	if var_14_1:
		warning("AspectRatioFitter", var_14_1.enabled)

	if arg_14_0._animator:
		warning("Animator", arg_14_0._animator.enabled)

def var_0_0.checkBgmStop(arg_15_0, arg_15_1):
	if arg_15_0._onPlaying:
		local var_15_0 = arg_15_1.numAudioStreams

		if var_15_0 and var_15_0 > 0:
			pg.BgmMgr.GetInstance().StopPlay()

			arg_15_0._stopGameBGM = True

def var_0_0.DisposeCpkMovie(arg_16_0):
	if arg_16_0._onPlaying:
		if arg_16_0._mainTF:
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_16_0._mainTF.transform, arg_16_0._tf)
			Destroy(arg_16_0._mainTF)

			if arg_16_0._animator != None:
				arg_16_0._animator.enabled = False

			if arg_16_0._timer != None:
				arg_16_0._timer.Stop()

				arg_16_0._timer = None

			if arg_16_0._criUsm:
				arg_16_0._criUsm.Stop()

			if arg_16_0._stopGameBGM:
				pg.BgmMgr.GetInstance().ContinuePlay()

			arg_16_0._onPlaying = False

			pg.DelegateInfo.Dispose(arg_16_0)

		arg_16_0.Reset()
