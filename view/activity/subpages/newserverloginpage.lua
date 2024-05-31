﻿local var_0_0 = class("NewServerLoginPage", import("...base.BaseActivityPage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.item = arg_1_0:findTF("item", arg_1_0.bg)
	arg_1_0.items = arg_1_0:findTF("scrollrect/items", arg_1_0.bg)
	arg_1_0.itemList = UIItemList.New(arg_1_0.items, arg_1_0.item)
end

function var_0_0.OnDataSetting(arg_2_0)
	arg_2_0.config = pg.activity_7_day_sign[arg_2_0.activity:getConfig("config_id")]
	arg_2_0.Day = #arg_2_0.config.front_drops
end

function var_0_0.OnFirstFlush(arg_3_0)
	setActive(arg_3_0.item, false)
	arg_3_0.itemList:make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventInit then
			local var_4_0 = arg_3_0:findTF("item", arg_4_2)
			local var_4_1 = arg_3_0.config.front_drops[arg_4_1 + 1]
			local var_4_2 = {
				type = var_4_1[1],
				id = var_4_1[2],
				count = var_4_1[3]
			}

			updateDrop(var_4_0, var_4_2)
			onButton(arg_3_0, arg_4_2, function()
				arg_3_0:emit(BaseUI.ON_DROP, var_4_2)
			end, SFX_PANEL)
			GetImageSpriteFromAtlasAsync("ui/activityuipage/newserverloginpage_atlas", arg_4_1 + 1, arg_3_0:findTF("day", arg_4_2), true)
		elseif arg_4_0 == UIItemList.EventUpdate then
			local var_4_3 = arg_3_0:findTF("got", arg_4_2)

			setActive(var_4_3, arg_4_1 < arg_3_0.nday)
		end
	end)
	onButton(arg_3_0, arg_3_0:findTF("go_btn", arg_3_0.bg), function()
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.NAVALTACTICS)
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_7_0)
	arg_7_0.nday = arg_7_0.activity.data1

	arg_7_0.itemList:align(arg_7_0.Day)
	setLocalPosition(arg_7_0.items, Vector2(-185 - 106 * (arg_7_0.nday - 1), 0))
end

function var_0_0.OnDestroy(arg_8_0)
	clearImageSprite(arg_8_0.bg)
	removeAllChildren(arg_8_0.items)
end

return var_0_0
