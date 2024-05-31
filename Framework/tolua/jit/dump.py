local var_0_0 = require("jit")

assert(var_0_0.version_num == 20100, "LuaJIT core/library version mismatch")

local var_0_1 = require("jit.util")
local var_0_2 = require("jit.vmdef")
local var_0_3 = var_0_1.funcinfo
local var_0_4 = var_0_1.funcbc
local var_0_5 = var_0_1.traceinfo
local var_0_6 = var_0_1.traceir
local var_0_7 = var_0_1.tracek
local var_0_8 = var_0_1.tracemc
local var_0_9 = var_0_1.tracesnap
local var_0_10 = var_0_1.traceexitstub
local var_0_11 = var_0_1.ircalladdr
local var_0_12 = require("bit")
local var_0_13 = var_0_12.band
local var_0_14 = var_0_12.rshift
local var_0_15 = var_0_12.tohex
local var_0_16 = string.sub
local var_0_17 = string.gsub
local var_0_18 = string.format
local var_0_19 = string.byte
local var_0_20 = string.rep
local var_0_21 = type
local var_0_22 = tostring
local var_0_23 = io.stdout
local var_0_24 = io.stderr
local var_0_25
local var_0_26
local var_0_27
local var_0_28
local var_0_29
local var_0_30 = {
	__index = False
}
local var_0_31 = {}
local var_0_32 = 0

local function var_0_33(arg_1_0, arg_1_1)
	local var_1_0 = {}

	var_0_30.__index = var_1_0

	if var_0_0.arch.sub(1, 4) == "mips":
		var_1_0[var_0_10(arg_1_0, 0)] = "exit"

		return

	for iter_1_0 = 0, arg_1_1 - 1:
		local var_1_1 = var_0_10(arg_1_0, iter_1_0)

		if var_1_1 < 0:
			var_1_1 = var_1_1 + 4294967296

		var_1_0[var_1_1] = var_0_22(iter_1_0)

	local var_1_2 = var_0_10(arg_1_0, arg_1_1)

	if var_1_2:
		var_1_0[var_1_2] = "stack_check"

local function var_0_34(arg_2_0, arg_2_1)
	local var_2_0 = var_0_31

	if var_0_32 == 0:
		local var_2_1 = var_0_2.ircall

		for iter_2_0 = 0, #var_2_1:
			local var_2_2 = var_0_11(iter_2_0)

			if var_2_2 != 0:
				if var_2_2 < 0:
					var_2_2 = var_2_2 + 4294967296

				var_2_0[var_2_2] = var_2_1[iter_2_0]

	if var_0_32 == 1000000:
		var_0_33(arg_2_0, arg_2_1)
	elif arg_2_1 > var_0_32:
		for iter_2_1 = var_0_32, arg_2_1 - 1:
			local var_2_3 = var_0_10(iter_2_1)

			if var_2_3 == None:
				var_0_33(arg_2_0, arg_2_1)
				setmetatable(var_0_31, var_0_30)

				arg_2_1 = 1000000

				break

			if var_2_3 < 0:
				var_2_3 = var_2_3 + 4294967296

			var_2_0[var_2_3] = var_0_22(iter_2_1)

		var_0_32 = arg_2_1

	return var_2_0

local function var_0_35(arg_3_0)
	var_0_28.write(arg_3_0)

