local var_0_0 = class("MusicGameView", import("..BaseMiniGameView"))
local var_0_1 = False
local var_0_2 = 0.95
local var_0_3 = 0
local var_0_4 = 1
local var_0_5 = 3
local var_0_6 = 5
local var_0_7 = 2

def var_0_0.getUIName(arg_1_0):
	return "MusicGameUI"

def var_0_0.MyGetRuntimeData(arg_2_0):
	local var_2_0 = getProxy(PlayerProxy).getData().id

	arg_2_0.achieve_times = checkExist(arg_2_0.GetMGData().GetRuntimeData("elements"), {
		1
	}) or 0
	arg_2_0.isFirstgame = PlayerPrefs.GetInt("musicgame_first_" .. var_2_0)
	arg_2_0.bestScorelist = {}

	for iter_2_0 = 1, arg_2_0.music_amount * 2:
		local var_2_1 = arg_2_0.GetMGData().GetRuntimeData("elements")

		arg_2_0.bestScorelist[iter_2_0] = checkExist(var_2_1, {
			iter_2_0 + 2
		}) or 0

	arg_2_0.updatSelectview()

def var_0_0.MyStoreDataToServer(arg_3_0):
	local var_3_0 = getProxy(PlayerProxy).getData().id
	local var_3_1 = {
		arg_3_0.achieve_times,
		1
	}

	PlayerPrefs.SetInt("musicgame_first_" .. var_3_0, 1)

	for iter_3_0 = 1, arg_3_0.music_amount * 2:
		table.insert(var_3_1, iter_3_0 + 2, arg_3_0.bestScorelist[iter_3_0])

	arg_3_0.StoreDataToServer(var_3_1)

def var_0_0.init(arg_4_0):
	arg_4_0.UIMgr = pg.UIMgr.GetInstance()
	arg_4_0.useGetKey_flag = True
	arg_4_0.game_playingflag = False
	arg_4_0.countingfive_flag = False
	arg_4_0.downingleft_flag = False
	arg_4_0.downingright_flag = False
	arg_4_0.downingright_lastflag = False
	arg_4_0.downingleft_lastflag = False
	arg_4_0.nowS_flag = False
	arg_4_0.firstview_timerRunflag = False
	arg_4_0.ahead_timeflag = False
	arg_4_0.ahead_timerPauseFlag = False
	arg_4_0.changeLocalposTimerflag = False
	arg_4_0.piecelist_rf = {}
	arg_4_0.piecelist_rf[0] = 0
	arg_4_0.piecelist_lf = {}
	arg_4_0.piecelist_lf[0] = 0
	arg_4_0.piece_nowl = {}
	arg_4_0.piece_nowr = {}
	arg_4_0.piece_nowl_downflag = False
	arg_4_0.piece_nowr_downflag = False
	arg_4_0.piece_nowl_aloneflag = False
	arg_4_0.piece_nowr_aloneflag = False
	arg_4_0.SDmodel = {}
	arg_4_0.SDmodel_idolflag = False
	arg_4_0.musicgame_nowtime = 0
	arg_4_0.musicgame_lasttime = 0
	arg_4_0.time_interval = 0.01666
	arg_4_0.music_amount = #pg.beat_game_music.all
	arg_4_0.music_amount_middle = math.ceil(#pg.beat_game_music.all / 2)
	arg_4_0.musicDatas = {}

	for iter_4_0 = 1, #pg.beat_game_music.all:
		local var_4_0 = pg.beat_game_music.all[iter_4_0]
		local var_4_1 = pg.beat_game_music[var_4_0]

		table.insert(arg_4_0.musicDatas, var_4_1)

	table.sort(arg_4_0.musicDatas, function(arg_5_0, arg_5_1)
		if arg_5_0.sort and arg_5_1.sort:
			return arg_5_0.sort < arg_5_1.sort

		return arg_5_0.id < arg_5_1.id)

	arg_4_0.game_speed = PlayerPrefs.GetInt("musicgame_idol_speed") > 0 and PlayerPrefs.GetInt("musicgame_idol_speed") or 1
	arg_4_0.game_dgree = 1
	arg_4_0.countContent = arg_4_0.findTF("countContent")
	arg_4_0.countTf = None
	arg_4_0.top = arg_4_0.findTF("top")
	arg_4_0.btn_pause = arg_4_0.top.Find("pause")
	arg_4_0.score = arg_4_0.top.Find("score")
	arg_4_0.game_content = arg_4_0.findTF("GameContent")
	arg_4_0.noteTpl = arg_4_0.game_content.Find("noteTpl")
	arg_4_0.pauseview = arg_4_0.findTF("Pauseview")
	arg_4_0.selectview = arg_4_0.findTF("Selectview")

	local var_4_2 = findTF(arg_4_0.selectview, "bg")

	LoadSpriteAtlasAsync("ui/musicgameother_atlas", "selectbg", function(arg_6_0)
		GetComponent(var_4_2, typeof(Image)).sprite = arg_6_0

		setActive(var_4_2, True))

	arg_4_0.firstview = arg_4_0.findTF("firstview")
	arg_4_0.scoreview = arg_4_0.findTF("ScoreView")

	setActive(arg_4_0.scoreview, False)

	arg_4_0.scoreview_flag = False
	arg_4_0.bg = findTF(arg_4_0._tf, "bg")

	pg.BgmMgr.GetInstance().StopPlay()
	arg_4_0.updateMusic(var_0_4)

def var_0_0.didEnter(arg_7_0):
	local var_7_0 = 0

	local function var_7_1()
		var_7_0 = var_7_0 + arg_7_0.time_interval

		if var_7_0 == arg_7_0.time_interval:
			arg_7_0.MyGetRuntimeData()
			arg_7_0.showSelevtView()
		elif var_7_0 == arg_7_0.time_interval * 2:
			arg_7_0.updatSelectview()
			arg_7_0.Getdata_timer.Stop()

	LeanTween.delayedCall(go(arg_7_0.selectview), 2, System.Action(function()
		arg_7_0.MyGetRuntimeData()))

	arg_7_0.Getdata_timer = Timer.New(var_7_1, arg_7_0.time_interval, -1)

	arg_7_0.Getdata_timer.Start()

	arg_7_0.score_number = 0
	arg_7_0.combo_link = 0
	arg_7_0.combo_number = 0
	arg_7_0.perfect_number = 0
	arg_7_0.good_number = 0
	arg_7_0.miss_number = 0

	local var_7_2 = arg_7_0.GetMGData().getConfig("simple_config_data")

	arg_7_0.piecelist_speed = var_7_2.speed
	arg_7_0.piecelist_speedmin = var_7_2.speed_min
	arg_7_0.piecelist_speedmax = var_7_2.speed_max
	arg_7_0.specialcombo_number = var_7_2.special_combo
	arg_7_0.specialscore_number = var_7_2.special_score
	arg_7_0.score_perfect = var_7_2.perfect
	arg_7_0.score_good = var_7_2.good
	arg_7_0.score_miss = var_7_2.miss
	arg_7_0.score_combo = var_7_2.combo
	arg_7_0.time_perfect = var_7_2.perfecttime
	arg_7_0.time_good = var_7_2.goodtime
	arg_7_0.time_miss = var_7_2.misstime
	arg_7_0.time_laterperfect = var_7_2.laterperfecttime
	arg_7_0.time_latergood = var_7_2.latergoodtime
	arg_7_0.combo_interval = var_7_2.combo_interval
	arg_7_0.BtnRightDelegate = GetOrAddComponent(arg_7_0.game_content.Find("btn_right"), "EventTriggerListener")

	arg_7_0.BtnRightDelegate.AddPointDownFunc(function()
		arg_7_0.mousedowningright_flag = True

		setActive(arg_7_0.bottonRightBg, True))
	arg_7_0.BtnRightDelegate.AddPointUpFunc(function()
		arg_7_0.mousedowningright_flag = False

		setActive(arg_7_0.bottonRightBg, False))

	arg_7_0.BtnLeftDelegate = GetOrAddComponent(arg_7_0.game_content.Find("btn_left"), "EventTriggerListener")

	arg_7_0.BtnLeftDelegate.AddPointDownFunc(function()
		arg_7_0.mousedowningleft_flag = True

		setActive(arg_7_0.bottonLeftBg, True))
	arg_7_0.BtnLeftDelegate.AddPointUpFunc(function()
		arg_7_0.mousedowningleft_flag = False

		setActive(arg_7_0.bottonLeftBg, False))
	onButton(arg_7_0, arg_7_0.top.Find("pause"), function()
		arg_7_0.UIMgr.BlurPanel(arg_7_0.pauseview)
		setActive(arg_7_0.pauseview, True)

		arg_7_0.game_playingflag = False

		arg_7_0.effect_play("nothing")
		LoadSpriteAtlasAsync("ui/musicgameother_atlas", "pause_" .. arg_7_0.musicData.picture, function(arg_15_0)
			setImageSprite(arg_7_0.pauseview.Find("bottom/song"), arg_15_0, True))
		GetComponent(arg_7_0.pauseview.Find("bottom/img"), typeof(Image)).SetNativeSize()

		if not arg_7_0.ahead_timeflag:
			arg_7_0.pauseBgm()

			local var_14_0 = arg_7_0.getStampTime()
			local var_14_1 = arg_7_0.song_Tlength

			if var_14_0 < 0:
				var_14_0 = 0

			if var_14_0 >= 0 and var_14_1 > 0:
				local function var_14_2(arg_16_0)
					if arg_16_0 < 10:
						return "0" .. arg_16_0
					else
						return arg_16_0

				local var_14_3 = var_14_2(math.floor(var_14_0 % 60000 / 1000))
				local var_14_4 = var_14_2(math.floor(var_14_0 / 60000))

				setText(arg_7_0.pauseview.Find("bottom/now"), var_14_4 .. "." .. var_14_3)

				local var_14_5 = var_14_2(math.floor(var_14_1 % 60000 / 1000))
				local var_14_6 = var_14_2(math.floor(var_14_1 / 60000))

				setText(arg_7_0.pauseview.Find("bottom/total"), var_14_6 .. "." .. var_14_5)
				setActive(arg_7_0.pauseview.Find("bottom/triangle"), True)
				setActive(arg_7_0.pauseview.Find("bottom/TimeSlider"), True)
				setActive(arg_7_0.pauseview.Find("bottom/now"), True)
				setActive(arg_7_0.pauseview.Find("bottom/total"), True)
				setSlider(arg_7_0.pauseview.Find("bottom/TimeSlider"), 0, 1, var_14_0 / var_14_1)

				local var_14_7 = arg_7_0.pauseview.Find("bottom/triangle/min").localPosition.x
				local var_14_8 = arg_7_0.pauseview.Find("bottom/triangle/max").localPosition.x
				local var_14_9 = arg_7_0.pauseview.Find("bottom/triangle/now").localPosition

				arg_7_0.pauseview.Find("bottom/triangle/now").localPosition = Vector3(var_14_7 + var_14_0 / var_14_1 * (var_14_8 - var_14_7), var_14_9.y, var_14_9.z)

				arg_7_0.setActionSDmodel("stand2")
		else
			setActive(arg_7_0.pauseview.Find("bottom/triangle"), False)
			setActive(arg_7_0.pauseview.Find("bottom/TimeSlider"), False)
			setActive(arg_7_0.pauseview.Find("bottom/now"), False)
			setActive(arg_7_0.pauseview.Find("bottom/total"), False)

			arg_7_0.ahead_timerPauseFlag = True, SFX_UI_CLICK)
	onButton(arg_7_0, arg_7_0.pauseview.Find("bottom/back"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("reselect_music_game"),
			def onYes:()
				arg_7_0.UIMgr.UnblurPanel(arg_7_0.pauseview, arg_7_0._tf)
				setActive(arg_7_0.pauseview, False)
				arg_7_0.stopTimer()

				if arg_7_0.ahead_timer:
					arg_7_0.ahead_timer.Stop()

					arg_7_0.ahead_timeflag = False

				setActive(arg_7_0.selectview, True)

				GetOrAddComponent(arg_7_0.selectview, "CanvasGroup").blocksRaycasts = True

				arg_7_0.song_btns[arg_7_0.game_music].GetComponent(typeof(Animator)).Play("plate_out")

				arg_7_0.game_playingflag = False

				arg_7_0.loadAndPlayMusic()
				arg_7_0.rec_scorce()
		}), SFX_UI_CLICK)
	onButton(arg_7_0, arg_7_0.pauseview.Find("bottom/restart"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("restart_music_game"),
			def onYes:()
				arg_7_0.UIMgr.UnblurPanel(arg_7_0.pauseview, arg_7_0._tf)
				setActive(arg_7_0.pauseview, False)
				arg_7_0.stopTimer()

				if arg_7_0.ahead_timer:
					arg_7_0.ahead_timer.Stop()

					arg_7_0.ahead_timeflag = False

				arg_7_0.rec_scorce()
				arg_7_0.game_start()
				arg_7_0.effect_play("prepare")
		}), SFX_UI_CLICK)
	onButton(arg_7_0, arg_7_0.pauseview.Find("bottom/resume"), function()
		arg_7_0.UIMgr.UnblurPanel(arg_7_0.pauseview, arg_7_0._tf)
		setActive(arg_7_0.pauseview, False)
		arg_7_0.effect_play("prepare")

		if not arg_7_0.ahead_timeflag:
			local function var_21_0()
				arg_7_0.resumeBgm()

				arg_7_0.game_playingflag = True

			arg_7_0.count_five(var_21_0)
		else
			local function var_21_1()
				arg_7_0.ahead_timerPauseFlag = False
				arg_7_0.game_playingflag = True

				setActive(arg_7_0.pauseview.Find("bottom/triangle"), True)
				setActive(arg_7_0.pauseview.Find("bottom/TimeSlider"), True)
				setActive(arg_7_0.pauseview.Find("bottom/now"), True)
				setActive(arg_7_0.pauseview.Find("bottom/total"), True)

			arg_7_0.count_five(var_21_1), SFX_UI_CLICK)
	arg_7_0.addRingDragListenter()
	setActive(arg_7_0.selectview, True)

	GetOrAddComponent(arg_7_0.selectview, "CanvasGroup").blocksRaycasts = True

