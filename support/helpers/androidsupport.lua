﻿PERMISSION_GRANTED = "permission_granted"
PERMISSION_NEVER_REMIND = "permission_never_remind"
PERMISSION_REJECT = "permission_reject"
ANDROID_CAMERA_PERMISSION = "android.permission.CAMERA"
ANDROID_RECORD_AUDIO_PERMISSION = "android.permission.RECORD_AUDIO"
ANDROID_WRITE_EXTERNAL_PERMISSION = "android.permission.WRITE_EXTERNAL_STORAGE"

function CheckPermissionGranted(arg_1_0)
	return PermissionMgr.Inst:CheckPermissionGranted(arg_1_0)
end

function ApplyPermission(arg_2_0)
	PermissionMgr.Inst:ApplyPermission(arg_2_0)
end

function OpenDetailSetting()
	PermissionMgr.Inst:OpenDetailSetting()
end

function OnPermissionRequestResult(arg_4_0)
	pg.m02:sendNotification(PERMISSION_GRANTED, arg_4_0)
end

function OnPermissionNeverRemind(arg_5_0)
	pg.m02:sendNotification(PERMISSION_NEVER_REMIND, arg_5_0)
end

function OnPermissionReject(arg_6_0)
	pg.m02:sendNotification(PERMISSION_REJECT, arg_6_0)
end
