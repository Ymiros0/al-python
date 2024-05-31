local var_0_0 = class("WorldMediaCollectionMemoryGroupLayer", import(".WorldMediaCollectionSubLayer"))

function var_0_0.getUIName(arg_1_0)
	return "WorldMediaCollectionMemoryGroupUI"
end

var_0_0.PAGE_ACTIVITY = 2

function var_0_0.OnInit(arg_2_0)
	var_0_0.super.OnInit(arg_2_0)
	assert(arg_2_0.viewParent, "Need assign ViewParent for " .. arg_2_0.__cname)

	arg_2_0.memoryGroups = _.map(pg.memory_group.all, function(arg_3_0)
		return pg.memory_group[arg_3_0]
	end)
	arg_2_0.memoryGroupList = arg_2_0:findTF("GroupRect"):GetComponent("LScrollRect")

	function arg_2_0.memoryGroupList.onInitItem(arg_4_0)
		arg_2_0:onInitMemoryGroup(arg_4_0)
	end

	function arg_2_0.memoryGroupList.onUpdateItem(arg_5_0, arg_5_1)
		arg_2_0:onUpdateMemoryGroup(arg_5_0 + 1, arg_5_1)
	end

	arg_2_0.memoryGroupInfos = {}

	local var_2_0 = arg_2_0:findTF("GroupItem", arg_2_0.memoryGroupList)

	setActive(var_2_0, false)

	arg_2_0.memoryGroupViewport = arg_2_0:findTF("Viewport", arg_2_0.memoryGroupList)
	arg_2_0.memoryGroupsGrid = arg_2_0:findTF("Viewport/Content", arg_2_0.memoryGroupList):GetComponent(typeof(GridLayoutGroup))
	arg_2_0.memoryTogGroup = arg_2_0:findTF("Toggles", arg_2_0._tf)

	setActive(arg_2_0.memoryTogGroup, true)

	arg_2_0.memoryToggles = {}

	for iter_2_0 = 0, 3 do
		arg_2_0.memoryToggles[iter_2_0 + 1] = arg_2_0:findTF(iter_2_0, arg_2_0.memoryTogGroup)
	end

	arg_2_0.memoryFilterIndex = {
		true,
		true,
		true
	}
	arg_2_0.memoryActivityTogGroup = arg_2_0:findTF("ActivityBar", arg_2_0._tf)

	setActive(arg_2_0.memoryActivityTogGroup, true)

	arg_2_0.memoryActivityToggles = {}

	for iter_2_1 = 0, 3 do
		arg_2_0.memoryActivityToggles[iter_2_1 + 1] = arg_2_0:findTF(iter_2_1, arg_2_0.memoryActivityTogGroup)
	end

	arg_2_0.activityFilter = 0

	arg_2_0:UpdateActivityBar()

	for iter_2_2, iter_2_3 in ipairs(arg_2_0.memoryActivityToggles) do
		onButton(arg_2_0, iter_2_3, function()
			if iter_2_2 == arg_2_0.activityFilter then
				arg_2_0.activityFilter = 0
			elseif iter_2_2 ~= arg_2_0.activityFilter then
				arg_2_0.activityFilter = iter_2_2
			end

			arg_2_0:UpdateActivityBar()
			arg_2_0:MemoryFilter()
		end, SFX_UI_TAG)
	end

	setText(arg_2_0.memoryActivityToggles[1]:Find("Image1/Text"), i18n("memory_actiivty_ex"))
	setText(arg_2_0.memoryActivityToggles[1]:Find("Image2/Text"), i18n("memory_actiivty_ex"))
	setText(arg_2_0.memoryActivityToggles[2]:Find("Image1/Text"), i18n("memory_activity_sp"))
	setText(arg_2_0.memoryActivityToggles[2]:Find("Image2/Text"), i18n("memory_activity_sp"))
	setText(arg_2_0.memoryActivityToggles[3]:Find("Image1/Text"), i18n("memory_activity_daily"))
	setText(arg_2_0.memoryActivityToggles[3]:Find("Image2/Text"), i18n("memory_activity_daily"))
	setText(arg_2_0.memoryActivityToggles[4]:Find("Image1/Text"), i18n("memory_activity_others"))
	setText(arg_2_0.memoryActivityToggles[4]:Find("Image2/Text"), i18n("memory_activity_others"))

	arg_2_0.contextData.toggle = arg_2_0.contextData.toggle or 1

	local var_2_1 = arg_2_0.contextData.toggle

	triggerToggle(arg_2_0.memoryToggles[var_2_1], true)
	arg_2_0:SwitchMemoryFilter(var_2_1)

	for iter_2_4, iter_2_5 in ipairs(arg_2_0.memoryToggles) do
		onToggle(arg_2_0, iter_2_5, function(arg_7_0)
			if not arg_7_0 then
				return
			end

			arg_2_0:SwitchMemoryFilter(iter_2_4)
			arg_2_0:MemoryFilter()
		end, SFX_UI_TAG)
	end

	arg_2_0.viewParent:Add2TopContainer(arg_2_0.memoryTogGroup)

	arg_2_0.loader = AutoLoader.New()

	arg_2_0:MemoryFilter()

	arg_2_0.rectAnchorX = arg_2_0:findTF("GroupRect").anchoredPosition.x

	arg_2_0:UpdateView()
