local var_0_0 = class("PlayerVitaeShipCard", import(".PlayerVitaeBaseCard"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bgImage = arg_1_0._tf.Find("bg").GetComponent(typeof(Image))
	arg_1_0.paintingTr = arg_1_0._tf.Find("ship_icon/painting")
	arg_1_0.detailTF = arg_1_0._tf.Find("detail")
	arg_1_0.lvTxtTF = arg_1_0.detailTF.Find("top/level")
	arg_1_0.lvTxt = arg_1_0.lvTxtTF.GetComponent(typeof(Text))
	arg_1_0.shipType = arg_1_0.detailTF.Find("top/type")
	arg_1_0.propsTr = arg_1_0.detailTF.Find("info")
	arg_1_0.nameTxt = arg_1_0.detailTF.Find("name_mask/name")
	arg_1_0.frame = arg_1_0._tf.Find("front/frame")
	arg_1_0.UIlist = UIItemList.New(arg_1_0._tf.Find("front/stars"), arg_1_0._tf.Find("front/stars/star_tpl"))
	arg_1_0.shipState = arg_1_0._tf.Find("front/flag")
	arg_1_0.proposeMark = arg_1_0._tf.Find("front/propose")
	arg_1_0.otherBg = arg_1_0._tf.Find("front/bg_other")
	arg_1_0.editTr = arg_1_0._tf.Find("mask")
	arg_1_0.changskinBtn = arg_1_0.editTr.Find("skin")
	arg_1_0.changskinBtnTag = arg_1_0.changskinBtn.Find("Tag")
	arg_1_0.randomTr = arg_1_0._tf.Find("mask1")
	arg_1_0.randomSkinBtn = arg_1_0.randomTr.Find("random_skin")
	arg_1_0.randomShipBtn = arg_1_0.randomTr.Find("random_ship")
	arg_1_0.tipTime = 0
	arg_1_0.nativeTr = arg_1_0._tf.Find("mask_2")

	local var_1_0 = arg_1_0.editTr.Find("tpl")

	eachChild(arg_1_0.editTr, function(arg_2_0)
		if string.find(arg_2_0.gameObject.name, "tpl") and arg_2_0 != var_1_0:
			Object.Destroy(arg_2_0.gameObject))

	arg_1_0.btns = {
		PlayerVitaeSpineBtn.New(var_1_0, PlayerVitaeBaseBtn.VEC_TYPE),
		PlayerVitaeBGBtn.New(var_1_0, PlayerVitaeBaseBtn.VEC_TYPE),
		PlayerVitaeLive2dBtn.New(var_1_0, PlayerVitaeBaseBtn.VEC_TYPE)
	}

	onButton(arg_1_0, arg_1_0.changskinBtn, function()
		arg_1_0.emit(PlayerVitaeMediator.CHANGE_SKIN, arg_1_0.displayShip), SFX_PANEL)
	onButton(arg_1_0, arg_1_0._tf, function()
		if arg_1_0.inEdit:
			return

		if not arg_1_0.canClick:
			if arg_1_0.ShouldTip():
				arg_1_0.SetNextTipTime()
				pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_forbidden"))

			return

		arg_1_0.emit(PlayerVitaeMediator.CHANGE_PAINT, arg_1_0.displayShip), SFX_PANEL)

	arg_1_0.eventTrigger = GetOrAddComponent(arg_1_0._go, typeof(EventTriggerListener))

	arg_1_0.RegisterEvent()
	setText(arg_1_0.randomSkinBtn.Find("Text"), i18n("random_ship_skin_label"))
	setText(arg_1_0.randomShipBtn.Find("Text"), i18n("random_ship_label"))
	setText(arg_1_0.changskinBtn.Find("Text"), i18n("random_flag_ship_changskinBtn_label"))

	arg_1_0.canDragFlag = True

def var_0_0.DisableDrag(arg_5_0):
	arg_5_0.canDragFlag = False

def var_0_0.EnableDrag(arg_6_0):
	arg_6_0.canDragFlag = True

def var_0_0.CanDrag(arg_7_0):
	return not arg_7_0.inEdit and arg_7_0.canDragFlag

def var_0_0.ShouldTip(arg_8_0):
	return arg_8_0.tipTime <= pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.SetNextTipTime(arg_9_0):
	arg_9_0.tipTime = pg.TimeMgr.GetInstance().GetServerTime() + 3

def var_0_0.RegisterEvent(arg_10_0):
	local var_10_0 = arg_10_0.eventTrigger
	local var_10_1 = PlayerVitaeShipsPage.GetSlotMaxCnt()

	var_10_0.AddBeginDragFunc(function()
		if not arg_10_0.CanDrag():
			return

		if not arg_10_0.canClick:
			if arg_10_0.ShouldTip():
				arg_10_0.SetNextTipTime()
				pg.TipsMgr.GetInstance().ShowTips(i18n("random_ship_forbidden"))

			return

		LeanTween.scale(arg_10_0.paintingTr, Vector3(1.1, 1.1, 0), 0.3)
		arg_10_0._tf.SetSiblingIndex(var_10_1 - 1)
		arg_10_0.emit(PlayerVitaeShipsPage.ON_BEGIN_DRAG_CARD, arg_10_0.slotIndex)
		setButtonEnabled(arg_10_0._tf, False))
	var_10_0.AddDragFunc(function(arg_12_0, arg_12_1)
		if not arg_10_0.CanDrag():
			return

		if not arg_10_0.canClick:
			return

		local var_12_0 = arg_10_0.Change2RectPos(arg_10_0._tf.parent, arg_12_1.position)

		arg_10_0._tf.localPosition = Vector3(var_12_0.x, arg_10_0._tf.localPosition.y, 0)

		arg_10_0.emit(PlayerVitaeShipsPage.ON_DRAGING_CARD, var_12_0))
	var_10_0.AddDragEndFunc(function(arg_13_0, arg_13_1)
		if not arg_10_0.CanDrag():
			return

		if not arg_10_0.canClick:
			return

		LeanTween.scale(arg_10_0.paintingTr, Vector3(1, 1, 0), 0.3)
		arg_10_0.emit(PlayerVitaeShipsPage.ON_DRAG_END_CARD)
		setButtonEnabled(arg_10_0._tf, True))

def var_0_0.Change2RectPos(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = GameObject.Find("OverlayCamera").GetComponent("Camera")

	return (LuaHelper.ScreenToLocal(arg_14_1, arg_14_2, var_14_0))

def var_0_0.OnUpdate(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4, arg_15_5):
	arg_15_0.canClick = arg_15_4 != PlayerVitaeShipsPage.RANDOM_FLAG_SHIP_PAGE
	arg_15_0.slotIndex = arg_15_1
	arg_15_0.typeIndex = arg_15_2
	arg_15_0.shipIds = arg_15_3
	arg_15_0.pageType = arg_15_4
	arg_15_0.native = arg_15_5

	local var_15_0 = arg_15_3[arg_15_2]
	local var_15_1 = getProxy(BayProxy).RawGetShipById(var_15_0)

	if not arg_15_0.displayShip or arg_15_0.displayShip.skinId != var_15_1.skinId or arg_15_0.displayShip.id != var_15_1.id:
		arg_15_0.UpdateShip(var_15_1)

	local var_15_2 = not HXSet.isHxSkin() and getProxy(ShipSkinProxy).HasFashion(var_15_1)

	setActive(arg_15_0.changskinBtn, var_15_2)
	setActive(arg_15_0.nativeTr, arg_15_0.canClick and arg_15_0.native)

	if var_15_2:
		arg_15_0.updatePaintingTag(var_15_1)

def var_0_0.Refresh(arg_16_0):
	arg_16_0.OnUpdate(arg_16_0.slotIndex, arg_16_0.typeIndex, arg_16_0.shipIds, arg_16_0.pageType, arg_16_0.native)

	if isActive(arg_16_0.editTr):
		arg_16_0.UpdateBtns()

def var_0_0.UpdateShip(arg_17_0, arg_17_1):
	arg_17_0.displayShip = arg_17_1
	arg_17_0.lvTxt.text = "Lv." .. arg_17_1.level

	local var_17_0 = arg_17_1.getMaxStar()
	local var_17_1 = arg_17_1.getStar()

	arg_17_0.UIlist.make(function(arg_18_0, arg_18_1, arg_18_2)
		if arg_18_0 == UIItemList.EventUpdate:
			setActive(arg_18_2.Find("star"), arg_18_1 < var_17_1))
	arg_17_0.UIlist.align(var_17_0)
	setScrollText(arg_17_0.nameTxt, arg_17_1.GetColorName())
	setPaintingPrefabAsync(arg_17_0.paintingTr, arg_17_1.getPainting(), "biandui")

	local var_17_2 = arg_17_1.rarity2bgPrint()

	GetImageSpriteFromAtlasAsync("bg/star_level_card_" .. var_17_2, "", arg_17_0.bgImage)

	local var_17_3 = arg_17_1.getShipType()

	setImageSprite(arg_17_0.shipType, GetSpriteFromAtlas("shiptype", shipType2print(var_17_3)))

	local var_17_4, var_17_5 = arg_17_1.GetFrameAndEffect(True)

	setRectShipCardFrame(arg_17_0.frame, var_17_2, var_17_4)
	setFrameEffect(arg_17_0.otherBg, var_17_5)
	setProposeMarkIcon(arg_17_0.proposeMark, arg_17_1)
	arg_17_0.UpdateProps(arg_17_1)

def var_0_0.updatePaintingTag(arg_19_0):
	local var_19_0 = arg_19_0.displayShip

	if var_19_0:
		setActive(arg_19_0.changskinBtnTag, #PaintingGroupConst.GetPaintingNameListByShipVO(var_19_0) > 0)

def var_0_0.UpdateProps(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1.getShipCombatPower()
	local var_20_1, var_20_2 = arg_20_1.getIntimacyDetail()
	local var_20_3 = {
		{
			i18n("word_lv"),
			arg_20_1.level
		},
		{
			i18n("attribute_intimacy"),
			var_20_2
		},
		{
			i18n("word_synthesize_power"),
			"<color=#ffff00>" .. var_20_0 .. "</color>"
		}
	}

	for iter_20_0 = 0, 2:
		local var_20_4 = arg_20_0.propsTr.GetChild(iter_20_0)

		if iter_20_0 < #var_20_3:
			var_20_4.gameObject.SetActive(True)

			var_20_4.GetChild(0).GetComponent("Text").text = var_20_3[iter_20_0 + 1][1]
			var_20_4.GetChild(1).GetComponent("Text").text = var_20_3[iter_20_0 + 1][2]
		else
			var_20_4.gameObject.SetActive(False)

def var_0_0.EditCard(arg_21_0, arg_21_1):
	if not arg_21_0.displayShip:
		return

	setActive(arg_21_0.editTr, arg_21_1)
	arg_21_0.UpdateBtns()

	arg_21_0.inEdit = arg_21_1

	setActive(arg_21_0.nativeTr, arg_21_0.canClick and arg_21_0.native and not arg_21_0.inEdit)

def var_0_0.UpdateBtns(arg_22_0):
	local var_22_0 = arg_22_0.displayShip
	local var_22_1 = 0

	for iter_22_0, iter_22_1 in ipairs(arg_22_0.btns):
		local var_22_2 = iter_22_1.IsActive(var_22_0)

		if var_22_2:
			var_22_1 = var_22_1 + 1

		iter_22_1.Update(var_22_2, var_22_1, var_22_0)

def var_0_0.EditCardForRandom(arg_23_0, arg_23_1):
	if not arg_23_0.displayShip:
		return

	setActive(arg_23_0.randomTr, arg_23_1)

	if arg_23_1:
		arg_23_0.UpdateRandomBtns()
	else
		removeOnButton(arg_23_0.randomSkinBtn)
		removeOnButton(arg_23_0.randomShipBtn)
		arg_23_0.ClearRandomFlagValue()

	arg_23_0.inEdit = arg_23_1
	arg_23_0.inRandomEdit = arg_23_1

local function var_0_1(arg_24_0, arg_24_1, arg_24_2, arg_24_3)
	local var_24_0 = arg_24_1.Find("on")
	local var_24_1 = arg_24_1.Find("off")

	onButton(arg_24_0, arg_24_1, function()
		arg_24_2 = not arg_24_2

		setActive(var_24_0, arg_24_2)
		setActive(var_24_1, not arg_24_2)
		arg_24_3(arg_24_2), SFX_PANEL)
	setActive(var_24_0, arg_24_2)
	setActive(var_24_1, not arg_24_2)

def var_0_0.UpdateRandomBtns(arg_26_0):
	local function var_26_0(arg_27_0, arg_27_1)
		return (arg_27_0 and 1 or 0) + (arg_27_1 and 2 or 0)

	local var_26_1 = arg_26_0.slotIndex or 1
	local var_26_2 = getProxy(PlayerProxy).getRawData()
	local var_26_3 = var_26_2.IsOpenRandomFlagShipSkinInPos(var_26_1)
	local var_26_4 = var_26_2.IsOpenRandomFlagShipInPos(var_26_1)

	var_0_1(arg_26_0, arg_26_0.randomSkinBtn, var_26_3, function(arg_28_0)
		var_26_3 = arg_28_0
		arg_26_0.randomFlagValue = var_26_0(var_26_3, var_26_4))
	var_0_1(arg_26_0, arg_26_0.randomShipBtn, var_26_4, function(arg_29_0)
		var_26_4 = arg_29_0
		arg_26_0.randomFlagValue = var_26_0(var_26_3, var_26_4))

	arg_26_0.randomFlagValue = var_26_0(var_26_3, var_26_4)

	setActive(arg_26_0.randomShipBtn, var_26_2.CanRandomFlagShipInPos(var_26_1))

def var_0_0.GetRandomFlagValue(arg_30_0):
	assert(arg_30_0.inRandomEdit)

	if arg_30_0.randomFlagValue:
		return arg_30_0.randomFlagValue
	else
		return getProxy(PlayerProxy).getRawData().RawGetRandomShipAndSkinValueInpos(arg_30_0.slotIndex)

def var_0_0.ClearRandomFlagValue(arg_31_0):
	arg_31_0.randomFlagValue = None

def var_0_0.Disable(arg_32_0):
	var_0_0.super.Disable(arg_32_0)

	arg_32_0.inEdit = False
	arg_32_0.inRandomEdit = False

def var_0_0.OnDispose(arg_33_0):
	local var_33_0 = arg_33_0.displayShip

	if var_33_0:
		retPaintingPrefab(arg_33_0.paintingTr, var_33_0.getPainting())

	ClearEventTrigger(arg_33_0.eventTrigger)

	for iter_33_0, iter_33_1 in ipairs(arg_33_0.btns):
		iter_33_1.Dispose()

	arg_33_0.btns = None

	arg_33_0.Disable()

return var_0_0
