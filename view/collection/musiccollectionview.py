local var_0_0 = class("MusicCollectionView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "MusicCollectionUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()
	arg_2_0.initPlateListPanel()
	arg_2_0.initSongListPanel()
	arg_2_0.Show()
	arg_2_0.recoverRunData()
	arg_2_0.initTimer()
	arg_2_0.tryShowTipMsgBox()

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.stopMusic()
	arg_3_0.resLoader.Clear()

	if arg_3_0.playProgressTimer:
		arg_3_0.playProgressTimer.Stop()

		arg_3_0.playProgressTimer = None

	if arg_3_0.downloadCheckTimer:
		arg_3_0.downloadCheckTimer.Stop()

		arg_3_0.downloadCheckTimer = None

	if arg_3_0.playbackInfo:
		arg_3_0.playbackInfo = None

	if arg_3_0.appreciateUnlockMsgBox and arg_3_0.appreciateUnlockMsgBox.CheckState(BaseSubView.STATES.INITED):
		arg_3_0.appreciateUnlockMsgBox.Destroy()

	arg_3_0.closeSongListPanel(True)

def var_0_0.onBackPressed(arg_4_0):
	if arg_4_0.appreciateUnlockMsgBox and arg_4_0.appreciateUnlockMsgBox.CheckState(BaseSubView.STATES.INITED):
		arg_4_0.appreciateUnlockMsgBox.hideCustomMsgBox()
		arg_4_0.appreciateUnlockMsgBox.Destroy()

		return False
	elif isActive(arg_4_0.songListPanel):
		arg_4_0.closeSongListPanel()

		return False
	else
		return True

def var_0_0.initData(arg_5_0):
	arg_5_0.appreciateProxy = getProxy(AppreciateProxy)

	arg_5_0.appreciateProxy.checkMusicFileState()

	arg_5_0.resLoader = AutoLoader.New()
	arg_5_0.criMgr = pg.CriMgr.GetInstance()
	arg_5_0.manager = BundleWizard.Inst.GetGroupMgr("GALLERY_BGM")
	arg_5_0.downloadCheckIDList = {}
	arg_5_0.downloadCheckTimer = None
	arg_5_0.musicForShowConfigList = {}
	arg_5_0.plateTFList = {}
	arg_5_0.songTFList = {}
	arg_5_0.curMidddleIndex = 1
	arg_5_0.sortValue = MusicCollectionConst.Sort_Order_Up
	arg_5_0.likeValue = MusicCollectionConst.Filte_Normal_Value
	arg_5_0.isPlayingAni = False
	arg_5_0.cueData = None
	arg_5_0.playbackInfo = None
	arg_5_0.playProgressTimer = None
	arg_5_0.onDrag = False
	arg_5_0.hadDrag = False
	arg_5_0.isPlayingSong = False

def var_0_0.saveRunData(arg_6_0):
	arg_6_0.appreciateProxy.updateMusicRunData(arg_6_0.sortValue, arg_6_0.curMidddleIndex, arg_6_0.likeValue)

def var_0_0.recoverRunData(arg_7_0):
	local var_7_0 = arg_7_0.appreciateProxy.getMusicRunData()

	arg_7_0.sortValue = var_7_0.sortValue
	arg_7_0.curMidddleIndex = var_7_0.middleIndex
	arg_7_0.likeValue = var_7_0.likeValue
	arg_7_0.musicForShowConfigList = arg_7_0.fliteMusicConfigForShow()

	arg_7_0.sortMusicConfigList(arg_7_0.sortValue == MusicCollectionConst.Sort_Order_Down)

	arg_7_0.musicForShowConfigList = arg_7_0.filteMusicConfigByLike()
	arg_7_0.lScrollPageSC.MiddleIndexOnInit = arg_7_0.curMidddleIndex - 1

	arg_7_0.updatePlateListPanel()
	arg_7_0.updateSongListPanel()
	arg_7_0.updatePlayPanel()
	arg_7_0.updateSortToggle()
	arg_7_0.updateLikeToggle()

	if not arg_7_0.appreciateProxy.isMusicHaveNewRes():
		arg_7_0.tryPlayMusic()

def var_0_0.findUI(arg_8_0):
	setLocalPosition(arg_8_0._tf, Vector2.zero)

	arg_8_0._tf.anchorMin = Vector2.zero
	arg_8_0._tf.anchorMax = Vector2.one
	arg_8_0._tf.offsetMax = Vector2.zero
	arg_8_0._tf.offsetMin = Vector2.zero
	arg_8_0.topPanel = arg_8_0.findTF("TopPanel")
	arg_8_0.likeFilteToggle = arg_8_0.findTF("LikeBtn", arg_8_0.topPanel)
	arg_8_0.sortToggle = arg_8_0.findTF("SortBtn", arg_8_0.topPanel)
	arg_8_0.songNameText = arg_8_0.findTF("MusicNameMask/MusicName", arg_8_0.topPanel)
	arg_8_0.staicImg = arg_8_0.findTF("SoundImg", arg_8_0.topPanel)
	arg_8_0.playingAni = arg_8_0.findTF("SoundAni", arg_8_0.topPanel)
	arg_8_0.resRepaireBtn = arg_8_0.findTF("RepaireBtn", arg_8_0.topPanel)

	setActive(arg_8_0.likeFilteToggle, True)

	arg_8_0.plateListPanel = arg_8_0.findTF("PlateList")
	arg_8_0.plateTpl = arg_8_0.findTF("Plate", arg_8_0.plateListPanel)
	arg_8_0.lScrollPageSC = GetComponent(arg_8_0.plateListPanel, "LScrollPage")
	arg_8_0.playPanel = arg_8_0.findTF("PLayPanel")
	arg_8_0.playPanelNameText = arg_8_0.findTF("NameText", arg_8_0.playPanel)
	arg_8_0.likeToggle = arg_8_0.findTF("LikeBtn", arg_8_0.playPanel)
	arg_8_0.songImg = arg_8_0.findTF("SongImg", arg_8_0.playPanel)
	arg_8_0.pauseBtn = arg_8_0.findTF("PlayingBtn", arg_8_0.playPanel)
	arg_8_0.playBtn = arg_8_0.findTF("StopingBtn", arg_8_0.playPanel)
	arg_8_0.lockImg = arg_8_0.findTF("LockedBtn", arg_8_0.playPanel)
	arg_8_0.nextBtn = arg_8_0.findTF("NextBtn", arg_8_0.playPanel)
	arg_8_0.preBtn = arg_8_0.findTF("PreBtn", arg_8_0.playPanel)
	arg_8_0.playProgressBar = arg_8_0.findTF("Progress", arg_8_0.playPanel)
	arg_8_0.nowTimeText = arg_8_0.findTF("NowTimeText", arg_8_0.playProgressBar)
	arg_8_0.totalTimeText = arg_8_0.findTF("TotalTimeText", arg_8_0.playProgressBar)
	arg_8_0.playSliderSC = GetComponent(arg_8_0.playProgressBar, "LSlider")
	arg_8_0.listBtn = arg_8_0.findTF("ListBtn", arg_8_0.playPanel)

	setActive(arg_8_0.likeToggle, True)

	arg_8_0.songListPanel = arg_8_0.findTF("SongListPanel")
	arg_8_0.closeBtn = arg_8_0.findTF("BG", arg_8_0.songListPanel)
	arg_8_0.panel = arg_8_0.findTF("Panel", arg_8_0.songListPanel)
	arg_8_0.songContainer = arg_8_0.findTF("Container/Viewport/Content", arg_8_0.panel)
	arg_8_0.songTpl = arg_8_0.findTF("SongTpl", arg_8_0.panel)
	arg_8_0.upToggle = arg_8_0.findTF("BG2/UpToggle", arg_8_0.panel)
	arg_8_0.downToggle = arg_8_0.findTF("BG2/DownToggle", arg_8_0.panel)
	arg_8_0.songUIItemList = UIItemList.New(arg_8_0.songContainer, arg_8_0.songTpl)
	arg_8_0.emptyPanel = arg_8_0.findTF("EmptyPanel")
	arg_8_0.upImg1 = arg_8_0.findTF("Up", arg_8_0.sortToggle)
	arg_8_0.downImg1 = arg_8_0.findTF("Down", arg_8_0.sortToggle)
	arg_8_0.upImg2 = arg_8_0.findTF("SelImg", arg_8_0.upToggle)
	arg_8_0.downImg2 = arg_8_0.findTF("SelImg", arg_8_0.downToggle)
	arg_8_0.likeFilteOffImg = arg_8_0.findTF("Off", arg_8_0.likeFilteToggle)
	arg_8_0.likeFilteOnImg = arg_8_0.findTF("On", arg_8_0.likeFilteToggle)
	arg_8_0.likeOffImg = arg_8_0.findTF("Off", arg_8_0.likeToggle)
	arg_8_0.likeOnImg = arg_8_0.findTF("On", arg_8_0.likeToggle)

def var_0_0.addListener(arg_9_0):
	onButton(arg_9_0, arg_9_0.listBtn, function()
		arg_9_0.openSongListPanel(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.closeBtn, function()
		arg_9_0.closeSongListPanel(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.resRepaireBtn, function()
		local var_12_0 = {
			text = i18n("msgbox_repair"),
			def onCallback:()
				if PathMgr.FileExists(Application.persistentDataPath .. "/hashes-bgm.csv"):
					BundleWizard.Inst.GetGroupMgr("GALLERY_BGM").StartVerifyForLua()
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
		}

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideYes = True,
			content = i18n("resource_verify_warn"),
			custom = {
				var_12_0
			}
		}), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.sortToggle, function()
		arg_9_0.sortValue = arg_9_0.sortValue == MusicCollectionConst.Sort_Order_Up and MusicCollectionConst.Sort_Order_Down or MusicCollectionConst.Sort_Order_Up

		arg_9_0.saveRunData()
		arg_9_0.sortAndUpdate(arg_9_0.sortValue == MusicCollectionConst.Sort_Order_Down), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.upToggle, function()
		if arg_9_0.sortValue == MusicCollectionConst.Sort_Order_Up:
			return
		else
			arg_9_0.sortValue = MusicCollectionConst.Sort_Order_Up

			arg_9_0.saveRunData()
			arg_9_0.sortAndUpdate(False), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.downToggle, function()
		if arg_9_0.sortValue == MusicCollectionConst.Sort_Order_Down:
			return
		else
			arg_9_0.sortValue = MusicCollectionConst.Sort_Order_Down

			arg_9_0.saveRunData()
			arg_9_0.sortAndUpdate(True), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.likeFilteToggle, function()
		arg_9_0.likeValue = arg_9_0.likeValue == MusicCollectionConst.Filte_Normal_Value and MusicCollectionConst.Filte_Like_Value or MusicCollectionConst.Filte_Normal_Value

		arg_9_0.saveRunData()
		arg_9_0.sortAndUpdate(arg_9_0.sortValue == MusicCollectionConst.Sort_Order_Down), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.playBtn, function()
		if not arg_9_0.playbackInfo:
			arg_9_0.playMusic()
		elif arg_9_0.hadDrag:
			arg_9_0.hadDrag = False

			arg_9_0.playbackInfo.SetStartTimeAndPlay(arg_9_0.playSliderSC.value)
			arg_9_0.playProgressTimer.Start()
		else
			arg_9_0.playbackInfo.playback.Resume(CriAtomEx.ResumeMode.PausedPlayback)

		setActive(arg_9_0.playingAni, True)
		setActive(arg_9_0.staicImg, False)
		SetActive(arg_9_0.pauseBtn, True)
		SetActive(arg_9_0.playBtn, False), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.pauseBtn, function()
		if arg_9_0.playbackInfo:
			arg_9_0.playbackInfo.playback.Pause()

		setActive(arg_9_0.playingAni, False)
		setActive(arg_9_0.staicImg, True)
		SetActive(arg_9_0.pauseBtn, False)
		SetActive(arg_9_0.playBtn, True), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.preBtn, function()
		if arg_9_0.curMidddleIndex == 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("res_music_no_pre_tip"))
		elif not arg_9_0.isPlayingAni:
			arg_9_0.setAniState(True)
			arg_9_0.closePlateAni(arg_9_0.plateTFList[arg_9_0.curMidddleIndex])
			arg_9_0.lScrollPageSC.MoveToItemID(arg_9_0.curMidddleIndex - 1 - 1), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.nextBtn, function()
		if arg_9_0.curMidddleIndex == #arg_9_0.musicForShowConfigList:
			pg.TipsMgr.GetInstance().ShowTips(i18n("res_music_no_next_tip"))
		elif not arg_9_0.isPlayingAni:
			arg_9_0.setAniState(True)
			arg_9_0.closePlateAni(arg_9_0.plateTFList[arg_9_0.curMidddleIndex])
			arg_9_0.lScrollPageSC.MoveToItemID(arg_9_0.curMidddleIndex + 1 - 1), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.likeToggle, function()
		local var_22_0 = arg_9_0.getMusicConfigForShowByIndex(arg_9_0.curMidddleIndex).id

		if arg_9_0.appreciateProxy.isLikedByMusicID(var_22_0) == True:
			pg.m02.sendNotification(GAME.APPRECIATE_MUSIC_LIKE, {
				isAdd = 1,
				musicID = var_22_0
			})
			setActive(arg_9_0.likeOnImg, False)
			arg_9_0.updateSongTFLikeImg(arg_9_0.songTFList[arg_9_0.curMidddleIndex], False)
		else
			pg.m02.sendNotification(GAME.APPRECIATE_MUSIC_LIKE, {
				isAdd = 0,
				musicID = var_22_0
			})
			setActive(arg_9_0.likeOnImg, True)
			arg_9_0.updateSongTFLikeImg(arg_9_0.songTFList[arg_9_0.curMidddleIndex], True), SFX_PANEL)
	arg_9_0.playSliderSC.AddPointDownFunc(function(arg_23_0)
		if arg_9_0.playbackInfo and not arg_9_0.onDrag:
			arg_9_0.onDrag = True

			if arg_9_0.playbackInfo.playback.IsPaused():
				-- block empty
			else
				arg_9_0.playbackInfo.playback.Stop(True)

			arg_9_0.playProgressTimer.Stop())
	arg_9_0.playSliderSC.AddPointUpFunc(function(arg_24_0)
		if arg_9_0.playbackInfo and arg_9_0.onDrag:
			arg_9_0.onDrag = False

			if arg_9_0.playbackInfo.playback.IsPaused():
				arg_9_0.hadDrag = True
			else
				arg_9_0.playbackInfo.SetStartTimeAndPlay(arg_9_0.playSliderSC.value)
				arg_9_0.playProgressTimer.Start()
		else
			arg_9_0.playSliderSC.SetValueWithoutEvent(0))

