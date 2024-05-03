import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
number fp
'''
		expect = '''Program([VarDecl(Id(fp), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
bool Jk9[3.27,19.71,86.55]
func nq2 (number nZ0[51.56,54.84,70.83], string vx68[15.44,3.95])	return fK[true, - kN]

bool hC_
func bY (string XB, number aP[3.7,77.76], bool ZQp[74.43,2.18])
	return
'''
		expect = '''Program([VarDecl(Id(Jk9), ArrayType([3.27, 19.71, 86.55], BoolType), None, None), FuncDecl(Id(nq2), [VarDecl(Id(nZ0), ArrayType([51.56, 54.84, 70.83], NumberType), None, None), VarDecl(Id(vx68), ArrayType([15.44, 3.95], StringType), None, None)], Return(ArrayCell(Id(fK), [BooleanLit(True), UnaryOp(-, Id(kN))]))), VarDecl(Id(hC_), BoolType, None, None), FuncDecl(Id(bY), [VarDecl(Id(XB), StringType, None, None), VarDecl(Id(aP), ArrayType([3.7, 77.76], NumberType), None, None), VarDecl(Id(ZQp), ArrayType([74.43, 2.18], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
func QQGI (bool uUN, string vWI)
	return xh
func C_ (number oX[39.54], bool Tp[23.26,37.84], string KX)	return
'''
		expect = '''Program([FuncDecl(Id(QQGI), [VarDecl(Id(uUN), BoolType, None, None), VarDecl(Id(vWI), StringType, None, None)], Return(Id(xh))), FuncDecl(Id(C_), [VarDecl(Id(oX), ArrayType([39.54], NumberType), None, None), VarDecl(Id(Tp), ArrayType([23.26, 37.84], BoolType), None, None), VarDecl(Id(KX), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
func aTSy (bool fy6V)	return
func ZEr (bool x72)	return
'''
		expect = '''Program([FuncDecl(Id(aTSy), [VarDecl(Id(fy6V), BoolType, None, None)], Return()), FuncDecl(Id(ZEr), [VarDecl(Id(x72), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
string atLy[39.89] <- rZ
string goOw[68.11,0.67] <- true
func wm (string zc)	return "VE"
func HZ5F ()	return true
'''
		expect = '''Program([VarDecl(Id(atLy), ArrayType([39.89], StringType), None, Id(rZ)), VarDecl(Id(goOw), ArrayType([68.11, 0.67], StringType), None, BooleanLit(True)), FuncDecl(Id(wm), [VarDecl(Id(zc), StringType, None, None)], Return(StringLit(VE))), FuncDecl(Id(HZ5F), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
string D1D
func qR_ (string rp[94.58,6.87,15.67], string jD)	return 8.44
func GK (bool E8fM, string y5i, number SUPX)
	begin
		var BM4Y <- ck
		for RlJI until "p" by "JKDX"
			var fn07 <- hCS5
		if ("CMRAp")
		continue
		elif (true) number Qe[16.73,80.32,38.41]
		elif ("TblWG")
		continue
		else Yz[WQKL] <- "Cg"
	end

string Jz_B[11.57,92.48,5.95]
number iS <- 64.09
'''
		expect = '''Program([VarDecl(Id(D1D), StringType, None, None), FuncDecl(Id(qR_), [VarDecl(Id(rp), ArrayType([94.58, 6.87, 15.67], StringType), None, None), VarDecl(Id(jD), StringType, None, None)], Return(NumLit(8.44))), FuncDecl(Id(GK), [VarDecl(Id(E8fM), BoolType, None, None), VarDecl(Id(y5i), StringType, None, None), VarDecl(Id(SUPX), NumberType, None, None)], Block([VarDecl(Id(BM4Y), None, var, Id(ck)), For(Id(RlJI), StringLit(p), StringLit(JKDX), VarDecl(Id(fn07), None, var, Id(hCS5))), If((StringLit(CMRAp), Continue), [(BooleanLit(True), VarDecl(Id(Qe), ArrayType([16.73, 80.32, 38.41], NumberType), None, None)), (StringLit(TblWG), Continue)], AssignStmt(ArrayCell(Id(Yz), [Id(WQKL)]), StringLit(Cg)))])), VarDecl(Id(Jz_B), ArrayType([11.57, 92.48, 5.95], StringType), None, None), VarDecl(Id(iS), NumberType, None, NumLit(64.09))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
number clGI[87.61,4.04,72.2]
func mzZ1 ()	begin
		CS[false, Je] <- true
		continue
		if (58.36) for CIHo until 28.71 by fh
			return
		elif (false) for fDo until 24.91 by 81.47
			for TJ9B until PN by iST
				for fU until bIQ by 81.93
					for QAn until l6 by "Uh"
						continue
		elif ("HUWOo")
		break
		elif (53.5)
		string nb[46.23,26.9] <- true
		else number yrf[17.22,76.65] <- false
	end
bool g4
'''
		expect = '''Program([VarDecl(Id(clGI), ArrayType([87.61, 4.04, 72.2], NumberType), None, None), FuncDecl(Id(mzZ1), [], Block([AssignStmt(ArrayCell(Id(CS), [BooleanLit(False), Id(Je)]), BooleanLit(True)), Continue, If((NumLit(58.36), For(Id(CIHo), NumLit(28.71), Id(fh), Return())), [(BooleanLit(False), For(Id(fDo), NumLit(24.91), NumLit(81.47), For(Id(TJ9B), Id(PN), Id(iST), For(Id(fU), Id(bIQ), NumLit(81.93), For(Id(QAn), Id(l6), StringLit(Uh), Continue))))), (StringLit(HUWOo), Break), (NumLit(53.5), VarDecl(Id(nb), ArrayType([46.23, 26.9], StringType), None, BooleanLit(True)))], VarDecl(Id(yrf), ArrayType([17.22, 76.65], NumberType), None, BooleanLit(False)))])), VarDecl(Id(g4), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
number dso[89.31,24.85] <- M1
func d2ZH (string Ie)
	return

func UJ (bool vEa)	return yn
func pHC (number V6, string WNF4[27.13,47.21])
	return

'''
		expect = '''Program([VarDecl(Id(dso), ArrayType([89.31, 24.85], NumberType), None, Id(M1)), FuncDecl(Id(d2ZH), [VarDecl(Id(Ie), StringType, None, None)], Return()), FuncDecl(Id(UJ), [VarDecl(Id(vEa), BoolType, None, None)], Return(Id(yn))), FuncDecl(Id(pHC), [VarDecl(Id(V6), NumberType, None, None), VarDecl(Id(WNF4), ArrayType([27.13, 47.21], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
func Ek (bool kAF, string vz)	begin
		begin
			gSue[false, 82.38, true] <- z7
			for t_ until "ui" by true
				number bhDc
		end
	end

func uuT (string fB[49.53], number ZY, string Oz)
	return

func dY3X (number wB[31.54])
	begin
	end

func Xe (string rb, string AWJ[97.44,3.62,66.94])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Ek), [VarDecl(Id(kAF), BoolType, None, None), VarDecl(Id(vz), StringType, None, None)], Block([Block([AssignStmt(ArrayCell(Id(gSue), [BooleanLit(False), NumLit(82.38), BooleanLit(True)]), Id(z7)), For(Id(t_), StringLit(ui), BooleanLit(True), VarDecl(Id(bhDc), NumberType, None, None))])])), FuncDecl(Id(uuT), [VarDecl(Id(fB), ArrayType([49.53], StringType), None, None), VarDecl(Id(ZY), NumberType, None, None), VarDecl(Id(Oz), StringType, None, None)], Return()), FuncDecl(Id(dY3X), [VarDecl(Id(wB), ArrayType([31.54], NumberType), None, None)], Block([])), FuncDecl(Id(Xe), [VarDecl(Id(rb), StringType, None, None), VarDecl(Id(AWJ), ArrayType([97.44, 3.62, 66.94], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
bool ESd[17.12,16.32,68.6]
func PX (string M3u, number IfT)	return
'''
		expect = '''Program([VarDecl(Id(ESd), ArrayType([17.12, 16.32, 68.6], BoolType), None, None), FuncDecl(Id(PX), [VarDecl(Id(M3u), StringType, None, None), VarDecl(Id(IfT), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
func ZqB (bool iwRa, number A0)
	return false
bool rg[24.77,18.73,70.6]
string yK7D[3.0,45.27,31.66] <- "OXh"
bool p8_[88.61,51.03,70.54] <- "wjXbC"
bool C0CY[18.98] <- z64
'''
		expect = '''Program([FuncDecl(Id(ZqB), [VarDecl(Id(iwRa), BoolType, None, None), VarDecl(Id(A0), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(rg), ArrayType([24.77, 18.73, 70.6], BoolType), None, None), VarDecl(Id(yK7D), ArrayType([3.0, 45.27, 31.66], StringType), None, StringLit(OXh)), VarDecl(Id(p8_), ArrayType([88.61, 51.03, 70.54], BoolType), None, StringLit(wjXbC)), VarDecl(Id(C0CY), ArrayType([18.98], BoolType), None, Id(z64))])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
number bB[21.07,74.06]
func Ojfw ()
	begin
		continue
		return
		bool qLXf[76.46] <- "mTDd"
	end

'''
		expect = '''Program([VarDecl(Id(bB), ArrayType([21.07, 74.06], NumberType), None, None), FuncDecl(Id(Ojfw), [], Block([Continue, Return(), VarDecl(Id(qLXf), ArrayType([76.46], BoolType), None, StringLit(mTDd))]))])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
number wUS[16.29]
func gQ1 (string P3)	return
number HDu[55.08,57.12,19.97] <- false
func b2w6 ()	begin
		for Nsw until Wx7G by LdV
			continue
		Da8v(76.21)
		begin
			break
			ZSS8()
		end
	end
'''
		expect = '''Program([VarDecl(Id(wUS), ArrayType([16.29], NumberType), None, None), FuncDecl(Id(gQ1), [VarDecl(Id(P3), StringType, None, None)], Return()), VarDecl(Id(HDu), ArrayType([55.08, 57.12, 19.97], NumberType), None, BooleanLit(False)), FuncDecl(Id(b2w6), [], Block([For(Id(Nsw), Id(Wx7G), Id(LdV), Continue), CallStmt(Id(Da8v), [NumLit(76.21)]), Block([Break, CallStmt(Id(ZSS8), [])])]))])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
var RrU <- false
dynamic Upkm
func TUA (number vL)
	return

bool zm[21.33,54.89,37.19]
'''
		expect = '''Program([VarDecl(Id(RrU), None, var, BooleanLit(False)), VarDecl(Id(Upkm), None, dynamic, None), FuncDecl(Id(TUA), [VarDecl(Id(vL), NumberType, None, None)], Return()), VarDecl(Id(zm), ArrayType([21.33, 54.89, 37.19], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
number Wg1
string xVR[30.51]
func YwR ()	begin
		if (false) for WVGG until 6.72 by true
			number ss[19.57,93.85,29.84] <- true
		elif (false)
		for BZha until "no" by Qc9
			dynamic E_c <- 79.04
		elif (HpaA)
		begin
			break
		end
		else if (SU) pPs(false, 72.87)
		elif ("W")
		if ("zofI")
		return 37.87
		elif (i6) return
		elif ("Z") dBs(fE9)
		elif (false)
		continue
		else break
		elif ("VLGmj") return
		elif (80.77)
		gj[1.03] <- "hZsM"
		else break
	end
number uYj
'''
		expect = '''Program([VarDecl(Id(Wg1), NumberType, None, None), VarDecl(Id(xVR), ArrayType([30.51], StringType), None, None), FuncDecl(Id(YwR), [], Block([If((BooleanLit(False), For(Id(WVGG), NumLit(6.72), BooleanLit(True), VarDecl(Id(ss), ArrayType([19.57, 93.85, 29.84], NumberType), None, BooleanLit(True)))), [(BooleanLit(False), For(Id(BZha), StringLit(no), Id(Qc9), VarDecl(Id(E_c), None, dynamic, NumLit(79.04)))), (Id(HpaA), Block([Break]))], If((Id(SU), CallStmt(Id(pPs), [BooleanLit(False), NumLit(72.87)])), [(StringLit(W), If((StringLit(zofI), Return(NumLit(37.87))), [(Id(i6), Return()), (StringLit(Z), CallStmt(Id(dBs), [Id(fE9)])), (BooleanLit(False), Continue)], Break)), (StringLit(VLGmj), Return()), (NumLit(80.77), AssignStmt(ArrayCell(Id(gj), [NumLit(1.03)]), StringLit(hZsM)))], Break))])), VarDecl(Id(uYj), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = '''
var NF <- H4
string IW[3.34] <- mJ
func EQ1Z ()	return

func JUf (number Klg, string Ft[10.43,40.57], bool Emi)
	return aN
'''
		expect = '''Program([VarDecl(Id(NF), None, var, Id(H4)), VarDecl(Id(IW), ArrayType([3.34], StringType), None, Id(mJ)), FuncDecl(Id(EQ1Z), [], Return()), FuncDecl(Id(JUf), [VarDecl(Id(Klg), NumberType, None, None), VarDecl(Id(Ft), ArrayType([10.43, 40.57], StringType), None, None), VarDecl(Id(Emi), BoolType, None, None)], Return(Id(aN)))])'''
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = '''
number bnu[46.85,84.38,49.75]
func KLEV (bool CJFR[75.92,20.99,21.98])
	return
bool ha
'''
		expect = '''Program([VarDecl(Id(bnu), ArrayType([46.85, 84.38, 49.75], NumberType), None, None), FuncDecl(Id(KLEV), [VarDecl(Id(CJFR), ArrayType([75.92, 20.99, 21.98], BoolType), None, None)], Return()), VarDecl(Id(ha), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
bool ADv[52.14] <- 8.46
'''
		expect = '''Program([VarDecl(Id(ADv), ArrayType([52.14], BoolType), None, NumLit(8.46))])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
func yTS (bool GA, string SDlp[24.72], string bju)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(yTS), [VarDecl(Id(GA), BoolType, None, None), VarDecl(Id(SDlp), ArrayType([24.72], StringType), None, None), VarDecl(Id(bju), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
var biA <- Ep
func e9z (number b6vh[8.17], number ie)	begin
		if (60.87)
		number LAW6
		elif (true) if (ZGm)
		string sFw <- false
		elif (false)
		break
		elif ("FNEe")
		wDZ(wV, RfEL)
		elif (27.05) HyP2[gh, false, kX] <- aWDD
		else Vtt <- 17.71
		elif (true) if (true) LS[zC] <- 93.85
		elif (72.94) return "mzNu"
		elif (afAX) number Gb1l[18.89] <- "MqRv"
		elif (EJe) if (49.67) number TS[52.45] <- 87.77
		elif (false) if (true) break
		elif (true)
		break
		else continue
		elif (false)
		UD1(pa, "m", true)
		else continue
		elif (KanZ) bool Arap[61.87,76.27] <- false
		elif (37.45) fv[true] <- oHH
		elif (eLHm)
		begin
			continue
		end
		elif (59.88) lrQ5()
		elif (true) number VSl0[56.44] <- Qu4o
		else continue
		FNK[kg, uA, ZoD] <- true
		return p5X
	end
bool SbG[3.35,37.76]
func hQ47 ()
	begin
		number KoAi <- false
		begin
			continue
		end
		for JF until w4 by "nasE"
			break
	end
'''
		expect = '''Program([VarDecl(Id(biA), None, var, Id(Ep)), FuncDecl(Id(e9z), [VarDecl(Id(b6vh), ArrayType([8.17], NumberType), None, None), VarDecl(Id(ie), NumberType, None, None)], Block([If((NumLit(60.87), VarDecl(Id(LAW6), NumberType, None, None)), [(BooleanLit(True), If((Id(ZGm), VarDecl(Id(sFw), StringType, None, BooleanLit(False))), [(BooleanLit(False), Break), (StringLit(FNEe), CallStmt(Id(wDZ), [Id(wV), Id(RfEL)])), (NumLit(27.05), AssignStmt(ArrayCell(Id(HyP2), [Id(gh), BooleanLit(False), Id(kX)]), Id(aWDD)))], AssignStmt(Id(Vtt), NumLit(17.71)))), (BooleanLit(True), If((BooleanLit(True), AssignStmt(ArrayCell(Id(LS), [Id(zC)]), NumLit(93.85))), [(NumLit(72.94), Return(StringLit(mzNu))), (Id(afAX), VarDecl(Id(Gb1l), ArrayType([18.89], NumberType), None, StringLit(MqRv))), (Id(EJe), If((NumLit(49.67), VarDecl(Id(TS), ArrayType([52.45], NumberType), None, NumLit(87.77))), [(BooleanLit(False), If((BooleanLit(True), Break), [(BooleanLit(True), Break)], Continue)), (BooleanLit(False), CallStmt(Id(UD1), [Id(pa), StringLit(m), BooleanLit(True)]))], Continue)), (Id(KanZ), VarDecl(Id(Arap), ArrayType([61.87, 76.27], BoolType), None, BooleanLit(False))), (NumLit(37.45), AssignStmt(ArrayCell(Id(fv), [BooleanLit(True)]), Id(oHH))), (Id(eLHm), Block([Continue])), (NumLit(59.88), CallStmt(Id(lrQ5), [])), (BooleanLit(True), VarDecl(Id(VSl0), ArrayType([56.44], NumberType), None, Id(Qu4o)))], Continue))], None), AssignStmt(ArrayCell(Id(FNK), [Id(kg), Id(uA), Id(ZoD)]), BooleanLit(True)), Return(Id(p5X))])), VarDecl(Id(SbG), ArrayType([3.35, 37.76], BoolType), None, None), FuncDecl(Id(hQ47), [], Block([VarDecl(Id(KoAi), NumberType, None, BooleanLit(False)), Block([Continue]), For(Id(JF), Id(w4), StringLit(nasE), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
string zdp <- "Gzo"
func tM (number Pf, bool zrz1[67.62,74.08], number J5Z[61.18,88.69,79.24])	return

'''
		expect = '''Program([VarDecl(Id(zdp), StringType, None, StringLit(Gzo)), FuncDecl(Id(tM), [VarDecl(Id(Pf), NumberType, None, None), VarDecl(Id(zrz1), ArrayType([67.62, 74.08], BoolType), None, None), VarDecl(Id(J5Z), ArrayType([61.18, 88.69, 79.24], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''
func tpzI (bool o05[78.49,26.0], string bpt[50.77,56.44])	return 66.71

func n5G ()	return
'''
		expect = '''Program([FuncDecl(Id(tpzI), [VarDecl(Id(o05), ArrayType([78.49, 26.0], BoolType), None, None), VarDecl(Id(bpt), ArrayType([50.77, 56.44], StringType), None, None)], Return(NumLit(66.71))), FuncDecl(Id(n5G), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
bool mDk[95.4,27.81,7.33]
bool jz[5.21] <- 81.61
func MxFb (bool RI, bool qDaM)
	return 96.15

func wqPH (bool rU[92.17,19.53,27.43], string em[32.1])	return gU

var ZQc <- "AlULV"
'''
		expect = '''Program([VarDecl(Id(mDk), ArrayType([95.4, 27.81, 7.33], BoolType), None, None), VarDecl(Id(jz), ArrayType([5.21], BoolType), None, NumLit(81.61)), FuncDecl(Id(MxFb), [VarDecl(Id(RI), BoolType, None, None), VarDecl(Id(qDaM), BoolType, None, None)], Return(NumLit(96.15))), FuncDecl(Id(wqPH), [VarDecl(Id(rU), ArrayType([92.17, 19.53, 27.43], BoolType), None, None), VarDecl(Id(em), ArrayType([32.1], StringType), None, None)], Return(Id(gU))), VarDecl(Id(ZQc), None, var, StringLit(AlULV))])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
func IoN (string Ei, string vT[13.98,38.0,6.85])	begin
		return mESc
		kc(92.43, h_4)
		begin
		end
	end
bool UhnQ <- tF1K
func lN ()
	return

func IGAb (bool fr43)	return 42.69

func pf_ (number aR, bool aO, number h8H)	return

'''
		expect = '''Program([FuncDecl(Id(IoN), [VarDecl(Id(Ei), StringType, None, None), VarDecl(Id(vT), ArrayType([13.98, 38.0, 6.85], StringType), None, None)], Block([Return(Id(mESc)), CallStmt(Id(kc), [NumLit(92.43), Id(h_4)]), Block([])])), VarDecl(Id(UhnQ), BoolType, None, Id(tF1K)), FuncDecl(Id(lN), [], Return()), FuncDecl(Id(IGAb), [VarDecl(Id(fr43), BoolType, None, None)], Return(NumLit(42.69))), FuncDecl(Id(pf_), [VarDecl(Id(aR), NumberType, None, None), VarDecl(Id(aO), BoolType, None, None), VarDecl(Id(h8H), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
func q4 (string Bt[98.3,86.31])
	return

func VPg (number i3)
	return

'''
		expect = '''Program([FuncDecl(Id(q4), [VarDecl(Id(Bt), ArrayType([98.3, 86.31], StringType), None, None)], Return()), FuncDecl(Id(VPg), [VarDecl(Id(i3), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
func KQqe (number Wo)	begin
	end
func PRdM (string WFj, bool bg0, string QAs)
	begin
		l0B[84.45, "b"] <- false
		bool yXA
		return
	end

bool wrX[53.49,0.37]
'''
		expect = '''Program([FuncDecl(Id(KQqe), [VarDecl(Id(Wo), NumberType, None, None)], Block([])), FuncDecl(Id(PRdM), [VarDecl(Id(WFj), StringType, None, None), VarDecl(Id(bg0), BoolType, None, None), VarDecl(Id(QAs), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(l0B), [NumLit(84.45), StringLit(b)]), BooleanLit(False)), VarDecl(Id(yXA), BoolType, None, None), Return()])), VarDecl(Id(wrX), ArrayType([53.49, 0.37], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
func LMA (string Rk7[32.26,33.85,98.32], number kcRT[0.08,39.7])
	return true
func Ya2e (number pGM, string ibi)	begin
	end

func Db (number oNoF, number Y_e)
	begin
		for Fh until 37.02 by true
			for rCJh until true by true
				M5d3(true, true)
	end
'''
		expect = '''Program([FuncDecl(Id(LMA), [VarDecl(Id(Rk7), ArrayType([32.26, 33.85, 98.32], StringType), None, None), VarDecl(Id(kcRT), ArrayType([0.08, 39.7], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Ya2e), [VarDecl(Id(pGM), NumberType, None, None), VarDecl(Id(ibi), StringType, None, None)], Block([])), FuncDecl(Id(Db), [VarDecl(Id(oNoF), NumberType, None, None), VarDecl(Id(Y_e), NumberType, None, None)], Block([For(Id(Fh), NumLit(37.02), BooleanLit(True), For(Id(rCJh), BooleanLit(True), BooleanLit(True), CallStmt(Id(M5d3), [BooleanLit(True), BooleanLit(True)])))]))])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
number cP4Y[24.21,67.27] <- false
func JH ()
	begin
		ro_w()
		for cS4 until "YmNh" by xVTn
			begin
				continue
				return zks2
				L_w(1.43, Wlvy, zwJ)
			end
	end
'''
		expect = '''Program([VarDecl(Id(cP4Y), ArrayType([24.21, 67.27], NumberType), None, BooleanLit(False)), FuncDecl(Id(JH), [], Block([CallStmt(Id(ro_w), []), For(Id(cS4), StringLit(YmNh), Id(xVTn), Block([Continue, Return(Id(zks2)), CallStmt(Id(L_w), [NumLit(1.43), Id(Wlvy), Id(zwJ)])]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
string uWNn
bool Ach[10.95,25.93]
'''
		expect = '''Program([VarDecl(Id(uWNn), StringType, None, None), VarDecl(Id(Ach), ArrayType([10.95, 25.93], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
number XY[99.13,34.93]
func d8Ej (bool wx[97.43,5.48,91.9])	begin
	end

func qbq (bool ziO, bool G0A, string YN[55.87,84.25,58.25])	return
string jt[60.33,26.21,1.05] <- IX
bool rs[43.89,44.87,26.64]
'''
		expect = '''Program([VarDecl(Id(XY), ArrayType([99.13, 34.93], NumberType), None, None), FuncDecl(Id(d8Ej), [VarDecl(Id(wx), ArrayType([97.43, 5.48, 91.9], BoolType), None, None)], Block([])), FuncDecl(Id(qbq), [VarDecl(Id(ziO), BoolType, None, None), VarDecl(Id(G0A), BoolType, None, None), VarDecl(Id(YN), ArrayType([55.87, 84.25, 58.25], StringType), None, None)], Return()), VarDecl(Id(jt), ArrayType([60.33, 26.21, 1.05], StringType), None, Id(IX)), VarDecl(Id(rs), ArrayType([43.89, 44.87, 26.64], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
func dy (bool byo)	return

func aQZ ()
	begin
	end
func qc2j ()
	return zJVI

func gT (bool jZK, number tir)	return
func Cv (bool uOU0[34.33,85.07,63.56], bool Cq, bool BW6[42.54,39.78])	begin
		continue
		break
	end

'''
		expect = '''Program([FuncDecl(Id(dy), [VarDecl(Id(byo), BoolType, None, None)], Return()), FuncDecl(Id(aQZ), [], Block([])), FuncDecl(Id(qc2j), [], Return(Id(zJVI))), FuncDecl(Id(gT), [VarDecl(Id(jZK), BoolType, None, None), VarDecl(Id(tir), NumberType, None, None)], Return()), FuncDecl(Id(Cv), [VarDecl(Id(uOU0), ArrayType([34.33, 85.07, 63.56], BoolType), None, None), VarDecl(Id(Cq), BoolType, None, None), VarDecl(Id(BW6), ArrayType([42.54, 39.78], BoolType), None, None)], Block([Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
bool Egp7 <- D8o
'''
		expect = '''Program([VarDecl(Id(Egp7), BoolType, None, Id(D8o))])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
func lia7 (bool zC9[10.9,17.82], number cgW[22.66,47.33], string qI[43.56])
	return

'''
		expect = '''Program([FuncDecl(Id(lia7), [VarDecl(Id(zC9), ArrayType([10.9, 17.82], BoolType), None, None), VarDecl(Id(cgW), ArrayType([22.66, 47.33], NumberType), None, None), VarDecl(Id(qI), ArrayType([43.56], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
number ZsvJ
number Im2z[52.0] <- 14.53
bool ii6J[54.73,95.94] <- 24.86
func IazM (bool zWVU)	return
func eFsJ ()
	begin
		begin
			break
			apb[hj1v, S6] <- "rwc"
			continue
		end
		dynamic jclR
		begin
			string J8p2 <- Kd
			return false
			string coj[31.97]
		end
	end
'''
		expect = '''Program([VarDecl(Id(ZsvJ), NumberType, None, None), VarDecl(Id(Im2z), ArrayType([52.0], NumberType), None, NumLit(14.53)), VarDecl(Id(ii6J), ArrayType([54.73, 95.94], BoolType), None, NumLit(24.86)), FuncDecl(Id(IazM), [VarDecl(Id(zWVU), BoolType, None, None)], Return()), FuncDecl(Id(eFsJ), [], Block([Block([Break, AssignStmt(ArrayCell(Id(apb), [Id(hj1v), Id(S6)]), StringLit(rwc)), Continue]), VarDecl(Id(jclR), None, dynamic, None), Block([VarDecl(Id(J8p2), StringType, None, Id(Kd)), Return(BooleanLit(False)), VarDecl(Id(coj), ArrayType([31.97], StringType), None, None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
func ZNJz (number YyYg[88.02,62.42,73.79], number yQ, number sw)
	begin
	end

func OVs (bool oxMF, number q8_)
	return
dynamic DQWm <- false
string dnf[54.54,5.64,10.79] <- ULT
'''
		expect = '''Program([FuncDecl(Id(ZNJz), [VarDecl(Id(YyYg), ArrayType([88.02, 62.42, 73.79], NumberType), None, None), VarDecl(Id(yQ), NumberType, None, None), VarDecl(Id(sw), NumberType, None, None)], Block([])), FuncDecl(Id(OVs), [VarDecl(Id(oxMF), BoolType, None, None), VarDecl(Id(q8_), NumberType, None, None)], Return()), VarDecl(Id(DQWm), None, dynamic, BooleanLit(False)), VarDecl(Id(dnf), ArrayType([54.54, 5.64, 10.79], StringType), None, Id(ULT))])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
func RS (bool cZZ, bool drE[9.78,75.01,64.6], bool kr)	begin
		vOS(Aj, true)
	end

number NG[56.1]
func dpLq (string pudT, string g1Us, string bb)
	return
'''
		expect = '''Program([FuncDecl(Id(RS), [VarDecl(Id(cZZ), BoolType, None, None), VarDecl(Id(drE), ArrayType([9.78, 75.01, 64.6], BoolType), None, None), VarDecl(Id(kr), BoolType, None, None)], Block([CallStmt(Id(vOS), [Id(Aj), BooleanLit(True)])])), VarDecl(Id(NG), ArrayType([56.1], NumberType), None, None), FuncDecl(Id(dpLq), [VarDecl(Id(pudT), StringType, None, None), VarDecl(Id(g1Us), StringType, None, None), VarDecl(Id(bb), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
bool cY <- false
func ylNB (string C0)	return "Kt"
func vR9 (bool OZH[1.57,0.86,37.82], bool JclK)	begin
		for SM until 96.63 by false
			VVv <- gecE
		string EmZJ[15.13,83.14] <- true
	end
'''
		expect = '''Program([VarDecl(Id(cY), BoolType, None, BooleanLit(False)), FuncDecl(Id(ylNB), [VarDecl(Id(C0), StringType, None, None)], Return(StringLit(Kt))), FuncDecl(Id(vR9), [VarDecl(Id(OZH), ArrayType([1.57, 0.86, 37.82], BoolType), None, None), VarDecl(Id(JclK), BoolType, None, None)], Block([For(Id(SM), NumLit(96.63), BooleanLit(False), AssignStmt(Id(VVv), Id(gecE))), VarDecl(Id(EmZJ), ArrayType([15.13, 83.14], StringType), None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
number jz
var uY <- "KP"
string dy0N
'''
		expect = '''Program([VarDecl(Id(jz), NumberType, None, None), VarDecl(Id(uY), None, var, StringLit(KP)), VarDecl(Id(dy0N), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
func w2we (string zxZ, string YdY[29.54,41.41,39.09])
	begin
		begin
			return 87.22
		end
		for hV7 until 30.46 by "qNI"
			break
	end

func hZ ()
	begin
		begin
			continue
		end
	end
func bbky (number r1)
	return "pnrUk"

bool S29
'''
		expect = '''Program([FuncDecl(Id(w2we), [VarDecl(Id(zxZ), StringType, None, None), VarDecl(Id(YdY), ArrayType([29.54, 41.41, 39.09], StringType), None, None)], Block([Block([Return(NumLit(87.22))]), For(Id(hV7), NumLit(30.46), StringLit(qNI), Break)])), FuncDecl(Id(hZ), [], Block([Block([Continue])])), FuncDecl(Id(bbky), [VarDecl(Id(r1), NumberType, None, None)], Return(StringLit(pnrUk))), VarDecl(Id(S29), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
string SA[95.42,37.12,14.71]
bool IpiM[18.52,49.53,28.34] <- 37.18
func nA0 (bool dupE[39.39,0.19,50.85])	begin
		return true
		break
		begin
			begin
			end
			if (tFeF) var I4 <- 50.19
			elif (false)
			for dDr until Sidi by false
				bQM <- true
			elif (true) break
			elif (NKxP)
			for TblG until "hRB" by true
				bool d5P[23.26]
			elif ("C")
			JL <- false
			elif ("VjUFy")
			continue
		end
	end
func mjSm (string cc[70.59,27.3], string sCMb[30.69,57.55], number HX)
	return LWVn

func XCS (bool GOi[43.36])	return 5.85
'''
		expect = '''Program([VarDecl(Id(SA), ArrayType([95.42, 37.12, 14.71], StringType), None, None), VarDecl(Id(IpiM), ArrayType([18.52, 49.53, 28.34], BoolType), None, NumLit(37.18)), FuncDecl(Id(nA0), [VarDecl(Id(dupE), ArrayType([39.39, 0.19, 50.85], BoolType), None, None)], Block([Return(BooleanLit(True)), Break, Block([Block([]), If((Id(tFeF), VarDecl(Id(I4), None, var, NumLit(50.19))), [(BooleanLit(False), For(Id(dDr), Id(Sidi), BooleanLit(False), AssignStmt(Id(bQM), BooleanLit(True)))), (BooleanLit(True), Break), (Id(NKxP), For(Id(TblG), StringLit(hRB), BooleanLit(True), VarDecl(Id(d5P), ArrayType([23.26], BoolType), None, None))), (StringLit(C), AssignStmt(Id(JL), BooleanLit(False))), (StringLit(VjUFy), Continue)], None)])])), FuncDecl(Id(mjSm), [VarDecl(Id(cc), ArrayType([70.59, 27.3], StringType), None, None), VarDecl(Id(sCMb), ArrayType([30.69, 57.55], StringType), None, None), VarDecl(Id(HX), NumberType, None, None)], Return(Id(LWVn))), FuncDecl(Id(XCS), [VarDecl(Id(GOi), ArrayType([43.36], BoolType), None, None)], Return(NumLit(5.85)))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
func RZGP (bool oS[66.78,63.06], string ixUg, number Pab[48.45,37.58])
	return false

func jwYi (string rHL_)	return true

func y0Ps (string Hp78, string Zmo, string H3)	return

bool XRQE[46.45,90.58]
bool Ou1E <- "WxE"
'''
		expect = '''Program([FuncDecl(Id(RZGP), [VarDecl(Id(oS), ArrayType([66.78, 63.06], BoolType), None, None), VarDecl(Id(ixUg), StringType, None, None), VarDecl(Id(Pab), ArrayType([48.45, 37.58], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(jwYi), [VarDecl(Id(rHL_), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(y0Ps), [VarDecl(Id(Hp78), StringType, None, None), VarDecl(Id(Zmo), StringType, None, None), VarDecl(Id(H3), StringType, None, None)], Return()), VarDecl(Id(XRQE), ArrayType([46.45, 90.58], BoolType), None, None), VarDecl(Id(Ou1E), BoolType, None, StringLit(WxE))])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
func i9nB (string MeJK, number k2E[35.24], string YC[71.24,64.8,33.54])
	return
func g6 ()
	return true
func AeL (bool SXoQ, number Rog[18.6,11.25], number l5H)	return
func mQ ()
	return

func elyw (number Ahq, number mt[48.63,26.71,11.3])
	begin
		string IW <- 1.68
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(i9nB), [VarDecl(Id(MeJK), StringType, None, None), VarDecl(Id(k2E), ArrayType([35.24], NumberType), None, None), VarDecl(Id(YC), ArrayType([71.24, 64.8, 33.54], StringType), None, None)], Return()), FuncDecl(Id(g6), [], Return(BooleanLit(True))), FuncDecl(Id(AeL), [VarDecl(Id(SXoQ), BoolType, None, None), VarDecl(Id(Rog), ArrayType([18.6, 11.25], NumberType), None, None), VarDecl(Id(l5H), NumberType, None, None)], Return()), FuncDecl(Id(mQ), [], Return()), FuncDecl(Id(elyw), [VarDecl(Id(Ahq), NumberType, None, None), VarDecl(Id(mt), ArrayType([48.63, 26.71, 11.3], NumberType), None, None)], Block([VarDecl(Id(IW), StringType, None, NumLit(1.68)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
number An[29.66] <- 18.98
func NY ()
	return
func go (bool v3c9[53.64,99.03], string HBA, string QOa9)	return qN

func dA (number Eb6[94.42], bool fg[43.89,10.59,70.15])
	return
bool np
'''
		expect = '''Program([VarDecl(Id(An), ArrayType([29.66], NumberType), None, NumLit(18.98)), FuncDecl(Id(NY), [], Return()), FuncDecl(Id(go), [VarDecl(Id(v3c9), ArrayType([53.64, 99.03], BoolType), None, None), VarDecl(Id(HBA), StringType, None, None), VarDecl(Id(QOa9), StringType, None, None)], Return(Id(qN))), FuncDecl(Id(dA), [VarDecl(Id(Eb6), ArrayType([94.42], NumberType), None, None), VarDecl(Id(fg), ArrayType([43.89, 10.59, 70.15], BoolType), None, None)], Return()), VarDecl(Id(np), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
func Kg ()
	return 5.15

func aD (string RU, bool tUqs, string Ip)	return 91.01

'''
		expect = '''Program([FuncDecl(Id(Kg), [], Return(NumLit(5.15))), FuncDecl(Id(aD), [VarDecl(Id(RU), StringType, None, None), VarDecl(Id(tUqs), BoolType, None, None), VarDecl(Id(Ip), StringType, None, None)], Return(NumLit(91.01)))])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
string Y4
number IvPv[30.49,34.86] <- "r"
number I61[94.05,98.68,6.95] <- 35.56
string af8[96.04,99.62,69.13]
'''
		expect = '''Program([VarDecl(Id(Y4), StringType, None, None), VarDecl(Id(IvPv), ArrayType([30.49, 34.86], NumberType), None, StringLit(r)), VarDecl(Id(I61), ArrayType([94.05, 98.68, 6.95], NumberType), None, NumLit(35.56)), VarDecl(Id(af8), ArrayType([96.04, 99.62, 69.13], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
func u_ (number Jck)
	return
func BTP7 (number OE9Q[45.66,94.01], number DSLH)
	return

'''
		expect = '''Program([FuncDecl(Id(u_), [VarDecl(Id(Jck), NumberType, None, None)], Return()), FuncDecl(Id(BTP7), [VarDecl(Id(OE9Q), ArrayType([45.66, 94.01], NumberType), None, None), VarDecl(Id(DSLH), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
func fQoa (bool xYI)	begin
		begin
		end
	end

func wxu (bool P6, string TIYA[90.67,52.78,57.21], number TU1V)	begin
		zJQ[true, OE08, "M"] <- "kIPU"
		if (AO9z)
		f04("IhKD", "eN", "KHfZJ")
		elif (false)
		break
		elif (false)
		break
		elif ("UnpF")
		u1[jV, true] <- true
		elif (false) bIJt["Mdx", "ZIHOR", "lWJx"] <- true
		elif (40.34) return
		else continue
	end
func AMd (string Ww[70.99,42.37,26.46], number Wo[52.79])
	return

number ei2[65.74,82.12,91.63]
func dhW ()	begin
		zmQ(65.83)
		break
		k_i <- 29.48
	end

'''
		expect = '''Program([FuncDecl(Id(fQoa), [VarDecl(Id(xYI), BoolType, None, None)], Block([Block([])])), FuncDecl(Id(wxu), [VarDecl(Id(P6), BoolType, None, None), VarDecl(Id(TIYA), ArrayType([90.67, 52.78, 57.21], StringType), None, None), VarDecl(Id(TU1V), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(zJQ), [BooleanLit(True), Id(OE08), StringLit(M)]), StringLit(kIPU)), If((Id(AO9z), CallStmt(Id(f04), [StringLit(IhKD), StringLit(eN), StringLit(KHfZJ)])), [(BooleanLit(False), Break), (BooleanLit(False), Break), (StringLit(UnpF), AssignStmt(ArrayCell(Id(u1), [Id(jV), BooleanLit(True)]), BooleanLit(True))), (BooleanLit(False), AssignStmt(ArrayCell(Id(bIJt), [StringLit(Mdx), StringLit(ZIHOR), StringLit(lWJx)]), BooleanLit(True))), (NumLit(40.34), Return())], Continue)])), FuncDecl(Id(AMd), [VarDecl(Id(Ww), ArrayType([70.99, 42.37, 26.46], StringType), None, None), VarDecl(Id(Wo), ArrayType([52.79], NumberType), None, None)], Return()), VarDecl(Id(ei2), ArrayType([65.74, 82.12, 91.63], NumberType), None, None), FuncDecl(Id(dhW), [], Block([CallStmt(Id(zmQ), [NumLit(65.83)]), Break, AssignStmt(Id(k_i), NumLit(29.48))]))])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
string Rh[42.38,20.28,36.86]
'''
		expect = '''Program([VarDecl(Id(Rh), ArrayType([42.38, 20.28, 36.86], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
string NYn <- 32.78
dynamic TP <- X4yI
bool Hk <- true
func JMwQ (number OgIZ[71.77,91.18])	return

'''
		expect = '''Program([VarDecl(Id(NYn), StringType, None, NumLit(32.78)), VarDecl(Id(TP), None, dynamic, Id(X4yI)), VarDecl(Id(Hk), BoolType, None, BooleanLit(True)), FuncDecl(Id(JMwQ), [VarDecl(Id(OgIZ), ArrayType([71.77, 91.18], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
bool U4 <- 48.36
string KJj[80.07,54.54] <- "iyvcS"
func wF (bool YRGa, string iQFI)	return 64.74

string E2F[50.01,35.37]
'''
		expect = '''Program([VarDecl(Id(U4), BoolType, None, NumLit(48.36)), VarDecl(Id(KJj), ArrayType([80.07, 54.54], StringType), None, StringLit(iyvcS)), FuncDecl(Id(wF), [VarDecl(Id(YRGa), BoolType, None, None), VarDecl(Id(iQFI), StringType, None, None)], Return(NumLit(64.74))), VarDecl(Id(E2F), ArrayType([50.01, 35.37], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
string J8aT
dynamic WA
func fFSJ (string Hz, bool lCw[50.42,81.29,28.69], number rWw[88.07,98.48,63.72])	return

'''
		expect = '''Program([VarDecl(Id(J8aT), StringType, None, None), VarDecl(Id(WA), None, dynamic, None), FuncDecl(Id(fFSJ), [VarDecl(Id(Hz), StringType, None, None), VarDecl(Id(lCw), ArrayType([50.42, 81.29, 28.69], BoolType), None, None), VarDecl(Id(rWw), ArrayType([88.07, 98.48, 63.72], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
func CDqh (number PgC, number R4[31.31,87.91])
	begin
		m7M <- "YNO"
	end

'''
		expect = '''Program([FuncDecl(Id(CDqh), [VarDecl(Id(PgC), NumberType, None, None), VarDecl(Id(R4), ArrayType([31.31, 87.91], NumberType), None, None)], Block([AssignStmt(Id(m7M), StringLit(YNO))]))])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
bool y9_0[59.13] <- JM
number TH6e
bool LK
'''
		expect = '''Program([VarDecl(Id(y9_0), ArrayType([59.13], BoolType), None, Id(JM)), VarDecl(Id(TH6e), NumberType, None, None), VarDecl(Id(LK), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
bool uXS2[71.96,78.57,87.17]
string bO
'''
		expect = '''Program([VarDecl(Id(uXS2), ArrayType([71.96, 78.57, 87.17], BoolType), None, None), VarDecl(Id(bO), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
dynamic HR <- ph
string nfk[92.48,56.6,6.1]
'''
		expect = '''Program([VarDecl(Id(HR), None, dynamic, Id(ph)), VarDecl(Id(nfk), ArrayType([92.48, 56.6, 6.1], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
func pTz ()	return

'''
		expect = '''Program([FuncDecl(Id(pTz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''
bool R6U
bool tc[77.0,74.85,66.88] <- SUJe
'''
		expect = '''Program([VarDecl(Id(R6U), BoolType, None, None), VarDecl(Id(tc), ArrayType([77.0, 74.85, 66.88], BoolType), None, Id(SUJe))])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
func q0a ()	begin
		break
		tHLt(cV)
		break
	end
func xwL (bool IP[33.71], number eQhN[0.19])	return

'''
		expect = '''Program([FuncDecl(Id(q0a), [], Block([Break, CallStmt(Id(tHLt), [Id(cV)]), Break])), FuncDecl(Id(xwL), [VarDecl(Id(IP), ArrayType([33.71], BoolType), None, None), VarDecl(Id(eQhN), ArrayType([0.19], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
func U5 (bool a6)
	begin
		continue
	end
func Gy (bool ew, string YSy[31.01,69.63,93.21], bool NW3l)	return 96.78
func wR (number rh4O, number HZY, bool Z5C)
	return

'''
		expect = '''Program([FuncDecl(Id(U5), [VarDecl(Id(a6), BoolType, None, None)], Block([Continue])), FuncDecl(Id(Gy), [VarDecl(Id(ew), BoolType, None, None), VarDecl(Id(YSy), ArrayType([31.01, 69.63, 93.21], StringType), None, None), VarDecl(Id(NW3l), BoolType, None, None)], Return(NumLit(96.78))), FuncDecl(Id(wR), [VarDecl(Id(rh4O), NumberType, None, None), VarDecl(Id(HZY), NumberType, None, None), VarDecl(Id(Z5C), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
dynamic MxGS
'''
		expect = '''Program([VarDecl(Id(MxGS), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
func oR (string cw[66.01])
	begin
		continue
	end
bool VYPY[64.16,32.61] <- "i"
func oV (bool m_, string v3Rs[45.2,28.98,75.81])	begin
		QD["Z", true, 12.24] <- "E"
		if (16.24)
		krJI(3.04, mC)
		elif (true) g_O0("xXJ")
		elif ("Gxb")
		continue
		elif (false)
		wVj3 <- true
		else continue
	end

number HY[1.67,25.78]
'''
		expect = '''Program([FuncDecl(Id(oR), [VarDecl(Id(cw), ArrayType([66.01], StringType), None, None)], Block([Continue])), VarDecl(Id(VYPY), ArrayType([64.16, 32.61], BoolType), None, StringLit(i)), FuncDecl(Id(oV), [VarDecl(Id(m_), BoolType, None, None), VarDecl(Id(v3Rs), ArrayType([45.2, 28.98, 75.81], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(QD), [StringLit(Z), BooleanLit(True), NumLit(12.24)]), StringLit(E)), If((NumLit(16.24), CallStmt(Id(krJI), [NumLit(3.04), Id(mC)])), [(BooleanLit(True), CallStmt(Id(g_O0), [StringLit(xXJ)])), (StringLit(Gxb), Continue), (BooleanLit(False), AssignStmt(Id(wVj3), BooleanLit(True)))], Continue)])), VarDecl(Id(HY), ArrayType([1.67, 25.78], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
string Q6KW <- "Vp"
'''
		expect = '''Program([VarDecl(Id(Q6KW), StringType, None, StringLit(Vp))])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
var nk2 <- plZs
func vbZ ()	return 89.99

bool NQv <- true
func MvM (number KEf[45.65,16.75])
	return jmU

func NL (number NAV[26.08,75.48,39.57], number fYIE)
	return
'''
		expect = '''Program([VarDecl(Id(nk2), None, var, Id(plZs)), FuncDecl(Id(vbZ), [], Return(NumLit(89.99))), VarDecl(Id(NQv), BoolType, None, BooleanLit(True)), FuncDecl(Id(MvM), [VarDecl(Id(KEf), ArrayType([45.65, 16.75], NumberType), None, None)], Return(Id(jmU))), FuncDecl(Id(NL), [VarDecl(Id(NAV), ArrayType([26.08, 75.48, 39.57], NumberType), None, None), VarDecl(Id(fYIE), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
var qJ0q <- false
'''
		expect = '''Program([VarDecl(Id(qJ0q), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
string rl <- 91.12
func ID (string N4[76.84,77.17], bool HFM, number KFdj)
	return "fZPRY"
var vvc <- xn
func ydH (bool AW, bool SO[12.12,24.47])
	begin
		break
		begin
			break
		end
		for YJ3S until "zGJj" by 29.51
			for t2 until "vL" by maXp
				if (rIb) continue
	end

func QOo (bool DR[94.46,3.83,55.78], number tR[16.12,10.96,63.82])
	return
'''
		expect = '''Program([VarDecl(Id(rl), StringType, None, NumLit(91.12)), FuncDecl(Id(ID), [VarDecl(Id(N4), ArrayType([76.84, 77.17], StringType), None, None), VarDecl(Id(HFM), BoolType, None, None), VarDecl(Id(KFdj), NumberType, None, None)], Return(StringLit(fZPRY))), VarDecl(Id(vvc), None, var, Id(xn)), FuncDecl(Id(ydH), [VarDecl(Id(AW), BoolType, None, None), VarDecl(Id(SO), ArrayType([12.12, 24.47], BoolType), None, None)], Block([Break, Block([Break]), For(Id(YJ3S), StringLit(zGJj), NumLit(29.51), For(Id(t2), StringLit(vL), Id(maXp), If((Id(rIb), Continue), [], None)))])), FuncDecl(Id(QOo), [VarDecl(Id(DR), ArrayType([94.46, 3.83, 55.78], BoolType), None, None), VarDecl(Id(tR), ArrayType([16.12, 10.96, 63.82], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
func crTl ()
	return false

bool pAV[17.59,97.49]
bool onz
number ewI
func BVho (number LN2, number CnxM[72.57,5.1])	return

'''
		expect = '''Program([FuncDecl(Id(crTl), [], Return(BooleanLit(False))), VarDecl(Id(pAV), ArrayType([17.59, 97.49], BoolType), None, None), VarDecl(Id(onz), BoolType, None, None), VarDecl(Id(ewI), NumberType, None, None), FuncDecl(Id(BVho), [VarDecl(Id(LN2), NumberType, None, None), VarDecl(Id(CnxM), ArrayType([72.57, 5.1], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
bool cF <- false
func jc (string Sg)
	begin
		if (true)
		dynamic FkQN
		elif ("g") continue
		elif (qJ4)
		for Qe until 43.55 by true
			X63 <- Fu
		elif (false) continue
		else return
		break
	end
number D6[33.93] <- "DBmP"
'''
		expect = '''Program([VarDecl(Id(cF), BoolType, None, BooleanLit(False)), FuncDecl(Id(jc), [VarDecl(Id(Sg), StringType, None, None)], Block([If((BooleanLit(True), VarDecl(Id(FkQN), None, dynamic, None)), [(StringLit(g), Continue), (Id(qJ4), For(Id(Qe), NumLit(43.55), BooleanLit(True), AssignStmt(Id(X63), Id(Fu)))), (BooleanLit(False), Continue)], Return()), Break])), VarDecl(Id(D6), ArrayType([33.93], NumberType), None, StringLit(DBmP))])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
var r4c <- DmwK
'''
		expect = '''Program([VarDecl(Id(r4c), None, var, Id(DmwK))])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
number LU <- 22.64
func zfF (number iy3, string wEMs[92.85], bool nl[67.26,26.15,2.74])	return "jtC"
var n9 <- 75.65
'''
		expect = '''Program([VarDecl(Id(LU), NumberType, None, NumLit(22.64)), FuncDecl(Id(zfF), [VarDecl(Id(iy3), NumberType, None, None), VarDecl(Id(wEMs), ArrayType([92.85], StringType), None, None), VarDecl(Id(nl), ArrayType([67.26, 26.15, 2.74], BoolType), None, None)], Return(StringLit(jtC))), VarDecl(Id(n9), None, var, NumLit(75.65))])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func p5ar ()	return
func DQI (bool cBLb, string rsE[39.47], number sV)
	begin
		LXRu <- "eve"
	end

func EJ (bool D_C[55.2,45.12], number mie[27.06,70.35,11.24], bool aAb[43.93,4.1])
	return true

dynamic KGwJ <- lIq
'''
		expect = '''Program([FuncDecl(Id(p5ar), [], Return()), FuncDecl(Id(DQI), [VarDecl(Id(cBLb), BoolType, None, None), VarDecl(Id(rsE), ArrayType([39.47], StringType), None, None), VarDecl(Id(sV), NumberType, None, None)], Block([AssignStmt(Id(LXRu), StringLit(eve))])), FuncDecl(Id(EJ), [VarDecl(Id(D_C), ArrayType([55.2, 45.12], BoolType), None, None), VarDecl(Id(mie), ArrayType([27.06, 70.35, 11.24], NumberType), None, None), VarDecl(Id(aAb), ArrayType([43.93, 4.1], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(KGwJ), None, dynamic, Id(lIq))])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
bool BiYp
func M0 (string zB, number qq4)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(BiYp), BoolType, None, None), FuncDecl(Id(M0), [VarDecl(Id(zB), StringType, None, None), VarDecl(Id(qq4), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
string Hq[42.3,65.96]
'''
		expect = '''Program([VarDecl(Id(Hq), ArrayType([42.3, 65.96], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
dynamic qBY <- false
func JW (number VUp, bool codr)	return

'''
		expect = '''Program([VarDecl(Id(qBY), None, dynamic, BooleanLit(False)), FuncDecl(Id(JW), [VarDecl(Id(VUp), NumberType, None, None), VarDecl(Id(codr), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
bool vV5M <- true
func Mba (number sT)	begin
	end
func iU9x (string m4ri, number P2v, bool ci[42.47,2.38])	begin
		break
	end

var o7 <- 92.7
'''
		expect = '''Program([VarDecl(Id(vV5M), BoolType, None, BooleanLit(True)), FuncDecl(Id(Mba), [VarDecl(Id(sT), NumberType, None, None)], Block([])), FuncDecl(Id(iU9x), [VarDecl(Id(m4ri), StringType, None, None), VarDecl(Id(P2v), NumberType, None, None), VarDecl(Id(ci), ArrayType([42.47, 2.38], BoolType), None, None)], Block([Break])), VarDecl(Id(o7), None, var, NumLit(92.7))])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
bool Zx <- "mjh"
func NUWC (number QJn[96.39,65.7])	return true
string s_m[4.04,4.2,10.15]
'''
		expect = '''Program([VarDecl(Id(Zx), BoolType, None, StringLit(mjh)), FuncDecl(Id(NUWC), [VarDecl(Id(QJn), ArrayType([96.39, 65.7], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(s_m), ArrayType([4.04, 4.2, 10.15], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
number Cr
'''
		expect = '''Program([VarDecl(Id(Cr), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
number mRe
var E1 <- "BftBw"
func dPrB (number Nb[54.58,11.29], bool MkD)	return "wRa"

dynamic vkX
func AFG (bool Y4hi[57.67])	return true
'''
		expect = '''Program([VarDecl(Id(mRe), NumberType, None, None), VarDecl(Id(E1), None, var, StringLit(BftBw)), FuncDecl(Id(dPrB), [VarDecl(Id(Nb), ArrayType([54.58, 11.29], NumberType), None, None), VarDecl(Id(MkD), BoolType, None, None)], Return(StringLit(wRa))), VarDecl(Id(vkX), None, dynamic, None), FuncDecl(Id(AFG), [VarDecl(Id(Y4hi), ArrayType([57.67], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
string Ux[42.26] <- true
string Uow
func v3Yw ()	return "etB"

'''
		expect = '''Program([VarDecl(Id(Ux), ArrayType([42.26], StringType), None, BooleanLit(True)), VarDecl(Id(Uow), StringType, None, None), FuncDecl(Id(v3Yw), [], Return(StringLit(etB)))])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
number bX <- "MKd"
'''
		expect = '''Program([VarDecl(Id(bX), NumberType, None, StringLit(MKd))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
func GL (string AGnq[6.41,89.05], number ClLx)
	return
number Oxf[92.19,47.1,84.69]
string n_8
func L8b0 (bool KF[35.27,8.04], bool GIOB, number kON)
	return
bool Jbp[60.1,8.41]
'''
		expect = '''Program([FuncDecl(Id(GL), [VarDecl(Id(AGnq), ArrayType([6.41, 89.05], StringType), None, None), VarDecl(Id(ClLx), NumberType, None, None)], Return()), VarDecl(Id(Oxf), ArrayType([92.19, 47.1, 84.69], NumberType), None, None), VarDecl(Id(n_8), StringType, None, None), FuncDecl(Id(L8b0), [VarDecl(Id(KF), ArrayType([35.27, 8.04], BoolType), None, None), VarDecl(Id(GIOB), BoolType, None, None), VarDecl(Id(kON), NumberType, None, None)], Return()), VarDecl(Id(Jbp), ArrayType([60.1, 8.41], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
number KT
string y32[21.84,34.17,1.24] <- 53.05
number ow
'''
		expect = '''Program([VarDecl(Id(KT), NumberType, None, None), VarDecl(Id(y32), ArrayType([21.84, 34.17, 1.24], StringType), None, NumLit(53.05)), VarDecl(Id(ow), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
number VAJ6 <- JH3
string d60[69.4,13.64,11.42]
func lF ()	return
func tWGg ()	return
bool THG[29.6] <- true
'''
		expect = '''Program([VarDecl(Id(VAJ6), NumberType, None, Id(JH3)), VarDecl(Id(d60), ArrayType([69.4, 13.64, 11.42], StringType), None, None), FuncDecl(Id(lF), [], Return()), FuncDecl(Id(tWGg), [], Return()), VarDecl(Id(THG), ArrayType([29.6], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
number v3DN <- 48.34
func J1s (string QI[13.04,27.46,29.84], string A4[49.56], bool MC)
	return
var g3L9 <- SPN
'''
		expect = '''Program([VarDecl(Id(v3DN), NumberType, None, NumLit(48.34)), FuncDecl(Id(J1s), [VarDecl(Id(QI), ArrayType([13.04, 27.46, 29.84], StringType), None, None), VarDecl(Id(A4), ArrayType([49.56], StringType), None, None), VarDecl(Id(MC), BoolType, None, None)], Return()), VarDecl(Id(g3L9), None, var, Id(SPN))])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
dynamic bq
number VuU
func kq (number Ff, number cGhn, number Ks)
	return wzX

func Rugn (bool QMqW[23.19,37.36])
	return
'''
		expect = '''Program([VarDecl(Id(bq), None, dynamic, None), VarDecl(Id(VuU), NumberType, None, None), FuncDecl(Id(kq), [VarDecl(Id(Ff), NumberType, None, None), VarDecl(Id(cGhn), NumberType, None, None), VarDecl(Id(Ks), NumberType, None, None)], Return(Id(wzX))), FuncDecl(Id(Rugn), [VarDecl(Id(QMqW), ArrayType([23.19, 37.36], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
number qZ[99.61]
'''
		expect = '''Program([VarDecl(Id(qZ), ArrayType([99.61], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
bool hsM[47.48,5.23,76.14]
func aKBJ (string bX)
	return s1
var Eojw <- 6.98
string oM <- true
number OZkr <- "D"
'''
		expect = '''Program([VarDecl(Id(hsM), ArrayType([47.48, 5.23, 76.14], BoolType), None, None), FuncDecl(Id(aKBJ), [VarDecl(Id(bX), StringType, None, None)], Return(Id(s1))), VarDecl(Id(Eojw), None, var, NumLit(6.98)), VarDecl(Id(oM), StringType, None, BooleanLit(True)), VarDecl(Id(OZkr), NumberType, None, StringLit(D))])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
number X9hT[18.77,55.14] <- knn
func Mr ()
	begin
		vGw(14.2, "j")
		break
		begin
			if ("yZABf") number F1Pz[20.63]
			elif ("gAl") jPG()
			elif (81.0) break
			elif (false) number BDB[88.71,76.67] <- false
			elif (Eht)
			O2l <- 13.03
			else return
		end
	end
func vog ()	return false
'''
		expect = '''Program([VarDecl(Id(X9hT), ArrayType([18.77, 55.14], NumberType), None, Id(knn)), FuncDecl(Id(Mr), [], Block([CallStmt(Id(vGw), [NumLit(14.2), StringLit(j)]), Break, Block([If((StringLit(yZABf), VarDecl(Id(F1Pz), ArrayType([20.63], NumberType), None, None)), [(StringLit(gAl), CallStmt(Id(jPG), [])), (NumLit(81.0), Break), (BooleanLit(False), VarDecl(Id(BDB), ArrayType([88.71, 76.67], NumberType), None, BooleanLit(False))), (Id(Eht), AssignStmt(Id(O2l), NumLit(13.03)))], Return())])])), FuncDecl(Id(vog), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
bool qsHC[37.27]
var dkk <- false
dynamic lN0
'''
		expect = '''Program([VarDecl(Id(qsHC), ArrayType([37.27], BoolType), None, None), VarDecl(Id(dkk), None, var, BooleanLit(False)), VarDecl(Id(lN0), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
bool jss[74.76,36.15] <- "iDTNx"
func ol (string Q1[97.57,14.19,55.09], number tu_9)	return
func oi (number cIA[83.22], bool OS)	return "n"

number gbI[89.45,24.39] <- MPsQ
'''
		expect = '''Program([VarDecl(Id(jss), ArrayType([74.76, 36.15], BoolType), None, StringLit(iDTNx)), FuncDecl(Id(ol), [VarDecl(Id(Q1), ArrayType([97.57, 14.19, 55.09], StringType), None, None), VarDecl(Id(tu_9), NumberType, None, None)], Return()), FuncDecl(Id(oi), [VarDecl(Id(cIA), ArrayType([83.22], NumberType), None, None), VarDecl(Id(OS), BoolType, None, None)], Return(StringLit(n))), VarDecl(Id(gbI), ArrayType([89.45, 24.39], NumberType), None, Id(MPsQ))])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
bool GQ[11.56,46.56] <- AKt
func vt (bool bA, number IyCG[54.1])
	begin
		Vy(qnWD, false)
	end
func suXl ()	return WJma
'''
		expect = '''Program([VarDecl(Id(GQ), ArrayType([11.56, 46.56], BoolType), None, Id(AKt)), FuncDecl(Id(vt), [VarDecl(Id(bA), BoolType, None, None), VarDecl(Id(IyCG), ArrayType([54.1], NumberType), None, None)], Block([CallStmt(Id(Vy), [Id(qnWD), BooleanLit(False)])])), FuncDecl(Id(suXl), [], Return(Id(WJma)))])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
number L28[1.77] <- "DRxiJ"
func TT (bool HmB[34.3,61.3,70.72], bool wS)
	return false
bool tG_[64.43,49.64,17.12] <- "YYt"
'''
		expect = '''Program([VarDecl(Id(L28), ArrayType([1.77], NumberType), None, StringLit(DRxiJ)), FuncDecl(Id(TT), [VarDecl(Id(HmB), ArrayType([34.3, 61.3, 70.72], BoolType), None, None), VarDecl(Id(wS), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(tG_), ArrayType([64.43, 49.64, 17.12], BoolType), None, StringLit(YYt))])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
string dtA[8.58,29.84,17.08] <- true
func MJ1 (number Vi, bool dW)
	return E3LM

var SZx8 <- q8
func kj (string LLtn[98.97], number WRn)	begin
		break
	end
func wEE3 (number Zx[19.23,74.33], bool Qj[34.84,73.46], number OfY)
	begin
		Zj6 <- "XmmB"
		begin
			return
			break
		end
	end

'''
		expect = '''Program([VarDecl(Id(dtA), ArrayType([8.58, 29.84, 17.08], StringType), None, BooleanLit(True)), FuncDecl(Id(MJ1), [VarDecl(Id(Vi), NumberType, None, None), VarDecl(Id(dW), BoolType, None, None)], Return(Id(E3LM))), VarDecl(Id(SZx8), None, var, Id(q8)), FuncDecl(Id(kj), [VarDecl(Id(LLtn), ArrayType([98.97], StringType), None, None), VarDecl(Id(WRn), NumberType, None, None)], Block([Break])), FuncDecl(Id(wEE3), [VarDecl(Id(Zx), ArrayType([19.23, 74.33], NumberType), None, None), VarDecl(Id(Qj), ArrayType([34.84, 73.46], BoolType), None, None), VarDecl(Id(OfY), NumberType, None, None)], Block([AssignStmt(Id(Zj6), StringLit(XmmB)), Block([Return(), Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
func wp (bool TE8m[4.85,21.92], bool Nr)	begin
	end
number Vr[79.35,24.9,26.84]
string PSM[49.02,1.76,83.32]
'''
		expect = '''Program([FuncDecl(Id(wp), [VarDecl(Id(TE8m), ArrayType([4.85, 21.92], BoolType), None, None), VarDecl(Id(Nr), BoolType, None, None)], Block([])), VarDecl(Id(Vr), ArrayType([79.35, 24.9, 26.84], NumberType), None, None), VarDecl(Id(PSM), ArrayType([49.02, 1.76, 83.32], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
func qX0T (string R2v, bool tnlR)
	return
func cTM (number Itr1[9.94,49.36])
	begin
		if ("KiYE") break
		else break
	end
func ikb (number a0xl, string oE[40.07,27.79])
	return false

func cS (string wKKJ)
	return
string IHa[7.48,87.38] <- true
'''
		expect = '''Program([FuncDecl(Id(qX0T), [VarDecl(Id(R2v), StringType, None, None), VarDecl(Id(tnlR), BoolType, None, None)], Return()), FuncDecl(Id(cTM), [VarDecl(Id(Itr1), ArrayType([9.94, 49.36], NumberType), None, None)], Block([If((StringLit(KiYE), Break), [], Break)])), FuncDecl(Id(ikb), [VarDecl(Id(a0xl), NumberType, None, None), VarDecl(Id(oE), ArrayType([40.07, 27.79], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(cS), [VarDecl(Id(wKKJ), StringType, None, None)], Return()), VarDecl(Id(IHa), ArrayType([7.48, 87.38], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
func Bo (number npmc[57.07,13.17], string y8XB[31.94])	begin
	end

func kaD ()
	return
number pSYf <- false
func Xrie ()	return

string ikD3[83.65,84.64]
'''
		expect = '''Program([FuncDecl(Id(Bo), [VarDecl(Id(npmc), ArrayType([57.07, 13.17], NumberType), None, None), VarDecl(Id(y8XB), ArrayType([31.94], StringType), None, None)], Block([])), FuncDecl(Id(kaD), [], Return()), VarDecl(Id(pSYf), NumberType, None, BooleanLit(False)), FuncDecl(Id(Xrie), [], Return()), VarDecl(Id(ikD3), ArrayType([83.65, 84.64], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
func uFLM ()	return

string YQY <- NbuI
number VK[0.08,79.37,56.6] <- 69.15
dynamic b4Z <- false
'''
		expect = '''Program([FuncDecl(Id(uFLM), [], Return()), VarDecl(Id(YQY), StringType, None, Id(NbuI)), VarDecl(Id(VK), ArrayType([0.08, 79.37, 56.6], NumberType), None, NumLit(69.15)), VarDecl(Id(b4Z), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
dynamic im
func W4H ()
	return false
'''
		expect = '''Program([VarDecl(Id(im), None, dynamic, None), FuncDecl(Id(W4H), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
func GTEN ()	return
func PgOx (number NL[67.84], number Hl0M, bool Sun)
	return

func bSO (bool gfP)	return true

'''
		expect = '''Program([FuncDecl(Id(GTEN), [], Return()), FuncDecl(Id(PgOx), [VarDecl(Id(NL), ArrayType([67.84], NumberType), None, None), VarDecl(Id(Hl0M), NumberType, None, None), VarDecl(Id(Sun), BoolType, None, None)], Return()), FuncDecl(Id(bSO), [VarDecl(Id(gfP), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
func jfHr (number CM, bool df[12.68,11.55], number qkzA[37.6])
	return
func LYGH ()	return Dy
number qz
func tkgy ()
	return "kQ"

func yz ()	return
'''
		expect = '''Program([FuncDecl(Id(jfHr), [VarDecl(Id(CM), NumberType, None, None), VarDecl(Id(df), ArrayType([12.68, 11.55], BoolType), None, None), VarDecl(Id(qkzA), ArrayType([37.6], NumberType), None, None)], Return()), FuncDecl(Id(LYGH), [], Return(Id(Dy))), VarDecl(Id(qz), NumberType, None, None), FuncDecl(Id(tkgy), [], Return(StringLit(kQ))), FuncDecl(Id(yz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
string yPF <- LOK
func C6uT ()	return aDDk

string Dq[3.36,59.01,30.24]
'''
		expect = '''Program([VarDecl(Id(yPF), StringType, None, Id(LOK)), FuncDecl(Id(C6uT), [], Return(Id(aDDk))), VarDecl(Id(Dq), ArrayType([3.36, 59.01, 30.24], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 400))
