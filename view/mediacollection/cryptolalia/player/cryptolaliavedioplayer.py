local var_0_0 = class("CryptolaliaVedioPlayer")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5

local function var_0_6(arg_1_0)
	return PathMgr.getAssetBundle("originsource/cipher/" .. arg_1_0 .. ".txt")

local function var_0_7(arg_2_0)
	return PathMgr.getAssetBundle("originsource/cipher/" .. arg_2_0 .. ".cpk")

def var_0_0.Ctor(arg_3_0, arg_3_1):
	pg.DelegateInfo.New(arg_3_0)

	arg_3_0.root = arg_3_1
	arg_3_0.state = var_0_1

	if not arg_3_0.handle:
		arg_3_0.handle = UpdateBeat.CreateListener(arg_3_0.Update, arg_3_0)

	arg_3_0.text = None
	arg_3_0.subtile = None
	arg_3_0.player = None

	UpdateBeat.AddListener(arg_3_0.handle)

def var_0_0.Play(arg_4_0, arg_4_1, arg_4_2):
	if not arg_4_0.CheckCpkAndSubtitle(arg_4_1, next):
		pg.TipsMgr.GetInstance().ShowTips(i18n("Resource:es not exist"))

		return

	arg_4_0.onExit = arg_4_2

	seriesAsync({
		function(arg_5_0)
			arg_4_0.DownloadCpkAndSubtitle(arg_4_1, arg_5_0),
		function(arg_6_0)
			arg_4_0.LoadVedioPlayer(arg_4_1, arg_6_0)
	}, function()
		arg_4_0.RegisterEvent())

def var_0_0.RegisterEvent(arg_8_0):
	onButton(arg_8_0, arg_8_0.playBtn, function()
		if not arg_8_0.player:
			return

		arg_8_0._Play(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.backBtn, function()
		if not arg_8_0.player:
			return

		if arg_8_0.onExit:
			arg_8_0.onExit()

		arg_8_0.Stop(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0._go, function()
		arg_8_0.Pause(), SFX_PANEL)

def var_0_0._Play(arg_12_0):
	if arg_12_0.state == var_0_3:
		arg_12_0.player.Pause(False)
	elif arg_12_0.state == var_0_4:
		arg_12_0.subtile = Clone(arg_12_0.subtileBackUp)

		arg_12_0.player.player.SetSeekPosition(0)
		arg_12_0.player.player.Start()
	else
		arg_12_0.subtile = Clone(arg_12_0.subtileBackUp)

		arg_12_0.player.PlayCpk()

	setActive(arg_12_0.playBtn, False)
	setActive(arg_12_0.backBtn, False)

	arg_12_0.state = var_0_2

def var_0_0.Pause(arg_13_0):
	if arg_13_0.state != var_0_2:
		return

	arg_13_0.state = var_0_3

	setActive(arg_13_0.playBtn, True)
	arg_13_0.player.Pause(True)
	setActive(arg_13_0.backBtn, True)

def var_0_0.Stop(arg_14_0):
	arg_14_0.Dispose()

	arg_14_0.state = var_0_5

def var_0_0.CheckCpkAndSubtitle(arg_15_0, arg_15_1, arg_15_2):
	return PathMgr.FileExists(var_0_7(arg_15_1)) and PathMgr.FileExists(var_0_6(arg_15_1))

def var_0_0.DownloadCpkAndSubtitle(arg_16_0, arg_16_1, arg_16_2):
	arg_16_2()

local function var_0_8(arg_17_0)
	local var_17_0 = var_0_6(arg_17_0)
	local var_17_1 = PathMgr.ReadAllLines(var_17_0)
	local var_17_2 = {}

	for iter_17_0 = 1, var_17_1.Length:
		local var_17_3 = var_17_1[iter_17_0 - 1]
		local var_17_4 = string.match(var_17_3, "#%d+#%d+$")
		local var_17_5 = string.split(var_17_4, "#")
		local var_17_6 = var_17_5[2]
		local var_17_7 = var_17_5[3]
		local var_17_8 = string.gsub(var_17_3, var_17_4, "")

		table.insert(var_17_2, {
			startTime = tonumber(var_17_6),Time = tonumber(var_17_7),
			content = var_17_8
		})

	return var_17_2

def var_0_0.LoadVedioPlayer(arg_18_0, arg_18_1, arg_18_2):
	ResourceMgr.Inst.getAssetAsync("Cryptolalia/" .. arg_18_1, arg_18_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_19_0)
		local var_19_0 = Object.Instantiate(arg_19_0, arg_18_0.root)

		arg_18_0.text = var_19_0.transform.Find("Text").GetComponent(typeof(Text))
		arg_18_0.subtileBackUp = var_0_8(arg_18_1)
		arg_18_0.player = var_19_0.transform.Find("cpk").GetComponent(typeof(CriManaCpkUI))
		arg_18_0.playBtn = var_19_0.transform.Find("play")
		arg_18_0.backBtn = var_19_0.transform.Find("back")
		arg_18_0._go = var_19_0

		arg_18_0._Play()
		arg_18_2()), True, True)

