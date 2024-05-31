local var_0_0 = class("CryptolaliaVedioPlayer")
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5

local function var_0_6(arg_1_0)
	return PathMgr.getAssetBundle("originsource/cipher/" .. arg_1_0 .. ".txt")
end

local function var_0_7(arg_2_0)
	return PathMgr.getAssetBundle("originsource/cipher/" .. arg_2_0 .. ".cpk")
end

function var_0_0.Ctor(arg_3_0, arg_3_1)
	pg.DelegateInfo.New(arg_3_0)

	arg_3_0.root = arg_3_1
	arg_3_0.state = var_0_1

	if not arg_3_0.handle then
		arg_3_0.handle = UpdateBeat:CreateListener(arg_3_0.Update, arg_3_0)
	end

	arg_3_0.text = nil
	arg_3_0.subtile = nil
	arg_3_0.player = nil

	UpdateBeat:AddListener(arg_3_0.handle)
end

function var_0_0.Play(arg_4_0, arg_4_1, arg_4_2)
	if not arg_4_0:CheckCpkAndSubtitle(arg_4_1, next) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("Resource does not exist"))

		return
	end

	arg_4_0.onExit = arg_4_2

	seriesAsync({
		function(arg_5_0)
			arg_4_0:DownloadCpkAndSubtitle(arg_4_1, arg_5_0)
		end,
		function(arg_6_0)
			arg_4_0:LoadVedioPlayer(arg_4_1, arg_6_0)
		end
	}, function()
		arg_4_0:RegisterEvent()
	end)
end

function var_0_0.RegisterEvent(arg_8_0)
	onButton(arg_8_0, arg_8_0.playBtn, function()
		if not arg_8_0.player then
			return
		end

		arg_8_0:_Play()
	end, SFX_PANEL)
	onButton(arg_8_0, arg_8_0.backBtn, function()
		if not arg_8_0.player then
			return
		end

		if arg_8_0.onExit then
			arg_8_0.onExit()
		end

		arg_8_0:Stop()
	end, SFX_PANEL)
	onButton(arg_8_0, arg_8_0._go, function()
		arg_8_0:Pause()
	end, SFX_PANEL)
end

function var_0_0._Play(arg_12_0)
	if arg_12_0.state == var_0_3 then
		arg_12_0.player:Pause(false)
	elseif arg_12_0.state == var_0_4 then
		arg_12_0.subtile = Clone(arg_12_0.subtileBackUp)

		arg_12_0.player.player:SetSeekPosition(0)
		arg_12_0.player.player:Start()
	else
		arg_12_0.subtile = Clone(arg_12_0.subtileBackUp)

		arg_12_0.player:PlayCpk()
	end

	setActive(arg_12_0.playBtn, false)
	setActive(arg_12_0.backBtn, false)

	arg_12_0.state = var_0_2
end

function var_0_0.Pause(arg_13_0)
	if arg_13_0.state ~= var_0_2 then
		return
	end

	arg_13_0.state = var_0_3

	setActive(arg_13_0.playBtn, true)
	arg_13_0.player:Pause(true)
	setActive(arg_13_0.backBtn, true)
end

function var_0_0.Stop(arg_14_0)
	arg_14_0:Dispose()

	arg_14_0.state = var_0_5
end

function var_0_0.CheckCpkAndSubtitle(arg_15_0, arg_15_1, arg_15_2)
	return PathMgr.FileExists(var_0_7(arg_15_1)) and PathMgr.FileExists(var_0_6(arg_15_1))
end

function var_0_0.DownloadCpkAndSubtitle(arg_16_0, arg_16_1, arg_16_2)
	arg_16_2()
end

local function var_0_8(arg_17_0)
	local var_17_0 = var_0_6(arg_17_0)
	local var_17_1 = PathMgr.ReadAllLines(var_17_0)
	local var_17_2 = {}

	for iter_17_0 = 1, var_17_1.Length do
		local var_17_3 = var_17_1[iter_17_0 - 1]
		local var_17_4 = string.match(var_17_3, "#%d+#%d+$")
		local var_17_5 = string.split(var_17_4, "#")
		local var_17_6 = var_17_5[2]
		local var_17_7 = var_17_5[3]
		local var_17_8 = string.gsub(var_17_3, var_17_4, "")

		table.insert(var_17_2, {
			startTime = tonumber(var_17_6),
			endTime = tonumber(var_17_7),
			content = var_17_8
		})
	end

	return var_17_2
