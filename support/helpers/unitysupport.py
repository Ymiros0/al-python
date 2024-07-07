from packages.Vector3 import Vector2, Vector3
from packages.luatable import table, ipairs
from packages.alsupport import math, typeof, defaultValue

from Framework.tolua.system.Timer import Timer, FrameTimer
from Framework.tolua.tolua import Application, Button, Canvas, CanvasGroup, Color, Image, Input, InputField, Material, Object, Outline, RectTransform, ScrollRect, Slider, Text, Toggle #!
from Framework.tolua.unityengine.Time import Time
from const import SFX_PANEL, SLIP_TYPE_HRZ, SLIP_TYPE_VERT
from model.const.SoundEffect import SFX_UI_TAG
from mgr.CriMgr import CriMgr #!
from mgr.ShaderMgr import ShaderMgr #!
from mgr.UIMgr import UIMgr #!
from support.helpers.LuaSupport import IsNil, existCall #!
from support.helpers.M02 import splitByWordEN
from support.object.DelegateInfo import DelegateInfo #!


import LuaHelper #???? Injection
import UILongPressTrigger
import UIToggleEvent
import UnityEngine
import UIUtil
import EventTriggerListener

def tf(arg_1_0):
	return arg_1_0.transform

def go(arg_2_0):
	return tf(arg_2_0).gameObject

def rtf(arg_3_0):
	return arg_3_0.transform

def findGO(arg_4_0, arg_4_1):
	assert(arg_4_0, "object or transform should exist")

	var_4_0 = tf(arg_4_0).Find(arg_4_1)

	return var_4_0 and var_4_0.gameObject

def findTF(arg_5_0, arg_5_1):
	assert arg_5_0, "object or transform should exist " + arg_5_1

	return (tf(arg_5_0).Find(arg_5_1))

def Instantiate(arg_6_0):
	return Object.Instantiate(go(arg_6_0))

instantiate = Instantiate

def Destroy(arg_7_0):
	Object.Destroy(go(arg_7_0))

destroy = Destroy

def SetActive(arg_8_0, arg_8_1):
	LuaHelper.SetActiveForLua(arg_8_0, bool(arg_8_1))

setActive = SetActive

def isActive(arg_9_0):
	return go(arg_9_0).activeSelf

def SetName(arg_10_0, arg_10_1):
	arg_10_0.name = arg_10_1

setName = SetName

def SetParent(arg_11_0, arg_11_1, arg_11_2):
	LuaHelper.SetParentForLua(arg_11_0, arg_11_1, bool(arg_11_2))

setParent = SetParent

def setText(arg_12_0, arg_12_1):
	if not arg_12_1:
		return

	arg_12_0.GetComponent(typeof(Text)).text = str(arg_12_1)

def setTextEN(arg_13_0, arg_13_1):
	if not arg_13_1:
		return

	arg_13_1 = splitByWordEN(arg_13_1, arg_13_0)
	arg_13_0.GetComponent(typeof(Text)).text = str(arg_13_1)

def setBestFitTextEN(arg_14_0, arg_14_1, arg_14_2):
	if not arg_14_1:
		return

	var_14_0 = arg_14_0.GetComponent(typeof(RectTransform))
	var_14_1 = arg_14_0.GetComponent(typeof(Text))
	var_14_2 = arg_14_2 or 20
	var_14_3 = var_14_0.rect.width
	var_14_4 = var_14_0.rect.height

	while var_14_2 > 0:
		var_14_1.fontSize = var_14_2

		var_14_5 = splitByWordEN(arg_14_1, arg_14_0)

		var_14_1.text = str(var_14_5)

		if var_14_3 >= var_14_1.preferredWidth and var_14_4 >= var_14_1.preferredHeight:
			break

		var_14_2 = var_14_2 - 1

def setTextFont(arg_15_0, arg_15_1):
	if not arg_15_1:
		return

	arg_15_0.GetComponent(typeof(Text)).font = arg_15_1