def var_0_0.updateBg(arg_24_0):
	if arg_24_0.isLoading:
		arg_24_0.dynamicBgHandler(arg_24_0.bgGo, function()
			setParent(arg_24_0.bgGo, arg_24_0.bg)
			setActive(arg_24_0.bgGo, True))

		return

	if arg_24_0.bgGo and arg_24_0.bgName:
		arg_24_0.dynamicBgHandler(arg_24_0.bgGo)
		PoolMgr.GetInstance().ReturnUI(arg_24_0.bgName, arg_24_0.bgGo)

	arg_24_0.bgName = "musicgamebg" .. arg_24_0.musicBg
	arg_24_0.isLoading = True

	local var_24_0 = arg_24_0.bgName

	PoolMgr.GetInstance().GetUI("" .. var_24_0, True, function(arg_26_0)
		arg_24_0.bgGo = arg_26_0

		if arg_24_0.isLoading == False:
			arg_24_0.dynamicBgHandler(arg_24_0.bgGo)
			PoolMgr.GetInstance().ReturnUI(var_24_0, arg_24_0.bgGo)
		else
			arg_24_0.isLoading = False

			setParent(arg_24_0.bgGo, arg_24_0.bg)
			setActive(arg_24_0.bgGo, True))

def var_0_0.dynamicBgHandler(arg_27_0, arg_27_1, arg_27_2):
	if IsNil(arg_27_1):
		return

	if arg_27_2 != None:
		arg_27_2()

def var_0_0.onBackPressed(arg_28_0):
	if not arg_28_0.countingfive_flag and not arg_28_0.firstview_timerRunflag:
		if arg_28_0.game_playingflag:
			if not isActive(arg_28_0.top.Find("pause_above")):
				triggerButton(arg_28_0.top.Find("pause"))
		elif isActive(arg_28_0.selectview) and var_0_3 == 0:
			arg_28_0.emit(var_0_0.ON_BACK)

def var_0_0.OnApplicationPaused(arg_29_0, arg_29_1):
	if arg_29_1 and not arg_29_0.countingfive_flag and not arg_29_0.firstview_timerRunflag and arg_29_0.game_playingflag and not isActive(arg_29_0.top.Find("pause_above")):
		triggerButton(arg_29_0.top.Find("pause"))

def var_0_0.willExit(arg_30_0):
	arg_30_0.isLoading = False

	if arg_30_0.bgGo and arg_30_0.bgName:
		arg_30_0.dynamicBgHandler(arg_30_0.bgGo)
		PoolMgr.GetInstance().ReturnUI(arg_30_0.bgName, arg_30_0.bgGo)

	if arg_30_0.timer:
		if arg_30_0.timer.running:
			arg_30_0.timer.Stop()

		arg_30_0.timer = None

	if arg_30_0.ahead_timer:
		if arg_30_0.ahead_timer.running:
			arg_30_0.ahead_timer.Stop()

		arg_30_0.ahead_timer = None

	if arg_30_0.firstview_timer:
		if arg_30_0.firstview_timer.running:
			arg_30_0.firstview_timer.Stop()

		arg_30_0.firstview_timer = None

	if arg_30_0.changeLocalpos_timer:
		if arg_30_0.changeLocalpos_timer.running:
			arg_30_0.changeLocalpos_timer.Stop()

		arg_30_0.changeLocalpos_timer = None

	if arg_30_0.count_timer:
		if arg_30_0.count_timer.running:
			arg_30_0.count_timer.Stop()

		arg_30_0.count_timer = None

	if arg_30_0.Scoceview_timer:
		if arg_30_0.Scoceview_timer.running:
			arg_30_0.Scoceview_timer.Stop()

		arg_30_0.Scoceview_timer = None

	if arg_30_0.Getdata_timer:
		if arg_30_0.Getdata_timer.running:
			arg_30_0.Getdata_timer.Stop()

		arg_30_0.Getdata_timer = None

	arg_30_0.clearSDModel()

	arg_30_0.piecelist_lt = {}
	arg_30_0.piecelist_lf = {}
	arg_30_0.musictable_l = {}
	arg_30_0.piece_nowl = {}
	arg_30_0.piecelist_rt = {}
	arg_30_0.piecelist_rf = {}
	arg_30_0.musictable_r = {}
	arg_30_0.piece_nowr = {}

	if arg_30_0.painting:
		retPaintingPrefab(arg_30_0.scoreview.Find("paint"), arg_30_0.painting)

		arg_30_0.painting = None

	if arg_30_0.criInfo:
		arg_30_0.criInfo.PlaybackStop()
		arg_30_0.criInfo.SetStartTimeAndPlay(0)
		pg.CriMgr.GetInstance().UnloadCueSheet(arg_30_0.getMusicBgm(arg_30_0.musicData))

		arg_30_0.criInfo = None

	if LeanTween.isTweening(go(arg_30_0.selectview)):
		LeanTween.cancel(go(arg_30_0.selectview))

	if LeanTween.isTweening(go(arg_30_0.countContent)):
		LeanTween.cancel(go(arg_30_0.countContent))

	if LeanTween.isTweening(go(arg_30_0.scoreview)):
		LeanTween.cancel(go(arg_30_0.scoreview))

	if LeanTween.isTweening(go(arg_30_0.game_content)):
		LeanTween.cancel(go(arg_30_0.game_content))

	pg.BgmMgr.GetInstance().ContinuePlay()

def var_0_0.clearSDModel(arg_31_0):
	if not arg_31_0.SDmodel or not arg_31_0.SDname or arg_31_0.SDname == "" or arg_31_0.SDname == "none":
		return

	for iter_31_0 = 1, #arg_31_0.SDmodel:
		if arg_31_0.SDmodel[iter_31_0]:
			PoolMgr.GetInstance().ReturnSpineChar(arg_31_0.SDname[iter_31_0], arg_31_0.SDmodel[iter_31_0])

	arg_31_0.SDmodel = {}

def var_0_0.list_push(arg_32_0, arg_32_1, arg_32_2):
	arg_32_1[arg_32_1[0] + 1] = arg_32_2
	arg_32_1[0] = arg_32_1[0] + 1

def var_0_0.list_pop(arg_33_0, arg_33_1):
	if arg_33_1[0] == 0:
		return

	local var_33_0 = arg_33_1[1]

	for iter_33_0 = 1, arg_33_1[0] - 1:
		arg_33_1[iter_33_0] = arg_33_1[iter_33_0 + 1]

	arg_33_1[0] = arg_33_1[0] - 1

	return var_33_0

def var_0_0.game_start(arg_34_0):
	arg_34_0.game_before()
	arg_34_0.effect_play("prepare")

	arg_34_0.game_playingflag = True
	arg_34_0.SDmodel_jumpcount = 0
	arg_34_0.gotspecialcombo_flag = False

	arg_34_0.updateBg()

	arg_34_0.song_Tlength = False

	arg_34_0.effect_play("nothing")
	arg_34_0.effect_play("prepare")

	if arg_34_0.isFirstgame == 0:
		arg_34_0.Firstshow(arg_34_0.firstview, function()
			arg_34_0.gameStart(), 2)
		arg_34_0.MyStoreDataToServer()
	else
		arg_34_0.gameStart()

