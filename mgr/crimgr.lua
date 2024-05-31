pg = pg or {}

local var_0_0 = pg

var_0_0.CriMgr = singletonClass("CriMgr")

local var_0_1 = var_0_0.CriMgr

var_0_1.Category_CV = "Category_CV"
var_0_1.Category_BGM = "Category_BGM"
var_0_1.Category_SE = "Category_SE"
var_0_1.C_BGM = "C_BGM"
var_0_1.C_VOICE = "cv"
var_0_1.C_SE = "C_SE"
var_0_1.C_BATTLE_SE = "C_BATTLE_SE"
var_0_1.C_GALLERY_MUSIC = "C_GALLERY_MUSIC"
var_0_1.C_BATTLE_CV_EXTRA = "C_BATTLE_CV_EXTRA"
var_0_1.NEXT_VER = 40

function var_0_1.Init(arg_1_0, arg_1_1)
	print("initializing cri manager...")
	seriesAsync({
		function(arg_2_0)
			arg_1_0:InitCri(arg_2_0)
		end,
		function(arg_3_0)
			local var_3_0 = CueData.GetCueData()

			var_3_0.cueSheetName = "se-ui"
			var_3_0.channelName = var_0_1.C_SE

			arg_1_0.criInst:LoadCueSheet(var_3_0, function(arg_4_0)
				arg_3_0()
			end, true)
		end,
		function(arg_5_0)
			local var_5_0 = CueData.GetCueData()

			var_5_0.cueSheetName = "se-battle"
			var_5_0.channelName = var_0_1.C_BATTLE_SE

			arg_1_0.criInst:LoadCueSheet(var_5_0, function(arg_6_0)
				arg_5_0()
			end, true)
		end,
		function(arg_7_0)
			arg_1_0:InitBgmCfg(arg_7_0)
		end
	}, arg_1_1)
end

function var_0_1.InitCri(arg_8_0, arg_8_1)
	arg_8_0.criInitializer = GameObject.Find("CRIWARE"):GetComponent(typeof(CriWareInitializer))
	arg_8_0.criInitializer.fileSystemConfig.numberOfLoaders = 128
	arg_8_0.criInitializer.manaConfig.numberOfDecoders = 128
	arg_8_0.criInitializer.atomConfig.useRandomSeedWithTime = true

	arg_8_0.criInitializer:Initialize()

	arg_8_0.criInst = CriWareMgr.Inst

	arg_8_0.criInst:Init(function()
		CriAtom.SetCategoryVolume(var_0_1.Category_CV, arg_8_0:getCVVolume())
		CriAtom.SetCategoryVolume(var_0_1.Category_SE, arg_8_0:getSEVolume())
		CriAtom.SetCategoryVolume(var_0_1.Category_BGM, arg_8_0:getBGMVolume())
		arg_8_0.criInst:RemoveChannel("C_VOICE")
		Object.Destroy(GameObject.Find("CRIWARE/C_VOICE"))
		arg_8_0.criInst:CreateChannel(var_0_1.C_VOICE, CriWareMgr.CRI_CHANNEL_TYPE.MULTI_NOT_REPEAT)

		CriWareMgr.C_VOICE = var_0_1.C_VOICE

		local var_9_0 = arg_8_0.criInst:GetChannelData(var_0_1.C_VOICE)

		arg_8_0.criInst:CreateChannel(var_0_1.C_GALLERY_MUSIC, CriWareMgr.CRI_CHANNEL_TYPE.SINGLE)

		arg_8_0.criInst:GetChannelData(var_0_1.C_BGM).channelPlayer.loop = true

		arg_8_0.criInst:CreateChannel(var_0_1.C_BATTLE_CV_EXTRA, CriWareMgr.CRI_CHANNEL_TYPE.SINGLE)

		arg_8_0.criInst:GetChannelData(var_0_1.C_BATTLE_CV_EXTRA).channelPlayer.volume = 0.6

		arg_8_1()
	end)
end

