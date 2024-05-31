pg = pg or {}
pg.DynamicBgMgr = singletonClass("DynamicBgMgr")

local var_0_0 = pg.DynamicBgMgr

function var_0_0.Ctor(arg_1_0)
	arg_1_0.cache = {}
end

function var_0_0.LoadBg(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, arg_2_6)
	local var_2_0 = "bg/star_level_bg_" .. arg_2_2
	local var_2_1 = "ui/star_level_bg_" .. arg_2_2

	if checkABExist(var_2_1) then
		arg_2_0:ClearBg(arg_2_1:getUIName())
		PoolMgr.GetInstance():GetPrefab(var_2_1, "", true, function(arg_3_0)
			if not arg_2_1.exited then
				setParent(arg_3_0, arg_2_3, false)

				local var_3_0 = arg_3_0:GetComponent(typeof(CriManaEffectUI))

				if var_3_0 then
					var_3_0.renderMode = ReflectionHelp.RefGetField(typeof("CriManaMovieMaterial+RenderMode"), "Always", nil)

					var_3_0:Pause(false)
				end

				setActive(arg_2_4, false)

				if arg_2_5 ~= nil then
					arg_2_5(arg_3_0)
				end

				arg_2_0:InsertCache(arg_2_1:getUIName(), arg_2_2, arg_3_0)
			else
				PoolMgr.GetInstance():DestroyPrefab(var_2_1, "")
			end
		end, 1)
	else
		arg_2_0:ClearBg(arg_2_1:getUIName())
		GetSpriteFromAtlasAsync(var_2_0, "", function(arg_4_0)
			if not arg_2_1.exited then
				setImageSprite(arg_2_4, arg_4_0)
				setActive(arg_2_4, true)

				if arg_2_6 ~= nil then
					arg_2_6(arg_4_0)
				end
			else
				PoolMgr.GetInstance():DestroySprite(var_2_0)
			end
		end)
	end
end

function var_0_0.ClearBg(arg_5_0, arg_5_1)
	for iter_5_0 = #arg_5_0.cache, 1, -1 do
		local var_5_0 = arg_5_0.cache[iter_5_0]

		if var_5_0.uiName == arg_5_1 then
			local var_5_1 = "ui/star_level_bg_" .. var_5_0.bgName
			local var_5_2 = var_5_0.dyBg

			if IsNil(var_5_2) then
				table.remove(arg_5_0.cache, iter_5_0)

				return
			end

			local var_5_3 = var_5_2:GetComponent(typeof(CriManaEffectUI))

			if var_5_3 then
				var_5_3:Pause(true)
			end

			PoolMgr.GetInstance():ReturnPrefab(var_5_1, "", var_5_2)

			if #arg_5_0.cache > 1 then
				PoolMgr.GetInstance():DestroyPrefab(var_5_1, "")
			end

			table.remove(arg_5_0.cache, iter_5_0)
		end
	end
end

function var_0_0.InsertCache(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.cache) do
		if iter_6_1.uiName == arg_6_1 and iter_6_1.bgName == arg_6_2 then
			iter_6_1.dyBg = arg_6_3

			return
		end
	end

	table.insert(arg_6_0.cache, {
		uiName = arg_6_1,
		bgName = arg_6_2,
		dyBg = arg_6_3
	})
end
