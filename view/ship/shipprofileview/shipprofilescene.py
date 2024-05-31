local var_0_0 = class("ShipProfileScene", import("...base.BaseUI"))

var_0_0.SHOW_SKILL_INFO = "event show skill info"
var_0_0.SHOW_EVALUATION = "event show evalution"
var_0_0.WEDDING_REVIEW = "event wedding review"
var_0_0.INDEX_DETAIL = 1
var_0_0.INDEX_PROFILE = 2
var_0_0.CHAT_ANIMATION_TIME = 0.3
var_0_0.CHAT_SHOW_TIME = 3

local var_0_1 = 0.35

def var_0_0.getUIName(arg_1_0):
	return "ShipProfileUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(CollectionProxy).getShipGroup(arg_2_0.contextData.groupId)

	LoadSpriteAtlasAsync("bg/star_level_bg_" .. var_2_0.rarity2bgPrintForGet(arg_2_0.showTrans), "", arg_2_1)

def var_0_0.setShipGroup(arg_3_0, arg_3_1):
	arg_3_0.shipGroup = arg_3_1
	arg_3_0.groupSkinList = arg_3_1.getDisplayableSkinList()
	arg_3_0.isBluePrintGroup = arg_3_0.shipGroup.isBluePrintGroup()
	arg_3_0.isMetaGroup = arg_3_0.shipGroup.isMetaGroup()

def var_0_0.setShowTrans(arg_4_0, arg_4_1):
	arg_4_0.showTrans = arg_4_1

def var_0_0.setOwnedSkinList(arg_5_0, arg_5_1):
	arg_5_0.ownedSkinList = arg_5_1

def var_0_0.init(arg_6_0):
	arg_6_0.bg = arg_6_0.findTF("bg")
	arg_6_0.staticBg = arg_6_0.bg.Find("static_bg")
	arg_6_0.painting = arg_6_0.findTF("paint")
	arg_6_0.paintingFitter = findTF(arg_6_0.painting, "fitter")
	arg_6_0.paintingInitPos = arg_6_0.painting.transform.localPosition
	arg_6_0.chatTF = arg_6_0.findTF("paint/chat")

	setActive(arg_6_0.chatTF, False)

	arg_6_0.commonPainting = arg_6_0.painting.Find("fitter")
	arg_6_0.l2dRoot = arg_6_0.findTF("live2d", arg_6_0.painting)
	arg_6_0.spinePaintingRoot = arg_6_0.findTF("spinePainting", arg_6_0.painting)
	arg_6_0.spinePaintingBgRoot = arg_6_0.findTF("paintBg/spinePainting")
	arg_6_0.chatBg = arg_6_0.findTF("chatbgtop", arg_6_0.chatTF)
	arg_6_0.initChatBgH = arg_6_0.chatBg.sizeDelta.y
	arg_6_0.chatText = arg_6_0.findTF("Text", arg_6_0.chatBg)
	arg_6_0.name = arg_6_0.findTF("name")
	arg_6_0.nameInitPos = arg_6_0.name.transform.localPosition
	arg_6_0.shipType = arg_6_0.findTF("type", arg_6_0.name)
	arg_6_0.labelName = arg_6_0.findTF("name_mask/Text", arg_6_0.name).GetComponent(typeof(Text))
	arg_6_0.labelEnName = arg_6_0.findTF("english_name", arg_6_0.name).GetComponent(typeof(Text))
	arg_6_0.stars = arg_6_0.findTF("stars", arg_6_0.name)
	arg_6_0.star = arg_6_0.getTpl("star_tpl", arg_6_0.stars)
	arg_6_0.blurPanel = arg_6_0.findTF("blur_panel")
	arg_6_0.top = arg_6_0.findTF("blur_panel/adapt/top")
	arg_6_0.btnBack = arg_6_0.findTF("back", arg_6_0.top)
	arg_6_0.bottomTF = arg_6_0.findTF("bottom")
	arg_6_0.labelHeart = arg_6_0.findTF("adapt/detail_left_panel/heart/label", arg_6_0.blurPanel)
	arg_6_0.btnLike = arg_6_0.findTF("adapt/detail_left_panel/heart/btnLike", arg_6_0.blurPanel)
	arg_6_0.btnLikeAct = arg_6_0.btnLike.Find("like")
	arg_6_0.btnLikeDisact = arg_6_0.btnLike.Find("unlike")
	arg_6_0.obtainBtn = arg_6_0.findTF("bottom/others/obtain_btn")
	arg_6_0.evaBtn = arg_6_0.findTF("bottom/others/eva_btn")
	arg_6_0.viewBtn = arg_6_0.findTF("bottom/others/view_btn")
	arg_6_0.shareBtn = arg_6_0.findTF("bottom/others/share_btn")
	arg_6_0.rotateBtn = arg_6_0.findTF("bottom/others/rotate_btn")
	arg_6_0.cryptolaliaBtn = arg_6_0.findTF("bottom/others/cryptolalia_btn")
	arg_6_0.equipCodeBtn = arg_6_0.findTF("bottom/others/equip_code_btn")
	arg_6_0.leftProfile = arg_6_0.findTF("adapt/profile_left_panel", arg_6_0.blurPanel)
	arg_6_0.modelContainer = arg_6_0.findTF("model", arg_6_0.leftProfile)
	arg_6_0.live2DBtn = ShipProfileLive2dBtn.New(arg_6_0.findTF("L2D_btn", arg_6_0.blurPanel))

	GetComponent(arg_6_0.findTF("L2D_btn", arg_6_0.blurPanel), typeof(Image)).SetNativeSize()
	GetComponent(arg_6_0.findTF("L2D_btn/img", arg_6_0.blurPanel), typeof(Image)).SetNativeSize()

	arg_6_0.spinePaintingBtn = arg_6_0.findTF("SP_btn", arg_6_0.blurPanel)

	GetComponent(arg_6_0.spinePaintingBtn, typeof(Image)).SetNativeSize()
	GetComponent(arg_6_0.findTF("SP_btn/img", arg_6_0.blurPanel), typeof(Image)).SetNativeSize()
	GetComponent(arg_6_0.findTF("adapt/top/title", arg_6_0.blurPanel), typeof(Image)).SetNativeSize()

	arg_6_0.spinePaintingToggle = arg_6_0.spinePaintingBtn.Find("toggle")
	arg_6_0.cvLoader = ShipProfileCVLoader.New()
	arg_6_0.pageTFs = arg_6_0.findTF("pages")
	arg_6_0.paintingView = ShipProfilePaintingView.New(arg_6_0._tf, arg_6_0.painting)
	arg_6_0.toggles = {
		arg_6_0.findTF("bottom/detail"),
		arg_6_0.findTF("bottom/profile")
	}

	local var_6_0 = ShipProfileInformationPage.New(arg_6_0.pageTFs, arg_6_0.event)
	local var_6_1 = ShipProfileDetailPage.New(arg_6_0.pageTFs, arg_6_0.event)

	var_6_0.SetCvLoader(arg_6_0.cvLoader)
	var_6_0.SetCallback(function(arg_7_0)
		arg_6_0.OnCVBtnClick(arg_7_0))

	arg_6_0.pages = {
		var_6_1,
		var_6_0
	}
	arg_6_0.UISkinList = UIItemList.New(arg_6_0.leftProfile.Find("scroll/Viewport/skin_container"), arg_6_0.leftProfile.Find("scroll/Viewport/skin_container/skin_tpl"))