def var_0_0.game_before(arg_36_0):
	arg_36_0.effect_play("nothing")

	arg_36_0.nowS_flag = False

	arg_36_0.setTfChildVisible(arg_36_0.top.Find("scoreContent/scroll"), False)

	arg_36_0.scoreSliderTf = arg_36_0.top.Find("scoreContent/scroll/" .. tostring(arg_36_0.musicData.content_type))

	setSlider(arg_36_0.scoreSliderTf, 0, 1, 0)
	setActive(arg_36_0.scoreSliderTf, True)
	setActive(findTF(arg_36_0.scoreSliderTf, "img/mask/yinyue20_S"), False)

	arg_36_0.scoreSFlag = False

	setImageColor(findTF(arg_36_0.scoreSliderTf, "img"), Color(1, 1, 1, 1))

	local var_36_0 = arg_36_0.game_content.Find("evaluate")

	for iter_36_0 = 1, var_36_0.childCount:
		local var_36_1 = var_36_0.GetChild(iter_36_0 - 1)

		for iter_36_1 = 1, var_36_1.childCount:
			setActive(var_36_1.GetChild(iter_36_1 - 1), False)

		setActive(findTF(var_36_1, tostring(arg_36_0.musicData.content_type)), True)
		setActive(var_36_0.GetChild(iter_36_0 - 1), False)

	local var_36_2 = arg_36_0.game_content.Find("bottomList")

	for iter_36_2 = 1, var_36_2.childCount:
		local var_36_3 = var_36_2.GetChild(iter_36_2 - 1)

		setActive(var_36_3, False)

	if arg_36_0.musicData.bottom_type and arg_36_0.musicData.bottom_type > 0:
		arg_36_0.bottonLeftBg = arg_36_0.game_content.Find("bottomList/" .. arg_36_0.musicData.bottom_type .. "/bottom_leftbg")
		arg_36_0.bottonRightBg = arg_36_0.game_content.Find("bottomList/" .. arg_36_0.musicData.bottom_type .. "/bottom_rightbg")

		setActive(arg_36_0.bottonLeftBg, False)
		setActive(arg_36_0.bottonRightBg, False)
		setActive(arg_36_0.game_content.Find("bottomList/" .. arg_36_0.musicData.bottom_type), True)
		setActive(arg_36_0.game_content.Find("bottomList/" .. arg_36_0.musicData.bottom_type), True)

	arg_36_0.clearSDModel()

	for iter_36_3 = 1, #arg_36_0.SDname:
		arg_36_0.loadSDModel(iter_36_3)

	arg_36_0.setActionSDmodel("stand2")
	setActive(arg_36_0.game_content.Find("combo"), False)
	setActive(arg_36_0.game_content.Find("combo_n"), False)
	setActive(arg_36_0.game_content.Find("MusicStar"), False)
	setActive(arg_36_0.game_content, True)
	setActive(arg_36_0._tf.Find("Spinelist"), True)
	setActive(arg_36_0.top, True)
	setActive(arg_36_0.fullComboEffect, False)
	setActive(arg_36_0.liveClearEffect, False)

	local var_36_4 = arg_36_0.getMusicNote(arg_36_0.musicData, arg_36_0.game_dgree)
	local var_36_5 = require(var_36_4)

	arg_36_0.leftPu = {}
	arg_36_0.rightPu = {}

	for iter_36_4, iter_36_5 in ipairs(var_36_5.left_track):
		table.insert(arg_36_0.leftPu, iter_36_5)

	for iter_36_6, iter_36_7 in ipairs(var_36_5.right_track):
		table.insert(arg_36_0.rightPu, iter_36_7)

	arg_36_0.setTfChildVisible(arg_36_0.noteTpl, False)

	if not arg_36_0.gameNoteLeft:
		arg_36_0.gameNoteLeft = MusicGameNote.New(findTF(arg_36_0.game_content, "MusicPieceLeft"), arg_36_0.noteTpl, MusicGameNote.type_left)

	if not arg_36_0.gameNoteRight:
		arg_36_0.gameNoteRight = MusicGameNote.New(findTF(arg_36_0.game_content, "MusicPieceRight"), arg_36_0.noteTpl, MusicGameNote.type_right)

	arg_36_0.gameNoteLeft.setStartData(arg_36_0.leftPu, arg_36_0.game_speed, arg_36_0.game_dgree, arg_36_0.noteType)
	arg_36_0.gameNoteLeft.setStateCallback(function(arg_37_0)
		arg_36_0.onStateCallback(arg_37_0))
	arg_36_0.gameNoteLeft.setLongTimeCallback(function(arg_38_0)
		arg_36_0.onLongTimeCallback(arg_38_0))
	arg_36_0.gameNoteRight.setStartData(arg_36_0.rightPu, arg_36_0.game_speed, arg_36_0.game_dgree, arg_36_0.noteType)
	arg_36_0.gameNoteRight.setStateCallback(function(arg_39_0)
		arg_36_0.onStateCallback(arg_39_0))
	arg_36_0.gameNoteRight.setLongTimeCallback(function(arg_40_0)
		arg_36_0.onLongTimeCallback(arg_40_0))

	arg_36_0.gameStepTime = 0
	arg_36_0.musictable_l = {}
	arg_36_0.musictable_l[0] = 0
	arg_36_0.musictable_r = {}
	arg_36_0.musictable_r[0] = 0
	arg_36_0.nowmusic_l = None
	arg_36_0.nowmusic_r = None

	local var_36_6 = arg_36_0.getMusicNote(arg_36_0.musicData, arg_36_0.game_dgree)

	arg_36_0.musicpu = require(var_36_6)

	for iter_36_8, iter_36_9 in ipairs(arg_36_0.musicpu.left_track):
		arg_36_0.list_push(arg_36_0.musictable_l, iter_36_9)

	for iter_36_10, iter_36_11 in ipairs(arg_36_0.musicpu.right_track):
		arg_36_0.list_push(arg_36_0.musictable_r, iter_36_11)

	local var_36_7 = arg_36_0.scoreSliderTf
	local var_36_8 = arg_36_0.top.Find("scoreContent/B")
	local var_36_9 = arg_36_0.top.Find("scoreContent/A")
	local var_36_10 = arg_36_0.top.Find("scoreContent/S")

	var_36_8.anchoredPosition = Vector3(arg_36_0.scoreSliderTf.anchoredPosition.x + var_36_7.rect.width * 0.53, var_36_8.anchoredPosition.y, var_36_8.anchoredPosition.z)
	var_36_9.anchoredPosition = Vector3(arg_36_0.scoreSliderTf.anchoredPosition.x + var_36_7.rect.width * 0.72, var_36_8.anchoredPosition.y, var_36_8.anchoredPosition.z)
	var_36_10.anchoredPosition = Vector3(arg_36_0.scoreSliderTf.anchoredPosition.x + var_36_7.rect.width * 0.885, var_36_8.anchoredPosition.y, var_36_8.anchoredPosition.z)

	arg_36_0.scoresliderAcombo_update()

def var_0_0.stopTimer(arg_41_0):
	if arg_41_0.timer.running:
		arg_41_0.timer.Stop()

def var_0_0.startTimer(arg_42_0):
	if not arg_42_0.timer.running:
		arg_42_0.timer.Start()

def var_0_0.loadSDModel(arg_43_0, arg_43_1):
	if not arg_43_0.SDname[arg_43_1] or arg_43_0.SDname[arg_43_1] == "" or arg_43_0.SDname[arg_43_1] == "none":
		arg_43_0.SDmodel[arg_43_1] = False

		setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/shadow"), False)
		setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/light"), False)

		return

	local var_43_0 = findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/light")
	local var_43_1 = findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/shadow")
	local var_43_2 = findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/" .. arg_43_0.musicData.content_type)

	var_43_0.anchoredPosition = var_43_2.anchoredPosition
	var_43_1.anchoredPosition = var_43_2.anchoredPosition

	setActive(var_43_0, True)

	if arg_43_0.musicLight and arg_43_0.shadowLight:
		setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/shadow"), True)
	else
		setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/shadow"), False)

	for iter_43_0 = 1, var_0_6:
		if arg_43_0.musicLight and arg_43_0.musicLight > 0:
			setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/light"), False)

			local var_43_3 = iter_43_0

			if arg_43_0.musicData.ships[iter_43_0] and arg_43_0.musicData.ships[iter_43_0] != "" and arg_43_0.musicData.ships[iter_43_0] != "none":
				LoadSpriteAtlasAsync("ui/musicgameother_atlas", "light" .. arg_43_0.musicLight, function(arg_44_0)
					setActive(findTF(arg_43_0._tf, "Spinelist/" .. var_43_3 .. "/light"), True)
					setImageSprite(findTF(arg_43_0._tf, "Spinelist/" .. var_43_3 .. "/light"), arg_44_0, True))

		setActive(findTF(arg_43_0._tf, "Spinelist/" .. arg_43_1 .. "/light"), False)

	pg.UIMgr.GetInstance().LoadingOff()
	PoolMgr.GetInstance().GetSpineChar(arg_43_0.SDname[arg_43_1], True, function(arg_45_0)
		arg_43_0.SDmodel[arg_43_1] = arg_45_0
		tf(arg_45_0).localScale = Vector3(1, 1, 1)

		arg_45_0.GetComponent("SpineAnimUI").SetAction("stand2", 0)
		setParent(arg_45_0, arg_43_0._tf.Find("Spinelist/" .. arg_43_1))

		local var_45_0 = arg_43_0._tf.Find("Spinelist/" .. arg_43_1 .. "/" .. arg_43_0.musicData.content_type)

		tf(arg_45_0).anchoredPosition = var_45_0.anchoredPosition)

def var_0_0.SDmodeljump_btnup(arg_46_0):
	if arg_46_0.downingright_flag or arg_46_0.downingleft_flag:
		arg_46_0.SDmodel_jumpcount = arg_46_0.SDmodel_jumpcount + arg_46_0.time_interval
		arg_46_0.SDmodel_jumpcount = arg_46_0.SDmodel_jumpcount > 1 and 1 or arg_46_0.SDmodel_jumpcount
	else
		if arg_46_0.SDmodel_jumpcount == 1:
			arg_46_0.setActionSDmodel("jump")

			arg_46_0.SDmodel_idolflag = False

		if arg_46_0.SDmodel_jumpcount > 0:
			arg_46_0.SDmodel_jumpcount = arg_46_0.SDmodel_jumpcount - arg_46_0.time_interval
			arg_46_0.SDmodel_jumpcount = arg_46_0.SDmodel_jumpcount < 0 and 0 or arg_46_0.SDmodel_jumpcount

		if arg_46_0.SDmodel_jumpcount == 0 and not arg_46_0.SDmodel_idolflag:
			arg_46_0.SDmodel_idolflag = True

			arg_46_0.setActionSDmodel("idol")

def var_0_0.setActionSDmodel(arg_47_0, arg_47_1, arg_47_2):
	arg_47_2 = arg_47_2 or 0

	for iter_47_0 = 1, #arg_47_0.SDmodel:
		if arg_47_0.SDmodel[iter_47_0]:
			arg_47_0.SDmodel[iter_47_0].GetComponent("SpineAnimUI").SetAction(arg_47_1, arg_47_2)

