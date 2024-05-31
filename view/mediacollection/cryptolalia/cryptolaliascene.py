local var_0_0 = class("CryptolaliaScene", import("view.base.BaseUI"))

var_0_0.ON_UNLOCK = "CryptolaliaScene.ON_UNLOCK"
var_0_0.ON_DELETE = "CryptolaliaScene.ON_DELETE"
var_0_0.ON_SELECT = "CryptolaliaScene.ON_SELECT"

def var_0_0.getUIName(arg_1_0):
	return "CryptolaliaUI"

def var_0_0.SetCryptolaliaList(arg_2_0, arg_2_1):
	arg_2_0.cryptolaliaList = arg_2_1

def var_0_0.init(arg_3_0):
	arg_3_0.cg = arg_3_0._tf.GetComponent(typeof(CanvasGroup))
	arg_3_0.backBtn = arg_3_0.findTF("Top/blur_panel/adapt/top/back_btn")
	arg_3_0.auditionBtn = arg_3_0.findTF("Main/audition/toggle")
	arg_3_0.auditionBtnOn = arg_3_0.findTF("Main/audition/toggle/on")
	arg_3_0.auditionBtnOff = arg_3_0.findTF("Main/audition/toggle/off")
	arg_3_0.cdImg = arg_3_0.findTF("Main/cd").GetComponent(typeof(Image))
	arg_3_0.cdSignatureImg = arg_3_0.findTF("Main/cd/signature").GetComponent(typeof(Image))
	arg_3_0.shipName = arg_3_0.findTF("Main/cd/name").GetComponent(typeof(Text))
	arg_3_0.timeLimit = arg_3_0.findTF("Main/cd/timelimit")
	arg_3_0.timeTxt = arg_3_0.findTF("Main/cd/timelimit/Text").GetComponent(typeof(Text))
	arg_3_0.nameTxt = arg_3_0.findTF("Main/name").GetComponent(typeof(Text))
	arg_3_0.authorTxt = arg_3_0.findTF("Main/name/author").GetComponent(typeof(Text))
	arg_3_0.descTxt = arg_3_0.findTF("Main/desc").GetComponent(typeof(Text))
	arg_3_0.signatureImg = arg_3_0.findTF("Main/desc/signature").GetComponent(typeof(Image))
	arg_3_0.auditionTxt = arg_3_0.findTF("Main/audition/mask/Text").GetComponent("ScrollText")
	arg_3_0.auditionEffect = arg_3_0.findTF("Main/audition/p2/Lines").GetComponent(typeof(Animation))

	arg_3_0.auditionEffect.Play("anim_line_reset")

	arg_3_0.btnsTr = arg_3_0.findTF("Main/btns")
	arg_3_0.lockBtn = arg_3_0.btnsTr.Find("lock")
	arg_3_0.downloadBtn = arg_3_0.btnsTr.Find("download")
	arg_3_0.downloadingBtn = arg_3_0.btnsTr.Find("downloading")
	arg_3_0.playBtn = arg_3_0.btnsTr.Find("play")
	arg_3_0.playPrevBtn = arg_3_0.btnsTr.Find("play/prev")
	arg_3_0.playNextBtn = arg_3_0.btnsTr.Find("play/next")
	arg_3_0.deleteBtn = arg_3_0.btnsTr.Find("delete")
	arg_3_0.stateBtn = arg_3_0.btnsTr.Find("state")
	arg_3_0.stateBtnTxt = arg_3_0.stateBtn.Find("Text").GetComponent(typeof(Text))
	arg_3_0.switchBtn = arg_3_0.btnsTr.Find("switch")
	arg_3_0.listBtn = arg_3_0.btnsTr.Find("list")
	arg_3_0.optionBtn = arg_3_0.findTF("Top/blur_panel/adapt/top/option")
	arg_3_0.purchaseWindow = CryptolaliaPurchaseWindow.New(arg_3_0._tf, arg_3_0.event)
	arg_3_0.resDeleteWindow = CryptolaliaResDeleteWindow.New(arg_3_0._tf, arg_3_0.event)
	arg_3_0.downloadMgr = CryptolaliaDownloadMgr.New()
	arg_3_0.soundPlayer = CryptolaliaSoundPlayer.New()
	arg_3_0.mainView = CryptolaliaMainView.New(arg_3_0)
	arg_3_0.listView = CryptolaliaListView.New(arg_3_0._tf, arg_3_0.event)

	local var_3_0 = CryptolaliaScrollRectAnimation.New(arg_3_0._tf)

	arg_3_0.scrollRect = CryptolaliaScrollRect.New(arg_3_0.findTF("Main/list/tpl"), var_3_0)

	arg_3_0.scrollRect.Make(function(arg_4_0)
		arg_3_0.OnItemUpdate(arg_4_0), function(arg_5_0)
		arg_3_0.OnItemSelected(arg_5_0.GetInitIndex()))

	arg_3_0.dftAniEvent = arg_3_0._tf.GetComponent(typeof(DftAniEvent))

	setText(arg_3_0.findTF("Main/cd/timelimit/label"), i18n("cryptolalia_timelimie"))
	setText(arg_3_0.downloadingBtn.Find("label"), i18n("cryptolalia_label_downloading"))

	Input.multiTouchEnabled = False

