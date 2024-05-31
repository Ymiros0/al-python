local var_0_0 = class("SnapshotSceneMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bind(SnapshotScene.SELECT_CHAR_PANEL, function(arg_2_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = SnapshotSelectCharMediator,
			viewComponent = SnapshotSelectCharLayer
		})))
	arg_1_0.bind(SnapshotScene.SHARE_PANEL, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0.addSubLayers(Context.New({
			mediator = SnapshotShareMediator,
			viewComponent = SnapshotShareLayer,
			data = {
				photoTex = arg_3_1,
				photoData = arg_3_2
			}
		})))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		SnapshotSelectCharMediator.SELECT_CHAR,
		PERMISSION_GRANTED,
		PERMISSION_REJECT,
		PERMISSION_NEVER_REMIND
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == SnapshotSelectCharMediator.SELECT_CHAR:
		if pg.ship_skin_template[var_5_1]:
			local var_5_2 = pg.ship_skin_template[var_5_1].ship_group
			local var_5_3 = getProxy(BayProxy).getGroupPropose(var_5_2)

			arg_5_0.viewComponent.contextData.propose = var_5_3

		arg_5_0.viewComponent.setSkin(var_5_1)
	elif PERMISSION_GRANTED == var_5_0:
		if var_5_1 == ANDROID_RECORD_AUDIO_PERMISSION:
			arg_5_0.viewComponent.changeToTakeVideo()
	elif PERMISSION_REJECT == var_5_0:
		if var_5_1 == ANDROID_RECORD_AUDIO_PERMISSION:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("apply_permission_record_audio_tip3"),
				def onYes:()
					ApplyPermission({
						ANDROID_RECORD_AUDIO_PERMISSION
					})
			})
	elif PERMISSION_NEVER_REMIND and var_5_1 == ANDROID_RECORD_AUDIO_PERMISSION:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("apply_permission_record_audio_tip2"),
			def onYes:()
				OpenDetailSetting()
		})

return var_0_0
