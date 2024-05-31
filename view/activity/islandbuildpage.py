local var_0_0 = class("IslandBuildPage")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.buildPanel = arg_1_1
	arg_1_0.activityId = ActivityConst.ISLAND_TASK_ID

	local var_1_0 = pg.activity_template[arg_1_0.activityId].config_client

	if var_1_0.pt_id and var_1_0.pt_id > 0:
		arg_1_0.ptId = var_1_0.pt_id
		arg_1_0.ptName = pg.player_resource[arg_1_0.ptId].name

	arg_1_0.buffs = var_1_0.buff
	arg_1_0.maxNum = arg_1_0.buffs[#arg_1_0.buffs].pt[1]

	setActive(arg_1_0.buildPanel, False)

	arg_1_0.pointProgressText = findTF(arg_1_0.buildPanel, "progressContent/progress")
	arg_1_0.pointProgressSlider = findTF(arg_1_0.buildPanel, "slider")
	arg_1_0.pointStarTpl = findTF(arg_1_0.buildPanel, "levelStar/starTpl")
	arg_1_0.pointAdd = findTF(arg_1_0.buildPanel, "add")
	arg_1_0.pointLevelStar = findTF(arg_1_0.buildPanel, "levelStar")
	arg_1_0.pointStarTfs = {}

	local var_1_1 = arg_1_0.pointLevelStar.sizeDelta.x

	for iter_1_0 = 1, #arg_1_0.buffs:
		local var_1_2 = tf(Instantiate(arg_1_0.pointStarTpl))

		SetParent(var_1_2, arg_1_0.pointLevelStar)
		setActive(var_1_2, True)
		setText(findTF(var_1_2, "bg/text"), iter_1_0)
		setImageSprite(findTF(var_1_2, "img"), LoadSprite(IslandTaskScene.ui_atlas, "img_level_" .. iter_1_0))

		local var_1_3 = arg_1_0.buffs[iter_1_0].pt[1]

		var_1_2.anchoredPosition = Vector3(var_1_3 / arg_1_0.maxNum * var_1_1, 0, 0)

		table.insert(arg_1_0.pointStarTfs, var_1_2)

		if iter_1_0 == 1:
			setActive(var_1_2, False)

	setText(findTF(arg_1_0.buildPanel, "levelNum/text"), i18n(IslandTaskScene.island_build_level))
	setText(findTF(arg_1_0.buildPanel, "levelBuff/text"), i18n(IslandTaskScene.island_build_level))
	setText(findTF(arg_1_0.buildPanel, "buildDesc"), i18n(IslandTaskScene.island_build_desc))
	arg_1_0.updatePoint()

def var_0_0.updatePoint(arg_2_0):
	local var_2_0 = 0
	local var_2_1 = 1

	if arg_2_0.ptId:
		var_2_0 = getProxy(PlayerProxy).getData()[arg_2_0.ptName] or 0
	else
		var_2_0 = arg_2_0.getNum()

	if var_2_0 > arg_2_0.maxNum:
		var_2_0 = arg_2_0.maxNum

	local var_2_2 = arg_2_0.getBuildLv(var_2_0)

	for iter_2_0 = 1, #arg_2_0.pointStarTfs:
		local var_2_3 = arg_2_0.pointStarTfs[iter_2_0]

		if iter_2_0 <= var_2_2:
			setActive(findTF(var_2_3, "img"), True)
			setActive(findTF(var_2_3, "lock"), False)

			GetComponent(var_2_3, typeof(CanvasGroup)).alpha = 1
		else
			setActive(findTF(var_2_3, "img"), False)
			setActive(findTF(var_2_3, "lock"), True)

			GetComponent(var_2_3, typeof(CanvasGroup)).alpha = 0.5

	local var_2_4 = arg_2_0.buffs[var_2_2].benefit

	for iter_2_1 = 1, #var_2_4:
		local var_2_5 = var_2_4[iter_2_1]
		local var_2_6 = pg.benefit_buff_template[var_2_5].desc
		local var_2_7 = findTF(arg_2_0.buildPanel, "add/" .. iter_2_1)

		if PLATFORM_CODE == PLATFORM_JP:
			findTF(var_2_7, "img").sizeDelta = Vector2(450, 70)

			setText(findTF(var_2_7, "text_jp"), var_2_6)
		else
			setText(findTF(var_2_7, "text"), var_2_6)

	setSlider(arg_2_0.pointProgressSlider, 0, arg_2_0.maxNum, var_2_0)
	setText(findTF(arg_2_0.buildPanel, "levelNum/num"), "Lv." .. var_2_2)
	setText(findTF(arg_2_0.buildPanel, "levelBuff/num"), "Lv." .. var_2_2)
	arg_2_0.setProgressText()

def var_0_0.getBuildLv(arg_3_0, arg_3_1):
	local var_3_0 = 1

	for iter_3_0 = #arg_3_0.buffs, 1, -1:
		var_3_0 = arg_3_1 >= arg_3_0.buffs[iter_3_0].pt[1] and var_3_0 < iter_3_0 and iter_3_0 or var_3_0

	return var_3_0

def var_0_0.setProgressText(arg_4_0):
	local var_4_0 = arg_4_0.getNum()
	local var_4_1 = arg_4_0.maxNum

	setText(arg_4_0.pointProgressText, setColorStr(var_4_0, "#C2695B") .. setColorStr("/" .. var_4_1, "#9D6B59"))

def var_0_0.getNum(arg_5_0):
	return getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2).GetBuildingLevelSum()

def var_0_0.setActive(arg_6_0, arg_6_1):
	setActive(arg_6_0.buildPanel, arg_6_1)

def var_0_0.dispose(arg_7_0):
	return

return var_0_0