def var_0_0.tryShowTipMsgBox(arg_25_0):
	if arg_25_0.appreciateProxy.isMusicHaveNewRes():
		local function var_25_0()
			arg_25_0.lScrollPageSC.MoveToItemID(MusicCollectionConst.AutoScrollIndex - 1)
			PlayerPrefs.SetInt("musicVersion", MusicCollectionConst.Version)
			arg_25_0.emit(CollectionScene.UPDATE_RED_POINT)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideClose = True,
			hideNo = True,
			content = i18n("res_music_new_tip", MusicCollectionConst.NewCount),
			onYes = var_25_0,
			onCancel = var_25_0,
			onClose = var_25_0
		})

def var_0_0.initPlateListPanel(arg_27_0):
	function arg_27_0.lScrollPageSC.itemInitedCallback(arg_28_0, arg_28_1)
		local var_28_0 = arg_28_0 + 1

		arg_27_0.plateTFList[var_28_0] = arg_28_1

		arg_27_0.updatePlateTF(arg_28_1, arg_28_0)

	function arg_27_0.lScrollPageSC.itemClickCallback(arg_29_0, arg_29_1)
		local var_29_0 = arg_29_0 + 1

		if arg_27_0.curMidddleIndex != var_29_0 and not arg_27_0.isPlayingAni:
			arg_27_0.setAniState(True)
			arg_27_0.closePlateAni(arg_27_0.plateTFList[arg_27_0.curMidddleIndex])
			arg_27_0.lScrollPageSC.MoveToItemID(arg_29_0)

	function arg_27_0.lScrollPageSC.itemPitchCallback(arg_30_0, arg_30_1)
		local var_30_0 = arg_30_0 + 1

		arg_27_0.stopMusic()
		arg_27_0.checkUpdateSongTF()

		arg_27_0.curMidddleIndex = arg_30_0 + 1

		arg_27_0.saveRunData()
		arg_27_0.playPlateAni(arg_30_1, True)
		arg_27_0.updatePlayPanel()
		arg_27_0.tryPlayMusic()

	function arg_27_0.lScrollPageSC.itemRecycleCallback(arg_31_0, arg_31_1)
		arg_27_0.plateTFList[arg_31_0 + 1] = None

	addSlip(SLIP_TYPE_HRZ, arg_27_0.plateListPanel, function()
		if arg_27_0.curMidddleIndex > 1 and not arg_27_0.isPlayingAni:
			arg_27_0.setAniState(True)
			arg_27_0.lScrollPageSC.MoveToItemID(arg_27_0.curMidddleIndex - 1 - 1)
			arg_27_0.closePlateAni(arg_27_0.plateTFList[arg_27_0.curMidddleIndex]), function()
		if arg_27_0.curMidddleIndex < arg_27_0.lScrollPageSC.DataCount and not arg_27_0.isPlayingAni:
			arg_27_0.setAniState(True)
			arg_27_0.lScrollPageSC.MoveToItemID(arg_27_0.curMidddleIndex + 1 - 1)
			arg_27_0.closePlateAni(arg_27_0.plateTFList[arg_27_0.curMidddleIndex]))