def var_0_0.OnPlayEnd(arg_20_0):
	arg_20_0.player.player.frameInfo.frameNo = 0
	arg_20_0.state = var_0_4

	setActive(arg_20_0.playBtn, True)
	setActive(arg_20_0.backBtn, True)

local function var_0_9(arg_21_0)
	if not arg_21_0.frameInfo:
		return 0

	local var_21_0 = arg_21_0.frameInfo

	return var_21_0.frameNo / var_21_0.framerateN / var_21_0.framerateD * 1000000

local function var_0_10(arg_22_0, arg_22_1)
	if not arg_22_0 or #arg_22_0 <= 0:
		return ""

	local var_22_0 = arg_22_0[1]

	if arg_22_1 >= var_22_0.startTime and arg_22_1 <= var_22_0.endTime:
		table.remove(arg_22_0, 1)

		return var_22_0.content, var_22_0.endTime
	elif arg_22_1 > var_22_0.startTime and arg_22_1 > var_22_0.endTime:
		table.remove(arg_22_0, 1)

	return ""

def var_0_0.Update(arg_23_0):
	if arg_23_0.text == None or arg_23_0.subtile == None or arg_23_0.player == None or arg_23_0.player.player.frameInfo == None:
		return

	if arg_23_0.state == var_0_3 or arg_23_0.state == var_0_4:
		return

	if arg_23_0.player.player.frameInfo.frameNo >= arg_23_0.player.player.movieInfo.totalFrames - 1:
		arg_23_0.OnPlayEnd()

		return

	local var_23_0 = var_0_9(arg_23_0.player.player)
	local var_23_1, var_23_2 = var_0_10(arg_23_0.subtile, var_23_0)

	if var_23_1 and var_23_1 != "":
		arg_23_0.hideTime = var_23_2
		arg_23_0.text.text = var_23_1

		setActive(arg_23_0.text.gameObject, True)
	elif arg_23_0.hideTime and var_23_0 >= arg_23_0.hideTime:
		arg_23_0.text.text = ""
		arg_23_0.hideTime = None

		setActive(arg_23_0.text.gameObject, False)

def var_0_0.Dispose(arg_24_0):
	if arg_24_0.state == var_0_5:
		return

	pg.DelegateInfo.Dispose(arg_24_0)

	if arg_24_0.player:
		arg_24_0.player.SetPlayEndHandler(None)
		arg_24_0.player.player.Stop()

	if arg_24_0.player and not IsNil(arg_24_0.player.gameObject):
		Object.Destroy(arg_24_0.player.gameObject.transform.parent.gameObject)

	arg_24_0.onExit = None
	arg_24_0.text = None
	arg_24_0.subtile = None
	arg_24_0.player = None
	arg_24_0.hideTime = None

	if arg_24_0.handle:
		UpdateBeat.RemoveListener(arg_24_0.handle)

return var_0_0
