local var_0_0 = class("MangaView", import("..base.BaseSubView"))

var_0_0.MangaGroupName = "MANGA"

def var_0_0.getUIName(arg_1_0):
	return "MangaUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()
	arg_2_0.updateBtnList()
	arg_2_0.Show()
	arg_2_0.updatePanel()
	arg_2_0.tryShowTipMsgBox()

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.resLoader.Clear()
	arg_3_0.stopUpdateEmpty()
	arg_3_0.stopUpdateDownloadBtnPanel()

def var_0_0.onBackPressed(arg_4_0):
	return True

def var_0_0.initData(arg_5_0):
	arg_5_0.appreciateProxy = getProxy(AppreciateProxy)
	arg_5_0.resLoader = AutoLoader.New()
	arg_5_0.isShowNotRead = False
	arg_5_0.isShowLike = False
	arg_5_0.isUpOrder = False
	arg_5_0.group = GroupHelper.GetGroupMgrByName(var_0_0.MangaGroupName)
	arg_5_0.mangaIDListForShow = arg_5_0.getMangaIDListForShow()

def var_0_0.initUI(arg_6_0):
	setLocalPosition(arg_6_0._tf, Vector2.zero)

	arg_6_0._tf.anchorMin = Vector2.zero
	arg_6_0._tf.anchorMax = Vector2.one
	arg_6_0._tf.offsetMax = Vector2.zero
	arg_6_0._tf.offsetMin = Vector2.zero

	local var_6_0 = arg_6_0.findTF("BtnList")

	arg_6_0.likeFilteBtn = arg_6_0.findTF("LikeFilterBtn", var_6_0)
	arg_6_0.readFilteBtn = arg_6_0.findTF("ReadFilteBtn", var_6_0)
	arg_6_0.orderBtn = arg_6_0.findTF("OrderBtn", var_6_0)
	arg_6_0.repairBtn = arg_6_0.findTF("RepairBtn", var_6_0)
	arg_6_0.scrollView = arg_6_0.findTF("ScrollView")
	arg_6_0.emptyPanel = arg_6_0.findTF("EmptyPanel")
	arg_6_0.downloadBtnPanel = arg_6_0.findTF("UpdatePanel")
	arg_6_0.mangaContainer = arg_6_0.findTF("ScrollView/Content")
	arg_6_0.lScrollRectSC = arg_6_0.findTF("ScrollView/Content").GetComponent("LScrollRect")
	arg_6_0.mangaTpl = arg_6_0.findTF("MangaTpl")

	arg_6_0.lScrollRectSC.BeginLayout()
	arg_6_0.lScrollRectSC.EndLayout()
	arg_6_0.initUIText()

def var_0_0.initUIText(arg_7_0):
	local var_7_0 = arg_7_0.findTF("ShowingAll/Text", arg_7_0.readFilteBtn)
	local var_7_1 = arg_7_0.findTF("ShowingNotRead/Text", arg_7_0.readFilteBtn)
	local var_7_2 = arg_7_0.findTF("Content/Bottom/BottomNotRead/Tag/Text", arg_7_0.mangaTpl)
	local var_7_3 = arg_7_0.findTF("Text", arg_7_0.emptyPanel)

	setText(var_7_0, i18n("cartoon_notall"))
	setText(var_7_1, i18n("cartoon_notall"))
	setText(var_7_2, i18n("cartoon_notall"))
	setText(var_7_3, i18n("cartoon_haveno"))

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.likeFilteBtn, function()
		arg_8_0.isShowLike = not arg_8_0.isShowLike
		arg_8_0.mangaIDListForShow = arg_8_0.getMangaIDListForShow()

		arg_8_0.updateBtnList()
		arg_8_0.updatePanel(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.readFilteBtn, function()
		arg_8_0.isShowNotRead = not arg_8_0.isShowNotRead
		arg_8_0.mangaIDListForShow = arg_8_0.getMangaIDListForShow()

		arg_8_0.updateBtnList()
		arg_8_0.updatePanel(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.orderBtn, function()
		arg_8_0.isUpOrder = not arg_8_0.isUpOrder
		arg_8_0.mangaIDListForShow = arg_8_0.getMangaIDListForShow()

		arg_8_0.updateBtnList()
		arg_8_0.updatePanel(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.repairBtn, function()
		local var_12_0 = {
			text = i18n("msgbox_repair"),
			def onCallback:()
				if PathMgr.FileExists(Application.persistentDataPath .. "/hashes-manga.csv"):
					arg_8_0.group.StartVerifyForLua()
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
		}

		if IsUnityEditor:
			PlayerPrefs.SetInt("mangaVersion", 0)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideYes = True,
			content = i18n("resource_verify_warn"),
			custom = {
				var_12_0
			}
		}), SFX_PANEL)

