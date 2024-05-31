local var_0_0 = type
local var_0_1 = string.sub
local var_0_2 = string.byte
local var_0_3 = string.format
local var_0_4 = string.match
local var_0_5 = string.gmatch
local var_0_6 = table.concat
local var_0_7 = require("bit")
local var_0_8 = var_0_7.band
local var_0_9 = var_0_7.bor
local var_0_10 = var_0_7.ror
local var_0_11 = var_0_7.tohex
local var_0_12 = var_0_7.lshift
local var_0_13 = var_0_7.rshift
local var_0_14 = var_0_7.arshift
local var_0_15 = {
	shift = 8,
	mask = 15,
	[10] = {
		[0] = {
			[0] = "vmovFmDN",
			"vstmFNdr",
			shift = 23,
			mask = 3,
			_ = {
				[0] = "vstrFdl",
				{
					_ = "vstmdbFNdr",
					shift = 16,
					[13] = "vpushFdr",
					mask = 15
				},
				shift = 21,
				mask = 1
			}
		},
		{
			[0] = "vmovFDNm",
			{
				_ = "vldmFNdr",
				shift = 16,
				[13] = "vpopFdr",
				mask = 15
			},
			shift = 23,
			mask = 3,
			_ = {
				[0] = "vldrFdl",
				"vldmdbFNdr",
				shift = 21,
				mask = 1
			}
		},
		shift = 20,
		mask = 1
	},
	[11] = {
		[0] = {
			[0] = "vmovGmDN",
			"vstmGNdr",
			shift = 23,
			mask = 3,
			_ = {
				[0] = "vstrGdl",
				{
					_ = "vstmdbGNdr",
					shift = 16,
					[13] = "vpushGdr",
					mask = 15
				},
				shift = 21,
				mask = 1
			}
		},
		{
			[0] = "vmovGDNm",
			{
				_ = "vldmGNdr",
				shift = 16,
				[13] = "vpopGdr",
				mask = 15
			},
			shift = 23,
			mask = 3,
			_ = {
				[0] = "vldrGdl",
				"vldmdbGNdr",
				shift = 21,
				mask = 1
			}
		},
		shift = 20,
		mask = 1
	},
	_ = {
		shift = 0,
		mask = 0
	}
}
local var_0_16 = {
	[0] = "vmlaF.dnm",
	"vmlsF.dnm",
	[147456] = "vfnmsF.dnm",
	[163840] = "vfmaF.dnm",
	[16385] = "vnmlaF.dnm",
	mask = 180225,
	[32769] = "vnmulF.dnm",
	[163841] = "vfmsF.dnm",
	[32768] = "vmulF.dnm",
	[180224] = "vmovF.dY",
	[49153] = "vsubF.dnm",
	shift = 6,
	[16384] = "vnmlsF.dnm",
	[49152] = "vaddF.dnm",
	[131072] = "vdivF.dnm",
	[147457] = "vfnmaF.dnm",
	[180225] = {
		[0] = "vmovF.dm",
		"vabsF.dm",
		[513] = "vsqrtF.dm",
		[2049] = "vcmpeF.dm",
		[4096] = "vcvt.f32.u32Fdm",
		mask = 7681,
		[4097] = "vcvt.f32.s32Fdm",
		[2561] = "vcmpzeF.d",
		[2048] = "vcmpF.dm",
		[6145] = "vcvt.u32F.dm",
		[6144] = "vcvtr.u32F.dm",
		[2560] = "vcmpzF.d",
		[6656] = "vcvtr.s32F.dm",
		[6657] = "vcvt.s32F.dm",
		shift = 7,
		[512] = "vnegF.dm",
		[3585] = "vcvtG.dF.m"
	}
}
local var_0_17 = {
	[0] = "vmlaG.dnm",
	"vmlsG.dnm",
	[147456] = "vfnmsG.dnm",
	[163840] = "vfmaG.dnm",
	[16385] = "vnmlaG.dnm",
	mask = 180225,
	[32769] = "vnmulG.dnm",
	[163841] = "vfmsG.dnm",
	[32768] = "vmulG.dnm",
	[180224] = "vmovG.dY",
	[49153] = "vsubG.dnm",
	shift = 6,
	[16384] = "vnmlsG.dnm",
	[49152] = "vaddG.dnm",
	[131072] = "vdivG.dnm",
	[147457] = "vfnmaG.dnm",
	[180225] = {
		[0] = "vmovG.dm",
		"vabsG.dm",
		[513] = "vsqrtG.dm",
		[2049] = "vcmpeG.dm",
		[4096] = "vcvt.f64.u32GdFm",
		mask = 7681,
		[4097] = "vcvt.f64.s32GdFm",
		[2561] = "vcmpzeG.d",
		[2048] = "vcmpG.dm",
		[6145] = "vcvt.u32FdG.m",
		[6144] = "vcvtr.u32FdG.m",
		[2560] = "vcmpzG.d",
		[6656] = "vcvtr.s32FdG.m",
		[6657] = "vcvt.s32FdG.m",
		shift = 7,
		[512] = "vnegG.dm",
		[3585] = "vcvtF.dG.m"
	}
}
local var_0_18 = {
	"svcT",
	shift = 24,
	mask = 1,
	[0] = {
		[0] = {
			shift = 8,
			mask = 15,
			[10] = var_0_16,
			[11] = var_0_17
		},
		{
			shift = 8,
			mask = 15,
			[10] = {
				[0] = "vmovFnD",
				"vmovFDn",
				mask = 15,
				shift = 20,
				[14] = "vmsrD",
				[15] = {
					shift = 12,
					[15] = "vmrs",
					_ = "vmrsD",
					mask = 15
				}
			}
		},
		shift = 4,
		mask = 1
	}
}
local var_0_19 = {
	shift = 0,
	mask = 0
}
local var_0_20 = {
	shift = 0,
	mask = 0
}
local var_0_21 = {
	shift = 0,
	mask = 0
}
local var_0_22 = {
	shift = 0,
	mask = 0
}
local var_0_23 = {
	shift = 0,
	mask = 0
}
local var_0_24 = {
	[0] = False,
	{
		[0] = "sadd16DNM",
		"sasxDNM",
		"ssaxDNM",
		"ssub16DNM",
		"sadd8DNM",
		False,
		False,
		"ssub8DNM",
		shift = 5,
		mask = 7
	},
	{
		[0] = "qadd16DNM",
		"qasxDNM",
		"qsaxDNM",
		"qsub16DNM",
		"qadd8DNM",
		False,
		False,
		"qsub8DNM",
		shift = 5,
		mask = 7
	},
	{
		[0] = "shadd16DNM",
		"shasxDNM",
		"shsaxDNM",
		"shsub16DNM",
		"shadd8DNM",
		False,
		False,
		"shsub8DNM",
		shift = 5,
		mask = 7
	},
	False,
	{
		[0] = "uadd16DNM",
		"uasxDNM",
		"usaxDNM",
		"usub16DNM",
		"uadd8DNM",
		False,
		False,
		"usub8DNM",
		shift = 5,
		mask = 7
	},
	{
		[0] = "uqadd16DNM",
		"uqasxDNM",
		"uqsaxDNM",
		"uqsub16DNM",
		"uqadd8DNM",
		False,
		False,
		"uqsub8DNM",
		shift = 5,
		mask = 7
	},
	{
		[0] = "uhadd16DNM",
		"uhasxDNM",
		"uhsaxDNM",
		"uhsub16DNM",
		"uhadd8DNM",
		False,
		False,
		"uhsub8DNM",
		shift = 5,
		mask = 7
	},
	{
		[0] = "pkhbtDNMU",
		False,
		"pkhtbDNMU",
		{
			shift = 16,
			[15] = "sxtb16DMU",
			_ = "sxtab16DNMU",
			mask = 15
		},
		"pkhbtDNMU",
		"selDNM",
		"pkhtbDNMU",
		shift = 5,
		mask = 7
	},
	False,
	{
		[0] = "ssatDxMu",
		"ssat16DxM",
		"ssatDxMu",
		{
			shift = 16,
			[15] = "sxtbDMU",
			_ = "sxtabDNMU",
			mask = 15
		},
		"ssatDxMu",
		False,
		"ssatDxMu",
		shift = 5,
		mask = 7
	},
	{
		[0] = "ssatDxMu",
		"revDM",
		"ssatDxMu",
		{
			shift = 16,
			[15] = "sxthDMU",
			_ = "sxtahDNMU",
			mask = 15
		},
		"ssatDxMu",
		"rev16DM",
		"ssatDxMu",
		shift = 5,
		mask = 7
	},
	{
		shift = 5,
		mask = 7,
		[3] = {
			shift = 16,
			[15] = "uxtb16DMU",
			_ = "uxtab16DNMU",
			mask = 15
		}
	},
	False,
	{
		[0] = "usatDwMu",
		"usat16DwM",
		"usatDwMu",
		{
			shift = 16,
			[15] = "uxtbDMU",
			_ = "uxtabDNMU",
			mask = 15
		},
		"usatDwMu",
		False,
		"usatDwMu",
		shift = 5,
		mask = 7
	},
	{
		[0] = "usatDwMu",
		"rbitDM",
		"usatDwMu",
		{
			shift = 16,
			[15] = "uxthDMU",
			_ = "uxtahDNMU",
			mask = 15
		},
		"usatDwMu",
		"revshDM",
		"usatDwMu",
		shift = 5,
		mask = 7
	},
	{
		shift = 12,
		mask = 15,
		[15] = {
			"smuadNMS",
			"smuadxNMS",
			"smusdNMS",
			"smusdxNMS",
			shift = 5,
			mask = 7
		},
		_ = {
			[0] = "smladNMSD",
			"smladxNMSD",
			"smlsdNMSD",
			"smlsdxNMSD",
			shift = 5,
			mask = 7
		}
	},
	False,
	False,
	False,
	{
		[0] = "smlaldDNMS",
		"smlaldxDNMS",
		"smlsldDNMS",
		"smlsldxDNMS",
		shift = 5,
		mask = 7
	},
	{
		[0] = {
			shift = 12,
			[15] = "smmulNMS",
			_ = "smmlaNMSD",
			mask = 15
		},
		{
			shift = 12,
			[15] = "smmulrNMS",
			_ = "smmlarNMSD",
			mask = 15
		},
		False,
		False,
		False,
		False,
		"smmlsNMSD",
		"smmlsrNMSD",
		shift = 5,
		mask = 7
	},
	False,
	False,
	{
		shift = 5,
		mask = 7,
		[0] = {
			shift = 12,
			[15] = "usad8NMS",
			_ = "usada8NMSD",
			mask = 15
		}
	},
	False,
	{
		None,
		"sbfxDMvw",
		shift = 5,
		mask = 3
	},
	{
		None,
		"sbfxDMvw",
		shift = 5,
		mask = 3
	},
	{
		shift = 5,
		mask = 3,
		[0] = {
			shift = 0,
			[15] = "bfcDvX",
			_ = "bfiDMvX",
			mask = 15
		}
	},
	{
		shift = 5,
		mask = 3,
		[0] = {
			shift = 0,
			[15] = "bfcDvX",
			_ = "bfiDMvX",
			mask = 15
		}
	},
	{
		None,
		"ubfxDMvw",
		shift = 5,
		mask = 3
	},
	{
		None,
		"ubfxDMvw",
		shift = 5,
		mask = 3
	},
	shift = 20,
	mask = 31
}
local var_0_25 = {
	{
		[0] = "strtDL",
		"ldrtDL",
		None,
		None,
		"strbtDL",
		"ldrbtDL",
		shift = 20,
		mask = 5
	},
	shift = 21,
	mask = 9,
	_ = {
		[0] = "strDL",
		"ldrDL",
		None,
		None,
		"strbDL",
		"ldrbDL",
		shift = 20,
		mask = 5
	}
}
local var_0_26 = {
	[0] = var_0_25,
	var_0_24,
	shift = 4,
	mask = 1
}
local var_0_27 = {
	[0] = {
		[0] = "stmdaNR",
		"stmNR",
		{
			shift = 16,
			mask = 63,
			_ = "stmdbNR",
			[45] = "pushR"
		},
		"stmibNR",
		shift = 23,
		mask = 3
	},
	{
		[0] = "ldmdaNR",
		{
			shift = 16,
			[61] = "popR",
			_ = "ldmNR",
			mask = 63
		},
		"ldmdbNR",
		"ldmibNR",
		shift = 23,
		mask = 3
	},
	shift = 20,
	mask = 1
}
local var_0_28 = {
	[0] = "andDNPs",
	"eorDNPs",
	"subDNPs",
	"rsbDNPs",
	"addDNPs",
	"adcDNPs",
	"sbcDNPs",
	"rscDNPs",
	"tstNP",
	"teqNP",
	"cmpNP",
	"cmnNP",
	"orrDNPs",
	"movDPs",
	"bicDNPs",
	"mvnDPs",
	shift = 21,
	mask = 15
}
local var_0_29 = {
	[0] = "mulNMSs",
	"mlaNMSDs",
	"umaalDNMS",
	"mlsDNMS",
	"umullDNMSs",
	"umlalDNMSs",
	"smullDNMSs",
	"smlalDNMSs",
	shift = 21,
	mask = 7
}
local var_0_30 = {
	[0] = "swpDMN",
	False,
	False,
	False,
	"swpbDMN",
	False,
	False,
	False,
	"strexDMN",
	"ldrexDN",
	"strexdDN",
	"ldrexdDN",
	"strexbDMN",
	"ldrexbDN",
	"strexhDN",
	"ldrexhDN",
	shift = 20,
	mask = 15
}
local var_0_31 = {
	[0] = {
		[0] = "smlabbNMSD",
		"smlatbNMSD",
		"smlabtNMSD",
		"smlattNMSD",
		shift = 5,
		mask = 3
	},
	{
		[0] = "smlawbNMSD",
		"smulwbNMS",
		"smlawtNMSD",
		"smulwtNMS",
		shift = 5,
		mask = 3
	},
	{
		[0] = "smlalbbDNMS",
		"smlaltbDNMS",
		"smlalbtDNMS",
		"smlalttDNMS",
		shift = 5,
		mask = 3
	},
	{
		[0] = "smulbbNMS",
		"smultbNMS",
		"smulbtNMS",
		"smulttNMS",
		shift = 5,
		mask = 3
	},
	shift = 21,
	mask = 3
}
local var_0_32 = {
	[0] = {
		[0] = "mrsD",
		"msrM",
		shift = 21,
		mask = 1
	},
	{
		"bxM",
		False,
		"clzDM",
		shift = 21,
		mask = 3
	},
	{
		"bxjM",
		shift = 21,
		mask = 3
	},
	{
		"blxM",
		shift = 21,
		mask = 3
	},
	False,
	{
		[0] = "qaddDMN",
		"qsubDMN",
		"qdaddDMN",
		"qdsubDMN",
		shift = 21,
		mask = 3
	},
	False,
	{
		"bkptK",
		shift = 21,
		mask = 3
	},
	shift = 4,
	mask = 7
}
local var_0_33 = {
	shift = 4,
	mask = 9,
	[9] = {
		[0] = {
			[0] = var_0_29,
			var_0_30,
			shift = 24,
			mask = 1
		},
		{
			[0] = "strhDL",
			"ldrhDL",
			shift = 20,
			mask = 1
		},
		{
			[0] = "ldrdDL",
			"ldrsbDL",
			shift = 20,
			mask = 1
		},
		{
			[0] = "strdDL",
			"ldrshDL",
			shift = 20,
			mask = 1
		},
		shift = 5,
		mask = 3
	},
	_ = {
		shift = 20,
		mask = 25,
		[16] = {
			[0] = var_0_32,
			var_0_31,
			shift = 7,
			mask = 1
		},
		_ = {
			shift = 0,
			mask = 4294967295,
			[var_0_9(3785359360)] = "nop",
			_ = var_0_28
		}
	}
}
local var_0_34 = {
	[16] = "movwDW",
	mask = 31,
	[20] = "movtDW",
	shift = 20,
	[22] = "msrNW",
	[18] = {
		[0] = "nopv6",
		shift = 0,
		_ = "msrNW",
		mask = 983295
	},
	_ = var_0_28
}
local var_0_35 = {
	[0] = "bB",
	"blB",
	shift = 24,
	mask = 1
}
local var_0_36 = {
	[0] = var_0_33,
	var_0_34,
	var_0_25,
	var_0_26,
	var_0_27,
	var_0_35,
	var_0_15,
	var_0_18
}
local var_0_37 = {
	[0] = False,
	var_0_21,
	var_0_22,
	var_0_23,
	False,
	"blxB",
	var_0_19,
	var_0_20
}
local var_0_38 = {
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
	"sp",
	"lr",
	"pc"
}
local var_0_39 = {
	[0] = "eq",
	"ne",
	"hs",
	"lo",
	"mi",
	"pl",
	"vs",
	"vc",
	"hi",
	"ls",
	"ge",
	"lt",
	"gt",
	"le",
	"al"
}
local var_0_40 = {
	[0] = "lsl",
	"lsr",
	"asr",
	"ror"
}