def var_0_0.loadAndPlayMusic(arg_48_0, arg_48_1, arg_48_2):
	local var_48_0 = arg_48_0.getMusicBgm(arg_48_0.musicData)

	var_0_3 = var_0_3 + 1

	CriWareMgr.Inst.PlayBGM(var_48_0, CriWareMgr.CRI_FADE_TYPE.FADE_INOUT, function(arg_49_0)
		if arg_49_0 == None:
			warning("Missing BGM ." .. (var_48_0 or "NIL"))
		else
			print("加载完毕,开始播放音乐")

			if arg_48_0.countingfive_flag:
				return

			arg_48_0.criInfo = arg_49_0
			arg_48_0.song_Tlength = arg_49_0.GetLength()

			arg_49_0.PlaybackStop()

			if IsUnityEditor and var_0_1:
				arg_48_0.criInfo.SetStartTimeAndPlay(arg_48_0.criInfo.GetLength() * var_0_2)
			else
				arg_49_0.SetStartTimeAndPlay(arg_48_2 and arg_48_2 >= 0 and arg_48_2 or 0)

			var_0_3 = var_0_3 - 1

			if arg_48_1:
				arg_48_1())

def var_0_0.getStampTime(arg_50_0):
	if arg_50_0.aheadtime_count:
		return (arg_50_0.aheadtime_count - 2) * 1000
	elif arg_50_0.criInfo:
		return arg_50_0.criInfo.GetTime()

	return None

def var_0_0.pauseBgm(arg_51_0):
	if arg_51_0.criInfo:
		arg_51_0.pauseTime = arg_51_0.criInfo.GetTime()

		arg_51_0.criInfo.PlaybackStop()

	if arg_51_0.timer and arg_51_0.timer.running:
		arg_51_0.timer.Stop()

def var_0_0.resumeBgm(arg_52_0):
	if not arg_52_0.timer.running:
		arg_52_0.timer.Start()

	arg_52_0.loadAndPlayMusic(function()
		return, arg_52_0.pauseTime)

def var_0_0.rec_scorce(arg_54_0):
	arg_54_0.score_number = 0
	arg_54_0.combo_link = 0
	arg_54_0.combo_number = 0
	arg_54_0.perfect_number = 0
	arg_54_0.good_number = 0
	arg_54_0.miss_number = 0
	arg_54_0.gotspecialcombo_flag = False

	setActive(arg_54_0.top.Find("scoreContent/B/bl"), False)
	setActive(arg_54_0.top.Find("scoreContent/A/al"), False)
	setActive(arg_54_0.top.Find("scoreContent/S/sl"), False)
	setText(arg_54_0.gameScoreTf, 0)
	setText(arg_54_0.game_content.Find("combo_n/" .. arg_54_0.musicData.content_type), 0)

def var_0_0.effect_play(arg_55_0, arg_55_1, arg_55_2):
	if arg_55_1 == "nothing":
		setActive(arg_55_0.yinyuePefectLoop, False)
		setActive(arg_55_0.top.Find("scoreContent/S/liubianxing"), False)
		setActive(arg_55_0.yinyueGood, False)
		setActive(arg_55_0.yinyuePerfect, False)
		setActive(arg_55_0.game_content.Find("MusicStar"), False)
		SetActive(arg_55_0.yinyueComboeffect, False)
	elif arg_55_1 == "prepare":
		-- block empty
	elif arg_55_1 == "good":
		setActive(arg_55_0.yinyueGood, False)
		setActive(arg_55_0.yinyueGood, True)
	elif arg_55_1 == "perfect":
		setActive(arg_55_0.yinyuePerfect, False)
		setActive(arg_55_0.yinyuePerfect, True)
	elif arg_55_1 == "perfect_loop02":
		if arg_55_2:
			if not isActive(arg_55_0.yinyuePefectLoop):
				setActive(arg_55_0.yinyuePefectLoop, True)
		else
			setActive(arg_55_0.yinyuePefectLoop, False)
	elif arg_55_1 == "S":
		if arg_55_2:
			setActive(findTF(arg_55_0.scoreSliderTf, "img/mask/yinyue20_S"), True)
		else
			setActive(findTF(arg_55_0.scoreSliderTf, "img/mask/yinyue20_S"), False)

def var_0_0.scoresliderAcombo_update(arg_56_0):
	local var_56_0 = arg_56_0.score_number
	local var_56_1 = 0

	setText(arg_56_0.gameScoreTf, arg_56_0.score_number)

	local var_56_2 = arg_56_0.game_music
	local var_56_3 = arg_56_0.game_dgree

	if var_56_0 < arg_56_0.score_blist[var_56_3]:
		var_56_1 = var_56_0 / arg_56_0.score_blist[var_56_3] * 0.53
	elif var_56_0 >= arg_56_0.score_blist[var_56_3] and var_56_0 < arg_56_0.score_alist[var_56_3]:
		var_56_1 = 0.53 + (var_56_0 - arg_56_0.score_blist[var_56_3]) / (arg_56_0.score_alist[var_56_3] - arg_56_0.score_blist[var_56_3]) * 0.19
	elif var_56_0 >= arg_56_0.score_alist[var_56_3] and var_56_0 < arg_56_0.score_slist[var_56_3]:
		var_56_1 = 0.72 + (var_56_0 - arg_56_0.score_alist[var_56_3]) / (arg_56_0.score_slist[var_56_3] - arg_56_0.score_alist[var_56_3]) * 0.155
	else
		var_56_1 = 0.885 + (var_56_0 - arg_56_0.score_slist[var_56_3]) / (arg_56_0.score_sslist[var_56_3] - arg_56_0.score_slist[var_56_3]) * 0.115

	setSlider(arg_56_0.scoreSliderTf, 0, 1, var_56_1)

	if var_56_1 < 0.53:
		setActive(arg_56_0.top.Find("scoreContent/B/bl"), False)
		setActive(arg_56_0.top.Find("scoreContent/A/al"), False)
		setActive(arg_56_0.top.Find("scoreContent/S/sl"), False)
	elif var_56_1 >= 0.53:
		setActive(arg_56_0.top.Find("scoreContent/B/bl"), True)

		if var_56_1 >= 0.72:
			setActive(arg_56_0.top.Find("scoreContent/A/al"), True)

			if var_56_1 >= 0.885:
				if not arg_56_0.nowS_flag:
					arg_56_0.nowS_flag = True

					arg_56_0.effect_play("S", True)

				setActive(arg_56_0.top.Find("scoreContent/S/sl"), True)

	setText(arg_56_0.game_content.Find("combo_n/" .. arg_56_0.musicData.content_type), arg_56_0.combo_link)

def var_0_0.score_update(arg_57_0, arg_57_1):
	local var_57_0 = arg_57_0.game_content.Find("evaluate")

	for iter_57_0 = 1, 3:
		setActive(var_57_0.GetChild(iter_57_0 - 1), False)

	setActive(var_57_0.GetChild(arg_57_1), True)

	if arg_57_1 == 0:
		arg_57_0.combo_link = 0
		arg_57_0.score_number = arg_57_0.score_number + arg_57_0.score_miss
		arg_57_0.miss_number = arg_57_0.miss_number + 1

		setActive(arg_57_0.game_content.Find("combo"), False)
		setActive(arg_57_0.game_content.Find("combo_n"), False)
	else
		arg_57_0.combo_link = arg_57_0.combo_link + 1
		arg_57_0.combo_number = arg_57_0.combo_number > arg_57_0.combo_link and arg_57_0.combo_number or arg_57_0.combo_link

		if arg_57_0.combo_link > 1:
			setActive(arg_57_0.game_content.Find("combo"), True)
			setActive(arg_57_0.game_content.Find("combo_n"), True)
			arg_57_0.game_content.Find("combo").GetComponent(typeof(Animation)).Play()
			arg_57_0.game_content.Find("combo_n").GetComponent(typeof(Animation)).Play()
		else
			setActive(arg_57_0.game_content.Find("combo"), False)
			setActive(arg_57_0.game_content.Find("combo_n"), False)

		pg.CriMgr.GetInstance().PlaySE_V3("ui-maoudamashii")

	local var_57_1 = 0

	for iter_57_1 = 1, #arg_57_0.combo_interval:
		if arg_57_0.combo_link > arg_57_0.combo_interval[iter_57_1]:
			var_57_1 = var_57_1 + 1
		else
			break

	if arg_57_1 == 1:
		arg_57_0.score_number = arg_57_0.score_number + arg_57_0.score_good + var_57_1 * arg_57_0.score_combo
		arg_57_0.good_number = arg_57_0.good_number + 1

		arg_57_0.effect_play("good")
	elif arg_57_1 == 2:
		arg_57_0.score_number = arg_57_0.score_number + arg_57_0.score_perfect + var_57_1 * arg_57_0.score_combo
		arg_57_0.perfect_number = arg_57_0.perfect_number + 1

		arg_57_0.effect_play("perfect")

	if arg_57_0.gameNoteLeft.loopTime() or arg_57_0.gameNoteRight.loopTime():
		arg_57_0.effect_play("perfect_loop02", True)
	else
		arg_57_0.effect_play("perfect_loop02", False)

	local var_57_2 = arg_57_0.yinyueComboeffect

	if arg_57_0.game_dgree == 2 and arg_57_0.combo_link > 50 or arg_57_0.game_dgree == 1 and arg_57_0.combo_link > 20:
		if not isActive(var_57_2):
			SetActive(var_57_2, True)
			setActive(arg_57_0.game_content.Find("MusicStar"), True)
	else
		SetActive(var_57_2, False)
		setActive(arg_57_0.game_content.Find("MusicStar"), False)