def var_0_0.didEnter(arg_8_0):
	onButton(arg_8_0, arg_8_0.btnBack, function()
		arg_8_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.equipCodeBtn, function()
		arg_8_0.emit(ShipProfileMediator.OPEN_EQUIP_CODE_SHARE, arg_8_0.shipGroup.id), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.cryptolaliaBtn, function()
		arg_8_0.emit(ShipProfileMediator.OPEN_CRYPTOLALIA, arg_8_0.shipGroup.id), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.obtainBtn, function()
		local var_12_0 = {
			type = MSGBOX_TYPE_OBTAIN,
			shipId = arg_8_0.shipGroup.getShipConfigId(),
			list = arg_8_0.shipGroup.groupConfig.description,
			mediatorName = ShipProfileMediator.__cname
		}

		pg.MsgboxMgr.GetInstance().ShowMsgBox(var_12_0))
	onButton(arg_8_0, arg_8_0.evaBtn, function()
		arg_8_0.emit(var_0_0.SHOW_EVALUATION, arg_8_0.shipGroup.id), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.viewBtn, function()
		if LeanTween.isTweening(arg_8_0.chatTF.gameObject):
			LeanTween.cancel(arg_8_0.chatTF.gameObject)

			arg_8_0.chatTF.localScale = Vector3(0, 0, 0)

			if arg_8_0.dailogueCallback:
				arg_8_0.dailogueCallback()

				arg_8_0.dailogueCallback = None

		arg_8_0.paintingView.Start(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.shareBtn, function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeShipProfile), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.rotateBtn, function()
		setActive(arg_8_0._tf, False)
		arg_8_0.emit(ShipProfileMediator.CLICK_ROTATE_BTN, arg_8_0.shipGroup, arg_8_0.showTrans, arg_8_0.skin), SFX_PANEL)
	arg_8_0.live2DBtn.AddListener(function(arg_17_0)
		if arg_17_0:
			arg_8_0.CreateLive2D()

		setActive(arg_8_0.viewBtn, not arg_17_0)
		setActive(arg_8_0.rotateBtn, not arg_17_0)
		setActive(arg_8_0.commonPainting, not arg_17_0)
		setActive(arg_8_0.l2dRoot, arg_17_0)
		arg_8_0.StopDailogue()

		arg_8_0.l2dActioning = None

		if arg_8_0.skin:
			arg_8_0.pages[var_0_0.INDEX_PROFILE].ExecuteAction("Flush", arg_8_0.skin, arg_17_0))

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.toggles):
		onToggle(arg_8_0, iter_8_1, function(arg_18_0)
			if iter_8_0 == var_0_0.INDEX_DETAIL:
				arg_8_0.live2DBtn.Update(arg_8_0.paintingName, False)

				arg_8_0.spinePaintingisOn = False

				arg_8_0.updateSpinePaintingState()
				arg_8_0.DisplaySpinePainting(False)

			if arg_18_0:
				arg_8_0.SwitchPage(iter_8_0), SFX_PANEL)

	arg_8_0.InitCommon()
	arg_8_0.live2DBtn.Update(arg_8_0.paintingName, False)
	arg_8_0.updateSpinePaintingState()
	setActive(arg_8_0.bottomTF, False)
	triggerToggle(arg_8_0.toggles[var_0_0.INDEX_DETAIL], True)

