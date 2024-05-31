local var_0_0 = class("NewShipLayer", import("..base.BaseUI"))

var_0_0.PAINT_DURATION = 0.35
var_0_0.STAR_DURATION = 0.5
var_0_0.STAR_ANIMATION_DUR1 = 0.075
var_0_0.STAR_ANIMATION_DUR2 = 0.1
var_0_0.STAR_ANIMATION_DUR3 = 0.4
var_0_0.STAR_ANIMATION_DUR4 = 0.26

local var_0_1 = 19

def var_0_0.getUIName(arg_1_0):
	return "NewShipUI"

def var_0_0.getLayerWeight(arg_2_0):
	return LayerWeightConst.THIRD_LAYER

def var_0_0.preload(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.contextData.ship

	LoadSpriteAsync("newshipbg/bg_" .. var_3_0.rarity2bgPrintForGet(), function(arg_4_0)
		arg_3_0.bgSprite = arg_4_0
		arg_3_0.isLoadBg = True

		arg_3_1())

def var_0_0.init(arg_5_0):
	arg_5_0._animator = GetComponent(arg_5_0._tf, "Animator")
	arg_5_0._canvasGroup = GetOrAddComponent(arg_5_0._tf, typeof(CanvasGroup))
	arg_5_0._shake = arg_5_0.findTF("shake_panel")
	arg_5_0._shade = arg_5_0.findTF("shade")
	arg_5_0._bg = arg_5_0._shake.Find("bg")
	arg_5_0._drag = arg_5_0._shake.Find("drag")
	arg_5_0._paintingTF = arg_5_0._shake.Find("paint")
	arg_5_0._paintingShadowTF = arg_5_0._shake.Find("shadow")
	arg_5_0._dialogue = arg_5_0._shake.Find("dialogue")
	arg_5_0._shipName = arg_5_0._dialogue.Find("bg/name").GetComponent(typeof(Text))
	arg_5_0._shipType = arg_5_0._dialogue.Find("bg/type").GetComponent(typeof(Text))
	arg_5_0._dialogueText = arg_5_0._dialogue.Find("Text")
	arg_5_0._left = arg_5_0._shake.Find("ForNotch/left_panel")
	arg_5_0._lockTF = arg_5_0._left.Find("lock")
	arg_5_0._lockBtn = arg_5_0._left.Find("lock/lock")
	arg_5_0._unlockBtn = arg_5_0._left.Find("lock/unlock_btn")
	arg_5_0._viewBtn = arg_5_0._left.Find("view_btn")
	arg_5_0._evaluationBtn = arg_5_0._left.Find("evaluation_btn")
	arg_5_0._shareBtn = arg_5_0._left.Find("share_btn")
	arg_5_0.audioBtn = arg_5_0._shake.Find("property_btn")
	arg_5_0.clickTF = arg_5_0._shake.Find("click")
	arg_5_0.npc = arg_5_0.findTF("shake_panel/npc")

	setActive(arg_5_0.npc, False)

	arg_5_0.newTF = arg_5_0._shake.Find("New")
	arg_5_0.rarityTF = arg_5_0._shake.Find("rarity")
	arg_5_0.starsTF = arg_5_0.rarityTF.Find("stars")
	arg_5_0.starsCont = arg_5_0.findTF("content", arg_5_0.starsTF)
	arg_5_0._skipButton = arg_5_0._shake.Find("ForNotch/skip")

	setActive(arg_5_0._skipButton, arg_5_0.contextData.canSkipBatch)
	setActive(arg_5_0._left, True)
	setActive(arg_5_0.audioBtn, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf, {
		hideLowerLayer = True,
		weight = arg_5_0.getWeightFromData()
	})

	arg_5_0.metaRepeatTF = arg_5_0.findTF("MetaRepeat", arg_5_0.rarityTF)
	arg_5_0.metaDarkTF = arg_5_0.findTF("MetaMask", arg_5_0._shake)
	arg_5_0.rarityEffect = {}

	if arg_5_0.contextData.autoExitTime:
		arg_5_0.autoExitTimer = Timer.New(function()
			arg_5_0.showExitTip(), arg_5_0.contextData.autoExitTime)

		arg_5_0.autoExitTimer.Start()

		arg_5_0.contextData.autoExitTime = None

	arg_5_0.PauseAnimation()

def var_0_0.voice(arg_7_0, arg_7_1):
	if not arg_7_1:
		return

	arg_7_0.stopVoice()

	arg_7_0._currentVoice = arg_7_1

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_7_1)

