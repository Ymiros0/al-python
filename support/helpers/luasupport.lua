﻿local var_0_0 = print

function originalPrint(...)
	if IsUnityEditor then
		var_0_0(debug.traceback(printEx(...), 2))
	else
		var_0_0(printEx(...))
	end
end

if IsUnityEditor then
	function print(...)
		var_0_0(debug.traceback(printEx(...), 2))
	end
else
	function print()
		return
	end
end

local var_0_1 = setmetatable({}, {
	__mode = "kv"
})
local var_0_2 = getmetatable(GameObject)
local var_0_3 = var_0_2.__index

function var_0_2.__index(arg_4_0, arg_4_1)
	if arg_4_1 == "transform" then
		local var_4_0 = var_0_1[arg_4_0]

		if var_4_0 then
			return var_4_0
		end

		local var_4_1 = var_0_3(arg_4_0, arg_4_1)

		var_0_1[arg_4_0] = var_4_1

		return var_4_1
	elseif arg_4_1 == "gameObject" then
		return arg_4_0
	else
		return var_0_3(arg_4_0, arg_4_1)
	end
end

local var_0_4 = setmetatable({}, {
	__mode = "kv"
})
local var_0_5 = getmetatable(Transform)
local var_0_6 = var_0_5.__index

function var_0_5.__index(arg_5_0, arg_5_1)
	if arg_5_1 == "gameObject" then
		local var_5_0 = var_0_4[arg_5_0]

		if var_5_0 then
			return var_5_0
		end

		local var_5_1 = var_0_6(arg_5_0, arg_5_1)

		var_0_4[arg_5_0] = var_5_1

		return var_5_1
	elseif arg_5_1 == "transform" then
		return arg_5_0
	else
		return var_0_6(arg_5_0, arg_5_1)
	end
end

function gcAll(arg_6_0)
	PoolMgr.GetInstance():ExcessPainting()
	ResourceMgr.Inst:unloadUnusedAssetBundles()
	GCThread.GetInstance():GC(arg_6_0)
end

