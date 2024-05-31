local var_0_0 = class("ChapterBoxAction", import(".ChapterCommonAction"))

function var_0_0.applyTo(arg_1_0, arg_1_1, arg_1_2)
	if arg_1_2 then
		return true
	end

	arg_1_0.command.chapter = arg_1_1

	arg_1_0.command:doOpenBox()

	return var_0_0.super.applyTo(arg_1_0, arg_1_1, arg_1_2)
end

function var_0_0.PlayAIAction(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = arg_2_1.fleet.line
	local var_2_1 = arg_2_1:getChapterCell(var_2_0.row, var_2_0.column)
	local var_2_2 = pg.box_data_template[var_2_1.attachmentId]

	seriesAsync({
		function(arg_3_0)
			if var_2_2.type == ChapterConst.BoxAirStrike then
				arg_2_2.viewComponent:doPlayAirStrike(ChapterConst.SubjectChampion, false, arg_3_0)

				return
			elseif var_2_2.type == ChapterConst.BoxTorpedo then
				if arg_2_1.fleet:canClearTorpedo() then
					pg.TipsMgr.GetInstance():ShowTips(i18n("levelScene_destroy_torpedo"))
				else
					arg_2_2.viewComponent:doPlayTorpedo(arg_3_0)

					return
				end
			elseif var_2_2.type == ChapterConst.BoxBanaiDamage then
				arg_2_2.viewComponent:doPlayAirStrike(ChapterConst.SubjectChampion, false, arg_3_0)

				return
			elseif var_2_2.type == ChapterConst.BoxLavaDamage then
				pg.CriMgr.GetInstance():PlaySE_V3("ui-magma")
				arg_2_2.viewComponent:doPlayAnim("AirStrikeLava", function(arg_4_0)
					setActive(arg_4_0, false)
					arg_3_0()
				end)

				return
			end

			arg_3_0()
		end,
		arg_2_3
	})
end

return var_0_0
