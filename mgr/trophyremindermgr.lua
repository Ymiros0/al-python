pg = pg or {}

local var_0_0 = pg

var_0_0.TrophyReminderMgr = singletonClass("TrophyReminderMgr")

local var_0_1 = var_0_0.TrophyReminderMgr

function var_0_1.Ctor(arg_1_0)
	arg_1_0._go = nil
end

function var_0_1.Init(arg_2_0, arg_2_1)
	print("initializing tip manager...")

	arg_2_0._count = 0
	arg_2_0._tipTable = {}

	PoolMgr.GetInstance():GetUI("TrophyRemindPanel", true, function(arg_3_0)
		arg_2_0._go = arg_3_0

		arg_2_0._go:SetActive(false)

		local var_3_0 = GameObject.Find("Overlay/UIOverlay")

		arg_2_0._go.transform:SetParent(var_3_0.transform, false)

		arg_2_0._tips = arg_2_0._go.transform:Find("trophyRemind")
		arg_2_0._grid = arg_2_0._go.transform:Find("Grid_trophy")

		arg_2_1()
	end)
end

function var_0_1.ShowTips(arg_4_0, arg_4_1)
	var_0_0.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_TIP)
	arg_4_0._go.transform:SetAsLastSibling()
	SetActive(arg_4_0._go, true)

	arg_4_0._count = arg_4_0._count + 1

	local var_4_0 = cloneTplTo(arg_4_0._tips, arg_4_0._grid)
	local var_4_1 = var_0_0.medal_template[arg_4_1]

	LoadImageSpriteAsync("medal/s_" .. var_4_1.icon, var_4_0.transform:Find("content/icon"), true)
	setText(var_4_0.transform:Find("content/name"), var_4_1.name)
	setText(var_4_0.transform:Find("content/label"), i18n("trophy_achieved"))

	local var_4_2 = var_4_0.transform:Find("content")

	var_4_2.localPosition = Vector3(-850, 0, 0)

	;(function(arg_5_0)
		LeanTween.moveX(rtf(var_4_2), -275, 0.5)
		LeanTween.moveX(rtf(var_4_2), -850, 0.5):setDelay(5):setOnComplete(System.Action(function()
			Destroy(arg_5_0)

			arg_4_0._count = arg_4_0._count - 1

			if arg_4_0._count == 0 then
				SetActive(arg_4_0._go, false)
			end
		end))
	end)(var_4_0)
end
