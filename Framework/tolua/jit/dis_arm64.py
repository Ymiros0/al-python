local var_0_0 = type
local var_0_1 = string.sub
local var_0_2 = string.byte
local var_0_3 = string.format
local var_0_4 = string.match
local var_0_5 = string.gmatch
local var_0_6 = string.gsub
local var_0_7 = table.concat
local var_0_8 = require("bit")
local var_0_9 = var_0_8.band
local var_0_10 = var_0_8.bor
local var_0_11 = var_0_8.bxor
local var_0_12 = var_0_8.tohex
local var_0_13 = var_0_8.lshift
local var_0_14 = var_0_8.rshift
local var_0_15 = var_0_8.arshift
local var_0_16 = var_0_8.ror
local var_0_17 = {
	[0] = "adrDBx",
	"adrpDBx",
	shift = 31,
	mask = 1
}
local var_0_18 = {
	[0] = "add|movDNIg",
	"adds|cmnD0NIg",
	"subDNIg",
	"subs|cmpD0NIg",
	shift = 29,
	mask = 3
}
local var_0_19 = {
	[0] = {
		False,
		shift = 22,
		mask = 1,
		[0] = {
			[0] = "andDNig",
			"orr|movDN0ig",
			"eorDNig",
			"ands|tstD0Nig",
			shift = 29,
			mask = 3
		}
	},
	{
		[0] = "andDNig",
		"orr|movDN0ig",
		"eorDNig",
		"ands|tstD0Nig",
		shift = 29,
		mask = 3
	},
	shift = 31,
	mask = 1
}
local var_0_20 = {
	[0] = {
		False,
		shift = 22,
		mask = 1,
		[0] = {
			[0] = "movnDWRg",
			False,
			"movz|movDYRg",
			"movkDWRg",
			shift = 29,
			mask = 3
		}
	},
	{
		[0] = "movnDWRg",
		False,
		"movz|movDYRg",
		"movkDWRg",
		shift = 29,
		mask = 3
	},
	shift = 31,
	mask = 1
}
local var_0_21 = {
	[0] = {
		shift = 22,
		mask = 1,
		[0] = {
			[0] = "sbfm|sbfiz|sbfx|asr|sxtw|sxth|sxtbDN12w",
			"bfm|bfi|bfxilDN13w",
			"ubfm|ubfiz|ubfx|lsr|lsl|uxth|uxtbDN12w",
			shift = 29,
			mask = 3
		}
	},
	{
		{
			[0] = "sbfm|sbfiz|sbfx|asr|sxtw|sxth|sxtbDN12x",
			"bfm|bfi|bfxilDN13x",
			"ubfm|ubfiz|ubfx|lsr|lsl|uxth|uxtbDN12x",
			shift = 29,
			mask = 3
		},
		shift = 22,
		mask = 1
	},
	shift = 31,
	mask = 1
}
local var_0_22 = {
	[0] = var_0_17,
	var_0_17,
	var_0_18,
	False,
	var_0_19,
	var_0_20,
	var_0_21,
	{
		[0] = "extr|rorDNM4w",
		shift = 15,
		[65665] = "extr|rorDNM4x",
		[65664] = "extr|rorDNM4x",
		mask = 114881
	},
	shift = 23,
	mask = 7
}
local var_0_23 = {
	[0] = {
		False,
		shift = 15,
		mask = 1,
		[0] = {
			[0] = {
				[0] = "andDNMSg",
				"bicDNMSg",
				"andDNMSg",
				"bicDNMSg",
				"andDNMSg",
				"bicDNMSg",
				"andDNMg",
				"bicDNMg",
				shift = 21,
				mask = 7
			},
			{
				[0] = "orr|movDN0MSg",
				"orn|mvnDN0MSg",
				"orr|movDN0MSg",
				"orn|mvnDN0MSg",
				"orr|movDN0MSg",
				"orn|mvnDN0MSg",
				"orr|movDN0Mg",
				"orn|mvnDN0Mg",
				shift = 21,
				mask = 7
			},
			{
				[0] = "eorDNMSg",
				"eonDNMSg",
				"eorDNMSg",
				"eonDNMSg",
				"eorDNMSg",
				"eonDNMSg",
				"eorDNMg",
				"eonDNMg",
				shift = 21,
				mask = 7
			},
			{
				[0] = "ands|tstD0NMSg",
				"bicsDNMSg",
				"ands|tstD0NMSg",
				"bicsDNMSg",
				"ands|tstD0NMSg",
				"bicsDNMSg",
				"ands|tstD0NMg",
				"bicsDNMg",
				shift = 21,
				mask = 7
			},
			shift = 29,
			mask = 3
		}
	},
	{
		[0] = {
			[0] = "andDNMSg",
			"bicDNMSg",
			"andDNMSg",
			"bicDNMSg",
			"andDNMSg",
			"bicDNMSg",
			"andDNMg",
			"bicDNMg",
			shift = 21,
			mask = 7
		},
		{
			[0] = "orr|movDN0MSg",
			"orn|mvnDN0MSg",
			"orr|movDN0MSg",
			"orn|mvnDN0MSg",
			"orr|movDN0MSg",
			"orn|mvnDN0MSg",
			"orr|movDN0Mg",
			"orn|mvnDN0Mg",
			shift = 21,
			mask = 7
		},
		{
			[0] = "eorDNMSg",
			"eonDNMSg",
			"eorDNMSg",
			"eonDNMSg",
			"eorDNMSg",
			"eonDNMSg",
			"eorDNMg",
			"eonDNMg",
			shift = 21,
			mask = 7
		},
		{
			[0] = "ands|tstD0NMSg",
			"bicsDNMSg",
			"ands|tstD0NMSg",
			"bicsDNMSg",
			"ands|tstD0NMSg",
			"bicsDNMSg",
			"ands|tstD0NMg",
			"bicsDNMg",
			shift = 21,
			mask = 7
		},
		shift = 29,
		mask = 3
	},
	shift = 31,
	mask = 1
}
local var_0_24 = {
	[0] = {
		False,
		shift = 15,
		mask = 1,
		[0] = {
			[0] = {
				[0] = "addDNMSg",
				"addDNMSg",
				"addDNMSg",
				"addDNMg",
				shift = 22,
				mask = 3
			},
			{
				[0] = "adds|cmnD0NMSg",
				"adds|cmnD0NMSg",
				"adds|cmnD0NMSg",
				"adds|cmnD0NMg",
				shift = 22,
				mask = 3
			},
			{
				[0] = "sub|negDN0MSg",
				"sub|negDN0MSg",
				"sub|negDN0MSg",
				"sub|negDN0Mg",
				shift = 22,
				mask = 3
			},
			{
				[0] = "subs|cmp|negsD0N0MzSg",
				"subs|cmp|negsD0N0MzSg",
				"subs|cmp|negsD0N0MzSg",
				"subs|cmp|negsD0N0Mzg",
				shift = 22,
				mask = 3
			},
			shift = 29,
			mask = 3
		}
	},
	{
		[0] = {
			[0] = "addDNMSg",
			"addDNMSg",
			"addDNMSg",
			"addDNMg",
			shift = 22,
			mask = 3
		},
		{
			[0] = "adds|cmnD0NMSg",
			"adds|cmnD0NMSg",
			"adds|cmnD0NMSg",
			"adds|cmnD0NMg",
			shift = 22,
			mask = 3
		},
		{
			[0] = "sub|negDN0MSg",
			"sub|negDN0MSg",
			"sub|negDN0MSg",
			"sub|negDN0Mg",
			shift = 22,
			mask = 3
		},
		{
			[0] = "subs|cmp|negsD0N0MzSg",
			"subs|cmp|negsD0N0MzSg",
			"subs|cmp|negsD0N0MzSg",
			"subs|cmp|negsD0N0Mzg",
			shift = 22,
			mask = 3
		},
		shift = 29,
		mask = 3
	},
	shift = 31,
	mask = 1
}
local var_0_25 = {
	[0] = var_0_24,
	var_0_24,
	var_0_24,
	shift = 22,
	mask = 3
}
local var_0_26 = {
	shift = 22,
	mask = 3,
	[0] = {
		[0] = "addDNMXg",
		"adds|cmnD0NMXg",
		"subDNMXg",
		"subs|cmpD0NMzXg",
		shift = 29,
		mask = 3
	}
}
local var_0_27 = {
	shift = 10,
	mask = 63,
	[0] = {
		[0] = "adcDNMg",
		"adcsDNMg",
		"sbc|ngcDN0Mg",
		"sbcs|ngcsDN0Mg",
		shift = 29,
		mask = 3
	}
}
local var_0_28 = {
	shift = 4,
	mask = 1,
	[0] = {
		shift = 10,
		mask = 3,
		[0] = {
			"ccmnNMVCg",
			False,
			"ccmpNMVCg",
			shift = 29,
			mask = 3
		},
		[2] = {
			"ccmnN5VCg",
			False,
			"ccmpN5VCg",
			shift = 29,
			mask = 3
		}
	}
}
local var_0_29 = {
	shift = 11,
	mask = 1,
	[0] = {
		[0] = {
			[0] = "cselDNMzCg",
			False,
			"csinv|cinv|csetmDNMcg",
			False,
			shift = 29,
			mask = 3
		},
		{
			[0] = "csinc|cinc|csetDNMcg",
			False,
			"csneg|cnegDNMcg",
			False,
			shift = 29,
			mask = 3
		},
		shift = 10,
		mask = 1
	}
}
local var_0_30 = {
	shift = 29,
	mask = 1,
	[0] = {
		[0] = {
			[0] = "rbitDNg",
			"rev16DNg",
			"revDNw",
			False,
			"clzDNg",
			"clsDNg",
			shift = 10,
			mask = 2047
		},
		{
			[0] = "rbitDNg",
			"rev16DNg",
			"rev32DNx",
			"revDNx",
			"clzDNg",
			"clsDNg",
			shift = 10,
			mask = 2047
		},
		shift = 31,
		mask = 1
	}
}
local var_0_31 = {
	shift = 29,
	mask = 1,
	[0] = {
		False,
		"udivDNMg",
		"sdivDNMg",
		False,
		False,
		False,
		False,
		"lslDNMg",
		"lsrDNMg",
		"asrDNMg",
		"rorDNMg",
		shift = 10,
		mask = 63
	}
}
local var_0_32 = {
	False,
	False,
	False,
	[0] = {
		shift = 21,
		mask = 7,
		[0] = {
			[0] = "madd|mulDNMA0g",
			"msub|mnegDNMA0g",
			shift = 15,
			mask = 1
		}
	},
	{
		[0] = {
			[0] = "madd|mulDNMA0g",
			"smaddl|smullDxNMwA0x",
			"smulhDNMx",
			False,
			False,
			"umaddl|umullDxNMwA0x",
			"umulhDNMx",
			shift = 21,
			mask = 7
		},
		{
			[0] = "msub|mnegDNMA0g",
			"smsubl|smneglDxNMwA0x",
			False,
			False,
			False,
			"umsubl|umneglDxNMwA0x",
			shift = 21,
			mask = 7
		},
		shift = 15,
		mask = 1
	},
	shift = 29,
	mask = 7
}
local var_0_33 = {
	[0] = {
		[0] = var_0_23,
		{
			[0] = var_0_25,
			var_0_26,
			shift = 21,
			mask = 1
		},
		shift = 24,
		mask = 1
	},
	{
		False,
		[0] = var_0_27,
		var_0_28,
		False,
		var_0_29,
		False,
		{
			[0] = var_0_31,
			var_0_30,
			shift = 30,
			mask = 1
		},
		False,
		var_0_32,
		var_0_32,
		var_0_32,
		var_0_32,
		var_0_32,
		var_0_32,
		var_0_32,
		var_0_32,
		shift = 21,
		mask = 15
	},
	shift = 28,
	mask = 1
}
local var_0_34 = {
	[0] = {
		[0] = "ldrDwB",
		"ldrDxB",
		"ldrswDxB",
		shift = 30,
		mask = 3
	},
	{
		[0] = "ldrDsB",
		"ldrDdB",
		shift = 30,
		mask = 3
	},
	shift = 26,
	mask = 1
}
local var_0_35 = {
	[0] = {
		shift = 26,
		mask = 1,
		[0] = {
			[0] = "strbDwzL",
			"ldrbDwzL",
			"ldrsbDxzL",
			"ldrsbDwzL",
			shift = 22,
			mask = 3
		}
	},
	{
		shift = 26,
		mask = 1,
		[0] = {
			[0] = "strhDwzL",
			"ldrhDwzL",
			"ldrshDxzL",
			"ldrshDwzL",
			shift = 22,
			mask = 3
		}
	},
	{
		[0] = {
			[0] = "strDwzL",
			"ldrDwzL",
			"ldrswDxzL",
			shift = 22,
			mask = 3
		},
		{
			[0] = "strDszL",
			"ldrDszL",
			shift = 22,
			mask = 3
		},
		shift = 26,
		mask = 1
	},
	{
		[0] = {
			[0] = "strDxzL",
			"ldrDxzL",
			shift = 22,
			mask = 3
		},
		{
			[0] = "strDdzL",
			"ldrDdzL",
			shift = 22,
			mask = 3
		},
		shift = 26,
		mask = 1
	},
	shift = 30,
	mask = 3
}
local var_0_36 = {
	[0] = {
		[0] = {
			shift = 26,
			mask = 1,
			[0] = {
				[0] = {
					[0] = "sturbDwK",
					"ldurbDwK",
					shift = 22,
					mask = 3
				},
				{
					[0] = "sturhDwK",
					"ldurhDwK",
					shift = 22,
					mask = 3
				},
				{
					[0] = "sturDwK",
					"ldurDwK",
					shift = 22,
					mask = 3
				},
				{
					[0] = "sturDxK",
					"ldurDxK",
					shift = 22,
					mask = 3
				},
				shift = 30,
				mask = 3
			}
		},
		var_0_35,
		False,
		var_0_35,
		shift = 10,
		mask = 3
	},
	{
		shift = 10,
		mask = 3,
		[2] = {
			[0] = {
				[0] = {
					[0] = "strbDwO",
					"ldrbDwO",
					"ldrsbDxO",
					"ldrsbDwO",
					shift = 22,
					mask = 3
				},
				{
					[0] = "strhDwO",
					"ldrhDwO",
					"ldrshDxO",
					"ldrshDwO",
					shift = 22,
					mask = 3
				},
				{
					[0] = "strDwO",
					"ldrDwO",
					"ldrswDxO",
					shift = 22,
					mask = 3
				},
				{
					[0] = "strDxO",
					"ldrDxO",
					shift = 22,
					mask = 3
				},
				shift = 30,
				mask = 3
			},
			{
				shift = 30,
				mask = 3,
				[2] = {
					[0] = "strDsO",
					"ldrDsO",
					shift = 22,
					mask = 3
				},
				[3] = {
					[0] = "strDdO",
					"ldrDdO",
					shift = 22,
					mask = 3
				}
			},
			shift = 26,
			mask = 1
		}
	},
	shift = 21,
	mask = 1
}
local var_0_37 = {
	[0] = {
		[0] = {
			[0] = "stpDzAzwP",
			"stpDzAzsP",
			shift = 26,
			mask = 1
		},
		{
			"stpDzAzdP",
			shift = 26,
			mask = 1
		},
		{
			[0] = "stpDzAzxP",
			shift = 26,
			mask = 1
		},
		shift = 30,
		mask = 3
	},
	{
		[0] = {
			[0] = "ldpDzAzwP",
			"ldpDzAzsP",
			shift = 26,
			mask = 1
		},
		{
			[0] = "ldpswDAxP",
			"ldpDzAzdP",
			shift = 26,
			mask = 1
		},
		{
			[0] = "ldpDzAzxP",
			shift = 26,
			mask = 1
		},
		shift = 30,
		mask = 3
	},
	shift = 22,
	mask = 1
}
local var_0_38 = {
	shift = 24,
	mask = 49,
	[16] = var_0_34,
	[48] = var_0_36,
	[32] = {
		var_0_37,
		var_0_37,
		var_0_37,
		shift = 23,
		mask = 3
	},
	[33] = {
		var_0_37,
		var_0_37,
		var_0_37,
		shift = 23,
		mask = 3
	},
	[49] = {
		[0] = {
			[0] = {
				[0] = "strbDwzU",
				"ldrbDwzU",
				shift = 22,
				mask = 3
			},
			{
				[0] = "strhDwzU",
				"ldrhDwzU",
				shift = 22,
				mask = 3
			},
			{
				[0] = "strDwzU",
				"ldrDwzU",
				shift = 22,
				mask = 3
			},
			{
				[0] = "strDxzU",
				"ldrDxzU",
				shift = 22,
				mask = 3
			},
			shift = 30,
			mask = 3
		},
		{
			shift = 30,
			mask = 3,
			[2] = {
				[0] = "strDszU",
				"ldrDszU",
				shift = 22,
				mask = 3
			},
			[3] = {
				[0] = "strDdzU",
				"ldrDdzU",
				shift = 22,
				mask = 3
			}
		},
		shift = 26,
		mask = 1
	}
}
local var_0_39 = {
	{
		[0] = {
			{
				[0] = {
					[0] = {
						[0] = {
							[0] = {
								shift = 15,
								mask = 1,
								[0] = {
									[0] = {
										[57] = "fcvtzuDwNs",
										[121] = "fcvtzuDwNd",
										[104] = "fcvtpsDwNd",
										[112] = "fcvtmsDwNd",
										[96] = "fcvtnsDwNd",
										[97] = "fcvtnuDwNd",
										[113] = "fcvtmuDwNd",
										[33] = "fcvtnuDwNs",
										[39] = "fmovDsNw",
										[120] = "fcvtzsDwNd",
										[38] = "fmovDwNs",
										[40] = "fcvtpsDwNs",
										[56] = "fcvtzsDwNs",
										[49] = "fcvtmuDwNs",
										[32] = "fcvtnsDwNs",
										shift = 16,
										[36] = "fcvtasDwNs",
										[100] = "fcvtasDwNd",
										mask = 255,
										[48] = "fcvtmsDwNs",
										[101] = "fcvtauDwNd",
										[35] = "ucvtfDsNw",
										[37] = "fcvtauDwNs",
										[98] = "scvtfDdNw",
										[41] = "fcvtpuDwNs",
										[99] = "ucvtfDdNw",
										[105] = "fcvtpuDwNd",
										[34] = "scvtfDsNw"
									},
									{
										[96] = "fcvtnsDxNd",
										[121] = "fcvtzuDxNd",
										[104] = "fcvtpsDxNd",
										[112] = "fcvtmsDxNd",
										[113] = "fcvtmuDxNd",
										[97] = "fcvtnuDxNd",
										[120] = "fcvtzsDxNd",
										[33] = "fcvtnuDxNs",
										[57] = "fcvtzuDxNs",
										[102] = "fmovDxNd",
										[40] = "fcvtpsDxNs",
										[35] = "ucvtfDsNx",
										[49] = "fcvtmuDxNs",
										[103] = "fmovDdNx",
										[32] = "fcvtnsDxNs",
										shift = 16,
										[36] = "fcvtasDxNs",
										[100] = "fcvtasDxNd",
										mask = 255,
										[48] = "fcvtmsDxNs",
										[101] = "fcvtauDxNd",
										[56] = "fcvtzsDxNs",
										[37] = "fcvtauDxNs",
										[98] = "scvtfDdNx",
										[41] = "fcvtpuDxNs",
										[99] = "ucvtfDdNx",
										[105] = "fcvtpuDxNd",
										[34] = "scvtfDsNx"
									},
									shift = 31,
									mask = 1
								}
							},
							{
								shift = 31,
								mask = 1,
								[0] = {
									[0] = {
										[0] = "fmovDNf",
										"fabsDNf",
										"fnegDNf",
										"fsqrtDNf",
										False,
										"fcvtDdNs",
										False,
										False,
										"frintnDNf",
										"frintpDNf",
										"frintmDNf",
										"frintzDNf",
										"frintaDNf",
										False,
										"frintxDNf",
										"frintiDNf",
										shift = 15,
										mask = 63
									},
									{
										[0] = "fmovDNf",
										"fabsDNf",
										"fnegDNf",
										"fsqrtDNf",
										"fcvtDsNd",
										False,
										False,
										False,
										"frintnDNf",
										"frintpDNf",
										"frintmDNf",
										"frintzDNf",
										"frintaDNf",
										False,
										"frintxDNf",
										"frintiDNf",
										shift = 15,
										mask = 63
									},
									shift = 22,
									mask = 3
								}
							},
							shift = 14,
							mask = 1
						},
						{
							shift = 31,
							mask = 1,
							[0] = {
								shift = 14,
								mask = 3,
								[0] = {
									shift = 23,
									mask = 1,
									[0] = {
										[0] = "fcmpNMf",
										[24] = "fcmpeNZf",
										shift = 0,
										[16] = "fcmpeNMf",
										mask = 31,
										[8] = "fcmpNZf"
									}
								}
							}
						},
						shift = 13,
						mask = 1
					},
					{
						shift = 31,
						mask = 1,
						[0] = {
							shift = 5,
							mask = 31,
							[0] = {
								[0] = "fmovDFf",
								shift = 23,
								mask = 1
							}
						}
					},
					shift = 12,
					mask = 1
				},
				{
					shift = 31,
					mask = 1,
					[0] = {
						shift = 23,
						mask = 1,
						[0] = {
							[0] = "fccmpNMVCf",
							"fccmpeNMVCf",
							shift = 4,
							mask = 1
						}
					}
				},
				{
					shift = 31,
					mask = 1,
					[0] = {
						shift = 23,
						mask = 1,
						[0] = {
							[0] = "fmulDNMf",
							"fdivDNMf",
							"faddDNMf",
							"fsubDNMf",
							"fmaxDNMf",
							"fminDNMf",
							"fmaxnmDNMf",
							"fminnmDNMf",
							"fnmulDNMf",
							shift = 12,
							mask = 15
						}
					}
				},
				{
					shift = 31,
					mask = 1,
					[0] = {
						[0] = "fcselDNMCf",
						shift = 23,
						mask = 1
					}
				},
				shift = 10,
				mask = 3
			},
			shift = 21,
			mask = 1
		},
		{
			shift = 31,
			mask = 1,
			[0] = {
				[0] = {
					[0] = "fmaddDNMAf",
					"fnmaddDNMAf",
					shift = 21,
					mask = 5
				},
				{
					[0] = "fmsubDNMAf",
					"fnmsubDNMAf",
					shift = 21,
					mask = 5
				},
				shift = 15,
				mask = 1
			}
		},
		shift = 24,
		mask = 1
	},
	shift = 28,
	mask = 7
}
local var_0_40 = {
	[0] = "bB",
	{
		[0] = "cbzDBg",
		"cbnzDBg",
		"tbzDTBw",
		"tbnzDTBw",
		shift = 24,
		mask = 3
	},
	{
		shift = 24,
		mask = 3,
		[0] = {
			shift = 4,
			mask = 1,
			[0] = {
				[0] = "beqB",
				"bneB",
				"bhsB",
				"bloB",
				"bmiB",
				"bplB",
				"bvsB",
				"bvcB",
				"bhiB",
				"blsB",
				"bgeB",
				"bltB",
				"bgtB",
				"bleB",
				"balB",
				shift = 0,
				mask = 15
			}
		}
	},
	False,
	"blB",
	{
		[0] = "cbzDBg",
		"cbnzDBg",
		"tbzDTBx",
		"tbnzDTBx",
		shift = 24,
		mask = 3
	},
	{
		[0] = {
			shift = 0,
			[2097152] = "brkW",
			mask = 14680095
		},
		{
			[204831] = "nop",
			shift = 0,
			mask = 4194303
		},
		{
			mask = 16776223,
			[4128768] = "blrNx",
			[6225920] = "retNx",
			[2031616] = "brNx",
			shift = 0
		},
		shift = 24,
		mask = 3
	},
	shift = 29,
	mask = 7
}
local var_0_41 = {
	[0] = False,
	False,
	False,
	False,
	var_0_38,
	var_0_33,
	var_0_38,
	var_0_39,
	var_0_22,
	var_0_22,
	var_0_40,
	var_0_40,
	var_0_38,
	var_0_33,
	var_0_38,
	var_0_39,
	shift = 25,
	mask = 15
}
local var_0_42 = {
	x = {},
	w = {},
	d = {},
	s = {}
}

