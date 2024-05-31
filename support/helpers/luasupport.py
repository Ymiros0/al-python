local var_0_0 = print

def originalPrint(...):
	if IsUnityEditor:
		var_0_0(debug.traceback(printEx(...), 2))
	else
		var_0_0(printEx(...))

if IsUnityEditor:
	function print(...)
		var_0_0(debug.traceback(printEx(...), 2))
else
	function print()
		return

local var_0_1 = setmetatable({}, {
	__mode = "kv"
})
local var_0_2 = getmetatable(GameObject)
local var_0_3 = var_0_2.__index

def var_0_2.__index(arg_4_0, arg_4_1):
	if arg_4_1 == "transform":
		local var_4_0 = var_0_1[arg_4_0]

		if var_4_0:
			return var_4_0

		local var_4_1 = var_0_3(arg_4_0, arg_4_1)

		var_0_1[arg_4_0] = var_4_1

		return var_4_1
	elif arg_4_1 == "gameObject":
		return arg_4_0
	else
		return var_0_3(arg_4_0, arg_4_1)

local var_0_4 = setmetatable({}, {
	__mode = "kv"
})
local var_0_5 = getmetatable(Transform)
local var_0_6 = var_0_5.__index

def var_0_5.__index(arg_5_0, arg_5_1):
	if arg_5_1 == "gameObject":
		local var_5_0 = var_0_4[arg_5_0]

		if var_5_0:
			return var_5_0

		local var_5_1 = var_0_6(arg_5_0, arg_5_1)

		var_0_4[arg_5_0] = var_5_1

		return var_5_1
	elif arg_5_1 == "transform":
		return arg_5_0
	else
		return var_0_6(arg_5_0, arg_5_1)

def gcAll(arg_6_0):
	PoolMgr.GetInstance().ExcessPainting()
	ResourceMgr.Inst.unloadUnusedAssetBundles()
	GCThread.GetInstance().GC(arg_6_0)

def RemoveTableItem(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = 0

	for iter_7_0 = 1, #arg_7_0:
		if arg_7_0[iter_7_0 - var_7_0] == arg_7_1:
			table.remove(arg_7_0, iter_7_0 - var_7_0)

			if arg_7_2:
				var_7_0 = var_7_0 + 1
			else
				break

def IsNil(arg_8_0):
	return arg_8_0 == None or arg_8_0.Equals(None)

def isnan(arg_9_0):
	return arg_9_0 != arg_9_0

def GetDir(arg_10_0):
	return string.match(arg_10_0, ".*/")

def GetFileName(arg_11_0):
	return string.match(arg_11_0, ".*/(.*)")

def DumpTable(arg_12_0):
	for iter_12_0, iter_12_1 in pairs(arg_12_0):
		if iter_12_1 != None:
			Debugger.Log("Key. {0}, Value. {1}", tostring(iter_12_0), tostring(iter_12_1))
		else
			Debugger.Log("Key. {0}, Value None", tostring(iter_12_0))

def PrintTable(arg_13_0):
	local var_13_0 = {}

	local function var_13_1(arg_14_0, arg_14_1, arg_14_2)
		for iter_14_0, iter_14_1 in pairs(arg_14_0):
			if type(iter_14_1) == "table":
				table.insert(arg_14_1, arg_14_2 .. tostring(iter_14_0) .. ".\n")
				var_13_1(iter_14_1, arg_14_1, arg_14_2 .. " ")
			else
				table.insert(arg_14_1, arg_14_2 .. tostring(iter_14_0) .. ". " .. tostring(iter_14_1) .. "\n")

	var_13_1(arg_13_0, var_13_0, "")

	return table.concat(var_13_0, "")

def PrintLua(arg_15_0, arg_15_1):
	local var_15_0

	arg_15_1 = arg_15_1 or _G

	for iter_15_0 in string.gmatch(arg_15_0, "%w+"):
		arg_15_1 = arg_15_1[iter_15_0]

	local var_15_1 = arg_15_1

	if var_15_1 == None:
		Debugger.Log("Lua Module {0} not exists", arg_15_0)

		return

	Debugger.Log("-----------------Dump Table {0}-----------------", arg_15_0)

	if type(var_15_1) == "table":
		for iter_15_1, iter_15_2 in pairs(var_15_1):
			Debugger.Log("Key. {0}, Value. {1}", iter_15_1, tostring(iter_15_2))

	local var_15_2 = getmetatable(var_15_1)

	Debugger.Log("-----------------Dump meta {0}-----------------", arg_15_0)

	while var_15_2 != None and var_15_2 != var_15_1:
		for iter_15_3, iter_15_4 in pairs(var_15_2):
			if iter_15_3 != None:
				Debugger.Log("Key. {0}, Value. {1}", tostring(iter_15_3), tostring(iter_15_4))

		var_15_2 = getmetatable(var_15_2)

	Debugger.Log("-----------------Dump meta Over-----------------")
	Debugger.Log("-----------------Dump Table Over-----------------")

def IsString(arg_16_0):
	return type(arg_16_0) == "string"

def IsNumber(arg_17_0):
	return type(arg_17_0) == "number"

def tobool(arg_18_0):
	return arg_18_0 and True or False

def warning(...):
	if IsUnityEditor:
		Debugger.LogWarning(debug.traceback(printEx(...), 2))
	else
		Debugger.LogWarning(printEx(...))

def errorMsg(...):
	if IsUnityEditor:
		Debugger.LogError(debug.traceback(printEx(...)))
	else
		Debugger.LogError(printEx(...))

def BuildVector3(arg_21_0):
	return Vector3(arg_21_0[1], arg_21_0[2], arg_21_0[3])

def ShowFuncInfo(arg_22_0):
	local var_22_0 = debug.getinfo(arg_22_0)

	return string.format("file.%s#%d", var_22_0.source, var_22_0.linedefined)

def String2Table(arg_23_0):
	local var_23_0 = {}

	for iter_23_0 in arg_23_0.gmatch("."):
		table.insert(var_23_0, iter_23_0)

	return var_23_0

local var_0_7 = require("bit")

def unicode_to_utf8(arg_24_0):
	if type(arg_24_0) != "string":
		return arg_24_0

	local var_24_0 = ""
	local var_24_1 = 1

	while True:
		local var_24_2 = string.byte(arg_24_0, var_24_1)
		local var_24_3

		if var_24_2 != None and string.sub(arg_24_0, var_24_1, var_24_1 + 1) == "\\u":
			var_24_3 = tonumber("0x" .. string.sub(arg_24_0, var_24_1 + 2, var_24_1 + 5))
			var_24_1 = var_24_1 + 6
		elif var_24_2 != None:
			var_24_3 = var_24_2
			var_24_1 = var_24_1 + 1
		else
			break

		if var_24_3 <= 127:
			var_24_0 = var_24_0 .. string.char(var_0_7.band(var_24_3, 127))
		elif var_24_3 >= 128 and var_24_3 <= 2047:
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(192, var_0_7.band(var_0_7.rshift(var_24_3, 6), 31)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_24_3, 63)))
		elif var_24_3 >= 2048 and var_24_3 <= 65535:
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(224, var_0_7.band(var_0_7.rshift(var_24_3, 12), 15)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_0_7.rshift(var_24_3, 6), 63)))
			var_24_0 = var_24_0 .. string.char(var_0_7.bor(128, var_0_7.band(var_24_3, 63)))

	return var_24_0 .. "\x00"