def var_0_0.updateMangaTpl(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = tf(arg_14_2)
	local var_14_1 = arg_14_0.mangaIDListForShow[arg_14_1]

	assert(var_14_1, "null mangaID")

	local var_14_2 = arg_14_0.findTF("Update", var_14_0)

	setActive(var_14_2, False)

	local var_14_3 = arg_14_0.findTF("Content/Mask/Pic", var_14_0)
	local var_14_4 = arg_14_0.findTF("Content/Bottom/BottomNew", var_14_0)
	local var_14_5 = arg_14_0.findTF("Content/Bottom/BottomNotRead", var_14_0)
	local var_14_6 = arg_14_0.findTF("Content/Bottom/BottomNormal", var_14_0)
	local var_14_7 = arg_14_0.findTF("Content/Bottom/BottomTip", var_14_0)
	local var_14_8 = arg_14_0.findTF("TopSpecial", var_14_0)
	local var_14_9 = arg_14_0.findTF("NumText", var_14_4)
	local var_14_10 = arg_14_0.findTF("NumText", var_14_5)
	local var_14_11 = arg_14_0.findTF("NumText", var_14_6)
	local var_14_12 = MangaConst.isMangaEverReadByID(var_14_1)
	local var_14_13 = MangaConst.isMangaNewByID(var_14_1)

	setActive(var_14_7, False)
	setActive(var_14_4, not var_14_12)
	setActive(var_14_5, False)
	setActive(var_14_6, var_14_12)
	setActive(var_14_8, not var_14_12)
	setText(var_14_9, "#" .. pg.cartoon[var_14_1].cartoon_id)
	setText(var_14_10, "#" .. pg.cartoon[var_14_1].cartoon_id)
	setText(var_14_11, "#" .. pg.cartoon[var_14_1].cartoon_id)
	removeOnButton(var_14_0)
	onButton(arg_14_0, var_14_0, function()
		arg_14_0.openMangaViewLayer(arg_14_1), SFX_PANEL)

	local var_14_14 = pg.cartoon[var_14_1].resource
	local var_14_15 = MangaConst.MANGA_PATH_PREFIX .. var_14_14
	local var_14_16 = GetComponent(var_14_3, "Image").sprite

	if not IsNil(var_14_16):
		if var_14_16.name != var_14_14:
			arg_14_0.resLoader.LoadSprite(var_14_15, var_14_14, var_14_3, False)
	else
		arg_14_0.resLoader.LoadSprite(var_14_15, var_14_14, var_14_3, False)

def var_0_0.initEmpty(arg_16_0, arg_16_1):
	local var_16_0 = tf(arg_16_1)
	local var_16_1 = arg_16_0.findTF("TopSpecial", var_16_0)

	setActive(var_16_1, False)

	local var_16_2 = arg_16_0.findTF("Content/Bottom/BottomNew", var_16_0)
	local var_16_3 = arg_16_0.findTF("Content/Bottom/BottomNotRead", var_16_0)
	local var_16_4 = arg_16_0.findTF("Content/Bottom/BottomNormal", var_16_0)
	local var_16_5 = arg_16_0.findTF("Content/Bottom/BottomTip", var_16_0)

	setActive(var_16_2, False)
	setActive(var_16_3, False)
	setActive(var_16_4, False)
	setActive(var_16_5, True)

	local var_16_6 = arg_16_0.findTF("Update", var_16_0)
	local var_16_7 = arg_16_0.findTF("Btn", var_16_6)
	local var_16_8 = arg_16_0.findTF("Progress", var_16_6)
	local var_16_9 = arg_16_0.findTF("Slider", var_16_8)

	setActive(var_16_6, True)
	setActive(var_16_7, True)
	setActive(var_16_8, False)

	local var_16_10
	local var_16_11

	for iter_16_0, iter_16_1 in ipairs(pg.cartoon.all):
		local var_16_12 = pg.cartoon[iter_16_1].resource
		local var_16_13 = MangaConst.MANGA_PATH_PREFIX .. var_16_12

		if checkABExist(var_16_13):
			var_16_10 = var_16_12
			var_16_11 = var_16_13

			break

	local var_16_14 = arg_16_0.findTF("Content/Mask/Pic", var_16_0)

	arg_16_0.resLoader.LoadSprite(var_16_11, var_16_10, var_16_14, False)
	setText(arg_16_0.findTF("Text", var_16_5), "")
	onButton(arg_16_0, var_16_7, function()
		local var_17_0 = arg_16_0.group.state

		if var_17_0 == DownloadState.None or var_17_0 == DownloadState.CheckFailure:
			arg_16_0.group.CheckD()
		elif var_17_0 == DownloadState.CheckToUpdate or var_17_0 == DownloadState.UpdateFailure:
			local var_17_1 = GroupHelper.GetGroupSize(var_0_0.MangaGroupName)
			local var_17_2 = HashUtil.BytesToString(var_17_1)

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_NORMAL,
				content = string.format(i18n("group_download_tip", var_17_2)),
				def onYes:()
					arg_16_0.group.UpdateD()
			}), SFX_PANEL)
	arg_16_0.startUpdateEmpty(arg_16_1)