def var_0_0.InitSkinList(arg_19_0):
	arg_19_0.skinBtns = {}

	arg_19_0.UISkinList.make(function(arg_20_0, arg_20_1, arg_20_2)
		if arg_20_0 == UIItemList.EventUpdate:
			local var_20_0 = arg_19_0.groupSkinList[arg_20_1 + 1]
			local var_20_1 = ShipProfileSkinBtn.New(arg_20_2)

			table.insert(arg_19_0.skinBtns, var_20_1)
			var_20_1.Update(var_20_0, arg_19_0.shipGroup, table.contains(arg_19_0.ownedSkinList, var_20_0.id))
			onButton(arg_19_0, var_20_1._tf, function()
				if not var_20_1.unlock:
					pg.TipsMgr.GetInstance().ShowTips(i18n("ship_profile_skin_locked"))

					return

				arg_19_0.contextData.skinIndex = arg_20_1 + 1

				arg_19_0.ShiftSkin(var_20_0)

				if arg_19_0.prevSkinBtn:
					arg_19_0.prevSkinBtn.UnShift()

				var_20_1.Shift()

				arg_19_0.prevSkinBtn = var_20_1, SFX_PANEL)
			setActive(arg_20_2, var_20_0.skin_type == ShipSkin.SKIN_TYPE_DEFAULT or not HXSet.isHxSkin()))
	arg_19_0.UISkinList.align(#arg_19_0.groupSkinList)

def var_0_0.InitCommon(arg_22_0):
	arg_22_0.LoadSkinBg(arg_22_0.shipGroup.rarity2bgPrintForGet(arg_22_0.showTrans))
	setImageSprite(arg_22_0.shipType, GetSpriteFromAtlas("shiptype", arg_22_0.shipGroup.getShipType(arg_22_0.showTrans)))

	arg_22_0.labelName.text = arg_22_0.shipGroup.getName(arg_22_0.showTrans)

	local var_22_0 = arg_22_0.shipGroup.shipConfig

	arg_22_0.labelEnName.text = var_22_0.english_name

	for iter_22_0 = 1, var_22_0.star:
		cloneTplTo(arg_22_0.star, arg_22_0.stars)

	arg_22_0.FlushHearts()

	local var_22_1 = arg_22_0.shipGroup.GetSkin(arg_22_0.showTrans).id

	arg_22_0.SetPainting(var_22_1, arg_22_0.showTrans)

def var_0_0.SetPainting(arg_23_0, arg_23_1, arg_23_2):
	arg_23_0.RecyclePainting()

	if arg_23_2 and arg_23_0.shipGroup.trans:
		arg_23_1 = arg_23_0.shipGroup.groupConfig.trans_skin

	local var_23_0 = pg.ship_skin_template[arg_23_1].painting

	setPaintingPrefabAsync(arg_23_0.painting, var_23_0, "chuanwu")

	arg_23_0.paintingName = var_23_0

	arg_23_0.UpdateCryptolaliaBtn(arg_23_1)

def var_0_0.RecyclePainting(arg_24_0):
	if arg_24_0.paintingName:
		retPaintingPrefab(arg_24_0.painting, arg_24_0.paintingName)

def var_0_0.FlushHearts(arg_25_0):
	local var_25_0 = arg_25_0.shipGroup.hearts

	setText(arg_25_0.labelHeart, var_25_0 > 999 and "999+" or var_25_0)

	arg_25_0.labelHeart.GetComponent("Text").color = arg_25_0.shipGroup.iheart and Color.New(1, 0.6, 0.6) or Color.New(1, 1, 1)

	setActive(arg_25_0.btnLikeDisact, not arg_25_0.shipGroup.iheart)
	setActive(arg_25_0.btnLikeAct, arg_25_0.shipGroup.iheart)

def var_0_0.LoadSkinBg(arg_26_0, arg_26_1):
	arg_26_0.bluePintBg = arg_26_0.isBluePrintGroup and arg_26_0.shipGroup.rarity2bgPrintForGet(arg_26_0.showTrans)
	arg_26_0.metaMainBg = arg_26_0.isMetaGroup and arg_26_0.shipGroup.rarity2bgPrintForGet(arg_26_0.showTrans)

	if arg_26_0.shipSkinBg != arg_26_1:
		arg_26_0.shipSkinBg = arg_26_1

		local function var_26_0(arg_27_0)
			rtf(arg_27_0).localPosition = Vector3(0, 0, 200)

		local function var_26_1()
			PoolMgr.GetInstance().GetUI("raritydesign" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans), True, function(arg_29_0)
				arg_26_0.designBg = arg_29_0
				arg_26_0.designName = "raritydesign" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans)

				arg_29_0.transform.SetParent(arg_26_0.staticBg, False)

				arg_29_0.transform.localPosition = Vector3(1, 1, 1)
				arg_29_0.transform.localScale = Vector3(1, 1, 1)

				arg_29_0.transform.SetSiblingIndex(1)

				local var_29_0 = arg_29_0.GetComponent("Canvas")

				if var_29_0:
					var_29_0.sortingOrder = -90

				setActive(arg_29_0, True))

		local function var_26_2()
			PoolMgr.GetInstance().GetUI("raritymeta" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans), True, function(arg_31_0)
				arg_26_0.metaBg = arg_31_0
				arg_26_0.metaName = "raritymeta" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans)

				arg_31_0.transform.SetParent(arg_26_0.staticBg, False)

				arg_31_0.transform.localPosition = Vector3(1, 1, 1)
				arg_31_0.transform.localScale = Vector3(1, 1, 1)

				arg_31_0.transform.SetSiblingIndex(1)
				setActive(arg_31_0, True))

		local function var_26_3(arg_32_0)
			if arg_26_0.bluePintBg and arg_26_1 == arg_26_0.bluePintBg:
				if arg_26_0.metaBg:
					setActive(arg_26_0.metaBg, False)

				if arg_26_0.designBg and arg_26_0.designName != "raritydesign" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans):
					PoolMgr.GetInstance().ReturnUI(arg_26_0.designName, arg_26_0.designBg)

					arg_26_0.designBg = None

				if not arg_26_0.designBg:
					var_26_1()
				else
					setActive(arg_26_0.designBg, True)
			elif arg_26_0.metaMainBg and arg_26_1 == arg_26_0.metaMainBg:
				if arg_26_0.designBg:
					setActive(arg_26_0.designBg, False)

				if arg_26_0.metaBg and arg_26_0.metaName != "raritymeta" .. arg_26_0.shipGroup.getRarity(arg_26_0.showTrans):
					PoolMgr.GetInstance().ReturnUI(arg_26_0.metaName, arg_26_0.metaBg)

					arg_26_0.metaBg = None

				if not arg_26_0.metaBg:
					var_26_2()
				else
					setActive(arg_26_0.metaBg, True)
			else
				if arg_26_0.designBg:
					setActive(arg_26_0.designBg, False)

				if arg_26_0.metaBg:
					setActive(arg_26_0.metaBg, False)

		pg.DynamicBgMgr.GetInstance().LoadBg(arg_26_0, arg_26_1, arg_26_0.bg, arg_26_0.staticBg, var_26_0, var_26_3)