def var_0_0.count_five(arg_58_0, arg_58_1):
	if arg_58_0.countingfive_flag:
		return

	arg_58_0.countingfive_flag = True

	setActive(arg_58_0.countTf, True)
	setActive(arg_58_0.countContent, True)
	arg_58_0.setActionSDmodel("stand2")

	local var_58_0 = var_0_5
	local var_58_1 = findTF(arg_58_0.countTf, "img")
	local var_58_2 = findTF(arg_58_0.countTf, "bg")

	local function var_58_3(arg_59_0)
		for iter_59_0 = 1, var_58_1.childCount:
			local var_59_0 = var_58_1.GetChild(iter_59_0 - 1)
			local var_59_1 = iter_59_0 == arg_59_0

			setActive(var_59_0, var_59_1)

	setActive(var_58_2, False)
	var_58_3(0)

	local var_58_4 = findTF(arg_58_0.countTf, "ready")
	local var_58_5 = findTF(arg_58_0.countTf, "effectContent")

	setActive(var_58_5, False)
	setActive(var_58_4, False)

	arg_58_0.count_timer = Timer.New(function()
		if arg_58_0.criInfo and arg_58_0.criInfo.GetTime() > 0:
			arg_58_0.pauseBgm()

		var_58_3(var_58_0)

		var_58_0 = var_58_0 - 1

		if var_58_0 < 0:
			arg_58_0.count_timer.Stop()
			setActive(var_58_2, False)
			var_58_3(0)
			setActive(var_58_4, True)
			setActive(var_58_5, True)
			LeanTween.value(go(arg_58_0.countContent), 0, 2, 2).setOnUpdate(System.Action_float(function(arg_61_0)
				local var_61_0

				if arg_61_0 <= 0.25:
					local var_61_1 = arg_61_0 * 4

					var_58_4.localScale = Vector3(var_61_1, var_61_1, var_61_1)

					setImageAlpha(var_58_4, var_61_1)
					setLocalScale(var_58_5, Vector3(var_61_1, var_61_1, var_61_1))
				elif arg_61_0 >= 1.8:
					local var_61_2 = (2 - arg_61_0) * 4

					var_58_4.localScale = Vector3(var_61_2, var_61_2, var_61_2)

					setLocalScale(var_58_5, Vector3(var_61_2, var_61_2, var_61_2))
					setImageAlpha(var_58_4, var_61_2))).setEase(LeanTweenType.linear).setOnComplete(System.Action(function()
				var_58_4.localScale = Vector3(1, 1, 1, 1)

				setLocalScale(var_58_5, Vector3(1, 1, 1, 1))
				setImageAlpha(var_58_4, 1)
				setActive(var_58_4, False)

				arg_58_0.countingfive_flag = False

				setActive(arg_58_0.countContent, False)
				setActive(arg_58_0.countTf, False)
				arg_58_0.setActionSDmodel("idol")
				arg_58_1()))
		else
			setActive(var_58_2, True), 1, -1)

	arg_58_0.count_timer.Start()

def var_0_0.showSelevtView(arg_63_0):
	if arg_63_0.isFirstgame == 0:
		arg_63_0.Firstshow(arg_63_0.firstview, function()
			return, 1)

	local var_63_0 = arg_63_0.selectview.Find("Main")
	local var_63_1 = var_63_0.Find("Start_btn")
	local var_63_2 = var_63_0.Find("DgreeList")
	local var_63_3 = var_63_0.Find("MusicList")
	local var_63_4 = var_63_0.Find("namelist")
	local var_63_5 = arg_63_0.selectview.Find("top")
	local var_63_6 = var_63_5.Find("Speedlist")
	local var_63_7 = var_63_5.Find("help_btn")
	local var_63_8 = var_63_5.Find("back")
	local var_63_9 = arg_63_0.selectview.GetComponent("Animator")

	arg_63_0.selectview.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_65_0)
		setActive(arg_63_0.selectview, False))
	onButton(arg_63_0, var_63_7, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_music_game.tip
		}), SFX_PANEL)
	onButton(arg_63_0, var_63_8, function()
		if var_0_3 == 0:
			arg_63_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_63_0, var_63_1, function()
		if var_0_3 == 0:
			var_63_9.Play("selectExitAnim")
			arg_63_0.clearSDModel()
			arg_63_0.updateMusic(arg_63_0.selectIndex)
			arg_63_0.game_start()

			GetOrAddComponent(arg_63_0.selectview, "CanvasGroup").blocksRaycasts = False
		else
			arg_63_0.startBtnReady = True, SFX_UI_CONFIRM)
	onButton(arg_63_0, var_63_2.Find("easy"), function()
		arg_63_0.game_dgree = 1

		setActive(var_63_2.Find("hard/frame"), False)
		setActive(var_63_2.Find("easy/frame"), True)
		arg_63_0.updatSelectview(), SFX_UI_CLICK)
	onButton(arg_63_0, var_63_2.Find("hard"), function()
		arg_63_0.game_dgree = 2

		setActive(var_63_2.Find("easy/frame"), False)
		setActive(var_63_2.Find("hard/frame"), True)
		arg_63_0.updatSelectview(), SFX_UI_CLICK)
	onButton(arg_63_0, var_63_6, function()
		setActive(var_63_6.Find("x" .. arg_63_0.game_speed), False)

		arg_63_0.game_speed = arg_63_0.game_speed + 1 > 4 and 1 or arg_63_0.game_speed + 1

		PlayerPrefs.SetInt("musicgame_idol_speed", arg_63_0.game_speed)
		setActive(var_63_6.Find("x" .. arg_63_0.game_speed), True), SFX_UI_CLICK)

	arg_63_0.song_btn = var_63_3.Find("song")

	setActive(arg_63_0.song_btn, False)

	arg_63_0.song_btns = {}

	local var_63_10 = arg_63_0.gameMusicIndex

	for iter_63_0 = 1, arg_63_0.music_amount:
		arg_63_0.song_btns[iter_63_0] = cloneTplTo(arg_63_0.song_btn, var_63_3, "music" .. iter_63_0)

		local var_63_11 = arg_63_0.musicDatas[iter_63_0]

		setActive(arg_63_0.song_btns[iter_63_0], True)

		local var_63_12 = arg_63_0.song_btn.localPosition
		local var_63_13 = math.abs(iter_63_0 - var_63_10)
		local var_63_14 = iter_63_0 - var_63_10 < arg_63_0.music_amount_middle and var_63_13 or iter_63_0 - arg_63_0.music_amount_middle * 2

		arg_63_0.song_btns[iter_63_0].localPosition = Vector3(var_63_12.x + var_63_14 * 1022, var_63_12.y, var_63_12.z)

		local var_63_15 = arg_63_0.song_btn.localScale

		arg_63_0.song_btns[iter_63_0].localScale = Vector3(var_63_15.x - math.abs(var_63_14) * 0.2, var_63_15.y - math.abs(var_63_14) * 0.2, var_63_15.z - math.abs(var_63_14) * 0.2)

		local var_63_16 = arg_63_0.song_btns[iter_63_0].Find("song").GetComponent(typeof(Image))

		var_63_16.sprite = var_63_3.Find("img/" .. var_63_11.picture).GetComponent(typeof(Image)).sprite
		arg_63_0.song_btns[iter_63_0].Find("zhuanji3/zhuanji2_5").GetComponent(typeof(Image)).sprite = var_63_3.Find("img/" .. var_63_11.picture .. "_1").GetComponent(typeof(Image)).sprite
		var_63_16.color = Color.New(1, 1, 1, 1 - math.abs(var_63_14) * 0.6)

		onButton(arg_63_0, arg_63_0.song_btns[iter_63_0], function()
			arg_63_0.clickSongBtns(var_63_4, iter_63_0), SFX_UI_CLICK)

		if iter_63_0 == var_63_10:
			arg_63_0.song_btns[iter_63_0].GetComponent(typeof(Animator)).Play("plate_out")

			arg_63_0.song_btns[iter_63_0].GetComponent(typeof(Button)).interactable = False

	arg_63_0.clickSongBtns(var_63_4, 1)

