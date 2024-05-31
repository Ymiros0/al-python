local var_0_0 = class("WorldMediaCollectionMemoryDetailLayer", import(".WorldMediaCollectionSubLayer"))

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionMemoryDetailUI"

def var_0_0.OnInit(arg_2_0):
	var_0_0.super.OnInit(arg_2_0)
	assert(arg_2_0.viewParent, "Need assign ViewParent for " .. arg_2_0.__cname)
	setActive(arg_2_0._tf.Find("ItemRect/TitleRecord"), False)
	setActive(arg_2_0._tf.Find("ItemRect/TitleMemory"), True)

	arg_2_0.memoryItemList = arg_2_0.findTF("ItemRect").GetComponent("LScrollRect")

	function arg_2_0.memoryItemList.onInitItem(arg_3_0)
		arg_2_0.onInitMemoryItem(arg_3_0)

	function arg_2_0.memoryItemList.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.onUpdateMemoryItem(arg_4_0, arg_4_1)

	arg_2_0.memoryItems = {}

	local var_2_0 = arg_2_0.findTF("Item", arg_2_0.memoryItemList)

	setActive(var_2_0, False)

	arg_2_0.loader = AutoLoader.New()

	setText(arg_2_0._tf.Find("ItemRect/ProgressDesc"), i18n("world_collection_2"))

	arg_2_0.rectAnchorX = arg_2_0.findTF("ItemRect").anchoredPosition.x

	arg_2_0.UpdateView()

def var_0_0.onInitMemoryItem(arg_5_0, arg_5_1):
	if arg_5_0.exited:
		return

	onButton(arg_5_0, arg_5_1, function()
		local var_6_0 = arg_5_0.memoryItems[arg_5_1]

		if var_6_0 and (var_6_0.is_open == 1 or pg.NewStoryMgr.GetInstance().IsPlayed(var_6_0.story, True)):
			arg_5_0.PlayMemory(var_6_0), SOUND_BACK)

def var_0_0.onUpdateMemoryItem(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_0.exited:
		return

	local var_7_0 = arg_7_0.memories and arg_7_0.memories[arg_7_1 + 1]

	arg_7_0.memoryItems[arg_7_2] = var_7_0

	local var_7_1 = tf(arg_7_2)

	if var_7_0.is_open == 1 or pg.NewStoryMgr.GetInstance().IsPlayed(var_7_0.story, True):
		setActive(var_7_1.Find("normal"), True)
		setActive(var_7_1.Find("lock"), False)

		var_7_1.Find("normal/title").GetComponent(typeof(Text)).text = var_7_0.title

		arg_7_0.loader.GetSpriteQuiet("memoryicon/" .. var_7_0.icon, "", var_7_1.Find("normal"))
		setText(var_7_1.Find("normal/id"), string.format("#%u", arg_7_1 + 1))
	else
		setActive(var_7_1.Find("normal"), False)
		setActive(var_7_1.Find("lock"), True)
		setText(var_7_1.Find("lock/condition"), var_7_0.condition)

def var_0_0.SetStoryMask(arg_8_0, arg_8_1):
	arg_8_0.memoryMask = arg_8_1

def var_0_0.PlayMemory(arg_9_0, arg_9_1):
	if arg_9_1.type == 1:
		local var_9_0 = findTF(arg_9_0.memoryMask, "pic")

		if string.len(arg_9_1.mask) > 0:
			setActive(var_9_0, True)

			var_9_0.GetComponent(typeof(Image)).sprite = LoadSprite(arg_9_1.mask)
		else
			setActive(var_9_0, False)

		setActive(arg_9_0.memoryMask, True)
		pg.NewStoryMgr.GetInstance().Play(arg_9_1.story, function()
			setActive(arg_9_0.memoryMask, False), True)
	elif arg_9_1.type == 2:
		local var_9_1 = pg.NewStoryMgr.GetInstance().StoryName2StoryId(arg_9_1.story)

		assert(var_9_1 and var_9_1 != 0, "Missing Story Stage ID. " .. (arg_9_1.story or "NIL"))
		arg_9_0.emit(WorldMediaCollectionMediator.BEGIN_STAGE, {
			memory = True,
			system = SYSTEM_PERFORM,
			stageId = var_9_1
		})

def var_0_0.ShowSubMemories(arg_11_0, arg_11_1):
	arg_11_0.contextData.memoryGroup = arg_11_1.id
	arg_11_0.memories = _.map(arg_11_1.memories, function(arg_12_0)
		return pg.memory_template[arg_12_0])

	arg_11_0.memoryItemList.SetTotalCount(#arg_11_0.memories, 0)

	local var_11_0 = #arg_11_0.memories
	local var_11_1 = _.reduce(arg_11_0.memories, 0, function(arg_13_0, arg_13_1)
		if arg_13_1.is_open == 1 or pg.NewStoryMgr.GetInstance().IsPlayed(arg_13_1.story, True):
			arg_13_0 = arg_13_0 + 1

		return arg_13_0)

	setText(arg_11_0._tf.Find("ItemRect/ProgressText"), var_11_1 .. "/" .. var_11_0)

	local var_11_2 = _.filter(pg.re_map_template.all, function(arg_14_0)
		return pg.re_map_template[arg_14_0].memory_group == arg_11_1.id)
	local var_11_3 = var_11_1 < var_11_0 and #var_11_2 > 0

	setActive(arg_11_0._tf.Find("ItemRect/UnlockTip"), var_11_3)

	if var_11_3:
		local var_11_4 = _.map(_.sort(Map.GetRearChaptersOfRemaster(var_11_2[1])), function(arg_15_0)
			return getProxy(ChapterProxy).getChapterById(arg_15_0, True).getConfig("chapter_name"))

		setText(arg_11_0._tf.Find("ItemRect/UnlockTip"), i18n("levelScene_remaster_unlock_tip", arg_11_1.title, table.concat(var_11_4, "/")))

def var_0_0.CleanList(arg_16_0):
	arg_16_0.memories = None

	arg_16_0.memoryItemList.SetTotalCount(0)

def var_0_0.UpdateView(arg_17_0):
	local var_17_0 = WorldMediaCollectionScene.WorldRecordLock()

	setAnchoredPosition(arg_17_0.findTF("ItemRect"), {
		x = var_17_0 and 0 or arg_17_0.rectAnchorX
	})

return var_0_0