def var_0_0.updateEmpty(arg_19_0, arg_19_1):
	local var_19_0 = tf(arg_19_1)
	local var_19_1 = arg_19_0.findTF("Update", var_19_0)
	local var_19_2 = arg_19_0.findTF("Btn", var_19_1)
	local var_19_3 = arg_19_0.findTF("Text", var_19_2)
	local var_19_4 = arg_19_0.findTF("Progress", var_19_1)
	local var_19_5 = arg_19_0.findTF("Slider", var_19_4)
	local var_19_6 = arg_19_0.group.state

	if var_19_6 == DownloadState.None:
		setText(var_19_3, "None")
		setActive(var_19_2, True)
		setActive(var_19_4, False)
	elif var_19_6 == DownloadState.Checking:
		setText(var_19_3, i18n("word_manga_checking"))
		setActive(var_19_2, True)
		setActive(var_19_4, False)
	elif var_19_6 == DownloadState.CheckToUpdate:
		setText(var_19_3, i18n("word_manga_checktoupdate"))
		setActive(var_19_2, True)
		setActive(var_19_4, False)
	elif var_19_6 == DownloadState.CheckOver:
		setText(var_19_3, "Latest Ver")
		setActive(var_19_2, True)
		setActive(var_19_4, False)
	elif var_19_6 == DownloadState.CheckFailure:
		setText(var_19_3, i18n("word_manga_checkfailure"))
		setActive(var_19_2, True)
		setActive(var_19_4, False)
	elif var_19_6 == DownloadState.Updating:
		setText(var_19_3, i18n("word_manga_updating", arg_19_0.group.downloadCount, arg_19_0.group.downloadTotal))
		setActive(var_19_2, False)
		setActive(var_19_4, True)
		setSlider(var_19_5, 0, arg_19_0.group.downloadTotal, arg_19_0.group.downloadCount)
	elif var_19_6 == DownloadState.UpdateSuccess:
		setText(var_19_3, i18n("word_manga_updatesuccess"))
		setActive(var_19_2, True)
		setActive(var_19_4, False)

		arg_19_0.mangaIDListForShow = arg_19_0.getMangaIDListForShow()

		arg_19_0.updatePanel()
	elif var_19_6 == DownloadState.UpdateFailure:
		setText(var_19_3, i18n("word_manga_updatefailure"))
		setActive(var_19_2, True)
		setActive(var_19_4, False)

