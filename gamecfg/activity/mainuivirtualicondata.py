return {
	CurrentIconList = {
		1
	},
	{
		Image = "doa_virtual_buff",
		IsVirtualIcon = True,
		def CheckExist:()
			local var_1_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.DOA_PT_ID)

			if not var_1_0:
				return False

			local var_1_1 = ActivityPtData.New(var_1_0)

			if not var_1_0.isEnd() and var_1_1.isInBuffTime():
				return True

			return False
	}
}