function RemoveTableItem(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = 0

	for iter_7_0 = 1, #arg_7_0 do
		if arg_7_0[iter_7_0 - var_7_0] == arg_7_1 then
			table.remove(arg_7_0, iter_7_0 - var_7_0)

			if arg_7_2 then
				var_7_0 = var_7_0 + 1
			else
				break
			end
		end
	end
end

function IsNil(arg_8_0)
	return arg_8_0 == nil or arg_8_0:Equals(nil)
end

function isnan(arg_9_0)
	return arg_9_0 ~= arg_9_0
end

function GetDir(arg_10_0)
	return string.match(arg_10_0, ".*/")
end

function GetFileName(arg_11_0)
	return string.match(arg_11_0, ".*/(.*)")
end

function DumpTable(arg_12_0)
	for iter_12_0, iter_12_1 in pairs(arg_12_0) do
		if iter_12_1 ~= nil then
			Debugger.Log("Key: {0}, Value: {1}", tostring(iter_12_0), tostring(iter_12_1))
		else
			Debugger.Log("Key: {0}, Value nil", tostring(iter_12_0))
		end
	end
end

function PrintTable(arg_13_0)
	local var_13_0 = {}

	local function var_13_1(arg_14_0, arg_14_1, arg_14_2)
		for iter_14_0, iter_14_1 in pairs(arg_14_0) do
			if type(iter_14_1) == "table" then
				table.insert(arg_14_1, arg_14_2 .. tostring(iter_14_0) .. ":\n")
				var_13_1(iter_14_1, arg_14_1, arg_14_2 .. " ")
			else
				table.insert(arg_14_1, arg_14_2 .. tostring(iter_14_0) .. ": " .. tostring(iter_14_1) .. "\n")
			end
		end
	end

	var_13_1(arg_13_0, var_13_0, "")

	return table.concat(var_13_0, "")
end

function PrintLua(arg_15_0, arg_15_1)
	local var_15_0

	arg_15_1 = arg_15_1 or _G

	for iter_15_0 in string.gmatch(arg_15_0, "%w+") do
		arg_15_1 = arg_15_1[iter_15_0]
	end

	local var_15_1 = arg_15_1

	if var_15_1 == nil then
		Debugger.Log("Lua Module {0} not exists", arg_15_0)

		return
	end

	Debugger.Log("-----------------Dump Table {0}-----------------", arg_15_0)

	if type(var_15_1) == "table" then
		for iter_15_1, iter_15_2 in pairs(var_15_1) do
			Debugger.Log("Key: {0}, Value: {1}", iter_15_1, tostring(iter_15_2))
		end
	end

	local var_15_2 = getmetatable(var_15_1)

	Debugger.Log("-----------------Dump meta {0}-----------------", arg_15_0)

	while var_15_2 ~= nil and var_15_2 ~= var_15_1 do
		for iter_15_3, iter_15_4 in pairs(var_15_2) do
			if iter_15_3 ~= nil then
				Debugger.Log("Key: {0}, Value: {1}", tostring(iter_15_3), tostring(iter_15_4))
			end
		end

		var_15_2 = getmetatable(var_15_2)
	end

	Debugger.Log("-----------------Dump meta Over-----------------")
	Debugger.Log("-----------------Dump Table Over-----------------")
end

function IsString(arg_16_0)
	return type(arg_16_0) == "string"
end

function IsNumber(arg_17_0)
	return type(arg_17_0) == "number"
end

function tobool(arg_18_0)
	return arg_18_0 and true or false
end

function warning(...)
	if IsUnityEditor then
		Debugger.LogWarning(debug.traceback(printEx(...), 2))
	else
		Debugger.LogWarning(printEx(...))
	end
end

function errorMsg(...)
	if IsUnityEditor then
		Debugger.LogError(debug.traceback(printEx(...)))
	else
		Debugger.LogError(printEx(...))
	end
end

function BuildVector3(arg_21_0)
	return Vector3(arg_21_0[1], arg_21_0[2], arg_21_0[3])
end

function ShowFuncInfo(arg_22_0)
	local var_22_0 = debug.getinfo(arg_22_0)

	return string.format("file:%s#%d", var_22_0.source, var_22_0.linedefined)
end

function String2Table(arg_23_0)
	local var_23_0 = {}

	for iter_23_0 in arg_23_0:gmatch(".") do
		table.insert(var_23_0, iter_23_0)
	end

	return var_23_0
end

local var_0_7 = require("bit")

function unicode_to_utf8(arg_24_0)
	if type(arg_24_0) ~= "string" then
		return arg_24_0
	end

	local var_24_0 = ""
	local var_24_1 = 1

	while true do
		local var_24_2 = string.byte(arg_24_0, var_24_1)
		local var_24_3

		if var_24_2 ~= nil and string.sub(arg_24_0, var_24_1, var_24_1 + 1) == "\\u" then
			var_24_3 = tonumber("0x" .. string.sub(arg_24_0, var_24_1 + 2, var_24_1 + 5))
			var_24_1 = var_24_1 + 6
		elseif var_24_2 ~= nil then
			var_24_3 = var_24_2
			var_24_1 = var_24_1 + 1
		else
			break
		end

		if var_24_3 <= 127 then
			var_24_0 = var_24_0 .. string.char(var_0_7.band(var_24_3, 127))
		elseif var_24_3 >= 128 and var_24_3 <= 2047 then
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(192, var_0_7.band(var_0_7.rshift(var_24_3, 6), 31)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_24_3, 63)))
		elseif var_24_3 >= 2048 and var_24_3 <= 65535 then
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(224, var_0_7.band(var_0_7.rshift(var_24_3, 12), 15)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_0_7.rshift(var_24_3, 6), 63)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_24_3, 63)))
		end
	end

	return var_24_0 .. "\x00"
end