end

function var_0_0.LoadVedioPlayer(arg_18_0, arg_18_1, arg_18_2)
	ResourceMgr.Inst:getAssetAsync("Cryptolalia/" .. arg_18_1, arg_18_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_19_0)
		local var_19_0 = Object.Instantiate(arg_19_0, arg_18_0.root)

		arg_18_0.text = var_19_0.transform:Find("Text"):GetComponent(typeof(Text))
		arg_18_0.subtileBackUp = var_0_8(arg_18_1)
		arg_18_0.player = var_19_0.transform:Find("cpk"):GetComponent(typeof(CriManaCpkUI))
		arg_18_0.playBtn = var_19_0.transform:Find("play")
		arg_18_0.backBtn = var_19_0.transform:Find("back")
		arg_18_0._go = var_19_0

		arg_18_0:_Play()
		arg_18_2()
	end), true, true)
end

function var_0_0.OnPlayEnd(arg_20_0)
	arg_20_0.player.player.frameInfo.frameNo = 0
	arg_20_0.state = var_0_4

	setActive(arg_20_0.playBtn, true)
	setActive(arg_20_0.backBtn, true)
end

local function var_0_9(arg_21_0)
	if not arg_21_0.frameInfo then
		return 0
	end

	local var_21_0 = arg_21_0.frameInfo

	return var_21_0.frameNo / var_21_0.framerateN / var_21_0.framerateD * 1000000
end

local function var_0_10(arg_22_0, arg_22_1)
	if not arg_22_0 or #arg_22_0 <= 0 then
		return ""
	end

	local var_22_0 = arg_22_0[1]

	if arg_22_1 >= var_22_0.startTime and arg_22_1 <= var_22_0.endTime then
		table.remove(arg_22_0, 1)

		return var_22_0.content, var_22_0.endTime
	elseif arg_22_1 > var_22_0.startTime and arg_22_1 > var_22_0.endTime then
		table.remove(arg_22_0, 1)
	end

	return ""
end

function var_0_0.Update(arg_23_0)
	if arg_23_0.text == nil or arg_23_0.subtile == nil or arg_23_0.player == nil or arg_23_0.player.player.frameInfo == nil then
		return
	end

	if arg_23_0.state == var_0_3 or arg_23_0.state == var_0_4 then
		return
	end

	if arg_23_0.player.player.frameInfo.frameNo >= arg_23_0.player.player.movieInfo.totalFrames - 1 then
		arg_23_0:OnPlayEnd()

		return
	end

	local var_23_0 = var_0_9(arg_23_0.player.player)
	local var_23_1, var_23_2 = var_0_10(arg_23_0.subtile, var_23_0)

	if var_23_1 and var_23_1 ~= "" then
		arg_23_0.hideTime = var_23_2
		arg_23_0.text.text = var_23_1

		setActive(arg_23_0.text.gameObject, true)
	elseif arg_23_0.hideTime and var_23_0 >= arg_23_0.hideTime then
		arg_23_0.text.text = ""
		arg_23_0.hideTime = nil

		setActive(arg_23_0.text.gameObject, false)
	end
end

function var_0_0.Dispose(arg_24_0)
	if arg_24_0.state == var_0_5 then
		return
	end

	pg.DelegateInfo.Dispose(arg_24_0)

	if arg_24_0.player then
		arg_24_0.player:SetPlayEndHandler(nil)
		arg_24_0.player.player:Stop()
	end

	if arg_24_0.player and not IsNil(arg_24_0.player.gameObject) then
		Object.Destroy(arg_24_0.player.gameObject.transform.parent.gameObject)
	end

	arg_24_0.onExit = nil
	arg_24_0.text = nil
	arg_24_0.subtile = nil
	arg_24_0.player = nil
	arg_24_0.hideTime = nil

	if arg_24_0.handle then
		UpdateBeat:RemoveListener(arg_24_0.handle)
	end
end

return var_0_0