def var_0_0.startUpdateEmpty(arg_20_0, arg_20_1):
	if arg_20_0.timer:
		arg_20_0.timer.Stop()

	arg_20_0.timer = Timer.New(function()
		arg_20_0.updateEmpty(arg_20_1), 0.5, -1)

	arg_20_0.timer.Start()
	arg_20_0.updateEmpty(arg_20_1)

def var_0_0.stopUpdateEmpty(arg_22_0, arg_22_1):
	if arg_22_0.timer:
		arg_22_0.timer.Stop()

def var_0_0.updateMangaList(arg_23_0):
	arg_23_0.resLoader.Clear()

	function arg_23_0.lScrollRectSC.onReturnItem(arg_24_0, arg_24_1)
		arg_24_0 = arg_24_0 + 1

		if arg_23_0.mangaIDListForShow[arg_24_0] == False:
			arg_23_0.stopUpdateEmpty(arg_24_1)

	function arg_23_0.lScrollRectSC.onUpdateItem(arg_25_0, arg_25_1)
		arg_25_0 = arg_25_0 + 1

		if arg_23_0.mangaIDListForShow[arg_25_0] == False:
			arg_23_0.initEmpty(arg_25_1)
			arg_23_0.updateEmpty(arg_25_1)
		else
			arg_23_0.updateMangaTpl(arg_25_0, arg_25_1)

	arg_23_0.lScrollRectSC.SetTotalCount(#arg_23_0.mangaIDListForShow)

def var_0_0.initDownloadBtnPanel(arg_26_0):
	local var_26_0 = arg_26_0.findTF("Btn", arg_26_0.downloadBtnPanel)
	local var_26_1 = arg_26_0.findTF("Text", var_26_0)
	local var_26_2 = arg_26_0.findTF("Progress", arg_26_0.downloadBtnPanel)
	local var_26_3 = arg_26_0.findTF("Slider", var_26_2)

	setActive(var_26_0, True)
	setActive(var_26_2, False)
	onButton(arg_26_0, var_26_0, function()
		local var_27_0 = arg_26_0.group.state

		if var_27_0 == DownloadState.None or var_27_0 == DownloadState.CheckFailure:
			arg_26_0.group.CheckD()
		elif var_27_0 == DownloadState.CheckToUpdate or var_27_0 == DownloadState.UpdateFailure:
			local var_27_1 = GroupHelper.GetGroupSize(var_0_0.MangaGroupName)
			local var_27_2 = HashUtil.BytesToString(var_27_1)

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_NORMAL,
				content = string.format(i18n("group_download_tip", var_27_2)),
				def onYes:()
					arg_26_0.group.UpdateD()
			}), SFX_PANEL)
	arg_26_0.startUpdateDownloadBtnPanel()

def var_0_0.updateDownloadBtnPanel(arg_29_0):
	local var_29_0 = arg_29_0.findTF("Btn", arg_29_0.downloadBtnPanel)
	local var_29_1 = arg_29_0.findTF("Text", var_29_0)
	local var_29_2 = arg_29_0.findTF("Progress", arg_29_0.downloadBtnPanel)
	local var_29_3 = arg_29_0.findTF("Slider", var_29_2)
	local var_29_4 = arg_29_0.group.state

	if var_29_4 == DownloadState.None:
		setText(var_29_1, "None")
		setActive(var_29_0, True)
		setActive(var_29_2, False)
	elif var_29_4 == DownloadState.Checking:
		setText(var_29_1, i18n("word_manga_checking"))
		setActive(var_29_0, True)
		setActive(var_29_2, False)
	elif var_29_4 == DownloadState.CheckToUpdate:
		setText(var_29_1, i18n("word_manga_checktoupdate"))
		setActive(var_29_0, True)
		setActive(var_29_2, False)
	elif var_29_4 == DownloadState.CheckOver:
		setText(var_29_1, "Latest Ver")
		setActive(var_29_0, True)
		setActive(var_29_2, False)
	elif var_29_4 == DownloadState.CheckFailure:
		setText(var_29_1, i18n("word_manga_checkfailure"))
		setActive(var_29_0, True)
		setActive(var_29_2, False)
	elif var_29_4 == DownloadState.Updating:
		setText(var_29_1, i18n("word_manga_updating", arg_29_0.group.downloadCount, arg_29_0.group.downloadTotal))
		setActive(var_29_0, False)
		setActive(var_29_2, True)
		setSlider(var_29_3, 0, arg_29_0.group.downloadTotal, arg_29_0.group.downloadCount)
	elif var_29_4 == DownloadState.UpdateSuccess:
		setText(var_29_1, i18n("word_manga_updatesuccess"))
		setActive(var_29_0, True)
		setActive(var_29_2, False)

		arg_29_0.mangaIDListForShow = arg_29_0.getMangaIDListForShow()

		arg_29_0.updatePanel()
	elif var_29_4 == DownloadState.UpdateFailure:
		setText(var_29_1, i18n("word_manga_updatefailure"))
		setActive(var_29_0, True)
		setActive(var_29_2, False)

