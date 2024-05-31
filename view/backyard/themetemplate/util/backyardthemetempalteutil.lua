local var_0_0 = class("BackYardThemeTempalteUtil")
local var_0_1 = false
local var_0_2 = true
local var_0_3 = 1920
local var_0_4 = 1080

var_0_0.TakeScale = 0.86
var_0_0.HideGos = {}
var_0_0.ScaleGos = {}
var_0_0.loader = {}

local var_0_5 = 7

var_0_0.caches = {}

local function var_0_6(...)
	if var_0_1 then
		print(...)
	end
end

local function var_0_7()
	return Application.persistentDataPath .. "/screen_scratch"
end

local function var_0_8(arg_3_0)
	return Application.persistentDataPath .. "/screen_scratch/" .. arg_3_0 .. ".png"
end

local function var_0_9(arg_4_0)
	return arg_4_0 .. ".png"
end

local function var_0_10(arg_5_0)
	if PathMgr.FileExists(arg_5_0) then
		return HashUtil.HashFile(arg_5_0)
	else
		return ""
	end
end

local function var_0_11(arg_6_0, arg_6_1, arg_6_2)
	if not var_0_0.FileExists(arg_6_0) then
		arg_6_2()

		return
	end

	local var_6_0 = var_0_8(arg_6_0)
	local var_6_1 = var_0_9(arg_6_0)

	pg.OSSMgr.GetInstance():GetTexture2D(var_6_1, var_6_0, false, var_0_3, var_0_4, function(arg_7_0, arg_7_1)
		if arg_7_0 and arg_7_1 then
			arg_6_2(arg_7_1)
		else
			arg_6_2()
		end
	end)
end

local function var_0_12(arg_8_0, arg_8_1, arg_8_2)
	if not var_0_2 then
		arg_8_2()

		return
	end

	local var_8_0 = var_0_8(arg_8_0)
	local var_8_1 = var_0_9(arg_8_0)

	pg.OSSMgr.GetInstance():GetTexture2D(var_8_1, var_8_0, true, var_0_3, var_0_4, function(arg_9_0, arg_9_1)
		if arg_9_0 and arg_9_1 and arg_8_1 == var_0_10(var_8_0) then
			arg_8_2(arg_9_1)
		else
			arg_8_2()
		end
	end)
end

local function var_0_13(arg_10_0, arg_10_1)
	if not var_0_2 then
		arg_10_1()

		return
	end

	local var_10_0 = var_0_8(arg_10_0)
	local var_10_1 = var_0_9(arg_10_0)

	pg.OSSMgr.GetInstance():DeleteObject(var_10_1, arg_10_1)
end

local function var_0_14(arg_11_0, arg_11_1)
	if not var_0_2 then
		arg_11_1()

		return
	end

	local var_11_0 = var_0_8(arg_11_0)
	local var_11_1 = var_0_9(arg_11_0)

	pg.OSSMgr.GetInstance():AsynUpdateLoad(var_11_1, var_11_0, arg_11_1)
end

function var_0_0.FileExists(arg_12_0)
	local var_12_0 = var_0_8(arg_12_0)

	return PathMgr.FileExists(var_12_0)
end

function var_0_0.TakePhoto(arg_13_0)
	local var_13_0 = pg.UIMgr.GetInstance().UIMain.parent
	local var_13_1 = var_13_0.sizeDelta.x
	local var_13_2 = var_13_0.sizeDelta.y

	return ScreenShooter.TakePhoto(arg_13_0, var_13_1, var_13_2)
end

function var_0_0.TakeIcon(arg_14_0)
	local var_14_0 = pg.UIMgr.GetInstance().UIMain.parent
	local var_14_1 = var_14_0.sizeDelta.x
	local var_14_2 = var_14_0.sizeDelta.y
	local var_14_3 = 426
	local var_14_4 = 320
	local var_14_5 = var_14_1 * 0.5 - var_14_3 * 0.5
	local var_14_6 = var_14_2 * 0.5 - var_14_4 * 0.5
	local var_14_7 = UnityEngine.Rect.New(var_14_5, var_14_6, var_14_3, var_14_4)

	return ScreenShooter.TakePhoto(arg_14_0, var_14_1, var_14_1, var_14_7)
end