def var_0_0.updatePlateListPanel(arg_34_0):
	arg_34_0.plateTFList = {}

	if #arg_34_0.musicForShowConfigList == 0:
		setActive(arg_34_0.plateListPanel, False)

		return
	else
		setActive(arg_34_0.plateListPanel, True)

	arg_34_0.lScrollPageSC.DataCount = #arg_34_0.musicForShowConfigList

	arg_34_0.lScrollPageSC.Init(arg_34_0.curMidddleIndex - 1)

def var_0_0.updatePlateTF(arg_35_0, arg_35_1, arg_35_2):
	if #arg_35_0.musicForShowConfigList == 0:
		return

	local var_35_0 = arg_35_0.findTF("CirclePanel/SmallImg", arg_35_1)
	local var_35_1 = arg_35_0.findTF("PlateImg", arg_35_1)
	local var_35_2 = arg_35_0.findTF("IndexNum", arg_35_1)
	local var_35_3 = arg_35_0.findTF("BlackMask", arg_35_1)
	local var_35_4 = arg_35_0.findTF("Lock", var_35_3)
	local var_35_5 = arg_35_0.findTF("UnlockTipText", var_35_3)
	local var_35_6 = arg_35_0.findTF("UnlockBtn", var_35_3)
	local var_35_7 = arg_35_0.findTF("DownloadBtn", var_35_3)
	local var_35_8 = arg_35_0.findTF("DownloadingImg", var_35_3)

	setText(var_35_8, i18n("res_downloading"))

	local var_35_9 = arg_35_2 + 1
	local var_35_10 = arg_35_0.getMusicConfigForShowByIndex(var_35_9)
	local var_35_11 = var_35_10.cover
	local var_35_12 = MusicCollectionConst.MUSIC_COVER_PATH_PREFIX .. var_35_11

	arg_35_0.resLoader.LoadSprite(var_35_12, var_35_11, var_35_1, False)
	setText(var_35_2, "#" .. var_35_9)

	local var_35_13 = var_35_10.id
	local var_35_14
	local var_35_15
	local var_35_16 = arg_35_0.appreciateProxy.getMusicExistStateByID(var_35_13)
	local var_35_17 = arg_35_0.getMusicStateByID(var_35_13)

	if var_35_17 == GalleryConst.CardStates.DirectShow:
		print("is impossible to go to this, something wrong")

		if var_35_16:
			setActive(var_35_3, False)
		else
			setActive(var_35_3, True)
			setActive(var_35_4, False)
			setActive(var_35_5, False)
			setActive(var_35_6, False)
			setActive(var_35_7, True)
			setActive(var_35_8, False)
	elif var_35_17 == GalleryConst.CardStates.Unlocked:
		if var_35_16:
			setActive(var_35_3, False)
		else
			local var_35_18 = arg_35_0.manager.state

			if var_35_18 == DownloadState.None or var_35_18 == DownloadState.CheckFailure:
				arg_35_0.manager.CheckD()

			local var_35_19 = var_35_10.music
			local var_35_20 = MusicCollectionConst.MUSIC_SONG_PATH_PREFIX .. var_35_19 .. ".b"
			local var_35_21 = arg_35_0.manager.CheckF(var_35_20)

			if var_35_21 == DownloadState.None or var_35_21 == DownloadState.CheckToUpdate or var_35_21 == DownloadState.UpdateFailure:
				setActive(var_35_3, True)
				setActive(var_35_4, False)
				setActive(var_35_5, False)
				setActive(var_35_6, False)
				setActive(var_35_7, True)
				setActive(var_35_8, False)
				table.removebyvalue(arg_35_0.downloadCheckIDList, var_35_13, True)
				onButton(arg_35_0, var_35_7, function()
					local function var_36_0()
						setActive(var_35_3, True)
						setActive(var_35_4, False)
						setActive(var_35_5, False)
						setActive(var_35_6, False)
						setActive(var_35_7, False)
						setActive(var_35_8, True)
						VersionMgr.Inst.RequestUIForUpdateF("GALLERY_BGM", var_35_20, False)

						if not table.contains(arg_35_0.downloadCheckIDList, var_35_13):
							table.insert(arg_35_0.downloadCheckIDList, var_35_13)

						arg_35_0.tryStartDownloadCheckTimer()

					if Application.internetReachability == UnityEngine.NetworkReachability.ReachableViaCarrierDataNetwork:
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							content = i18n("res_wifi_tip"),
							onYes = var_36_0
						})
					else
						var_36_0(), SFX_PANEL)
			elif var_35_21 == DownloadState.Updating:
				setActive(var_35_3, True)
				setActive(var_35_4, False)
				setActive(var_35_5, False)
				setActive(var_35_6, False)
				setActive(var_35_7, False)
				setActive(var_35_8, True)
			elif checkABExist(var_35_20):
				arg_35_0.appreciateProxy.updateMusicFileExistStateTable(var_35_13, True)
				table.removebyvalue(arg_35_0.downloadCheckIDList, var_35_13, True)

				if #arg_35_0.downloadCheckIDList == 0 and arg_35_0.downloadCheckTimer:
					arg_35_0.downloadCheckTimer.Stop()

					arg_35_0.downloadCheckTimer = None

				setActive(var_35_3, False)
				arg_35_0.updatePlayPanel()
	elif var_35_17 == GalleryConst.CardStates.Unlockable:
		setActive(var_35_3, True)
		setActive(var_35_4, True)
		setActive(var_35_5, False)
		setActive(var_35_6, True)
		setActive(var_35_7, False)
		setActive(var_35_8, False)
		onButton(arg_35_0, var_35_6, function()
			if not arg_35_0.appreciateUnlockMsgBox:
				arg_35_0.appreciateUnlockMsgBox = AppreciateUnlockMsgBox.New(arg_35_0._tf, arg_35_0.event, arg_35_0.contextData)

			arg_35_0.appreciateUnlockMsgBox.Reset()
			arg_35_0.appreciateUnlockMsgBox.Load()
			arg_35_0.appreciateUnlockMsgBox.ActionInvoke("showCustomMsgBox", {
				content = i18n("res_unlock_tip"),
				items = arg_35_0.appreciateProxy.getMusicUnlockMaterialByID(var_35_13),
				def onYes:()
					pg.m02.sendNotification(GAME.APPRECIATE_MUSIC_UNLOCK, {
						musicID = var_35_13,
						def unlockCBFunc:()
							arg_35_0.updatePlateTF(arg_35_1, arg_35_2)
							arg_35_0.updateSongTF(arg_35_0.songTFList[arg_35_2 + 1], arg_35_2 + 1)
							arg_35_0.updatePlayPanel()
							arg_35_0.tryPlayMusic()
							arg_35_0.appreciateUnlockMsgBox.hideCustomMsgBox()
					})
			}), SFX_PANEL)
	elif var_35_17 == GalleryConst.CardStates.DisUnlockable:
		setActive(var_35_3, True)
		setActive(var_35_4, True)
		setActive(var_35_5, True)
		setActive(var_35_6, False)
		setActive(var_35_7, False)
		setActive(var_35_8, False)
		setText(var_35_5, var_35_10.illustrate)

