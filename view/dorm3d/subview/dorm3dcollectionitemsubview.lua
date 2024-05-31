local var_0_0 = class("Dorm3dCollectionItemSubView", import("view.base.BaseSubView"))

function var_0_0.OnLoaded(arg_1_0)
	local var_1_0 = arg_1_0._tf:Find("list/container")

	arg_1_0.itemList = UIItemList.New(var_1_0, var_1_0:Find("tpl"))

	arg_1_0.itemList:make(function(arg_2_0, arg_2_1, arg_2_2)
		arg_2_1 = arg_2_1 + 1

		if arg_2_0 == UIItemList.EventUpdate then
			local var_2_0 = arg_1_0.ids[arg_2_1]
			local var_2_1 = pg.dorm3d_collection_template[var_2_0]
			local var_2_2 = arg_1_0.unlockDic[var_2_0]
			local var_2_3 = arg_1_0.contextData.apartment:checkUnlockConfig(var_2_1.unlock)
			local var_2_4 = arg_2_1

			for iter_2_0 = 1, 2 do
				cloneTplTo(arg_1_0.numContainer:Find("num_" .. var_2_4 % 10), arg_2_2:Find("num"))

				var_2_4 = math.floor(var_2_4 / 10)
			end

			setActive(arg_2_2:Find("content/lock"), not var_2_3)
			setActive(arg_2_2:Find("content/mark"), var_2_3 and not var_2_2)
			setText(arg_2_2:Find("content/name"), var_2_2 and var_2_1.name or string.format("locked:%s", var_2_0))
			onToggle(arg_1_0, arg_2_2, function(arg_3_0)
				if arg_3_0 then
					arg_1_0:UpdateDisplay(arg_2_1, var_2_0)
				end

				setTextColor(arg_2_2:Find("content/name"), Color.NewHex(not var_2_2 and "a9a9a9" or arg_3_0 and "2d1dfc" or "393a3c"))
				eachChild(arg_2_2:Find("num"), function(arg_4_0)
					setImageColor(arg_4_0, Color.NewHex(arg_3_0 and "2d1dfd" or "393a3c"))
				end)
			end, SFX_PANEL)
		end
	end)

	arg_1_0.numContainer = arg_1_0._tf:Find("list/number")
	arg_1_0.rtInfo = arg_1_0._tf:Find("info")
end

function var_0_0.OnInit(arg_5_0)
	local var_5_0 = arg_5_0.contextData.apartment

	arg_5_0.unlockDic = var_5_0.collectItemDic

	setText(arg_5_0.rtInfo:Find("count"), string.format("<color=#2d1dfc>%d</color>/%d", table.getCount(arg_5_0.unlockDic), #var_5_0:getCollectConfig("recall_list")))
	setText(arg_5_0.rtInfo:Find("empty"), "with out anything")

	arg_5_0.ids = var_5_0:getCollectConfig("collection_template_list")

	arg_5_0.itemList:align(#arg_5_0.ids)
	triggerToggle(arg_5_0.itemList.container:GetChild(0), true)
end

function var_0_0.UpdateDisplay(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0 = arg_6_0.unlockDic[arg_6_2]

	setActive(arg_6_0.rtInfo:Find("empty"), not var_6_0)

	local var_6_1 = arg_6_0.rtInfo:Find("content")

	setActive(var_6_1, var_6_0)

	if not var_6_0 then
		return
	end

	local var_6_2 = pg.dorm3d_collection_template[arg_6_2]

	GetImageSpriteFromAtlasAsync("dorm3dcollection/" .. var_6_2.model, "", var_6_1:Find("icon"), true)
	setText(var_6_1:Find("name/Text"), var_6_2.name)
	setText(var_6_1:Find("desc"), var_6_2.desc)

	local var_6_3 = pg.dorm3d_favor_trigger[var_6_2.award].num

	setText(var_6_1:Find("favor/Text"), string.format("favor plus:%d", var_6_3))
end

function var_0_0.OnDestroy(arg_7_0)
	return
end

return var_0_0