function utf8_to_unicode(arg_25_0)
	if type(arg_25_0) ~= "string" then
		return arg_25_0
	end

	local var_25_0 = ""
	local var_25_1 = 1
	local var_25_2 = string.byte(arg_25_0, var_25_1)
	local var_25_3 = 0

	while var_25_2 ~= nil do
		local var_25_4
		local var_25_5

		if var_25_2 >= 0 and var_25_2 <= 127 then
			var_25_4 = var_25_2
			var_25_5 = 0
		elseif var_0_7.band(var_25_2, 224) == 192 then
			local var_25_6 = 0
			local var_25_7 = 0
			local var_25_8 = var_0_7.band(var_25_2, var_0_7.rshift(255, 3))

			var_25_1 = var_25_1 + 1
			var_25_2 = string.byte(arg_25_0, var_25_1)

			local var_25_9 = var_0_7.band(var_25_2, var_0_7.rshift(255, 2))

			var_25_4 = var_0_7.bor(var_25_9, var_0_7.lshift(var_0_7.band(var_25_8, var_0_7.rshift(255, 6)), 6))
			var_25_5 = var_0_7.rshift(var_25_8, 2)
		elseif var_0_7.band(var_25_2, 240) == 224 then
			local var_25_10 = 0
			local var_25_11 = 0
			local var_25_12 = 0
			local var_25_13 = var_0_7.band(var_25_2, var_0_7.rshift(255, 3))

			var_25_1 = var_25_1 + 1
			var_25_2 = string.byte(arg_25_0, var_25_1)

			local var_25_14 = var_0_7.band(var_25_2, var_0_7.rshift(255, 2))

			var_25_1 = var_25_1 + 1
			var_25_2 = string.byte(arg_25_0, var_25_1)

			local var_25_15 = var_0_7.band(var_25_2, var_0_7.rshift(255, 2))

			var_25_4 = var_0_7.bor(var_0_7.lshift(var_0_7.band(var_25_14, var_0_7.rshift(255, 6)), 6), var_25_15)
			var_25_5 = var_0_7.bor(var_0_7.lshift(var_25_13, 4), var_0_7.rshift(var_25_14, 2))
		end

		var_25_0 = var_25_0 .. string.format("\\u%02x%02x", var_25_5, var_25_4)

		if var_25_5 == 0 then
			var_25_3 = var_25_3 + 1
		else
			var_25_3 = var_25_3 + 2
		end

		var_25_1 = var_25_1 + 1
		var_25_2 = string.byte(arg_25_0, var_25_1)
	end

	return var_25_0, var_25_3
end

function utf8_size(arg_26_0)
	if not arg_26_0 then
		return 0
	elseif arg_26_0 > 240 then
		return 4
	elseif arg_26_0 > 225 then
		return 3
	elseif arg_26_0 > 192 then
		return 2
	else
		return 1
	end
end

function utf8_len(arg_27_0)
	local var_27_0 = 1
	local var_27_1 = 0
	local var_27_2 = #arg_27_0

	while var_27_0 <= var_27_2 do
		local var_27_3 = string.byte(arg_27_0, var_27_0)

		var_27_0 = var_27_0 + utf8_size(var_27_3)
		var_27_1 = var_27_1 + 1
	end

	return var_27_1
end

function existCall(arg_28_0, ...)
	if arg_28_0 and type(arg_28_0) == "function" then
		return arg_28_0(...)
	end
end

function packEx(...)
	return {
		len = select("#", ...),
		...
	}
end

function unpackEx(arg_30_0)
	return unpack(arg_30_0, 1, arg_30_0.len)
end

function printEx(...)
	local var_31_0 = packEx(...)

	for iter_31_0 = 1, var_31_0.len do
		var_31_0[iter_31_0] = tostring(var_31_0[iter_31_0])
	end

	return table.concat(var_31_0, " ")
end

function envFunc(arg_32_0, arg_32_1, ...)
	assert(type(arg_32_0) == "table")

	local var_32_0 = getfenv(arg_32_1)

	warning(var_32_0 == _G)
	setfenv(arg_32_1, setmetatable({}, {
		__index = function(arg_33_0, arg_33_1)
			if arg_32_0[arg_33_1] ~= nil then
				return arg_32_0[arg_33_1]
			else
				return var_32_0[arg_33_1]
			end
		end,
		__newindex = function(arg_34_0, arg_34_1, arg_34_2)
			arg_32_0[arg_34_1] = arg_34_2
		end
	}))

	local var_32_1 = packEx(arg_32_1(...))

	setfenv(arg_32_1, var_32_0)

	return unpackEx(var_32_1)
end