def var_0_0.initSongListPanel(arg_41_0):
	arg_41_0.songUIItemList.make(function(arg_42_0, arg_42_1, arg_42_2)
		if arg_42_0 == UIItemList.EventUpdate:
			arg_42_1 = arg_42_1 + 1
			arg_41_0.songTFList[arg_42_1] = arg_42_2

			arg_41_0.updateSongTF(arg_42_2, arg_42_1))

def var_0_0.updateSongListPanel(arg_43_0):
	arg_43_0.songTFList = {}

	if #arg_43_0.musicForShowConfigList == 0:
		return

	arg_43_0.songUIItemList.align(#arg_43_0.musicForShowConfigList)

def var_0_0.updateSongTF(arg_44_0, arg_44_1, arg_44_2):
	if #arg_44_0.musicForShowConfigList == 0:
		return

	local var_44_0 = arg_44_1
	local var_44_1 = arg_44_0.findTF("IndexText", var_44_0)
	local var_44_2 = arg_44_0.findTF("LikeToggle", var_44_0)
	local var_44_3 = arg_44_0.findTF("NameText", var_44_0)
	local var_44_4 = arg_44_0.findTF("PlayingImg", var_44_0)
	local var_44_5 = arg_44_0.findTF("DownloadImg", var_44_0)
	local var_44_6 = arg_44_0.findTF("LockImg", var_44_0)

	setActive(var_44_2, True)

	local var_44_7 = arg_44_0.getMusicConfigForShowByIndex(arg_44_2)
	local var_44_8 = var_44_7.id

	arg_44_0.updateSongTFLikeImg(arg_44_1, arg_44_0.appreciateProxy.isLikedByMusicID(var_44_8))

	local var_44_9
	local var_44_10
	local var_44_11 = arg_44_0.appreciateProxy.getMusicExistStateByID(var_44_8)
	local var_44_12 = arg_44_0.getMusicStateByID(var_44_8)
	local var_44_13 = var_44_7.music
	local var_44_14 = MusicCollectionConst.MUSIC_SONG_PATH_PREFIX .. var_44_13 .. ".b"
	local var_44_15 = arg_44_0.manager.CheckF(var_44_14)
	local var_44_16

	if var_44_12 == MusicCollectionConst.MusicStates.Unlockable:
		var_44_16 = MusicCollectionConst.Color_Of_Empty_Song

		setActive(var_44_4, False)
		setActive(var_44_5, False)
		setActive(var_44_6, True)
	elif var_44_12 == MusicCollectionConst.MusicStates.DisUnlockable:
		var_44_16 = MusicCollectionConst.Color_Of_Empty_Song

		setActive(var_44_4, False)
		setActive(var_44_5, False)
		setActive(var_44_6, True)
	elif var_44_12 == MusicCollectionConst.MusicStates.Unlocked:
		if var_44_11:
			local var_44_17 = arg_44_0.isPlayingSong
			local var_44_18 = arg_44_2 == arg_44_0.curMidddleIndex

			if var_44_17 and var_44_18:
				var_44_16 = MusicCollectionConst.Color_Of_Playing_Song

				setActive(var_44_4, True)
				setActive(var_44_5, False)
				setActive(var_44_6, False)
			else
				var_44_16 = MusicCollectionConst.Color_Of_Normal_Song

				setActive(var_44_4, False)
				setActive(var_44_5, False)
				setActive(var_44_6, False)
		elif var_44_15 == DownloadState.None or var_44_15 == DownloadState.CheckToUpdate or var_44_15 == DownloadState.UpdateFailure:
			var_44_16 = MusicCollectionConst.Color_Of_Empty_Song

			setActive(var_44_4, False)
			setActive(var_44_5, False)
			setActive(var_44_6, False)
			table.removebyvalue(arg_44_0.downloadCheckIDList, var_44_8, True)

			if #arg_44_0.downloadCheckIDList == 0 and arg_44_0.downloadCheckTimer:
				arg_44_0.downloadCheckTimer.Stop()

				arg_44_0.downloadCheckTimer = None

				return
		elif var_44_15 == DownloadState.Updating:
			var_44_16 = MusicCollectionConst.Color_Of_Empty_Song

			setActive(var_44_4, False)
			setActive(var_44_5, True)
			setActive(var_44_6, False)
		else
			setActive(var_44_4, False)
			setActive(var_44_5, False)
			setActive(var_44_6, False)

			if checkABExist(var_44_14):
				var_44_16 = MusicCollectionConst.Color_Of_Normal_Song

				arg_44_0.appreciateProxy.updateMusicFileExistStateTable(var_44_8, True)
				table.removebyvalue(arg_44_0.downloadCheckIDList, var_44_8, True)

				if #arg_44_0.downloadCheckIDList == 0 and arg_44_0.downloadCheckTimer:
					arg_44_0.downloadCheckTimer.Stop()

					arg_44_0.downloadCheckTimer = None

	setText(var_44_1, arg_44_2)
	setText(var_44_3, setColorStr(var_44_7.name, var_44_16))
	onButton(arg_44_0, var_44_0, function()
		if arg_44_0.isPlayingAni:
			return
		else
			if var_44_12 == MusicCollectionConst.MusicStates.Unlocked:
				if var_44_11:
					if not isActive(var_44_4):
						arg_44_0.setAniState(True)
						arg_44_0.closePlateAni(arg_44_0.plateTFList[arg_44_0.curMidddleIndex])
						arg_44_0.lScrollPageSC.MoveToItemID(arg_44_2 - 1)
				else
					local function var_45_0()
						setActive(var_44_4, False)
						setActive(var_44_5, True)
						setActive(var_44_6, False)
						VersionMgr.Inst.RequestUIForUpdateF("GALLERY_BGM", var_44_14, False)

						if not table.contains(arg_44_0.downloadCheckIDList, var_44_8):
							table.insert(arg_44_0.downloadCheckIDList, var_44_8)

						arg_44_0.tryStartDownloadCheckTimer()
						arg_44_0.setAniState(True)
						arg_44_0.closePlateAni(arg_44_0.plateTFList[arg_44_0.curMidddleIndex])
						arg_44_0.lScrollPageSC.MoveToItemID(arg_44_2 - 1)

					if Application.internetReachability == UnityEngine.NetworkReachability.ReachableViaCarrierDataNetwork:
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							content = i18n("res_wifi_tip"),
							onYes = var_45_0
						})
					else
						var_45_0()
			elif var_44_12 == MusicCollectionConst.MusicStates.DisUnlockable:
				pg.TipsMgr.GetInstance().ShowTips(var_44_7.illustrate)
			elif var_44_12 == MusicCollectionConst.MusicStates.Unlockable:
				if not arg_44_0.appreciateUnlockMsgBox:
					arg_44_0.appreciateUnlockMsgBox = AppreciateUnlockMsgBox.New(arg_44_0._tf, arg_44_0.event, arg_44_0.contextData)

				arg_44_0.appreciateUnlockMsgBox.Reset()
				arg_44_0.appreciateUnlockMsgBox.Load()
				arg_44_0.appreciateUnlockMsgBox.ActionInvoke("showCustomMsgBox", {
					content = i18n("res_unlock_tip"),
					items = arg_44_0.appreciateProxy.getMusicUnlockMaterialByID(var_44_8),
					def onYes:()
						pg.m02.sendNotification(GAME.APPRECIATE_MUSIC_UNLOCK, {
							musicID = var_44_8,
							def unlockCBFunc:()
								arg_44_0.lScrollPageSC.MoveToItemID(arg_44_2 - 1)

								if arg_44_0.plateTFList[arg_44_2]:
									arg_44_0.updatePlateTF(arg_44_0.plateTFList[arg_44_2], arg_44_2 - 1)

								arg_44_0.updateSongTF(arg_44_1, arg_44_2)
								arg_44_0.appreciateUnlockMsgBox.hideCustomMsgBox()
						})
				})

			arg_44_0.closeSongListPanel(), SFX_PANEL)