for iter_0_0 = 0, 30:
	var_0_42.x[iter_0_0] = "x" .. iter_0_0
	var_0_42.w[iter_0_0] = "w" .. iter_0_0
	var_0_42.d[iter_0_0] = "d" .. iter_0_0
	var_0_42.s[iter_0_0] = "s" .. iter_0_0

var_0_42.x[31] = "sp"
var_0_42.w[31] = "wsp"
var_0_42.d[31] = "d31"
var_0_42.s[31] = "s31"

local var_0_43 = {
	[0] = "eq",
	"ne",
	"cs",
	"cc",
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
local var_0_44 = {
	[0] = "lsl",
	"lsr",
	"asr"
}
local var_0_45 = {
	[0] = "uxtb",
	"uxth",
	"uxtw",
	"uxtx",
	"sxtb",
	"sxth",
	"sxtw",
	"sxtx"
}

local function var_0_46(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_0.pos
	local var_1_1 = ""

	if arg_1_0.rel:
		local var_1_2 = arg_1_0.symtab[arg_1_0.rel]

		if var_1_2:
			var_1_1 = "\t->" .. var_1_2

	if arg_1_0.hexdump > 0:
		arg_1_0.out(var_0_3("%08x  %s  %-5s %s%s\n", arg_1_0.addr + var_1_0, var_0_12(arg_1_0.op), arg_1_1, var_0_7(arg_1_2, ", "), var_1_1))
	else
		arg_1_0.out(var_0_3("%08x  %-5s %s%s\n", arg_1_0.addr + var_1_0, arg_1_1, var_0_7(arg_1_2, ", "), var_1_1))

	arg_1_0.pos = var_1_0 + 4

local function var_0_47(arg_2_0)
	return var_0_46(arg_2_0, ".long", {
		"0x" .. var_0_12(arg_2_0.op)
	})

local function var_0_48(arg_3_0, arg_3_1, arg_3_2)
	return var_0_42[var_0_4(arg_3_1, arg_3_0 .. "%w-([xwds])")][arg_3_2]

local function var_0_49(arg_4_0)
	if arg_4_0 < 0:
		return var_0_12(arg_4_0)
	else
		return var_0_3("%x", arg_4_0)

local var_0_50 = {
	1431655765,
	286331153,
	16843009,
	65537,
	1
}

local function var_0_51(arg_5_0)
	local var_5_0 = var_0_9(var_0_14(arg_5_0, 10), 63)
	local var_5_1 = var_0_9(var_0_14(arg_5_0, 16), 63)

	if var_0_9(arg_5_0, 4194304) == 0:
		local var_5_2 = 5

		if var_5_0 >= 56:
			if var_5_0 >= 60:
				var_5_2 = 1
			else
				var_5_2 = 2
		elif var_5_0 >= 48:
			var_5_2 = 3
		elif var_5_0 >= 32:
			var_5_2 = 4

		local var_5_3 = var_0_13(1, var_5_2) - 1
		local var_5_4 = var_0_9(var_5_0, var_5_3)
		local var_5_5 = var_0_9(var_5_1, var_5_3)
		local var_5_6 = var_0_16(var_0_14(-1, 31 - var_5_4), var_5_5)

		if var_5_2 != 5:
			var_5_6 = var_0_9(var_5_6, var_0_13(1, var_5_3) - 1) + var_0_14(var_5_6, 31 - var_5_3)

		local var_5_7 = var_5_6 * var_0_50[var_5_2]
		local var_5_8 = var_0_49(var_5_7)

		if var_0_14(arg_5_0, 31) != 0:
			return var_5_8 .. var_0_12(var_5_7)
		else
			return var_5_8
	else
		local var_5_9 = -1
		local var_5_10 = 0

		if var_5_0 < 32:
			var_5_9 = var_0_14(-1, 31 - var_5_0)
		else
			var_5_10 = var_0_14(-1, 63 - var_5_0)

		if var_5_1 != 0:
			var_5_9, var_5_10 = var_0_16(var_5_9, var_5_1), var_0_16(var_5_10, var_5_1)

			local var_5_11 = var_5_1 == 32 and 0 or var_0_9(var_0_11(var_5_9, var_5_10), var_0_13(-1, 32 - var_5_1))

			var_5_9, var_5_10 = var_0_11(var_5_9, var_5_11), var_0_11(var_5_10, var_5_11)

			if var_5_1 >= 32:
				var_5_9, var_5_10 = var_5_10, var_5_9

		if var_5_10 != 0:
			return var_0_49(var_5_10) .. var_0_12(var_5_9)
		else
			return var_0_49(var_5_9)

local function var_0_52(arg_6_0, arg_6_1)
	if arg_6_1 == "b" or arg_6_1 == "bl":
		return var_0_15(var_0_13(arg_6_0, 6), 4)
	elif arg_6_1 == "adr" or arg_6_1 == "adrp":
		local var_6_0 = var_0_9(var_0_14(arg_6_0, 29), 3)
		local var_6_1 = var_0_13(var_0_15(var_0_13(arg_6_0, 8), 13), 2)

		return var_0_10(var_6_1, var_6_0)
	elif arg_6_1 == "tbz" or arg_6_1 == "tbnz":
		return var_0_13(var_0_15(var_0_13(arg_6_0, 13), 18), 2)
	else
		return var_0_13(var_0_15(var_0_13(arg_6_0, 8), 13), 2)

local function var_0_53(arg_7_0)
	local var_7_0 = var_0_9(arg_7_0, 1048576) == 0 and 1 or -1
	local var_7_1 = var_0_11(var_0_14(var_0_15(var_0_13(arg_7_0, 12), 5), 24), 128) - 131

	return var_7_0 * (16 + var_0_9(var_0_14(arg_7_0, 13), 15)) * 2^var_7_1

local function var_0_54(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	if arg_8_2 < arg_8_3 or arg_8_2 == 31 or arg_8_2 == 63:
		return False

	if arg_8_3 == 0:
		if arg_8_0 == 0 and (arg_8_2 == 7 or arg_8_2 == 15):
			return False

		if arg_8_0 != 0 and arg_8_1 == 0 and (arg_8_2 == 7 or arg_8_2 == 15 or arg_8_2 == 31):
			return False

	return True

local function var_0_55(arg_9_0)
	local var_9_0 = arg_9_0.pos
	local var_9_1, var_9_2, var_9_3, var_9_4 = var_0_2(arg_9_0.code, var_9_0 + 1, var_9_0 + 4)
	local var_9_5 = var_0_10(var_0_13(var_9_4, 24), var_0_13(var_9_3, 16), var_0_13(var_9_2, 8), var_9_1)
	local var_9_6 = {}
	local var_9_7 = ""
	local var_9_8
	local var_9_9
	local var_9_10
	local var_9_11

	arg_9_0.op = var_9_5
	arg_9_0.rel = None

	local var_9_12
	local var_9_13
	local var_9_14 = var_0_41[var_0_9(var_0_14(var_9_5, 25), 15)]

	while var_0_0(var_9_14) != "string":
		if not var_9_14:
			return var_0_47(arg_9_0)

		var_9_14 = var_9_14[var_0_9(var_0_14(var_9_5, var_9_14.shift), var_9_14.mask)] or var_9_14._

	local var_9_15, var_9_16 = var_0_4(var_9_14, "^([a-z0-9]*)(.*)")
	local var_9_17, var_9_18 = var_0_4(var_9_16, "|([a-z0-9_.|]*)(.*)")

	if var_9_17:
		var_9_16 = var_9_18

	if var_0_1(var_9_16, 1, 1) == ".":
		local var_9_19, var_9_20 = var_0_4(var_9_16, "^([a-z0-9.]*)(.*)")

		var_9_7 = var_9_7 .. var_9_19
		var_9_16 = var_9_20

	local var_9_21 = var_0_4(var_9_16, "[gf]")

	if var_9_21:
		if var_9_21 == "g":
			var_9_11 = var_0_9(var_9_5, 2147483648) != 0 and var_0_42.x or var_0_42.w
		else
			var_9_11 = var_0_9(var_9_5, 4194304) != 0 and var_0_42.d or var_0_42.s

	local var_9_22
	local var_9_23

	for iter_9_0 in var_0_5(var_9_16, "."):
		local var_9_24

		if iter_9_0 == "D":
			local var_9_25 = var_0_9(var_9_5, 31)

			var_9_24 = var_9_21 and var_9_11[var_9_25] or var_0_48(iter_9_0, var_9_16, var_9_25)
		elif iter_9_0 == "N":
			local var_9_26 = var_0_9(var_0_14(var_9_5, 5), 31)

			var_9_24 = var_9_21 and var_9_11[var_9_26] or var_0_48(iter_9_0, var_9_16, var_9_26)
		elif iter_9_0 == "M":
			local var_9_27 = var_0_9(var_0_14(var_9_5, 16), 31)

			var_9_24 = var_9_21 and var_9_11[var_9_27] or var_0_48(iter_9_0, var_9_16, var_9_27)
		elif iter_9_0 == "A":
			local var_9_28 = var_0_9(var_0_14(var_9_5, 10), 31)

			var_9_24 = var_9_21 and var_9_11[var_9_28] or var_0_48(iter_9_0, var_9_16, var_9_28)
		elif iter_9_0 == "B":
			local var_9_29 = arg_9_0.addr + var_9_0 + var_0_52(var_9_5, var_9_15)

			arg_9_0.rel = var_9_29
			var_9_24 = "0x" .. var_0_12(var_9_29)
		elif iter_9_0 == "T":
			var_9_24 = var_0_10(var_0_9(var_0_14(var_9_5, 26), 32), var_0_9(var_0_14(var_9_5, 19), 31))
		elif iter_9_0 == "V":
			var_9_24 = var_0_9(var_9_5, 15)
		elif iter_9_0 == "C":
			var_9_24 = var_0_43[var_0_9(var_0_14(var_9_5, 12), 15)]
		elif iter_9_0 == "c":
			local var_9_30 = var_0_9(var_0_14(var_9_5, 5), 31)
			local var_9_31 = var_0_9(var_0_14(var_9_5, 16), 31)
			local var_9_32 = var_0_9(var_0_14(var_9_5, 12), 15)
			local var_9_33 = var_0_11(var_9_32, 1)

			var_9_24 = var_0_43[var_9_32]

			if var_9_17 and var_9_32 != 14 and var_9_32 != 15:
				local var_9_34, var_9_35 = var_0_4(var_9_17, "([^|]*)|(.*)")

				if var_9_30 == var_9_31:
					local var_9_36 = #var_9_6

					var_9_6[var_9_36] = None
					var_9_24 = var_0_43[var_9_33]

					if var_9_30 != 31:
						if var_9_34:
							var_9_15 = var_9_34
						else
							var_9_15 = var_9_17
					else
						var_9_6[var_9_36 - 1] = None
						var_9_15 = var_9_35
		elif iter_9_0 == "W":
			var_9_24 = var_0_9(var_0_14(var_9_5, 5), 65535)
		elif iter_9_0 == "Y":
			var_9_24 = var_0_9(var_0_14(var_9_5, 5), 65535)

			local var_9_37 = var_0_9(var_0_14(var_9_5, 21), 3)

			if var_9_17 and (var_9_37 == 0 or var_9_24 != 0):
				var_9_15 = var_9_17
		elif iter_9_0 == "L":
			local var_9_38 = var_0_42.x[var_0_9(var_0_14(var_9_5, 5), 31)]
			local var_9_39 = var_0_15(var_0_13(var_9_5, 11), 23)

			if var_0_9(var_9_5, 2048) != 0:
				var_9_24 = "[" .. var_9_38 .. ", #" .. var_9_39 .. "]!"
			else
				var_9_24 = "[" .. var_9_38 .. "], #" .. var_9_39
		elif iter_9_0 == "U":
			local var_9_40 = var_0_42.x[var_0_9(var_0_14(var_9_5, 5), 31)]
			local var_9_41 = var_0_9(var_0_14(var_9_5, 30), 3)
			local var_9_42 = var_0_13(var_0_15(var_0_13(var_9_5, 10), 20), var_9_41)

			if var_9_42 != 0:
				var_9_24 = "[" .. var_9_40 .. ", #" .. var_9_42 .. "]"
			else
				var_9_24 = "[" .. var_9_40 .. "]"
		elif iter_9_0 == "K":
			local var_9_43 = var_0_42.x[var_0_9(var_0_14(var_9_5, 5), 31)]
			local var_9_44 = var_0_15(var_0_13(var_9_5, 11), 23)

			if var_9_44 != 0:
				var_9_24 = "[" .. var_9_43 .. ", #" .. var_9_44 .. "]"
			else
				var_9_24 = "[" .. var_9_43 .. "]"
		elif iter_9_0 == "O":
			local var_9_45 = var_0_42.x[var_0_9(var_0_14(var_9_5, 5), 31)]
			local var_9_46

			if var_0_9(var_0_14(var_9_5, 13), 1) == 0:
				var_9_46 = var_0_42.w[var_0_9(var_0_14(var_9_5, 16), 31)]
			else
				var_9_46 = var_0_42.x[var_0_9(var_0_14(var_9_5, 16), 31)]

			var_9_24 = "[" .. var_9_45 .. ", " .. var_9_46

			local var_9_47 = var_0_9(var_0_14(var_9_5, 13), 7)
			local var_9_48 = var_0_9(var_0_14(var_9_5, 12), 1)
			local var_9_49 = var_0_9(var_0_14(var_9_5, 30), 3)

			if var_9_47 == 3:
				if var_9_48 == 0:
					var_9_24 = var_9_24 .. "]"
				else
					var_9_24 = var_9_24 .. ", lsl #" .. var_9_49 .. "]"
			elif var_9_47 == 2 or var_9_47 == 6 or var_9_47 == 7:
				if var_9_48 == 0:
					var_9_24 = var_9_24 .. ", " .. var_0_45[var_9_47] .. "]"
				else
					var_9_24 = var_9_24 .. ", " .. var_0_45[var_9_47] .. " #" .. var_9_49 .. "]"
			else
				var_9_24 = var_9_24 .. "]"
		elif iter_9_0 == "P":
			local var_9_50 = var_0_14(var_9_5, 26)
			local var_9_51 = 2

			if var_9_50 >= 42:
				var_9_51 = 4
			elif var_9_50 >= 27:
				var_9_51 = 3

			local var_9_52 = var_0_13(var_0_15(var_0_13(var_9_5, 10), 25), var_9_51)
			local var_9_53 = var_0_42.x[var_0_9(var_0_14(var_9_5, 5), 31)]
			local var_9_54 = var_0_9(var_0_14(var_9_5, 23), 3)

			if var_9_54 == 1:
				var_9_24 = "[" .. var_9_53 .. "], #" .. var_9_52
			elif var_9_54 == 2:
				if var_9_52 == 0:
					var_9_24 = "[" .. var_9_53 .. "]"
				else
					var_9_24 = "[" .. var_9_53 .. ", #" .. var_9_52 .. "]"
			elif var_9_54 == 3:
				var_9_24 = "[" .. var_9_53 .. ", #" .. var_9_52 .. "]!"
		elif iter_9_0 == "I":
			local var_9_55 = var_0_9(var_0_14(var_9_5, 22), 3)
			local var_9_56 = var_0_9(var_0_14(var_9_5, 10), 4095)
			local var_9_57 = var_0_9(var_0_14(var_9_5, 5), 31)
			local var_9_58 = var_0_9(var_9_5, 31)

			if var_9_17 == "mov" and var_9_55 == 0 and var_9_56 == 0 and (var_9_57 == 31 or var_9_58 == 31):
				var_9_15 = var_9_17
				var_9_24 = None
			elif var_9_55 == 0:
				var_9_24 = var_9_56
			elif var_9_55 == 1:
				var_9_24 = var_9_56 .. ", lsl #12"
		elif iter_9_0 == "i":
			var_9_24 = "#0x" .. var_0_51(var_9_5)
		elif iter_9_0 == "1":
			var_9_23 = var_0_9(var_0_14(var_9_5, 16), 63)
			var_9_24 = var_9_23
		elif iter_9_0 == "2":
			var_9_24 = var_0_9(var_0_14(var_9_5, 10), 63)

			if var_9_17:
				local var_9_59, var_9_60, var_9_61, var_9_62, var_9_63, var_9_64 = var_0_4(var_9_17, "([^|]*)|([^|]*)|([^|]*)|([^|]*)|([^|]*)|(.*)")
				local var_9_65 = var_0_9(var_0_14(var_9_5, 26), 32)
				local var_9_66 = var_0_9(var_0_14(var_9_5, 30), 1)

				if var_0_54(var_9_65, var_9_66, var_9_24, var_9_23):
					var_9_15 = var_9_60
					var_9_24 = var_9_24 - var_9_23 + 1
				elif var_9_23 == 0 and var_9_24 == 7:
					local var_9_67 = #var_9_6

					var_9_6[var_9_67] = None

					if var_9_65 != 0:
						var_9_6[var_9_67 - 1] = var_0_6(var_9_6[var_9_67 - 1], "x", "w")

					var_9_12 = var_9_6[var_9_67 - 1]
					var_9_15 = var_9_64
					var_9_24 = None
				elif var_9_23 == 0 and var_9_24 == 15:
					local var_9_68 = #var_9_6

					var_9_6[var_9_68] = None

					if var_9_65 != 0:
						var_9_6[var_9_68 - 1] = var_0_6(var_9_6[var_9_68 - 1], "x", "w")

					var_9_12 = var_9_6[var_9_68 - 1]
					var_9_15 = var_9_63
					var_9_24 = None
				elif var_9_24 == 31 or var_9_24 == 63:
					if var_9_24 == 31 and var_9_23 == 0 and var_9_15 == "sbfm":
						var_9_15 = var_9_62

						local var_9_69 = #var_9_6

						var_9_6[var_9_69] = None

						if var_9_65 != 0:
							var_9_6[var_9_69 - 1] = var_0_6(var_9_6[var_9_69 - 1], "x", "w")

						var_9_12 = var_9_6[var_9_69 - 1]
					else
						var_9_15 = var_9_61

					var_9_24 = None
				elif var_0_9(var_9_24, 31) != 31 and var_9_23 == var_9_24 + 1 and var_9_15 == "ubfm":
					var_9_15 = var_9_62
					var_9_12 = "#" .. var_9_65 + 32 - var_9_23
					var_9_6[#var_9_6] = var_9_12
					var_9_24 = None
				elif var_9_24 < var_9_23:
					var_9_15 = var_9_59
					var_9_12 = "#" .. var_9_65 + 32 - var_9_23
					var_9_6[#var_9_6] = var_9_12
					var_9_24 = var_9_24 + 1
		elif iter_9_0 == "3":
			var_9_24 = var_0_9(var_0_14(var_9_5, 10), 63)

			if var_9_17:
				local var_9_70, var_9_71 = var_0_4(var_9_17, "([^|]*)|(.*)")

				if var_9_24 < var_9_23:
					var_9_15 = var_9_70

					local var_9_72 = var_0_9(var_0_14(var_9_5, 26), 32)

					var_9_12 = "#" .. var_9_72 + 32 - var_9_23
					var_9_6[#var_9_6] = var_9_12
					var_9_24 = var_9_24 + 1
				elif var_9_23 <= var_9_24:
					var_9_15 = var_9_71
					var_9_24 = var_9_24 - var_9_23 + 1
		elif iter_9_0 == "4":
			var_9_24 = var_0_9(var_0_14(var_9_5, 10), 63)

			local var_9_73 = var_0_9(var_0_14(var_9_5, 5), 31)
			local var_9_74 = var_0_9(var_0_14(var_9_5, 16), 31)

			if var_9_17 and var_9_73 == var_9_74:
				local var_9_75 = #var_9_6

				var_9_6[var_9_75] = None
				var_9_12 = var_9_6[var_9_75 - 1]
				var_9_15 = var_9_17
		elif iter_9_0 == "5":
			var_9_24 = var_0_9(var_0_14(var_9_5, 16), 31)
		elif iter_9_0 == "S":
			var_9_24 = var_0_9(var_0_14(var_9_5, 10), 63)

			if var_9_24 == 0:
				var_9_24 = None
			else
				var_9_24 = var_0_44[var_0_9(var_0_14(var_9_5, 22), 3)] .. " #" .. var_9_24
		elif iter_9_0 == "X":
			local var_9_76 = var_0_9(var_0_14(var_9_5, 13), 7)

			if var_9_76 != 3 and var_9_76 != 7:
				var_9_12 = var_0_42.w[var_0_9(var_0_14(var_9_5, 16), 31)]
				var_9_6[#var_9_6] = var_9_12

			var_9_24 = var_0_9(var_0_14(var_9_5, 10), 7)

			if var_9_76 == 2 + var_0_9(var_0_14(var_9_5, 31), 1) and var_0_9(var_0_14(var_9_5, var_9_22 and 5 or 0), 31) == 31:
				if var_9_24 == 0:
					var_9_24 = None
				else
					var_9_24 = "lsl #" .. var_9_24
			elif var_9_24 == 0:
				var_9_24 = var_0_45[var_0_9(var_0_14(var_9_5, 13), 7)]
			else
				var_9_24 = var_0_45[var_0_9(var_0_14(var_9_5, 13), 7)] .. " #" .. var_9_24
		elif iter_9_0 == "R":
			var_9_24 = var_0_9(var_0_14(var_9_5, 21), 3)

			if var_9_24 == 0:
				var_9_24 = None
			else
				var_9_24 = "lsl #" .. var_9_24 * 16
		elif iter_9_0 == "z":
			local var_9_77 = #var_9_6

			if var_9_6[var_9_77] == "sp":
				var_9_6[var_9_77] = "xzr"
			elif var_9_6[var_9_77] == "wsp":
				var_9_6[var_9_77] = "wzr"
		elif iter_9_0 == "Z":
			var_9_24 = 0
		elif iter_9_0 == "F":
			var_9_24 = var_0_53(var_9_5)
		elif iter_9_0 == "g" or iter_9_0 == "f" or iter_9_0 == "x" or iter_9_0 == "w" or iter_9_0 == "d" or iter_9_0 == "s":
			-- block empty
		elif iter_9_0 == "0":
			if var_9_12 == "sp" or var_9_12 == "wsp":
				local var_9_78 = #var_9_6

				var_9_6[var_9_78] = None
				var_9_12 = var_9_6[var_9_78 - 1]

				if var_9_17:
					local var_9_79, var_9_80 = var_0_4(var_9_17, "([^|]*)|(.*)")

					if not var_9_79:
						var_9_15 = var_9_17
					elif var_9_22:
						var_9_15, var_9_17 = var_9_80, var_9_79
					else
						var_9_15, var_9_17 = var_9_79, var_9_80

			var_9_22 = True
		else
			assert(False)

		if var_9_24:
			var_9_12 = var_9_24

			if var_0_0(var_9_24) == "number":
				var_9_24 = "#" .. var_9_24

			var_9_6[#var_9_6 + 1] = var_9_24

	return var_0_46(arg_9_0, var_9_15 .. var_9_7, var_9_6)

local function var_0_56(arg_10_0, arg_10_1, arg_10_2)
	arg_10_1 = arg_10_1 or 0

	local var_10_0 = arg_10_2 and arg_10_1 + arg_10_2 or #arg_10_0.code

	arg_10_0.pos = arg_10_1
	arg_10_0.rel = None

	while var_10_0 > arg_10_0.pos:
		var_0_55(arg_10_0)

local function var_0_57(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = {
		code = arg_11_0,
		addr = arg_11_1 or 0,
		out = arg_11_2 or io.write,
		symtab = {},
		disass = var_0_56
	}

	var_11_0.hexdump = 8

	return var_11_0

local function var_0_58(arg_12_0, arg_12_1, arg_12_2)
	var_0_57(arg_12_0, arg_12_1, arg_12_2).disass()

local function var_0_59(arg_13_0)
	if arg_13_0 < 32:
		return var_0_42.x[arg_13_0]

	return var_0_42.d[arg_13_0 - 32]

return {
	create = var_0_57,
	disass = var_0_58,
	regname = var_0_59
}
