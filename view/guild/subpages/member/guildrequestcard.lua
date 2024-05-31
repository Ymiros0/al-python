local var_0_0 = class("GuildRequestCard")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.nameTF = arg_1_0.tf:Find("frame/request_info/name"):GetComponent(typeof(Text))
	arg_1_0.levelTF = arg_1_0.tf:Find("frame/request_info/level"):GetComponent(typeof(Text))
	arg_1_0.dateTF = arg_1_0.tf:Find("frame/request_info/date"):GetComponent(typeof(Text))
	arg_1_0.msg = arg_1_0.tf:Find("frame/request_content/Text"):GetComponent(typeof(Text))
	arg_1_0.iconTF = arg_1_0.tf:Find("frame/shipicon/icon"):GetComponent(typeof(Image))
	arg_1_0.starsTF = arg_1_0.tf:Find("frame/shipicon/stars")
	arg_1_0.circle = arg_1_0.tf:Find("frame/shipicon/frame")
	arg_1_0.starTF = arg_1_0.tf:Find("frame/shipicon/stars/star")
	arg_1_0.rejectBtn = arg_1_0.tf:Find("frame/refuse_btn")
	arg_1_0.accpetBtn = arg_1_0.tf:Find("frame/accpet_btn")
end

function var_0_0.Update(arg_2_0, arg_2_1)
	arg_2_0:Clear()

	arg_2_0.requestVO = arg_2_1
	arg_2_0.nameTF.text = arg_2_1.player.name
	arg_2_0.levelTF.text = "Lv." .. arg_2_1.player.level

	local var_2_0 = getOfflineTimeStamp(arg_2_1.timestamp)

	arg_2_0.dateTF.text = var_2_0
	arg_2_0.msg.text = arg_2_1.content

	local var_2_1 = arg_2_1.player
	local var_2_2 = AttireFrame.attireFrameRes(var_2_1, var_2_1.id == getProxy(PlayerProxy):getRawData().id, AttireConst.TYPE_ICON_FRAME, var_2_1.propose)

	PoolMgr.GetInstance():GetPrefab("IconFrame/" .. var_2_2, var_2_2, true, function(arg_3_0)
		if IsNil(arg_2_0.tf) then
			return
		end

		if arg_2_0.circle then
			arg_3_0.name = var_2_2
			findTF(arg_3_0.transform, "icon"):GetComponent(typeof(Image)).raycastTarget = false

			setParent(arg_3_0, arg_2_0.circle, false)
		else
			PoolMgr.GetInstance():ReturnPrefab("IconFrame/" .. var_2_2, var_2_2, arg_3_0)
		end
	end)

	local var_2_3 = pg.ship_data_statistics[arg_2_1.player.icon]

	if var_2_3 then
		local var_2_4 = arg_2_1.player:getPainting()

		LoadSpriteAsync("qicon/" .. var_2_4, function(arg_4_0)
			arg_2_0.iconTF.sprite = arg_4_0
		end)

		local var_2_5 = arg_2_0.starsTF.childCount

		for iter_2_0 = var_2_5, var_2_3.star - 1 do
			cloneTplTo(arg_2_0.starTF, arg_2_0.starsTF)
		end

		for iter_2_1 = 1, var_2_5 do
			local var_2_6 = arg_2_0.starsTF:GetChild(iter_2_1 - 1)

			setActive(var_2_6, iter_2_1 <= var_2_3.star)
		end
	end
end

function var_0_0.Clear(arg_5_0)
	if arg_5_0.circle.childCount > 0 then
		local var_5_0 = arg_5_0.circle:GetChild(0)
		local var_5_1 = var_5_0.gameObject.name

		PoolMgr.GetInstance():ReturnPrefab("IconFrame/" .. var_5_1, var_5_1, var_5_0.gameObject)
	end
end

function var_0_0.Dispose(arg_6_0)
	arg_6_0:Clear()
end

return var_0_0
