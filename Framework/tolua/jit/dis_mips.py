local var_0_0 = type
local var_0_1 = string.byte
local var_0_2 = string.format
local var_0_3 = string.match
local var_0_4 = string.gmatch
local var_0_5 = table.concat
local var_0_6 = require("bit")
local var_0_7 = var_0_6.band
local var_0_8 = var_0_6.bor
local var_0_9 = var_0_6.tohex
local var_0_10 = var_0_6.lshift
local var_0_11 = var_0_6.rshift
local var_0_12 = var_0_6.arshift
local var_0_13 = {
	[0] = "movfDSC",
	"movtDSC",
	shift = 16,
	mask = 1
}
local var_0_14 = {
	[0] = "srlDTA",
	"rotrDTA",
	shift = 21,
	mask = 1
}
local var_0_15 = {
	[0] = "srlvDTS",
	"rotrvDTS",
	shift = 6,
	mask = 1
}
local var_0_16 = {
	[0] = {
		[0] = "nop",
		shift = 0,
		_ = "sllDTA",
		mask = -1
	},
	var_0_13,
	var_0_14,
	"sraDTA",
	"sllvDTS",
	False,
	var_0_15,
	"sravDTS",
	"jrS",
	"jalrD1S",
	"movzDST",
	"movnDST",
	"syscallY",
	"breakY",
	False,
	"sync",
	"mfhiD",
	"mthiS",
	"mfloD",
	"mtloS",
	"dsllvDST",
	False,
	"dsrlvDST",
	"dsravDST",
	"multST",
	"multuST",
	"divST",
	"divuST",
	"dmultST",
	"dmultuST",
	"ddivST",
	"ddivuST",
	"addDST",
	"addu|moveDST0",
	"subDST",
	"subu|neguDS0T",
	"andDST",
	"or|moveDST0",
	"xorDST",
	"nor|notDST0",
	False,
	False,
	"sltDST",
	"sltuDST",
	"daddDST",
	"dadduDST",
	"dsubDST",
	"dsubuDST",
	"tgeSTZ",
	"tgeuSTZ",
	"tltSTZ",
	"tltuSTZ",
	"teqSTZ",
	False,
	"tneSTZ",
	False,
	"dsllDTA",
	False,
	"dsrlDTA",
	"dsraDTA",
	"dsll32DTA",
	False,
	"dsrl32DTA",
	"dsra32DTA",
	shift = 0,
	mask = 63
}
local var_0_17 = {
	[0] = "maddST",
	"madduST",
	"mulDST",
	False,
	"msubST",
	"msubuST",
	shift = 0,
	[63] = "sdbbpY",
	mask = 63,
	[32] = "clzDS",
	[33] = "cloDS"
}
local var_0_18 = {
	None,
	"wsbhDT",
	[24] = "sehDT",
	shift = 6,
	[16] = "sebDT",
	mask = 31
}
local var_0_19 = {
	None,
	"dsbhDT",
	[5] = "dshdDT",
	shift = 6,
	mask = 31
}
local var_0_20 = {
	[0] = "extTSAK",
	"dextmTSAP",
	None,
	"dextTSAK",
	"insTSAL",
	None,
	"dinsuTSEQ",
	"dinsTSAL",
	[59] = "rdhwrTD",
	shift = 0,
	mask = 63,
	[32] = var_0_18,
	[36] = var_0_19
}
local var_0_21 = {
	[0] = "bltzSB",
	"bgezSB",
	"bltzlSB",
	"bgezlSB",
	False,
	False,
	False,
	False,
	"tgeiSI",
	"tgeiuSI",
	"tltiSI",
	"tltiuSI",
	"teqiSI",
	False,
	"tneiSI",
	False,
	"bltzalSB",
	"bgezalSB",
	"bltzallSB",
	"bgezallSB",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"synciSO",
	shift = 16,
	mask = 31
}
local var_0_22 = {
	[0] = {
		[0] = "mfc0TDW",
		None,
		None,
		None,
		"mtc0TDW",
		mask = 15,
		[10] = "rdpgprDT",
		shift = 21,
		[14] = "wrpgprDT",
		[11] = {
			[0] = "diT0",
			"eiT0",
			shift = 5,
			mask = 1
		}
	},
	{
		"tlbr",
		"tlbwi",
		None,
		None,
		None,
		"tlbwr",
		None,
		"tlbp",
		[24] = "eret",
		shift = 0,
		mask = 63,
		[31] = "deret",
		[32] = "wait"
	},
	shift = 25,
	mask = 1
}
local var_0_23 = {
	[0] = "add.sFGH",
	"sub.sFGH",
	"mul.sFGH",
	"div.sFGH",
	"sqrt.sFG",
	"abs.sFG",
	"mov.sFG",
	"neg.sFG",
	"round.l.sFG",
	"trunc.l.sFG",
	"ceil.l.sFG",
	"floor.l.sFG",
	"round.w.sFG",
	"trunc.w.sFG",
	"ceil.w.sFG",
	"floor.w.sFG",
	False,
	{
		[0] = "movf.sFGC",
		"movt.sFGC",
		shift = 16,
		mask = 1
	},
	"movz.sFGT",
	"movn.sFGT",
	False,
	"recip.sFG",
	"rsqrt.sFG",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"cvt.d.sFG",
	False,
	False,
	"cvt.w.sFG",
	"cvt.l.sFG",
	"cvt.ps.sFGH",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"c.f.sVGH",
	"c.un.sVGH",
	"c.eq.sVGH",
	"c.ueq.sVGH",
	"c.olt.sVGH",
	"c.ult.sVGH",
	"c.ole.sVGH",
	"c.ule.sVGH",
	"c.sf.sVGH",
	"c.ngle.sVGH",
	"c.seq.sVGH",
	"c.ngl.sVGH",
	"c.lt.sVGH",
	"c.nge.sVGH",
	"c.le.sVGH",
	"c.ngt.sVGH",
	shift = 0,
	mask = 63
}
local var_0_24 = {
	[0] = "add.dFGH",
	"sub.dFGH",
	"mul.dFGH",
	"div.dFGH",
	"sqrt.dFG",
	"abs.dFG",
	"mov.dFG",
	"neg.dFG",
	"round.l.dFG",
	"trunc.l.dFG",
	"ceil.l.dFG",
	"floor.l.dFG",
	"round.w.dFG",
	"trunc.w.dFG",
	"ceil.w.dFG",
	"floor.w.dFG",
	False,
	{
		[0] = "movf.dFGC",
		"movt.dFGC",
		shift = 16,
		mask = 1
	},
	"movz.dFGT",
	"movn.dFGT",
	False,
	"recip.dFG",
	"rsqrt.dFG",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"cvt.s.dFG",
	False,
	False,
	False,
	"cvt.w.dFG",
	"cvt.l.dFG",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"c.f.dVGH",
	"c.un.dVGH",
	"c.eq.dVGH",
	"c.ueq.dVGH",
	"c.olt.dVGH",
	"c.ult.dVGH",
	"c.ole.dVGH",
	"c.ule.dVGH",
	"c.df.dVGH",
	"c.ngle.dVGH",
	"c.deq.dVGH",
	"c.ngl.dVGH",
	"c.lt.dVGH",
	"c.nge.dVGH",
	"c.le.dVGH",
	"c.ngt.dVGH",
	shift = 0,
	mask = 63
}
local var_0_25 = {
	[0] = "add.psFGH",
	"sub.psFGH",
	"mul.psFGH",
	False,
	False,
	"abs.psFG",
	"mov.psFG",
	"neg.psFG",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	{
		[0] = "movf.psFGC",
		"movt.psFGC",
		shift = 16,
		mask = 1
	},
	"movz.psFGT",
	"movn.psFGT",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"cvt.s.puFG",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"cvt.s.plFG",
	False,
	False,
	False,
	"pll.psFGH",
	"plu.psFGH",
	"pul.psFGH",
	"puu.psFGH",
	"c.f.psVGH",
	"c.un.psVGH",
	"c.eq.psVGH",
	"c.ueq.psVGH",
	"c.olt.psVGH",
	"c.ult.psVGH",
	"c.ole.psVGH",
	"c.ule.psVGH",
	"c.psf.psVGH",
	"c.ngle.psVGH",
	"c.pseq.psVGH",
	"c.ngl.psVGH",
	"c.lt.psVGH",
	"c.nge.psVGH",
	"c.le.psVGH",
	"c.ngt.psVGH",
	shift = 0,
	mask = 63
}
local var_0_26 = {
	shift = 0,
	mask = 63,
	[32] = "cvt.s.wFG",
	[33] = "cvt.d.wFG"
}
local var_0_27 = {
	shift = 0,
	mask = 63,
	[32] = "cvt.s.lFG",
	[33] = "cvt.d.lFG"
}
local var_0_28 = {
	[0] = "bc1fCB",
	"bc1tCB",
	"bc1flCB",
	"bc1tlCB",
	shift = 16,
	mask = 3
}
local var_0_29 = {
	[0] = "mfc1TG",
	"dmfc1TG",
	"cfc1TG",
	"mfhc1TG",
	"mtc1TG",
	"dmtc1TG",
	"ctc1TG",
	"mthc1TG",
	var_0_28,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	var_0_23,
	var_0_24,
	False,
	False,
	var_0_26,
	var_0_27,
	var_0_25,
	shift = 21,
	mask = 31
}
local var_0_30 = {
	[0] = "lwxc1FSX",
	"ldxc1FSX",
	False,
	False,
	False,
	"luxc1FSX",
	False,
	False,
	"swxc1FSX",
	"sdxc1FSX",
	False,
	False,
	False,
	"suxc1FSX",
	False,
	"prefxMSX",
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	False,
	"alnv.psFGHS",
	False,
	"madd.sFRGH",
	"madd.dFRGH",
	False,
	False,
	False,
	False,
	"madd.psFRGH",
	False,
	"msub.sFRGH",
	"msub.dFRGH",
	False,
	False,
	False,
	False,
	"msub.psFRGH",
	False,
	"nmadd.sFRGH",
	"nmadd.dFRGH",
	False,
	False,
	False,
	False,
	"nmadd.psFRGH",
	False,
	"nmsub.sFRGH",
	"nmsub.dFRGH",
	False,
	False,
	False,
	False,
	"nmsub.psFRGH",
	False,
	shift = 0,
	mask = 63
}
local var_0_31 = {
	[0] = var_0_16,
	var_0_21,
	"jJ",
	"jalJ",
	"beq|beqz|bST00B",
	"bne|bnezST0B",
	"blezSB",
	"bgtzSB",
	"addiTSI",
	"addiu|liTS0I",
	"sltiTSI",
	"sltiuTSI",
	"andiTSU",
	"ori|liTS0U",
	"xoriTSU",
	"luiTU",
	var_0_22,
	var_0_29,
	False,
	var_0_30,
	"beql|beqzlST0B",
	"bnel|bnezlST0B",
	"blezlSB",
	"bgtzlSB",
	"daddiTSI",
	"daddiuTSI",
	False,
	False,
	var_0_17,
	"jalxJ",
	False,
	var_0_20,
	"lbTSO",
	"lhTSO",
	"lwlTSO",
	"lwTSO",
	"lbuTSO",
	"lhuTSO",
	"lwrTSO",
	False,
	"sbTSO",
	"shTSO",
	"swlTSO",
	"swTSO",
	False,
	False,
	"swrTSO",
	"cacheNSO",
	"llTSO",
	"lwc1HSO",
	"lwc2TSO",
	"prefNSO",
	False,
	"ldc1HSO",
	"ldc2TSO",
	"ldTSO",
	"scTSO",
	"swc1HSO",
	"swc2TSO",
	False,
	False,
	"sdc1HSO",
	"sdc2TSO",
	"sdTSO"
}
local var_0_32 = {
	[0] = "r0",
	"r1",
	"r2",
	"r3",
	"r4",
	"r5",
	"r6",
	"r7",
	"r8",
	"r9",
	"r10",
	"r11",
	"r12",
	"r13",
	"r14",
	"r15",
	"r16",
	"r17",
	"r18",
	"r19",
	"r20",
	"r21",
	"r22",
	"r23",
	"r24",
	"r25",
	"r26",
	"r27",
	"r28",
	"sp",
	"r30",
	"ra"
}

