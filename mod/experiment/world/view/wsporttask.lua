local var_0_0 = class("WSPortTask", import("...BaseEntity"))

var_0_0.Fields = {
	btnOnGoing = "userdata",
	txDesc = "userdata",
	onDrop = "function",
	transform = "userdata",
	task = "table",
	rtType = "userdata",
	progress = "userdata",
	onButton = "function",
	rtRarity = "userdata",
	timer = "number",
	rtName = "userdata",
	txProgress = "userdata",
	btnFinished = "userdata",
	btnInactive = "userdata",
	rfAwardPanle = "userdata",
	rfItemTpl = "userdata"
}
var_0_0.Listeners = {
	onTaskUpdate = "OnTaskUpdate"
}

function var_0_0.Build(arg_1_0, arg_1_1)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:Init(arg_1_1)
end

function var_0_0.Dispose(arg_2_0)
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0:Clear()
end

function var_0_0.Init(arg_3_0, arg_3_1)
	arg_3_0.transform = arg_3_1
	arg_3_0.rtType = arg_3_1:Find("type")
	arg_3_0.rtRarity = arg_3_1:Find("rarity")
	arg_3_0.rtName = arg_3_1:Find("name")
	arg_3_0.txDesc = arg_3_1:Find("desc")
	arg_3_0.btnInactive = arg_3_1:Find("button/inactive")
	arg_3_0.btnOnGoing = arg_3_1:Find("button/ongoing")
	arg_3_0.btnFinished = arg_3_1:Find("button/finished")
	arg_3_0.progress = arg_3_1:Find("name/slider")
	arg_3_0.txProgress = arg_3_1:Find("name/slider_progress")
	arg_3_0.rfAwardPanle = arg_3_1:Find("award_panel/content")
	arg_3_0.rfItemTpl = arg_3_1:Find("item_tpl")
end

function var_0_0.Setup(arg_4_0, arg_4_1)
	arg_4_0.task = arg_4_1

	arg_4_0:OnTaskUpdate()
end

function var_0_0.OnTaskUpdate(arg_5_0)
	setImageColor(arg_5_0.rtName, arg_5_0.task.config.type == 5 and Color(0.058823529411764705, 0.0784313725490196, 0.10980392156862745, 0.3) or Color(0.5450980392156862, 0.596078431372549, 0.8196078431372549, 0.3))
	setText(arg_5_0.rtName:Find("Text"), arg_5_0.task.config.name)
	setText(arg_5_0.txDesc, arg_5_0.task.config.description)
	GetImageSpriteFromAtlasAsync("ui/worldportui_atlas", pg.WorldToastMgr.Type2PictrueName[arg_5_0.task.config.type], arg_5_0.rtType, true)
	GetImageSpriteFromAtlasAsync("ui/worldportui_atlas", "rarity_" .. arg_5_0.task.config.rank, arg_5_0.rtRarity, true)

	local var_5_0 = arg_5_0.task.config.show

	removeAllChildren(arg_5_0.rfAwardPanle)

	for iter_5_0, iter_5_1 in ipairs(var_5_0) do
		local var_5_1 = cloneTplTo(arg_5_0.rfItemTpl, arg_5_0.rfAwardPanle)
		local var_5_2 = {
			type = iter_5_1[1],
			id = iter_5_1[2],
			count = iter_5_1[3]
		}

		updateDrop(var_5_1, var_5_2)
		onButton(arg_5_0, var_5_1, function()
			arg_5_0.onDrop(var_5_2)
		end, SFX_PANEL)
		setActive(var_5_1, true)
	end

	setActive(arg_5_0.rfItemTpl, false)

	local var_5_3 = arg_5_0.task:getState()

	setActive(arg_5_0.btnInactive, var_5_3 == WorldTask.STATE_INACTIVE)
	setActive(arg_5_0.btnOnGoing, var_5_3 == WorldTask.STATE_ONGOING)
	setActive(arg_5_0.btnFinished, var_5_3 == WorldTask.STATE_FINISHED)
	setActive(arg_5_0.txProgress, false)
	setActive(arg_5_0.progress, false)
end

return var_0_0
