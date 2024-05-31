local var_0_0 = type
local var_0_1 = string.sub
local var_0_2 = string.byte
local var_0_3 = string.format
local var_0_4 = string.match
local var_0_5 = string.gmatch
local var_0_6 = string.gsub
local var_0_7 = string.lower
local var_0_8 = string.rep
local var_0_9 = require("bit").tohex
local var_0_10 = {
	[0] = "addBmr",
	"addVmr",
	"addBrm",
	"addVrm",
	"addBai",
	"addVai",
	"push es",
	"pop es",
	"orBmr",
	"orVmr",
	"orBrm",
	"orVrm",
	"orBai",
	"orVai",
	"push cs",
	"opc2*",
	"adcBmr",
	"adcVmr",
	"adcBrm",
	"adcVrm",
	"adcBai",
	"adcVai",
	"push ss",
	"pop ss",
	"sbbBmr",
	"sbbVmr",
	"sbbBrm",
	"sbbVrm",
	"sbbBai",
	"sbbVai",
	"push ds",
	"pop ds",
	"andBmr",
	"andVmr",
	"andBrm",
	"andVrm",
	"andBai",
	"andVai",
	"es.seg",
	"daa",
	"subBmr",
	"subVmr",
	"subBrm",
	"subVrm",
	"subBai",
	"subVai",
	"cs.seg",
	"das",
	"xorBmr",
	"xorVmr",
	"xorBrm",
	"xorVrm",
	"xorBai",
	"xorVai",
	"ss.seg",
	"aaa",
	"cmpBmr",
	"cmpVmr",
	"cmpBrm",
	"cmpVrm",
	"cmpBai",
	"cmpVai",
	"ds.seg",
	"aas",
	"incVR",
	"incVR",
	"incVR",
	"incVR",
	"incVR",
	"incVR",
	"incVR",
	"incVR",
	"decVR",
	"decVR",
	"decVR",
	"decVR",
	"decVR",
	"decVR",
	"decVR",
	"decVR",
	"pushUR",
	"pushUR",
	"pushUR",
	"pushUR",
	"pushUR",
	"pushUR",
	"pushUR",
	"pushUR",
	"popUR",
	"popUR",
	"popUR",
	"popUR",
	"popUR",
	"popUR",
	"popUR",
	"popUR",
	"sz*pushaw,pusha",
	"sz*popaw,popa",
	"boundVrm",
	"arplWmr",
	"fs.seg",
	"gs.seg",
	"o16.",
	"a16",
	"pushUi",
	"imulVrmi",
	"pushBs",
	"imulVrms",
	"insb",
	"insVS",
	"outsb",
	"outsVS",
	"joBj",
	"jnoBj",
	"jbBj",
	"jnbBj",
	"jzBj",
	"jnzBj",
	"jbeBj",
	"jaBj",
	"jsBj",
	"jnsBj",
	"jpeBj",
	"jpoBj",
	"jlBj",
	"jgeBj",
	"jleBj",
	"jgBj",
	"arith!Bmi",
	"arith!Vmi",
	"arith!Bmi",
	"arith!Vms",
	"testBmr",
	"testVmr",
	"xchgBrm",
	"xchgVrm",
	"movBmr",
	"movVmr",
	"movBrm",
	"movVrm",
	"movVmg",
	"leaVrm",
	"movWgm",
	"popUm",
	"nop*xchgVaR|pause|xchgWaR|repne nop",
	"xchgVaR",
	"xchgVaR",
	"xchgVaR",
	"xchgVaR",
	"xchgVaR",
	"xchgVaR",
	"xchgVaR",
	"sz*cbw,cwde,cdqe",
	"sz*cwd,cdq,cqo",
	"call farViw",
	"wait",
	"sz*pushfw,pushf",
	"sz*popfw,popf",
	"sahf",
	"lahf",
	"movBao",
	"movVao",
	"movBoa",
	"movVoa",
	"movsb",
	"movsVS",
	"cmpsb",
	"cmpsVS",
	"testBai",
	"testVai",
	"stosb",
	"stosVS",
	"lodsb",
	"lodsVS",
	"scasb",
	"scasVS",
	"movBRi",
	"movBRi",
	"movBRi",
	"movBRi",
	"movBRi",
	"movBRi",
	"movBRi",
	"movBRi",
	"movVRI",
	"movVRI",
	"movVRI",
	"movVRI",
	"movVRI",
	"movVRI",
	"movVRI",
	"movVRI",
	"shift!Bmu",
	"shift!Vmu",
	"retBw",
	"ret",
	"vex*3$lesVrm",
	"vex*2$ldsVrm",
	"movBmi",
	"movVmi",
	"enterBwu",
	"leave",
	"retfBw",
	"retf",
	"int3",
	"intBu",
	"into",
	"iretVS",
	"shift!Bm1",
	"shift!Vm1",
	"shift!Bmc",
	"shift!Vmc",
	"aamBu",
	"aadBu",
	"salc",
	"xlatb",
	"fp*0",
	"fp*1",
	"fp*2",
	"fp*3",
	"fp*4",
	"fp*5",
	"fp*6",
	"fp*7",
	"loopneBj",
	"loopeBj",
	"loopBj",
	"sz*jcxzBj,jecxzBj,jrcxzBj",
	"inBau",
	"inVau",
	"outBua",
	"outVua",
	"callVj",
	"jmpVj",
	"jmp farViw",
	"jmpBj",
	"inBad",
	"inVad",
	"outBda",
	"outVda",
	"lock.",
	"int1",
	"repne.rep",
	"rep.",
	"hlt",
	"cmc",
	"testb!Bm",
	"testv!Vm",
	"clc",
	"stc",
	"cli",
	"sti",
	"cld",
	"std",
	"incb!Bm",
	"incd!Vm"
}