def var_0_0.stopVoice(arg_8_0):
	if arg_8_0._currentVoice:
		pg.CriMgr.GetInstance().UnloadSoundEffect_V3(arg_8_0._currentVoice)

	arg_8_0._currentVoice = None

def var_0_0.setShip(arg_9_0, arg_9_1):
	arg_9_0.recyclePainting()

	arg_9_0._shipVO = arg_9_1
	arg_9_0.isRemoulded = arg_9_1.isRemoulded()

	local var_9_0 = arg_9_1.isBluePrintShip()
	local var_9_1 = arg_9_1.isMetaShip()

	setImageSprite(arg_9_0._bg, arg_9_0.bgSprite)
	setActive(arg_9_0.metaDarkTF, arg_9_1.isMetaShip())

	if var_9_0:
		if arg_9_0.metaBg:
			setActive(arg_9_0.metaBg, False)

		if arg_9_0.designBg and arg_9_0.designName != "raritydesign" .. arg_9_1.getRarity():
			PoolMgr.GetInstance().ReturnUI(arg_9_0.designName, arg_9_0.designBg)

			arg_9_0.designBg = None

		if not arg_9_0.designBg:
			PoolMgr.GetInstance().GetUI("raritydesign" .. arg_9_1.getRarity(), True, function(arg_10_0)
				arg_9_0.designBg = arg_10_0
				arg_9_0.designName = "raritydesign" .. arg_9_1.getRarity()

				arg_10_0.transform.SetParent(arg_9_0._shake, False)

				arg_10_0.transform.localPosition = Vector3(1, 1, 1)
				arg_10_0.transform.localScale = Vector3(1, 1, 1)

				arg_10_0.transform.SetSiblingIndex(1)
				setActive(arg_10_0, True))
		else
			setActive(arg_9_0.designBg, True)
	elif var_9_1:
		if arg_9_0.designBg:
			setActive(arg_9_0.designBg, False)

		if arg_9_0.metaBg and arg_9_0.metaName != "raritymeta" .. arg_9_1.getRarity():
			PoolMgr.GetInstance().ReturnUI(arg_9_0.metaName, arg_9_0.metaBg)

			arg_9_0.metaBg = None

		if not arg_9_0.metaBg:
			PoolMgr.GetInstance().GetUI("raritymeta" .. arg_9_1.getRarity(), True, function(arg_11_0)
				arg_9_0.metaBg = arg_11_0
				arg_9_0.metaName = "raritymeta" .. arg_9_1.getRarity()

				arg_11_0.transform.SetParent(arg_9_0._shake, False)

				arg_11_0.transform.localPosition = Vector3(1, 1, 1)
				arg_11_0.transform.localScale = Vector3(1, 1, 1)

				arg_11_0.transform.SetSiblingIndex(1)
				setActive(arg_11_0, True))
		else
			setActive(arg_9_0.metaBg, True)
	else
		if arg_9_0.designBg:
			setActive(arg_9_0.designBg, False)

		if arg_9_0.metaBg:
			setActive(arg_9_0.metaBg, False)

	if arg_9_1.virgin and not arg_9_0.isRemoulded and not arg_9_1.isActivityNpc():
		setActive(arg_9_0.newTF, True)
		LoadImageSpriteAsync("clutter/new", arg_9_0.newTF)

		if OPEN_TEC_TREE_SYSTEM and table.indexof(pg.fleet_tech_ship_template.all, arg_9_0._shipVO.groupId, 1):
			local var_9_2 = pg.fleet_tech_ship_template[arg_9_0._shipVO.groupId].pt_get
			local var_9_3 = ShipType.FilterOverQuZhuType(pg.fleet_tech_ship_template[arg_9_0._shipVO.groupId].add_get_shiptype)
			local var_9_4 = pg.fleet_tech_ship_template[arg_9_0._shipVO.groupId].add_get_attr
			local var_9_5 = pg.fleet_tech_ship_template[arg_9_0._shipVO.groupId].add_get_value

			pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_TECPOINT, {
				point = var_9_2,
				typeList = var_9_3,
				attr = var_9_4,
				value = var_9_5
			})
	else
		setActive(arg_9_0.newTF, False)

		local var_9_6 = arg_9_1.getReMetaSpecialItemVO()

		arg_9_0.updateLockTF(var_9_6 != None)

		if var_9_6:
			local var_9_7 = arg_9_0.findTF("Icon", arg_9_0.metaRepeatTF)
			local var_9_8 = arg_9_0.findTF("Count", arg_9_0.metaRepeatTF)

			setImageSprite(var_9_7, LoadSprite(var_9_6.getConfig("icon")))
			GetImageSpriteFromAtlasAsync(var_9_6.getConfig("icon"), "", var_9_7)
			setText(var_9_8, var_9_6.count)

			local var_9_9 = pg.ship_transform[arg_9_0._shipVO.groupId].exclusive_item[1][2]
			local var_9_10 = pg.ship_transform[arg_9_0._shipVO.groupId].common_item[1][2]
			local var_9_11 = arg_9_0.findTF("Special", arg_9_0.metaRepeatTF)
			local var_9_12 = arg_9_0.findTF("Commom", arg_9_0.metaRepeatTF)

			setActive(var_9_11, var_9_6.id == var_9_9)
			setActive(var_9_12, var_9_6.id == var_9_10)
		else
			setActive(arg_9_0.metaRepeatTF, False)

	setActive(arg_9_0.audioBtn, not arg_9_0.isRemoulded)
	arg_9_0.UpdateLockButton(arg_9_0._shipVO.GetLockState())

	local var_9_13 = arg_9_0._shipVO.getConfigTable()

	if arg_9_0.isRemoulded:
		setPaintingPrefabAsync(arg_9_0._paintingTF, arg_9_0._shipVO.getRemouldPainting(), "huode")
		setPaintingPrefabAsync(arg_9_0._paintingShadowTF, arg_9_0._shipVO.getRemouldPainting(), "huode")
	else
		setPaintingPrefabAsync(arg_9_0._paintingTF, arg_9_0._shipVO.getPainting(), "huode")
		setPaintingPrefabAsync(arg_9_0._paintingShadowTF, arg_9_0._shipVO.getPainting(), "huode")

	arg_9_0._shipType.text = pg.ship_data_by_type[arg_9_0._shipVO.getShipType()].type_name
	arg_9_0._shipName.text = arg_9_1.getName()

	local var_9_14 = arg_9_1.getRarity()
	local var_9_15 = pg.ship_data_template[var_9_13.id].star_max
	local var_9_16 = arg_9_0._shipVO.getStar()

	if not (var_9_15 % 2 == 0) or not (var_9_15 / 2):
		local var_9_17 = math.floor(var_9_15 / 2) + 1

	local var_9_18 = 15

	for iter_9_0 = 1, 6:
		local var_9_19 = arg_9_0.starsTF.Find("content/star_" .. iter_9_0)
		local var_9_20 = var_9_19.Find("star_empty")
		local var_9_21 = var_9_19.Find("star")

		setActive(var_9_21, iter_9_0 <= var_9_16)
		setActive(var_9_20, var_9_16 < iter_9_0)

		if var_9_15 < iter_9_0:
			setActive(var_9_19, False)

	local var_9_22 = arg_9_0._shake.Find("rarity/nation")
	local var_9_23 = LoadSprite("prints/" .. nation2print(var_9_13.nationality) .. "_0")

	if not var_9_23:
		warning("找不到印花, shipConfigId. " .. arg_9_1.configId)
		setActive(var_9_22, False)
	else
		setImageSprite(var_9_22, var_9_23, False)

	local var_9_24 = arg_9_0._shake.Find("rarity/type")
	local var_9_25 = arg_9_0._shake.Find("rarity/type/rarLogo")

	if arg_9_1.isMetaShip():
		LoadImageSpriteAsync("shiprarity/1" .. var_9_14 .. "m", var_9_24, True)
		LoadImageSpriteAsync("shiprarity/1" .. var_9_14 .. "s", var_9_25, True)
	else
		LoadImageSpriteAsync("shiprarity/" .. (var_9_0 and "0" or "") .. var_9_14 .. "m", var_9_24, True)
		LoadImageSpriteAsync("shiprarity/" .. (var_9_0 and "0" or "") .. var_9_14 .. "s", var_9_25, True)

	setActive(var_9_22, False)
	setActive(arg_9_0.rarityTF, False)
	setActive(arg_9_0._shade, True)

	arg_9_0.inAnimating = True

	arg_9_0.AddLeanTween(function()
		return LeanTween.delayedCall(0.5, System.Action(function()
			setActive(var_9_22, True)
			setActive(arg_9_0.rarityTF, True)
			arg_9_0.starsAnimation())))

	local var_9_26 = arg_9_0._shake.Find("ship_type")
	local var_9_27 = var_9_26.Find("stars")
	local var_9_28 = var_9_26.Find("stars/startpl")
	local var_9_29 = var_9_26.Find("english_name")

	setText(var_9_29, arg_9_0._shipVO.getConfig("english_name"))

	local var_9_30 = var_9_27.childCount
	local var_9_31 = arg_9_0._shipVO.getStar()
	local var_9_32 = arg_9_0._shipVO.getMaxStar()

	for iter_9_1 = var_9_30, var_9_32 - 1:
		cloneTplTo(var_9_28, var_9_27)

	local var_9_33 = var_9_27.childCount

	for iter_9_2 = 0, var_9_33 - 1:
		local var_9_34 = var_9_27.GetChild(iter_9_2)

		var_9_34.gameObject.SetActive(iter_9_2 < var_9_32)
		setActive(var_9_34.Find("star"), iter_9_2 < var_9_31)
		setActive(var_9_34.Find("empty"), var_9_31 <= iter_9_2)

	local var_9_35 = arg_9_0._shipVO.getConfigTable()

	findTF(var_9_26, "type_bg/type").GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("shiptype", tostring(arg_9_0._shipVO.getShipType()))

	setScrollText(var_9_26.Find("name_bg/mask/Text"), arg_9_0._shipVO.getName())

	if var_9_0:
		var_9_14 = var_9_14 .. "_1"
	elif arg_9_1.isMetaShip():
		var_9_14 = var_9_14 .. "_2"

	if not arg_9_0.rarityEffect[var_9_14]:
		PoolMgr.GetInstance().GetUI("getrole_" .. var_9_14, True, function(arg_14_0)
			if IsNil(arg_9_0._tf):
				return

			arg_9_0.rarityEffect[var_9_14] = arg_14_0

			arg_14_0.transform.SetParent(arg_9_0._tf, False)

			arg_14_0.transform.localPosition = Vector3(1, 1, 1)
			arg_14_0.transform.localScale = Vector3(1, 1, 1)

			arg_14_0.transform.SetSiblingIndex(1)

			if arg_9_1.isMetaShip():
				local var_14_0 = arg_9_0.findTF("fire_ruchang", tf(arg_14_0))

				var_14_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_15_0)
					setActive(var_9_22, True)
					setActive(var_14_0, False))

			setActive(var_9_22, False)

			arg_9_0.effectObj = arg_14_0

			setActive(arg_9_0.effectObj, arg_9_0.isOpeningEnd))
	else
		arg_9_0.effectObj = arg_9_0.rarityEffect[var_9_14]

		setActive(arg_9_0.effectObj, arg_9_0.isOpeningEnd)

	arg_9_0.playOpening(function()
		arg_9_0.ResumeAnimation()
		arg_9_0.DisplayWord())