def var_0_0.updateSongTFLikeImg(arg_49_0, arg_49_1, arg_49_2):
	local var_49_0 = arg_49_1
	local var_49_1 = arg_49_0.findTF("LikeToggle", var_49_0)

	setActive(var_49_1, True)
	triggerToggle(var_49_1, arg_49_2)

def var_0_0.updateSortToggle(arg_50_0):
	setActive(arg_50_0.upImg1, arg_50_0.sortValue == MusicCollectionConst.Sort_Order_Up)
	setActive(arg_50_0.upImg2, arg_50_0.sortValue == MusicCollectionConst.Sort_Order_Up)
	setActive(arg_50_0.downImg1, arg_50_0.sortValue == MusicCollectionConst.Sort_Order_Down)
	setActive(arg_50_0.downImg2, arg_50_0.sortValue == MusicCollectionConst.Sort_Order_Down)

def var_0_0.updateLikeToggle(arg_51_0):
	setActive(arg_51_0.likeFilteOnImg, arg_51_0.likeValue == MusicCollectionConst.Filte_Like_Value)

def var_0_0.updatePlayPanel(arg_52_0):
	if #arg_52_0.musicForShowConfigList == 0:
		setActive(arg_52_0.playPanel, False)
		setActive(arg_52_0.playingAni, False)
		setActive(arg_52_0.staicImg, False)
		setActive(arg_52_0.songNameText, False)
		setActive(arg_52_0.emptyPanel, True)

		return
	else
		setActive(arg_52_0.playPanel, True)
		setActive(arg_52_0.playingAni, False)
		setActive(arg_52_0.staicImg, True)
		setActive(arg_52_0.songNameText, True)
		setActive(arg_52_0.emptyPanel, False)

	local var_52_0 = arg_52_0.getMusicConfigForShowByIndex(arg_52_0.curMidddleIndex)
	local var_52_1 = var_52_0.cover
	local var_52_2 = MusicCollectionConst.MUSIC_COVER_PATH_PREFIX .. var_52_1

	arg_52_0.resLoader.LoadSprite(var_52_2, var_52_1, arg_52_0.songImg, False)

	local var_52_3 = var_52_0.name

	setScrollText(arg_52_0.songNameText, var_52_3)
	setText(arg_52_0.playPanelNameText, var_52_3)
	setActive(arg_52_0.likeOnImg, arg_52_0.appreciateProxy.isLikedByMusicID(var_52_0.id))

	local var_52_4
	local var_52_5 = arg_52_0.getMusicStateByID(var_52_0.id)

	if var_52_5 == GalleryConst.CardStates.Unlockable or var_52_5 == GalleryConst.CardStates.DisUnlockable:
		setActive(arg_52_0.likeToggle, False)
	else
		setActive(arg_52_0.likeToggle, True)

	if not arg_52_0.isCanPlayByMusicID(var_52_0.id):
		setActive(arg_52_0.playBtn, False)
		setActive(arg_52_0.pauseBtn, False)
		setActive(arg_52_0.lockImg, True)

		arg_52_0.playSliderSC.enabled = False

		arg_52_0.playSliderSC.SetValueWithoutEvent(0)
		setActive(arg_52_0.nowTimeText, False)
		setActive(arg_52_0.totalTimeText, False)
	else
		setActive(arg_52_0.playBtn, True)
		setActive(arg_52_0.pauseBtn, False)
		setActive(arg_52_0.lockImg, False)

		arg_52_0.playSliderSC.enabled = True

		arg_52_0.playSliderSC.SetValueWithoutEvent(0)
		setActive(arg_52_0.nowTimeText, True)
		setActive(arg_52_0.totalTimeText, True)