assert(#var_0_10 == 255)

local var_0_11 = setmetatable({
	[96] = False,
	[69] = "rex*rb",
	[130] = False,
	[66] = "rex*x",
	[30] = False,
	[97] = False,
	[197] = "vex*2",
	[22] = False,
	[70] = "rex*rx",
	[206] = False,
	[72] = "rex*w",
	[68] = "rex*r",
	[79] = "rex*wrxb",
	[103] = "a32.",
	[65] = "rex*b",
	[71] = "rex*rxb",
	[6] = False,
	[99] = "movsxdVrDmt",
	[7] = False,
	[74] = "rex*wx",
	[196] = "vex*3",
	[75] = "rex*wxb",
	[154] = False,
	[14] = False,
	[73] = "rex*wb",
	[78] = "rex*wrx",
	[39] = False,
	[47] = False,
	[76] = "rex*wr",
	[55] = False,
	[77] = "rex*wrb",
	[63] = False,
	[214] = False,
	[212] = False,
	[23] = False,
	[213] = False,
	[98] = False,
	[64] = "rex*",
	[234] = False,
	[31] = False,
	[67] = "rex*xb"
}, {
	__index = var_0_10
})
local var_0_12 = {
	[0] = "sldt!Dmp",
	"sgdt!Ump",
	"larVrm",
	"lslVrm",
	None,
	"syscall",
	"clts",
	"sysret",
	"invd",
	"wbinvd",
	None,
	"ud1",
	None,
	"$prefetch!Bm",
	"femms",
	"3dnowMrmu",
	"movupsXrm|movssXrvm|movupdXrm|movsdXrvm",
	"movupsXmr|movssXmvr|movupdXmr|movsdXmvr",
	"movhlpsXrm$movlpsXrm|movsldupXrm|movlpdXrm|movddupXrm",
	"movlpsXmr||movlpdXmr",
	"unpcklpsXrvm||unpcklpdXrvm",
	"unpckhpsXrvm||unpckhpdXrvm",
	"movlhpsXrm$movhpsXrm|movshdupXrm|movhpdXrm",
	"movhpsXmr||movhpdXmr",
	"$prefetcht!Bm",
	"hintnopVm",
	"hintnopVm",
	"hintnopVm",
	"hintnopVm",
	"hintnopVm",
	"hintnopVm",
	"hintnopVm",
	"movUmx$",
	"movUmy$",
	"movUxm$",
	"movUym$",
	"movUmz$",
	None,
	"movUzm$",
	None,
	"movapsXrm||movapdXrm",
	"movapsXmr||movapdXmr",
	"cvtpi2psXrMm|cvtsi2ssXrvVmt|cvtpi2pdXrMm|cvtsi2sdXrvVmt",
	"movntpsXmr|movntssXmr|movntpdXmr|movntsdXmr",
	"cvttps2piMrXm|cvttss2siVrXm|cvttpd2piMrXm|cvttsd2siVrXm",
	"cvtps2piMrXm|cvtss2siVrXm|cvtpd2piMrXm|cvtsd2siVrXm",
	"ucomissXrm||ucomisdXrm",
	"comissXrm||comisdXrm",
	"wrmsr",
	"rdtsc",
	"rdmsr",
	"rdpmc",
	"sysenter",
	"sysexit",
	None,
	"getsec",
	"opc3*38",
	None,
	"opc3*3a",
	None,
	None,
	None,
	None,
	None,
	"cmovoVrm",
	"cmovnoVrm",
	"cmovbVrm",
	"cmovnbVrm",
	"cmovzVrm",
	"cmovnzVrm",
	"cmovbeVrm",
	"cmovaVrm",
	"cmovsVrm",
	"cmovnsVrm",
	"cmovpeVrm",
	"cmovpoVrm",
	"cmovlVrm",
	"cmovgeVrm",
	"cmovleVrm",
	"cmovgVrm",
	"movmskpsVrXm$||movmskpdVrXm$",
	"sqrtpsXrm|sqrtssXrm|sqrtpdXrm|sqrtsdXrm",
	"rsqrtpsXrm|rsqrtssXrvm",
	"rcppsXrm|rcpssXrvm",
	"andpsXrvm||andpdXrvm",
	"andnpsXrvm||andnpdXrvm",
	"orpsXrvm||orpdXrvm",
	"xorpsXrvm||xorpdXrvm",
	"addpsXrvm|addssXrvm|addpdXrvm|addsdXrvm",
	"mulpsXrvm|mulssXrvm|mulpdXrvm|mulsdXrvm",
	"cvtps2pdXrm|cvtss2sdXrvm|cvtpd2psXrm|cvtsd2ssXrvm",
	"cvtdq2psXrm|cvttps2dqXrm|cvtps2dqXrm",
	"subpsXrvm|subssXrvm|subpdXrvm|subsdXrvm",
	"minpsXrvm|minssXrvm|minpdXrvm|minsdXrvm",
	"divpsXrvm|divssXrvm|divpdXrvm|divsdXrvm",
	"maxpsXrvm|maxssXrvm|maxpdXrvm|maxsdXrvm",
	"punpcklbwPrvm",
	"punpcklwdPrvm",
	"punpckldqPrvm",
	"packsswbPrvm",
	"pcmpgtbPrvm",
	"pcmpgtwPrvm",
	"pcmpgtdPrvm",
	"packuswbPrvm",
	"punpckhbwPrvm",
	"punpckhwdPrvm",
	"punpckhdqPrvm",
	"packssdwPrvm",
	"||punpcklqdqXrvm",
	"||punpckhqdqXrvm",
	"movPrVSm",
	"movqMrm|movdquXrm|movdqaXrm",
	"pshufwMrmu|pshufhwXrmu|pshufdXrmu|pshuflwXrmu",
	"pshiftw!Pvmu",
	"pshiftd!Pvmu",
	"pshiftq!Mvmu||pshiftdq!Xvmu",
	"pcmpeqbPrvm",
	"pcmpeqwPrvm",
	"pcmpeqdPrvm",
	"emms*|",
	"vmreadUmr||extrqXmuu$|insertqXrmuu$",
	"vmwriteUrm||extrqXrm$|insertqXrm$",
	None,
	None,
	"||haddpdXrvm|haddpsXrvm",
	"||hsubpdXrvm|hsubpsXrvm",
	"movVSmMr|movqXrm|movVSmXr",
	"movqMmr|movdquXmr|movdqaXmr",
	"joVj",
	"jnoVj",
	"jbVj",
	"jnbVj",
	"jzVj",
	"jnzVj",
	"jbeVj",
	"jaVj",
	"jsVj",
	"jnsVj",
	"jpeVj",
	"jpoVj",
	"jlVj",
	"jgeVj",
	"jleVj",
	"jgVj",
	"setoBm",
	"setnoBm",
	"setbBm",
	"setnbBm",
	"setzBm",
	"setnzBm",
	"setbeBm",
	"setaBm",
	"setsBm",
	"setnsBm",
	"setpeBm",
	"setpoBm",
	"setlBm",
	"setgeBm",
	"setleBm",
	"setgBm",
	"push fs",
	"pop fs",
	"cpuid",
	"btVmr",
	"shldVmru",
	"shldVmrc",
	None,
	None,
	"push gs",
	"pop gs",
	"rsm",
	"btsVmr",
	"shrdVmru",
	"shrdVmrc",
	"fxsave!Dmp",
	"imulVrm",
	"cmpxchgBmr",
	"cmpxchgVmr",
	"$lssVrm",
	"btrVmr",
	"$lfsVrm",
	"$lgsVrm",
	"movzxVrBmt",
	"movzxVrWmt",
	"|popcntVrm",
	"ud2Dp",
	"bt!Vmu",
	"btcVmr",
	"bsfVrm",
	"bsrVrm|lzcntVrm|bsrWrm",
	"movsxVrBmt",
	"movsxVrWmt",
	"xaddBmr",
	"xaddVmr",
	"cmppsXrvmu|cmpssXrvmu|cmppdXrvmu|cmpsdXrvmu",
	"$movntiVmr|",
	"pinsrwPrvWmu",
	"pextrwDrPmu",
	"shufpsXrvmu||shufpdXrvmu",
	"$cmpxchg!Qmp",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"bswapVR",
	"||addsubpdXrvm|addsubpsXrvm",
	"psrlwPrvm",
	"psrldPrvm",
	"psrlqPrvm",
	"paddqPrvm",
	"pmullwPrvm",
	"|movq2dqXrMm|movqXmr|movdq2qMrXm$",
	"pmovmskbVrMm||pmovmskbVrXm",
	"psubusbPrvm",
	"psubuswPrvm",
	"pminubPrvm",
	"pandPrvm",
	"paddusbPrvm",
	"padduswPrvm",
	"pmaxubPrvm",
	"pandnPrvm",
	"pavgbPrvm",
	"psrawPrvm",
	"psradPrvm",
	"pavgwPrvm",
	"pmulhuwPrvm",
	"pmulhwPrvm",
	"|cvtdq2pdXrm|cvttpd2dqXrm|cvtpd2dqXrm",
	"$movntqMmr||$movntdqXmr",
	"psubsbPrvm",
	"psubswPrvm",
	"pminswPrvm",
	"porPrvm",
	"paddsbPrvm",
	"paddswPrvm",
	"pmaxswPrvm",
	"pxorPrvm",
	"|||lddquXrm",
	"psllwPrvm",
	"pslldPrvm",
	"psllqPrvm",
	"pmuludqPrvm",
	"pmaddwdPrvm",
	"psadbwPrvm",
	"maskmovqMrm||maskmovdquXrm$",
	"psubbPrvm",
	"psubwPrvm",
	"psubdPrvm",
	"psubqPrvm",
	"paddbPrvm",
	"paddwPrvm",
	"padddPrvm",
	"ud"
}

assert(var_0_12[255] == "ud")

local var_0_13 = {
	["38"] = {
		[0] = "pshufbPrvm",
		"phaddwPrvm",
		"phadddPrvm",
		"phaddswPrvm",
		"pmaddubswPrvm",
		"phsubwPrvm",
		"phsubdPrvm",
		"phsubswPrvm",
		"psignbPrvm",
		"psignwPrvm",
		"psigndPrvm",
		"pmulhrswPrvm",
		"||permilpsXrvm",
		"||permilpdXrvm",
		None,
		None,
		"||pblendvbXrma",
		None,
		None,
		None,
		"||blendvpsXrma",
		"||blendvpdXrma",
		"||permpsXrvm",
		"||ptestXrm",
		"||broadcastssXrm",
		"||broadcastsdXrm",
		"||broadcastf128XrlXm",
		None,
		"pabsbPrm",
		"pabswPrm",
		"pabsdPrm",
		None,
		"||pmovsxbwXrm",
		"||pmovsxbdXrm",
		"||pmovsxbqXrm",
		"||pmovsxwdXrm",
		"||pmovsxwqXrm",
		"||pmovsxdqXrm",
		None,
		None,
		"||pmuldqXrvm",
		"||pcmpeqqXrvm",
		"||$movntdqaXrm",
		"||packusdwXrvm",
		"||maskmovpsXrvm",
		"||maskmovpdXrvm",
		"||maskmovpsXmvr",
		"||maskmovpdXmvr",
		"||pmovzxbwXrm",
		"||pmovzxbdXrm",
		"||pmovzxbqXrm",
		"||pmovzxwdXrm",
		"||pmovzxwqXrm",
		"||pmovzxdqXrm",
		"||permdXrvm",
		"||pcmpgtqXrvm",
		"||pminsbXrvm",
		"||pminsdXrvm",
		"||pminuwXrvm",
		"||pminudXrvm",
		"||pmaxsbXrvm",
		"||pmaxsdXrvm",
		"||pmaxuwXrvm",
		"||pmaxudXrvm",
		"||pmulddXrvm",
		"||phminposuwXrm",
		None,
		None,
		None,
		"||psrlvVSXrvm",
		"||psravdXrvm",
		"||psllvVSXrvm",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||pbroadcastdXrlXm",
		"||pbroadcastqXrlXm",
		"||broadcasti128XrlXm",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||pbroadcastbXrlXm",
		"||pbroadcastwXrlXm",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||pmaskmovXrvVSm",
		None,
		"||pmaskmovVSmXvr",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||aesencXrvm",
		"||aesenclastXrvm",
		"||aesdecXrvm",
		"||aesdeclastXrvm",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"|||crc32TrBmt",
		"|||crc32TrVmt",
		None,
		None,
		None,
		None,
		None,
		"| sarxVrmv| shlxVrmv| shrxVrmv"
	},
	["3a"] = {
		[0] = "||permqXrmu",
		"||permpdXrmu",
		"||pblenddXrvmu",
		None,
		"||permilpsXrmu",
		"||permilpdXrmu",
		"||perm2f128Xrvmu",
		None,
		"||roundpsXrmu",
		"||roundpdXrmu",
		"||roundssXrvmu",
		"||roundsdXrvmu",
		"||blendpsXrvmu",
		"||blendpdXrvmu",
		"||pblendwXrvmu",
		"palignrPrvmu",
		None,
		None,
		None,
		None,
		"||pextrbVmXru",
		"||pextrwVmXru",
		"||pextrVmSXru",
		"||extractpsVmXru",
		"||insertf128XrvlXmu",
		"||extractf128XlXmYru",
		None,
		None,
		None,
		None,
		None,
		None,
		"||pinsrbXrvVmu",
		"||insertpsXrvmu",
		"||pinsrXrvVmuS",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||inserti128Xrvmu",
		"||extracti128XlXmYru",
		None,
		None,
		None,
		None,
		None,
		None,
		"||dppsXrvmu",
		"||dppdXrvmu",
		"||mpsadbwXrvmu",
		None,
		"||pclmulqdqXrvmu",
		None,
		"||perm2i128Xrvmu",
		None,
		None,
		None,
		"||blendvpsXrvmb",
		"||blendvpdXrvmb",
		"||pblendvbXrvmb",
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		"||pcmpestrmXrmu",
		"||pcmpestriXrmu",
		"||pcmpistrmXrmu",
		"||pcmpistriXrmu",
		[223] = "||aeskeygenassistXrmu",
		[240] = "||| rorxVrmu"
	}
}
local var_0_14 = {
	[217] = "vmmcall",
	[194] = "vmlaunch",
	[222] = "skinit",
	[248] = "swapgs",
	[223] = "invlpga",
	[196] = "vmxoff",
	[220] = "stgi",
	[193] = "vmcall",
	[221] = "clgi",
	[195] = "vmresume",
	[218] = "vmload",
	[201] = "mwait",
	[219] = "vmsave",
	[200] = "monitor",
	[216] = "vmrun",
	[249] = "rdtscp"
}
local var_0_15 = {
	[0] = "faddFm",
	"fmulFm",
	"fcomFm",
	"fcompFm",
	"fsubFm",
	"fsubrFm",
	"fdivFm",
	"fdivrFm",
	"fldFm",
	None,
	"fstFm",
	"fstpFm",
	"fldenvVm",
	"fldcwWm",
	"fnstenvVm",
	"fnstcwWm",
	"fiaddDm",
	"fimulDm",
	"ficomDm",
	"ficompDm",
	"fisubDm",
	"fisubrDm",
	"fidivDm",
	"fidivrDm",
	"fildDm",
	"fisttpDm",
	"fistDm",
	"fistpDm",
	None,
	"fld twordFmp",
	None,
	"fstp twordFmp",
	"faddGm",
	"fmulGm",
	"fcomGm",
	"fcompGm",
	"fsubGm",
	"fsubrGm",
	"fdivGm",
	"fdivrGm",
	"fldGm",
	"fisttpQm",
	"fstGm",
	"fstpGm",
	"frstorDmp",
	None,
	"fnsaveDmp",
	"fnstswWm",
	"fiaddWm",
	"fimulWm",
	"ficomWm",
	"ficompWm",
	"fisubWm",
	"fisubrWm",
	"fidivWm",
	"fidivrWm",
	"fildWm",
	"fisttpWm",
	"fistWm",
	"fistpWm",
	"fbld twordFmp",
	"fildQm",
	"fbstp twordFmp",
	"fistpQm",
	"faddFf",
	"fmulFf",
	"fcomFf",
	"fcompFf",
	"fsubFf",
	"fsubrFf",
	"fdivFf",
	"fdivrFf",
	"fldFf",
	"fxchFf",
	{
		"fnop"
	},
	None,
	{
		"fchs",
		"fabs",
		None,
		None,
		"ftst",
		"fxam"
	},
	{
		"fld1",
		"fldl2t",
		"fldl2e",
		"fldpi",
		"fldlg2",
		"fldln2",
		"fldz"
	},
	{
		"f2xm1",
		"fyl2x",
		"fptan",
		"fpatan",
		"fxtract",
		"fprem1",
		"fdecstp",
		"fincstp"
	},
	{
		"fprem",
		"fyl2xp1",
		"fsqrt",
		"fsincos",
		"frndint",
		"fscale",
		"fsin",
		"fcos"
	},
	"fcmovbFf",
	"fcmoveFf",
	"fcmovbeFf",
	"fcmovuFf",
	None,
	{
		None,
		"fucompp"
	},
	None,
	None,
	"fcmovnbFf",
	"fcmovneFf",
	"fcmovnbeFf",
	"fcmovnuFf",
	{
		None,
		None,
		"fnclex",
		"fninit"
	},
	"fucomiFf",
	"fcomiFf",
	None,
	"fadd toFf",
	"fmul toFf",
	None,
	None,
	"fsub toFf",
	"fsubr toFf",
	"fdivr toFf",
	"fdiv toFf",
	"ffreeFf",
	None,
	"fstFf",
	"fstpFf",
	"fucomFf",
	"fucompFf",
	None,
	None,
	"faddpFf",
	"fmulpFf",
	None,
	{
		None,
		"fcompp"
	},
	"fsubrpFf",
	"fsubpFf",
	"fdivrpFf",
	"fdivpFf",
	None,
	None,
	None,
	None,
	{
		"fnstsw ax"
	},
	"fucomipFf",
	"fcomipFf"
}

assert(var_0_15[126] == "fcomipFf")

local var_0_16 = {
	arith = {
		"add",
		"or",
		"adc",
		"sbb",
		"and",
		"sub",
		"xor",
		"cmp"
	},
	shift = {
		"rol",
		"ror",
		"rcl",
		"rcr",
		"shl",
		"shr",
		"sal",
		"sar"
	},
	testb = {
		"testBmi",
		"testBmi",
		"not",
		"neg",
		"mul",
		"imul",
		"div",
		"idiv"
	},
	testv = {
		"testVmi",
		"testVmi",
		"not",
		"neg",
		"mul",
		"imul",
		"div",
		"idiv"
	},
	incb = {
		"inc",
		"dec"
	},
	incd = {
		"inc",
		"dec",
		"callUmp",
		"$call farDmp",
		"jmpUmp",
		"$jmp farDmp",
		"pushUm"
	},
	sldt = {
		"sldt",
		"str",
		"lldt",
		"ltr",
		"verr",
		"verw"
	},
	sgdt = {
		"vm*$sgdt",
		"vm*$sidt",
		"$lgdt",
		"vm*$lidt",
		"smsw",
		None,
		"lmsw",
		"vm*$invlpg"
	},
	bt = {
		None,
		None,
		None,
		None,
		"bt",
		"bts",
		"btr",
		"btc"
	},
	cmpxchg = {
		None,
		"sz*,cmpxchg8bQmp,cmpxchg16bXmp",
		None,
		None,
		None,
		None,
		"vmptrld|vmxon|vmclear",
		"vmptrst"
	},
	pshiftw = {
		None,
		None,
		"psrlw",
		None,
		"psraw",
		None,
		"psllw"
	},
	pshiftd = {
		None,
		None,
		"psrld",
		None,
		"psrad",
		None,
		"pslld"
	},
	pshiftq = {
		None,
		None,
		"psrlq",
		None,
		None,
		None,
		"psllq"
	},
	pshiftdq = {
		None,
		None,
		"psrlq",
		"psrldq",
		None,
		None,
		"psllq",
		"pslldq"
	},
	fxsave = {
		"$fxsave",
		"$fxrstor",
		"$ldmxcsr",
		"$stmxcsr",
		None,
		"lfenceDp$",
		"mfenceDp$",
		"sfenceDp$clflush"
	},
	prefetch = {
		"prefetch",
		"prefetchw"
	},
	prefetcht = {
		"prefetchnta",
		"prefetcht0",
		"prefetcht1",
		"prefetcht2"
	}
}
local var_0_17 = {
	B = {
		"al",
		"cl",
		"dl",
		"bl",
		"ah",
		"ch",
		"dh",
		"bh",
		"r8b",
		"r9b",
		"r10b",
		"r11b",
		"r12b",
		"r13b",
		"r14b",
		"r15b"
	},
	B64 = {
		"al",
		"cl",
		"dl",
		"bl",
		"spl",
		"bpl",
		"sil",
		"dil",
		"r8b",
		"r9b",
		"r10b",
		"r11b",
		"r12b",
		"r13b",
		"r14b",
		"r15b"
	},
	W = {
		"ax",
		"cx",
		"dx",
		"bx",
		"sp",
		"bp",
		"si",
		"di",
		"r8w",
		"r9w",
		"r10w",
		"r11w",
		"r12w",
		"r13w",
		"r14w",
		"r15w"
	},
	D = {
		"eax",
		"ecx",
		"edx",
		"ebx",
		"esp",
		"ebp",
		"esi",
		"edi",
		"r8d",
		"r9d",
		"r10d",
		"r11d",
		"r12d",
		"r13d",
		"r14d",
		"r15d"
	},
	Q = {
		"rax",
		"rcx",
		"rdx",
		"rbx",
		"rsp",
		"rbp",
		"rsi",
		"rdi",
		"r8",
		"r9",
		"r10",
		"r11",
		"r12",
		"r13",
		"r14",
		"r15"
	},
	M = {
		"mm0",
		"mm1",
		"mm2",
		"mm3",
		"mm4",
		"mm5",
		"mm6",
		"mm7",
		"mm0",
		"mm1",
		"mm2",
		"mm3",
		"mm4",
		"mm5",
		"mm6",
		"mm7"
	},
	X = {
		"xmm0",
		"xmm1",
		"xmm2",
		"xmm3",
		"xmm4",
		"xmm5",
		"xmm6",
		"xmm7",
		"xmm8",
		"xmm9",
		"xmm10",
		"xmm11",
		"xmm12",
		"xmm13",
		"xmm14",
		"xmm15"
	},
	Y = {
		"ymm0",
		"ymm1",
		"ymm2",
		"ymm3",
		"ymm4",
		"ymm5",
		"ymm6",
		"ymm7",
		"ymm8",
		"ymm9",
		"ymm10",
		"ymm11",
		"ymm12",
		"ymm13",
		"ymm14",
		"ymm15"
	}
}
local var_0_18 = {
	"es",
	"cs",
	"ss",
	"ds",
	"fs",
	"gs",
	"segr6",
	"segr7"
}
local var_0_19 = {
	D = 4,
	M = 8,
	Y = 32,
	W = 2,
	Q = 8,
	X = 16,
	B = 1
}
local var_0_20 = {
	G = "qword",
	F = "dword",
	M = "qword",
	Y = "yword",
	Q = "qword",
	X = "xword",
	D = "dword",
	W = "word",
	B = "byte"
}

local function var_0_21(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_0.code
	local var_1_1 = arg_1_0.pos
	local var_1_2 = ""
	local var_1_3 = arg_1_0.hexdump

	if var_1_3 > 0:
		for iter_1_0 = arg_1_0.start, var_1_1 - 1:
			var_1_2 = var_1_2 .. var_0_3("%02X", var_0_2(var_1_0, iter_1_0, iter_1_0))

		if var_1_3 < #var_1_2:
			var_1_2 = var_0_1(var_1_2, 1, var_1_3) .. ". "
		else
			var_1_2 = var_1_2 .. var_0_8(" ", var_1_3 - #var_1_2 + 2)

	if arg_1_2:
		arg_1_1 = arg_1_1 .. " " .. arg_1_2

	if arg_1_0.o16:
		arg_1_1 = "o16 " .. arg_1_1
		arg_1_0.o16 = False

	if arg_1_0.a32:
		arg_1_1 = "a32 " .. arg_1_1
		arg_1_0.a32 = False

	if arg_1_0.rep:
		arg_1_1 = arg_1_0.rep .. " " .. arg_1_1
		arg_1_0.rep = False

	if arg_1_0.rex:
		local var_1_4 = (arg_1_0.rexw and "w" or "") .. (arg_1_0.rexr and "r" or "") .. (arg_1_0.rexx and "x" or "") .. (arg_1_0.rexb and "b" or "") .. (arg_1_0.vexl and "l" or "")

		if arg_1_0.vexv and arg_1_0.vexv != 0:
			var_1_4 = var_1_4 .. "v" .. arg_1_0.vexv

		if var_1_4 != "":
			arg_1_1 = arg_1_0.rex .. "." .. var_1_4 .. " " .. var_0_6(arg_1_1, "^ ", "")
		elif arg_1_0.rex == "vex":
			arg_1_1 = var_0_6("v" .. arg_1_1, "^v ", "")

		arg_1_0.rexw = False
		arg_1_0.rexr = False
		arg_1_0.rexx = False
		arg_1_0.rexb = False
		arg_1_0.rex = False
		arg_1_0.vexl = False
		arg_1_0.vexv = False

	if arg_1_0.seg:
		local var_1_5, var_1_6 = var_0_6(arg_1_1, "%[", "[" .. arg_1_0.seg .. ".")

		if var_1_6 == 0:
			arg_1_1 = arg_1_0.seg .. " " .. arg_1_1
		else
			arg_1_1 = var_1_5

		arg_1_0.seg = False

	if arg_1_0.lock:
		arg_1_1 = "lock " .. arg_1_1
		arg_1_0.lock = False

	local var_1_7 = arg_1_0.imm

	if var_1_7:
		local var_1_8 = arg_1_0.symtab[var_1_7]

		if var_1_8:
			arg_1_1 = arg_1_1 .. "\t->" .. var_1_8

	arg_1_0.out(var_0_3("%08x  %s%s\n", arg_1_0.addr + arg_1_0.start, var_1_2, arg_1_1))

	arg_1_0.mrm = False
	arg_1_0.vexv = False
	arg_1_0.start = var_1_1
	arg_1_0.imm = None

local function var_0_22(arg_2_0)
	arg_2_0.o16 = False
	arg_2_0.seg = False
	arg_2_0.lock = False
	arg_2_0.rep = False
	arg_2_0.rexw = False
	arg_2_0.rexr = False
	arg_2_0.rexx = False
	arg_2_0.rexb = False
	arg_2_0.rex = False
	arg_2_0.a32 = False
	arg_2_0.vexl = False

local function var_0_23(arg_3_0)
	arg_3_0.pos = arg_3_0.stop + 1

	var_0_22(arg_3_0)

	return var_0_21(arg_3_0, "(incomplete)")

local function var_0_24(arg_4_0)
	var_0_22(arg_4_0)

	return var_0_21(arg_4_0, "(unknown)")

local function var_0_25(arg_5_0, arg_5_1, arg_5_2)
	if arg_5_1 + arg_5_2 - 1 > arg_5_0.stop:
		return var_0_23(arg_5_0)

	local var_5_0 = arg_5_0.code

	if arg_5_2 == 1:
		return (var_0_2(var_5_0, arg_5_1, arg_5_1))
	elif arg_5_2 == 2:
		local var_5_1, var_5_2 = var_0_2(var_5_0, arg_5_1, arg_5_1 + 1)

		return var_5_1 + var_5_2 * 256
	else
		local var_5_3, var_5_4, var_5_5, var_5_6 = var_0_2(var_5_0, arg_5_1, arg_5_1 + 3)
		local var_5_7 = var_5_3 + var_5_4 * 256 + var_5_5 * 65536 + var_5_6 * 16777216

		arg_5_0.imm = var_5_7

		return var_5_7

local function var_0_26(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0
	local var_6_1
	local var_6_2
	local var_6_3
	local var_6_4
	local var_6_5
	local var_6_6
	local var_6_7
	local var_6_8
	local var_6_9 = arg_6_0.code
	local var_6_10 = arg_6_0.pos
	local var_6_11 = arg_6_0.stop
	local var_6_12 = arg_6_0.vexl

	for iter_6_0 in var_0_5(arg_6_2, "."):
		local var_6_13

		if iter_6_0 == "V" or iter_6_0 == "U":
			if arg_6_0.rexw:
				var_6_2 = "Q"
				arg_6_0.rexw = False
			elif arg_6_0.o16:
				var_6_2 = "W"
				arg_6_0.o16 = False
			else
				var_6_2 = iter_6_0 == "U" and arg_6_0.x64 and "Q" or "D"

			var_6_1 = var_0_17[var_6_2]
		elif iter_6_0 == "T":
			if arg_6_0.rexw:
				var_6_2 = "Q"
				arg_6_0.rexw = False
			else
				var_6_2 = "D"

			var_6_1 = var_0_17[var_6_2]
		elif iter_6_0 == "B":
			var_6_2 = "B"
			var_6_1 = arg_6_0.rex and var_0_17.B64 or var_0_17.B
		elif var_0_4(iter_6_0, "[WDQMXYFG]"):
			var_6_2 = iter_6_0

			if var_6_2 == "X" and var_6_12:
				var_6_2 = "Y"
				arg_6_0.vexl = False

			var_6_1 = var_0_17[var_6_2]
		elif iter_6_0 == "P":
			var_6_2 = arg_6_0.o16 and "X" or "M"
			arg_6_0.o16 = False

			if var_6_2 == "X" and var_6_12:
				var_6_2 = "Y"
				arg_6_0.vexl = False

			var_6_1 = var_0_17[var_6_2]
		elif iter_6_0 == "S":
			arg_6_1 = arg_6_1 .. var_0_7(var_6_2)
		elif iter_6_0 == "s":
			local var_6_14 = var_0_25(arg_6_0, var_6_10, 1)

			if not var_6_14:
				return

			var_6_13 = var_6_14 <= 127 and var_0_3("+0x%02x", var_6_14) or var_0_3("-0x%02x", 256 - var_6_14)
			var_6_10 = var_6_10 + 1
		elif iter_6_0 == "u":
			local var_6_15 = var_0_25(arg_6_0, var_6_10, 1)

			if not var_6_15:
				return

			var_6_13 = var_0_3("0x%02x", var_6_15)
			var_6_10 = var_6_10 + 1
		elif iter_6_0 == "b":
			local var_6_16 = var_0_25(arg_6_0, var_6_10, 1)

			if not var_6_16:
				return

			var_6_13 = var_6_1[var_6_16 / 16 + 1]
			var_6_10 = var_6_10 + 1
		elif iter_6_0 == "w":
			local var_6_17 = var_0_25(arg_6_0, var_6_10, 2)

			if not var_6_17:
				return

			var_6_13 = var_0_3("0x%x", var_6_17)
			var_6_10 = var_6_10 + 2
		elif iter_6_0 == "o":
			if arg_6_0.x64:
				local var_6_18 = var_0_25(arg_6_0, var_6_10, 4)

				if not var_6_18:
					return

				local var_6_19 = var_0_25(arg_6_0, var_6_10 + 4, 4)

				if not var_6_19:
					return

				var_6_13 = var_0_3("[0x%08x%08x]", var_6_19, var_6_18)
				var_6_10 = var_6_10 + 8
			else
				local var_6_20 = var_0_25(arg_6_0, var_6_10, 4)

				if not var_6_20:
					return

				var_6_13 = var_0_3("[0x%08x]", var_6_20)
				var_6_10 = var_6_10 + 4
		elif iter_6_0 == "i" or iter_6_0 == "I":
			local var_6_21 = var_0_19[var_6_2]

			if var_6_21 == 8 and arg_6_0.x64 and iter_6_0 == "I":
				local var_6_22 = var_0_25(arg_6_0, var_6_10, 4)

				if not var_6_22:
					return

				local var_6_23 = var_0_25(arg_6_0, var_6_10 + 4, 4)

				if not var_6_23:
					return

				var_6_13 = var_0_3("0x%08x%08x", var_6_23, var_6_22)
			else
				if var_6_21 == 8:
					var_6_21 = 4

				local var_6_24 = var_0_25(arg_6_0, var_6_10, var_6_21)

				if not var_6_24:
					return

				if var_6_2 == "Q" and (var_6_24 < 0 or var_6_24 > 2147483647):
					var_6_24 = 4294967296 - var_6_24
					var_6_13 = var_0_3(var_6_24 > 65535 and "-0x%08x" or "-0x%x", var_6_24)
				else
					var_6_13 = var_0_3(var_6_24 > 65535 and "0x%08x" or "0x%x", var_6_24)

			var_6_10 = var_6_10 + var_6_21
		elif iter_6_0 == "j":
			local var_6_25 = var_0_19[var_6_2]

			if var_6_25 == 8:
				var_6_25 = 4

			local var_6_26 = var_0_25(arg_6_0, var_6_10, var_6_25)

			if not var_6_26:
				return

			if var_6_2 == "B" and var_6_26 > 127:
				var_6_26 = var_6_26 - 256
			elif var_6_26 > 2147483647:
				var_6_26 = var_6_26 - 4294967296

			var_6_10 = var_6_10 + var_6_25

			local var_6_27 = var_6_26 + var_6_10 + arg_6_0.addr

			if var_6_27 > 4294967295 and not arg_6_0.x64:
				var_6_27 = var_6_27 - 4294967296

			arg_6_0.imm = var_6_27

			if var_6_2 == "W":
				var_6_13 = var_0_3("word 0x%04x", var_6_27 % 65536)
			elif arg_6_0.x64:
				local var_6_28 = var_6_27 % 16777216

				var_6_13 = var_0_3("0x%02x%06x", (var_6_27 - var_6_28) / 16777216, var_6_28)
			else
				var_6_13 = "0x" .. var_0_9(var_6_27)
		elif iter_6_0 == "R":
			local var_6_29 = var_0_2(var_6_9, var_6_10 - 1, var_6_10 - 1) % 8

			if arg_6_0.rexb:
				var_6_29 = var_6_29 + 8
				arg_6_0.rexb = False

			var_6_13 = var_6_1[var_6_29 + 1]
		elif iter_6_0 == "a":
			var_6_13 = var_6_1[1]
		elif iter_6_0 == "c":
			var_6_13 = "cl"
		elif iter_6_0 == "d":
			var_6_13 = "dx"
		elif iter_6_0 == "1":
			var_6_13 = "1"
		else
			if not var_6_3:
				var_6_3 = arg_6_0.mrm

				if not var_6_3:
					if var_6_11 < var_6_10:
						return var_0_23(arg_6_0)

					var_6_3 = var_0_2(var_6_9, var_6_10, var_6_10)
					var_6_10 = var_6_10 + 1

				var_6_5 = var_6_3 % 8
				var_6_3 = (var_6_3 - var_6_5) / 8
				var_6_4 = var_6_3 % 8
				var_6_3 = (var_6_3 - var_6_4) / 8
				var_6_8 = ""

				if var_6_3 < 3:
					if var_6_5 == 4:
						if var_6_11 < var_6_10:
							return var_0_23(arg_6_0)

						var_6_6 = var_0_2(var_6_9, var_6_10, var_6_10)
						var_6_10 = var_6_10 + 1
						var_6_5 = var_6_6 % 8
						var_6_6 = (var_6_6 - var_6_5) / 8
						var_6_7 = var_6_6 % 8
						var_6_6 = (var_6_6 - var_6_7) / 8

						if arg_6_0.rexx:
							var_6_7 = var_6_7 + 8
							arg_6_0.rexx = False

						if var_6_7 == 4:
							var_6_7 = None

					if var_6_3 > 0 or var_6_5 == 5:
						local var_6_30 = var_6_3

						if var_6_30 != 1:
							var_6_30 = 4

						local var_6_31 = var_0_25(arg_6_0, var_6_10, var_6_30)

						if not var_6_31:
							return

						if var_6_3 == 0:
							var_6_5 = None

						if var_6_5 or var_6_7 or not var_6_6 and arg_6_0.x64 and not arg_6_0.a32:
							if var_6_30 == 1 and var_6_31 > 127:
								var_6_8 = var_0_3("-0x%x", 256 - var_6_31)
							elif var_6_31 >= 0 and var_6_31 <= 2147483647:
								var_6_8 = var_0_3("+0x%x", var_6_31)
							else
								var_6_8 = var_0_3("-0x%x", 4294967296 - var_6_31)
						else
							var_6_8 = var_0_3(arg_6_0.x64 and not arg_6_0.a32 and (not (var_6_31 >= 0) or not (var_6_31 <= 2147483647)) and "0xffffffff%08x" or "0x%08x", var_6_31)

						var_6_10 = var_6_10 + var_6_30

				if var_6_5 and arg_6_0.rexb:
					var_6_5 = var_6_5 + 8
					arg_6_0.rexb = False

				if arg_6_0.rexr:
					var_6_4 = var_6_4 + 8
					arg_6_0.rexr = False

			if iter_6_0 == "m":
				if var_6_3 == 3:
					var_6_13 = var_6_1[var_6_5 + 1]
				else
					local var_6_32 = arg_6_0.a32 and var_0_17.D or arg_6_0.aregs
					local var_6_33 = ""
					local var_6_34 = ""

					if var_6_5:
						var_6_33 = var_6_32[var_6_5 + 1]
					elif not var_6_6 and arg_6_0.x64 and not arg_6_0.a32:
						var_6_33 = "rip"

					arg_6_0.a32 = False

					if var_6_7:
						if var_6_5:
							var_6_33 = var_6_33 .. "+"

						var_6_34 = var_6_32[var_6_7 + 1]

						if var_6_6 > 0:
							var_6_34 = var_6_34 .. "*" .. 2^var_6_6

					var_6_13 = var_0_3("[%s%s%s]", var_6_33, var_6_34, var_6_8)

				if var_6_3 < 3 and (not var_0_4(arg_6_2, "[aRrgp]") or var_0_4(arg_6_2, "t")):
					var_6_13 = var_0_20[var_6_2] .. " " .. var_6_13
			elif iter_6_0 == "r":
				var_6_13 = var_6_1[var_6_4 + 1]
			elif iter_6_0 == "g":
				var_6_13 = var_0_18[var_6_4 + 1]
			elif iter_6_0 == "p":
				-- block empty
			elif iter_6_0 == "f":
				var_6_13 = "st" .. var_6_5
			elif iter_6_0 == "x":
				if var_6_4 == 0 and arg_6_0.lock and not arg_6_0.x64:
					var_6_13 = "CR8"
					arg_6_0.lock = False
				else
					var_6_13 = "CR" .. var_6_4
			elif iter_6_0 == "v":
				if arg_6_0.vexv:
					var_6_13 = var_6_1[arg_6_0.vexv + 1]
					arg_6_0.vexv = False
			elif iter_6_0 == "y":
				var_6_13 = "DR" .. var_6_4
			elif iter_6_0 == "z":
				var_6_13 = "TR" .. var_6_4
			elif iter_6_0 == "l":
				var_6_12 = False
			elif iter_6_0 == "t":
				-- block empty
			else
				error("bad pattern `" .. arg_6_2 .. "'")

		if var_6_13:
			var_6_0 = var_6_0 and var_6_0 .. ", " .. var_6_13 or var_6_13

	arg_6_0.pos = var_6_10

	return var_0_21(arg_6_0, arg_6_1, var_6_0)

local var_0_27

local function var_0_28(arg_7_0)
	local var_7_0 = arg_7_0.mrm

	if not var_7_0:
		local var_7_1 = arg_7_0.pos

		if var_7_1 > arg_7_0.stop:
			return None

		var_7_0 = var_0_2(arg_7_0.code, var_7_1, var_7_1)
		arg_7_0.pos = var_7_1 + 1
		arg_7_0.mrm = var_7_0

	return var_7_0

local function var_0_29(arg_8_0, arg_8_1, arg_8_2)
	if not arg_8_1:
		return var_0_24(arg_8_0)

	if var_0_4(arg_8_1, "%|"):
		local var_8_0

		if arg_8_0.rep:
			var_8_0 = arg_8_0.rep == "rep" and "%|([^%|]*)" or "%|[^%|]*%|[^%|]*%|([^%|]*)"
			arg_8_0.rep = False
		elif arg_8_0.o16:
			var_8_0 = "%|[^%|]*%|([^%|]*)"
			arg_8_0.o16 = False
		else
			var_8_0 = "^[^%|]*"

		arg_8_1 = var_0_4(arg_8_1, var_8_0)

		if not arg_8_1:
			return var_0_24(arg_8_0)

	if var_0_4(arg_8_1, "%$"):
		local var_8_1 = var_0_28(arg_8_0)

		if not var_8_1:
			return var_0_23(arg_8_0)

		arg_8_1 = var_0_4(arg_8_1, var_8_1 >= 192 and "^[^%$]*" or "%$(.*)")

		if arg_8_1 == "":
			return var_0_24(arg_8_0)

	if arg_8_1 == "":
		return var_0_24(arg_8_0)

	local var_8_2, var_8_3 = var_0_4(arg_8_1, "^([a-z0-9 ]*)(.*)")

	if var_8_3 == "" and arg_8_2:
		var_8_3 = arg_8_2

	return var_0_27[var_0_1(var_8_3, 1, 1)](arg_8_0, var_8_2, var_8_3)

local function var_0_30(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_0.pos
	local var_9_1 = arg_9_1[var_0_2(arg_9_0.code, var_9_0, var_9_0)]

	arg_9_0.pos = var_9_0 + 1

	return var_0_29(arg_9_0, var_9_1)

var_0_27 = {
	[""] = function(arg_10_0, arg_10_1, arg_10_2)
		return var_0_21(arg_10_0, arg_10_1),
	B = var_0_26,
	W = var_0_26,
	D = var_0_26,
	Q = var_0_26,
	V = var_0_26,
	U = var_0_26,
	T = var_0_26,
	M = var_0_26,
	X = var_0_26,
	P = var_0_26,
	F = var_0_26,
	G = var_0_26,
	Y = var_0_26,
	["."] = function(arg_11_0, arg_11_1, arg_11_2)
		arg_11_0[arg_11_2 == "." and arg_11_1 or var_0_1(arg_11_2, 2)] = arg_11_1

		if arg_11_0.pos - arg_11_0.start > 5:
			return var_0_24(arg_11_0),
	["*"] = function(arg_12_0, arg_12_1, arg_12_2)
		return var_0_27[arg_12_1](arg_12_0, arg_12_1, var_0_1(arg_12_2, 2)),
	["!"] = function(arg_13_0, arg_13_1, arg_13_2)
		local var_13_0 = var_0_28(arg_13_0)

		if not var_13_0:
			return var_0_23(arg_13_0)

		return var_0_29(arg_13_0, var_0_16[arg_13_1][(var_13_0 - var_13_0 % 8) / 8 % 8 + 1], var_0_1(arg_13_2, 2)),
	def sz:(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0.o16:
			arg_14_0.o16 = False
		else
			arg_14_2 = var_0_4(arg_14_2, ",(.*)")

			if arg_14_0.rexw:
				local var_14_0 = var_0_4(arg_14_2, ",(.*)")

				if var_14_0:
					arg_14_2 = var_14_0
					arg_14_0.rexw = False

		arg_14_2 = var_0_4(arg_14_2, "^[^,]*")

		return var_0_29(arg_14_0, arg_14_2),
	def opc2:(arg_15_0, arg_15_1, arg_15_2)
		return var_0_30(arg_15_0, var_0_12),
	def opc3:(arg_16_0, arg_16_1, arg_16_2)
		return var_0_30(arg_16_0, var_0_13[arg_16_2]),
	def vm:(arg_17_0, arg_17_1, arg_17_2)
		return var_0_29(arg_17_0, var_0_14[arg_17_0.mrm]),
	def fp:(arg_18_0, arg_18_1, arg_18_2)
		local var_18_0 = var_0_28(arg_18_0)

		if not var_18_0:
			return var_0_23(arg_18_0)

		local var_18_1 = var_18_0 % 8
		local var_18_2 = arg_18_2 * 8 + (var_18_0 - var_18_1) / 8 % 8

		if var_18_0 >= 192:
			var_18_2 = var_18_2 + 64

		local var_18_3 = var_0_15[var_18_2]

		if var_0_0(var_18_3) == "table":
			var_18_3 = var_18_3[var_18_1 + 1]

		return var_0_29(arg_18_0, var_18_3),
	def rex:(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0.rex:
			return var_0_24(arg_19_0)

		for iter_19_0 in var_0_5(arg_19_2, "."):
			arg_19_0["rex" .. iter_19_0] = True

		arg_19_0.rex = "rex",
	def vex:(arg_20_0, arg_20_1, arg_20_2)
		if arg_20_0.rex:
			return var_0_24(arg_20_0)

		arg_20_0.rex = "vex"

		local var_20_0 = arg_20_0.pos

		if arg_20_0.mrm:
			arg_20_0.mrm = None
			var_20_0 = var_20_0 - 1

		local var_20_1 = var_0_2(arg_20_0.code, var_20_0, var_20_0)

		if not var_20_1:
			return var_0_23(arg_20_0)

		local var_20_2 = var_20_0 + 1

		if var_20_1 < 128:
			arg_20_0.rexr = True

		local var_20_3 = 1

		if arg_20_2 == "3":
			var_20_3 = var_20_1 % 32
			var_20_1 = (var_20_1 - var_20_3) / 32

			local var_20_4 = var_20_1 % 2

			var_20_1 = (var_20_1 - var_20_4) / 2

			if var_20_4 == 0:
				arg_20_0.rexb = True

			if var_20_1 % 2 == 0:
				arg_20_0.rexx = True

			var_20_1 = var_0_2(arg_20_0.code, var_20_2, var_20_2)

			if not var_20_1:
				return var_0_23(arg_20_0)

			var_20_2 = var_20_2 + 1

			if var_20_1 >= 128:
				arg_20_0.rexw = True

		arg_20_0.pos = var_20_2

		local var_20_5

		if var_20_3 == 1:
			var_20_5 = var_0_12
		elif var_20_3 == 2:
			var_20_5 = var_0_13["38"]
		elif var_20_3 == 3:
			var_20_5 = var_0_13["3a"]
		else
			return var_0_24(arg_20_0)

		local var_20_6 = var_20_1 % 4
		local var_20_7 = (var_20_1 - var_20_6) / 4

		if var_20_6 == 1:
			arg_20_0.o16 = "o16"
		elif var_20_6 == 2:
			arg_20_0.rep = "rep"
		elif var_20_6 == 3:
			arg_20_0.rep = "repne"

		local var_20_8 = var_20_7 % 2
		local var_20_9 = (var_20_7 - var_20_8) / 2

		if var_20_8 != 0:
			arg_20_0.vexl = True

		arg_20_0.vexv = (-1 - var_20_9) % 16

		return var_0_30(arg_20_0, var_20_5),
	def nop:(arg_21_0, arg_21_1, arg_21_2)
		return var_0_29(arg_21_0, arg_21_0.rex and arg_21_2 or "nop"),
	def emms:(arg_22_0, arg_22_1, arg_22_2)
		if arg_22_0.rex != "vex":
			return var_0_21(arg_22_0, "emms")
		elif arg_22_0.vexl:
			arg_22_0.vexl = False

			return var_0_21(arg_22_0, "zeroall")
		else
			return var_0_21(arg_22_0, "zeroupper")
}

local function var_0_31(arg_23_0, arg_23_1, arg_23_2)
	arg_23_1 = arg_23_1 or 0

	local var_23_0 = arg_23_2 and arg_23_1 + arg_23_2 or #arg_23_0.code

	arg_23_1 = arg_23_1 + 1
	arg_23_0.start = arg_23_1
	arg_23_0.pos = arg_23_1
	arg_23_0.stop = var_23_0
	arg_23_0.imm = None
	arg_23_0.mrm = False

	var_0_22(arg_23_0)

	while var_23_0 >= arg_23_0.pos:
		var_0_30(arg_23_0, arg_23_0.map1)

	if arg_23_0.pos != arg_23_0.start:
		var_0_23(arg_23_0)

local function var_0_32(arg_24_0, arg_24_1, arg_24_2)
	local var_24_0 = {
		code = arg_24_0,
		addr = (arg_24_1 or 0) - 1,
		out = arg_24_2 or io.write,
		symtab = {},
		disass = var_0_31
	}

	var_24_0.hexdump = 16
	var_24_0.x64 = False
	var_24_0.map1 = var_0_10
	var_24_0.aregs = var_0_17.D

	return var_24_0

local function var_0_33(arg_25_0, arg_25_1, arg_25_2)
	local var_25_0 = var_0_32(arg_25_0, arg_25_1, arg_25_2)

	var_25_0.x64 = True
	var_25_0.map1 = var_0_11
	var_25_0.aregs = var_0_17.Q

	return var_25_0

local function var_0_34(arg_26_0, arg_26_1, arg_26_2)
	var_0_32(arg_26_0, arg_26_1, arg_26_2).disass()

local function var_0_35(arg_27_0, arg_27_1, arg_27_2)
	var_0_33(arg_27_0, arg_27_1, arg_27_2).disass()

local function var_0_36(arg_28_0)
	if arg_28_0 < 8:
		return var_0_17.D[arg_28_0 + 1]

	return var_0_17.X[arg_28_0 - 7]

local function var_0_37(arg_29_0)
	if arg_29_0 < 16:
		return var_0_17.Q[arg_29_0 + 1]

	return var_0_17.X[arg_29_0 - 15]

return {
	create = var_0_32,
	create64 = var_0_33,
	disass = var_0_34,
	disass64 = var_0_35,
	regname = var_0_36,
	regname64 = var_0_37
}