def var_0_0.PauseAnimation(arg_17_0):
	arg_17_0._canvasGroup.alpha = 0
	arg_17_0._animator.enabled = False

def var_0_0.ResumeAnimation(arg_18_0):
	arg_18_0._canvasGroup.alpha = 1
	arg_18_0._animator.enabled = True
	arg_18_0.isOpeningEnd = True

	if arg_18_0.effectObj:
		setActive(arg_18_0.effectObj, True)

def var_0_0.DisplayWord(arg_19_0):
	local var_19_0
	local var_19_1 = ""
	local var_19_2

	if arg_19_0.isRemoulded:
		local var_19_3 = arg_19_0._shipVO.getRemouldSkinId()

		var_19_1 = ShipWordHelper.RawGetWord(var_19_3, ShipWordHelper.WORD_TYPE_UNLOCK)

		if var_19_1 == "":
			local var_19_4

			var_19_4, var_19_2, var_19_1 = ShipWordHelper.GetWordAndCV(var_19_3, ShipWordHelper.WORD_TYPE_DROP)
		else
			local var_19_5

			var_19_5, var_19_2, var_19_1 = ShipWordHelper.GetWordAndCV(var_19_3, ShipWordHelper.WORD_TYPE_UNLOCK)
	else
		local var_19_6

		var_19_6, var_19_2, var_19_1 = ShipWordHelper.GetWordAndCV(arg_19_0._shipVO.skinId, ShipWordHelper.WORD_TYPE_UNLOCK)

	setWidgetText(arg_19_0._dialogue, SwitchSpecialChar(var_19_1, True), "Text")

	arg_19_0._dialogue.transform.localScale = Vector3(0, 1, 1)

	SetActive(arg_19_0._dialogue, False)
	arg_19_0.AddLeanTween(function()
		return LeanTween.delayedCall(0.5, System.Action(function()
			SetActive(arg_19_0._dialogue, True)
			arg_19_0.AddLeanTween(function()
				return LeanTween.scale(arg_19_0._dialogue, Vector3(1, 1, 1), 0.1))
			arg_19_0.voice(var_19_2))))