def utf8_to_unicode(arg_25_0):
	if type(arg_25_0) != "string":
		return arg_25_0

	local var_25_0 = ""
	local var_25_1 = 1
	local var_25_2 = string.byte(arg_25_0, var_25_1)
	local var_25_3 = 0

	while var_25_2 != None:
		local var_25_4
		local var_25_5

		if var_25_2 >= 0 and var_25_2 <= 127:
			var_25_4 = var_25_2
			var_25_5 = 0
		elif var_0_7.band(var_25_2, 224) == 192:
			local var_25_6 = 0
			local var_25_7 = 0
			local var_25_8 = var_0_7.band(var_25_2, var_0_7.rshift(255, 3))

			var_25_1 = var_25_1 + 1
			var_25_2 = string.byte(arg_25_0, var_25_1)

			local var_25_9 = var_0_7.band(var_25_2, var_0_7.rshift(255, 2))

			var_25_4 = var_0_7.bor(var_25_9, var_0_7.lshift(var_0_7.band(var_25_8, var_0_7.rshift(255, 6)), 6))
			var_25_5 = var_0_7.rshift(var_25_8, 2)
		elif var_0_7.band(var_25_2, 240) == 224:
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

		var_25_0 = var_25_0 .. string.format("\\u%02x%02x", var_25_5, var_25_4)

		if var_25_5 == 0:
			var_25_3 = var_25_3 + 1
		else
			var_25_3 = var_25_3 + 2

		var_25_1 = var_25_1 + 1
		var_25_2 = string.byte(arg_25_0, var_25_1)

	return var_25_0, var_25_3

def utf8_size(arg_26_0):
	if not arg_26_0:
		return 0
	elif arg_26_0 > 240:
		return 4
	elif arg_26_0 > 225:
		return 3
	elif arg_26_0 > 192:
		return 2
	else
		return 1

def utf8_len(arg_27_0):
	local var_27_0 = 1
	local var_27_1 = 0
	local var_27_2 = #arg_27_0

	while var_27_0 <= var_27_2:
		local var_27_3 = string.byte(arg_27_0, var_27_0)

		var_27_0 = var_27_0 + utf8_size(var_27_3)
		var_27_1 = var_27_1 + 1

	return var_27_1

def existCall(arg_28_0, ...):
	if arg_28_0 and type(arg_28_0) == "function":
		return arg_28_0(...)

def packEx(...):
	return {
		len = select("#", ...),
		...
	}

def unpackEx(arg_30_0):
	return unpack(arg_30_0, 1, arg_30_0.len)

def printEx(...):
	local var_31_0 = packEx(...)

	for iter_31_0 = 1, var_31_0.len:
		var_31_0[iter_31_0] = tostring(var_31_0[iter_31_0])

	return table.concat(var_31_0, " ")

def envFunc(arg_32_0, arg_32_1, ...):
	assert(type(arg_32_0) == "table")

	local var_32_0 = getfenv(arg_32_1)

	warning(var_32_0 == _G)
	setfenv(arg_32_1, setmetatable({}, {
		def __index:(arg_33_0, arg_33_1)
			if arg_32_0[arg_33_1] != None:
				return arg_32_0[arg_33_1]
			else
				return var_32_0[arg_33_1],
		def __newindex:(arg_34_0, arg_34_1, arg_34_2)
			arg_32_0[arg_34_1] = arg_34_2
	}))

	local var_32_1 = packEx(arg_32_1(...))

	setfenv(arg_32_1, var_32_0)

	return unpackEx(var_32_1)
