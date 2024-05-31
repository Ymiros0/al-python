pg = pg or {}

local var_0_0 = pg

var_0_0.IPAddress = class("IPAddress")

local var_0_1 = var_0_0.IPAddress
local var_0_2 = "https.//www.azurlane.tw/getip"
local var_0_3 = {
	{
		"202.39.128.0",
		"202.39.255.255"
	},
	{
		"203.66.0.0",
		"203.66.255.255"
	},
	{
		"203.69.0.0",
		"203.69.255.255"
	},
	{
		"203.75.0.0",
		"203.75.255.255"
	},
	{
		"203.74.0.0",
		"203.74.255.255"
	},
	{
		"210.65.0.0",
		"210.65.255.255"
	},
	{
		"210.71.128.0",
		"210.71.255.255"
	},
	{
		"210.61.0.0",
		"210.61.255.255"
	},
	{
		"210.62.248.0",
		"210.62.255.255"
	},
	{
		"210.59.128.0",
		"210.59.255.255"
	},
	{
		"210.242.0.0",
		"210.242.127.255"
	},
	{
		"210.242.128.0",
		"210.242.255.255"
	},
	{
		"210.241.224.0",
		"210.241.255.255"
	},
	{
		"211.72.0.0",
		"211.72.127.255"
	},
	{
		"211.72.128.0",
		"211.72.255.255"
	},
	{
		"211.75.0.0",
		" 211.75.127.255"
	},
	{
		"211.75.128.0",
		"211.75.255.255"
	},
	{
		"211.20.0.0",
		"211.20.255.255"
	},
	{
		"211.21.0.0",
		"211.21.255.255"
	},
	{
		"211.22.0.0",
		"211.22.255.255"
	},
	{
		"211.23.0.0",
		"211.23.255.255"
	},
	{
		"61.216.0.0",
		"61.219.255.255"
	},
	{
		"61.220.0.0",
		"61.227.255.255"
	},
	{
		"61.228.0.0",
		"61.231.255.255"
	},
	{
		"218.160.0.0",
		"218.165.255.255"
	}
}

def var_0_1.Ctor(arg_1_0):
	arg_1_0.ConvertIPRange()

	arg_1_0.requestUrl = var_0_2

	if not IsUnityEditor:
		VersionMgr.Inst.WebRequest(arg_1_0.requestUrl, function(arg_2_0, arg_2_1)
			arg_1_0.exportIP = arg_2_1
			arg_1_0.isSpecialIP = arg_1_0.CheckExportIP())

def var_0_1.IsIPString(arg_3_0, arg_3_1):
	if type(arg_3_1) != "string":
		return False

	local var_3_0 = string.len(arg_3_1)

	if var_3_0 < 7 or var_3_0 > 15:
		return False

	local var_3_1 = string.find(arg_3_1, "%p", 1)
	local var_3_2 = 0

	while var_3_1 != None:
		if string.sub(arg_3_1, var_3_1, var_3_1) != ".":
			return False

		var_3_2 = var_3_2 + 1
		var_3_1 = string.find(arg_3_1, "%p", var_3_1 + 1)

		if var_3_2 > 3:
			return False

	if var_3_2 != 3:
		return False

	local var_3_3 = {}

	for iter_3_0 in string.gmatch(arg_3_1, "%d+"):
		var_3_3[#var_3_3 + 1] = iter_3_0

		local var_3_4 = tonumber(iter_3_0)

		if var_3_4 == None or var_3_4 > 255:
			return False

	if #var_3_3 != 4:
		return False

	return True

def var_0_1.IP2Int(arg_4_0, arg_4_1):
	local var_4_0 = 0
	local var_4_1, var_4_2, var_4_3, var_4_4 = arg_4_1.match("(%d+)%.(%d+)%.(%d+)%.(%d+)")

	return 16777216 * var_4_1 + 65536 * var_4_2 + 256 * var_4_3 + var_4_4

def var_0_1.ConvertIPRange(arg_5_0):
	arg_5_0.IPRangeIntList = {}

	for iter_5_0, iter_5_1 in ipairs(var_0_3):
		local var_5_0 = {}
		local var_5_1 = arg_5_0.IP2Int(iter_5_1[1])

		table.insert(var_5_0, var_5_1)

		local var_5_2 = arg_5_0.IP2Int(iter_5_1[2])

		table.insert(var_5_0, var_5_2)
		assert(var_5_1 < var_5_2, "ip range is illegal" .. iter_5_1[1] .. "-" .. iter_5_1[2])
		table.insert(arg_5_0.IPRangeIntList, var_5_0)

def var_0_1.CheckExportIP(arg_6_0):
	if not arg_6_0.exportIP or not arg_6_0.IsIPString(arg_6_0.exportIP):
		return False

	local var_6_0 = arg_6_0.IP2Int(arg_6_0.exportIP)

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.IPRangeIntList):
		if var_6_0 >= iter_6_1[1] and var_6_0 <= iter_6_1[2]:
			return True

	return False

def var_0_1.GetExportIPString(arg_7_0):
	return arg_7_0.exportIP

def var_0_1.GetLocalIP(arg_8_0):
	local var_8_0 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.Network"), "player")

	arg_8_0.localIP = ReflectionHelp.RefGetProperty(typeof("UnityEngine.NetworkPlayer"), "ipAddress", var_8_0)

	return arg_8_0.localIP

def var_0_1.IsSpecialIP(arg_9_0):
	return arg_9_0.isSpecialIP