function var_0_0.SavePhoto(arg_15_0, arg_15_1, arg_15_2, arg_15_3)
	seriesAsync({
		function(arg_16_0)
			local var_16_0 = var_0_8(arg_15_0 .. "_icon")

			ScreenShooter.SaveTextureToLocal(var_16_0, arg_15_2, true)
			arg_16_0()
		end,
		function(arg_17_0)
			onNextTick(arg_17_0)
		end,
		function(arg_18_0)
			local var_18_0 = var_0_8(arg_15_0)

			ScreenShooter.SaveTextureToLocal(var_18_0, arg_15_1, true)
			arg_18_0()
		end
	}, function()
		if arg_15_3 then
			arg_15_3()
		end
	end)
end

local function var_0_15(arg_20_0)
	return _.detect(var_0_0.caches, function(arg_21_0)
		return arg_21_0.name == arg_20_0
	end)
end

local function var_0_16(arg_22_0, arg_22_1, arg_22_2)
	local function var_22_0(arg_23_0)
		if arg_23_0 then
			var_0_0.CheckCache()
			table.insert(var_0_0.caches, {
				name = arg_22_0,
				asset = arg_23_0
			})
		end

		arg_22_2(arg_23_0)
	end

	if not arg_22_1 or arg_22_1 == "" then
		var_22_0(nil)
	elseif var_0_0.FileExists(arg_22_0) and arg_22_1 == var_0_10(var_0_8(arg_22_0)) then
		var_0_11(arg_22_0, arg_22_1, var_22_0)
	else
		var_0_12(arg_22_0, arg_22_1, var_22_0)
	end
end

function var_0_0.GetTexture(arg_24_0, arg_24_1, arg_24_2)
	local var_24_0 = var_0_15(arg_24_0)

	if var_24_0 then
		arg_24_2(var_24_0.asset)

		return
	end

	var_0_16(arg_24_0, arg_24_1, arg_24_2)
end

function var_0_0.GetNonCacheTexture(arg_25_0, arg_25_1, arg_25_2)
	if not arg_25_1 or arg_25_1 == "" then
		arg_25_2(nil)
	elseif var_0_0.FileExists(arg_25_0) and arg_25_1 == var_0_10(var_0_8(arg_25_0)) then
		var_0_11(arg_25_0, arg_25_1, arg_25_2)
	else
		var_0_12(arg_25_0, arg_25_1, arg_25_2)
	end
end

function var_0_0.UploadTexture(arg_26_0, arg_26_1)
	var_0_14(arg_26_0, arg_26_1)
end

function var_0_0.DeleteTexture(arg_27_0, arg_27_1)
	var_0_13(arg_27_0, arg_27_1)
end

function var_0_0.GetMd5(arg_28_0)
	local var_28_0 = var_0_8(arg_28_0)

	return var_0_10(var_28_0)
end

function var_0_0.GetIconMd5(arg_29_0)
	local var_29_0 = arg_29_0 .. "_icon"

	return var_0_0.GetMd5(var_29_0)
end

function var_0_0.CheckCache()
	if #var_0_0.caches >= var_0_5 then
		var_0_0.ClearCache(1)
		gcAll(false)
	end
end

function var_0_0.CheckSaveDirectory()
	local var_31_0 = var_0_7()

	if not System.IO.Directory.Exists(var_31_0) then
		System.IO.Directory.CreateDirectory(var_31_0)
	end
end

function var_0_0.ClearCaches(arg_32_0)
	if not var_0_0.caches or #var_0_0.caches == 0 then
		return
	end

	for iter_32_0, iter_32_1 in ipairs(arg_32_0) do
		for iter_32_2 = #var_0_0.caches, 1, -1 do
			if var_0_0.caches[iter_32_2].name == iter_32_1 then
				var_0_0.ClearCache(iter_32_2, destroy)
			end
		end
	end
end

function var_0_0.ClearCache(arg_33_0, arg_33_1)
	local var_33_0 = table.remove(var_0_0.caches, arg_33_0)

	if arg_33_1 and not IsNil(var_33_0.asset) then
		Object.Destroy(var_33_0.asset)
	end
end

function var_0_0.ClearAllCacheAsyn()
	for iter_34_0, iter_34_1 in pairs(var_0_0.caches) do
		if not IsNil(iter_34_1.asset) then
			Object.Destroy(iter_34_1.asset)
		end
	end

	var_0_0.caches = {}

	gcAll(false)
end

function var_0_0.ClearAllCache()
	var_0_0.loader = {}

	var_0_0.ClearAllCacheAsyn()
end

return var_0_0