def var_0_0.updateShip(arg_23_0, arg_23_1):
	arg_23_0._shipVO = arg_23_1

def var_0_0.switch2Property(arg_24_0):
	setActive(arg_24_0.newTF, False)
	setActive(arg_24_0._dialogue, False)
	setActive(arg_24_0.rarityTF, False)
	setActive(arg_24_0._shake.Find("rarity/nation"), False)

	local var_24_0 = arg_24_0._shake.Find("ship_type")

	setActive(var_24_0, True)
	arg_24_0.AddLeanTween(function()
		return LeanTween.move(rtf(var_24_0), Vector3(0, -149.55, 0), 0.3))
	arg_24_0.AddLeanTween(function()
		return LeanTween.move(rtf(arg_24_0._paintingTF), Vector3(-59, 21, 0), 0.2))
	arg_24_0.DisplayNewShipDocumentView()

def var_0_0.showExitTip(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0._shipVO.GetLockState()

	if arg_27_0._shipVO.virgin and var_27_0 == Ship.LOCK_STATE_UNLOCK:
		if arg_27_0.effectObj:
			setActive(arg_27_0.effectObj, False)

		if arg_27_0.effectLineObj:
			setActive(arg_27_0.effectLineObj, False)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			content = i18n("ship_lock_tip"),
			def onYes:()
				triggerButton(arg_27_0._lockBtn)

				if arg_27_1:
					arg_27_1()
				else
					arg_27_0.emit(NewShipMediator.ON_EXIT),
			def onNo:()
				if arg_27_1:
					arg_27_1()
				else
					arg_27_0.emit(NewShipMediator.ON_EXIT),
			weight = arg_27_0.getWeightFromData()
		})
	elif arg_27_1:
		arg_27_1()
	else
		arg_27_0.emit(NewShipMediator.ON_EXIT)

