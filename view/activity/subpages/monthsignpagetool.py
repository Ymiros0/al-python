local var_0_0 = class("MonthSignPageTool")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._event = arg_1_1

def var_0_0.onAcheve(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0

	local function var_2_1()
		if var_2_0 and coroutine.status(var_2_0) == "suspended":
			local var_3_0, var_3_1 = coroutine.resume(var_2_0)

			assert(var_3_0, var_3_1)

	var_2_0 = coroutine.create(function()
		if table.getCount(arg_2_1) > 0:
			local var_4_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MONTH_SIGN_ACTIVITY_ID)
			local var_4_1 = pg.activity_month_sign[var_4_0.data2].resign_count
			local var_4_2 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_4_3 = pg.TimeMgr.GetInstance().STimeDescS(var_4_2, "*t")

			if var_4_0.getSpecialData("reMonthSignDay") != None:
				arg_2_0.reMonthSignItems = arg_2_0.reMonthSignItems and arg_2_0.reMonthSignItems or {}

				for iter_4_0, iter_4_1 in pairs(arg_2_1):
					table.insert(arg_2_0.reMonthSignItems, iter_4_1)

				if var_4_3.day > #var_4_0.data1_list and var_4_1 > var_4_0.data3:
					Timer.New(function()
						arg_2_2(), 0.3, 1).Start()

					return
				else
					arg_2_0._event.emit(MonthSignPage.SHOW_RE_MONTH_SIGN, arg_2_0.reMonthSignItems, var_2_1)

					arg_2_1 = arg_2_0.reMonthSignItems
			else
				arg_2_0.reMonthSignItems = None

				arg_2_0._event.emit(BaseUI.ON_AWARD, {
					items = arg_2_1,
					removeFunc = var_2_1
				})

			coroutine.yield()

			local var_4_4 = #_.filter(arg_2_1, function(arg_6_0)
				return arg_6_0.type == DROP_TYPE_SHIP)
			local var_4_5 = _.filter(arg_2_1, function(arg_7_0)
				return arg_7_0.type == DROP_TYPE_OPERATION)
			local var_4_6 = var_4_4 + #var_4_5
			local var_4_7 = getProxy(BayProxy)
			local var_4_8 = var_4_7.getNewShip(True)

			_.each(var_4_5, function(arg_8_0)
				table.insert(var_4_8, var_4_7.getShipById(arg_8_0.id)))

			if var_4_6 <= (pg.gameset.award_ship_limit and pg.gameset.award_ship_limit.key_value or 20):
				for iter_4_2 = math.max(1, #var_4_8 - var_4_6 + 1), #var_4_8:
					arg_2_0._event.emit(ActivityMediator.OPEN_LAYER, Context.New({
						mediator = NewShipMediator,
						viewComponent = NewShipLayer,
						data = {
							ship = var_4_8[iter_4_2]
						},
						onRemoved = var_2_1
					}))
					coroutine.yield()

			for iter_4_3, iter_4_4 in pairs(arg_2_1):
				if iter_4_4.type == DROP_TYPE_SKIN:
					if pg.ship_skin_template[iter_4_4.id].skin_type == ShipSkin.SKIN_TYPE_REMAKE:
						-- block empty
					elif not getProxy(ShipSkinProxy).hasOldNonLimitSkin(iter_4_4.id):
						arg_2_0._event.emit(ActivityMediator.OPEN_LAYER, Context.New({
							mediator = NewSkinMediator,
							viewComponent = NewSkinLayer,
							data = {
								skinId = iter_4_4.id
							},
							onRemoved = var_2_1
						}))

					coroutine.yield()

		if arg_2_2:
			arg_2_2())

	var_2_1()

return var_0_0
