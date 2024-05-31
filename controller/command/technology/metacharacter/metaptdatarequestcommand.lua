local var_0_0 = class("MetaPTDataRequestCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = getProxy(MetaCharacterProxy)
	local var_1_1 = arg_1_1:getBody()
	local var_1_2 = {}

	if var_1_1.isAll then
		local var_1_3 = var_1_0:getMetaProgressVOList()

		for iter_1_0, iter_1_1 in ipairs(var_1_3) do
			if iter_1_1:isPtType() and (iter_1_1:isInAct() or iter_1_1:isInArchive()) then
				table.insert(var_1_2, iter_1_1.id)
			end
		end
	end

	print("34001 meta pt request:", table.concat(var_1_2, ","))
	pg.ConnectionMgr.GetInstance():Send(34001, {
		group_id = var_1_2
	}, 34002, function(arg_2_0)
		print("34002 meta pt request done:", #var_1_2)
		var_1_0:setAllProgressPTData(arg_2_0.meta_ship_list)
	end)
end

return var_0_0
