local var_0_0 = class("InstagramCard")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.view = arg_1_2
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0.iconTF = arg_1_0._tf.Find("head/icon")
	arg_1_0.nameTxt = arg_1_0._tf.Find("name")
	arg_1_0.txt = arg_1_0._tf.Find("Text")
	arg_1_0.like = arg_1_0._tf.Find("like/Text")
	arg_1_0.tip = arg_1_0._tf.Find("head/tip")
	arg_1_0.image = arg_1_0._tf.Find("image").GetComponent(typeof(RawImage))
	arg_1_0.loading = False
	arg_1_0.needRefresh = False

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.instagram = arg_2_1
	arg_2_2 = defaultValue(arg_2_2, True)

	setImageSprite(arg_2_0.iconTF, LoadSprite("qicon/" .. arg_2_1.GetIcon()), False)
	setText(arg_2_0.nameTxt, arg_2_1.GetName())
	arg_2_0.LoadImage()
	setText(arg_2_0.txt, arg_2_1.GetContent())
	setText(arg_2_0.like, arg_2_1.GetLikeCnt())
	arg_2_0.RemoveTimer()

	if arg_2_2:
		arg_2_0.AddCommentTimer(arg_2_1)

	setActive(arg_2_0.tip, arg_2_1.ShouldShowTip())

def var_0_0.LoadImage(arg_3_0):
	if arg_3_0.loading:
		arg_3_0.needRefresh = True

		return

	arg_3_0.loading = True

	arg_3_0.view.SetImageByUrl(arg_3_0.instagram.GetImage(), arg_3_0.image, function()
		arg_3_0.loading = False

		if arg_3_0.needRefresh:
			arg_3_0.needRefresh = False

			arg_3_0.LoadImage())

def var_0_0.AddCommentTimer(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.GetFastestRefreshTime()

	if var_5_0:
		local var_5_1 = var_5_0 - pg.TimeMgr.GetInstance().GetServerTime()

		if var_5_1 <= 0:
			arg_5_0.view.emit(InstagramMediator.ON_COMMENT_LIST_UPDATE, arg_5_1.id)
		else
			arg_5_0.timer = Timer.New(function()
				arg_5_0.view.emit(InstagramMediator.ON_COMMENT_LIST_UPDATE, arg_5_1.id), var_5_1, 1)

			arg_5_0.timer.Start()

def var_0_0.RemoveTimer(arg_7_0):
	if arg_7_0.timer:
		arg_7_0.timer.Stop()

		arg_7_0.timer = None

def var_0_0.Dispose(arg_8_0):
	arg_8_0.RemoveTimer()

	arg_8_0.loading = False
	arg_8_0.needRefresh = False

return var_0_0
