import ui
import console

def push_btn11(sender):
	push_btn(sender,11)

def push_btn12(sender):
	push_btn(sender,12)
	
def push_btn13(sender):
	push_btn(sender,13)
	
def push_btn14(sender):
	push_btn(sender,14)
	
def push_btn15(sender):
	push_btn(sender,15)
	
def push_btn16(sender):
	push_btn(sender,16)
	
def push_btn17(sender):
	push_btn(sender,17)
	
def push_btn18(sender):
	push_btn(sender,18)
	
def push_btn21(sender):
	push_btn(sender,21)
	
def push_btn22(sender):
	push_btn(sender,22)
	
def push_btn23(sender):
	push_btn(sender,23)
	
def push_btn24(sender):
	push_btn(sender,24)
	
def push_btn25(sender):
	push_btn(sender,25)
	
def push_btn26(sender):
	push_btn(sender,26)
	
def push_btn27(sender):
	push_btn(sender,27)
	
def push_btn28(sender):
	push_btn(sender,28)
	
def push_btn31(sender):
	push_btn(sender,31)
	
def push_btn32(sender):
	push_btn(sender,32)
	
def push_btn33(sender):
	push_btn(sender,33)
	
def push_btn34(sender):
	push_btn(sender,34)
	
def push_btn35(sender):
	push_btn(sender,35)
	
def push_btn36(sender):
	push_btn(sender,36)
	
def push_btn37(sender):
	push_btn(sender,37)
	
def push_btn38(sender):
	push_btn(sender,38)
	
def push_btn41(sender):
	push_btn(sender,41)
	
def push_btn42(sender):
	push_btn(sender,42)
	
def push_btn43(sender):
	push_btn(sender,43)
	
def push_btn44(sender):
	push_btn(sender,44)
	
def push_btn45(sender):
	push_btn(sender,45)
	
def push_btn46(sender):
	push_btn(sender,46)
	
def push_btn47(sender):
	push_btn(sender,47)
		
def push_btn48(sender):
	push_btn(sender,48)
		
def push_btn51(sender):
	push_btn(sender,51)	
	
def push_btn52(sender):
	push_btn(sender,52)
			
def push_btn53(sender):
	push_btn(sender,53)

def push_btn54(sender):
	push_btn(sender,54)

def push_btn55(sender):
	push_btn(sender,55)

def push_btn56(sender):
	push_btn(sender,56)

def push_btn57(sender):
	push_btn(sender,57)

def push_btn58(sender):
	push_btn(sender,58)
	
def push_btn61(sender):
	push_btn(sender,61)
	
def push_btn62(sender):
	push_btn(sender,62)

def push_btn63(sender):
	push_btn(sender,63)

def push_btn64(sender):
	push_btn(sender,64)
	
def push_btn65(sender):
	push_btn(sender,65)

def push_btn66(sender):
	push_btn(sender,66)
		
def push_btn67(sender):
	push_btn(sender,67)	
	
def push_btn68(sender):
	push_btn(sender,68)

def push_btn71(sender):
	push_btn(sender,71)

def push_btn72(sender):
	push_btn(sender,72)

def push_btn73(sender):
	push_btn(sender,73)

def push_btn74(sender):
	push_btn(sender,74)

def push_btn75(sender):
	push_btn(sender,75)	

def push_btn76(sender):
	push_btn(sender,76)
		
def push_btn77(sender):
	push_btn(sender,77)

def push_btn78(sender):
	push_btn(sender,78)

def push_btn81(sender):
	push_btn(sender,81)

def push_btn82(sender):
	push_btn(sender,82)

def push_btn83(sender):
	push_btn(sender,83)

def push_btn84(sender):
	push_btn(sender,84)

def push_btn85(sender):
	push_btn(sender,85)

def push_btn86(sender):
	push_btn(sender,86)

def push_btn87(sender):
	push_btn(sender,87)

def push_btn88(sender):
	push_btn(sender,88)

def push_btn0(sender):
	if sender.title == '⚪️':
		sender.title = '⚫️'
	else:
		sender.title = '⚪️'

def check_all(sender, p, mystone):
	#左上(stone1)/
	stone1 = cb1(sender, p, mystone)
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#右上　(stone3)
	stone3 = cb3(sender, p, mystone)
	#左　(stone4)
	stone4 = cb4(sender, p, mystone)
	#右　(stone5)
	stone5 = cb5(sender, p, mystone)
	#左下　(stone6)
	stone6 = cb6(sender, p, mystone)
	#下　(stone7)
	stone7 = cb7(sender, p, mystone)
	#右下　(stone8)
	stone8 = cb8(sender, p, mystone)
	#check0_listにチェック内容をリスト型で代入
	check0_list = [stone1, stone2, stone3, stone4, stone5, stone6, stone7, stone8]
	return check0_list