def var_0_0.startUpdateDownloadBtnPanel(arg_30_0):
	if arg_30_0.timer:
		arg_30_0.timer.Stop()

	arg_30_0.timer = Timer.New(function()
		arg_30_0.updateDownloadBtnPanel(), 0.5, -1)

	arg_30_0.timer.Start()
	arg_30_0.updateDownloadBtnPanel()

def var_0_0.stopUpdateDownloadBtnPanel(arg_32_0):
	if arg_32_0.timer:
		arg_32_0.timer.Stop()

def var_0_0.updatePanel(arg_33_0):
	local var_33_0 = #arg_33_0.mangaIDListForShow <= 0
	local var_33_1 = #arg_33_0.mangaIDListForShow == 1 and arg_33_0.mangaIDListForShow[1] == False

	setActive(arg_33_0.emptyPanel, var_33_0)
	setActive(arg_33_0.downloadBtnPanel, var_33_1)
	setActive(arg_33_0.scrollView, not var_33_0 and not var_33_1)
	arg_33_0.stopUpdateEmpty()
	arg_33_0.stopUpdateDownloadBtnPanel()

	if not var_33_0 and not var_33_1:
		arg_33_0.updateMangaList()
	elif var_33_1:
		arg_33_0.initDownloadBtnPanel()

def var_0_0.updateBtnList(arg_34_0):
	local var_34_0 = arg_34_0.findTF("On", arg_34_0.likeFilteBtn)

	setActive(var_34_0, arg_34_0.isShowLike)

	local var_34_1 = arg_34_0.findTF("ShowingAll", arg_34_0.readFilteBtn)
	local var_34_2 = arg_34_0.findTF("ShowingNotRead", arg_34_0.readFilteBtn)

	setActive(var_34_1, not arg_34_0.isShowNotRead)
	setActive(var_34_2, arg_34_0.isShowNotRead)

	local var_34_3 = arg_34_0.findTF("Up", arg_34_0.orderBtn)
	local var_34_4 = arg_34_0.findTF("Down", arg_34_0.orderBtn)

	setActive(var_34_3, arg_34_0.isUpOrder)
	setActive(var_34_4, not arg_34_0.isUpOrder)

def var_0_0.tryShowTipMsgBox(arg_35_0):
	if arg_35_0.appreciateProxy.isMangaHaveNewRes():
		local function var_35_0()
			PlayerPrefs.SetInt("mangaVersion", MangaConst.Version)
			arg_35_0.emit(CollectionScene.UPDATE_RED_POINT)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideClose = True,
			hideNo = True,
			content = i18n("res_cartoon_new_tip", MangaConst.NewCount),
			onYes = var_35_0,
			onCancel = var_35_0,
			onClose = var_35_0
		})

def var_0_0.openMangaViewLayer(arg_37_0, arg_37_1):
	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = MangaFullScreenMediator,
		viewComponent = MangaFullScreenLayer,
		data = {
			mangaIndex = arg_37_1,
			mangaIDLIst = arg_37_0.mangaIDListForShow,
			mangaContext = arg_37_0,
			isShowingNotRead = isActive(arg_37_0.findTF("ShowingNotRead", arg_37_0.readFilteBtn))
		},
		def onRemoved:()
			return
	}))