def getText(arg_16_0):
	return arg_16_0.GetComponent(typeof(Text)).text

def setInputText(arg_17_0, arg_17_1):
	if not arg_17_1:
		return

	arg_17_0.GetComponent(typeof(InputField)).text = arg_17_1

def getInputText(arg_18_0):
	return arg_18_0.GetComponent(typeof(InputField)).text

def onInputEndEdit(arg_19_0, arg_19_1, arg_19_2):
	var_19_0 = arg_19_1.GetComponent(typeof(InputField)).onEndEdit

	DelegateInfo.Add(arg_19_0, var_19_0)
	var_19_0.RemoveAllListeners()
	var_19_0.AddListener(arg_19_2)

def activateInputField(arg_20_0):
	arg_20_0.GetComponent(typeof(InputField)).ActivateInputField()

def setButtonText(arg_21_0, arg_21_1, arg_21_2):
	setWidgetText(arg_21_0, arg_21_1, arg_21_2)

def setWidgetText(arg_22_0, arg_22_1, arg_22_2):
	arg_22_2 = arg_22_2 or "Text"
	arg_22_2 = findTF(arg_22_0, arg_22_2)

	setText(arg_22_2, arg_22_1)

def setWidgetTextEN(arg_23_0, arg_23_1, arg_23_2):
	arg_23_2 = arg_23_2 or "Text"
	arg_23_2 = findTF(arg_23_0, arg_23_2)

	setTextEN(arg_23_2, arg_23_1)

var_0_1 = True
var_0_2 = -1

def onButton(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4):
	var_24_0 = GetOrAddComponent(arg_24_1, typeof(Button))

	assert var_24_0, "could not found Button component on " + arg_24_1.name
	assert arg_24_2, "callback should exist"

	var_24_1 = var_24_0.onClick

	DelegateInfo.Add(arg_24_0, var_24_1)
	var_24_1.RemoveAllListeners()
	def _func():
		if var_0_2 == Time.frameCount and Input.touchCount > 1:
			return

		var_0_2 = Time.frameCount

		if arg_24_3 and var_0_1:
			CriMgr.GetInstance().PlaySoundEffect_V3(arg_24_3)

		arg_24_2()
	var_24_1.AddListener(_func)

def removeOnButton(arg_26_0):
	var_26_0 = arg_26_0.GetComponent(typeof(Button))

	if var_26_0 != None:
		var_26_0.onClick.RemoveAllListeners()

def removeAllOnButton(arg_27_0):
	var_27_0 = arg_27_0.GetComponentsInChildren(typeof(Button))

	for iter_27_0 in range(1, var_27_0.Length):
		var_27_1 = var_27_0[iter_27_0 - 1]

		if var_27_1 != None:
			var_27_1.onClick.RemoveAllListeners()

def ClearAllText(arg_28_0):
	var_28_0 = arg_28_0.GetComponentsInChildren(typeof(Text))

	for iter_28_0 in range(1, var_28_0.Length):
		var_28_1 = var_28_0[iter_28_0 - 1]

		if var_28_1 != None:
			var_28_1.text = ""