def var_0_0.SwitchPage(arg_33_0, arg_33_1):
	if arg_33_0.index != arg_33_1:
		seriesAsync({
			function(arg_34_0)
				pg.UIMgr.GetInstance().OverlayPanel(arg_33_0.blurPanel, {
					groupName = LayerWeightConst.GROUP_SHIP_PROFILE
				})
				arg_34_0(),
			function(arg_35_0)
				local var_35_0 = arg_33_0.pages[arg_33_1]
				local var_35_1 = arg_33_1 == var_0_0.INDEX_PROFILE and not var_35_0.GetLoaded()

				var_35_0.ExecuteAction("Update", arg_33_0.shipGroup, arg_33_0.showTrans, function()
					if var_35_1:
						arg_33_0.InitSkinList()

					arg_35_0()),
			function(arg_37_0)
				if not arg_33_0.index:
					arg_37_0()

					return

				arg_33_0.pages[arg_33_0.index].ExecuteAction("ExistAnim", var_0_1)
				arg_37_0(),
			function(arg_38_0)
				local var_38_0 = arg_33_0.pages[arg_33_1]

				SetParent(arg_33_0.bottomTF, var_38_0._tf)
				setActive(arg_33_0.bottomTF, True)
				setAnchoredPosition(arg_33_0.bottomTF, {
					z = 0,
					x = -7,
					y = 24
				})
				var_38_0.ExecuteAction("EnterAnim", var_0_1)
				arg_33_0.TweenPage(arg_33_1)
				arg_38_0(),
			function(arg_39_0)
				arg_33_0.index = arg_33_1

				local var_39_0 = arg_33_0.contextData.skinIndex or 1

				if arg_33_1 == var_0_0.INDEX_PROFILE and var_39_0 <= #arg_33_0.skinBtns:
					triggerButton(arg_33_0.skinBtns[var_39_0]._tf)
		})

