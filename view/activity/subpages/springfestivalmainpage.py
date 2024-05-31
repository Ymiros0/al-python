local var_0_0 = class("SpringFestivalMainPage", import(".TemplatePage.PreviewTemplatePage"))
local var_0_1 = {
	1,
	2,
	3,
	4,
	8,
	9,
	10,
	14,
	15,
	17,
	18,
	19
}
local var_0_2 = 1
local var_0_3 = 3.5

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.rtPrint = arg_1_0._tf.Find("AD/print")
	arg_1_0.prints = {
		arg_1_0.rtPrint.Find("front"),
		arg_1_0.rtPrint.Find("back")
	}

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, arg_2_0.btnList.Find("mountain"), function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SPRING_FESTIVAL_BACKHILL_2023), SFX_PANEL)

	arg_2_0.printCount = 0

	setImageAlpha(arg_2_0.prints[1], 0)
	setImageAlpha(arg_2_0.prints[2], 0)

def var_0_0.OnUpdateFlush(arg_4_0):
	if arg_4_0.LT:
		for iter_4_0, iter_4_1 in ipairs(arg_4_0.LT):
			LeanTween.resume(iter_4_1)
	else
		arg_4_0.tempImg = None

		local var_4_0 = True
		local var_4_1

		local function var_4_2()
			arg_4_0.LT = {}

			parallelAsync({
				function(arg_6_0)
					arg_4_0.printCount = arg_4_0.printCount % #var_0_1 + 1

					LoadSpriteAtlasAsync("clutter/springfestivalmainpage_" .. var_0_1[arg_4_0.printCount], None, function(arg_7_0)
						if IsNil(arg_4_0.rtPrint):
							return
						else
							arg_4_0.tempImg = arg_7_0

							arg_6_0()),
				function(arg_8_0)
					table.insert(arg_4_0.LT, LeanTween.alpha(arg_4_0.prints[1], 0, var_0_2).setOnComplete(System.Action(arg_8_0)).setDelay(var_4_0 and 0 or var_0_3).uniqueId),
				function(arg_9_0)
					table.insert(arg_4_0.LT, LeanTween.alpha(arg_4_0.prints[2], 1, var_0_2).setOnComplete(System.Action(arg_9_0)).setDelay(var_4_0 and 0 or var_0_3).uniqueId)
			}, function()
				var_4_0 = False
				arg_4_0.prints[2], arg_4_0.prints[1] = arg_4_0.prints[1], arg_4_0.prints[2]

				setImageSprite(arg_4_0.prints[2], arg_4_0.tempImg, True)
				var_4_2())

		seriesAsync({
			function(arg_11_0)
				arg_4_0.printCount = arg_4_0.printCount % #var_0_1 + 1

				LoadSpriteAtlasAsync("clutter/springfestivalmainpage_" .. var_0_1[arg_4_0.printCount], None, function(arg_12_0)
					if IsNil(arg_4_0.rtPrint):
						return
					else
						setImageSprite(arg_4_0.prints[2], arg_12_0, True)
						arg_11_0())
		}, var_4_2)

def var_0_0.OnHideFlush(arg_13_0):
	if arg_13_0.LT:
		for iter_13_0, iter_13_1 in ipairs(arg_13_0.LT):
			LeanTween.pause(iter_13_1)

def var_0_0.OnDestroy(arg_14_0):
	if arg_14_0.LT:
		for iter_14_0, iter_14_1 in ipairs(arg_14_0.LT):
			LeanTween.cancel(iter_14_1)

return var_0_0
