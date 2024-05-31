local var_0_0 = class("WorldMediaCollectionFileDetailLayer", import(".WorldMediaCollectionSubLayer"))

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionFileDetailUI"

def var_0_0.OnInit(arg_2_0):
	assert(arg_2_0.viewParent, "Need assign ViewParent for " .. arg_2_0.__cname)
	onButton(arg_2_0, arg_2_0._tf.Find("Buttom"), function()
		arg_2_0.viewParent.Backward())

	arg_2_0.anim = arg_2_0._tf.GetComponent(typeof(Animation))
	arg_2_0.canvasGroup = arg_2_0._tf.GetComponent(typeof(CanvasGroup))

	arg_2_0.InitDocument()

	local var_2_0 = arg_2_0._tf.Find("ArchiveList")

	arg_2_0.scrollComp = var_2_0.GetComponent("LScrollRect")
	arg_2_0.fileChild = {}
	arg_2_0.fileChildIndex = {}

	function arg_2_0.scrollComp.onUpdateItem(arg_4_0, ...)
		arg_2_0.OnUpdateFile(arg_4_0 + 1, ...)

	setActive(var_2_0.Find("Item"), False)

	arg_2_0.loader = AutoLoader.New()

	setText(arg_2_0._tf.Find("ArchiveList/ProgressDesc"), i18n("world_collection_1"))

def var_0_0.InitDocument(arg_5_0):
	arg_5_0.document = arg_5_0._tf.Find("Document")
	arg_5_0.documentContentTF = arg_5_0.document.Find("Viewport/Content")
	arg_5_0.documentHead = arg_5_0.documentContentTF.Find("Head")
	arg_5_0.documentBody = arg_5_0.documentContentTF.Find("Body")
	arg_5_0.documentTitle = arg_5_0.documentHead.Find("Title")
	arg_5_0.documentRect = arg_5_0.documentBody.Find("Rect")
	arg_5_0.documentTip = arg_5_0.documentRect.Find("SubTitle")
	arg_5_0.documentText = arg_5_0.documentRect.Find("Text")
	arg_5_0.documentImage = arg_5_0.documentRect.Find("Image")
	arg_5_0.documentStamp = arg_5_0.documentImage.Find("ClassifiedStamp")

def var_0_0.Openning(arg_6_0):
	arg_6_0.anim.Play("Enter")
	arg_6_0.Enter()

def var_0_0.Enter(arg_7_0):
	local function var_7_0()
		local var_8_0 = nowWorld().GetCollectionProxy()
		local var_8_1 = WorldCollectionProxy.GetCollectionFileGroupTemplate(arg_7_0.contextData.FileGroupIndex)

		for iter_8_0, iter_8_1 in ipairs(var_8_1.child):
			if var_8_0.IsUnlock(iter_8_1):
				return iter_8_0

	local var_7_1 = arg_7_0.contextData.SelectedFile or var_7_0()

	arg_7_0.contextData.SelectedFile = None

	arg_7_0.UpdateView()
	arg_7_0.SwitchFileIndex(var_7_1)

def var_0_0.Hide(arg_9_0):
	arg_9_0.canvasGroup.alpha = 1

	var_0_0.super.Hide(arg_9_0)