end

function var_0_0.Show(arg_8_0)
	var_0_0.super.Show(arg_8_0)
	setActive(arg_8_0.memoryTogGroup, true)
end

function var_0_0.Hide(arg_9_0)
	setActive(arg_9_0.memoryTogGroup, false)
	var_0_0.super.Hide(arg_9_0)
end

function var_0_0.SwitchMemoryFilter(arg_10_0, arg_10_1)
	if arg_10_1 == 1 then
		arg_10_0.memoryFilterIndex = {
			true,
			true,
			true
		}
	else
		for iter_10_0 in ipairs(arg_10_0.memoryFilterIndex) do
			arg_10_0.memoryFilterIndex[iter_10_0] = arg_10_1 - 1 == iter_10_0
		end

		if arg_10_1 - 1 == var_0_0.PAGE_ACTIVITY then
			arg_10_0.activityFilter = 0

			arg_10_0:UpdateActivityBar()
		end
	end
end

function var_0_0.MemoryFilter(arg_11_0)
	table.clear(arg_11_0.memoryGroups)

	local var_11_0 = not _.all(arg_11_0.memoryFilterIndex, function(arg_12_0)
		return arg_12_0
	end) and arg_11_0.memoryFilterIndex[var_0_0.PAGE_ACTIVITY]

	for iter_11_0, iter_11_1 in ipairs(pg.memory_group.all) do
		local var_11_1 = pg.memory_group[iter_11_1]

		if arg_11_0.memoryFilterIndex[var_11_1.type] then
			if var_11_0 then
				if arg_11_0.activityFilter == 0 or arg_11_0.activityFilter == var_11_1.subtype then
					table.insert(arg_11_0.memoryGroups, var_11_1)
				end
			else
				table.insert(arg_11_0.memoryGroups, var_11_1)
			end
		end
	end

	table.sort(arg_11_0.memoryGroups, function(arg_13_0, arg_13_1)
		return arg_13_0.id < arg_13_1.id
	end)
	arg_11_0.memoryGroupList:SetTotalCount(#arg_11_0.memoryGroups, 0)
	setActive(arg_11_0.memoryActivityTogGroup, var_11_0)
end

function var_0_0.onInitMemoryGroup(arg_14_0, arg_14_1)
	if arg_14_0.exited then
		return
	end

	onButton(arg_14_0, arg_14_1, function()
		local var_15_0 = arg_14_0.memoryGroupInfos[arg_14_1]

		if var_15_0 then
			local var_15_1 = getProxy(PlayerProxy):getRawData().id

			PlayerPrefs.DeleteKey("MEMORY_GROUP_NOTIFICATION" .. var_15_1 .. " " .. var_15_0.id)
			arg_14_0.viewParent:ShowSubMemories(var_15_0)
		end
	end, SOUND_BACK)
end

function var_0_0.onUpdateMemoryGroup(arg_16_0, arg_16_1, arg_16_2)
	if arg_16_0.exited then
		return
	end

	local var_16_0 = arg_16_0.memoryGroups[arg_16_1]

	assert(var_16_0, "MemoryGroup Missing Config Index " .. arg_16_1)

	arg_16_0.memoryGroupInfos[arg_16_2] = var_16_0

	setText(tf(arg_16_2):Find("title"), var_16_0.title)
	arg_16_0.loader:GetSpriteQuiet("memoryicon/" .. var_16_0.icon, "", tf(arg_16_2):Find("BG"))

	local var_16_1 = getProxy(PlayerProxy):getRawData().id
	local var_16_2 = PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. var_16_1 .. " " .. var_16_0.id, 0) == 1

	setActive(tf(arg_16_2):Find("Tip"), var_16_2)

	local var_16_3 = #var_16_0.memories
	local var_16_4 = _.reduce(var_16_0.memories, 0, function(arg_17_0, arg_17_1)
		local var_17_0 = pg.memory_template[arg_17_1]

		if var_17_0.is_open == 1 or pg.NewStoryMgr.GetInstance():IsPlayed(var_17_0.story, true) then
			arg_17_0 = arg_17_0 + 1
		end

		return arg_17_0
	end)

	setText(tf(arg_16_2):Find("count"), var_16_4 .. "/" .. var_16_3)
