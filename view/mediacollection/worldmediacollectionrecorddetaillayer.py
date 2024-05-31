local var_0_0 = class("WorldMediaCollectionRecordDetailLayer", import(".WorldMediaCollectionSubLayer"))

var_0_0.TypeStory = 1
var_0_0.TypeBattle = 2

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionMemoryDetailUI"

def var_0_0.OnInit(arg_2_0):
	var_0_0.super.OnInit(arg_2_0)
	assert(arg_2_0.viewParent, "Need assign ViewParent for " .. arg_2_0.__cname)
	setActive(arg_2_0._tf.Find("ItemRect/TitleRecord"), True)
	setActive(arg_2_0._tf.Find("ItemRect/TitleMemory"), False)

	arg_2_0.recordItemList = arg_2_0.findTF("ItemRect").GetComponent("LScrollRect")

	function arg_2_0.recordItemList.onInitItem(arg_3_0)
		arg_2_0.OnInitRecordItem(arg_3_0)

	function arg_2_0.recordItemList.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.OnUpdateRecordItem(arg_4_0 + 1, arg_4_1)

	arg_2_0.recordItems = {}

	local var_2_0 = arg_2_0.findTF("Item", arg_2_0.recordItemList)

	setActive(var_2_0, False)

	arg_2_0.loader = AutoLoader.New()

	setText(arg_2_0._tf.Find("ItemRect/ProgressDesc"), i18n("world_collection_2"))

def var_0_0.OnInitRecordItem(arg_5_0, arg_5_1):
	if arg_5_0.exited:
		return

	onButton(arg_5_0, arg_5_1, function()
		local var_6_0 = arg_5_0.recordItems[arg_5_1]
		local var_6_1 = nowWorld().GetCollectionProxy()

		if var_6_0 and arg_5_0.CheckRecordIsUnlock(var_6_0):
			arg_5_0.PlayMemory(var_6_0), SOUND_BACK)

def var_0_0.OnUpdateRecordItem(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_0.exited:
		return

	local var_7_0 = arg_7_0.records and arg_7_0.records[arg_7_1]

	assert("Not Initialize RecordGroups ID. " .. (arg_7_0.contextData.recordGroup or "NIL"))

	arg_7_0.recordItems[arg_7_2] = var_7_0

	local var_7_1 = tf(arg_7_2)

	if arg_7_0.CheckRecordIsUnlock(var_7_0):
		setActive(var_7_1.Find("normal"), True)
		setActive(var_7_1.Find("lock"), False)

		var_7_1.Find("normal/title").GetComponent(typeof(Text)).text = var_7_0.name

		arg_7_0.loader.GetSpriteQuiet("memoryicon/" .. var_7_0.icon, "", var_7_1.Find("normal"))
		setText(var_7_1.Find("normal/id"), string.format("#%u", var_7_0.group_ID))
	else
		setActive(var_7_1.Find("normal"), False)
		setActive(var_7_1.Find("lock"), True)
		setText(var_7_1.Find("lock/condition"), var_7_0.condition)

	onButton(arg_7_0, var_7_1, function()
		if not arg_7_0.CheckRecordIsUnlock(var_7_0):
			return

		arg_7_0.PlayMemory(var_7_0), SFX_PANEL)

def var_0_0.SetStoryMask(arg_9_0, arg_9_1):
	arg_9_0.memoryMask = arg_9_1

def var_0_0.PlayMemory(arg_10_0, arg_10_1):
	if arg_10_1.type == var_0_0.TypeBattle:
		local var_10_0 = pg.NewStoryMgr.GetInstance().StoryName2StoryId(arg_10_1.story)

		arg_10_0.emit(WorldMediaCollectionMediator.BEGIN_STAGE, {
			memory = True,
			system = SYSTEM_PERFORM,
			stageId = var_10_0
		})
	else
		local var_10_1 = findTF(arg_10_0.memoryMask, "pic")

		if string.len(arg_10_1.mask) > 0:
			setActive(var_10_1, True)

			var_10_1.GetComponent(typeof(Image)).sprite = LoadSprite(arg_10_1.mask)
		else
			setActive(var_10_1, False)

		setActive(arg_10_0.memoryMask, True)
		pg.NewStoryMgr.GetInstance().Play(arg_10_1.story, function()
			setActive(arg_10_0.memoryMask, False), True)

def var_0_0.ShowRecordGroup(arg_12_0, arg_12_1):
	arg_12_0.contextData.recordGroup = arg_12_1

	local var_12_0 = WorldCollectionProxy.GetCollectionRecordGroupTemplate(arg_12_1)

	assert("Missing Record Group Config ID. " .. (arg_12_1 or "NIL"))

	arg_12_0.records = _.map(var_12_0.child, function(arg_13_0)
		return WorldCollectionProxy.GetCollectionTemplate(arg_13_0))

	arg_12_0.recordItemList.SetTotalCount(#arg_12_0.records, 0)

	local var_12_1 = #arg_12_0.records
	local var_12_2 = _.reduce(arg_12_0.records, 0, function(arg_14_0, arg_14_1)
		if arg_12_0.CheckRecordIsUnlock(arg_14_1):
			arg_14_0 = arg_14_0 + 1

		return arg_14_0)

	setText(arg_12_0._tf.Find("ItemRect/ProgressText"), var_12_2 .. "/" .. var_12_1)

def var_0_0.CheckRecordIsUnlock(arg_15_0):
	return nowWorld().GetCollectionProxy().IsUnlock(arg_15_0.id) or pg.NewStoryMgr.GetInstance().IsPlayed(arg_15_0.story, True)

def var_0_0.CleanList(arg_16_0):
	arg_16_0.records = None

	arg_16_0.recordItemList.SetTotalCount(0)

return var_0_0