def var_0_0.UpdateView(arg_10_0):
	assert(arg_10_0.contextData.FileGroupIndex, "Not Initialize FileGroupIndex")

	arg_10_0.archiveList = _.map(WorldCollectionProxy.GetCollectionFileGroupTemplate(arg_10_0.contextData.FileGroupIndex).child, function(arg_11_0)
		return WorldCollectionProxy.GetCollectionTemplate(arg_11_0))

	local var_10_0 = nowWorld().GetCollectionProxy()
	local var_10_1 = WorldCollectionProxy.GetCollectionFileGroupTemplate(arg_10_0.contextData.FileGroupIndex)
	local var_10_2 = 0
	local var_10_3 = #var_10_1.child

	for iter_10_0, iter_10_1 in ipairs(var_10_1.child):
		if var_10_0.IsUnlock(iter_10_1):
			var_10_2 = var_10_2 + 1

	setText(arg_10_0._tf.Find("ArchiveList/ProgressDesc/ProgressText"), var_10_2 .. "/" .. var_10_3)
	arg_10_0.scrollComp.SetTotalCount(#arg_10_0.archiveList)

local function var_0_1(arg_12_0)
	return (string.char(226, 133, 160 + (arg_12_0 - 1)))

def var_0_0.OnUpdateFile(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.exited:
		return

	local var_13_0 = arg_13_0.archiveList[arg_13_1]

	if arg_13_0.fileChildIndex[arg_13_2] and arg_13_0.fileChildIndex[arg_13_2] != arg_13_1:
		local var_13_1 = arg_13_0.fileChildIndex[arg_13_2]

		arg_13_0.fileChild[var_13_1] = None

	arg_13_0.fileChildIndex[arg_13_2] = arg_13_1
	arg_13_0.fileChild[arg_13_1] = arg_13_2

	local var_13_2 = nowWorld().GetCollectionProxy()
	local var_13_3 = tf(arg_13_2)
	local var_13_4 = WorldCollectionProxy.GetCollectionFileGroupTemplate(arg_13_0.contextData.FileGroupIndex)
	local var_13_5 = var_13_2.IsUnlock(var_13_0.id)
	local var_13_6 = arg_13_1 == arg_13_0.contextData.SelectedFile

	setActive(var_13_3.Find("Selected"), var_13_6)

	local var_13_7 = string.format("%s %s", shortenString(var_13_4.name or "", 6), var_0_1(var_13_0.group_ID))

	setText(var_13_3.Find("Desc"), setColorStr(var_13_7, var_13_6 and "#000" or COLOR_WHITE))
	setActive(var_13_3.Find("Desc"), var_13_5)
	setActive(var_13_3.Find("Icon"), var_13_5)
	setActive(var_13_3.Find("Cover"), var_13_5)
	setActive(var_13_3.Find("Locked"), not var_13_5)
	arg_13_0.loader.GetSprite("ui/WorldMediaCollectionFileDetailUI_atlas", "cover" .. var_13_4.type, var_13_3.Find("Cover"))
	onButton(arg_13_0, var_13_3, function()
		if not nowWorld().GetCollectionProxy().IsUnlock(var_13_0.id):
			return

		arg_13_0.SwitchFileIndex(arg_13_1), SFX_PANEL)

def var_0_0.SwitchFileIndex(arg_15_0, arg_15_1):
	if arg_15_0.contextData.SelectedFile and arg_15_0.contextData.SelectedFile == arg_15_1:
		return

	local var_15_0 = arg_15_1 and arg_15_0.archiveList[arg_15_1]

	if var_15_0 and nowWorld().GetCollectionProxy().IsUnlock(var_15_0.id):
		local var_15_1 = arg_15_0.contextData.SelectedFile
		local var_15_2 = arg_15_0.fileChild[var_15_1]

		arg_15_0.contextData.SelectedFile = arg_15_1

		if var_15_2:
			arg_15_0.OnUpdateFile(var_15_1, var_15_2)

		if arg_15_0.fileChild[arg_15_1]:
			arg_15_0.OnUpdateFile(arg_15_1, arg_15_0.fileChild[arg_15_1])

		setActive(arg_15_0.document, True)
		setText(arg_15_0.document.Find("Head/Title"), var_15_0.name)
		arg_15_0.SetDocument(var_15_0)
	else
		setActive(arg_15_0.document, False)

def var_0_0.SetDocument(arg_16_0, arg_16_1, arg_16_2):
	setText(arg_16_0.documentTitle, arg_16_1.name)

	local var_16_0 = arg_16_1.pic

	if var_16_0 and #var_16_0 > 0:
		local var_16_1 = LoadSprite("CollectionFileIllustration/" .. var_16_0, "")

		setImageSprite(arg_16_0.documentImage, var_16_1, True)
		setActive(arg_16_0.documentImage, var_16_1)

		if var_16_1:
			setActive(arg_16_0.documentStamp, arg_16_1.is_classified == 1)

			if arg_16_1.is_classified == 1:
				local var_16_2 = WorldCollectionProxy.GetCollectionGroup(arg_16_1.id)
				local var_16_3 = WorldCollectionProxy.GetCollectionFileGroupTemplate(var_16_2).type

				arg_16_0.loader.GetSprite("ui/WorldMediaCollectionFileDetailUI_atlas", "stamp" .. var_16_3, arg_16_0.documentStamp)
	else
		setActive(arg_16_0.documentImage, False)

	arg_16_0.SetDocumentText(arg_16_1.content, arg_16_1.subTitle, arg_16_2)

def var_0_0.getTextPreferredHeight(arg_17_0, arg_17_1, arg_17_2):
	local var_17_0 = arg_17_0.cachedTextGeneratorForLayout
	local var_17_1 = arg_17_0.GetGenerationSettings(Vector2(arg_17_1, 0))

	return ReflectionHelp.RefCallMethod(typeof("UnityEngine.TextGenerator"), "GetPreferredHeight", var_17_0, {
		typeof("System.String"),
		typeof("UnityEngine.TextGenerationSettings")
	}, {
		arg_17_2,
		var_17_1
	}) / arg_17_0.pixelsPerUnit

def var_0_0.SetDocumentText(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_0.documentRect.rect.width
	local var_18_1 = isActive(arg_18_0.documentImage)
	local var_18_2 = var_18_1 and arg_18_0.documentImage.rect.width or 0
	local var_18_3 = math.max(var_18_0 - var_18_2, 0)
	local var_18_4 = arg_18_0.documentImage.rect.height
	local var_18_5 = var_18_1 and var_18_4 + 100 or 0
	local var_18_6 = arg_18_0.documentText.GetComponent(typeof(Text))

	var_18_6.text = ""

	local var_18_7 = ""

	local function var_18_8()
		local var_19_0 = 0

		if isActive(arg_18_0.documentHead):
			var_19_0 = var_19_0 + arg_18_0.documentHead.GetComponent(typeof(LayoutElement)).preferredHeight

		local var_19_1 = arg_18_0.documentBody.GetComponent("LayoutGroup")
		local var_19_2 = var_19_0 + (var_19_1.padding.top + var_19_1.padding.bottom)

		setActive(arg_18_0.documentTip, arg_18_2 and #arg_18_2 > 0)

		local var_19_3 = 0

		if arg_18_2 and #arg_18_2 > 0:
			local var_19_4 = arg_18_0.documentTip.Find("Text").GetComponent(typeof(Text))

			var_19_4.text = arg_18_2
			var_19_3 = var_0_0.getTextPreferredHeight(var_19_4, var_18_0, arg_18_2)
			var_19_3 = var_19_3 + arg_18_0.documentRect.GetComponent(typeof(VerticalLayoutGroup)).spacing
			var_19_2 = var_19_2 + var_19_3

		if var_18_1:
			arg_18_0.documentImage.anchoredPosition = Vector2(0, -50 - var_19_3)

		local var_19_5 = var_0_0.getTextPreferredHeight(var_18_6, var_18_0, var_18_7)
		local var_19_6 = var_19_2 + var_19_5
		local var_19_7 = arg_18_0.documentContentTF.sizeDelta

		var_19_7.y = var_19_6
		arg_18_0.documentContentTF.sizeDelta = var_19_7

		local var_19_8 = arg_18_0.document.Find("Viewport")
		local var_19_9 = arg_18_0.document.Find("Arrow")
		local var_19_10 = var_19_8.rect.height

		setActive(var_19_9, var_19_10 < var_19_6)

		local var_19_11 = arg_18_0.document.GetComponent(typeof(ScrollRect))

		var_19_11.onValueChanged.RemoveAllListeners()

		arg_18_3 = arg_18_3 or 0

		local var_19_12 = math.max(var_19_5 - var_19_10, 0) * arg_18_3

		arg_18_0.documentContentTF.anchoredPosition = Vector2(0, var_19_12)
		var_19_11.velocity = Vector2.zero

		if var_19_10 < var_19_6:
			onScroll(arg_18_0, arg_18_0.document, function(arg_20_0)
				setActive(var_19_9, arg_20_0.y > 0.01))

	if not var_18_1:
		var_18_7 = arg_18_1
		var_18_6.text = var_18_7

		var_18_8()

		return

	local var_18_9, var_18_10 = arg_18_0.SplitRichAndLetters(arg_18_1)
	local var_18_11 = 1
	local var_18_12 = 1

	local function var_18_13(arg_21_0)
		local var_21_0 = ""
		local var_21_1 = ""
		local var_21_2 = {}

		for iter_21_0 = arg_21_0 and 1 or var_18_12, #var_18_10:
			if var_18_10[iter_21_0].start > var_18_9[var_18_11].start:
				break

			local var_21_3 = var_18_10[iter_21_0]

			if iter_21_0 == var_18_12:
				var_18_12 = var_18_12 + 1
				var_21_0 = var_21_0 .. var_21_3.value

			if arg_21_0:
				if var_21_3.EndTagIndex:
					var_21_2[#var_21_2 + 1] = var_21_3.EndTagIndex
				else
					table.remove(var_21_2)

		local var_21_4 = ""

		if var_18_11 <= #var_18_9:
			var_21_4 = var_18_9[var_18_11].value

		for iter_21_1, iter_21_2 in ipairs(var_21_2):
			var_21_1 = var_18_10[iter_21_2].value .. var_21_1

		var_18_11 = var_18_11 + 1

		return var_21_4, var_21_0, var_21_1

	local var_18_14 = 0

	while var_18_14 < var_18_5 and var_18_11 < #var_18_9:
		local var_18_15, var_18_16, var_18_17 = var_18_13(True)
		local var_18_18 = var_18_7 .. var_18_16 .. var_18_15 .. var_18_17

		var_18_6.text = var_18_18

		if var_18_3 < var_18_6.preferredWidth:
			var_18_18 = var_18_7 .. "\n" .. var_18_16 .. var_18_15
		else
			var_18_18 = var_18_7 .. var_18_16 .. var_18_15

		var_18_7 = var_18_18
		var_18_6.text = var_18_7
		var_18_14 = var_0_0.getTextPreferredHeight(var_18_6, var_18_6.preferredWidth, var_18_7)

	for iter_18_0 = var_18_11, #var_18_9:
		local var_18_19, var_18_20 = var_18_13(False)

		var_18_7 = var_18_7 .. var_18_20 .. var_18_19

	local var_18_21, var_18_22, var_18_23 = var_18_13(True)

	var_18_7 = var_18_7 .. var_18_23
	var_18_6.text = var_18_7

	var_18_8()

def var_0_0.SplitRichAndLetters(arg_22_0):
	local var_22_0 = 1
	local var_22_1 = "<([^>]*)>"
	local var_22_2 = {}
	local var_22_3 = {}

	while True:
		local var_22_4, var_22_5 = string.find(arg_22_0, var_22_1, var_22_0)

		if not var_22_5:
			break

		local var_22_6 = string.sub(arg_22_0, var_22_4, var_22_5)
		local var_22_7 = string.find(var_22_6, "=")
		local var_22_8 = string.find(var_22_6, "/")

		if not var_22_8 and not var_22_7:
			var_22_0 = var_22_5 + 1
		else
			table.insert(var_22_2, {
				value = var_22_6,
				start = var_22_4
			})

			if var_22_7:
				var_22_3[#var_22_3 + 1] = #var_22_2
			elif var_22_8 and #var_22_3 > 0:
				var_22_2[table.remove(var_22_3)].EndTagIndex = #var_22_2

			local var_22_9 = string.sub(arg_22_0, var_22_5 + 1, -1)

			arg_22_0 = string.sub(arg_22_0, 1, var_22_4 - 1) .. var_22_9
			var_22_0 = var_22_4

	local var_22_10 = {}
	local var_22_11 = 1
	local var_22_12 = False
	local var_22_13 = 1

	while True:
		local var_22_14, var_22_15 = string.find(arg_22_0, "[\x01-\x7F\xC2-\xF4][\x80-\xBF]*", var_22_11)

		if not var_22_15:
			var_22_10[#var_22_10 + 1] = {
				value = string.sub(arg_22_0, var_22_13, #arg_22_0),
				start = var_22_13
			}

			break

		local var_22_16 = string.sub(arg_22_0, var_22_14, var_22_15)
		local var_22_17 = False

		if PLATFORM_CODE == PLATFORM_US:
			local var_22_18 = var_22_16 == " " or var_22_16 == " "

			if var_22_12 != var_22_18:
				var_22_17 = var_22_14 > 1

			var_22_12 = var_22_18
		else
			var_22_17 = var_22_14 > 1

		if var_22_17:
			var_22_10[#var_22_10 + 1] = {
				value = string.sub(arg_22_0, var_22_13, var_22_14 - 1),
				start = var_22_13
			}
			var_22_13 = var_22_14

		var_22_11 = var_22_15 + 1

	return var_22_10, var_22_2

return var_0_0