def var_0_0.sortAndUpdate(arg_53_0, arg_53_1):
	arg_53_0.curMidddleIndex = 1

	arg_53_0.saveRunData()

	arg_53_0.musicForShowConfigList = arg_53_0.fliteMusicConfigForShow()

	arg_53_0.sortMusicConfigList(arg_53_1)

	arg_53_0.musicForShowConfigList = arg_53_0.filteMusicConfigByLike()

	arg_53_0.stopMusic()
	arg_53_0.checkUpdateSongTF()
	arg_53_0.updatePlateListPanel()
	arg_53_0.updateSongListPanel()
	arg_53_0.updatePlayPanel()
	arg_53_0.updateSortToggle()
	arg_53_0.updateLikeToggle()
	arg_53_0.tryPlayMusic()

def var_0_0.initTimer(arg_54_0):
	arg_54_0.playProgressTimer = Timer.New(function()
		if arg_54_0.playbackInfo:
			local var_55_0 = arg_54_0.playbackInfo.GetTime()

			arg_54_0.playSliderSC.SetValueWithoutEvent(var_55_0)
			setText(arg_54_0.nowTimeText, arg_54_0.descTime(var_55_0))

			if arg_54_0.playbackInfo.playback.GetStatus().ToInt() == 3:
				arg_54_0.stopMusic()
				arg_54_0.checkUpdateSongTF()
				SetActive(arg_54_0.pauseBtn, False)
				SetActive(arg_54_0.playBtn, True)
				arg_54_0.tryPlayMusic(), 0.033, -1)

	arg_54_0.playProgressTimer.Start()