def var_0_0.UpdateLockButton(arg_30_0, arg_30_1):
	setActive(arg_30_0._lockBtn, arg_30_1 != Ship.LOCK_STATE_LOCK)
	setActive(arg_30_0._unlockBtn, arg_30_1 != Ship.LOCK_STATE_UNLOCK)

def var_0_0.updateLockTF(arg_31_0, arg_31_1):
	setActive(arg_31_0._lockTF, not arg_31_1)

def var_0_0.didEnter(arg_32_0):
	onButton(arg_32_0, arg_32_0._lockBtn, function()
		arg_32_0.StopAutoExitTimer()
		arg_32_0.emit(NewShipMediator.ON_LOCK, {
			arg_32_0._shipVO.id
		}, Ship.LOCK_STATE_LOCK), SFX_PANEL)
	onButton(arg_32_0, arg_32_0._unlockBtn, function()
		arg_32_0.StopAutoExitTimer()
		arg_32_0.emit(NewShipMediator.ON_LOCK, {
			arg_32_0._shipVO.id
		}, Ship.LOCK_STATE_UNLOCK), SFX_PANEL)
	onButton(arg_32_0, arg_32_0._viewBtn, function()
		arg_32_0.StopAutoExitTimer()

		arg_32_0.isInView = True

		arg_32_0.paintView()
		setActive(arg_32_0.clickTF, False), SFX_PANEL)
	onButton(arg_32_0, arg_32_0._evaluationBtn, function()
		arg_32_0.StopAutoExitTimer()
		arg_32_0.emit(NewShipMediator.ON_EVALIATION, arg_32_0._shipVO.getGroupId()), SFX_PANEL)
	onButton(arg_32_0, arg_32_0._shareBtn, function()
		arg_32_0.StopAutoExitTimer()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeNewShip, None, {
			weight = arg_32_0.getWeightFromData()
		}), SFX_PANEL)
	onButton(arg_32_0, arg_32_0.clickTF, function()
		arg_32_0.StopAutoExitTimer()

		if arg_32_0.isInView or not arg_32_0.isLoadBg:
			return

		arg_32_0.showExitTip(), SFX_CANCEL)
	onButton(arg_32_0, arg_32_0.audioBtn, function()
		arg_32_0.StopAutoExitTimer()

		if arg_32_0.isInView:
			return

		if not arg_32_0.isOpenProperty:
			arg_32_0.switch2Property()

			arg_32_0.isOpenProperty = True

		setActive(arg_32_0.audioBtn, not arg_32_0.isRemoulded and not arg_32_0.isOpenProperty), SFX_PANEL)
	onButton(arg_32_0, arg_32_0._skipButton, function()
		arg_32_0.showExitTip(function()
			arg_32_0.emit(NewShipMediator.ON_SKIP_BATCH)), SFX_PANEL)
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_DOCKYARD_CHARGET)
	pg.SystemGuideMgr.GetInstance().Play(arg_32_0)