local function var_0_36(arg_4_0)
	local var_4_0 = var_0_5(arg_4_0)

	if not var_4_0:
		return

	local var_4_1, var_4_2, var_4_3 = var_0_8(arg_4_0)

	if not var_4_1:
		return

	if not var_0_26:
		var_0_26 = require("jit.dis_" .. var_0_0.arch)

	if var_4_2 < 0:
		var_4_2 = var_4_2 + 4294967296

	var_0_28.write("---- TRACE ", arg_4_0, " mcode ", #var_4_1, "\n")

	local var_4_4 = var_0_26.create(var_4_1, var_4_2, var_0_35)

	var_4_4.hexdump = 0
	var_4_4.symtab = var_0_34(arg_4_0, var_4_0.nexit)

	if var_4_3 != 0:
		var_0_31[var_4_2 + var_4_3] = "LOOP"

		var_4_4.disass(0, var_4_3)
		var_0_28.write("->LOOP.\n")
		var_4_4.disass(var_4_3, #var_4_1 - var_4_3)

		var_0_31[var_4_2 + var_4_3] = None
	else
		var_4_4.disass(0, #var_4_1)

local var_0_37 = {
	[0] = "None",
	"fal",
	"tru",
	"lud",
	"str",
	"p32",
	"thr",
	"pro",
	"fun",
	"p64",
	"cdt",
	"tab",
	"udt",
	"flt",
	"num",
	"i8 ",
	"u8 ",
	"i16",
	"u16",
	"int",
	"u32",
	"i64",
	"u64",
	"sfp"
}
local var_0_38 = {
	[0] = "%s",
	"%s",
	"%s",
	"\x1B[36m%s\x1B[m",
	"\x1B[32m%s\x1B[m",
	"%s",
	"\x1B[1m%s\x1B[m",
	"%s",
	"\x1B[1m%s\x1B[m",
	"%s",
	"\x1B[33m%s\x1B[m",
	"\x1B[31m%s\x1B[m",
	"\x1B[36m%s\x1B[m",
	"\x1B[34m%s\x1B[m",
	"\x1B[34m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m",
	"\x1B[35m%s\x1B[m"
}

local function var_0_39(arg_5_0)
	return arg_5_0

local function var_0_40(arg_6_0, arg_6_1)
	return var_0_18(var_0_38[arg_6_1], arg_6_0)

local var_0_41 = setmetatable({}, {
	def __index:(arg_7_0, arg_7_1)
		local var_7_0 = var_0_40(var_0_37[arg_7_1], arg_7_1)

		arg_7_0[arg_7_1] = var_7_0

		return var_7_0
})
local var_0_42 = {
	[">"] = "&gt;",
	["<"] = "&lt;",
	["&"] = "&amp;"
}

local function var_0_43(arg_8_0, arg_8_1)
	arg_8_0 = var_0_17(arg_8_0, "[<>&]", var_0_42)

	return var_0_18("<span class=\"irt_%s\">%s</span>", var_0_37[arg_8_1], arg_8_0)

local var_0_44 = setmetatable({}, {
	def __index:(arg_9_0, arg_9_1)
		local var_9_0 = var_0_43(var_0_37[arg_9_1], arg_9_1)

		arg_9_0[arg_9_1] = var_9_0

		return var_9_0
})
local var_0_45 = "<style type=\"text/css\">\nbackground { background. #ffffff; color. #000000; }\npre.ljdump {\nfont-size. 10pt;\nbackground. #f0f4ff;\ncolor. #000000;\nborder. 1px solid #bfcfff;\npadding. 0.5em;\nmargin-left. 2em;\nmargin-right. 2em;\n}\nspan.irt_str { color. #00a000; }\nspan.irt_thr, span.irt_fun { color. #404040; font-weight. bold; }\nspan.irt_tab { color. #c00000; }\nspan.irt_udt, span.irt_lud { color. #00c0c0; }\nspan.irt_num { color. #4040c0; }\nspan.irt_int, span.irt_i8, span.irt_u8, span.irt_i16, span.irt_u16 { color. #b040b0; }\n</style>\n"
local var_0_46
local var_0_47
local var_0_48 = {
	["SLOAD "] = setmetatable({}, {
		def __index:(arg_10_0, arg_10_1)
			local var_10_0 = ""

			if var_0_13(arg_10_1, 1) != 0:
				var_10_0 = var_10_0 .. "P"

			if var_0_13(arg_10_1, 2) != 0:
				var_10_0 = var_10_0 .. "F"

			if var_0_13(arg_10_1, 4) != 0:
				var_10_0 = var_10_0 .. "T"

			if var_0_13(arg_10_1, 8) != 0:
				var_10_0 = var_10_0 .. "C"

			if var_0_13(arg_10_1, 16) != 0:
				var_10_0 = var_10_0 .. "R"

			if var_0_13(arg_10_1, 32) != 0:
				var_10_0 = var_10_0 .. "I"

			arg_10_0[arg_10_1] = var_10_0

			return var_10_0
	}),
	["XLOAD "] = {
		[0] = "",
		"R",
		"V",
		"RV",
		"U",
		"RU",
		"VU",
		"RVU"
	},
	["CONV  "] = setmetatable({}, {
		def __index:(arg_11_0, arg_11_1)
			local var_11_0 = var_0_47[var_0_13(arg_11_1, 31)]
			local var_11_1 = var_0_47[var_0_13(var_0_14(arg_11_1, 5), 31)] .. "." .. var_11_0

			if var_0_13(arg_11_1, 2048) != 0:
				var_11_1 = var_11_1 .. " sext"

			local var_11_2 = var_0_14(arg_11_1, 14)

			if var_11_2 == 2:
				var_11_1 = var_11_1 .. " index"
			elif var_11_2 == 3:
				var_11_1 = var_11_1 .. " check"

			arg_11_0[arg_11_1] = var_11_1

			return var_11_1
	}),
	["FLOAD "] = var_0_2.irfield,
	["FREF  "] = var_0_2.irfield,
	FPMATH = var_0_2.irfpm,
	BUFHDR = {
		[0] = "RESET",
		"APPEND"
	},
	["TOSTR "] = {
		[0] = "INT",
		"NUM",
		"CHAR"
	}
}

local function var_0_49(arg_12_0)
	if arg_12_0 == "\n":
		return "\\n"
	elif arg_12_0 == "\r":
		return "\\r"
	elif arg_12_0 == "\t":
		return "\\t"
	else
		return var_0_18("\\%03d", var_0_19(arg_12_0))

local function var_0_50(arg_13_0, arg_13_1)
	local var_13_0 = var_0_3(arg_13_0, arg_13_1)

	if var_13_0.loc:
		return var_13_0.loc
	elif var_13_0.ffid:
		return var_0_2.ffnames[var_13_0.ffid]
	elif var_13_0.addr:
		return var_0_18("C.%x", var_13_0.addr)
	else
		return "(?)"

local function var_0_51(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0, var_14_1, var_14_2 = var_0_7(arg_14_0, arg_14_1)
	local var_14_3 = var_0_21(var_14_0)
	local var_14_4

	if var_14_3 == "number":
		if var_0_13(arg_14_2 or 0, 196608) != 0:
			var_14_4 = var_0_13(arg_14_2, 131072) != 0 and "contpc" or "ftsz"
		elif var_14_0 == 6755399441055744:
			var_14_4 = "bias"
		else
			var_14_4 = var_0_18(var_14_0 > 0 and var_14_0 < 1.390671161567e-309 and "%+a" or "%+.14g", var_14_0)
	elif var_14_3 == "string":
		var_14_4 = var_0_18(#var_14_0 > 20 and "\"%.20s\"~" or "\"%s\"", var_0_17(var_14_0, "%c", var_0_49))
	elif var_14_3 == "function":
		var_14_4 = var_0_50(var_14_0)
	elif var_14_3 == "table":
		var_14_4 = var_0_18("{%p}", var_14_0)
	elif var_14_3 == "userdata":
		if var_14_1 == 12:
			var_14_4 = var_0_18("userdata.%p", var_14_0)
		else
			var_14_4 = var_0_18("[%p]", var_14_0)

			if var_14_4 == "[NULL]":
				var_14_4 = "NULL"
	elif var_14_1 == 21:
		var_14_4 = var_0_16(var_0_22(var_14_0), 1, -3)

		if var_0_16(var_14_4, 1, 1) != "-":
			var_14_4 = "+" .. var_14_4
	elif arg_14_2 == 17137663:
		return "----"
	else
		var_14_4 = var_0_22(var_14_0)

	local var_14_5 = var_0_46(var_0_18("%-4s", var_14_4), var_14_1)

	if var_14_2:
		var_14_5 = var_0_18("%s @%d", var_14_5, var_14_2)

	return var_14_5

local function var_0_52(arg_15_0, arg_15_1)
	local var_15_0 = 2

	for iter_15_0 = 0, arg_15_1[1] - 1:
		local var_15_1 = arg_15_1[var_15_0]

		if var_0_14(var_15_1, 24) == iter_15_0:
			var_15_0 = var_15_0 + 1

			local var_15_2 = var_0_13(var_15_1, 65535) - 32768

			if var_15_2 < 0:
				var_0_28.write(var_0_51(arg_15_0, var_15_2, var_15_1))
			elif var_0_13(var_15_1, 524288) != 0:
				var_0_28.write(var_0_46(var_0_18("%04d/%04d", var_15_2, var_15_2 + 1), 14))
			else
				local var_15_3, var_15_4, var_15_5, var_15_6 = var_0_6(arg_15_0, var_15_2)

				var_0_28.write(var_0_46(var_0_18("%04d", var_15_2), var_0_13(var_15_4, 31)))

			var_0_28.write(var_0_13(var_15_1, 65536) == 0 and " " or "|")
		else
			var_0_28.write("---- ")

	var_0_28.write("]\n")

local function var_0_53(arg_16_0)
	var_0_28.write("---- TRACE ", arg_16_0, " snapshots\n")

	for iter_16_0 = 0, 1000000000:
		local var_16_0 = var_0_9(arg_16_0, iter_16_0)

		if not var_16_0:
			break

		var_0_28.write(var_0_18("#%-3d %04d [ ", iter_16_0, var_16_0[0]))
		var_0_52(arg_16_0, var_16_0)

local function var_0_54(arg_17_0, arg_17_1)
	if not var_0_26:
		var_0_26 = require("jit.dis_" .. var_0_0.arch)

	local var_17_0 = var_0_13(arg_17_0, 255)
	local var_17_1 = var_0_14(arg_17_0, 8)

	if var_17_0 == 253 or var_17_0 == 254:
		return (var_17_1 == 0 or var_17_1 == 255) and " {sink" or var_0_18(" {%04d", arg_17_1 - var_17_1)

	if arg_17_0 > 255:
		return var_0_18("[%x]", var_17_1 * 4)

	if var_17_0 < 128:
		return var_0_26.regname(var_17_0)

	return ""

local function var_0_55(arg_18_0, arg_18_1)
	local var_18_0

	if arg_18_1 > 0:
		local var_18_1, var_18_2, var_18_3, var_18_4 = var_0_6(arg_18_0, arg_18_1)

		if var_0_13(var_18_2, 31) == 0:
			arg_18_1 = var_18_3
			var_18_0 = var_0_51(arg_18_0, var_18_4)

	if arg_18_1 < 0:
		var_0_28.write(var_0_18("[0x%x](", tonumber((var_0_7(arg_18_0, arg_18_1)))))
	else
		var_0_28.write(var_0_18("%04d (", arg_18_1))

	return var_18_0

local function var_0_56(arg_19_0, arg_19_1)
	if arg_19_1 < 0:
		var_0_28.write(var_0_51(arg_19_0, arg_19_1))
	else
		local var_19_0, var_19_1, var_19_2, var_19_3 = var_0_6(arg_19_0, arg_19_1)
		local var_19_4 = 6 * var_0_14(var_19_1, 8)

		if var_0_16(var_0_2.irnames, var_19_4 + 1, var_19_4 + 6) == "CARG  ":
			var_0_56(arg_19_0, var_19_2)

			if var_19_3 < 0:
				var_0_28.write(" ", var_0_51(arg_19_0, var_19_3))
			else
				var_0_28.write(" ", var_0_18("%04d", var_19_3))
		else
			var_0_28.write(var_0_18("%04d", arg_19_1))

local function var_0_57(arg_20_0, arg_20_1, arg_20_2)
	local var_20_0 = var_0_5(arg_20_0)

	if not var_20_0:
		return

	local var_20_1 = var_20_0.nins

	var_0_28.write("---- TRACE ", arg_20_0, " IR\n")

	local var_20_2 = var_0_2.irnames
	local var_20_3 = 65536
	local var_20_4
	local var_20_5

	if arg_20_1:
		var_20_4 = var_0_9(arg_20_0, 0)
		var_20_3 = var_20_4[0]
		var_20_5 = 0

	for iter_20_0 = 1, var_20_1:
		if var_20_3 <= iter_20_0:
			if arg_20_2:
				var_0_28.write(var_0_18("....              SNAP   #%-3d [ ", var_20_5))
			else
				var_0_28.write(var_0_18("....        SNAP   #%-3d [ ", var_20_5))

			var_0_52(arg_20_0, var_20_4)

			var_20_5 = var_20_5 + 1
			var_20_4 = var_0_9(arg_20_0, var_20_5)
			var_20_3 = var_20_4 and var_20_4[0] or 65536

		local var_20_6, var_20_7, var_20_8, var_20_9, var_20_10 = var_0_6(arg_20_0, iter_20_0)
		local var_20_11 = 6 * var_0_14(var_20_7, 8)
		local var_20_12 = var_0_13(var_20_7, 31)
		local var_20_13 = var_0_16(var_20_2, var_20_11 + 1, var_20_11 + 6)

		if var_20_13 == "LOOP  ":
			if arg_20_2:
				var_0_28.write(var_0_18("%04d ------------ LOOP ------------\n", iter_20_0))
			else
				var_0_28.write(var_0_18("%04d ------ LOOP ------------\n", iter_20_0))
		elif var_20_13 != "NOP   " and var_20_13 != "CARG  " and (arg_20_2 or var_20_13 != "RENAME"):
			local var_20_14 = var_0_13(var_20_10, 255)

			if arg_20_2:
				var_0_28.write(var_0_18("%04d %-6s", iter_20_0, var_0_54(var_20_10, iter_20_0)))
			else
				var_0_28.write(var_0_18("%04d ", iter_20_0))

			var_0_28.write(var_0_18("%s%s %s %s ", (var_20_14 == 254 or var_20_14 == 253) and "}" or var_0_13(var_20_7, 128) == 0 and " " or ">", var_0_13(var_20_7, 64) == 0 and " " or "+", var_0_47[var_20_12], var_20_13))

			local var_20_15 = var_0_13(var_20_6, 3)
			local var_20_16 = var_0_13(var_20_6, 12)

			if var_0_16(var_20_13, 1, 4) == "CALL":
				local var_20_17

				if var_20_16 == 4:
					var_0_28.write(var_0_18("%-10s  (", var_0_2.ircall[var_20_9]))
				else
					var_20_17 = var_0_55(arg_20_0, var_20_9)

				if var_20_8 != -1:
					var_0_56(arg_20_0, var_20_8)

				var_0_28.write(")")

				if var_20_17:
					var_0_28.write(" ctype ", var_20_17)
			elif var_20_13 == "CNEW  " and var_20_9 == -1:
				var_0_28.write(var_0_51(arg_20_0, var_20_8))
			elif var_20_15 != 3:
				if var_20_8 < 0:
					var_0_28.write(var_0_51(arg_20_0, var_20_8))
				else
					var_0_28.write(var_0_18(var_20_15 == 0 and "%04d" or "#%-3d", var_20_8))

				if var_20_16 != 12:
					if var_20_16 == 4:
						local var_20_18 = var_0_48[var_20_13]

						if var_20_18 and var_20_18[var_20_9]:
							var_0_28.write("  ", var_20_18[var_20_9])
						elif var_20_13 == "UREFO " or var_20_13 == "UREFC ":
							var_0_28.write(var_0_18("  #%-3d", var_0_14(var_20_9, 8)))
						else
							var_0_28.write(var_0_18("  #%-3d", var_20_9))
					elif var_20_9 < 0:
						var_0_28.write("  ", var_0_51(arg_20_0, var_20_9))
					else
						var_0_28.write(var_0_18("  %04d", var_20_9))

			var_0_28.write("\n")

	if var_20_4:
		if arg_20_2:
			var_0_28.write(var_0_18("....              SNAP   #%-3d [ ", var_20_5))
		else
			var_0_28.write(var_0_18("....        SNAP   #%-3d [ ", var_20_5))

		var_0_52(arg_20_0, var_20_4)

local var_0_58 = ""
local var_0_59 = 0

local function var_0_60(arg_21_0, arg_21_1)
	if var_0_21(arg_21_0) == "number":
		if var_0_21(arg_21_1) == "function":
			arg_21_1 = var_0_50(arg_21_1)

		arg_21_0 = var_0_18(var_0_2.traceerr[arg_21_0], arg_21_1)

	return arg_21_0

local function var_0_61(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4, arg_22_5)
	if arg_22_0 == "stop" or arg_22_0 == "abort" and var_0_29.a:
		if var_0_29.i:
			var_0_57(arg_22_1, var_0_29.s, var_0_29.r and arg_22_0 == "stop")
		elif var_0_29.s:
			var_0_53(arg_22_1)

		if var_0_29.m:
			var_0_36(arg_22_1)

	if arg_22_0 == "start":
		if var_0_29.H:
			var_0_28.write("<pre class=\"ljdump\">\n")

		var_0_28.write("---- TRACE ", arg_22_1, " ", arg_22_0)

		if arg_22_4:
			var_0_28.write(" ", arg_22_4, "/", arg_22_5 == -1 and "stitch" or arg_22_5)

		var_0_28.write(" ", var_0_50(arg_22_2, arg_22_3), "\n")
	elif arg_22_0 == "stop" or arg_22_0 == "abort":
		var_0_28.write("---- TRACE ", arg_22_1, " ", arg_22_0)

		if arg_22_0 == "abort":
			var_0_28.write(" ", var_0_50(arg_22_2, arg_22_3), " -- ", var_0_60(arg_22_4, arg_22_5), "\n")
		else
			local var_22_0 = var_0_5(arg_22_1)
			local var_22_1 = var_22_0.link
			local var_22_2 = var_22_0.linktype

			if var_22_1 == arg_22_1 or var_22_1 == 0:
				var_0_28.write(" -> ", var_22_2, "\n")
			elif var_22_2 == "root":
				var_0_28.write(" -> ", var_22_1, "\n")
			else
				var_0_28.write(" -> ", var_22_1, " ", var_22_2, "\n")

		if var_0_29.H:
			var_0_28.write("</pre>\n\n")
		else
			var_0_28.write("\n")
	else
		if arg_22_0 == "flush":
			var_0_31, var_0_32 = {}, 0

		var_0_28.write("---- TRACE ", arg_22_0, "\n\n")

	var_0_28.flush()

local function var_0_62(arg_23_0, arg_23_1, arg_23_2, arg_23_3, arg_23_4)
	if arg_23_3 != var_0_59:
		var_0_59 = arg_23_3
		var_0_58 = var_0_20(" .", arg_23_3)

	local var_23_0

	if arg_23_2 >= 0:
		var_23_0 = var_0_25(arg_23_1, arg_23_2, var_0_58)

		if var_0_29.H:
			var_23_0 = var_0_17(var_23_0, "[<>&]", var_0_42)
	else
		var_23_0 = "0000 " .. var_0_58 .. " FUNCC      \n"
		arg_23_4 = arg_23_1

	if arg_23_2 <= 0:
		var_0_28.write(var_0_16(var_23_0, 1, -2), "         ; ", var_0_50(arg_23_1), "\n")
	else
		var_0_28.write(var_23_0)

	if arg_23_2 >= 0 and var_0_13(var_0_4(arg_23_1, arg_23_2), 255) < 16:
		var_0_28.write(var_0_25(arg_23_1, arg_23_2 + 1, var_0_58))

local function var_0_63(arg_24_0, arg_24_1, arg_24_2, arg_24_3, ...)
	var_0_28.write("---- TRACE ", arg_24_0, " exit ", arg_24_1, "\n")

	if var_0_29.X:
		local var_24_0 = {
			...
		}

		if var_0_0.arch == "x64":
			for iter_24_0 = 1, arg_24_2:
				var_0_28.write(var_0_18(" %016x", var_24_0[iter_24_0]))

				if iter_24_0 % 4 == 0:
					var_0_28.write("\n")
		else
			for iter_24_1 = 1, arg_24_2:
				var_0_28.write(" ", var_0_15(var_24_0[iter_24_1]))

				if iter_24_1 % 8 == 0:
					var_0_28.write("\n")

		if var_0_0.arch == "mips" or var_0_0.arch == "mipsel":
			for iter_24_2 = 1, arg_24_3, 2:
				var_0_28.write(var_0_18(" %+17.14g", var_24_0[arg_24_2 + iter_24_2]))

				if iter_24_2 % 8 == 7:
					var_0_28.write("\n")
		else
			for iter_24_3 = 1, arg_24_3:
				var_0_28.write(var_0_18(" %+17.14g", var_24_0[arg_24_2 + iter_24_3]))

				if iter_24_3 % 4 == 0:
					var_0_28.write("\n")

local function var_0_64()
	if var_0_27:
		var_0_27 = False

		var_0_0.attach(var_0_63)
		var_0_0.attach(var_0_62)
		var_0_0.attach(var_0_61)

		if var_0_28 and var_0_28 != var_0_23 and var_0_28 != var_0_24:
			var_0_28.close()

		var_0_28 = None

local function var_0_65(arg_26_0, arg_26_1)
	if var_0_27:
		var_0_64()

	local var_26_0 = os.getenv("TERM")
	local var_26_1 = (var_26_0 and var_26_0.match("color") or os.getenv("COLORTERM")) and "A" or "T"

	arg_26_0 = arg_26_0 and var_0_17(arg_26_0, "[TAH]", function(arg_27_0)
		var_26_1 = arg_27_0

		return "")

	local var_26_2 = {
		i = True,
		t = True,
		m = True,
		b = True
	}

	if arg_26_0 and arg_26_0 != "":
		local var_26_3 = var_0_16(arg_26_0, 1, 1)

		if var_26_3 != "+" and var_26_3 != "-":
			var_26_2 = {}

		for iter_26_0 = 1, #arg_26_0:
			var_26_2[var_0_16(arg_26_0, iter_26_0, iter_26_0)] = var_26_3 != "-"

	var_0_29 = var_26_2

	if var_26_2.t or var_26_2.b or var_26_2.i or var_26_2.s or var_26_2.m:
		var_0_0.attach(var_0_61, "trace")

	if var_26_2.b:
		var_0_0.attach(var_0_62, "record")

		if not var_0_25:
			var_0_25 = require("jit.bc").line

	if var_26_2.x or var_26_2.X:
		var_0_0.attach(var_0_63, "texit")

	arg_26_1 = arg_26_1 or os.getenv("LUAJIT_DUMPFILE")

	if arg_26_1:
		var_0_28 = arg_26_1 == "-" and var_0_23 or assert(io.open(arg_26_1, "w"))
	else
		var_0_28 = var_0_23

	var_26_2[var_26_1] = True

	if var_26_1 == "A":
		var_0_46 = var_0_40
		var_0_47 = var_0_41
	elif var_26_1 == "H":
		var_0_46 = var_0_43
		var_0_47 = var_0_44

		var_0_28.write(var_0_45)
	else
		var_0_46 = var_0_39
		var_0_47 = var_0_37

	var_0_27 = True

return {
	on = var_0_65,
	off = var_0_64,
	start = var_0_65
}