def var_0_0.TweenPage(arg_40_0, arg_40_1):
	if arg_40_1 == var_0_0.INDEX_DETAIL:
		LeanTween.moveX(rtf(arg_40_0.leftProfile), -700, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveY(rtf(arg_40_0.live2DBtn._tf), -70, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveY(rtf(arg_40_0.spinePaintingBtn), -70, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveX(rtf(arg_40_0.painting), arg_40_0.paintingInitPos.x, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveX(rtf(arg_40_0.name), arg_40_0.nameInitPos.x, var_0_1).setEase(LeanTweenType.easeInOutSine)
	elif arg_40_1 == var_0_0.INDEX_PROFILE:
		LeanTween.moveX(rtf(arg_40_0.leftProfile), 0, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveY(rtf(arg_40_0.live2DBtn._tf), 60, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveY(rtf(arg_40_0.spinePaintingBtn), 60, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveX(rtf(arg_40_0.painting), arg_40_0.paintingInitPos.x + 50, var_0_1).setEase(LeanTweenType.easeInOutSine)
		LeanTween.moveX(rtf(arg_40_0.name), arg_40_0.nameInitPos.x + 50, var_0_1).setEase(LeanTweenType.easeInOutSine)

def var_0_0.ShiftSkin(arg_41_0, arg_41_1):
	if arg_41_0.index != var_0_0.INDEX_PROFILE or arg_41_0.skin and arg_41_1.id == arg_41_0.skin.id:
		return

	arg_41_0.skin = arg_41_1

	arg_41_0.LoadModel(arg_41_1)
	arg_41_0.SetPainting(arg_41_1.id, False)
	arg_41_0.live2DBtn.Disable()
	arg_41_0.live2DBtn.Update(arg_41_0.paintingName, False)

	local var_41_0
	local var_41_1 = arg_41_1 and arg_41_1.spine_use_live2d == 1 and "spine_painting_bg" or "live2d_bg"

	LoadSpriteAtlasAsync("ui/share/btn_l2d_atlas", var_41_1, function(arg_42_0)
		GetComponent(arg_41_0.findTF("L2D_btn", arg_41_0.blurPanel), typeof(Image)).sprite = arg_42_0
		GetComponent(arg_41_0.findTF("L2D_btn/img", arg_41_0.blurPanel), typeof(Image)).sprite = arg_42_0

		GetComponent(arg_41_0.findTF("L2D_btn", arg_41_0.blurPanel), typeof(Image)).SetNativeSize()
		GetComponent(arg_41_0.findTF("L2D_btn/img", arg_41_0.blurPanel), typeof(Image)).SetNativeSize())

	arg_41_0.spinePaintingisOn = False

	arg_41_0.updateSpinePaintingState()
	arg_41_0.DestroySpinePainting()
	arg_41_0.pages[var_0_0.INDEX_PROFILE].ExecuteAction("Flush", arg_41_1, False)

	local var_41_2
	local var_41_3 = PlayerPrefs.GetInt("paint_hide_other_obj_" .. arg_41_0.skin.painting, 0) == 0

	if arg_41_0.skin.bg_sp and arg_41_0.skin.bg_sp != "" and var_41_3:
		var_41_2 = arg_41_0.skin.bg_sp
	elif arg_41_0.skin.bg and arg_41_0.skin.bg != "":
		var_41_2 = arg_41_0.skin.bg
	else
		var_41_2 = arg_41_0.shipGroup.rarity2bgPrintForGet(arg_41_0.showTrans, arg_41_0.skin.id)

	arg_41_0.LoadSkinBg(var_41_2)

	arg_41_0.haveOp = checkABExist("ui/skinunlockanim/star_level_unlock_anim_" .. arg_41_0.skin.id)

def var_0_0.UpdateCryptolaliaBtn(arg_43_0, arg_43_1):
	local var_43_0 = ShipSkin.New({
		id = arg_43_1
	}).getConfig("ship_group")

	setActive(arg_43_0.cryptolaliaBtn, getProxy(PlayerProxy).getRawData().ExistCryptolalia(var_43_0))

def var_0_0.LoadModel(arg_44_0, arg_44_1):
	if arg_44_0.inLoading:
		return

	arg_44_0.ReturnModel()

	local var_44_0 = arg_44_1.prefab

	arg_44_0.inLoading = True

	PoolMgr.GetInstance().GetSpineChar(var_44_0, True, function(arg_45_0)
		arg_44_0.inLoading = False
		arg_45_0.name = var_44_0
		arg_45_0.transform.localPosition = Vector3.zero
		arg_45_0.transform.localScale = Vector3(0.8, 0.8, 1)

		arg_45_0.transform.SetParent(arg_44_0.modelContainer, False)
		arg_45_0.GetComponent(typeof(SpineAnimUI)).SetAction(arg_44_1.show_skin or "stand", 0)

		arg_44_0.characterModel = arg_45_0
		arg_44_0.modelName = var_44_0)

def var_0_0.ReturnModel(arg_46_0):
	if not IsNil(arg_46_0.characterModel):
		PoolMgr.GetInstance().ReturnSpineChar(arg_46_0.modelName, arg_46_0.characterModel)

def var_0_0.CreateLive2D(arg_47_0):
	arg_47_0.live2DBtn.SetEnable(False)

	if arg_47_0.l2dChar:
		arg_47_0.l2dChar.Dispose()

	local var_47_0 = arg_47_0.shipGroup.getShipConfigId()
	local var_47_1 = pg.ship_skin_template[arg_47_0.skin.id].live2d_offset_profile
	local var_47_2

	if var_47_1 and type(var_47_1) != "string":
		var_47_2 = Vector3(0 + var_47_1[1], -40 + var_47_1[2], 100 + var_47_1[3])
	else
		var_47_2 = Vector3(0, -40, 100)

	local var_47_3 = Live2D.GenerateData({
		ship = Ship.New({
			configId = var_47_0,
			skin_id = arg_47_0.skin.id,
			propose = arg_47_0.shipGroup.married
		}),
		scale = Vector3(52, 52, 52),
		position = var_47_2,
		parent = arg_47_0.l2dRoot
	})

	arg_47_0.l2dChar = Live2D.New(var_47_3, function()
		arg_47_0.live2DBtn.SetEnable(True))

	if isHalfBodyLive2D(arg_47_0.skin.prefab):
		setAnchoredPosition(arg_47_0.l2dRoot, {
			y = -37 - (arg_47_0.painting.rect.height - arg_47_0.l2dRoot.rect.height * 1.5) / 2
		})
	else
		setAnchoredPosition(arg_47_0.l2dRoot, {
			y = 0
		})

	if Live2dConst.UnLoadL2dPating:
		Live2dConst.UnLoadL2dPating()

def var_0_0.GetModelAction(arg_49_0, arg_49_1):
	local var_49_0

	if not arg_49_1.spine_action or arg_49_1.spine_action == "":
		return "stand"
	else
		return arg_49_1.spine_action

def var_0_0.OnCVBtnClick(arg_50_0, arg_50_1):
	if arg_50_0.l2dActioning:
		return

	local var_50_0 = arg_50_1.voice

	local function var_50_1()
		local var_51_0

		if arg_50_1.isEx():
			local var_51_1 = var_50_0.l2d_action .. "_ex"

			if arg_50_0.l2dChar and arg_50_0.l2dChar.checkActionExist(var_51_1):
				var_51_0 = var_51_1
			else
				var_51_0 = var_50_0.l2d_action
		else
			var_51_0 = var_50_0.l2d_action

		if arg_50_0.l2dChar and not arg_50_0.l2dChar.enablePlayAction(var_51_0):
			return

		arg_50_0.UpdatePaintingFace(arg_50_1)

		if arg_50_0.characterModel:
			local var_51_2 = arg_50_0.GetModelAction(var_50_0)

			arg_50_0.characterModel.GetComponent(typeof(SpineAnimUI)).SetAction(var_51_2, 0)

		local var_51_3 = {
			var_0_0.CHAT_SHOW_TIME
		}

		if arg_50_0.live2DBtn.isOn and arg_50_0.l2dChar:
			if arg_50_0.l2dChar.IsLoaded():
				arg_50_0.l2dActioning = True

				if not arg_50_1.L2dHasEvent():
					parallelAsync({
						function(arg_52_0)
							arg_50_0.RemoveLive2DTimer()
							arg_50_0.l2dChar.TriggerAction(var_51_0, arg_52_0),
						function(arg_53_0)
							arg_50_0.PlayVoice(arg_50_1, var_51_3)
							arg_50_0.ShowDailogue(arg_50_1, var_51_3, arg_53_0)
					}, function()
						arg_50_0.l2dActioning = False)
				else
					seriesAsync({
						function(arg_55_0)
							arg_50_0.RemoveLive2DTimer()
							arg_50_0.l2dChar.TriggerAction(var_51_0, arg_55_0, None, function(arg_56_0)
								arg_50_0.PlayVoice(arg_50_1, var_51_3)
								arg_50_0.ShowDailogue(arg_50_1, var_51_3, arg_55_0))
					}, function()
						arg_50_0.l2dActioning = False)
		else
			arg_50_0.PlayVoice(arg_50_1, var_51_3)
			arg_50_0.ShowDailogue(arg_50_1, var_51_3)

	if var_50_0.key == "unlock" and arg_50_0.haveOp:
		arg_50_0.playOpening(var_50_1)
	else
		var_50_1()

def var_0_0.UpdatePaintingFace(arg_58_0, arg_58_1):
	local var_58_0 = arg_58_1.wordData
	local var_58_1 = var_58_0.mainIndex != None
	local var_58_2 = arg_58_1.voice.key

	if var_58_1:
		var_58_2 = "main_" .. var_58_0.mainIndex

	if arg_58_0.paintingFitter.childCount > 0:
		ShipExpressionHelper.SetExpression(arg_58_0.paintingFitter.GetChild(0), arg_58_0.paintingName, var_58_2, var_58_0.maxfavor, arg_58_1.skin.id)

	if arg_58_0.spinePainting:
		local var_58_3 = ShipExpressionHelper.GetExpression(arg_58_0.paintingName, var_58_2, var_58_0.maxfavor, arg_58_1.skin.id)

		if var_58_3 != "":
			arg_58_0.spinePainting.SetAction(var_58_3, 1)
		else
			arg_58_0.spinePainting.SetEmptyAction(1)

def var_0_0.PlayVoice(arg_59_0, arg_59_1, arg_59_2):
	local var_59_0 = arg_59_1.wordData
	local var_59_1 = arg_59_1.skin
	local var_59_2 = arg_59_1.words

	arg_59_0.RemoveCvTimer()

	if not var_59_0.cvPath or var_59_0.cvPath == "":
		return

	if var_59_2.voice_key >= ShipWordHelper.CV_KEY_REPALCE or var_59_2.voice_key_2 >= ShipWordHelper.CV_KEY_REPALCE or var_59_2.voice_key == ShipWordHelper.CV_KEY_BAN_NEW:
		local var_59_3 = 0

		if arg_59_1.isLive2d and arg_59_0.l2dChar and var_59_0.voiceCalibrate:
			var_59_3 = var_59_0.voiceCalibrate

		arg_59_0.cvLoader.DelayPlaySound(var_59_0.cvPath, var_59_3, function(arg_60_0)
			if arg_60_0:
				arg_59_2[1] = long2int(arg_60_0.length) * 0.001)

	local var_59_4 = var_59_0.se

	if arg_59_1.isLive2d and arg_59_0.l2dChar and var_59_4:
		arg_59_0.cvLoader.RawPlaySound("event./ui/" .. var_59_4[1], var_59_4[2])

def var_0_0.RemoveCvSeTimer(arg_61_0):
	if arg_61_0.cvSeTimer:
		arg_61_0.cvSeTimer.Stop()

		arg_61_0.cvSeTimer = None

def var_0_0.RemoveCvTimer(arg_62_0):
	if arg_62_0.cvTimer:
		arg_62_0.cvTimer.Stop()

		arg_62_0.cvTimer = None

def var_0_0.RemoveLive2DTimer(arg_63_0):
	if arg_63_0.Live2DTimer:
		LeanTween.cancel(arg_63_0.Live2DTimer)

		arg_63_0.Live2DTimer = None

def var_0_0.ShowDailogue(arg_64_0, arg_64_1, arg_64_2, arg_64_3):
	arg_64_0.dailogueCallback = arg_64_3 or function()
		return

	local var_64_0 = arg_64_1.wordData.textContent

	if not var_64_0 or var_64_0 == "" or var_64_0 == "None":
		if arg_64_0.dailogueCallback:
			arg_64_0.dailogueCallback()

			arg_64_0.dailogueCallback = None

		return

	local var_64_1 = arg_64_1.wordData.voiceCalibrate
	local var_64_2 = arg_64_0.chatText.GetComponent(typeof(Text))

	setText(arg_64_0.chatText, SwitchSpecialChar(var_64_0))

	var_64_2.alignment = #var_64_2.text > CHAT_POP_STR_LEN and TextAnchor.MiddleLeft or TextAnchor.MiddleCenter

	local var_64_3 = var_64_2.preferredHeight + 120

	arg_64_0.chatBg.sizeDelta = var_64_3 > arg_64_0.initChatBgH and Vector2.New(arg_64_0.chatBg.sizeDelta.x, var_64_3) or Vector2.New(arg_64_0.chatBg.sizeDelta.x, arg_64_0.initChatBgH)

	arg_64_0.StopDailogue()
	setActive(arg_64_0.chatTF, True)
	LeanTween.scale(rtf(arg_64_0.chatTF.gameObject), Vector3.New(1, 1, 1), var_0_0.CHAT_ANIMATION_TIME).setEase(LeanTweenType.easeOutBack).setDelay(var_64_1 and var_64_1 or 0).setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_64_0.chatTF.gameObject), Vector3.New(0, 0, 1), var_0_0.CHAT_ANIMATION_TIME).setEase(LeanTweenType.easeInBack).setDelay(var_0_0.CHAT_ANIMATION_TIME + arg_64_2[1]).setOnComplete(System.Action(function()
			if arg_64_0.dailogueCallback:
				arg_64_0.dailogueCallback()

				arg_64_0.dailogueCallback = None

			if arg_64_0.spinePainting:
				arg_64_0.spinePainting.SetEmptyAction(1)))))

def var_0_0.StopDailogue(arg_68_0):
	LeanTween.cancel(arg_68_0.chatTF.gameObject)

	arg_68_0.chatTF.localScale = Vector3(0, 0)

def var_0_0.onBackPressed(arg_69_0):
	if arg_69_0.paintingView.isPreview:
		arg_69_0.paintingView.Finish(True)

		return

	triggerButton(arg_69_0.btnBack)

def var_0_0.playOpening(arg_70_0, arg_70_1):
	local var_70_0 = "star_level_unlock_anim_" .. arg_70_0.skin.id

	if checkABExist("ui/skinunlockanim/" .. var_70_0):
		pg.CpkPlayMgr.GetInstance().PlayCpkMovie(function()
			return, function()
			if arg_70_1:
				arg_70_1(), "ui/skinunlockanim", var_70_0, True, False, None)
	elif arg_70_1:
		arg_70_1()

def var_0_0.updateSpinePaintingState(arg_73_0):
	local var_73_0 = HXSet.autoHxShiftPath("spinepainting/" .. arg_73_0.paintingName)

	if checkABExist(var_73_0):
		setActive(arg_73_0.spinePaintingBtn, True)
		setActive(arg_73_0.spinePaintingToggle.Find("on"), arg_73_0.spinePaintingisOn)
		setActive(arg_73_0.spinePaintingToggle.Find("off"), not arg_73_0.spinePaintingisOn)
		removeOnButton(arg_73_0.spinePaintingBtn)
		onButton(arg_73_0, arg_73_0.spinePaintingBtn, function()
			arg_73_0.spinePaintingisOn = not arg_73_0.spinePaintingisOn

			setActive(arg_73_0.spinePaintingToggle.Find("on"), arg_73_0.spinePaintingisOn)
			setActive(arg_73_0.spinePaintingToggle.Find("off"), not arg_73_0.spinePaintingisOn)

			if arg_73_0.spinePaintingisOn:
				arg_73_0.CreateSpinePainting()

			setActive(arg_73_0.viewBtn, not arg_73_0.spinePaintingisOn)
			setActive(arg_73_0.rotateBtn, not arg_73_0.spinePaintingisOn)
			setActive(arg_73_0.commonPainting, not arg_73_0.spinePaintingisOn)
			setActive(arg_73_0.spinePaintingRoot, arg_73_0.spinePaintingisOn)
			setActive(arg_73_0.spinePaintingBgRoot, arg_73_0.spinePaintingisOn)
			arg_73_0.StopDailogue()

			if arg_73_0.skin:
				arg_73_0.pages[var_0_0.INDEX_PROFILE].ExecuteAction("Flush", arg_73_0.skin, False), SFX_PANEL)
	else
		setActive(arg_73_0.spinePaintingBtn, False)

def var_0_0.CreateSpinePainting(arg_75_0):
	if arg_75_0.skin.id != arg_75_0.preSkinId:
		arg_75_0.DestroySpinePainting()

		local var_75_0 = arg_75_0.shipGroup.getShipConfigId()
		local var_75_1 = SpinePainting.GenerateData({
			ship = Ship.New({
				configId = var_75_0,
				skin_id = arg_75_0.skin.id
			}),
			position = Vector3(0, 0, 0),
			parent = arg_75_0.spinePaintingRoot,
			effectParent = arg_75_0.spinePaintingBgRoot
		})

		arg_75_0.spinePainting = SpinePainting.New(var_75_1, function()
			return)
		arg_75_0.preSkinId = arg_75_0.skin.id

	arg_75_0.DisplaySpinePainting(True)

def var_0_0.DestroySpinePainting(arg_77_0):
	if arg_77_0.spinePainting:
		arg_77_0.spinePainting.Dispose()

		arg_77_0.spinePainting = None

	arg_77_0.preSkinId = None

def var_0_0.onWeddingReview(arg_78_0, arg_78_1):
	if not arg_78_1 and arg_78_0.exitLoadL2d:
		arg_78_0.exitLoadL2d = False

		arg_78_0.live2DBtn.Update(arg_78_0.paintingName, True)
	else
		arg_78_0.live2DBtn.Update(arg_78_0.paintingName, False)

	arg_78_0.live2DBtn.SetEnable(not arg_78_1)

	if arg_78_0.l2dChar and arg_78_1:
		arg_78_0.l2dChar.Dispose()

		arg_78_0.l2dChar = None
		arg_78_0.l2dActioning = False
		arg_78_0.cvLoader.prevCvPath = None

		arg_78_0.StopDailogue()
		arg_78_0.cvLoader.StopSound()

		arg_78_0.exitLoadL2d = True

def var_0_0.DisplaySpinePainting(arg_79_0, arg_79_1):
	setActive(arg_79_0.spinePaintingRoot, arg_79_1)
	setActive(arg_79_0.spinePaintingBgRoot, arg_79_1)

def var_0_0.willExit(arg_80_0):
	pg.CpkPlayMgr.GetInstance().DisposeCpkMovie()
	SetParent(arg_80_0.bottomTF, arg_80_0._tf)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_80_0.blurPanel, arg_80_0._tf)

	for iter_80_0, iter_80_1 in ipairs(arg_80_0.pages):
		iter_80_1.Destroy()

	if arg_80_0.l2dChar:
		arg_80_0.l2dChar.Dispose()

	arg_80_0.DestroySpinePainting()
	arg_80_0.paintingView.Dispose()
	arg_80_0.live2DBtn.Dispose()
	arg_80_0.cvLoader.Dispose()
	arg_80_0.ReturnModel()
	arg_80_0.RecyclePainting()
	_.each(arg_80_0.skinBtns or {}, function(arg_81_0)
		arg_81_0.Dispose())
	arg_80_0.RemoveCvTimer()
	arg_80_0.RemoveCvSeTimer()
	arg_80_0.RemoveLive2DTimer()

return var_0_0