def var_0_0.onBackPressed(arg_42_0):
	if arg_42_0.inAnimating:
		return

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if arg_42_0.isInView:
		arg_42_0.hidePaintView(True)

		return

	arg_42_0.DestroyNewShipDocumentView()
	triggerButton(arg_42_0.clickTF)

def var_0_0.paintView(arg_43_0):
	local var_43_0 = {}
	local var_43_1 = arg_43_0._shake.childCount
	local var_43_2 = 0

	while var_43_2 < var_43_1:
		local var_43_3 = arg_43_0._shake.GetChild(var_43_2)

		if var_43_3.gameObject.activeSelf and var_43_3 != arg_43_0._paintingTF and var_43_3 != arg_43_0._bg and var_43_3 != arg_43_0._drag:
			var_43_0[#var_43_0 + 1] = var_43_3

			setActive(var_43_3, False)

		var_43_2 = var_43_2 + 1

	setActive(arg_43_0._paintingShadowTF, False)
	openPortrait()

	local var_43_4 = arg_43_0._paintingTF
	local var_43_5 = var_43_4.anchoredPosition.x
	local var_43_6 = var_43_4.anchoredPosition.y
	local var_43_7 = var_43_4.rect.width
	local var_43_8 = var_43_4.rect.height
	local var_43_9 = arg_43_0._tf.rect.width / UnityEngine.Screen.width
	local var_43_10 = arg_43_0._tf.rect.height / UnityEngine.Screen.height
	local var_43_11 = var_43_7 / 2
	local var_43_12 = var_43_8 / 2
	local var_43_13
	local var_43_14

	if not LeanTween.isTweening(go(var_43_4)):
		arg_43_0.AddLeanTween(function()
			return LeanTween.moveX(rtf(var_43_4), 150, 0.5).setEase(LeanTweenType.easeInOutSine))

	local var_43_15 = GetOrAddComponent(arg_43_0._drag, "MultiTouchZoom")

	var_43_15.SetZoomTarget(arg_43_0._paintingTF)

	local var_43_16 = GetOrAddComponent(arg_43_0._drag, "EventTriggerListener")

	arg_43_0.dragTrigger = var_43_16

	local var_43_17 = True

	var_43_15.enabled = True
	var_43_16.enabled = True

	local var_43_18 = False

	var_43_16.AddPointDownFunc(function(arg_45_0)
		if Input.touchCount == 1 or IsUnityEditor:
			var_43_18 = True
			var_43_17 = True
		elif Input.touchCount >= 2:
			var_43_17 = False
			var_43_18 = False)
	var_43_16.AddPointUpFunc(function(arg_46_0)
		if Input.touchCount <= 2:
			var_43_17 = True)
	var_43_16.AddBeginDragFunc(function(arg_47_0, arg_47_1)
		var_43_18 = False
		var_43_13 = arg_47_1.position.x * var_43_9 - var_43_11 - tf(arg_43_0._paintingTF).localPosition.x
		var_43_14 = arg_47_1.position.y * var_43_10 - var_43_12 - tf(arg_43_0._paintingTF).localPosition.y)
	var_43_16.AddDragFunc(function(arg_48_0, arg_48_1)
		if var_43_17:
			local var_48_0 = tf(arg_43_0._paintingTF).localPosition

			tf(arg_43_0._paintingTF).localPosition = Vector3(arg_48_1.position.x * var_43_9 - var_43_11 - var_43_13, arg_48_1.position.y * var_43_10 - var_43_12 - var_43_14, -22))
	onButton(arg_43_0, arg_43_0._drag, function()
		arg_43_0.hidePaintView(), SFX_CANCEL)

	function var_0_0.hidePaintView(arg_50_0, arg_50_1)
		if not arg_50_1 and not var_43_18:
			return

		var_43_16.enabled = False
		var_43_15.enabled = False

		for iter_50_0, iter_50_1 in ipairs(var_43_0):
			setActive(iter_50_1, True)

		setActive(arg_50_0._paintingShadowTF, True)
		closePortrait()
		LeanTween.cancel(go(arg_50_0._paintingTF))

		arg_50_0._paintingTF.localScale = Vector3(1, 1, 1)

		setAnchoredPosition(arg_50_0._paintingTF, {
			x = var_43_5,
			y = var_43_6
		})

		arg_50_0.isInView = False

		setActive(arg_50_0.clickTF, True)

def var_0_0.recyclePainting(arg_51_0):
	if arg_51_0._shipVO:
		retPaintingPrefab(arg_51_0._paintingTF, arg_51_0._shipVO.getPainting())
		retPaintingPrefab(arg_51_0._paintingShadowTF, arg_51_0._shipVO.getPainting())

		arg_51_0._shipVO = None

def var_0_0.starsAnimation(arg_52_0):
	arg_52_0.inAnimating = True

	if arg_52_0._shipVO.getMaxStar() >= 6 and PlayerPrefs.GetInt(RARE_SHIP_VIBRATE, 1) > 0:
		LuaHelper.Vibrate()

	setActive(arg_52_0.starsCont, False)

	local var_52_0 = arg_52_0._tf.GetComponent(typeof(DftAniEvent))

	var_52_0.SetTriggerEvent(function(arg_53_0)
		arg_52_0.AddLeanTween(function()
			return LeanTween.scale(rtf(arg_52_0.starsCont), Vector3.one, 0).setOnComplete(System.Action(function()
				setActive(arg_52_0.starsCont, True))))

		local var_53_0 = arg_52_0.STAR_ANIMATION_DUR1

		for iter_53_0 = 0, arg_52_0.starsCont.childCount - 1:
			local var_53_1 = arg_52_0.starsCont.GetChild(iter_53_0)
			local var_53_2 = var_53_1.Find("star_empty")
			local var_53_3 = var_53_1.Find("star")

			setActive(var_53_2, False)
			setActive(var_53_3, False)

			local var_53_4 = iter_53_0 * var_53_0

			arg_52_0.AddLeanTween(function()
				return LeanTween.scale(rtf(var_53_2), Vector3(1.8, 1.8, 1.8), 0).setDelay(var_53_4).setOnComplete(System.Action(function()
					setActive(var_53_2, True)
					arg_52_0.AddLeanTween(function()
						return LeanTween.scale(rtf(var_53_2), Vector3(1, 1, 1), var_53_0)))))

		local var_53_5 = arg_52_0._shipVO.getStar()
		local var_53_6 = arg_52_0.STAR_ANIMATION_DUR2
		local var_53_7 = arg_52_0.STAR_ANIMATION_DUR3

		for iter_53_1 = 0, var_53_5 - 1:
			local var_53_8 = arg_52_0.starsCont.GetChild(iter_53_1)
			local var_53_9 = var_53_8.Find("star_empty")
			local var_53_10 = var_53_8.Find("star")
			local var_53_11 = var_53_0 * arg_52_0.starsCont.childCount + iter_53_1 * var_53_6

			arg_52_0.AddLeanTween(function()
				return LeanTween.scale(rtf(var_53_10), Vector3(1.8, 1.8, 1.8), 0).setDelay(var_53_11).setOnStart(System.Action(function()
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_DOCKYARD_STAR))).setOnComplete(System.Action(function()
					setActive(var_53_9, False)
					setActive(var_53_10, True)
					arg_52_0.AddLeanTween(function()
						return LeanTween.scale(rtf(var_53_10), Vector3(1, 1, 1), var_53_6)))))

			local var_53_12 = var_53_8.Find("light")

			if var_53_12:
				arg_52_0.AddLeanTween(function()
					return LeanTween.delayedCall(var_53_11, System.Action(function()
						if arg_52_0.exited:
							return

						setActive(var_53_12, True))))
				arg_52_0.AddLeanTween(function()
					return LeanTween.alpha(rtf(var_53_12), 0, var_53_7).setDelay(var_53_11).setOnComplete(System.Action(function()
						SetActive(var_53_12, False)
						LeanTween.alpha(rtf(var_53_12), 1, 0))))

				var_53_12.transform.localScale = Vector3(1, 1, 1)

				arg_52_0.AddLeanTween(function()
					return LeanTween.scale(rtf(var_53_12), Vector3(0.5, 1, 1), arg_52_0.STAR_ANIMATION_DUR4).setDelay(var_53_11 + var_53_7 * 1 / 3)))
	var_52_0.SetEndEvent(function(arg_68_0)
		if arg_52_0._shipVO.getReMetaSpecialItemVO():
			GetComponent(arg_52_0.metaRepeatTF, "CanvasGroup").alpha = 1

			arg_52_0.managedTween(LeanTween.value, function()
				setAnchoredPosition(arg_52_0.metaRepeatTF, {
					x = 0
				})

				arg_52_0.inAnimating = False

				setActive(arg_52_0.npc, arg_52_0._shipVO.isActivityNpc())
				setActive(arg_52_0._shade, False), go(arg_52_0.metaRepeatTF), arg_52_0.metaRepeatTF.rect.width, 0, 1).setOnUpdate(System.Action_float(function(arg_70_0)
				setAnchoredPosition(arg_52_0.metaRepeatTF, {
					x = arg_70_0
				})))
			setAnchoredPosition(arg_52_0.metaRepeatTF, {
				x = arg_52_0.metaRepeatTF.rect.width
			})
			setActive(arg_52_0.metaRepeatTF, True)
		else
			arg_52_0.inAnimating = False

			setActive(arg_52_0.npc, arg_52_0._shipVO.isActivityNpc())
			setActive(arg_52_0._shade, False))