local function var_0_33(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_0.pos
	local var_1_1 = ""

	if arg_1_0.rel:
		local var_1_2 = arg_1_0.symtab[arg_1_0.rel]

		if var_1_2:
			var_1_1 = "\t->" .. var_1_2

	if arg_1_0.hexdump > 0:
		arg_1_0.out(var_0_2("%08x  %s  %-7s %s%s\n", arg_1_0.addr + var_1_0, var_0_9(arg_1_0.op), arg_1_1, var_0_5(arg_1_2, ", "), var_1_1))
	else
		arg_1_0.out(var_0_2("%08x  %-7s %s%s\n", arg_1_0.addr + var_1_0, arg_1_1, var_0_5(arg_1_2, ", "), var_1_1))

	arg_1_0.pos = var_1_0 + 4

local function var_0_34(arg_2_0)
	return var_0_33(arg_2_0, ".long", {
		"0x" .. var_0_9(arg_2_0.op)
	})

local function var_0_35(arg_3_0)
	local var_3_0 = arg_3_0.pos
	local var_3_1, var_3_2, var_3_3, var_3_4 = var_0_1(arg_3_0.code, var_3_0 + 1, var_3_0 + 4)

	return var_0_8(var_0_10(var_3_1, 24), var_0_10(var_3_2, 16), var_0_10(var_3_3, 8), var_3_4)

local function var_0_36(arg_4_0)
	local var_4_0 = arg_4_0.pos
	local var_4_1, var_4_2, var_4_3, var_4_4 = var_0_1(arg_4_0.code, var_4_0 + 1, var_4_0 + 4)

	return var_0_8(var_0_10(var_4_4, 24), var_0_10(var_4_3, 16), var_0_10(var_4_2, 8), var_4_1)

local function var_0_37(arg_5_0)
	local var_5_0 = arg_5_0.get()
	local var_5_1 = {}
	local var_5_2

	arg_5_0.op = var_5_0
	arg_5_0.rel = None

	local var_5_3 = var_0_31[var_0_11(var_5_0, 26)]

	while var_0_0(var_5_3) != "string":
		if not var_5_3:
			return var_0_34(arg_5_0)

		var_5_3 = var_5_3[var_0_7(var_0_11(var_5_0, var_5_3.shift), var_5_3.mask)] or var_5_3._

	local var_5_4, var_5_5 = var_0_3(var_5_3, "^([a-z0-9_.]*)(.*)")
	local var_5_6, var_5_7 = var_0_3(var_5_5, "|([a-z0-9_.|]*)(.*)")

	if var_5_6:
		var_5_5 = var_5_7

	for iter_5_0 in var_0_4(var_5_5, "."):
		local var_5_8

		if iter_5_0 == "S":
			var_5_8 = var_0_32[var_0_7(var_0_11(var_5_0, 21), 31)]
		elif iter_5_0 == "T":
			var_5_8 = var_0_32[var_0_7(var_0_11(var_5_0, 16), 31)]
		elif iter_5_0 == "D":
			var_5_8 = var_0_32[var_0_7(var_0_11(var_5_0, 11), 31)]
		elif iter_5_0 == "F":
			var_5_8 = "f" .. var_0_7(var_0_11(var_5_0, 6), 31)
		elif iter_5_0 == "G":
			var_5_8 = "f" .. var_0_7(var_0_11(var_5_0, 11), 31)
		elif iter_5_0 == "H":
			var_5_8 = "f" .. var_0_7(var_0_11(var_5_0, 16), 31)
		elif iter_5_0 == "R":
			var_5_8 = "f" .. var_0_7(var_0_11(var_5_0, 21), 31)
		elif iter_5_0 == "A":
			var_5_8 = var_0_7(var_0_11(var_5_0, 6), 31)
		elif iter_5_0 == "E":
			var_5_8 = var_0_7(var_0_11(var_5_0, 6), 31) + 32
		elif iter_5_0 == "M":
			var_5_8 = var_0_7(var_0_11(var_5_0, 11), 31)
		elif iter_5_0 == "N":
			var_5_8 = var_0_7(var_0_11(var_5_0, 16), 31)
		elif iter_5_0 == "C":
			var_5_8 = var_0_7(var_0_11(var_5_0, 18), 7)

			if var_5_8 == 0:
				var_5_8 = None
		elif iter_5_0 == "K":
			var_5_8 = var_0_7(var_0_11(var_5_0, 11), 31) + 1
		elif iter_5_0 == "P":
			var_5_8 = var_0_7(var_0_11(var_5_0, 11), 31) + 33
		elif iter_5_0 == "L":
			var_5_8 = var_0_7(var_0_11(var_5_0, 11), 31) - var_5_2 + 1
		elif iter_5_0 == "Q":
			var_5_8 = var_0_7(var_0_11(var_5_0, 11), 31) - var_5_2 + 33
		elif iter_5_0 == "I":
			var_5_8 = var_0_12(var_0_10(var_5_0, 16), 16)
		elif iter_5_0 == "U":
			var_5_8 = var_0_7(var_5_0, 65535)
		elif iter_5_0 == "O":
			local var_5_9 = var_0_12(var_0_10(var_5_0, 16), 16)

			var_5_1[#var_5_1] = var_0_2("%d(%s)", var_5_9, var_5_2)
		elif iter_5_0 == "X":
			local var_5_10 = var_0_32[var_0_7(var_0_11(var_5_0, 16), 31)]

			var_5_1[#var_5_1] = var_0_2("%s(%s)", var_5_10, var_5_2)
		elif iter_5_0 == "B":
			var_5_8 = arg_5_0.addr + arg_5_0.pos + var_0_12(var_0_10(var_5_0, 16), 16) * 4 + 4
			arg_5_0.rel = var_5_8
			var_5_8 = var_0_2("0x%08x", var_5_8)
		elif iter_5_0 == "J":
			local var_5_11 = arg_5_0.addr + arg_5_0.pos

			var_5_8 = var_5_11 - var_0_7(var_5_11, 268435455) + var_0_7(var_5_0, 67108863) * 4
			arg_5_0.rel = var_5_8
			var_5_8 = var_0_2("0x%08x", var_5_8)
		elif iter_5_0 == "V":
			var_5_8 = var_0_7(var_0_11(var_5_0, 8), 7)

			if var_5_8 == 0:
				var_5_8 = None
		elif iter_5_0 == "W":
			var_5_8 = var_0_7(var_5_0, 7)

			if var_5_8 == 0:
				var_5_8 = None
		elif iter_5_0 == "Y":
			var_5_8 = var_0_7(var_0_11(var_5_0, 6), 1048575)

			if var_5_8 == 0:
				var_5_8 = None
		elif iter_5_0 == "Z":
			var_5_8 = var_0_7(var_0_11(var_5_0, 6), 1023)

			if var_5_8 == 0:
				var_5_8 = None
		elif iter_5_0 == "0":
			if var_5_2 == "r0" or var_5_2 == 0:
				local var_5_12 = #var_5_1

				var_5_1[var_5_12] = None
				var_5_2 = var_5_1[var_5_12 - 1]

				if var_5_6:
					local var_5_13, var_5_14 = var_0_3(var_5_6, "([^|]*)|(.*)")

					if var_5_13:
						var_5_4, var_5_6 = var_5_13, var_5_14
					else
						var_5_4 = var_5_6
		elif iter_5_0 == "1":
			if var_5_2 == "ra":
				var_5_1[#var_5_1] = None
		else
			assert(False)

		if var_5_8:
			var_5_1[#var_5_1 + 1] = var_5_8
			var_5_2 = var_5_8

	return var_0_33(arg_5_0, var_5_4, var_5_1)

local function var_0_38(arg_6_0, arg_6_1, arg_6_2)
	arg_6_1 = arg_6_1 or 0

	local var_6_0 = arg_6_2 and arg_6_1 + arg_6_2 or #arg_6_0.code
	local var_6_1 = var_6_0 - var_6_0 % 4

	arg_6_0.pos = arg_6_1 - arg_6_1 % 4
	arg_6_0.rel = None

	while var_6_1 > arg_6_0.pos:
		var_0_37(arg_6_0)

local function var_0_39(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = {
		code = arg_7_0,
		addr = arg_7_1 or 0,
		out = arg_7_2 or io.write,
		symtab = {},
		disass = var_0_38
	}

	var_7_0.hexdump = 8
	var_7_0.get = var_0_35

	return var_7_0

local function var_0_40(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = var_0_39(arg_8_0, arg_8_1, arg_8_2)

	var_8_0.get = var_0_36

	return var_8_0

local function var_0_41(arg_9_0, arg_9_1, arg_9_2)
	var_0_39(arg_9_0, arg_9_1, arg_9_2).disass()

local function var_0_42(arg_10_0, arg_10_1, arg_10_2)
	var_0_40(arg_10_0, arg_10_1, arg_10_2).disass()

local function var_0_43(arg_11_0)
	if arg_11_0 < 32:
		return var_0_32[arg_11_0]

	return "f" .. arg_11_0 - 32

return {
	create = var_0_39,
	create_el = var_0_40,
	disass = var_0_41,
	disass_el = var_0_42,
	regname = var_0_43
}