function var_0_1.PlayBGM(arg_10_0, arg_10_1, arg_10_2)
	local var_10_0 = "bgm-" .. arg_10_1

	if arg_10_0.bgmName == var_10_0 then
		return
	end

	arg_10_0.bgmName = var_10_0

	arg_10_0.criInst:PlayBGM(var_10_0, CriWareMgr.CRI_FADE_TYPE.FADE_INOUT, function(arg_11_0)
		if arg_11_0 == nil then
			warning("Missing BGM :" .. (arg_10_1 or "NIL"))
		end
	end)
end

function var_0_1.StopBGM(arg_12_0)
	arg_12_0.criInst:StopBGM(CriWareMgr.CRI_FADE_TYPE.FADE_INOUT)

	arg_12_0.bgmName = nil
end

function var_0_1.StopPlaybackInfoForce(arg_13_0, arg_13_1)
	arg_13_1.playback:Stop(true)
end

function var_0_1.LoadCV(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0 = var_0_1.GetCVBankName(arg_14_1)

	arg_14_0:LoadCueSheet(var_14_0, arg_14_2)
end

function var_0_1.LoadBattleCV(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = var_0_1.GetBattleCVBankName(arg_15_1)

	arg_15_0:LoadCueSheet(var_15_0, arg_15_2)
end

function var_0_1.UnloadCVBank(arg_16_0)
	var_0_1.GetInstance():UnloadCueSheet(arg_16_0)
end

function var_0_1.GetCVBankName(arg_17_0)
	return "cv-" .. arg_17_0
end

function var_0_1.GetBattleCVBankName(arg_18_0)
	return "cv-" .. arg_18_0 .. "-battle"
end

function var_0_1.CheckFModeEvent(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	if not arg_19_1 then
		return
	end

	local var_19_0
	local var_19_1

	string.gsub(arg_19_1, "event:/cv/(.+)/(.+)", function(arg_20_0, arg_20_1)
		local var_20_0 = string.gsub(arg_20_1, "_%w+", "")
		local var_20_1 = tobool(ShipWordHelper.CVBattleKey[var_20_0])

		var_19_0 = "cv-" .. arg_20_0 .. (var_20_1 and "-battle" or "")
		var_19_1 = arg_20_1
	end)
	string.gsub(arg_19_1, "event:/tb/(.+)/(.+)", function(arg_21_0, arg_21_1)
		var_19_0 = "tb-" .. arg_21_0
		var_19_1 = arg_21_1
	end)
	string.gsub(arg_19_1, "event:/educate/(.+)/(.+)", function(arg_22_0, arg_22_1)
		var_19_0 = "educate-" .. arg_22_0
		var_19_1 = arg_22_1
	end)

	if string.find(arg_19_1, "event:/educate%-cv/") then
		local var_19_2 = string.split(arg_19_1, "/")

		var_19_1 = var_19_2[#var_19_2]
		var_19_0 = var_19_2[#var_19_2 - 1]
	end

	if var_19_0 and var_19_1 then
		arg_19_2(var_19_0, var_19_1)
	else
		var_19_1 = arg_19_1
		var_19_1 = string.gsub(var_19_1, "event:/(battle)/(.+)", "%1-%2")
		var_19_1 = string.gsub(var_19_1, "event:/(ui)/(.+)", "%1-%2")

		arg_19_3(var_19_1)
	end
end

function var_0_1.CheckHasCue(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = CriAtom.GetCueSheet(arg_23_1)

	return var_23_0 ~= nil and var_23_0.acb:Exists(arg_23_2)
end

function var_0_1.PlaySoundEffect_V3(arg_24_0, arg_24_1, arg_24_2)
	arg_24_0:CheckFModeEvent(arg_24_1, function(arg_25_0, arg_25_1)
		arg_24_0:PlayCV_V3(arg_25_0, arg_25_1, arg_24_2)
	end, function(arg_26_0)
		arg_24_0:PlaySE_V3(arg_26_0, arg_24_2)
	end)
end

function var_0_1.PlayMultipleSound_V3(arg_27_0, arg_27_1, arg_27_2)
	arg_27_0:CheckFModeEvent(arg_27_1, function(arg_28_0, arg_28_1)
		arg_27_0:CreateCvMultipleHandler(arg_28_0, arg_28_1, arg_27_2)
	end, function(arg_29_0)
		arg_27_0:PlaySE_V3(arg_29_0, arg_27_2)
	end)
end

function var_0_1.StopSoundEffect_V3(arg_30_0, arg_30_1)
	arg_30_0:CheckFModeEvent(arg_30_1, function(arg_31_0, arg_31_1)
		arg_30_0:StopCV_V3()
	end, function(arg_32_0)
		arg_30_0:StopSE_V3()
	end)
end

function var_0_1.UnloadSoundEffect_V3(arg_33_0, arg_33_1)
	arg_33_0:CheckFModeEvent(arg_33_1, function(arg_34_0, arg_34_1)
		arg_33_0:UnloadCueSheet(arg_34_0)
	end, function(arg_35_0)
		arg_33_0:StopSE_V3()
	end)
end

function var_0_1.PlayCV_V3(arg_36_0, arg_36_1, arg_36_2, arg_36_3)
	assert(arg_36_1, "cueSheetName can not be nil.")
	assert(arg_36_2, "cueName can not be nil.")
	arg_36_0.criInst:PlayVoice(arg_36_2, CriWareMgr.CRI_FADE_TYPE.NONE, arg_36_1, function(arg_37_0)
		if arg_36_3 ~= nil then
			arg_36_3(arg_37_0)
		end
	end)
end

function var_0_1.CreateCvMultipleHandler(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
	if not arg_38_0.luHandle then
		arg_38_0.luHandle = LateUpdateBeat:CreateListener(arg_38_0.LateCvHandler, arg_38_0)

		LateUpdateBeat:AddListener(arg_38_0.luHandle)
	end

	arg_38_0.cvCacheDataList = arg_38_0.cvCacheDataList or {}

	local var_38_0 = true

	for iter_38_0, iter_38_1 in ipairs(arg_38_0.cvCacheDataList) do
		if iter_38_1[1] == arg_38_1 and iter_38_1[2] == arg_38_2 then
			var_38_0 = false

			break
		end
	end

	if var_38_0 then
		arg_38_0.cvCacheDataList[#arg_38_0.cvCacheDataList + 1] = {
			arg_38_1,
			arg_38_2,
			arg_38_3
		}
	end
end

function var_0_1.LateCvHandler(arg_39_0)
	for iter_39_0, iter_39_1 in ipairs(arg_39_0.cvCacheDataList) do
		local var_39_0 = iter_39_1[1]
		local var_39_1 = iter_39_1[2]
		local var_39_2 = iter_39_1[3]

		if iter_39_0 == 1 then
			arg_39_0.criInst:PlayVoice(var_39_1, CriWareMgr.CRI_FADE_TYPE.NONE, var_39_0, function(arg_40_0)
				if var_39_2 ~= nil then
					var_39_2(arg_40_0)
				end
			end)
		else
			local var_39_3 = CueData.GetCueData()

			var_39_3.cueSheetName = var_39_0
			var_39_3.channelName = var_0_1.C_BATTLE_CV_EXTRA
			var_39_3.cueName = var_39_1

			onDelayTick(function()
				arg_39_0.criInst:PlaySound(var_39_3, CriWareMgr.CRI_FADE_TYPE.FADE_CROSS, function(arg_42_0)
					if var_39_2 ~= nil then
						var_39_2(arg_42_0)
					end
				end)
			end, iter_39_0 * 0.4)
		end
	end

	arg_39_0.cvCacheDataList = nil

	if arg_39_0.luHandle then
		LateUpdateBeat:RemoveListener(arg_39_0.luHandle)

		arg_39_0.luHandle = nil
	end
end

function var_0_1.StopCV_V3(arg_43_0)
	arg_43_0.criInst:GetChannelData(var_0_1.C_VOICE).channelPlayer:Stop()
end

function var_0_1.PlaySE_V3(arg_44_0, arg_44_1, arg_44_2)
	assert(arg_44_1, "cueName can not be nil.")
	arg_44_0.criInst:PlayAnySE(arg_44_1, nil, function(arg_45_0)
		if arg_44_2 ~= nil then
			arg_44_2(arg_45_0)
		end
	end)
end

function var_0_1.StopSE_V3(arg_46_0)
	arg_46_0.criInst:GetChannelData(var_0_1.C_SE).channelPlayer:Stop()
	arg_46_0.criInst:GetChannelData(var_0_1.C_BATTLE_SE).channelPlayer:Stop()
end

function var_0_1.StopSEBattle_V3(arg_47_0)
	arg_47_0.criInst:GetChannelData(var_0_1.C_BATTLE_SE).channelPlayer:Stop()
end

function var_0_1.LoadCueSheet(arg_48_0, arg_48_1, arg_48_2)
	local var_48_0 = CueData.GetCueData()

	var_48_0.cueSheetName = arg_48_1

	arg_48_0.criInst:LoadCueSheet(var_48_0, function(arg_49_0)
		arg_48_2(arg_49_0)
	end, true)
end

function var_0_1.UnloadCueSheet(arg_50_0, arg_50_1)
	arg_50_0.criInst:UnloadCueSheet(arg_50_1)
end

function var_0_1.getCVVolume(arg_51_0)
	return PlayerPrefs.GetFloat("cv_vol", DEFAULT_CVVOLUME)
end

function var_0_1.setCVVolume(arg_52_0, arg_52_1)
	PlayerPrefs.SetFloat("cv_vol", arg_52_1)
	CriAtom.SetCategoryVolume(var_0_1.Category_CV, arg_52_1)
end

function var_0_1.getBGMVolume(arg_53_0)
	return PlayerPrefs.GetFloat("bgm_vol", DEFAULT_BGMVOLUME)
end

function var_0_1.setBGMVolume(arg_54_0, arg_54_1)
	PlayerPrefs.SetFloat("bgm_vol", arg_54_1)
	CriAtom.SetCategoryVolume(var_0_1.Category_BGM, arg_54_1)
end

function var_0_1.getSEVolume(arg_55_0)
	return PlayerPrefs.GetFloat("se_vol", DEFAULT_SEVOLUME)
end

function var_0_1.setSEVolume(arg_56_0, arg_56_1)
	PlayerPrefs.SetFloat("se_vol", arg_56_1)
	CriAtom.SetCategoryVolume(var_0_1.Category_SE, arg_56_1)
end

function var_0_1.InitBgmCfg(arg_57_0, arg_57_1)
	arg_57_0.isDefaultBGM = false

	if OPEN_SPECIAL_IP_BGM and PLATFORM_CODE == PLATFORM_US then
		if Application.isEditor then
			if arg_57_1 then
				arg_57_1()
			end

			return
		end

		local var_57_0 = {
			"Malaysia",
			"Indonesia"
		}
		local var_57_1 = "https://pro.ip-api.com/json/?key=TShzQlq7O9KuthI"
		local var_57_2 = ""

		local function var_57_3(arg_58_0)
			local var_58_0 = "\"country\":\""
			local var_58_1 = "\","
			local var_58_2, var_58_3 = string.find(arg_58_0, var_58_0)

			if var_58_3 then
				arg_58_0 = string.sub(arg_58_0, var_58_3 + 1)
			end

			local var_58_4 = string.find(arg_58_0, var_58_1)

			if var_58_4 then
				arg_58_0 = string.sub(arg_58_0, 1, var_58_4 - 1)
			end

			return arg_58_0
		end

		local function var_57_4(arg_59_0)
			local var_59_0 = false

			for iter_59_0, iter_59_1 in ipairs(var_57_0) do
				if iter_59_1 == arg_59_0 then
					var_59_0 = true
				end
			end

			return var_59_0
		end

		VersionMgr.Inst:WebRequest(var_57_1, function(arg_60_0, arg_60_1)
			local var_60_0 = var_57_3(arg_60_1)

			print("content: " .. arg_60_1)
			print("country is: " .. var_60_0)

			arg_57_0.isDefaultBGM = var_57_4(var_60_0)

			print("IP limit: " .. tostring(arg_57_0.isDefaultBGM))

			if arg_57_1 then
				arg_57_1()
			end
		end)
	elseif arg_57_1 then
		arg_57_1()
	end
end

function var_0_1.IsDefaultBGM(arg_61_0)
	return arg_61_0.isDefaultBGM
end

function var_0_1.getAtomSource(arg_62_0, arg_62_1)
	return GetComponent(GameObject.Find("CRIWARE/" .. arg_62_1), "CriAtomSource")
end
