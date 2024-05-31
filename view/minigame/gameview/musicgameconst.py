local var_0_0 = class("MusicGameConst")

var_0_0.music_game_data = {
	{
		bg = 1,
		pu = "06",
		music_id = 1,
		comboEffect = 1,
		music_piece = 2,
		light = 2,
		img = 1,
		bgm = "06",
		settlement_painting = {
			"daiduo_idol_n",
			"baerdimo_idol_n",
			"guanghui_idol_n",
			"tashigan_idol_n",
			"daqinghuayu_idolns"
		},
		ships = {
			"daiduo_idol",
			"baerdimo_idol",
			"guanghui_idol",
			"tashigan_idol",
			"daqinghuayu_idol"
		}
	},
	{
		bg = 2,
		pu = "08",
		music_id = 2,
		comboEffect = 1,
		music_piece = 2,
		light = 3,
		img = 2,
		bgm = "08",
		settlement_painting = {
			"luoen_idol_n",
			"dafeng_idol_n"
		},
		ships = {
			False,
			"dafeng_idol",
			False,
			"luoen_idol",
			False
		}
	},
	{
		bg = 3,
		pu = "07",
		music_id = 3,
		comboEffect = 1,
		music_piece = 2,
		light = 1,
		img = 3,
		bgm = "07",
		settlement_painting = {
			"edu_idol_n"
		},
		ships = {
			False,
			False,
			"edu_idol",
			False,
			False
		}
	},
	{
		bg = 4,
		pu = "09",
		music_id = 4,
		comboEffect = 1,
		music_piece = 2,
		light = False,
		img = 4,
		bgm = "09",
		settlement_painting = {
			"chicheng_idolns",
			"xiefeierde_idolns",
			"jiasikenie_idolns",
			"kelifulan_idolns",
			"xipeier_idolns"
		},
		ships = {
			"chicheng_idol",
			"xiefeierde_idol",
			"jiasikenie_idol",
			"kelifulan_idol",
			"xipeier_idol"
		}
	},
	{
		img = 5,
		pu = "010",
		music_id = 5,
		comboEffect = 1,
		music_piece = 2,
		bg = 4,
		bgm = "10"
	},
	{
		bg = 4,
		pu = "01",
		music_id = 6,
		comboEffect = 1,
		music_piece = 2,
		light = False,
		img = 6,
		bgm = "01",
		settlement_painting = {
			"chicheng_idol"
		},
		ships = {
			"chicheng_idol",
			"xiefeierde_idol",
			"jiasikenie_idol",
			"kelifulan_idol",
			"xipeier_idol"
		}
	},
	{
		img = 7,
		pu = "02",
		music_id = 7,
		comboEffect = 1,
		music_piece = 2,
		bg = 4,
		bgm = "02"
	},
	{
		img = 8,
		pu = "03",
		music_id = 8,
		comboEffect = 1,
		music_piece = 2,
		bg = 4,
		bgm = "03"
	},
	{
		img = 9,
		pu = "04",
		music_id = 9,
		comboEffect = 1,
		music_piece = 2,
		bg = 4,
		bgm = "04"
	},
	{
		img = 10,
		pu = "05",
		music_id = 10,
		comboEffect = 1,
		music_piece = 2,
		bg = 4,
		bgm = "05"
	}
}

def var_0_0.getRandomBand():
	local var_1_0 = math.random(1, #MusicGameConst.random_band)

	return MusicGameConst.random_band[var_1_0]

var_0_0.painting_const_key = {
	jiasikenie_idolns = "jiasikenie_idol",
	kelifulan_idolns = "kelifulan_idol",
	ougen_idol_n = "ougen_idol",
	boyixi_idol_n = "boyixi_idol",
	baerdimo_idol_n = "baerdimo_idol",
	edu_idol_n = "edu_idol",
	lumang_idol_n = "lumang_idol",
	jingang_idol_n = "jingang_idol",
	luoen_idol_n = "luoen_idol",
	dafeng_idol_n = "dafeng_idol",
	nengdai_idol_n = "nengdai_idol",
	kewei_idol_n = "kewei_idol",
	xiefeierde_idolns = "xiefeierde_idol",
	daqinghuayu_idolns = "tashigan_idol_n",
	xipeier_idolns = "xipeier_idol",
	daiduo_idol_n = "daiduo_idol",
	tashigan_idol_n = "tashigan_idol",
	guanghui_idol_n = "guanghui_idol",
	chicheng_idolns = "chicheng_idol"
}
var_0_0.random_band = {
	{
		bg = 4,
		light = False,
		settlement_painting = {
			"chicheng_idolns",
			"xiefeierde_idolns",
			"jiasikenie_idolns",
			"kelifulan_idolns",
			"xipeier_idolns"
		},
		ships = {
			"chicheng_idol",
			"xiefeierde_idol",
			"jiasikenie_idol",
			"kelifulan_idol",
			"xipeier_idol"
		}
	},
	{
		bg = 1,
		light = 2,
		settlement_painting = {
			"daiduo_idol_n",
			"baerdimo_idol_n",
			"guanghui_idol_n",
			"tashigan_idol_n",
			"daqinghuayu_idolns"
		},
		ships = {
			"daiduo_idol",
			"baerdimo_idol",
			"guanghui_idol",
			"tashigan_idol",
			"daqinghuayu_idol"
		}
	},
	{
		bg = 3,
		light = 1,
		settlement_painting = {
			"edu_idol_n"
		},
		ships = {
			False,
			False,
			"edu_idol",
			False,
			False
		}
	},
	{
		bg = 2,
		light = 3,
		settlement_painting = {
			"luoen_idol_n",
			"dafeng_idol_n"
		},
		ships = {
			False,
			"dafeng_idol",
			False,
			"luoen_idol",
			False
		}
	}
}
var_0_0.music_all_ship = {
	"chicheng_idol",
	"xiefeierde_idol",
	"jiasikenie_idol",
	"kelifulan_idol",
	"xipeier_idol",
	"luoen_idol",
	"baerdimo_idol",
	"edu_idol",
	"dafeng_idol",
	"daiduo_idol",
	"guanghui_idol",
	"tashigan_idol",
	"daqinghuayu_idol"
}
var_0_0.music_all_painting = {
	"chicheng_idolns",
	"xiefeierde_idolns",
	"jiasikenie_idolns",
	"kelifulan_idolns",
	"xipeier_idolns",
	"baerdimo_idol_n",
	"dafeng_idol_n",
	"daiduo_idol_n",
	"daqinghuayu_idolns",
	"edu_idol_n",
	"guanghui_idol_n",
	"luoen_idol_n",
	"tashigan_idol_n"
}

return var_0_0
