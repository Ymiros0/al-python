local var_0_0 = class("GuildReportCard")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.viewComponent = arg_1_2
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.bg = arg_1_0._tf.GetComponent(typeof(Image))
	arg_1_0.label = arg_1_0._tf.Find("label").GetComponent(typeof(Image))
	arg_1_0.titleTxt = arg_1_0._tf.Find("title/name").GetComponent(typeof(Text))
	arg_1_0.descTxt = arg_1_0._tf.Find("desc").GetComponent(typeof(Text))
	arg_1_0.awardList = UIItemList.New(arg_1_0._tf.Find("awards/content"), arg_1_0._tf.Find("awards/content/item"))
	arg_1_0.getBtn = arg_1_0._tf.Find("get")
	arg_1_0.gotBtn = arg_1_0._tf.Find("got")
	arg_1_0.rankBtn = arg_1_0._tf.Find("rank")

	onButton(arg_1_0, arg_1_0.rankBtn, function()
		arg_1_0.viewComponent.ShowReportRank(arg_1_0.report.id), SFX_PANEL)

def var_0_0.Update(arg_3_0, arg_3_1):
	arg_3_0.report = arg_3_1

	local var_3_0 = arg_3_1.GetType()

	arg_3_0.bg.sprite = GetSpriteFromAtlas("ui/GuildEventReportUI_atlas", "bg_" .. var_3_0)
	arg_3_0.label.sprite = GetSpriteFromAtlas("ui/GuildEventReportUI_atlas", "text_" .. var_3_0)

	local var_3_1 = arg_3_1.IsSubmited()

	setActive(arg_3_0.getBtn, not var_3_1)
	setActive(arg_3_0.gotBtn, var_3_1)

	if not var_3_1:
		setGray(arg_3_0.getBtn, arg_3_1.IsLock(), True)

	arg_3_0.UpdateAwards()

	arg_3_0.titleTxt.text = arg_3_1.getConfig("name")
	arg_3_0.descTxt.text = arg_3_1.GetReportDesc()

	local var_3_2 = arg_3_1.IsBoss()

	setActive(arg_3_0.rankBtn, var_3_2)

def var_0_0.UpdateAwards(arg_4_0):
	local var_4_0, var_4_1 = arg_4_0.report.GetDrop()

	arg_4_0.awardList.make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate:
			local var_5_0 = var_4_0[arg_5_1 + 1]
			local var_5_1 = {
				type = var_5_0[1],
				id = var_5_0[2],
				count = var_5_0[3]
			}

			updateDrop(arg_5_2, var_5_1)
			onButton(arg_4_0, arg_5_2, function()
				arg_4_0.viewComponent.emit(BaseUI.ON_DROP, var_5_1), SFX_PANEL)
			setActive(arg_5_2.Find("icon_bg/bouns"), arg_5_1 + 1 <= var_4_1))
	arg_4_0.awardList.align(#var_4_0)

def var_0_0.Dispose(arg_7_0):
	pg.DelegateInfo.Dispose(arg_7_0)

return var_0_0