def onLongPressTrigger(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	var_29_0 = GetOrAddComponent(arg_29_1, typeof(UILongPressTrigger))

	assert var_29_0, "could not found UILongPressTrigger component on " + arg_29_1.name
	assert arg_29_2, "callback should exist"

	var_29_1 = var_29_0.onLongPressed

	DelegateInfo.Add(arg_29_0, var_29_1)
	var_29_1.RemoveAllListeners()
	def _func():
		if arg_29_3:
			CriMgr.GetInstance().PlaySoundEffect_V3(arg_29_3)

		arg_29_2()
	var_29_1.AddListener(_func)

def removeOnLongPressTrigger(arg_31_0):
	var_31_0 = arg_31_0.GetComponent(typeof(UILongPressTrigger))

	if var_31_0 != None:
		var_31_0.onLongPressed.RemoveAllListeners()

def setButtonEnabled(arg_32_0, arg_32_1):
	GetComponent(arg_32_0, typeof(Button)).interactable = arg_32_1

def setToggleEnabled(arg_33_0, arg_33_1):
	GetComponent(arg_33_0, typeof(Toggle)).interactable = arg_33_1

def setSliderEnable(arg_34_0, arg_34_1):
	GetComponent(arg_34_0, typeof(Slider)).interactable = arg_34_1

def triggerButton(arg_35_0):
	var_35_0 = GetComponent(arg_35_0, typeof(Button))

	var_0_1 = False
	var_0_2 = -1

	var_35_0.onClick.Invoke()

	var_0_1 = True

var_0_3 = True

def onToggle(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4):
	var_36_0 = GetComponent(arg_36_1, typeof(Toggle))

	assert arg_36_2, "callback should exist"

	var_36_1 = var_36_0.onValueChanged

	var_36_1.RemoveAllListeners()
	DelegateInfo.Add(arg_36_0, var_36_1)
	def _func(arg_37_0):
		if var_0_3:
			if arg_37_0 and arg_36_3 and var_36_0.isOn == arg_37_0:
				arg_36_3 = SFX_UI_TAG

				CriMgr.GetInstance().PlaySoundEffect_V3(arg_36_3)
			elif not arg_37_0 and arg_36_4:
				CriMgr.GetInstance().PlaySoundEffect_V3(arg_36_4)

		arg_36_2(arg_37_0)
	var_36_1.AddListener(_func)

	var_36_2 = GetComponent(arg_36_1, typeof(UIToggleEvent))

	if not IsNil(var_36_2):
		var_36_2.Rebind()

def removeOnToggle(arg_38_0):
	var_38_0 = GetComponent(arg_38_0, typeof(Toggle))

	if var_38_0 != None:
		var_38_0.onValueChanged.RemoveAllListeners()

def triggerToggle(arg_39_0, arg_39_1):
	var_39_0 = GetComponent(arg_39_0, typeof(Toggle))

	var_0_3 = False
	arg_39_1 = bool(arg_39_1)

	if var_39_0.isOn != arg_39_1:
		var_39_0.isOn = arg_39_1
	else:
		var_39_0.onValueChanged.Invoke(arg_39_1)

	var_0_3 = True

def triggerToggleWithoutNotify(arg_40_0, arg_40_1):
	var_40_0 = GetComponent(arg_40_0, typeof(Toggle))

	var_0_3 = False
	arg_40_1 = bool(arg_40_1)

	LuaHelper.ChangeToggleValueWithoutNotify(var_40_0, arg_40_1)

	var_0_3 = True

def onSlider(arg_41_0, arg_41_1, arg_41_2):
	var_41_0 = GetComponent(arg_41_1, typeof(Slider)).onValueChanged

	assert(arg_41_2, "callback should exist")
	var_41_0.RemoveAllListeners()
	DelegateInfo.Add(arg_41_0, var_41_0)
	var_41_0.AddListener(arg_41_2)

def setSlider(arg_42_0, arg_42_1, arg_42_2, arg_42_3):
	var_42_0 = GetComponent(arg_42_0, typeof(Slider))

	assert(var_42_0, "slider should exist")

	var_42_0.minValue = arg_42_1
	var_42_0.maxValue = arg_42_2
	var_42_0.value = arg_42_3

def eachChild(arg_43_0, arg_43_1):
	var_43_0 = tf(arg_43_0)

	for iter_43_0 in range(var_43_0.childCount - 1, 0, -1):
		arg_43_1(var_43_0.GetChild(iter_43_0))

def removeAllChildren(arg_44_0):
	def _func(arg_45_0):
		tf(arg_45_0).transform.SetParent(None, False)
		Destroy(arg_45_0)
	eachChild(arg_44_0, _func)

def scrollTo(arg_46_0, arg_46_1, arg_46_2):
	Canvas.ForceUpdateCanvases()

	var_46_0 = GetComponent(arg_46_0, typeof(ScrollRect))
	var_46_1 = Vector2(arg_46_1 or var_46_0.normalizedPosition.x, arg_46_2 or var_46_0.normalizedPosition.y)

	def _func():
		if not IsNil(arg_46_0):
			var_46_0.normalizedPosition = var_46_1

			var_46_0.onValueChanged.Invoke(var_46_1)

	onNextTick(_func)

def scrollToBottom(arg_48_0):
	scrollTo(arg_48_0, 0, 0)

def onScroll(arg_49_0, arg_49_1, arg_49_2):
	var_49_0 = GetComponent(arg_49_1, typeof(ScrollRect)).onValueChanged

	assert(arg_49_2, "callback should exist")
	var_49_0.RemoveAllListeners()
	DelegateInfo.Add(arg_49_0, var_49_0)
	var_49_0.AddListener(arg_49_2)

def ClearEventTrigger(arg_50_0):
	arg_50_0.RemovePointClickFunc()
	arg_50_0.RemovePointDownFunc()
	arg_50_0.RemovePointEnterFunc()
	arg_50_0.RemovePointExitFunc()
	arg_50_0.RemovePointUpFunc()
	arg_50_0.RemoveCheckDragFunc()
	arg_50_0.RemoveBeginDragFunc()
	arg_50_0.RemoveDragFunc()
	arg_50_0.RemoveDragEndFunc()
	arg_50_0.RemoveDropFunc()
	arg_50_0.RemoveScrollFunc()
	arg_50_0.RemoveSelectFunc()
	arg_50_0.RemoveUpdateSelectFunc()
	arg_50_0.RemoveMoveFunc()

def ClearLScrollrect(arg_51_0):
	arg_51_0.onStart = None
	arg_51_0.onInitItem = None
	arg_51_0.onUpdateItem = None
	arg_51_0.onReturnItem = None

def GetComponent(arg_52_0, arg_52_1):
	return (arg_52_0.GetComponent(arg_52_1))

def GetOrAddComponent(arg_53_0, arg_53_1): #Uhhhhh
	assert arg_53_0, "objectOrTransform not found. " + debug.traceback()

	var_53_0 = arg_53_1

	if type(arg_53_1) == str:
		assert _G[arg_53_1], arg_53_1 + " not exist in Global"

		var_53_0 = typeof(_G[arg_53_1])

	return LuaHelper.GetOrAddComponentForLua(arg_53_0, var_53_0)

def RemoveComponent(arg_54_0, arg_54_1):
	var_54_0 = arg_54_0.GetComponent(arg_54_1)

	if var_54_0:
		Object.Destroy(var_54_0)

def SetCompomentEnabled(arg_55_0, arg_55_1, arg_55_2):
	var_55_0 = arg_55_0.GetComponent(arg_55_1)

	assert(var_55_0, "compoment not found")

	var_55_0.enabled = bool(arg_55_2)

def GetInChildren(arg_56_0, arg_56_1):
	def var_56_0(arg_57_0, arg_57_1):
		if not arg_57_0:
			return None

		if arg_57_0.name == arg_57_1:
			return arg_57_0

		for iter_57_0 in range(0, arg_57_0.childCount - 1):
			var_57_0 = arg_57_0.GetChild(iter_57_0)

			if arg_57_1 == var_57_0.name:
				return var_57_0

			var_57_1 = var_56_0(var_57_0, arg_57_1)

			if var_57_1:
				return var_57_1

		return None

	return var_56_0(arg_56_0, arg_56_1)

def onNextTick(arg_58_0):
	FrameTimer.New(arg_58_0, 1, 1).Start()

def onDelayTick(arg_59_0, arg_59_1):
	Timer.New(arg_59_0, arg_59_1, 1).Start()

def seriesAsync(arg_60_0, arg_60_1, *args):
	var_60_0 = 0
	var_60_1 = len(arg_60_0)

	def var_60_3(*args):
		var_60_0 += 1

		if var_60_0 <= var_60_1:
			arg_60_0[var_60_0](var_60_3, *args)
		elif var_60_0 == var_60_1 + 1 and arg_60_1:
			arg_60_1(*args)

	var_60_3(*args)

def seriesAsyncExtend(arg_62_0, arg_62_1, *args):

	def var_62_1(*args):
		if len(arg_62_0) > 0:
			table.remove(arg_62_0, 1)(var_62_1, *args)
		elif arg_62_1:
			arg_62_1(*args)

	var_62_1(*args)

def parallelAsync(arg_64_0, arg_64_1):
	var_64_0 = len(arg_64_0)

	def var_64_1():
		var_64_0 = var_64_0 - 1

		if var_64_0 == 0 and arg_64_1:
			arg_64_1()

	if var_64_0 > 0:
		for iter_64_0, iter_64_1 in ipairs(arg_64_0):
			iter_64_1(var_64_1)
	elif arg_64_1:
		arg_64_1()

def limitedParallelAsync(arg_66_0, arg_66_1, arg_66_2):
	var_66_0 = len(arg_66_0)
	var_66_1 = var_66_0

	if var_66_1 == 0:
		arg_66_2()

		return

	var_66_2 = min(arg_66_1, var_66_0)

	def var_66_4():
		var_66_1 = var_66_1 - 1

		if var_66_1 == 0:
			arg_66_2()
		elif var_66_2 + 1 <= var_66_0:
			var_66_2 = var_66_2 + 1

			arg_66_0[var_66_2](var_66_4)

	for iter_66_0 in range(1, var_66_2):
		arg_66_0[iter_66_0](var_66_4)

def waitUntil(arg_68_0, arg_68_1):
	def _func():
		if arg_68_0():
			arg_68_1()
			var_68_0.Stop()

			return

	var_68_0 = FrameTimer(_func, 1, -1)

	var_68_0.Start()

	return var_68_0

def setImageSprite(arg_70_0, arg_70_1, arg_70_2):
	if IsNil(arg_70_0):
		assert(False)

		return

	var_70_0 = GetComponent(arg_70_0, typeof(Image))

	if IsNil(var_70_0):
		return

	var_70_0.sprite = arg_70_1

	if arg_70_2:
		var_70_0.SetNativeSize()

def clearImageSprite(arg_71_0):
	GetComponent(arg_71_0, typeof(Image)).sprite = None

def getImageSprite(arg_72_0):
	var_72_0 = GetComponent(arg_72_0, typeof(Image))

	return var_72_0 and var_72_0.sprite

def tex2sprite(arg_73_0):
	return UnityEngine.Sprite.Create(arg_73_0, UnityEngine.Rect.New(0, 0, arg_73_0.width, arg_73_0.height), Vector2(0.5, 0.5), 100)

def setFillAmount(arg_74_0, arg_74_1):
	GetComponent(arg_74_0, typeof(Image)).fillAmount = arg_74_1

def string2vector3(arg_75_0):
	var_75_0 = str.split(arg_75_0, ",")

	return Vector3(var_75_0[1], var_75_0[2], var_75_0[3])

def getToggleState(arg_76_0):
	return arg_76_0.GetComponent(typeof(Toggle)).isOn

def setLocalPosition(arg_77_0, arg_77_1):
	var_77_0 = tf(arg_77_0).localPosition

	arg_77_1.x = arg_77_1.x or var_77_0.x
	arg_77_1.y = arg_77_1.y or var_77_0.y
	arg_77_1.z = arg_77_1.z or var_77_0.z
	tf(arg_77_0).localPosition = arg_77_1

def setAnchoredPosition(arg_78_0, arg_78_1):
	var_78_0 = rtf(arg_78_0)
	var_78_1 = var_78_0.anchoredPosition

	arg_78_1.x = arg_78_1.x or var_78_1.x
	arg_78_1.y = arg_78_1.y or var_78_1.y
	var_78_0.anchoredPosition = arg_78_1

def setAnchoredPosition3D(arg_79_0, arg_79_1):
	var_79_0 = rtf(arg_79_0)
	var_79_1 = var_79_0.anchoredPosition3D

	arg_79_1.x = arg_79_1.x or var_79_1.x
	arg_79_1.y = arg_79_1.y or var_79_1.y
	arg_79_1.z = arg_79_1.y or var_79_1.z
	var_79_0.anchoredPosition3D = arg_79_1

def getAnchoredPosition(arg_80_0):
	return rtf(arg_80_0).anchoredPosition

def setLocalScale(arg_81_0, arg_81_1):
	var_81_0 = tf(arg_81_0).localScale

	arg_81_1.x = arg_81_1.x or var_81_0.x
	arg_81_1.y = arg_81_1.y or var_81_0.y
	arg_81_1.z = arg_81_1.z or var_81_0.z
	tf(arg_81_0).localScale = arg_81_1

def setLocalRotation(arg_82_0, arg_82_1):
	var_82_0 = tf(arg_82_0).localRotation

	arg_82_1.x = arg_82_1.x or var_82_0.x
	arg_82_1.y = arg_82_1.y or var_82_0.y
	arg_82_1.z = arg_82_1.z or var_82_0.z
	tf(arg_82_0).localRotation = arg_82_1

def setLocalEulerAngles(arg_83_0, arg_83_1):
	var_83_0 = tf(arg_83_0).localEulerAngles

	arg_83_1.x = arg_83_1.x or var_83_0.x
	arg_83_1.y = arg_83_1.y or var_83_0.y
	arg_83_1.z = arg_83_1.z or var_83_0.z
	tf(arg_83_0).localEulerAngles = arg_83_1

def ActivateInputField(arg_84_0):
	GetComponent(arg_84_0, typeof(InputField)).ActivateInputField()

def onInputChanged(arg_85_0, arg_85_1, arg_85_2):
	var_85_0 = GetComponent(arg_85_1, typeof(InputField)).onValueChanged

	var_85_0.RemoveAllListeners()
	DelegateInfo.Add(arg_85_0, var_85_0)
	var_85_0.AddListener(arg_85_2)

def getImageColor(arg_86_0):
	return GetComponent(arg_86_0, typeof(Image)).color

def setImageColor(arg_87_0, arg_87_1):
	GetComponent(arg_87_0, typeof(Image)).color = arg_87_1

def getImageAlpha(arg_88_0):
	return GetComponent(arg_88_0, typeof(Image)).color.a

def setImageAlpha(arg_89_0, arg_89_1):
	var_89_0 = GetComponent(arg_89_0, typeof(Image))
	var_89_1 = var_89_0.color

	var_89_1.a = arg_89_1
	var_89_0.color = var_89_1

def getImageRaycastTarget(arg_90_0):
	return GetComponent(arg_90_0, typeof(Image)).raycastTarget

def setImageRaycastTarget(arg_91_0, arg_91_1):
	GetComponent(arg_91_0, typeof(Image)).raycastTarget = bool(arg_91_1)

def getCanvasGroupAlpha(arg_92_0):
	return GetComponent(arg_92_0, typeof(CanvasGroup)).alpha

def setCanvasGroupAlpha(arg_93_0, arg_93_1):
	GetComponent(arg_93_0, typeof(CanvasGroup)).alpha = arg_93_1

def setActiveViaLayer(arg_94_0, arg_94_1):
	UIUtil.SetUIActiveViaLayer(go(arg_94_0), arg_94_1)

def setActiveViaCG(arg_95_0, arg_95_1):
	UIUtil.SetUIActiveViaCG(go(arg_95_0), arg_95_1)

def getTextColor(arg_96_0):
	return GetComponent(arg_96_0, typeof(Text)).color

def setTextColor(arg_97_0, arg_97_1):
	GetComponent(arg_97_0, typeof(Text)).color = arg_97_1

def getTextAlpha(arg_98_0):
	return GetComponent(arg_98_0, typeof(Text)).color.a

def setTextAlpha(arg_99_0, arg_99_1):
	var_99_0 = GetComponent(arg_99_0, typeof(Text))
	var_99_1 = var_99_0.color

	var_99_1.a = arg_99_1
	var_99_0.color = var_99_1

def setSizeDelta(arg_100_0, arg_100_1):
	var_100_0 = GetComponent(arg_100_0, typeof(RectTransform))

	if not var_100_0:
		return

	var_100_1 = var_100_0.sizeDelta

	var_100_1.x = arg_100_1.x
	var_100_1.y = arg_100_1.y
	var_100_0.sizeDelta = var_100_1

def getOutlineColor(arg_101_0):
	return GetComponent(arg_101_0, typeof(Outline)).effectColor

def setOutlineColor(arg_102_0, arg_102_1):
	GetComponent(arg_102_0, typeof(Outline)).effectColor = arg_102_1

def pressPersistTrigger(arg_103_0, arg_103_1, arg_103_2, arg_103_3, arg_103_4, arg_103_5, arg_103_6, arg_103_7):
	arg_103_6 = defaultValue(arg_103_6, 0.25)

	assert arg_103_6 > 0, "maxSpeed less than zero"
	assert arg_103_0, "should exist objectOrTransform"

	var_103_0 = GetOrAddComponent(arg_103_0, typeof(EventTriggerListener))

	assert arg_103_2, "should exist callback"

	def _func2():
		def _func():
			if arg_103_5:
				var_105_0 = max(var_103_1.duration - arg_103_1 / 10, arg_103_6)

				var_103_1.duration = var_105_0

			existCall(arg_103_2)

		var_103_1 = Timer(_func, arg_103_1, -1)

		if arg_103_4:
			var_103_1.func()

		var_103_1.Start()

		if arg_103_7 and var_0_1:
			CriMgr.GetInstance().PlaySoundEffect_V3(arg_103_7)

	var_103_0.AddPointDownFunc(_func2)
	def _func():
		var_103_1.Stop()

		var_103_1 = None

		if arg_103_3:
			arg_103_3()
	var_103_0.AddPointUpFunc(_func)

	return var_103_0

def getSpritePivot(arg_107_0):
	var_107_0 = arg_107_0.bounds
	var_107_1 = -var_107_0.center.x / var_107_0.extents.x / 2 + 0.5
	var_107_2 = -var_107_0.center.y / var_107_0.extents.y / 2 + 0.5

	return Vector2(var_107_1, var_107_2)

def resetAspectRatio(arg_108_0):
	var_108_0 = GetComponent(arg_108_0, "Image")

	GetComponent(arg_108_0, "AspectRatioFitter").aspectRatio = var_108_0.preferredWidth / var_108_0.preferredHeight

def cloneTplTo(arg_109_0, arg_109_1, arg_109_2):
	var_109_0 = tf(Instantiate(arg_109_0))

	var_109_0.SetParent(tf(arg_109_1), False)
	SetActive(var_109_0, True)

	if arg_109_2:
		var_109_0.name = arg_109_2

	return var_109_0

def setGray(arg_110_0, arg_110_1, arg_110_2):
	if arg_110_1:
		var_110_0 = GetOrAddComponent(arg_110_0, "UIGrayScale")

		var_110_0.Recursive = defaultValue(arg_110_2, True)
		var_110_0.enabled = True
	else:
		RemoveComponent(arg_110_0, "UIGrayScale")

def setBlackMask(arg_111_0, arg_111_1, arg_111_2):
	if arg_111_1:
		arg_111_2 = arg_111_2 or {}

		var_111_0 = GetOrAddComponent(arg_111_0, "UIMaterialAdjuster")

		var_111_0.Recursive = bool(defaultValue(arg_111_2.recursive, True))

		var_111_1 = Material.New(ShaderMgr.GetInstance().GetShader("M02/Unlit Colored_Alpha_UI"))

		var_111_1.SetColor("_Color", arg_111_2.color or Color(0, 0, 0, 0.2))

		var_111_0.adjusterMaterial = var_111_1
		var_111_0.enabled = True
	else:
		RemoveComponent(arg_111_0, "UIMaterialAdjuster")

def blockBlackMask(arg_112_0, arg_112_1, arg_112_2):
	if arg_112_1:
		var_112_0 = GetOrAddComponent(arg_112_0, "UIMaterialAdjuster")

		var_112_0.Recursive = bool(defaultValue(arg_112_2, True))
		var_112_0.enabled = False
	else:
		RemoveComponent(arg_112_0, "UIMaterialAdjuster")

def long2int(arg_113_0):
	var_113_0, var_113_1 = int64.tonum2(arg_113_0) #????

	return var_113_0

def OnSliderWithButton(arg_114_0, arg_114_1, arg_114_2):
	var_114_0 = arg_114_1.GetComponent("Slider")

	var_114_0.onValueChanged.RemoveAllListeners()
	DelegateInfo.Add(arg_114_0, var_114_0.onValueChanged)
	var_114_0.onValueChanged.AddListener(arg_114_2)

	var_114_1 = (var_114_0.maxValue - var_114_0.minValue) * 0.1

	onButton(arg_114_0, arg_114_1.Find("up"), lambda: setattr(var_114_0, 'value', math.clamp(var_114_0.value + var_114_1, var_114_0.minValue, var_114_0.maxValue)), SFX_PANEL)
	onButton(arg_114_0, arg_114_1.Find("down"), lambda: setattr(var_114_0, 'value', math.clamp(var_114_0.value - var_114_1, var_114_0.minValue, var_114_0.maxValue), SFX_PANEL))

def addSlip(arg_117_0, arg_117_1, arg_117_2, arg_117_3, arg_117_4):
	var_117_0 = GetOrAddComponent(arg_117_1, "EventTriggerListener")
	var_117_2 = 0
	var_117_3 = 50

	def _function():
		var_117_2 = 0
		var_117_1 = None

	var_117_0.AddPointDownFunc(_function)

	def _func(arg_119_0, arg_119_1):
		var_119_0 = arg_119_1.position

		if not var_117_1:
			var_117_1 = var_119_0

		if arg_117_0 == SLIP_TYPE_HRZ:
			var_117_2 = var_119_0.x - var_117_1.x
		elif arg_117_0 == SLIP_TYPE_VERT:
			var_117_2 = var_119_0.y - var_117_1.y

	var_117_0.AddDragFunc(_func)

	def _function(arg_120_0, arg_120_1):
		if var_117_2 < -var_117_3:
			if arg_117_3:
				arg_117_3()
		elif var_117_2 > var_117_3:
			if arg_117_2:
				arg_117_2()
		elif arg_117_4:
			arg_117_4()
	var_117_0.AddPointUpFunc(_function)

def getSizeRate():
	var_121_0 = UIMgr.GetInstance().LevelMain.transform.rect
	var_121_1 = UnityEngine.Screen

	return Vector2.New(var_121_0.width / var_121_1.width, var_121_0.height / var_121_1.height), var_121_0.width, var_121_0.height

def IsUsingWifi():
	return Application.internetReachability == UnityEngine.NetworkReachability.ReachableViaLocalAreaNetwork
