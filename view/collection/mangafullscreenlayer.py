local var_0_0 = class("MangaFullScreenLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MangaViewUI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)
	arg_3_0.readManga()
	arg_3_0.updatePicImg()
	arg_3_0.updateLikeBtn()

def var_0_0.willExit(arg_4_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf)
	arg_4_0.resLoader.Clear()

	if arg_4_0.contextData.mangaContext:
		local var_4_0 = arg_4_0.mangaIDLIst[arg_4_0.curMangaIndex]

		arg_4_0.contextData.mangaContext.updateToMangaID(var_4_0)

def var_0_0.onBackPressed(arg_5_0):
	if not arg_5_0.isShowing:
		arg_5_0.closeView()

def var_0_0.findUI(arg_6_0):
	arg_6_0.bg = arg_6_0.findTF("BG")
	arg_6_0.picImg = arg_6_0.findTF("Manga/Pic")
	arg_6_0.indexText = arg_6_0.findTF("Manga/Index")
	arg_6_0.preBtn = arg_6_0.findTF("LeftBtn")
	arg_6_0.rightBtn = arg_6_0.findTF("RightBtn")
	arg_6_0.tipText = arg_6_0.findTF("Tip")
	arg_6_0.likeOnBtn = arg_6_0.findTF("Manga/LikeOn")
	arg_6_0.likeOffBtn = arg_6_0.findTF("Manga/LikeOff")

	setText(arg_6_0.tipText, i18n("world_collection_back"))

def var_0_0.initData(arg_7_0):
	arg_7_0.resLoader = AutoLoader.New()
	arg_7_0.curMangaIndex = arg_7_0.contextData.mangaIndex
	arg_7_0.mangaIDLIst = arg_7_0.contextData.mangaIDLIst

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.bg, function()
		if not arg_8_0.isShowing:
			arg_8_0.closeView(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.preBtn, function()
		if arg_8_0.curMangaIndex > 1:
			arg_8_0.curMangaIndex = arg_8_0.curMangaIndex - 1

			arg_8_0.readManga()
			arg_8_0.updatePicImg()
			arg_8_0.updateLikeBtn(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.rightBtn, function()
		if arg_8_0.curMangaIndex < #arg_8_0.mangaIDLIst:
			arg_8_0.curMangaIndex = arg_8_0.curMangaIndex + 1

			arg_8_0.readManga()
			arg_8_0.updatePicImg()
			arg_8_0.updateLikeBtn(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.likeOnBtn, function()
		local var_12_0 = arg_8_0.mangaIDLIst[arg_8_0.curMangaIndex]

		pg.m02.sendNotification(GAME.APPRECIATE_MANGA_LIKE, {
			mangaID = var_12_0,
			action = MangaConst.CANCEL_MANGA_LIKE
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.likeOffBtn, function()
		local var_13_0 = arg_8_0.mangaIDLIst[arg_8_0.curMangaIndex]

		pg.m02.sendNotification(GAME.APPRECIATE_MANGA_LIKE, {
			mangaID = var_13_0,
			action = MangaConst.SET_MANGA_LIKE
		}), SFX_PANEL)
	addSlip(SLIP_TYPE_HRZ, arg_8_0.picImg, function()
		triggerButton(arg_8_0.preBtn), function()
		triggerButton(arg_8_0.rightBtn))
	addSlip(SLIP_TYPE_HRZ, arg_8_0.bg, function()
		triggerButton(arg_8_0.preBtn), function()
		triggerButton(arg_8_0.rightBtn))

def var_0_0.updatePicImg(arg_18_0):
	local var_18_0 = arg_18_0.mangaIDLIst[arg_18_0.curMangaIndex]
	local var_18_1 = pg.cartoon[var_18_0].resource
	local var_18_2 = MangaConst.MANGA_PATH_PREFIX .. var_18_1

	arg_18_0.resLoader.LoadSprite(var_18_2, var_18_1, arg_18_0.picImg, False)

	local var_18_3

	if arg_18_0.contextData.isShowingNotRead:
		var_18_3 = "#" .. pg.cartoon[var_18_0].cartoon_id
	else
		var_18_3 = "#" .. pg.cartoon[var_18_0].cartoon_id .. "/" .. #arg_18_0.mangaIDLIst

	setText(arg_18_0.indexText, var_18_3)

	arg_18_0.isShowing = True

	arg_18_0.managedTween(LeanTween.value, None, go(arg_18_0.picImg), 0, 1, 0.3).setOnUpdate(System.Action_float(function(arg_19_0)
		setImageAlpha(arg_18_0.picImg, arg_19_0))).setOnComplete(System.Action(function()
		arg_18_0.isShowing = False

		setImageAlpha(arg_18_0.picImg, 1)))
	setActive(arg_18_0.preBtn, arg_18_0.curMangaIndex > 1)
	setActive(arg_18_0.rightBtn, arg_18_0.curMangaIndex < #arg_18_0.mangaIDLIst)

def var_0_0.updateLikeBtn(arg_21_0):
	local var_21_0 = arg_21_0.mangaIDLIst[arg_21_0.curMangaIndex]
	local var_21_1 = MangaConst.isMangaLikeByID(var_21_0)

	setActive(arg_21_0.likeOnBtn, var_21_1)
	setActive(arg_21_0.likeOffBtn, not var_21_1)

def var_0_0.readManga(arg_22_0):
	local var_22_0 = arg_22_0.mangaIDLIst[arg_22_0.curMangaIndex]

	if not MangaConst.isMangaEverReadByID(var_22_0):
		pg.m02.sendNotification(GAME.APPRECIATE_MANGA_READ, {
			mangaID = var_22_0
		})

return var_0_0