def check_234(sender, p, mystone):
		#左　(stone4)
	stone4 = cb4(sender, p, mystone)
	#右　(stone5)
	stone5 = cb5(sender, p, mystone)
	#左下　(stone6)
	stone6 = cb6(sender, p, mystone)
	#下　(stone7)
	stone7 = cb7(sender, p, mystone)
	#右下　(stone8)
	stone8 = cb8(sender, p, mystone)
	check0_list = [stone4, stone5, stone6, stone7, stone8]
	return check0_list

def check_134(sender, p, mystone):
	#左上(stone1)
	stone1 = cb1(sender, p, mystone)
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#左　(stone4)
	stone4 = cb4(sender, p, mystone)
	#左下　(stone6)
	stone6 = cb6(sender, p, mystone)
	#下　(stone7)
	stone7 = cb7(sender, p, mystone)
	check0_list = [stone1, stone2, stone4, stone6, stone7]
	return check0_list

def check_124(sender, p, mystone):
	#左上(stone1)
	stone1 = cb1(sender, p, mystone)
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#右上　(stone3)
	stone3 = cb3(sender, p, mystone)
	#左　(stone4)
	stone4 = cb4(sender, p, mystone)
	#右　(stone5)
	stone5 = cb5(sender, p, mystone)
	check0_list = [stone1, stone2, stone3, stone4, stone5]
	return check0_list
	
def check_123(sender, p, mystone):
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#右上　(stone3)
	stone3 = cb3(sender, p, mystone)
	#右　(stone5)
	stone5 = cb5(sender, p, mystone)
	#下　(stone7)
	stone7 = cb7(sender, p, mystone)
	#右下　(stone8)
	stone8 = cb8(sender, p, mystone)
	check0_list = [stone2, stone3, stone5, stone7, stone8]
	return check0_list
	
def check_23(sender, p, mystone):
	#右(stone5)
	stone5 = cb5(sender, p, mystone)
	#下(stone7)
	stone7 = cb7(sender, p, mystone)
	#右下(stone8)
	stone8 = cb8(sender, p, mystone)
	check0_list = [stone5, stone7, stone8 ]
	return check0_list

def check_34(sender, p, mystone):
	#左(stone5)
	stone4 = cb4(sender, p, mystone)
	#左下(stone6)
	stone6 = cb6(sender, p, mystone)
	#下(stone7)
	stone7 = cb7(sender, p, mystone)
	check0_list = [stone4, stone6, stone7]
	return check0_list
	
def check_12(sender, p, mystone):
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#右上(stone3)
	stone3 = cb3(sender, p, mystone)
	#右(stone5)
	stone5 = cb5(sender, p, mystone)
	check0_list = [stone2, stone3, stone5]
	return check0_list
	
def check_14(sender, p, mystone):
	#左上(stone1)
	stone1 = cb1(sender, p, mystone)
	#上(stone2)
	stone2 = cb2(sender, p, mystone)
	#左(stone4)
	stone4 = cb4(sender, p, mystone)
	check0_list = [stone1, stone2, stone4]
	return check0_list
#_____________チェックをメソッド化_______________
def cb1(sender, p, mystone):
	#左上(stone1)
	p = p - 11
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone1 = 1
	elif btn_cb.title == '':
		stone1 = 2 
	else:
		stone1 = 0
	return stone1
def cb2(sender, p, mystone):
	#上(stone2)
	p = p - 10
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone2 = 1
	elif btn_cb.title == '':
		stone2 = 2
	else:
		stone2 = 0
	return  stone2
def cb3(sender, p, mystone):
	#右上　(stone3)
	p = p - 9
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone3 = 1
	elif btn_cb.title == '':
		stone3 = 2
	else:
		stone3 = 0
	return  stone3
def cb4(sender, p, mystone):
	#左　(stone4)
	p = p - 1
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone4 = 1
	elif btn_cb.title == '':
		stone4 = 2
	else:
		stone4 = 0
	return  stone4
def cb5(sender, p, mystone):
	#右　(stone5)
	p = p + 1
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone5 = 1
	elif btn_cb.title == '':
		stone5 = 2
	else:
		stone5 = 0
	return  stone5
def cb6(sender, p, mystone):
	#左下　(stone6)
	p = p + 9
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone6 = 1
	elif btn_cb.title == '':
		stone6 = 2
	else:
		stone6 = 0
	return stone6