end

function var_0_0.Return2MemoryGroup(arg_18_0)
	local var_18_0 = arg_18_0.contextData.memoryGroup

	if not var_18_0 then
		return
	end

	local var_18_1 = 0

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.memoryGroups) do
		if iter_18_1.id == var_18_0 then
			var_18_1 = iter_18_0

			break
		end
	end

	local var_18_2 = arg_18_0:GetIndexRatio(var_18_1)

	arg_18_0.memoryGroupList:SetTotalCount(#arg_18_0.memoryGroups, var_18_2)
end

function var_0_0.SwitchReddotMemory(arg_19_0)
	local var_19_0 = 0
	local var_19_1 = getProxy(PlayerProxy):getRawData().id

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.memoryGroups) do
		if PlayerPrefs.GetInt("MEMORY_GROUP_NOTIFICATION" .. var_19_1 .. " " .. iter_19_1.id, 0) == 1 then
			var_19_0 = iter_19_0

			break
		end
	end

	if var_19_0 == 0 then
		return
	end

	local var_19_2 = arg_19_0:GetIndexRatio(var_19_0)

	arg_19_0.memoryGroupList:SetTotalCount(#arg_19_0.memoryGroups, var_19_2)
end

function var_0_0.GetIndexRatio(arg_20_0, arg_20_1)
	local var_20_0 = 0

	if arg_20_1 > 0 then
		local var_20_1 = arg_20_0.memoryGroupList
		local var_20_2 = arg_20_0.memoryGroupsGrid.cellSize.y + arg_20_0.memoryGroupsGrid.spacing.y
		local var_20_3 = arg_20_0.memoryGroupsGrid.constraintCount
		local var_20_4 = var_20_2 * math.ceil(#arg_20_0.memoryGroups / var_20_3)

		var_20_0 = (var_20_2 * math.floor((arg_20_1 - 1) / var_20_3) + var_20_1.paddingFront) / (var_20_4 - arg_20_0.memoryGroupViewport.rect.height)
		var_20_0 = Mathf.Clamp01(var_20_0)
	end

	return var_20_0
end

function var_0_0.UpdateView(arg_21_0)
	local var_21_0 = WorldMediaCollectionScene.WorldRecordLock()

	setAnchoredPosition(arg_21_0:findTF("GroupRect"), {
		x = var_21_0 and 0 or arg_21_0.rectAnchorX
	})

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.memoryActivityToggles) do
		setActive(iter_21_1, _.any(pg.memory_group.all, function(arg_22_0)
			return pg.memory_group[arg_22_0].subtype == iter_21_0
		end))
	end
end

function var_0_0.UpdateActivityBar(arg_23_0)
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.memoryActivityToggles) do
		local var_23_0 = arg_23_0.activityFilter == iter_23_0

		setActive(iter_23_1:Find("Image1"), not var_23_0)
		setActive(iter_23_1:Find("Image2"), var_23_0)
	end
end

return var_0_0
