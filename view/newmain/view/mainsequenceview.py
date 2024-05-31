local var_0_0 = class("MainSequenceView")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.sequence = {
		MainRefundSequence.New(),
		MainForcePlayerNameModificationSequence.New(),
		MainRequestVoteInfoSequence.New(),
		MainStroySequence.New(),
		MainRequestActDataSequence.New(),
		MainUrShipReFetchSequence.New(),
		MainUrgencySceneSequence.New(),
		MainEquipmentChangeSequence.New(),
		MainServerNoticeSequence.New(),
		MainSublayerSequence.New(),
		MainChapterTimeUpSequence.New(),
		MainTechnologySequence.New(),
		MainSubmitTaskSequence.New(),
		MainRemoveNpcSequence.New(),
		MainReplaceFoodSequence.New(),
		MainOverDueEquipmentSequence.New(),
		MainOverDueAttireSequence.New(),
		MainOverDueSkinSequence.New(),
		MainGuildSequence.New(),
		MainMonthCardSequence.New(),
		MainMetaSkillSequence.New(),
		MainCrusingActSequence.New(),
		MainReceiveBossRushAwardsSequence.New(),
		MainNotificationWindowSequence.New(),
		MainRequestFeastActDataSequence.New(),
		MainActDataExpirationReminderSequence.New(),
		MainCalcHxSequence.New(),
		MainGuideSequence.New(),
		MainOpenSystemSequence.New()
	}

def var_0_0.MapSequence(arg_2_0, arg_2_1):
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1):
		table.insert(var_2_0, function(arg_3_0)
			if arg_2_0._exited:
				return

			iter_2_1.Execute(arg_3_0))

	return var_2_0

def var_0_0.Execute(arg_4_0, arg_4_1):
	if not pg.SeriesGuideMgr.GetInstance().isEnd():
		arg_4_1()

		return

	if not arg_4_0.executable:
		arg_4_0.executable = arg_4_0.MapSequence(arg_4_0.sequence)

	seriesAsync(arg_4_0.executable, arg_4_1)

def var_0_0.Disable(arg_5_0):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.sequence):
		if iter_5_1.Clear != None:
			iter_5_1.Clear()

def var_0_0.Dispose(arg_6_0):
	arg_6_0._exited = True

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.sequence):
		if iter_6_1.Dispose != None:
			iter_6_1.Dispose()

	arg_6_0.sequence = None
	arg_6_0.executable = None

return var_0_0
