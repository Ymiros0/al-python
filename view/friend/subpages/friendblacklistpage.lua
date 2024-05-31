﻿local var_0_0 = class("FriendBlackListPage", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "FriendBlackListUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.blackListPanel = arg_2_0:findTF("blacklist_panel")
	arg_2_0.blacklistTopTF = arg_2_0:findTF("blacklist_view_top")
end

function var_0_0.OnInit(arg_3_0)
	return
end

function var_0_0.UpdateData(arg_4_0, arg_4_1)
	arg_4_0.blackVOs = arg_4_1.blackVOs

	if not arg_4_0.isInit then
		arg_4_0.isInit = true

		arg_4_0:initBlackList()

		if not arg_4_0.blackVOs then
			arg_4_0:emit(FriendMediator.GET_BLACK_LIST)
		else
			arg_4_0:sortBlackList()
		end
	else
		arg_4_0.blackVOs = arg_4_0.blackVOs or {}

		arg_4_0:sortBlackList()
	end
end

function var_0_0.initBlackList(arg_5_0)
	arg_5_0.blackItems = {}
	arg_5_0.blackRect = arg_5_0.blackListPanel:Find("mask/view"):GetComponent("LScrollRect")

	function arg_5_0.blackRect.onInitItem(arg_6_0)
		arg_5_0:onInitItem(arg_6_0)
	end

	function arg_5_0.blackRect.onUpdateItem(arg_7_0, arg_7_1)
		arg_5_0:onUpdateItem(arg_7_0, arg_7_1)
	end
end

function var_0_0.onInitItem(arg_8_0, arg_8_1)
	local var_8_0 = FriendBlackListCard.New(arg_8_1)

	onButton(arg_8_0, var_8_0.btn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("firend_relieve_blacklist_tip", var_8_0.friendVO.name),
			onYes = function()
				arg_8_0:emit(FriendMediator.RELIEVE_BLACKLIST, var_8_0.friendVO.id)
			end
		})
	end)

	arg_8_0.blackItems[arg_8_1] = var_8_0
end

function var_0_0.onUpdateItem(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_0.blackItems[arg_11_2]

	if not var_11_0 then
		arg_11_0:onInitItem(arg_11_2)

		var_11_0 = arg_11_0.blackItems[arg_11_2]
	end

	local var_11_1 = arg_11_0.blackVOs[arg_11_1 + 1]

	var_11_0:update(var_11_1)
end

function var_0_0.sortBlackList(arg_12_0)
	table.sort(arg_12_0.blackVOs, function(arg_13_0, arg_13_1)
		return arg_13_0.id < arg_13_1.id
	end)
	arg_12_0.blackRect:SetTotalCount(#arg_12_0.blackVOs, -1)
end

function var_0_0.OnDestroy(arg_14_0)
	for iter_14_0, iter_14_1 in pairs(arg_14_0.blackItems or {}) do
		iter_14_1:dispose()
	end
end

return var_0_0