def var_0_0.playOpening(arg_71_0, arg_71_1):
	if arg_71_0._shipVO.isMetaShip() and not getProxy(ContextProxy).getContextByMediator(BuildShipMediator):
		if arg_71_1:
			arg_71_1()

		return

	local var_71_0

	if arg_71_0._shipVO.isRemoulded():
		var_71_0 = ShipGroup.GetGroupConfig(arg_71_0._shipVO.getGroupId()).trans_skin
	else
		var_71_0 = ShipGroup.getDefaultSkin(arg_71_0._shipVO.getGroupId()).id

	local var_71_1 = "star_level_unlock_anim_" .. var_71_0

	if checkABExist("ui/skinunlockanim/" .. var_71_1):
		pg.CpkPlayMgr.GetInstance().PlayCpkMovie(function()
			return, function()
			if arg_71_1:
				arg_71_1(), "ui/skinunlockanim", var_71_1, True, False, {
			weight = arg_71_0.getWeightFromData()
		})
	elif arg_71_1:
		arg_71_1()

def var_0_0.ClearTweens(arg_74_0, arg_74_1):
	arg_74_0.cleanManagedTween(True)

def var_0_0.willExit(arg_75_0):
	pg.CpkPlayMgr.GetInstance().DisposeCpkMovie()
	arg_75_0.StopAutoExitTimer()
	arg_75_0.DestroyNewShipDocumentView()

	if arg_75_0.designBg:
		PoolMgr.GetInstance().ReturnUI(arg_75_0.designName, arg_75_0.designBg)

	if arg_75_0.metaBg:
		PoolMgr.GetInstance().ReturnUI(arg_75_0.metaName, arg_75_0.metaBg)

	for iter_75_0, iter_75_1 in pairs(arg_75_0.rarityEffect):
		if iter_75_1:
			PoolMgr.GetInstance().ReturnUI("getrole_" .. iter_75_0, iter_75_1)

	if arg_75_0.dragTrigger:
		ClearEventTrigger(arg_75_0.dragTrigger)

		arg_75_0.dragTrigger = None

	if not arg_75_0.isRemoulded:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_newShipLayer_get", pg.ship_data_by_type[arg_75_0._shipVO.getShipType()].type_name, arg_75_0._shipVO.getName()), COLOR_GREEN)

	arg_75_0.recyclePainting()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_75_0._tf)
	arg_75_0.stopVoice()

	if arg_75_0.loadedCVBankName:
		pg.CriMgr.UnloadCVBank(arg_75_0.loadedCVBankName)

		arg_75_0.loadedCVBankName = None

	if LeanTween.isTweening(go(arg_75_0.rarityTF)):
		LeanTween.cancel(go(arg_75_0.rarityTF))

	cameraPaintViewAdjust(False)

def var_0_0.DisplayNewShipDocumentView(arg_76_0):
	arg_76_0.newShipDocumentView = NewShipDocumentView.New(arg_76_0._shake.Find("ForNotch"), arg_76_0.event, arg_76_0.contextData)

	arg_76_0.newShipDocumentView.Load()

	local function var_76_0()
		if not arg_76_0.isLoadBg:
			return

		arg_76_0.showExitTip()

	arg_76_0.newShipDocumentView.ActionInvoke("SetParams", arg_76_0._shipVO, var_76_0)
	arg_76_0.newShipDocumentView.ActionInvoke("RefreshUI")

def var_0_0.DestroyNewShipDocumentView(arg_78_0):
	if arg_78_0.newShipDocumentView and arg_78_0.newShipDocumentView.CheckState(BaseSubView.STATES.INITED):
		arg_78_0.newShipDocumentView.Destroy()

def var_0_0.StopAutoExitTimer(arg_79_0):
	if not arg_79_0.autoExitTimer:
		return

	arg_79_0.autoExitTimer.Stop()

	arg_79_0.autoExitTimer = None

return var_0_0