def cb7(sender, p, mystone):
	#下　(stone7)
	p = p + 10
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone7 = 1
	elif btn_cb.title == '':
		stone7 = 2
	else:
		stone7 = 0
	return stone7
def cb8(sender, p, mystone):
	#右下　(stone8)
	p = p + 11
	checkbtn = 'btn{}'.format(p)
	btn_cb = sender.superview[checkbtn]
	if btn_cb.title == mystone:
		stone8 = 1
	elif btn_cb.title == '':
		stone8 = 2
	else:
		stone8 = 0
	return stone8
	
def wall_0(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	cn3list = [0]
	cn4list = [0]
	cn5list = [0]
	cn6list = [0]
	cn7list = [0]
	if clist[0] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn0list = cn0(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn1(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn2(sender, p, mystone, clist, cn2list)
		
	if clist[3] == 0:
#チェックリストの3番目がmystoneじゃない色の石ならば
		cn3list = cn3(sender, p, mystone, clist, cn3list)

	if clist[4] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn4list = cn4(sender, p, mystone, clist, cn4list)
			
	if clist[5] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn5list = cn5(sender, p, mystone, clist, cn5list)

	if clist[6] == 0:
#チェックリストの6番目がmystoneじゃない色の石ならば
		cn6list = cn6(sender, p, mystone, clist, cn6list)
								
	if clist[7] == 0:
#チェックリストの7番目がmystoneじゃない色の石ならば
		cn7list = cn7(sender, p, mystone, clist, cn7list)	

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if not (len(cn3list) == 1 or len(cn3list) == 0):
		cnlist.append(cn3list)
	if not (len(cn4list) == 1 or len(cn4list) == 0):
		cnlist.append(cn4list)
	if not (len(cn5list) == 1 or len(cn5list) == 0):
		cnlist.append(cn5list)
	if not (len(cn6list) == 1 or len(cn6list) == 0):
		cnlist.append(cn6list)
	if not (len(cn7list) == 1 or len(cn7list) == 0):
		cnlist.append(cn7list)
	if len(cnlist) == 1:
		return 0
	else:
		return cnlist
		
def wall_up(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	cn3list = [0]
	cn4list = [0]
	if clist[0] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn0list = cn3(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn4(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn5(sender, p, mystone, clist, cn2list)
		
	if clist[3] == 0:
#チェックリストの3番目がmystoneじゃない色の石ならば
		cn3list = cn6(sender, p, mystone, clist, cn3list)

	if clist[4] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn4list = cn7(sender, p, mystone, clist, cn4list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if not (len(cn3list) == 1 or len(cn3list) == 0):
		cnlist.append(cn3list)
	if not (len(cn4list) == 1 or len(cn4list) == 0):
		cnlist.append(cn4list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_right(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	cn3list = [0]
	cn4list = [0]
	if clist[0] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn0list = cn0(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn1(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn3(sender, p, mystone, clist, cn2list)
		
	if clist[3] == 0:
#チェックリストの3番目がmystoneじゃない色の石ならば
		cn3list = cn5(sender, p, mystone, clist, cn3list)

	if clist[4] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn4list = cn6(sender, p, mystone, clist, cn4list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if not (len(cn3list) == 1 or len(cn3list) == 0):
		cnlist.append(cn3list)
	if not (len(cn4list) == 1 or len(cn4list) == 0):
		cnlist.append(cn4list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_under(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	cn3list = [0]
	cn4list = [0]
	if clist[0] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn0list = cn0(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn1(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn2(sender, p, mystone, clist, cn2list)
		
	if clist[3] == 0:
#チェックリストの3番目がmystoneじゃない色の石ならば
		cn3list = cn3(sender, p, mystone, clist, cn3list)

	if clist[4] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn4list = cn4(sender, p, mystone, clist, cn4list)
	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if not (len(cn3list) == 1 or len(cn3list) == 0):
		cnlist.append(cn3list)
	if not (len(cn4list) == 1 or len(cn4list) == 0):
		cnlist.append(cn4list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_left(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	cn3list = [0]
	cn4list = [0]
	if clist[0] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn0list = cn1(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn2(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn4(sender, p, mystone, clist, cn2list)
		
	if clist[3] == 0:
#チェックリストの3番目がmystoneじゃない色の石ならば
		cn3list = cn6(sender, p, mystone, clist, cn3list)

	if clist[4] == 0:
#チェックリストの4番目がmystoneじゃない色の石ならば
		cn4list = cn7(sender, p, mystone, clist, cn4list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if not (len(cn3list) == 1 or len(cn3list) == 0):
		cnlist.append(cn3list)
	if not (len(cn4list) == 1 or len(cn4list) == 0):
		cnlist.append(cn4list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist
		
def wall_p11(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	if clist[0] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn0list = cn4(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn6(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn7(sender, p, mystone, clist, cn2list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_p18(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	if clist[0] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn0list = cn3(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn5(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn6(sender, p, mystone, clist, cn2list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_p81(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	if clist[0] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn0list = cn1(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn2(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn4(sender, p, mystone, clist, cn2list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist

def wall_p88(sender, p, mystone, clist):
	cn0list = [0]
	cn1list = [0]
	cn2list = [0]
	if clist[0] == 0:
#チェックリストの0番目がmystoneじゃない色の石ならば
		cn0list = cn0(sender, p, mystone, clist, cn0list)		
	if clist[1] == 0:
#チェックリストの1番目がmystoneじゃない色の石ならば
		cn1list = cn1(sender, p, mystone, clist, cn1list)
	
	if clist[2] == 0:
#チェックリストの2番目がmystoneじゃない色の石ならば
		cn2list = cn3(sender, p, mystone, clist, cn2list)

	cnlist = [0]
	if not (len(cn0list) == 1 or len(cn0list) == 0):
		cnlist.append(cn0list)
	if not (len(cn1list) == 1 or len(cn1list) == 0):
		cnlist.append(cn1list)
	if not (len(cn2list) == 1 or len(cn2list) == 0):
		cnlist.append(cn2list)
	if len(cnlist) == 1:
		#cnlistにの要素数が1ならば
		return 0
	else:
		#cnlistの要素数が1以外であれば
		return cnlist
		
		
#取れる場所チェックをメソッド化する＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

def cn0(sender, p, mystone, clist, cn0list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i - 11
		if not((i <= 18) or ((i-1)%10 == 0)):
#壁に面していなければ
			if cb1(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn0list.append(i)
			elif cb1(sender, i, mystone) == 1:
#mystoneと同じならば
				cn0list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn0list.clear()
		else:
			is_same = 0
			cn0list.clear()
	return cn0list

def cn1(sender, p, mystone, clist, cn1list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i - 10
		if not(i <= 18):
#壁に面していなければ
			if cb2(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn1list.append(i)
			elif cb2(sender, i, mystone) == 1:
#mystoneと同じならば
				cn1list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn1list.clear()
		else:
			is_same = 0
			cn1list.clear()
	return cn1list

def cn2(sender, p, mystone, clist, cn2list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i - 9
		if not((i <= 18) or ((i+2)%10 == 0)):
#壁に面していなければ
			if cb3(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn2list.append(i)
			elif cb3(sender, i, mystone) == 1:
#mystoneと同じならば
				cn2list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn2list.clear()
		else:
			is_same = 0
			cn2list.clear()
	return cn2list

def cn3(sender, p, mystone, clist, cn3list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i - 1
		if not((i-1)%10 == 0):
	#壁に面していなければ
			if cb4(sender, i, mystone) == 0:
	#mystoneじゃない色の石ならば
				cn3list.append(i)
			elif cb4(sender, i, mystone) == 1:
	#mystoneと同じならば
				cn3list.append(i)
				is_same = 0
			else:
	#何も無ければ
				is_same = 0
				cn3list.clear()
		else:
			is_same = 0
			cn3list.clear()
	return cn3list

def cn4(sender, p, mystone, clist, cn4list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i + 1
		if not((i+2)%10 == 0):
#壁に面していなければ
			if cb5(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn4list.append(i)
			elif cb5(sender, i, mystone) == 1:
#mystoneと同じならば
				cn4list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn4list.clear()
		else:
			is_same = 0
			cn4list.clear()
	return cn4list

def cn5(sender, p, mystone, clist, cn5list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i + 9
		if not(((i-1)%10 == 0) or (i >= 81)):
#壁に面していなければ
			if cb6(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn5list.append(i)
			elif cb6(sender, i, mystone) == 1:
#mystoneと同じならば
				cn5list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn5list.clear()
		else:
			is_same = 0
			cn5list.clear()
	return cn5list

def cn6(sender, p, mystone, clist, cn6list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i + 10
		if not(i >= 81):
#壁に面していなければ
			if cb7(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn6list.append(i)
			elif cb7(sender, i, mystone) == 1:
#mystoneと同じならば
				cn6list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn6list.clear()
		else:
			is_same = 0
			cn6list.clear()
	return cn6list

def cn7(sender, p, mystone, clist, cn7list):
	i = int(p)
	is_same = 1
	while is_same == 1:
#is_sameが1であればLOOPする
		i = i + 11
		if not(((i+2)%10 == 0) or(i >= 81)):
#壁に面していなければ
			if cb8(sender, i, mystone) == 0:
#mystoneじゃない色の石ならば
				cn7list.append(i)
			elif cb8(sender, i, mystone) == 1:
#mystoneと同じならば
				cn7list.append(i)
				is_same = 0
			else:
#何も無ければ
				is_same = 0
				cn7list.clear()
		else:
			is_same = 0
			cn7list.clear()
	return cn7list
	
def p_check(sender, p, btn_0, check0_list, check_list):
	#壁に面してない組
	if not((p <= 18) or ((p-1)%10 == 0) or ((p+2)%10 == 0) or(p >= 81)):
		#壁に面してない
		check0_list = check_all(sender, p, btn_0.title)
	else:
		if p <= 18:
		#上が壁
			check_list.append(1)
		if (p+2)%10 == 0:
			#壁が右
			check_list.append(2)
		if p >= 81:
			#壁が下
			check_list.append(3)
		if (p-1)%10 == 0:
			#壁が左
			check_list.append(4)
		if len(check_list) == 1:
			if check_list[0] in {1}:
				#壁が上
				check0_list = check_234(sender, p, btn_0.title)
			if check_list[0] in {2}:
				#壁が右
				check0_list = check_134(sender, p, btn_0.title)
			if check_list[0] in {3}:
				#壁が左
				check0_list = check_124(sender, p, btn_0.title)
			if check_list[0] in {4}:
				#壁が左
				check0_list = check_123(sender, p, btn_0.title)
		else:
			if p == 11:
				#壁が左＆上
				check0_list = check_23(sender, p, btn_0.title)
			elif p == 18:
				#壁が右＆上
				check0_list = check_34(sender, p, btn_0.title)
			elif p == 81:
				#壁が左＆下
				check0_list = check_12(sender, p, btn_0.title)
			elif p == 88:
				#壁が右＆下
				check0_list = check_14(sender, p, btn_0.title)
	return check0_list
	
def push_btn(sender,p):
	btn_0 = sender.superview['btn_0']
	check_list = list()
	check0_list = list()
	if sender.title == '':
#ポジションチェック
		check0_list = p_check(sender, p, btn_0, check0_list, check_list)
#置ける場所であるかのチェック
		if 0 in check0_list:
			if len(check0_list) == 8:
				#かべに面していない石の場合
				result = wall_0(sender, p, btn_0.title, check0_list)
			elif len(check0_list) == 5:
				#1つの壁に面している場合
				if p <= 18:
					#上が壁の場合
					result = wall_up(sender, p, btn_0.title, check0_list)
				if (p-1)%10 == 0:
					#左が壁の場合
					result = wall_left(sender, p, btn_0.title, check0_list)
				if (p+2)%10 == 0:
					#右が壁の場合
					result = wall_right(sender, p, btn_0.title, check0_list)
				if p >= 81:
					#壁が下の場合
					result = wall_under(sender, p, btn_0.title, check0_list)
				
			else:
				#2つの壁に面している場合
				if p == 11:
					result = wall_p11(sender, p, btn_0.title, check0_list)
				if p == 18:
					result = wall_p18(sender, p, btn_0.title, check0_list)
				if p == 81:
					result = wall_p81(sender, p, btn_0.title, check0_list)
				if p == 88:
					result = wall_p88(sender, p, btn_0.title, check0_list)
		else:
			return
		if result == 0:
			return 
		else:
			change_stone = list()
			for i in result:
				if i == 0:
					continue
				for j in i:
					if j == 0:
						continue
					change_stone.append(j)
		
		if not (len(change_stone) == 0):
			sender.title = btn_0.title
			for cstone in change_stone:
				ecs = 'btn{}'.format(cstone)
				ecstone = sender.superview[ecs]
				ecstone.title = btn_0.title
			if btn_0.title == '⚪️':
				btn_0.title = '⚫️'
			else:
				btn_0.title = '⚪️'
	count_w = 0
	count_b = 0
	for i in range(89):
		if i in {0,1,2,3,4,5,6,7,8,9,10,19,20,29,30,39,40,49,50,59,60,69,70,79,80}:
			continue
		else:
			istone = 'btn{}'.format(i)
			istone = sender.superview[istone]
			if istone.title == '⚪️':
				count_w = count_w + 1
			elif istone.title == '⚫️':
				count_b = count_b + 1
			lv1 = sender.superview['lv1']
			lv1.text = '⚪️ ：　{}    ⚫️ ：　{}'.format(count_w, count_b)
		
v = ui.load_view()
v.present('sheet')
