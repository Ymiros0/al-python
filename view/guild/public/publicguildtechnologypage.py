local var_0_0 = class("PublicGuildTechnologyPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "PublicGuildTechnologyPage"

def var_0_0.OnTechGroupUpdate(arg_2_0, arg_2_1):
	arg_2_0.UpdateUpgradeList()

def var_0_0.OnLoaded(arg_3_0):
	arg_3_0.upgradeList = UIItemList.New(arg_3_0.findTF("frame/upgrade/content"), arg_3_0.findTF("frame/upgrade/content/tpl"))

def var_0_0.OnInit(arg_4_0):
	arg_4_0.upgradeList.make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate:
			local var_5_0 = arg_4_0.technologyVOs[arg_5_1 + 1]

			PublicGuildTechnologyCard.New(arg_5_2.Find("content"), arg_4_0).Update(var_5_0)
			setActive(arg_5_2.Find("back"), False))

def var_0_0.Show(arg_6_0, arg_6_1):
	arg_6_0.guildVO = arg_6_1

	arg_6_0.UpdateUpgradeList()
	var_0_0.super.Show(arg_6_0)

def var_0_0.UpdateUpgradeList(arg_7_0):
	arg_7_0.technologyVOs = {}

	local var_7_0 = arg_7_0.guildVO.GetTechnologys()

	for iter_7_0, iter_7_1 in pairs(var_7_0):
		if not iter_7_1.IsGuildMember():
			table.insert(arg_7_0.technologyVOs, iter_7_1)

	table.sort(arg_7_0.technologyVOs, function(arg_8_0, arg_8_1)
		return arg_8_0.id < arg_8_1.id)
	arg_7_0.upgradeList.align(#arg_7_0.technologyVOs)

def var_0_0.OnDestroy(arg_9_0):
	return

return var_0_0
