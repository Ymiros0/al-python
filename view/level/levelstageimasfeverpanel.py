local var_0_0 = class("LevelStageIMasFeverPanel", import("view.base.BaseSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "LevelStageIMasFeverPanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.fillImg = arg_2_0._tf.Find("Fill")
	arg_2_0.banner = arg_2_0._tf.Find("Banner")

	setActive(arg_2_0.banner, False)

local var_0_1 = {
	[0] = 0,
	0.38,
	0.5471839,
	0.7228736,
	1
}
local var_0_2 = {
	"Yellow",
	"Red",
	"Blue"
}

def var_0_0.UpdateView(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = getProxy(ChapterProxy).GetLastDefeatedEnemy(arg_3_1.id)
	local var_3_1 = arg_3_1.defeatEnemies
	local var_3_2 = pg.gameset.doa_fever_count.key_value
	local var_3_3 = var_0_1[Mathf.Min(var_3_2, var_3_1)]

	seriesAsync({
		function(arg_4_0)
			LeanTween.cancel(go(arg_3_0.fillImg))

			if not var_3_0 or var_3_1 > var_3_2:
				arg_4_0()

				return

			local var_4_0 = math.max(var_3_1 - 1, 0)
			local var_4_1 = arg_3_0.fillImg.GetComponent(typeof(Image))
			local var_4_2 = var_0_1[var_4_0]

			LeanTween.value(go(arg_3_0.fillImg), 0, 1, 1).setOnUpdate(System.Action_float(function(arg_5_0)
				local var_5_0 = Mathf.Lerp(var_4_2, var_3_3, arg_5_0)

				var_4_1.fillAmount = var_5_0)).setOnComplete(System.Action(arg_4_0)),
		function(arg_6_0)
			arg_3_0.fillImg.GetComponent(typeof(Image)).fillAmount = var_3_3

			if var_3_0 and var_3_1 == var_3_2:
				arg_3_0.ShowPanel(arg_3_1)

			existCall(arg_3_2)
	})

def var_0_0.ShowPanel(arg_7_0, arg_7_1):
	arg_7_0.viewParent.emit(LevelUIConst.FROZEN)
	pg.UIMgr.GetInstance().OverlayPanel(arg_7_0.banner)

	local var_7_0 = var_0_2[1]
	local var_7_1 = arg_7_1.GetBuffOfLinkAct()

	if var_7_1:
		local var_7_2 = pg.gameset.doa_fever_buff.description

		var_7_0 = var_0_2[table.indexof(var_7_2, var_7_1)]

	local var_7_3 = arg_7_0.banner.Find(var_7_0)
	local var_7_4 = var_7_3.Find("Character")
	local var_7_5 = var_7_4.GetComponent(typeof(Image))
	local var_7_6 = math.random(1, 7)

	setImageSprite(var_7_4, LoadSprite("ui/LevelStageIMasFeverPanel_atlas", "character" .. tostring(var_7_6)))
	setActive(arg_7_0.banner, True)
	setActive(var_7_3, True)

	var_7_5.enabled = True

	local function var_7_7()
		arg_7_0.ClosePanel()

	var_7_3.GetComponent(typeof(DftAniEvent)).SetEndEvent(var_7_7)
	onButton(arg_7_0, arg_7_0.banner, var_7_7)

	arg_7_0.showingPanel = True

def var_0_0.ClosePanel(arg_9_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_9_0.banner, arg_9_0._tf)
	setActive(arg_9_0.banner, False)
	arg_9_0.viewParent.emit(LevelUIConst.UN_FROZEN)

	arg_9_0.showingPanel = None

def var_0_0.OnDestroy(arg_10_0):
	if arg_10_0.showingPanel:
		arg_10_0.ClosePanel()

return var_0_0
