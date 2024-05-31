local var_0_0 = class("PublicGuildResPage", import("..subPages.main.GuildResPage"))

def var_0_0.OnInit(arg_1_0):
	local var_1_0 = "blue"

	arg_1_0.contributionBg.sprite = GetSpriteFromAtlas("ui/GuildMainUI_atlas", "res_" .. var_1_0)
	arg_1_0.captailBg.sprite = GetSpriteFromAtlas("ui/GuildMainUI_atlas", "res_" .. var_1_0)

	setActive(arg_1_0.captailBg.gameObject, False)

def var_0_0.Update(arg_2_0, arg_2_1):
	arg_2_0.resContributionTxt.text = arg_2_1.getResource(8)

return var_0_0
