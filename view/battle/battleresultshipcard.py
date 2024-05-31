local var_0_0 = class("BattleResultShipCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._expTF = arg_1_1

	arg_1_0.init()

def var_0_0.init(arg_2_0):
	arg_2_0._expContent = findTF(arg_2_0._expTF, "content")
	arg_2_0._expInfo = findTF(arg_2_0._expContent, "exp")
	arg_2_0._nameTxt = findTF(arg_2_0._expContent, "info/name_mask/name")
	arg_2_0._intimacyUpFX = findTF(arg_2_0._expContent, "heartsfly")
	arg_2_0._intimacyDownFX = findTF(arg_2_0._expContent, "heartsbroken")
	arg_2_0._lvText = findTF(arg_2_0._expContent, "dockyard/lv/Text")
	arg_2_0._lvUp = findTF(arg_2_0._expContent, "dockyard/lv_bg/levelUpLabel")
	arg_2_0._lvFX = findTF(arg_2_0._expContent, "dockyard/lv_bg/levelup")
	arg_2_0._expText = findTF(arg_2_0._expInfo, "exp_text")
	arg_2_0._expProgress = findTF(arg_2_0._expInfo, "exp_progress")
	arg_2_0._expImage = arg_2_0._expProgress.GetComponent(typeof(Image))
	arg_2_0._expBuff = findTF(arg_2_0._expInfo, "exp_buff_mask/exp_buff")

	arg_2_0._expTF.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function(arg_3_0)
		arg_2_0.expAnimation())
	SetActive(arg_2_0._expTF, False)

def var_0_0.SetShipVO(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4):
	flushShipCard(arg_4_0._expTF, arg_4_1)

	arg_4_0._oldShipVO = arg_4_1
	arg_4_0._newShipVO = arg_4_2
	arg_4_0._isMVP = arg_4_3
	arg_4_0._buffName = arg_4_4

	arg_4_0.setShipInfo()

def var_0_0.RegisterPreEXPTF(arg_5_0, arg_5_1):
	arg_5_1.GetTF().GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_6_0)
		setActive(arg_5_0._expTF, True))

def var_0_0.ConfigCallback(arg_7_0, arg_7_1):
	arg_7_0._expTF.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_8_0)
		arg_7_1())

def var_0_0.setShipInfo(arg_9_0):
	setScrollText(arg_9_0._nameTxt, arg_9_0._oldShipVO.GetColorName())
	setActive(findTF(arg_9_0._expContent, "mvp"), arg_9_0._isMVP)
	SetActive(arg_9_0._expBuff, arg_9_0._buffName != None)
	setScrollText(arg_9_0._expBuff, arg_9_0._buffName or "")

def var_0_0.expAnimation(arg_10_0):
	SetActive(arg_10_0._expInfo, True)
	SetActive(arg_10_0._intimacyUpFX, arg_10_0._oldShipVO.getIntimacy() < arg_10_0._newShipVO.getIntimacy())
	SetActive(arg_10_0._intimacyDownFX, arg_10_0._oldShipVO.getIntimacy() > arg_10_0._newShipVO.getIntimacy())

	local var_10_0 = arg_10_0._oldShipVO.getConfig("rarity")
	local var_10_1 = getExpByRarityFromLv1(var_10_0, arg_10_0._oldShipVO.level)

	arg_10_0._expImage.fillAmount = arg_10_0._oldShipVO.getExp() / var_10_1

	if arg_10_0._oldShipVO.level < arg_10_0._newShipVO.level:
		local var_10_2 = 0

		for iter_10_0 = arg_10_0._oldShipVO.level, arg_10_0._newShipVO.level - 1:
			var_10_2 = var_10_2 + getExpByRarityFromLv1(var_10_0, iter_10_0)

		arg_10_0.playAnimation(arg_10_0._expTF, 0, var_10_2 + arg_10_0._newShipVO.getExp() - arg_10_0._oldShipVO.getExp(), 1, 0, function(arg_11_0)
			setText(arg_10_0._expText, "+" .. math.ceil(arg_11_0)))

		arg_10_0._animationLV = arg_10_0._oldShipVO.level

		arg_10_0.loopAnimation(arg_10_0._oldShipVO.getExp() / var_10_1, 1, 0.7, True)
	else
		local var_10_3 = math.ceil(arg_10_0._newShipVO.getExp() - arg_10_0._oldShipVO.getExp())

		setText(arg_10_0._expText, "+" .. var_10_3)

		if arg_10_0._oldShipVO.level == arg_10_0._oldShipVO.getMaxLevel():
			arg_10_0._expImage.fillAmount = 1

			return

		arg_10_0.playAnimation(arg_10_0._expTF, arg_10_0._oldShipVO.getExp() / var_10_1, arg_10_0._newShipVO.getExp() / var_10_1, 1, 0, function(arg_12_0)
			arg_10_0._expImage.fillAmount = arg_12_0)