def var_0_0.updateLineAfterRead(arg_39_0, arg_39_1):
	local var_39_0 = table.indexof(arg_39_0.mangaIDListForShow, arg_39_1) - 1
	local var_39_1 = arg_39_0.findTF(tostring(var_39_0), arg_39_0.mangaContainer)

	if var_39_1:
		local var_39_2 = arg_39_0.findTF("Content/Bottom/BottomNew", var_39_1)
		local var_39_3 = arg_39_0.findTF("Content/Bottom/BottomNotRead", var_39_1)
		local var_39_4 = arg_39_0.findTF("Content/Bottom/BottomNormal", var_39_1)
		local var_39_5 = arg_39_0.findTF("TopSpecial", var_39_1)
		local var_39_6 = MangaConst.isMangaEverReadByID(arg_39_1)
		local var_39_7 = MangaConst.isMangaNewByID(arg_39_1)

		setActive(var_39_2, var_39_7 and not var_39_6)
		setActive(var_39_3, not var_39_7 and not var_39_6)
		setActive(var_39_4, var_39_6)
		setActive(var_39_5, not var_39_6)

def var_0_0.updateToMangaID(arg_40_0, arg_40_1):
	local var_40_0 = table.indexof(arg_40_0.mangaIDListForShow, arg_40_1) - 1
	local var_40_1 = arg_40_0.lScrollRectSC.HeadIndexToValue(var_40_0)

	arg_40_0.lScrollRectSC.SetTotalCount(#arg_40_0.mangaIDListForShow, defaultValue(var_40_1, -1))

def var_0_0.getMangaIDListForShow(arg_41_0, arg_41_1):
	local var_41_0 = {}

	for iter_41_0, iter_41_1 in ipairs(pg.cartoon.all):
		if arg_41_0.isMangaExist(iter_41_1):
			local var_41_1 = MangaConst.isMangaEverReadByID(iter_41_1)
			local var_41_2 = MangaConst.isMangaLikeByID(iter_41_1)

			if arg_41_0.isShowNotRead and arg_41_0.isShowLike:
				if not var_41_1 and var_41_2:
					table.insert(var_41_0, iter_41_1)
			elif arg_41_0.isShowNotRead and not arg_41_0.isShowLike:
				if not var_41_1:
					table.insert(var_41_0, iter_41_1)
			elif not arg_41_0.isShowNotRead and arg_41_0.isShowLike:
				if var_41_2:
					table.insert(var_41_0, iter_41_1)
			else
				table.insert(var_41_0, iter_41_1)

	local function var_41_3(arg_42_0, arg_42_1)
		local var_42_0 = pg.cartoon[arg_42_0]
		local var_42_1 = pg.cartoon[arg_42_1]
		local var_42_2 = var_42_0.cartoon_id
		local var_42_3 = var_42_1.cartoon_id

		if var_42_3 < var_42_2:
			return not arg_41_0.isUpOrder
		elif var_42_2 == var_42_3:
			return arg_42_0 < arg_42_1
		elif var_42_2 < var_42_3:
			return arg_41_0.isUpOrder

	table.sort(var_41_0, var_41_3)

	if arg_41_0.isNeedShowDownBtn():
		table.insert(var_41_0, 1, False)

	return var_41_0

def var_0_0.isMangaExist(arg_43_0, arg_43_1):
	local var_43_0 = MangaConst.MANGA_PATH_PREFIX .. arg_43_1
	local var_43_1 = arg_43_0.group.CheckF(var_43_0)

	return var_43_1 == DownloadState.None or var_43_1 == DownloadState.UpdateSuccess

def var_0_0.isNeedShowDownBtn(arg_44_0):
	if Application.isEditor:
		return False

	if GroupHelper.IsGroupVerLastest(var_0_0.MangaGroupName):
		return False

	if not GroupHelper.IsGroupWaitToUpdate(var_0_0.MangaGroupName):
		return False

	return True

return var_0_0
