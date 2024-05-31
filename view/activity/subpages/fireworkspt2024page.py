local var_0_0 = class("FireworksPt2024Page", import(".FireworksPtPage"))

var_0_0.ANIM_SHOW = {
	{
		70166,
		70167,
		70165,
		70168,
		70169
	},
	{
		70170,
		70172,
		70171,
		70173,
		70174
	},
	{
		70175,
		70176,
		70177,
		70178
	}
}

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.fireBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SPRING_FESTIVAL_BACKHILL_2024, {
			openFireworkLayer = True
		}), SFX_PANEL)

def var_0_0.UpdateFrieworkPanel(arg_3_0, arg_3_1):
	arg_3_0.fireworkAct = getProxy(ActivityProxy).getActivityById(arg_3_0.fireworkActID)

	assert(arg_3_0.fireworkAct and not arg_3_0.fireworkAct.isEnd(), "烟花活动(type92)已结束")

	arg_3_0.unlockCount = arg_3_0.fireworkAct.getData1()
	arg_3_0.unlockIds = arg_3_0.fireworkAct.getData1List()

	local var_3_0 = #arg_3_0.fireworkPages

	if var_3_0 < arg_3_1 or arg_3_1 < 1:
		return

	arg_3_0.pageIndex = arg_3_1

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.fireworkPages):
		setActive(iter_3_1, tonumber(iter_3_1.name) == arg_3_1)

	for iter_3_2, iter_3_3 in ipairs(arg_3_0.dots):
		setActive(iter_3_3, tonumber(iter_3_3.name) == arg_3_1)

	setButtonEnabled(arg_3_0.nextPageBtn, arg_3_1 != var_3_0)
	setButtonEnabled(arg_3_0.lastPageBtn, arg_3_1 != 1)
	setText(arg_3_0.fireworkNumText, #arg_3_0.unlockIds .. "/" .. #arg_3_0.fireworkIds)

	arg_3_0.ptNum = getProxy(PlayerProxy).getRawData().getResource(arg_3_0.ptID)

	setText(arg_3_0.ptText, arg_3_0.ptNum)

	local var_3_1 = arg_3_0.getAnimId()
	local var_3_2 = arg_3_0.unlockCount > 0 and arg_3_0.ptNum >= arg_3_0.ptConsume

	for iter_3_4 = #arg_3_0.fireworkPages, 1, -1:
		eachChild(arg_3_0.fireworkPages[iter_3_4], function(arg_4_0)
			local var_4_0 = tonumber(arg_4_0.name)

			if table.contains(arg_3_0.unlockIds, var_4_0):
				setActive(arg_4_0, False)
			else
				setActive(arg_4_0, True)

				if var_3_2 and var_3_1 and var_4_0 == var_3_1:
					arg_3_0.playSwingAnim(arg_4_0)
				else
					arg_3_0.stopSwingAnim(arg_4_0)

				onButton(arg_3_0, arg_4_0, function()
					arg_3_0.OnUnlockClick(var_4_0), SFX_PANEL))

def var_0_0.getAnimId(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(var_0_0.ANIM_SHOW[arg_6_0.pageIndex]):
		if not table.contains(arg_6_0.unlockIds, iter_6_1):
			return iter_6_1

	return None

def var_0_0.playSwingAnim(arg_7_0, arg_7_1):
	arg_7_0.findTF("pos/Image", arg_7_1).GetComponent(typeof(Animation)).Play("swing")

def var_0_0.stopSwingAnim(arg_8_0, arg_8_1):
	arg_8_0.findTF("pos/Image", arg_8_1).GetComponent(typeof(Animation)).Stop()

return var_0_0
