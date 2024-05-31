local var_0_0 = {}

def var_0_0.FailNotify(...):
	if var_0_0.NotifyFunc:
		var_0_0.NotifyFunc(...)

def var_0_0.DebugNofity(...):
	if var_0_0.DebugNofityFunc:
		var_0_0.DebugNofityFunc(...)

local function var_0_1()
	return FileTool.GetCurrentDirectiory() .. "\\"

local function var_0_2(arg_4_0)
	arg_4_0 = arg_4_0.gsub("/", "\\")

	if arg_4_0.find(".") == None:
		arg_4_0 = var_0_1() .. arg_4_0

	local var_4_0 = #arg_4_0

	if arg_4_0.sub(var_4_0, var_4_0) == "\\":
		arg_4_0 = arg_4_0.sub(1, var_4_0 - 1)

	local var_4_1 = {}

	for iter_4_0 in arg_4_0.gmatch("[^\\]+"):
		if iter_4_0 == ".." and #var_4_1 != 0:
			table.remove(var_4_1)
		elif iter_4_0 != ".":
			table.insert(var_4_1, iter_4_0)

	return table.concat(var_4_1, "\\")

def var_0_0.InitFileMap(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0):
		iter_5_1 = var_0_2(iter_5_1)

		var_0_0.NotifyFunc("root path. " .. iter_5_1)

		local var_5_0 = FileTool.GetAllFiles(iter_5_1)

		print("count " .. var_5_0.Count)

		for iter_5_2 = 0, var_5_0.Count - 1:
			local var_5_1 = var_5_0.get_Item(iter_5_2)
			local var_5_2 = string.match(var_5_1, ".*\\(.[_a-zA-Z][_a-zA-Z0-9]*)%.lua")

			if var_5_2 != None:
				if var_0_0.FileMap[var_5_2] == None:
					var_0_0.FileMap[var_5_2] = {}

				local var_5_3 = string.sub(var_5_1, #iter_5_1 + 2, #var_5_1 - 4)
				local var_5_4 = string.gsub(var_5_3, "\\", ".")

				var_0_0.LuaPathToSysPath[var_5_4] = SysPath

				table.insert(var_0_0.FileMap[var_5_2], {
					SysPath = var_5_1,
					LuaPath = var_5_4
				})

		var_0_0.NotifyFunc("load module count. " .. table.getn(var_0_0.FileMap))

def var_0_0.InitFakeTable():
	local var_6_0 = {}

	var_0_0.Meta = var_6_0

	local function var_6_1()
		return setmetatable({}, var_6_0)

	local function var_6_2()
		return

	local function var_6_3()
		return var_6_2

	local function var_6_4(arg_10_0, arg_10_1)
		var_0_0.MetaMap[arg_10_0] = arg_10_1

		return arg_10_0

	local function var_6_5(arg_11_0)
		if not var_0_0.RequireMap[arg_11_0]:
			local var_11_0 = var_6_1()

			var_0_0.RequireMap[arg_11_0] = var_11_0

		return var_0_0.RequireMap[arg_11_0]

	function var_6_0.__index(arg_12_0, arg_12_1)
		if arg_12_1 == "setmetatable":
			return var_6_4
		elif arg_12_1 == "pairs" or arg_12_1 == "ipairs":
			return var_6_3
		elif arg_12_1 == "next":
			return var_6_2
		elif arg_12_1 == "require":
			return var_6_5
		else
			local var_12_0 = var_6_1()

			rawset(arg_12_0, arg_12_1, var_12_0)

			return var_12_0

	function var_6_0.__newindex(arg_13_0, arg_13_1, arg_13_2)
		rawset(arg_13_0, arg_13_1, arg_13_2)

	function var_6_0.__call()
		return var_6_1(), var_6_1(), var_6_1()

	function var_6_0.__add()
		return var_6_0.__call()

	function var_6_0.__sub()
		return var_6_0.__call()

	function var_6_0.__mul()
		return var_6_0.__call()

	function var_6_0.__div()
		return var_6_0.__call()

	function var_6_0.__mod()
		return var_6_0.__call()

	function var_6_0.__pow()
		return var_6_0.__call()

	function var_6_0.__unm()
		return var_6_0.__call()

	function var_6_0.__concat()
		return var_6_0.__call()

	function var_6_0.__eq()
		return var_6_0.__call()

	function var_6_0.__lt()
		return var_6_0.__call()

	function var_6_0.__le()
		return var_6_0.__call()

	function var_6_0.__len()
		return var_6_0.__call()

	return var_6_1

def var_0_0.InitProtection():
	var_0_0.Protection = {}
	var_0_0.Protection[setmetatable] = True
	var_0_0.Protection[pairs] = True
	var_0_0.Protection[ipairs] = True
	var_0_0.Protection[next] = True
	var_0_0.Protection[require] = True
	var_0_0.Protection[var_0_0] = True
	var_0_0.Protection[var_0_0.Meta] = True
	var_0_0.Protection[math] = True
	var_0_0.Protection[string] = True
	var_0_0.Protection[table] = True

def var_0_0.AddFileFromHUList():
	package.loaded[var_0_0.UpdateListFile] = None

	local var_28_0 = require(var_0_0.UpdateListFile)

	var_0_0.ALL = False
	var_0_0.HUMap = {}

	for iter_28_0, iter_28_1 in pairs(var_28_0):
		if iter_28_1 == "_ALL_":
			var_0_0.ALL = True

			for iter_28_2, iter_28_3 in pairs(var_0_0.FileMap):
				for iter_28_4, iter_28_5 in pairs(iter_28_3):
					var_0_0.HUMap[iter_28_5.LuaPath] = iter_28_5.SysPath

			return

		if var_0_0.FileMap[iter_28_1]:
			for iter_28_6, iter_28_7 in pairs(var_0_0.FileMap[iter_28_1]):
				var_0_0.HUMap[iter_28_7.LuaPath] = iter_28_7.SysPath
		else
			var_0_0.FailNotify("HotUpdate can't not find " .. iter_28_1)

def var_0_0.ErrorHandle(arg_29_0):
	var_0_0.FailNotify("HotUpdate Error\n" .. tostring(arg_29_0))

	var_0_0.ErrorHappen = True

def var_0_0.BuildNewCode(arg_30_0, arg_30_1):
	io.input(arg_30_0)

	local var_30_0 = io.read("*all")

	if var_0_0.ALL and var_0_0.OldCode[arg_30_0] == None:
		var_0_0.OldCode[arg_30_0] = var_30_0

		io.input().close()

		return

	if var_0_0.OldCode[arg_30_0] == var_30_0:
		io.input().close()

		return False

	io.input().close()
	io.input(arg_30_0)

	local var_30_1 = ("--[[" .. arg_30_1 .. "]] ") .. var_30_0

	io.input().close()

	local var_30_2 = loadstring(var_30_1)

	if not var_30_2:
		var_0_0.FailNotify(arg_30_0 .. " has syntax error.")
		collectgarbage("collect")

		return False
	else
		var_0_0.FakeENV = var_0_0.FakeT()
		var_0_0.MetaMap = {}
		var_0_0.RequireMap = {}

		setfenv(var_30_2, var_0_0.FakeENV)

		local var_30_3

		var_0_0.ErrorHappen = False

		xpcall(function()
			var_30_3 = var_30_2(), var_0_0.ErrorHandle)

		if not var_0_0.ErrorHappen:
			var_0_0.OldCode[arg_30_0] = var_30_0

			return True, var_30_3
		else
			collectgarbage("collect")

			return False

def var_0_0.Travel_G():
	local var_32_0 = {
		[var_0_0] = True
	}

	local function var_32_1(arg_33_0)
		if type(arg_33_0) != "function" and type(arg_33_0) != "table" or var_32_0[arg_33_0] or var_0_0.Protection[arg_33_0]:
			return

		var_32_0[arg_33_0] = True

		if type(arg_33_0) == "function":
			for iter_33_0 = 1, math.huge:
				local var_33_0, var_33_1 = debug.getupvalue(arg_33_0, iter_33_0)

				if not var_33_0:
					break

				if type(var_33_1) == "function":
					for iter_33_1, iter_33_2 in ipairs(var_0_0.ChangedFuncList):
						if var_33_1 == iter_33_2[1]:
							debug.setupvalue(arg_33_0, iter_33_0, iter_33_2[2])

				var_32_1(var_33_1)
		elif type(arg_33_0) == "table":
			var_32_1(debug.getmetatable(arg_33_0))

			local var_33_2 = {}

			for iter_33_3, iter_33_4 in pairs(arg_33_0):
				var_32_1(iter_33_3)
				var_32_1(iter_33_4)

				if type(iter_33_4) == "function":
					for iter_33_5, iter_33_6 in ipairs(var_0_0.ChangedFuncList):
						if iter_33_4 == iter_33_6[1]:
							arg_33_0[iter_33_3] = iter_33_6[2]

				if type(iter_33_3) == "function":
					for iter_33_7, iter_33_8 in ipairs(var_0_0.ChangedFuncList):
						if iter_33_3 == iter_33_8[1]:
							var_33_2[#var_33_2 + 1] = iter_33_7

			for iter_33_9, iter_33_10 in ipairs(var_33_2):
				local var_33_3 = var_0_0.ChangedFuncList[iter_33_10]

				arg_33_0[var_33_3[2]] = arg_33_0[var_33_3[1]]
				arg_33_0[var_33_3[1]] = None

	var_32_1(_G)

	local var_32_2 = debug.getregistry()

	for iter_32_0, iter_32_1 in ipairs(var_0_0.ChangedFuncList):
		for iter_32_2, iter_32_3 in pairs(var_32_2):
			if iter_32_3 == iter_32_1[1]:
				var_32_2[iter_32_2] = iter_32_1[2]

	for iter_32_4, iter_32_5 in ipairs(var_0_0.ChangedFuncList):
		if iter_32_5[3] == "HUDebug":
			iter_32_5[4].HUDebug()

def var_0_0.ReplaceOld(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4):
	if type(arg_34_0) == type(arg_34_1):
		if type(arg_34_1) == "table":
			var_0_0.UpdateAllFunction(arg_34_0, arg_34_1, arg_34_2, arg_34_3, "")
		elif type(arg_34_1) == "function":
			var_0_0.UpdateOneFunction(arg_34_0, arg_34_1, arg_34_2, None, arg_34_3, "")

def var_0_0.HotUpdateCode(arg_35_0, arg_35_1):
	local var_35_0 = package.loaded[arg_35_0]

	if var_35_0 != None:
		var_0_0.VisitedSig = {}
		var_0_0.ChangedFuncList = {}

		local var_35_1, var_35_2 = var_0_0.BuildNewCode(arg_35_1, arg_35_0)

		if var_35_1:
			var_0_0.NotifyFunc("update module " .. arg_35_0)
			var_0_0.ReplaceOld(var_35_0, var_35_2, arg_35_0, "Main", "")

			for iter_35_0, iter_35_1 in pairs(var_0_0.RequireMap):
				local var_35_3 = package.loaded[iter_35_0]

				var_0_0.ReplaceOld(var_35_3, iter_35_1, iter_35_0, "Main_require", "")

			setmetatable(var_0_0.FakeENV, None)
			var_0_0.UpdateAllFunction(var_0_0.ENV, var_0_0.FakeENV, " ENV ", "Main", "")

			if #var_0_0.ChangedFuncList > 0:
				var_0_0.Travel_G()

			collectgarbage("collect")
	elif var_0_0.OldCode[arg_35_1] == None:
		io.input(arg_35_1)

		var_0_0.OldCode[arg_35_1] = io.read("*all")

		io.input().close()

def var_0_0.ResetENV(arg_36_0, arg_36_1, arg_36_2, arg_36_3):
	local var_36_0 = {}

	local function var_36_1(arg_37_0, arg_37_1)
		if not arg_37_0 or var_36_0[arg_37_0]:
			return

		var_36_0[arg_37_0] = True

		if type(arg_37_0) == "function":
			var_0_0.DebugNofity(arg_36_3 .. "HU.ResetENV", arg_37_1, "  from." .. arg_36_2)
			xpcall(function()
				setfenv(arg_37_0, var_0_0.ENV), var_0_0.FailNotify)
		elif type(arg_37_0) == "table":
			var_0_0.DebugNofity(arg_36_3 .. "HU.ResetENV", arg_37_1, "  from." .. arg_36_2)

			for iter_37_0, iter_37_1 in pairs(arg_37_0):
				var_36_1(iter_37_0, tostring(iter_37_0) .. "__key", " HU.ResetENV ", arg_36_3 .. "    ")
				var_36_1(iter_37_1, tostring(iter_37_0), " HU.ResetENV ", arg_36_3 .. "    ")

	var_36_1(arg_36_0, arg_36_1)

def var_0_0.UpdateUpvalue(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4):
	var_0_0.DebugNofity(arg_39_4 .. "HU.UpdateUpvalue", arg_39_2, "  from." .. arg_39_3)

	local var_39_0 = {}
	local var_39_1 = {}

	for iter_39_0 = 1, math.huge:
		local var_39_2, var_39_3 = debug.getupvalue(arg_39_0, iter_39_0)

		if not var_39_2:
			break

		var_39_0[var_39_2] = var_39_3
		var_39_1[var_39_2] = True

	for iter_39_1 = 1, math.huge:
		local var_39_4, var_39_5 = debug.getupvalue(arg_39_1, iter_39_1)

		if not var_39_4:
			break

		if var_39_1[var_39_4]:
			local var_39_6 = var_39_0[var_39_4]

			if type(var_39_6) != type(var_39_5):
				debug.setupvalue(arg_39_1, iter_39_1, var_39_6)
			elif type(var_39_6) == "function":
				var_0_0.UpdateOneFunction(var_39_6, var_39_5, var_39_4, None, "HU.UpdateUpvalue", arg_39_4 .. "    ")
			elif type(var_39_6) == "table":
				var_0_0.UpdateAllFunction(var_39_6, var_39_5, var_39_4, "HU.UpdateUpvalue", arg_39_4 .. "    ")
				debug.setupvalue(arg_39_1, iter_39_1, var_39_6)
			else
				debug.setupvalue(arg_39_1, iter_39_1, var_39_6)
		else
			var_0_0.ResetENV(var_39_5, var_39_4, "HU.UpdateUpvalue", arg_39_4 .. "    ")

def var_0_0.UpdateOneFunction(arg_40_0, arg_40_1, arg_40_2, arg_40_3, arg_40_4, arg_40_5):
	if var_0_0.Protection[arg_40_0] or var_0_0.Protection[arg_40_1]:
		return

	if arg_40_0 == arg_40_1:
		return

	local var_40_0 = tostring(arg_40_0) .. tostring(arg_40_1)

	if var_0_0.VisitedSig[var_40_0]:
		return

	var_0_0.VisitedSig[var_40_0] = True

	var_0_0.DebugNofity(arg_40_5 .. "HU.UpdateOneFunction " .. arg_40_2 .. "  from." .. arg_40_4)

	if pcall(debug.setfenv, arg_40_1, getfenv(arg_40_0)):
		var_0_0.UpdateUpvalue(arg_40_0, arg_40_1, arg_40_2, "HU.UpdateOneFunction", arg_40_5 .. "    ")

		var_0_0.ChangedFuncList[#var_0_0.ChangedFuncList + 1] = {
			arg_40_0,
			arg_40_1,
			arg_40_2,
			arg_40_3
		}

def var_0_0.UpdateAllFunction(arg_41_0, arg_41_1, arg_41_2, arg_41_3, arg_41_4):
	if var_0_0.Protection[arg_41_0] or var_0_0.Protection[arg_41_1]:
		return

	if arg_41_0 == arg_41_1:
		return

	local var_41_0 = tostring(arg_41_0) .. tostring(arg_41_1)

	if var_0_0.VisitedSig[var_41_0]:
		return

	var_0_0.VisitedSig[var_41_0] = True

	var_0_0.DebugNofity(arg_41_4 .. "HU.UpdateAllFunction " .. arg_41_2 .. "  from." .. arg_41_3)

	for iter_41_0, iter_41_1 in pairs(arg_41_1):
		local var_41_1 = arg_41_0[iter_41_0]

		if type(iter_41_1) == type(var_41_1):
			if type(iter_41_1) == "function":
				var_0_0.UpdateOneFunction(var_41_1, iter_41_1, iter_41_0, arg_41_0, "HU.UpdateAllFunction", arg_41_4 .. "    ")
			elif type(iter_41_1) == "table":
				var_0_0.UpdateAllFunction(var_41_1, iter_41_1, iter_41_0, "HU.UpdateAllFunction", arg_41_4 .. "    ")
		elif var_41_1 == None and type(iter_41_1) == "function" and pcall(setfenv, iter_41_1, var_0_0.ENV):
			arg_41_0[iter_41_0] = iter_41_1

	local var_41_2 = debug.getmetatable(arg_41_0)
	local var_41_3 = var_0_0.MetaMap[arg_41_1]

	if type(var_41_2) == "table" and type(var_41_3) == "table":
		var_0_0.UpdateAllFunction(var_41_2, var_41_3, arg_41_2 .. "'s Meta", "HU.UpdateAllFunction", arg_41_4 .. "    ")

def var_0_0.Init(arg_42_0, arg_42_1, arg_42_2, arg_42_3):
	var_0_0.UpdateListFile = arg_42_0
	var_0_0.HUMap = {}
	var_0_0.FileMap = {}
	var_0_0.NotifyFunc = arg_42_2
	var_0_0.OldCode = {}
	var_0_0.ChangedFuncList = {}
	var_0_0.VisitedSig = {}
	var_0_0.FakeENV = None
	var_0_0.ENV = arg_42_3 or _G
	var_0_0.LuaPathToSysPath = {}

	var_0_0.InitFileMap(arg_42_1)

	var_0_0.FakeT = var_0_0.InitFakeTable()

	var_0_0.InitProtection()

	var_0_0.ALL = False

def var_0_0.Update():
	var_0_0.AddFileFromHUList()

	for iter_43_0, iter_43_1 in pairs(var_0_0.HUMap):
		var_0_0.HotUpdateCode(iter_43_0, iter_43_1)

return var_0_0