def var_0_0.playPlateAni(arg_56_0, arg_56_1, arg_56_2, arg_56_3, arg_56_4):
	local var_56_0 = arg_56_0.findTF("CirclePanel", arg_56_1)
	local var_56_1 = arg_56_0.findTF("BoxImg", arg_56_1)

	setActive(var_56_0, arg_56_2)
	setActive(var_56_1, arg_56_2)

	local var_56_2 = 0.5

	if arg_56_2 == True:
		local var_56_3 = 198
		local var_56_4 = 443
		local var_56_5 = (var_56_4 - var_56_3) / var_56_2
		local var_56_6 = 0
		local var_56_7 = -121
		local var_56_8 = (var_56_7 - var_56_6) / var_56_2

		LeanTween.value(go(arg_56_1), 0, var_56_2, var_56_2).setOnUpdate(System.Action_float(function(arg_57_0)
			local var_57_0 = var_56_3 + var_56_5 * arg_57_0
			local var_57_1 = var_56_6 + var_56_8 * arg_57_0

			setAnchoredPosition(var_56_0, Vector2.New(var_57_0, 0))
			setAnchoredPosition(arg_56_1, Vector2.New(var_57_1, 0)))).setOnComplete(System.Action(function()
			setAnchoredPosition(var_56_0, Vector2.New(var_56_4, 0))
			setAnchoredPosition(arg_56_1, Vector2.New(var_56_7, 0))
			arg_56_0.setAniState(False)))
	else
		local var_56_9 = 448
		local var_56_10 = 198
		local var_56_11 = (var_56_10 - var_56_9) / var_56_2
		local var_56_12 = getAnchoredPosition(arg_56_1).x
		local var_56_13 = (arg_56_3 - arg_56_4) * (arg_56_0.lScrollPageSC.ItemSize.x + arg_56_0.lScrollPageSC.MarginSize.x)
		local var_56_14 = (var_56_13 - var_56_12) / var_56_2

		setAnchoredPosition(var_56_0, Vector2.New(var_56_10, 0))
		setAnchoredPosition(arg_56_1, Vector2.New(var_56_13, 0))

def var_0_0.closePlateAni(arg_59_0, arg_59_1):
	local var_59_0 = arg_59_0.findTF("CirclePanel", arg_59_1)
	local var_59_1 = arg_59_0.findTF("BoxImg", arg_59_1)

	setActive(var_59_0, False)
	setActive(var_59_1, False)
	setAnchoredPosition(var_59_0, Vector2.New(198, 0))
	setAnchoredPosition(arg_59_1, Vector2.zero)

def var_0_0.setAniState(arg_60_0, arg_60_1):
	arg_60_0.isPlayingAni = arg_60_1

def var_0_0.openSongListPanel(arg_61_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_61_0.songListPanel, False, {
		groupName = LayerWeightConst.GROUP_COLLECTION
	})

	arg_61_0.songListPanel.offsetMax = arg_61_0._tf.parent.offsetMax
	arg_61_0.songListPanel.offsetMin = arg_61_0._tf.parent.offsetMin

	setActive(arg_61_0.songListPanel, True)
	LeanTween.value(go(arg_61_0.panel), -460, 500, 0.3).setOnUpdate(System.Action_float(function(arg_62_0)
		setAnchoredPosition(arg_61_0.panel, {
			y = arg_62_0
		}))).setOnComplete(System.Action(function()
		setAnchoredPosition(arg_61_0.panel, {
			y = 500
		})))

def var_0_0.closeSongListPanel(arg_64_0, arg_64_1):
	if arg_64_1 == True:
		pg.UIMgr.GetInstance().UnblurPanel(arg_64_0.songListPanel, arg_64_0._tf)
		setActive(arg_64_0.songListPanel, False)

	if isActive(arg_64_0.songListPanel):
		LeanTween.cancel(go(arg_64_0.panel))

		local var_64_0 = getAnchoredPosition(arg_64_0.panel).y

		LeanTween.value(go(arg_64_0.panel), var_64_0, -460, 0.3).setOnUpdate(System.Action_float(function(arg_65_0)
			setAnchoredPosition(arg_64_0.panel, {
				y = arg_65_0
			}))).setOnComplete(System.Action(function()
			setAnchoredPosition(arg_64_0.panel, {
				y = -460
			})
			pg.UIMgr.GetInstance().UnblurPanel(arg_64_0.songListPanel, arg_64_0._tf)
			setActive(arg_64_0.songListPanel, False)))

def var_0_0.playMusic(arg_67_0):
	local var_67_0 = arg_67_0.getMusicConfigForShowByIndex(arg_67_0.curMidddleIndex).music

	if not arg_67_0.cueData:
		arg_67_0.cueData = CueData.GetCueData()

	arg_67_0.cueData.channelName = pg.CriMgr.C_GALLERY_MUSIC
	arg_67_0.cueData.cueSheetName = var_67_0
	arg_67_0.cueData.cueName = ""

	CriWareMgr.Inst.PlaySound(arg_67_0.cueData, CriWareMgr.CRI_FADE_TYPE.FADE_INOUT, function(arg_68_0)
		arg_67_0.playbackInfo = arg_68_0

		arg_67_0.playbackInfo.SetIgnoreAutoUnload(True)

		local var_68_0 = arg_67_0.playbackInfo.GetLength()

		setSlider(arg_67_0.playProgressBar, 0, arg_67_0.playbackInfo.GetLength(), 0)
		setText(arg_67_0.totalTimeText, arg_67_0.descTime(var_68_0))

		arg_67_0.isPlayingSong = True

		setActive(arg_67_0.playingAni, True)
		setActive(arg_67_0.staicImg, False)
		arg_67_0.updateSongTF(arg_67_0.songTFList[arg_67_0.curMidddleIndex], arg_67_0.curMidddleIndex))

def var_0_0.stopMusic(arg_69_0):
	if arg_69_0.playbackInfo:
		arg_69_0.playbackInfo.SetStartTime(0)
		CriWareMgr.Inst.StopSound(arg_69_0.cueData, CriWareMgr.CRI_FADE_TYPE.NONE)

		arg_69_0.playbackInfo = None
		arg_69_0.isPlayingSong = False

	setActive(arg_69_0.playingAni, False)
	setActive(arg_69_0.staicImg, True)
	arg_69_0.playSliderSC.SetValueWithoutEvent(0)
	setText(arg_69_0.nowTimeText, arg_69_0.descTime(0))