def var_0_0.loopAnimation(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4):
	local var_13_0 = getExpByRarityFromLv1(arg_13_0._oldShipVO.getConfig("rarity"), arg_13_0._newShipVO.level)

	LeanTween.value(go(arg_13_0._expTF), arg_13_1, arg_13_2, arg_13_3).setOnUpdate(System.Action_float(function(arg_14_0)
		arg_13_0._expImage.fillAmount = arg_14_0)).setOnComplete(System.Action(function()
		arg_13_0._animationLV = arg_13_0._animationLV + 1

		if arg_13_4:
			arg_13_0.levelUpEffect()

		if arg_13_0._newShipVO.level == arg_13_0._animationLV:
			if arg_13_0._animationLV == arg_13_0._newShipVO.getMaxLevel():
				arg_13_0._expImage.fillAmount = 1
			else
				arg_13_0.loopAnimation(0, arg_13_0._newShipVO.getExp() / var_13_0, 1, False)
		elif arg_13_0._newShipVO.level > arg_13_0._animationLV:
			arg_13_0.loopAnimation(0, 1, 0.7, True)))

def var_0_0.levelUpEffect(arg_16_0):
	SetActive(arg_16_0._lvUp, True)
	SetActive(arg_16_0._lvFX, True)

	local var_16_0 = arg_16_0._lvUp.localPosition

	LeanTween.moveY(rtf(arg_16_0._lvUp), var_16_0.y + 30, 0.5).setOnComplete(System.Action(function()
		SetActive(arg_16_0._lvUp, False)

		arg_16_0._lvUp.localPosition = var_16_0

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_BOAT_LEVEL_UP)))

	if arg_16_0._animationLV <= arg_16_0._newShipVO.level:
		setText(arg_16_0._lvText, arg_16_0._animationLV)

def var_0_0.Play(arg_18_0):
	setActive(arg_18_0._expTF, True)

def var_0_0.SkipAnimation(arg_19_0):
	arg_19_0._expTF.GetComponent(typeof(Animator)).enabled = False

	SetActive(arg_19_0._expTF, True)
	SetActive(arg_19_0._expContent, True)
	SetActive(arg_19_0._expInfo, True)

	arg_19_0._expTF.GetComponent(typeof(CanvasGroup)).alpha = 1

	LeanTween.cancel(go(arg_19_0._lvUp))
	LeanTween.cancel(go(arg_19_0._expTF))
	SetActive(arg_19_0._intimacyUpFX, arg_19_0._oldShipVO.getIntimacy() < arg_19_0._newShipVO.getIntimacy())
	SetActive(arg_19_0._intimacyDownFX, arg_19_0._oldShipVO.getIntimacy() > arg_19_0._newShipVO.getIntimacy())

	arg_19_0._expContent.localPosition = Vector3(0, 0, 0)

	setText(arg_19_0._lvText, arg_19_0._newShipVO.level)

	if arg_19_0._oldShipVO.level == arg_19_0._oldShipVO.getMaxLevel():
		setText(arg_19_0._expText, "+" .. math.ceil(arg_19_0._newShipVO.getExp() - arg_19_0._oldShipVO.getExp()))

		arg_19_0._expImage.fillAmount = 1
	else
		local var_19_0 = arg_19_0._oldShipVO.getConfig("rarity")

		if arg_19_0._oldShipVO.level < arg_19_0._newShipVO.level:
			local var_19_1 = 0

			for iter_19_0 = arg_19_0._oldShipVO.level, arg_19_0._newShipVO.level - 1:
				var_19_1 = var_19_1 + getExpByRarityFromLv1(var_19_0, iter_19_0)

			setText(arg_19_0._expText, "+" .. var_19_1 + arg_19_0._newShipVO.getExp() - arg_19_0._oldShipVO.getExp())
		else
			setText(arg_19_0._expText, "+" .. math.ceil(arg_19_0._newShipVO.getExp() - arg_19_0._oldShipVO.getExp()))

		arg_19_0._expImage.fillAmount = arg_19_0._newShipVO.getExp() / getExpByRarityFromLv1(var_19_0, arg_19_0._newShipVO.level)

	SetActive(arg_19_0._lvUp, False)

def var_0_0.GetTF(arg_20_0):
	return arg_20_0._expTF

def var_0_0.playAnimation(arg_21_0, arg_21_1, arg_21_2, arg_21_3, arg_21_4, arg_21_5):
	LeanTween.value(arg_21_0.gameObject, arg_21_1, arg_21_2, arg_21_3).setDelay(arg_21_4).setOnUpdate(System.Action_float(function(arg_22_0)
		arg_21_5(arg_22_0)))

def var_0_0.Dispose(arg_23_0):
	arg_23_0._oldShipVO = None
	arg_23_0._newShipVO = None

return var_0_0
