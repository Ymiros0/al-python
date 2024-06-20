pg = pg or {}
pg.WorldToastMgr = singletonClass("WorldToastMgr")

local var_0_0 = pg.WorldToastMgr

var_0_0.Type2PicTrueName = {
	[0] = "type_operation",
	"type_fight",
	"type_search",
	"type_build",
	"type_defience",
	"type_special",
	"type_collection",
	"type_boss"
}

def var_0_0.Init(arg_1_0, arg_1_1):
	PoolMgr.GetInstance().GetUI("WorldTaskFloatUI", True, function(arg_2_0)
		arg_1_0._go = arg_2_0

		arg_1_0._go.SetActive(False)

		arg_1_0._tf = arg_1_0._go.transform

		arg_1_0._tf.SetParent(pg.UIMgr.GetInstance().OverlayToast, False)

		arg_1_0.displayList = {}

		if arg_1_1:
			arg_1_1())

def var_0_0.ShowToast(arg_3_0, arg_3_1, arg_3_2):
	table.insert(arg_3_0.displayList, {
		taskVO = arg_3_1,
		isSubmitDone = arg_3_2
	})

	if #arg_3_0.displayList == 1:
		arg_3_0.StartToast()

def var_0_0.StartToast(arg_4_0):
	setAnchoredPosition(arg_4_0._tf, {
		y = arg_4_0._tf.rect.height
	})
	setActive(arg_4_0._tf, True)

	local var_4_0 = arg_4_0.displayList[1]

	setActive(arg_4_0._tf.Find("accept_info"), not var_4_0.isSubmitDone)
	setActive(arg_4_0._tf.Find("submit_info"), var_4_0.isSubmitDone)

	local var_4_1 = var_4_0.taskVO

	GetImageSpriteFromAtlasAsync("ui/worldtaskfloatui_atlas", var_0_0.Type2PicTrueName[var_4_1.config.type], arg_4_0._tf.Find("type_icon"), True)
	setText(arg_4_0._tf.Find("desc"), setColorStr(shortenString(var_4_1.config.name, 12), var_4_0.isSubmitDone and COLOR_GREEN or COLOR_WHITE))

	local var_4_2 = {}

	table.insert(var_4_2, function(arg_5_0)
		arg_4_0.twId = LeanTween.moveY(arg_4_0._tf, 0, 0.5).setOnComplete(System.Action(arg_5_0)))
	table.insert(var_4_2, function(arg_6_0)
		arg_4_0.twId = LeanTween.moveY(arg_4_0._tf, arg_4_0._tf.rect.height, 0.5).setDelay(3).setOnComplete(System.Action(arg_6_0)))
	seriesAsync(var_4_2, function()
		table.remove(arg_4_0.displayList, 1)

		if #arg_4_0.displayList > 0:
			arg_4_0.StartToast()
		else
			setActive(arg_4_0._tf, False))

def var_0_0.Dispose(arg_8_0):
	LeanTween.cancel(arg_8_0.twId)

	arg_8_0.displayList = None

	PoolMgr.GetInstance().ReturnUI("WorldTaskFloatUI", arg_8_0._go)