def var_0_0.updateMusic(arg_73_0, arg_73_1):
	arg_73_0.musicData = arg_73_0.musicDatas[arg_73_1]
	arg_73_0.selectIndex = arg_73_1
	arg_73_0.game_music = arg_73_0.musicData.id

	if arg_73_0.musicData.ships and #arg_73_0.musicData.ships > 0:
		arg_73_0.musicShips = arg_73_0.musicData.ships
		arg_73_0.settlementPainting = arg_73_0.musicData.settlement_painting
		arg_73_0.musicLight = arg_73_0.musicData.light
		arg_73_0.shadowLight = arg_73_0.musicData.shadow == 1
		arg_73_0.musicBg = arg_73_0.musicData.bg
	else
		local var_73_0 = MusicGameConst.getRandomBand()

		arg_73_0.musicShips = var_73_0.ships
		arg_73_0.settlementPainting = var_73_0.settlement_painting
		arg_73_0.musicLight = var_73_0.light
		arg_73_0.shadowLight = True
		arg_73_0.musicBg = var_73_0.bg

	arg_73_0.noteType = arg_73_0.musicData.note_type
	arg_73_0.gameMusicIndex = var_0_4
	arg_73_0.SDname = arg_73_0.musicShips
	arg_73_0.score_blist = arg_73_0.musicData.score_rank[1]
	arg_73_0.score_alist = arg_73_0.musicData.score_rank[2]
	arg_73_0.score_slist = arg_73_0.musicData.score_rank[3]
	arg_73_0.score_sslist = arg_73_0.musicData.score_rank[4]

	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/B/bl"), False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/B/b"), False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/A/al"), False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/A/a"), False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/S/sl"), False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("scoreContent/S/s"), False)
	setActive(arg_73_0.top.Find("scoreContent/B/b/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.top.Find("scoreContent/B/bl/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.top.Find("scoreContent/A/a/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.top.Find("scoreContent/A/al/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.top.Find("scoreContent/S/s/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.top.Find("scoreContent/S/sl/" .. arg_73_0.musicData.content_type), True)
	arg_73_0.setTfChildVisible(arg_73_0.game_content.Find("combo_n"), False)
	arg_73_0.setTfChildVisible(arg_73_0.game_content.Find("combo"), False)
	setActive(arg_73_0.game_content.Find("combo_n/" .. arg_73_0.musicData.content_type), True)
	setActive(arg_73_0.game_content.Find("combo/" .. arg_73_0.musicData.content_type), True)
	arg_73_0.setTfChildVisible(arg_73_0.btn_pause, False)
	setActive(findTF(arg_73_0.btn_pause, arg_73_0.musicData.content_type), True)
	arg_73_0.setTfChildVisible(arg_73_0.countContent, False)
	arg_73_0.setTfChildVisible(arg_73_0.top.Find("score"), False)
	setActive(arg_73_0.top.Find("score/" .. tostring(arg_73_0.musicData.content_type)), True)

	arg_73_0.gameScoreTf = arg_73_0.top.Find("score/" .. tostring(arg_73_0.musicData.content_type) .. "/text")
	arg_73_0.countTf = findTF(arg_73_0.countContent, arg_73_0.musicData.content_type)

	arg_73_0.updateEffectTf()

def var_0_0.setTfChildVisible(arg_74_0, arg_74_1, arg_74_2):
	for iter_74_0 = 1, arg_74_1.childCount:
		local var_74_0 = arg_74_1.GetChild(iter_74_0 - 1)

		setActive(var_74_0, False)

def var_0_0.updateEffectTf(arg_75_0):
	local var_75_0 = findTF(arg_75_0.game_content, "effect")

	for iter_75_0 = 1, var_75_0.childCount:
		local var_75_1 = var_75_0.GetChild(iter_75_0 - 1)

		setActive(var_75_1, False)

	local var_75_2 = arg_75_0.musicData.content_type

	setActive(findTF(arg_75_0.game_content, "effect/" .. var_75_2))

	arg_75_0.fullComboEffect = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_Fullcombo")
	arg_75_0.liveClearEffect = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_LiveClear")
	arg_75_0.yinyueGood = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_good")
	arg_75_0.yinyueComboeffect = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_comboeffect")
	arg_75_0.yinyuePerfect = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_perfect")
	arg_75_0.yinyuePefectLoop = arg_75_0.game_content.Find("effect/" .. var_75_2 .. "/yinyue_perfect_loop02")

def var_0_0.getBeatGameMusicData(arg_76_0, arg_76_1):
	for iter_76_0 = 1, #arg_76_0.musicDatas:
		if arg_76_0.musicDatas[iter_76_0].id == arg_76_1:
			return arg_76_0.musicDatas[iter_76_0]

	return None

def var_0_0.clickSongBtns(arg_77_0, arg_77_1, arg_77_2):
	if var_0_3 > 0:
		return

	setActive(arg_77_1.Find("song" .. arg_77_0.musicData.picture), False)
	arg_77_0.MyGetRuntimeData()
	arg_77_0.clearSDModel()
	arg_77_0.updateMusic(arg_77_2)
	arg_77_0.loadAndPlayMusic()
	arg_77_0.updatSelectview()
	arg_77_0.changeLocalpos(arg_77_2)
	setActive(arg_77_1.Find("song" .. arg_77_0.musicData.picture), True)

def var_0_0.changeLocalpos(arg_78_0, arg_78_1):
	local var_78_0 = arg_78_0.music_amount_middle
	local var_78_1 = var_78_0 - arg_78_1
	local var_78_2 = 0.5
	local var_78_3 = {}

	for iter_78_0 = 1, arg_78_0.music_amount:
		var_78_3[iter_78_0] = arg_78_0.song_btns[iter_78_0].localPosition

	local var_78_4 = {}

	for iter_78_1 = 1, arg_78_0.music_amount:
		var_78_4[iter_78_1] = arg_78_0.song_btns[iter_78_1].localScale

	arg_78_0.changeLocalpos_timer = Timer.New(function()
		var_78_2 = var_78_2 - arg_78_0.time_interval
		arg_78_0.changeLocalposTimerflag = True

		for iter_79_0 = 1, arg_78_0.music_amount:
			local var_79_0 = iter_79_0 + var_78_1

			if iter_79_0 + var_78_1 > arg_78_0.music_amount:
				var_79_0 = iter_79_0 + var_78_1 - arg_78_0.music_amount

			if iter_79_0 + var_78_1 < 1:
				var_79_0 = iter_79_0 + var_78_1 + arg_78_0.music_amount

			if var_78_2 <= 0:
				if var_79_0 == var_78_0:
					arg_78_0.song_btns[iter_79_0].GetComponent(typeof(Animator)).Play("plate_out")
				else
					arg_78_0.song_btns[iter_79_0].GetComponent(typeof(Animator)).Play("plate_static")

					arg_78_0.song_btns[iter_79_0].GetComponent(typeof(Button)).interactable = True
			else
				arg_78_0.song_btns[iter_79_0].GetComponent(typeof(Animator)).Play("plate_static")

				arg_78_0.song_btns[iter_79_0].GetComponent(typeof(Button)).interactable = False

			local var_79_1 = arg_78_0.song_btn.localPosition
			local var_79_2 = math.abs(var_79_0 - var_78_0)
			local var_79_3 = (var_79_1.x + (var_79_0 - var_78_0 > 0 and 1 or -1) * var_79_2 * 1022) * (1 - var_78_2 * 2) + var_78_3[iter_79_0].x * var_78_2 * 2

			arg_78_0.song_btns[iter_79_0].localPosition = Vector3(var_79_3, var_79_1.y, var_79_1.z)

			local var_79_4 = arg_78_0.song_btns[iter_79_0].localScale
			local var_79_5 = (1 - var_79_2 * 0.2) * (1 - var_78_2 * 2) + var_78_4[iter_79_0].x * var_78_2 * 2

			arg_78_0.song_btns[iter_79_0].localScale = Vector3(var_79_5, var_79_5, var_79_5)

			local var_79_6 = arg_78_0.song_btns[iter_79_0].Find("song").GetComponent(typeof(Image))
			local var_79_7 = (1 - var_79_2 * 0.6) * (1 - var_78_2 * 2) + var_79_6.color.a * var_78_2 * 2

			var_79_6.color = Color.New(1, 1, 1, 1 - var_79_2 * 0.6)

		if var_78_2 <= 0:
			arg_78_0.changeLocalposTimerflag = False

			arg_78_0.changeLocalpos_timer.Stop(), arg_78_0.time_interval, -1)

	arg_78_0.changeLocalpos_timer.Start()

def var_0_0.addRingDragListenter(arg_80_0):
	local var_80_0 = GetOrAddComponent(arg_80_0.selectview, "EventTriggerListener")
	local var_80_1
	local var_80_2 = 0
	local var_80_3

	var_80_0.AddBeginDragFunc(function()
		var_80_2 = 0
		var_80_1 = None)
	var_80_0.AddDragFunc(function(arg_82_0, arg_82_1)
		if not arg_80_0.inPaintingView:
			local var_82_0 = arg_82_1.position

			if not var_80_1:
				var_80_1 = var_82_0

			var_80_2 = var_82_0.x - var_80_1.x)
	var_80_0.AddDragEndFunc(function(arg_83_0, arg_83_1)
		if not arg_80_0.inPaintingView and not arg_80_0.changeLocalposTimerflag:
			local var_83_0, var_83_1 = arg_80_0.getNextPreSelectId()

			if var_80_2 < -50:
				triggerButton(arg_80_0.song_btns[var_83_0])
			elif var_80_2 > 50:
				triggerButton(arg_80_0.song_btns[var_83_1]))

def var_0_0.getNextPreSelectId(arg_84_0):
	local var_84_0
	local var_84_1
	local var_84_2 = arg_84_0.game_music + 1
	local var_84_3 = arg_84_0.game_music - 1

	if var_84_3 <= 0:
		var_84_3 = #arg_84_0.musicDatas

	if var_84_2 > #arg_84_0.musicDatas:
		var_84_2 = 1

	for iter_84_0, iter_84_1 in ipairs(arg_84_0.musicDatas):
		if arg_84_0.musicDatas[iter_84_0].id == var_84_2:
			var_84_0 = iter_84_0

		if arg_84_0.musicDatas[iter_84_0].id == var_84_3:
			var_84_1 = iter_84_0

	return var_84_0, var_84_1

def var_0_0.Firstshow(arg_85_0, arg_85_1, arg_85_2, arg_85_3):
	arg_85_0.count = 0

	setActive(arg_85_1, True)
	LoadSpriteAtlasAsync("ui/musicgameother_atlas", "help1", function(arg_86_0)
		GetComponent(findTF(arg_85_0.firstview, "num/img1"), typeof(Image)).sprite = arg_86_0)
	LoadSpriteAtlasAsync("ui/musicgameother_atlas", "help2", function(arg_87_0)
		GetComponent(findTF(arg_85_0.firstview, "num/img2"), typeof(Image)).sprite = arg_87_0)

	for iter_85_0 = 1, 2:
		local var_85_0 = findTF(arg_85_1, "num/img" .. iter_85_0)

		setActive(var_85_0, iter_85_0 == arg_85_3 and True or False)

	if arg_85_0.firstview_timer:
		if arg_85_0.firstview_timer.running:
			arg_85_0.firstview_timer.Stop()

		arg_85_0.firstview_timer = None

	arg_85_0.firstview_timerRunflag = True
	arg_85_0.firstview_timer = Timer.New(function()
		arg_85_0.count = arg_85_0.count + 1

		if arg_85_0.count > 3:
			onButton(arg_85_0, arg_85_0.firstview, function()
				if arg_85_2:
					arg_85_2()

				arg_85_0.firstview_timer.Stop()
				setActive(arg_85_1, False)

				arg_85_0.firstview_timerRunflag = False

				removeOnButton(arg_85_0.firstview)), 1, -1)

	arg_85_0.firstview_timer.Start()

def var_0_0.updatSelectview(arg_90_0):
	if not arg_90_0.song_btns or #arg_90_0.song_btns <= 0 or not arg_90_0.selectview:
		return

	setActive(arg_90_0.selectview.Find("top/Speedlist/x" .. arg_90_0.game_speed), True)

	for iter_90_0 = 1, arg_90_0.music_amount:
		local var_90_0 = arg_90_0.musicDatas[iter_90_0].id

		setActive(arg_90_0.song_btns[var_90_0].Find("song/best"), False)
		arg_90_0.setSelectview_pj("e", var_90_0)

	local var_90_1 = arg_90_0.game_dgree
	local var_90_2 = arg_90_0.game_music
	local var_90_3 = arg_90_0.bestScorelist[var_90_2 + (var_90_1 - 1) * arg_90_0.music_amount]

	if arg_90_0.song_btns[var_90_2] and var_90_3 > 0:
		setActive(arg_90_0.song_btns[var_90_2].Find("song/best"), True)

		local var_90_4 = arg_90_0.song_btns[var_90_2].Find("song/best/score")

		setText(var_90_4, var_90_3)
		arg_90_0.setSelectview_pj("e", var_90_2)

		if var_90_3 < arg_90_0.score_blist[var_90_1]:
			arg_90_0.setSelectview_pj("c", var_90_2)
		elif var_90_3 >= arg_90_0.score_blist[var_90_1] and var_90_3 < arg_90_0.score_alist[var_90_1]:
			arg_90_0.setSelectview_pj("b", var_90_2)
		elif var_90_3 >= arg_90_0.score_alist[var_90_1] and var_90_3 < arg_90_0.score_slist[var_90_1]:
			arg_90_0.setSelectview_pj("a", var_90_2)
		else
			arg_90_0.setSelectview_pj("s", var_90_2)

def var_0_0.setSelectview_pj(arg_91_0, arg_91_1, arg_91_2):
	if arg_91_1 == "e":
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/c"), False)
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/b"), False)
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/a"), False)
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/s"), False)
	elif arg_91_1 == "c":
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/c"), True)
	elif arg_91_1 == "b":
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/b"), True)
	elif arg_91_1 == "a":
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/a"), True)
	elif arg_91_1 == "s":
		setActive(arg_91_0.song_btns[arg_91_2].Find("song/s"), True)

def var_0_0.updateScoreUIContent(arg_92_0):
	local var_92_0 = findTF(arg_92_0.scoreview, "ui")

	for iter_92_0 = 1, var_92_0.childCount:
		local var_92_1 = var_92_0.GetChild(iter_92_0 - 1)

		setActive(var_92_1, False)

	if arg_92_0.musicData.settlement_type and arg_92_0.musicData.settlement_type != "":
		arg_92_0.scoreUIContent = findTF(arg_92_0.scoreview, "ui/" .. arg_92_0.musicData.settlement_type)
	else
		arg_92_0.scoreUIContent = findTF(arg_92_0.scoreview, "ui/normal")

	setActive(arg_92_0.scoreUIContent, True)

def var_0_0.locadScoreView(arg_93_0):
	arg_93_0.updateScoreUIContent()
	arg_93_0.effect_play("nothing")

	arg_93_0.game_playingflag = False

	setActive(arg_93_0.scoreview, True)

	arg_93_0.scoreview_flag = True

	local var_93_0 = findTF(arg_93_0.scoreview, "bg")

	setImageColor(var_93_0, Color(0, 0, 0))
	LoadSpriteAtlasAsync("ui/musicgameother_atlas", "scoreBg" .. arg_93_0.musicBg, function(arg_94_0)
		if var_93_0:
			GetComponent(var_93_0, typeof(Image)).sprite = arg_94_0

			setImageColor(var_93_0, Color(1, 1, 1))
			setActive(var_93_0, True))
	setActive(arg_93_0.game_content.Find("combo"), False)
	setActive(arg_93_0.game_content.Find("MusicStar"), False)
	setActive(arg_93_0.game_content.Find("combo_n"), False)
	setActive(arg_93_0.game_content, False)
	setActive(arg_93_0.top, False)
	setActive(arg_93_0._tf.Find("Spinelist"), False)

	local var_93_1 = arg_93_0.scoreview.Find("maskBg").childCount

	for iter_93_0 = 1, var_93_1:
		setActive(arg_93_0.scoreview.Find("maskBg/bg" .. iter_93_0), iter_93_0 == arg_93_0.musicBg)

	local var_93_2 = arg_93_0.scoreview.Find("maskBgBottom").childCount

	for iter_93_1 = 1, var_93_2:
		local var_93_3 = iter_93_1 == arg_93_0.musicBg

		setActive(arg_93_0.scoreview.Find("maskBgBottom/bg" .. iter_93_1), var_93_3)

	local var_93_4 = arg_93_0.game_dgree
	local var_93_5 = arg_93_0.game_music

	if arg_93_0.painting:
		retPaintingPrefab(arg_93_0.scoreview.Find("paint"), arg_93_0.painting)

	local var_93_6 = {}

	for iter_93_2 = 1, #arg_93_0.settlementPainting:
		if arg_93_0.settlementPainting[iter_93_2] and arg_93_0.settlementPainting[iter_93_2] != "" and arg_93_0.settlementPainting[iter_93_2] != "none":
			table.insert(var_93_6, arg_93_0.settlementPainting[iter_93_2])

	arg_93_0.painting = var_93_6[math.random(1, #var_93_6)]

	local var_93_7 = MusicGameConst.painting_const_key[string.lower(arg_93_0.painting)]

	if var_93_7:
		local var_93_8 = {}

		PaintingConst.AddPaintingNameWithFilteMap(var_93_8, var_93_7)
		PaintingConst.PaintingDownload({
			isShowBox = False,
			paintingNameList = var_93_8,
			def finishFunc:()
				setPaintingPrefabAsync(arg_93_0.scoreview.Find("paint"), arg_93_0.painting, "mainNormal")
		})
	else
		setPaintingPrefabAsync(arg_93_0.scoreview.Find("paint"), arg_93_0.painting, "mainNormal")

	setActive(arg_93_0.scoreUIContent.Find("scoreImg/square/easy"), var_93_4 == 1)
	setActive(arg_93_0.scoreUIContent.Find("scoreImg/square/hard"), var_93_4 == 2)
	setActive(arg_93_0.scoreUIContent.Find("scoreList/fullCombo"), arg_93_0.miss_number == 0)
	setActive(arg_93_0.scoreUIContent.Find("scoreImg/perfect/noMiss"), arg_93_0.miss_number == 0 and arg_93_0.good_number == 0)

	local function var_93_9(arg_96_0, arg_96_1, arg_96_2)
		LeanTween.value(go(arg_93_0.scoreview), 0, arg_96_1, 0.6).setOnUpdate(System.Action_float(function(arg_97_0)
			setText(arg_96_0, math.round(arg_97_0)))).setOnComplete(System.Action(function()
			arg_96_2()))

	seriesAsync({
		function(arg_99_0)
			var_93_9(arg_93_0.scoreUIContent.Find("scoreList/perfect"), arg_93_0.perfect_number, arg_99_0),
		function(arg_100_0)
			var_93_9(arg_93_0.scoreUIContent.Find("scoreList/good"), arg_93_0.good_number, arg_100_0),
		function(arg_101_0)
			var_93_9(arg_93_0.scoreUIContent.Find("scoreList/miss"), arg_93_0.miss_number, arg_101_0),
		function(arg_102_0)
			var_93_9(arg_93_0.scoreUIContent.Find("scoreList/combo"), arg_93_0.combo_number, arg_102_0),
		function(arg_103_0)
			local var_103_0 = arg_93_0.bestScorelist[var_93_5 + (var_93_4 - 1) * arg_93_0.music_amount]

			if not var_103_0 or var_103_0 == 0:
				var_103_0 = arg_93_0.score_number

			if arg_93_0.score_number > arg_93_0.bestScorelist[var_93_5 + (var_93_4 - 1) * arg_93_0.music_amount]:
				setActive(arg_93_0.scoreUIContent.Find("scoreImg/square/newScore"), True)

				arg_93_0.bestScorelist[var_93_5 + (var_93_4 - 1) * arg_93_0.music_amount] = arg_93_0.score_number
			else
				setActive(arg_93_0.scoreUIContent.Find("scoreImg/square/newScore"), False)

			var_93_9(arg_93_0.scoreUIContent.Find("scoreImg/square/bestscore"), var_103_0, arg_103_0)
			var_93_9(arg_93_0.scoreUIContent.Find("scoreImg/square/score"), arg_93_0.score_number, function()
				return)
			arg_93_0.MyStoreDataToServer()
			arg_93_0.MyGetRuntimeData(),
		function(arg_105_0)
			local var_105_0

			if arg_93_0.score_number < arg_93_0.score_blist[var_93_4]:
				function var_105_0()
					arg_93_0.setScoceview_pj("c")
			elif arg_93_0.score_number >= arg_93_0.score_blist[var_93_4] and arg_93_0.score_number < arg_93_0.score_alist[var_93_4]:
				function var_105_0()
					arg_93_0.setScoceview_pj("b")
					arg_93_0.emit(BaseMiniGameMediator.MINI_GAME_SUCCESS, 0)
			elif arg_93_0.score_number >= arg_93_0.score_alist[var_93_4] and arg_93_0.score_number < arg_93_0.score_slist[var_93_4]:
				function var_105_0()
					arg_93_0.setScoceview_pj("a")
					arg_93_0.emit(BaseMiniGameMediator.MINI_GAME_SUCCESS, 0)
			else
				function var_105_0()
					arg_93_0.setScoceview_pj("s")
					arg_93_0.emit(BaseMiniGameMediator.MINI_GAME_SUCCESS, 0)

			local var_105_1 = arg_93_0.GetMGHubData()
			local var_105_2 = pg.NewStoryMgr.GetInstance()
			local var_105_3 = arg_93_0.GetMGData().getConfig("simple_config_data").story
			local var_105_4 = var_105_3[var_105_1.usedtime + 1] and var_105_3[var_105_1.usedtime + 1][1] or None

			if var_105_1.count > 0 and var_105_4 and not var_105_2.IsPlayed(var_105_4) and arg_93_0.score_number >= arg_93_0.score_blist[var_93_4]:
				var_105_2.Play(var_105_4, var_105_0)
			else
				var_105_0()

			arg_105_0()
	}, function()
		return)

	local var_93_10 = arg_93_0.scoreUIContent.Find("scoreImg/square/nameText")

	setText(var_93_10, arg_93_0.musicData.music_name)

	local var_93_11 = arg_93_0.scoreUIContent.Find("scoreImg/square/name").GetComponent(typeof(Image))

	var_93_11.sprite = arg_93_0.selectview.Find("Main/namelist/song" .. arg_93_0.musicData.picture).GetComponent(typeof(Image)).sprite

	var_93_11.SetNativeSize()

	arg_93_0.scoreUIContent.Find("scoreImg/square/song").GetComponent(typeof(Image)).sprite = arg_93_0.selectview.Find("Main/MusicList/img/" .. arg_93_0.musicData.picture).GetComponent(typeof(Image)).sprite

	GetComponent(arg_93_0.scoreUIContent.Find("btnList/share"), typeof(Image)).SetNativeSize()
	onButton(arg_93_0, arg_93_0.scoreUIContent.Find("btnList/share"), function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeSummary), SFX_PANEL)
	GetComponent(arg_93_0.scoreUIContent.Find("btnList/restart"), typeof(Image)).SetNativeSize()
	onButton(arg_93_0, arg_93_0.scoreUIContent.Find("btnList/restart"), function()
		setActive(arg_93_0.scoreview, False)

		arg_93_0.scoreview_flag = False

		arg_93_0.stopTimer()
		arg_93_0.rec_scorce()
		arg_93_0.game_start()
		arg_93_0.setScoceview_pj("e")

		if arg_93_0.painting:
			retPaintingPrefab(arg_93_0.scoreview.Find("paint"), arg_93_0.painting)

			arg_93_0.painting = None, SFX_UI_CLICK)
	GetComponent(arg_93_0.scoreUIContent.Find("btnList/reselect"), typeof(Image)).SetNativeSize()
	onButton(arg_93_0, arg_93_0.scoreUIContent.Find("btnList/reselect"), function()
		arg_93_0.dynamicBgHandler(arg_93_0.bgGo)
		setActive(arg_93_0.scoreview, False)

		arg_93_0.scoreview_flag = False

		arg_93_0.stopTimer()
		setActive(arg_93_0.selectview, True)

		GetOrAddComponent(arg_93_0.selectview, "CanvasGroup").blocksRaycasts = True

		arg_93_0.updatSelectview()
		arg_93_0.song_btns[arg_93_0.game_music].GetComponent(typeof(Animator)).Play("plate_out")
		arg_93_0.loadAndPlayMusic()
		arg_93_0.rec_scorce()
		arg_93_0.setScoceview_pj("e")

		if arg_93_0.painting:
			retPaintingPrefab(arg_93_0.scoreview.Find("paint"), arg_93_0.painting)

			arg_93_0.painting = None, SFX_UI_CLICK)

def var_0_0.setScoceview_pj(arg_114_0, arg_114_1):
	setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/c"), False)
	setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/b"), False)
	setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/a"), False)
	setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/s"), False)

	if arg_114_1 == "e":
		-- block empty
	elif arg_114_1 == "c":
		setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/c"), True)
	elif arg_114_1 == "b":
		setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/b"), True)
	elif arg_114_1 == "a":
		setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/a"), True)
	elif arg_114_1 == "s":
		setActive(arg_114_0.scoreUIContent.Find("scoreImg/square/s"), True)

def var_0_0.Scoceview_ani(arg_115_0):
	local var_115_0 = 0

	setActive(arg_115_0.scoreUIContent.Find("btnList/reselect"), False)
	setActive(arg_115_0.scoreUIContent.Find("btnList/restart"), False)
	setActive(arg_115_0.scoreUIContent.Find("btnList/share"), False)

	local function var_115_1()
		var_115_0 = var_115_0 + arg_115_0.time_interval

		if var_115_0 >= 0.99:
			setActive(arg_115_0.scoreUIContent.Find("btnList/reselect"), True)
			setActive(arg_115_0.scoreUIContent.Find("btnList/restart"), True)
			setActive(arg_115_0.scoreUIContent.Find("btnList/share"), True)
			setText(arg_115_0.scoreUIContent.Find("scoreList/perfect"), arg_115_0.perfect_number)
			setText(arg_115_0.scoreUIContent.Find("scoreList/good"), arg_115_0.good_number)
			setText(arg_115_0.scoreUIContent.Find("scoreList/miss"), arg_115_0.miss_number)
			setText(arg_115_0.scoreUIContent.Find("scoreList/combo"), arg_115_0.combo_number)
			setText(arg_115_0.scoreUIContent.Find("scoreImg/square/bestscore"), arg_115_0.score_number)
		else
			setText(arg_115_0.scoreUIContent.Find("scoreList/perfect"), math.floor(arg_115_0.perfect_number * var_115_0))
			setText(arg_115_0.scoreUIContent.Find("scoreList/good"), math.floor(arg_115_0.good_number * var_115_0))
			setText(arg_115_0.scoreUIContent.Find("scoreList/miss"), math.floor(arg_115_0.miss_number * var_115_0))
			setText(arg_115_0.scoreUIContent.Find("scoreList/combo"), math.floor(arg_115_0.combo_number * var_115_0))
			setText(arg_115_0.scoreUIContent.Find("scoreImg/square/bestscore"), math.floor(arg_115_0.score_number * var_115_0))

		if var_115_0 >= 1.03:
			arg_115_0.Scoceview_timer.Stop()

	arg_115_0.Scoceview_timer = Timer.New(var_115_1, arg_115_0.time_interval, -1)

	arg_115_0.Scoceview_timer.Start()

def var_0_0.gameStart(arg_117_0):
	if not arg_117_0.timer:
		arg_117_0.timer = Timer.New(function()
			arg_117_0.gameStepNew(), arg_117_0.time_interval, -1)

	arg_117_0.aheadtime_count = 0

	local var_117_0 = 2

	arg_117_0.ahead_timerPauseFlag = False

	local function var_117_1()
		arg_117_0.ahead_timeflag = True

		if not arg_117_0.timer.running:
			arg_117_0.startTimer()

		if not arg_117_0.ahead_timerPauseFlag:
			arg_117_0.aheadtime_count = arg_117_0.aheadtime_count + arg_117_0.time_interval

			if arg_117_0.aheadtime_count > var_117_0:
				arg_117_0.aheadtime_count = None
				arg_117_0.ahead_timeflag = False
				arg_117_0.gotspecialcombo_flag = False

				arg_117_0.ahead_timer.Stop()
				arg_117_0.loadAndPlayMusic(function()
					return)

	CriWareMgr.Inst.UnloadCueSheet(arg_117_0.getMusicBgm(arg_117_0.musicData))

	arg_117_0.ahead_timer = Timer.New(var_117_1, arg_117_0.time_interval, -1)

	arg_117_0.count_five(function()
		arg_117_0.ahead_timer.Start())

def var_0_0.getMusicBgm(arg_122_0, arg_122_1):
	local var_122_0 = "bgm-song"

	if arg_122_1.bgm < 10:
		var_122_0 = var_122_0 .. "0" .. tostring(arg_122_1.bgm)
	else
		var_122_0 = var_122_0 .. tostring(arg_122_1.bgm)

	return var_122_0

def var_0_0.getMusicNote(arg_123_0, arg_123_1, arg_123_2):
	return "view/miniGame/gameView/musicGame/bgm_song" .. "0" .. arg_123_1.note .. "_" .. arg_123_2

def var_0_0.gameStepNew(arg_124_0):
	local var_124_0 = arg_124_0.game_dgree

	arg_124_0.gameStepTime = arg_124_0.getStampTime()
	arg_124_0.downingright_lastflag = arg_124_0.downingright_flag
	arg_124_0.downingleft_lastflag = arg_124_0.downingleft_flag

	if IsUnityEditor:
		if var_124_0 == 2:
			arg_124_0.downingright_flag = Input.GetKey(KeyCode.J)
			arg_124_0.downingleft_flag = Input.GetKey(KeyCode.F)
		elif var_124_0 == 1:
			if Input.GetKey(KeyCode.J) or Input.GetKey(KeyCode.F):
				arg_124_0.downingright_flag = True
				arg_124_0.downingleft_flag = True
			else
				arg_124_0.downingright_flag = False
				arg_124_0.downingleft_flag = False
	elif var_124_0 == 2:
		arg_124_0.downingright_flag = arg_124_0.mousedowningright_flag
		arg_124_0.downingleft_flag = arg_124_0.mousedowningleft_flag
	elif var_124_0 == 1:
		if arg_124_0.mousedowningright_flag or arg_124_0.mousedowningleft_flag:
			arg_124_0.downingright_flag = True
			arg_124_0.downingleft_flag = True
		else
			arg_124_0.downingright_flag = False
			arg_124_0.downingleft_flag = False

	if var_124_0 == 2:
		if not arg_124_0.downingleft_lastflag and arg_124_0.downingleft_flag:
			arg_124_0.gameNoteLeft.onKeyDown()

			arg_124_0.leftDownStepTime = arg_124_0.gameStepTime

			if arg_124_0.rightDownStepTime and math.abs(arg_124_0.leftDownStepTime - arg_124_0.rightDownStepTime) < 100:
				arg_124_0.gameNoteLeft.bothDown()
				arg_124_0.gameNoteRight.bothDown()
		elif arg_124_0.downingleft_lastflag and not arg_124_0.downingleft_flag:
			arg_124_0.leftUpStepTime = arg_124_0.gameStepTime

			arg_124_0.gameNoteLeft.onKeyUp()

			if arg_124_0.rightUpStepTime and math.abs(arg_124_0.leftUpStepTime - arg_124_0.rightUpStepTime) < 100:
				arg_124_0.gameNoteLeft.bothUp()
				arg_124_0.gameNoteRight.bothUp()

		if not arg_124_0.downingright_lastflag and arg_124_0.downingright_flag:
			arg_124_0.gameNoteRight.onKeyDown()

			arg_124_0.rightDownStepTime = arg_124_0.gameStepTime

			if arg_124_0.leftDownStepTime and math.abs(arg_124_0.leftDownStepTime - arg_124_0.rightDownStepTime) < 200:
				arg_124_0.gameNoteLeft.bothDown()
				arg_124_0.gameNoteRight.bothDown()
		elif arg_124_0.downingright_lastflag and not arg_124_0.downingright_flag:
			arg_124_0.rightUpStepTime = arg_124_0.gameStepTime

			arg_124_0.gameNoteRight.onKeyUp()

			if arg_124_0.leftUpStepTime and math.abs(arg_124_0.leftUpStepTime - arg_124_0.rightUpStepTime) < 200:
				arg_124_0.gameNoteLeft.bothUp()
				arg_124_0.gameNoteRight.bothUp()
	elif not arg_124_0.downingright_lastflag and arg_124_0.downingright_flag:
		arg_124_0.gameNoteLeft.onKeyDown()
		arg_124_0.gameNoteRight.onKeyDown()
	elif arg_124_0.downingleft_lastflag and not arg_124_0.downingleft_flag:
		arg_124_0.gameNoteLeft.onKeyUp()
		arg_124_0.gameNoteRight.onKeyUp()

	arg_124_0.musicgame_lasttime = arg_124_0.musicgame_nowtime or 0

	if arg_124_0.criInfo:
		arg_124_0.musicgame_nowtime = arg_124_0.getStampTime() / 1000
	else
		arg_124_0.musicgame_nowtime = 0

	if arg_124_0.song_Tlength and not arg_124_0.scoreview_flag and long2int(arg_124_0.song_Tlength) / 1000 - arg_124_0.musicgame_nowtime <= 0.01666:
		print("歌曲播放结束")
		arg_124_0.pauseBgm()

		arg_124_0.game_playingflag = False

		local function var_124_1()
			arg_124_0.locadScoreView()

		if arg_124_0.perfect_number > 0 and arg_124_0.good_number == 0 and arg_124_0.miss_number == 0:
			setActive(arg_124_0.fullComboEffect, True)

			if not arg_124_0.gotspecialcombo_flag:
				arg_124_0.score_number = arg_124_0.score_number + arg_124_0.specialscore_number
				arg_124_0.gotspecialcombo_flag = True

			LeanTween.delayedCall(go(arg_124_0.fullComboEffect), 2, System.Action(function()
				var_124_1()))
		elif (arg_124_0.good_number > 0 or arg_124_0.perfect_number > 0) and arg_124_0.miss_number <= 0:
			setActive(arg_124_0.fullComboEffect, True)

			if not arg_124_0.gotspecialcombo_flag:
				arg_124_0.score_number = arg_124_0.score_number + arg_124_0.specialscore_number
				arg_124_0.gotspecialcombo_flag = True

			LeanTween.delayedCall(go(arg_124_0.fullComboEffect), 2, System.Action(function()
				var_124_1()))
		else
			setActive(arg_124_0.liveClearEffect, True)
			LeanTween.delayedCall(go(arg_124_0.liveClearEffect), 2, System.Action(function()
				var_124_1()))

		return

	arg_124_0.gameNoteLeft.step(arg_124_0.gameStepTime)
	arg_124_0.gameNoteRight.step(arg_124_0.gameStepTime)
	arg_124_0.scoresliderAcombo_update()

	if arg_124_0.drumpFlag and not arg_124_0.gameNoteLeft.loopTime() and not arg_124_0.gameNoteRight.loopTime():
		arg_124_0.drumpFlag = False
		arg_124_0.drupTime = Time.realtimeSinceStartup

		arg_124_0.setActionSDmodel("jump")
		LeanTween.delayedCall(go(arg_124_0.game_content), 1, System.Action(function()
			arg_124_0.setActionSDmodel("idol")))

def var_0_0.onStateCallback(arg_130_0, arg_130_1):
	arg_130_0.score_update(arg_130_1)

def var_0_0.onLongTimeCallback(arg_131_0, arg_131_1):
	if arg_131_0.drupTime and Time.realtimeSinceStartup - arg_131_0.drupTime < 2:
		return

	if arg_131_1 > 0.5:
		arg_131_0.drumpFlag = True

return var_0_0
