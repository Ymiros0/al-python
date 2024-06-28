from luatable import table
from Framework.i18n import i18n
CM = 0
US = 1
EN = 2
JP = 3
DE = 4
CN = 5
ITA = 6
SN = 7
FF = 8
MNF = 9
FR = 10
MOT = 96
META = 97
BURIN = 98
SIRE = 99
LINK = 100
IDOL_LINK = 107

def IsLinkType(arg_1_0):
	return arg_1_0 > LINK

def IsMeta(arg_2_0):
	return arg_2_0 == META

def Nation2Print(arg_3_0):
	if not prints:
		prints = table({
			0: "cm",
			1: "us",
			2: "en",
			3: "jp",
			4: "de",
			5: "cn",
			6: "ita",
			7: "sn",
			8: "ff",
			9: "mnf",
			10: "ff",
			96: "mot",
			97: "meta",
			104: "um",
			108: "um",
			102: "bili",
			101: "np",
			107: "um",
			110: "um",
			103: "um",
			98: "cm",
			106: "um",
			105: "um",
			99: "sr",
			109: "um"
		})

	return prints[arg_3_0]

def Nation2Side(arg_4_0):
	if not side:
		side = table({
			0: "West",
			1: "West",
			2: "West",
			3: "Jp",
			4: "West",
			5: "Cn",
			6: "West",
			7: "West",
			8: "West",
			9: "West",
			10: "West",
			96: "West",
			108: "Jp",
			104: "West",
			97: "Meta",
			102: "Cn",
			101: "Jp",
			107: "Imas",
			106: "Jp",
			105: "Jp",
			98: "West",
			110: "Jp",
			103: "Jp",
			109: "West"
		})

	return side[arg_4_0]

def Nation2BG(arg_5_0):
	if not bg:
		bg = table({
			0: "bg/bg_church",
			1: "bg/bg_church",
			2: "bg/bg_church",
			3: "bg/bg_church_jp",
			4: "bg/bg_church",
			5: "bg/bg_church_cn",
			6: "bg/bg_church",
			7: "bg/bg_church",
			8: "bg/bg_church",
			9: "bg/bg_church",
			10: "bg/bg_church",
			96: "bg/bg_church",
			108: "bg/bg_church",
			104: "bg/bg_church",
			97: "bg/bg_church_meta",
			102: "bg/bg_church",
			101: "bg/bg_church",
			107: "bg/bg_church_imas",
			106: "bg/bg_church",
			105: "bg/bg_church",
			98: "bg/bg_church",
			110: "bg/bg_church",
			103: "bg/bg_church",
			109: "bg/bg_church"
		})

	return bg[arg_5_0]

def Nation2Name(arg_6_0):
	if not nationName:
		nationName = table({
			0: i18n("word_shipNation_other"),
			1: i18n("word_shipNation_baiYing"),
			2: i18n("word_shipNation_huangJia"),
			3: i18n("word_shipNation_chongYing"),
			4: i18n("word_shipNation_tieXue"),
			5: i18n("word_shipNation_dongHuang"),
			6: i18n("word_shipNation_saDing"),
			7: i18n("word_shipNation_beiLian"),
			8: i18n("word_shipNation_ziyou"),
			9: i18n("word_shipNation_weixi"),
			10: i18n("word_shipNation_yuanwei"),
			96: i18n("word_shipNation_mot"),
			97: i18n("word_shipNation_meta"),
			98: i18n("word_shipNation_other"),
			101: i18n("word_shipNation_np"),
			102: i18n("word_shipNation_bili"),
			103: i18n("word_shipNation_um"),
			104: i18n("word_shipNation_ai"),
			105: i18n("word_shipNation_holo"),
			106: i18n("word_shipNation_doa"),
			107: i18n("word_shipNation_imas"),
			108: i18n("word_shipNation_ssss"),
			109: i18n("word_shipNation_ryza"),
			110: i18n("word_shipNation_senran")
		})

	return nationName[arg_6_0]

def Nation2facionName(arg_7_0):
	if not facionName:
		facionName = table({
			0: i18n("guild_faction_unknown"),
			1: i18n("guild_faction_blhx"),
			2: i18n("guild_faction_blhx"),
			3: i18n("guild_faction_cszz"),
			4: i18n("guild_faction_cszz"),
			5: i18n("guild_faction_blhx"),
			6: i18n("guild_faction_cszz"),
			7: i18n("guild_faction_blhx"),
			8: i18n("guild_faction_blhx"),
			9: i18n("guild_faction_cszz"),
			10: i18n("guild_faction_blhx"),
			96: i18n("guild_faction_unknown"),
			97: i18n("guild_faction_meta"),
			98: i18n("guild_faction_unknown"),
			101: i18n("guild_faction_unknown"),
			102: i18n("guild_faction_unknown"),
			103: i18n("guild_faction_unknown"),
			104: i18n("guild_faction_unknown"),
			105: i18n("guild_faction_unknown"),
			106: i18n("guild_faction_unknown"),
			107: i18n("guild_faction_unknown"),
			108: i18n("guild_faction_unknown"),
			109: i18n("guild_faction_unknown"),
			110: i18n("guild_faction_unknown")
		})

	return facionName[arg_7_0]
