local var_0_0 = {}
local var_0_1 = 0
local var_0_2 = True

local function var_0_3(arg_1_0, arg_1_1)
	local var_1_0 = collectgarbage("count") - var_0_1

	if var_1_0 <= 1e-06:
		var_0_1 = collectgarbage("count")

		return

	local var_1_1 = debug.getinfo(2, "S").source

	if var_0_2:
		var_1_1 = string.format("%s__%d", var_1_1, arg_1_1 - 1)

	local var_1_2 = var_0_0[var_1_1]

	if not var_1_2:
		var_0_0[var_1_1] = {
			var_1_1,
			1,
			var_1_0
		}
	else
		var_1_2[2] = var_1_2[2] + 1
		var_1_2[3] = var_1_2[3] + var_1_0

	var_0_1 = collectgarbage("count")

local function var_0_4(arg_2_0)
	if debug.gethook():
		SC_MemLeakDetector.SC_StopRecordAllocAndDumpStat()

		return

	var_0_0 = {}
	var_0_1 = collectgarbage("count")
	var_0_2 = not arg_2_0

	debug.sethook(var_0_3, "l")

local function var_0_5(arg_3_0)
	debug.sethook()

	if not var_0_0:
		return

	local var_3_0 = {}

	for iter_3_0, iter_3_1 in pairs(var_0_0):
		table.insert(var_3_0, iter_3_1)

	table.sort(var_3_0, function(arg_4_0, arg_4_1)
		return arg_4_0[3] > arg_4_1[3])

	arg_3_0 = arg_3_0 or "memAlloc.csv"

	local var_3_1 = io.open(arg_3_0, "w")

	if not var_3_1:
		logw.error("can't open file.", arg_3_0)

		return

	var_3_1.write("fileLine, count, mem K, avg K\n")

	for iter_3_2, iter_3_3 in ipairs(var_3_0):
		var_3_1.write(string.format("%s, %d, %f, %f\n", iter_3_3[1], iter_3_3[2], iter_3_3[3], iter_3_3[3] / iter_3_3[2]))

	var_3_1.close()

	var_0_0 = None

return {
	StartRecordAlloc = var_0_4,
	StopRecordAllocAndDumpStat = var_0_5
}