def var_0_0.didEnter(arg_6_0):
	arg_6_0.cards = {}
	arg_6_0.downloadReqList = {}

	parallelAsync({
		function(arg_7_0)
			arg_6_0.dftAniEvent.SetEndEvent(arg_7_0),
		function(arg_8_0)
			arg_6_0.InitCryptolaliaList(arg_8_0)
	}, function()
		arg_6_0.dftAniEvent.SetEndEvent(None)
		arg_6_0.scrollRect.SetUp()
		arg_6_0.ActiveDefault()
		arg_6_0.RegisterEvent())

def var_0_0.ActiveDefault(arg_10_0):
	if not arg_10_0.contextData.groupId:
		return

	local var_10_0 = -1

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.displays):
		if iter_10_1 and iter_10_1.IsSameGroup(arg_10_0.contextData.groupId):
			var_10_0 = iter_10_0

			break

	if var_10_0 <= 0:
		return

	for iter_10_2, iter_10_3 in pairs(arg_10_0.cards):
		if iter_10_3.GetInitIndex() == var_10_0:
			triggerButton(iter_10_3._go)

			break

def var_0_0.OnItemUpdate(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.displays[arg_11_1.GetInitIndex()]

	arg_11_1.Interactable(False)

	if not var_11_0:
		return

	arg_11_1.Interactable(True)

	local var_11_1 = var_11_0.GetShipGroupId()

	LoadSpriteAtlasAsync("CryptolaliaShip/" .. var_11_1, "icon", function(arg_12_0)
		arg_11_1.UpdateSprite(arg_12_0))

	arg_11_0.cards[var_11_0.id] = arg_11_1

def var_0_0.OnItemSelected(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.displays[arg_13_1]

	if not var_13_0:
		return

	if not arg_13_0.langType or not var_13_0.ExistLang(arg_13_0.langType):
		arg_13_0.langType = var_13_0.GetDefaultLangType()

	local var_13_1 = var_13_0.GetCpkName(arg_13_0.langType)
	local var_13_2 = Cryptolalia.BuildCpkPath(var_13_1)
	local var_13_3 = arg_13_0.downloadMgr.IsDownloadState(var_13_2)

	if var_13_3 and arg_13_0.downloadReqList[var_13_0.id] == None:
		arg_13_0.OnUpdateForResDownload("ReConnection", var_13_0, arg_13_1)

	arg_13_0.mainView.Flush(var_13_0, arg_13_0.langType, var_13_3)

	arg_13_0.selectedIndex = arg_13_1

	if arg_13_0.auditionFlag:
		triggerButton(arg_13_0.auditionBtn)

def var_0_0.Filter(arg_14_0):
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.cryptolaliaList or {}):
		if iter_14_1.InTime() or not iter_14_1.IsLock():
			table.insert(var_14_0, iter_14_1)

	table.sort(var_14_0, function(arg_15_0, arg_15_1)
		local var_15_0 = arg_15_0.GetSortIndex()
		local var_15_1 = arg_15_1.GetSortIndex()

		if var_15_0 == var_15_1:
			return arg_15_0.id < arg_15_1.id
		else
			return var_15_0 < var_15_1)

	return var_14_0

def var_0_0.InitCryptolaliaList(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.Filter()

	arg_16_0.displays = arg_16_0.FillEmptyDisplayIfNeed(var_16_0)

	arg_16_0.scrollRect.Align(#arg_16_0.displays, arg_16_1)

def var_0_0.FillEmptyDisplayIfNeed(arg_17_0, arg_17_1):
	local var_17_0 = {}

	for iter_17_0 = 1, math.max(5, #arg_17_1):
		local var_17_1 = defaultValue(arg_17_1[iter_17_0], False)

		if iter_17_0 % 2 == 0:
			table.insert(var_17_0, var_17_1)
		else
			table.insert(var_17_0, 1, var_17_1)

	return var_17_0

def var_0_0.RegisterEvent(arg_18_0):
	arg_18_0.bind(var_0_0.ON_UNLOCK, function(arg_19_0, arg_19_1)
		arg_18_0.OnUnlockCryptolalia(arg_19_1))
	arg_18_0.bind(var_0_0.ON_DELETE, function(arg_20_0)
		if not arg_18_0.selectedIndex:
			return

		arg_18_0.OnItemSelected(arg_18_0.selectedIndex))
	arg_18_0.bind(var_0_0.ON_SELECT, function(arg_21_0, arg_21_1)
		local var_21_0 = arg_18_0.cards[arg_21_1]

		if var_21_0:
			triggerButton(var_21_0._go))
	onButton(arg_18_0, arg_18_0.optionBtn, function()
		arg_18_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.backBtn, function()
		arg_18_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_18_0, arg_18_0.switchBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_24_0 = arg_18_0.displays[arg_18_0.selectedIndex]

		if not var_24_0:
			return

		if not var_24_0.IsMultiVersion():
			pg.TipsMgr.GetInstance().ShowTips(i18n("cryptolalia_coming_soom"))

			return

		arg_18_0.langType = 1 - arg_18_0.langType

		arg_18_0.OnItemSelected(arg_18_0.selectedIndex), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.listBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_25_0 = arg_18_0.displays[arg_18_0.selectedIndex]

		if var_25_0:
			local var_25_1 = arg_18_0.Filter()

			arg_18_0.listView.ExecuteAction("Show", var_25_1, arg_18_0.langType, var_25_0.id, arg_18_0.scrollRect), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.deleteBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_26_0 = arg_18_0.displays[arg_18_0.selectedIndex]

		if var_26_0 and var_26_0.IsPlayableState(arg_18_0.langType):
			arg_18_0.resDeleteWindow.ExecuteAction("Show", var_26_0, arg_18_0.langType), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.playBtn.Find("play"), function()
		if not arg_18_0.selectedIndex:
			return

		arg_18_0.PlayVedio(arg_18_0.selectedIndex), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.playNextBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_28_0 = arg_18_0.displays[arg_18_0.selectedIndex + 1]

		if var_28_0:
			arg_18_0.emit(var_0_0.ON_SELECT, var_28_0.id), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.playPrevBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_29_0 = arg_18_0.displays[arg_18_0.selectedIndex - 1]

		if var_29_0:
			arg_18_0.emit(var_0_0.ON_SELECT, var_29_0.id), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.downloadBtn, function()
		if not arg_18_0.selectedIndex:
			return

		arg_18_0.DownloadRes(arg_18_0.selectedIndex), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.lockBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_31_0 = arg_18_0.displays[arg_18_0.selectedIndex]

		if var_31_0 and var_31_0.IsLockState():
			arg_18_0.purchaseWindow.ExecuteAction("Show", var_31_0, arg_18_0.langType), SFX_PANEL)

	arg_18_0.auditionFlag = False

	onButton(arg_18_0, arg_18_0.auditionBtn, function()
		if not arg_18_0.selectedIndex:
			return

		local var_32_0 = arg_18_0.displays[arg_18_0.selectedIndex]

		if not var_32_0:
			return

		arg_18_0.auditionFlag = not arg_18_0.auditionFlag

		if arg_18_0.auditionFlag:
			arg_18_0.PlayAudition(var_32_0)
		else
			arg_18_0.ClearAuditionTimer()
			arg_18_0.soundPlayer.Stop()
			arg_18_0.auditionEffect.Play("anim_line_reset")

		arg_18_0.UpdateAudition(arg_18_0.auditionFlag), SFX_PANEL)
	arg_18_0.UpdateAudition(arg_18_0.auditionFlag)

def var_0_0.UpdateAudition(arg_33_0, arg_33_1):
	setActive(arg_33_0.auditionBtnOn, arg_33_1)
	setActive(arg_33_0.auditionBtnOff, not arg_33_1)

def var_0_0.PlayAudition(arg_34_0, arg_34_1):
	arg_34_0.ClearAuditionTimer()
	arg_34_0.auditionEffect.Play("anim_line_loop")

	local var_34_0 = getProxy(PlayerProxy).getRawData().GetFlagShip()
	local var_34_1 = arg_34_1.GetAudition(arg_34_0.langType)
	local var_34_2 = arg_34_1.GetAuditionVoice(arg_34_0.langType)

	arg_34_0.soundPlayer.Load(var_34_1, var_34_2, 0, function(arg_35_0)
		arg_34_0.timer = Timer.New(function()
			if arg_34_0.auditionFlag:
				triggerButton(arg_34_0.auditionBtn), arg_35_0, 1)

		arg_34_0.timer.Start())

def var_0_0.ClearAuditionTimer(arg_37_0):
	if arg_37_0.timer:
		arg_37_0.timer.Stop()

		arg_37_0.timer = None

def var_0_0.IsDownloading(arg_38_0, arg_38_1):
	if not arg_38_1:
		return False

	if arg_38_1.ExistLang(Cryptolalia.LANG_TYPE_CH):
		local var_38_0 = arg_38_1.GetCpkName(Cryptolalia.LANG_TYPE_CH)
		local var_38_1 = Cryptolalia.BuildCpkPath(var_38_0)

		if arg_38_0.downloadMgr.IsDownloadState(var_38_1):
			return True

	if arg_38_1.ExistLang(Cryptolalia.LANG_TYPE_JP):
		local var_38_2 = arg_38_1.GetCpkName(Cryptolalia.LANG_TYPE_JP)
		local var_38_3 = Cryptolalia.BuildCpkPath(var_38_2)

		if arg_38_0.downloadMgr.IsDownloadState(var_38_3):
			return True

	return False

def var_0_0.DownloadRes(arg_39_0, arg_39_1):
	for iter_39_0, iter_39_1 in ipairs(arg_39_0.displays or {}):
		if arg_39_0.IsDownloading(iter_39_1):
			pg.TipsMgr.GetInstance().ShowTips(i18n("cryptolalia_download_task_already_exists", iter_39_1.GetName()))

			return

	if IsUnityEditor:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_open"))

		return

	local var_39_0 = arg_39_0.displays[arg_39_1]

	originalPrint(var_39_0.IsDownloadableState(arg_39_0.langType))

	if var_39_0 and var_39_0.IsDownloadableState(arg_39_0.langType) and not arg_39_0.downloadReqList[var_39_0.id]:
		originalPrint("Downloading............")
		arg_39_0.OnUpdateForResDownload("Request", var_39_0, arg_39_1)
		arg_39_0.OnItemSelected(arg_39_0.selectedIndex)

def var_0_0.OnUpdateForResDownload(arg_40_0, arg_40_1, arg_40_2, arg_40_3):
	local var_40_0 = arg_40_2.GetCpkName(arg_40_0.langType)
	local var_40_1 = Cryptolalia.BuildCpkPath(var_40_0)
	local var_40_2 = Cryptolalia.BuildSubtitlePath(var_40_0)

	arg_40_0.downloadMgr[arg_40_1](arg_40_0.downloadMgr, {
		var_40_2,
		var_40_1
	}, function(arg_41_0, arg_41_1)
		local var_41_0 = arg_40_0.downloadReqList[arg_40_2.id]

		if not var_41_0 or var_41_0.index != arg_40_0.selectedIndex:
			return

		if arg_41_1 == CryptolaliaDownloadMgr.PROGRESS_FINISH or arg_41_1 == CryptolaliaDownloadMgr.PROGRESS_ERROR:
			arg_40_0.downloadReqList[arg_40_2.id] = None
			arg_40_0.cg.blocksRaycasts = False

			onNextTick(function()
				arg_40_0.OnItemSelected(arg_40_0.selectedIndex)

				arg_40_0.cg.blocksRaycasts = True)

			if arg_41_1 == CryptolaliaDownloadMgr.PROGRESS_FINISH:
				pg.TipsMgr.GetInstance().ShowTips(i18n("cryptolalia_download_done"))
		else
			setSlider(arg_40_0.downloadingBtn, 0, 1, arg_41_1))

	arg_40_0.downloadReqList[arg_40_2.id] = {
		index = arg_40_3
	}

def var_0_0.PlayVedio(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_0.displays[arg_43_1]

	if var_43_0 and var_43_0.IsPlayableState(arg_43_0.langType):
		pg.BgmMgr.GetInstance().StopPlay()

		local var_43_1 = var_43_0.GetCpkName(arg_43_0.langType)
		local var_43_2 = CryptolaliaVedioPlayer.New(arg_43_0._tf)

		var_43_2.Play(var_43_1, function()
			pg.BgmMgr.GetInstance().ContinuePlay())

		arg_43_0.player = var_43_2

def var_0_0.OnUnlockCryptolalia(arg_45_0, arg_45_1):
	for iter_45_0, iter_45_1 in ipairs(arg_45_0.cryptolaliaList):
		if iter_45_1.id == arg_45_1:
			iter_45_1.Unlock()

	for iter_45_2, iter_45_3 in ipairs(arg_45_0.displays):
		if iter_45_3 and iter_45_3.id == arg_45_1:
			iter_45_3.Unlock()

	if not arg_45_0.selectedIndex:
		return

	local var_45_0 = arg_45_0.displays[arg_45_0.selectedIndex]

	if var_45_0 and var_45_0.id == arg_45_1:
		arg_45_0.OnItemSelected(arg_45_0.selectedIndex)

	if arg_45_0.purchaseWindow and arg_45_0.purchaseWindow.GetLoaded() and arg_45_0.purchaseWindow.isShowing():
		arg_45_0.purchaseWindow.Hide()

def var_0_0.onBackPressed(arg_46_0):
	if arg_46_0.purchaseWindow and arg_46_0.purchaseWindow.GetLoaded() and arg_46_0.purchaseWindow.isShowing():
		arg_46_0.purchaseWindow.Hide()

		return

	if arg_46_0.resDeleteWindow and arg_46_0.resDeleteWindow.GetLoaded() and arg_46_0.resDeleteWindow.isShowing():
		arg_46_0.resDeleteWindow.Hide()

		return

	if arg_46_0.listView and arg_46_0.listView.GetLoaded() and arg_46_0.listView.isShowing():
		arg_46_0.listView.Hide()

		return

	var_0_0.super.onBackPressed(arg_46_0)

def var_0_0.willExit(arg_47_0):
	arg_47_0.ClearAuditionTimer()

	if arg_47_0.scrollRect:
		arg_47_0.scrollRect.Dispose()

		arg_47_0.scrollRect = None

	arg_47_0.downloadReqList = None

	if arg_47_0.purchaseWindow:
		arg_47_0.purchaseWindow.Destroy()

		arg_47_0.purchaseWindow = None

	if arg_47_0.resDeleteWindow:
		arg_47_0.resDeleteWindow.Destroy()

		arg_47_0.resDeleteWindow = None

	if arg_47_0.mainView:
		arg_47_0.mainView.Dispose()

		arg_47_0.mainView = None

	if arg_47_0.player:
		arg_47_0.player.Dispose()

		arg_47_0.player = None

	if arg_47_0.downloadMgr:
		arg_47_0.downloadMgr.Dispose()

		arg_47_0.downloadMgr = None

	if arg_47_0.listView:
		arg_47_0.listView.Destroy()

		arg_47_0.listView = None

	arg_47_0.cards = None

	if arg_47_0.soundPlayer:
		arg_47_0.soundPlayer.Dispose()

		arg_47_0.soundPlayer = None

	Input.multiTouchEnabled = True

return var_0_0