def var_0_0.checkUpdateSongTF(arg_70_0):
	if #arg_70_0.songTFList > 0:
		arg_70_0.updateSongTF(arg_70_0.songTFList[arg_70_0.curMidddleIndex], arg_70_0.curMidddleIndex)

def var_0_0.tryPlayMusic(arg_71_0):
	if #arg_71_0.musicForShowConfigList == 0:
		return

	local var_71_0 = arg_71_0.getMusicConfigForShowByIndex(arg_71_0.curMidddleIndex)

	if arg_71_0.isCanPlayByMusicID(var_71_0.id) and isActive(arg_71_0.playBtn):
		triggerButton(arg_71_0.playBtn)

def var_0_0.tryPauseMusic(arg_72_0):
	if isActive(arg_72_0.pauseBtn) and arg_72_0.playbackInfo:
		triggerButton(arg_72_0.pauseBtn)

def var_0_0.fliteMusicConfigForShow(arg_73_0):
	local var_73_0 = {}

	for iter_73_0, iter_73_1 in ipairs(pg.music_collect_config.all):
		local var_73_1 = arg_73_0.appreciateProxy.getSingleMusicConfigByID(iter_73_1)

		if arg_73_0.appreciateProxy.isMusicNeedUnlockByID(iter_73_1):
			if not arg_73_0.appreciateProxy.isMusicUnlockedByID(iter_73_1):
				local var_73_2, var_73_3 = arg_73_0.appreciateProxy.isMusicUnlockableByID(iter_73_1)

				if var_73_2:
					var_73_0[#var_73_0 + 1] = var_73_1
				elif var_73_3:
					var_73_0[#var_73_0 + 1] = var_73_1
			else
				var_73_0[#var_73_0 + 1] = var_73_1
		else
			var_73_0[#var_73_0 + 1] = var_73_1

	return var_73_0

def var_0_0.getMusicConfigForShowByIndex(arg_74_0, arg_74_1):
	local var_74_0 = arg_74_0.musicForShowConfigList[arg_74_1]

	if var_74_0:
		return var_74_0
	else
		assert(False, "不存在的index" .. tostring(arg_74_1))

def var_0_0.getMusicStateByID(arg_75_0, arg_75_1):
	if not arg_75_0.appreciateProxy.isMusicNeedUnlockByID(arg_75_1):
		return MusicCollectionConst.MusicStates.Unlocked
	elif arg_75_0.appreciateProxy.isMusicUnlockedByID(arg_75_1):
		return MusicCollectionConst.MusicStates.Unlocked
	elif arg_75_0.appreciateProxy.isMusicUnlockableByID(arg_75_1):
		return MusicCollectionConst.MusicStates.Unlockable
	else
		return MusicCollectionConst.MusicStates.DisUnlockable

def var_0_0.sortMusicConfigList(arg_76_0, arg_76_1):
	local function var_76_0(arg_77_0, arg_77_1)
		local var_77_0 = arg_77_0.id
		local var_77_1 = arg_77_1.id

		if arg_76_1 == True:
			return var_77_1 < var_77_0
		else
			return var_77_0 < var_77_1

	table.sort(arg_76_0.musicForShowConfigList, var_76_0)

def var_0_0.filteMusicConfigByLike(arg_78_0):
	if arg_78_0.likeValue == MusicCollectionConst.Filte_Normal_Value:
		return arg_78_0.musicForShowConfigList

	local var_78_0 = {}

	for iter_78_0, iter_78_1 in ipairs(arg_78_0.musicForShowConfigList):
		local var_78_1 = iter_78_1.id

		if arg_78_0.appreciateProxy.isLikedByMusicID(var_78_1):
			var_78_0[#var_78_0 + 1] = iter_78_1

	return var_78_0

def var_0_0.isCanPlayByMusicID(arg_79_0, arg_79_1):
	local var_79_0
	local var_79_1
	local var_79_2 = arg_79_0.appreciateProxy.getMusicExistStateByID(arg_79_1)
	local var_79_3 = arg_79_0.getMusicStateByID(arg_79_1)

	if var_79_3 == GalleryConst.CardStates.DirectShow:
		print("is impossible to go to this, something wrong")

		if var_79_2:
			return True
		else
			return False
	elif var_79_3 == GalleryConst.CardStates.Unlocked:
		if var_79_2:
			return True
		else
			return False
	elif var_79_3 == GalleryConst.CardStates.Unlockable:
		return False
	elif var_79_3 == GalleryConst.CardStates.DisUnlockable:
		return False

def var_0_0.descTime(arg_80_0, arg_80_1):
	local var_80_0 = math.floor(arg_80_1 / 1000)
	local var_80_1 = math.floor(var_80_0 / 3600)
	local var_80_2 = var_80_0 - var_80_1 * 3600
	local var_80_3 = math.floor(var_80_2 / 60)
	local var_80_4 = var_80_2 % 60

	if var_80_1 != 0:
		return string.format("%02d.%02d.%02d", var_80_1, var_80_3, var_80_4)
	else
		return string.format("%02d.%02d", var_80_3, var_80_4)

def var_0_0.tryStartDownloadCheckTimer(arg_81_0):
	if #arg_81_0.downloadCheckIDList == 0 and arg_81_0.downloadCheckTimer:
		arg_81_0.downloadCheckTimer.Stop()

		arg_81_0.downloadCheckTimer = None

		return

	if not arg_81_0.downloadCheckTimer and #arg_81_0.downloadCheckIDList > 0:
		local function var_81_0()
			for iter_82_0, iter_82_1 in ipairs(arg_81_0.downloadCheckIDList):
				local var_82_0

				for iter_82_2, iter_82_3 in ipairs(arg_81_0.musicForShowConfigList):
					if iter_82_3.id == iter_82_1:
						var_82_0 = iter_82_2

						break

				if var_82_0:
					local var_82_1 = arg_81_0.plateTFList[var_82_0]

					arg_81_0.updatePlateTF(var_82_1, var_82_0 - 1)

					local var_82_2 = arg_81_0.songTFList[var_82_0]

					arg_81_0.updateSongTF(var_82_2, var_82_0)

		arg_81_0.downloadCheckTimer = Timer.New(var_81_0, 1, -1)

		arg_81_0.downloadCheckTimer.Start()

return var_0_0