local function var_0_41(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_0.pos
	local var_1_1 = ""

	if arg_1_0.rel:
		local var_1_2 = arg_1_0.symtab[arg_1_0.rel]

		if var_1_2:
			var_1_1 = "\t->" .. var_1_2
		elif var_0_8(arg_1_0.op, 234881024) != 167772160:
			var_1_1 = "\t; 0x" .. var_0_11(arg_1_0.rel)

	if arg_1_0.hexdump > 0:
		arg_1_0.out(var_0_3("%08x  %s  %-5s %s%s\n", arg_1_0.addr + var_1_0, var_0_11(arg_1_0.op), arg_1_1, var_0_6(arg_1_2, ", "), var_1_1))
	else
		arg_1_0.out(var_0_3("%08x  %-5s %s%s\n", arg_1_0.addr + var_1_0, arg_1_1, var_0_6(arg_1_2, ", "), var_1_1))

	arg_1_0.pos = var_1_0 + 4

local function var_0_42(arg_2_0)
	return var_0_41(arg_2_0, ".long", {
		"0x" .. var_0_11(arg_2_0.op)
	})

local function var_0_43(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = var_0_38[var_0_8(var_0_13(arg_3_1, 16), 15)]
	local var_3_1
	local var_3_2
	local var_3_3 = var_0_8(arg_3_1, 67108864) == 0

	if not var_3_3 and var_0_8(arg_3_1, 33554432) == 0:
		var_3_2 = var_0_8(arg_3_1, 4095)

		if var_0_8(arg_3_1, 8388608) == 0:
			var_3_2 = -var_3_2

		if var_3_0 == "pc":
			arg_3_0.rel = arg_3_0.addr + arg_3_2 + 8 + var_3_2

		var_3_2 = "#" .. var_3_2
	elif var_3_3 and var_0_8(arg_3_1, 4194304) != 0:
		var_3_2 = var_0_8(arg_3_1, 15) + var_0_8(var_0_13(arg_3_1, 4), 240)

		if var_0_8(arg_3_1, 8388608) == 0:
			var_3_2 = -var_3_2

		if var_3_0 == "pc":
			arg_3_0.rel = arg_3_0.addr + arg_3_2 + 8 + var_3_2

		var_3_2 = "#" .. var_3_2
	else
		var_3_2 = var_0_38[var_0_8(arg_3_1, 15)]

		if var_3_3 or var_0_8(arg_3_1, 4064) == 0:
			-- block empty
		elif var_0_8(arg_3_1, 4064) == 96:
			var_3_2 = var_0_3("%s, rrx", var_3_2)
		else
			local var_3_4 = var_0_8(var_0_13(arg_3_1, 7), 31)

			if var_3_4 == 0:
				var_3_4 = 32

			var_3_2 = var_0_3("%s, %s #%d", var_3_2, var_0_40[var_0_8(var_0_13(arg_3_1, 5), 3)], var_3_4)

		if var_0_8(arg_3_1, 8388608) == 0:
			var_3_2 = "-" .. var_3_2

	if var_3_2 == "#0":
		var_3_1 = var_0_3("[%s]", var_3_0)
	elif var_0_8(arg_3_1, 16777216) == 0:
		var_3_1 = var_0_3("[%s], %s", var_3_0, var_3_2)
	else
		var_3_1 = var_0_3("[%s, %s]", var_3_0, var_3_2)

	if var_0_8(arg_3_1, 18874368) == 18874368:
		var_3_1 = var_3_1 .. "!"

	return var_3_1

local function var_0_44(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = var_0_38[var_0_8(var_0_13(arg_4_1, 16), 15)]
	local var_4_1 = var_0_8(arg_4_1, 255) * 4

	if var_0_8(arg_4_1, 8388608) == 0:
		var_4_1 = -var_4_1

	if var_4_0 == "pc":
		arg_4_0.rel = arg_4_0.addr + arg_4_2 + 8 + var_4_1

	if var_4_1 == 0:
		return var_0_3("[%s]", var_4_0)
	else
		return var_0_3("[%s, #%d]", var_4_0, var_4_1)

local function var_0_45(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if arg_5_1 == "s":
		return var_0_3("s%d", 2 * var_0_8(var_0_13(arg_5_0, arg_5_2), 15) + var_0_8(var_0_13(arg_5_0, arg_5_3), 1))
	else
		return var_0_3("d%d", var_0_8(var_0_13(arg_5_0, arg_5_2), 15) + var_0_8(var_0_13(arg_5_0, arg_5_3 - 4), 16))

local function var_0_46(arg_6_0)
	local var_6_0 = arg_6_0.pos
	local var_6_1, var_6_2, var_6_3, var_6_4 = var_0_2(arg_6_0.code, var_6_0 + 1, var_6_0 + 4)
	local var_6_5 = var_0_9(var_0_12(var_6_4, 24), var_0_12(var_6_3, 16), var_0_12(var_6_2, 8), var_6_1)
	local var_6_6 = {}
	local var_6_7 = ""
	local var_6_8
	local var_6_9
	local var_6_10
	local var_6_11

	arg_6_0.op = var_6_5
	arg_6_0.rel = None

	local var_6_12 = var_0_13(var_6_5, 28)
	local var_6_13

	if var_6_12 == 15:
		var_6_13 = var_0_37[var_0_8(var_0_13(var_6_5, 25), 7)]
	else
		if var_6_12 != 14:
			var_6_7 = var_0_39[var_6_12]

		var_6_13 = var_0_36[var_0_8(var_0_13(var_6_5, 25), 7)]

	while var_0_0(var_6_13) != "string":
		if not var_6_13:
			return var_0_42(arg_6_0)

		var_6_13 = var_6_13[var_0_8(var_0_13(var_6_5, var_6_13.shift), var_6_13.mask)] or var_6_13._

	local var_6_14, var_6_15 = var_0_4(var_6_13, "^([a-z0-9]*)(.*)")

	if var_0_1(var_6_15, 1, 1) == ".":
		local var_6_16, var_6_17 = var_0_4(var_6_15, "^([a-z0-9.]*)(.*)")

		var_6_7 = var_6_7 .. var_6_16
		var_6_15 = var_6_17

	for iter_6_0 in var_0_5(var_6_15, "."):
		local var_6_18

		if iter_6_0 == "D":
			var_6_18 = var_0_38[var_0_8(var_0_13(var_6_5, 12), 15)]
		elif iter_6_0 == "N":
			var_6_18 = var_0_38[var_0_8(var_0_13(var_6_5, 16), 15)]
		elif iter_6_0 == "S":
			var_6_18 = var_0_38[var_0_8(var_0_13(var_6_5, 8), 15)]
		elif iter_6_0 == "M":
			var_6_18 = var_0_38[var_0_8(var_6_5, 15)]
		elif iter_6_0 == "d":
			var_6_18 = var_0_45(var_6_5, var_6_11, 12, 22)
		elif iter_6_0 == "n":
			var_6_18 = var_0_45(var_6_5, var_6_11, 16, 7)
		elif iter_6_0 == "m":
			var_6_18 = var_0_45(var_6_5, var_6_11, 0, 5)
		elif iter_6_0 == "P":
			if var_0_8(var_6_5, 33554432) != 0:
				var_6_18 = var_0_10(var_0_8(var_6_5, 255), 2 * var_0_8(var_0_13(var_6_5, 8), 15))
			else
				var_6_18 = var_0_38[var_0_8(var_6_5, 15)]

				if var_0_8(var_6_5, 4080) != 0:
					var_6_6[#var_6_6 + 1] = var_6_18

					local var_6_19 = var_0_40[var_0_8(var_0_13(var_6_5, 5), 3)]
					local var_6_20

					if var_0_8(var_6_5, 3984) == 0:
						if var_6_19 == "ror":
							var_6_19 = "rrx"
						else
							var_6_20 = "#32"
					elif var_0_8(var_6_5, 16) == 0:
						var_6_20 = "#" .. var_0_8(var_0_13(var_6_5, 7), 31)
					else
						var_6_20 = var_0_38[var_0_8(var_0_13(var_6_5, 8), 15)]

					if var_6_14 == "mov":
						var_6_14 = var_6_19
						var_6_18 = var_6_20
					elif var_6_20:
						var_6_18 = var_0_3("%s %s", var_6_19, var_6_20)
					else
						var_6_18 = var_6_19
		elif iter_6_0 == "L":
			var_6_18 = var_0_43(arg_6_0, var_6_5, var_6_0)
		elif iter_6_0 == "l":
			var_6_18 = var_0_44(arg_6_0, var_6_5, var_6_0)
		elif iter_6_0 == "B":
			local var_6_21 = arg_6_0.addr + var_6_0 + 8 + var_0_14(var_0_12(var_6_5, 8), 6)

			if var_6_12 == 15:
				var_6_21 = var_6_21 + var_0_8(var_0_13(var_6_5, 23), 2)

			arg_6_0.rel = var_6_21
			var_6_18 = "0x" .. var_0_11(var_6_21)
		elif iter_6_0 == "F":
			var_6_11 = "s"
		elif iter_6_0 == "G":
			var_6_11 = "d"
		elif iter_6_0 == ".":
			var_6_7 = var_6_7 .. (var_6_11 == "s" and ".f32" or ".f64")
		elif iter_6_0 == "R":
			if var_0_8(var_6_5, 2097152) != 0 and #var_6_6 == 1:
				var_6_6[1] = var_6_6[1] .. "!"

			local var_6_22 = {}

			for iter_6_1 = 0, 15:
				if var_0_8(var_0_13(var_6_5, iter_6_1), 1) == 1:
					var_6_22[#var_6_22 + 1] = var_0_38[iter_6_1]

			var_6_18 = "{" .. var_0_6(var_6_22, ", ") .. "}"
		elif iter_6_0 == "r":
			if var_0_8(var_6_5, 2097152) != 0 and #var_6_6 == 2:
				var_6_6[1] = var_6_6[1] .. "!"

			local var_6_23 = tonumber(var_0_1(var_6_8, 2))
			local var_6_24 = var_0_8(var_6_5, 255)

			if var_6_11 == "d":
				var_6_24 = var_0_13(var_6_24, 1)

			var_6_6[#var_6_6] = var_0_3("{%s-%s%d}", var_6_8, var_6_11, var_6_23 + var_6_24 - 1)
		elif iter_6_0 == "W":
			var_6_18 = var_0_8(var_6_5, 4095) + var_0_8(var_0_13(var_6_5, 4), 61440)
		elif iter_6_0 == "T":
			var_6_18 = "#0x" .. var_0_11(var_0_8(var_6_5, 16777215), 6)
		elif iter_6_0 == "U":
			var_6_18 = var_0_8(var_0_13(var_6_5, 7), 31)

			if var_6_18 == 0:
				var_6_18 = None
		elif iter_6_0 == "u":
			var_6_18 = var_0_8(var_0_13(var_6_5, 7), 31)

			if var_0_8(var_6_5, 64) == 0:
				if var_6_18 == 0:
					var_6_18 = None
				else
					var_6_18 = "lsl #" .. var_6_18
			elif var_6_18 == 0:
				var_6_18 = "asr #32"
			else
				var_6_18 = "asr #" .. var_6_18
		elif iter_6_0 == "v":
			var_6_18 = var_0_8(var_0_13(var_6_5, 7), 31)
		elif iter_6_0 == "w":
			var_6_18 = var_0_8(var_0_13(var_6_5, 16), 31)
		elif iter_6_0 == "x":
			var_6_18 = var_0_8(var_0_13(var_6_5, 16), 31) + 1
		elif iter_6_0 == "X":
			var_6_18 = var_0_8(var_0_13(var_6_5, 16), 31) - var_6_8 + 1
		elif iter_6_0 == "Y":
			var_6_18 = var_0_8(var_0_13(var_6_5, 12), 240) + var_0_8(var_6_5, 15)
		elif iter_6_0 == "K":
			var_6_18 = "#0x" .. var_0_11(var_0_8(var_0_13(var_6_5, 4), 65520) + var_0_8(var_6_5, 15), 4)
		elif iter_6_0 == "s":
			if var_0_8(var_6_5, 1048576) != 0:
				var_6_7 = "s" .. var_6_7
		else
			assert(False)

		if var_6_18:
			var_6_8 = var_6_18

			if var_0_0(var_6_18) == "number":
				var_6_18 = "#" .. var_6_18

			var_6_6[#var_6_6 + 1] = var_6_18

	return var_0_41(arg_6_0, var_6_14 .. var_6_7, var_6_6)

local function var_0_47(arg_7_0, arg_7_1, arg_7_2)
	arg_7_1 = arg_7_1 or 0

	local var_7_0 = arg_7_2 and arg_7_1 + arg_7_2 or #arg_7_0.code

	arg_7_0.pos = arg_7_1
	arg_7_0.rel = None

	while var_7_0 > arg_7_0.pos:
		var_0_46(arg_7_0)

local function var_0_48(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = {
		code = arg_8_0,
		addr = arg_8_1 or 0,
		out = arg_8_2 or io.write,
		symtab = {},
		disass = var_0_47
	}

	var_8_0.hexdump = 8

	return var_8_0

local function var_0_49(arg_9_0, arg_9_1, arg_9_2)
	var_0_48(arg_9_0, arg_9_1, arg_9_2).disass()

local function var_0_50(arg_10_0)
	if arg_10_0 < 16:
		return var_0_38[arg_10_0]

	return "d" .. arg_10_0 - 16

return {
	create = var_0_48,
	disass = var_0_49,
	regname = var_0_50
}
