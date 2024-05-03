# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u017a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\7,\u0117\n,")
        buf.write("\f,\16,\u011a\13,\3-\3-\5-\u011e\n-\3-\5-\u0121\n-\3.")
        buf.write("\6.\u0124\n.\r.\16.\u0125\3/\3/\7/\u012a\n/\f/\16/\u012d")
        buf.write("\13/\3\60\3\60\5\60\u0131\n\60\3\60\6\60\u0134\n\60\r")
        buf.write("\60\16\60\u0135\3\61\3\61\7\61\u013a\n\61\f\61\16\61\u013d")
        buf.write("\13\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\5\62\u0147")
        buf.write("\n\62\3\63\3\63\3\63\3\63\7\63\u014d\n\63\f\63\16\63\u0150")
        buf.write("\13\63\3\63\3\63\3\64\6\64\u0155\n\64\r\64\16\64\u0156")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\7\66\u0160\n\66\f")
        buf.write("\66\16\66\u0163\13\66\3\66\3\66\3\66\5\66\u0168\n\66\3")
        buf.write("\66\3\66\3\67\3\67\7\67\u016e\n\67\f\67\16\67\u0171\13")
        buf.write("\67\3\67\3\67\3\67\38\38\38\58\u0179\n8\2\29\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[\2]\2_\2a/c\2e\60g\61i\62k\63m\64o\2\3\2\21\3\2\f\f")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\60\60\4\2GGgg\4")
        buf.write("\2--//\3\2$$\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv\3\2)")
        buf.write(")\4\2\f\f\16\17\5\2\n\13\16\17\"\"\3\3\f\f\3\2\16\17\2")
        buf.write("\u0184\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\3q\3\2\2\2\5v\3\2\2\2\7|\3\2\2\2\t\u0083\3\2\2\2\13\u0088")
        buf.write("\3\2\2\2\r\u008f\3\2\2\2\17\u0096\3\2\2\2\21\u009a\3\2")
        buf.write("\2\2\23\u00a2\3\2\2\2\25\u00a7\3\2\2\2\27\u00ad\3\2\2")
        buf.write("\2\31\u00b0\3\2\2\2\33\u00b6\3\2\2\2\35\u00bf\3\2\2\2")
        buf.write("\37\u00c2\3\2\2\2!\u00c7\3\2\2\2#\u00cc\3\2\2\2%\u00d2")
        buf.write("\3\2\2\2\'\u00d6\3\2\2\2)\u00da\3\2\2\2+\u00de\3\2\2\2")
        buf.write("-\u00e1\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9")
        buf.write("\3\2\2\2\65\u00eb\3\2\2\2\67\u00ed\3\2\2\29\u00ef\3\2")
        buf.write("\2\2;\u00f1\3\2\2\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00fc\3\2\2\2E\u00fe\3\2\2\2G\u0101\3\2\2\2")
        buf.write("I\u0105\3\2\2\2K\u0108\3\2\2\2M\u010a\3\2\2\2O\u010c\3")
        buf.write("\2\2\2Q\u010e\3\2\2\2S\u0110\3\2\2\2U\u0112\3\2\2\2W\u0114")
        buf.write("\3\2\2\2Y\u011b\3\2\2\2[\u0123\3\2\2\2]\u0127\3\2\2\2")
        buf.write("_\u012e\3\2\2\2a\u0137\3\2\2\2c\u0146\3\2\2\2e\u0148\3")
        buf.write("\2\2\2g\u0154\3\2\2\2i\u015a\3\2\2\2k\u015d\3\2\2\2m\u016b")
        buf.write("\3\2\2\2o\u0178\3\2\2\2qr\7v\2\2rs\7t\2\2st\7w\2\2tu\7")
        buf.write("g\2\2u\4\3\2\2\2vw\7h\2\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z")
        buf.write("{\7g\2\2{\6\3\2\2\2|}\7p\2\2}~\7w\2\2~\177\7o\2\2\177")
        buf.write("\u0080\7d\2\2\u0080\u0081\7g\2\2\u0081\u0082\7t\2\2\u0082")
        buf.write("\b\3\2\2\2\u0083\u0084\7d\2\2\u0084\u0085\7q\2\2\u0085")
        buf.write("\u0086\7q\2\2\u0086\u0087\7n\2\2\u0087\n\3\2\2\2\u0088")
        buf.write("\u0089\7u\2\2\u0089\u008a\7v\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\u008c\7k\2\2\u008c\u008d\7p\2\2\u008d\u008e\7i\2\2\u008e")
        buf.write("\f\3\2\2\2\u008f\u0090\7t\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7w\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7p\2\2\u0095\16\3\2\2\2\u0096\u0097\7x\2\2\u0097")
        buf.write("\u0098\7c\2\2\u0098\u0099\7t\2\2\u0099\20\3\2\2\2\u009a")
        buf.write("\u009b\7f\2\2\u009b\u009c\7{\2\2\u009c\u009d\7p\2\2\u009d")
        buf.write("\u009e\7c\2\2\u009e\u009f\7o\2\2\u009f\u00a0\7k\2\2\u00a0")
        buf.write("\u00a1\7e\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6")
        buf.write("\24\3\2\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7n\2\2\u00ac")
        buf.write("\26\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af\7{\2\2\u00af")
        buf.write("\30\3\2\2\2\u00b0\u00b1\7d\2\2\u00b1\u00b2\7t\2\2\u00b2")
        buf.write("\u00b3\7g\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7m\2\2\u00b5")
        buf.write("\32\3\2\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8\7q\2\2\u00b8")
        buf.write("\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7k\2\2\u00bb")
        buf.write("\u00bc\7p\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\34\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7h\2\2\u00c1")
        buf.write("\36\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6 \3\2\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write("\u00cb\7h\2\2\u00cb\"\3\2\2\2\u00cc\u00cd\7d\2\2\u00cd")
        buf.write("\u00ce\7g\2\2\u00ce\u00cf\7i\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1$\3\2\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\u00d4\7p\2\2\u00d4\u00d5\7f\2\2\u00d5&\3\2\2\2\u00d6")
        buf.write("\u00d7\7p\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write("(\3\2\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\u00dd\7f\2\2\u00dd*\3\2\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7t\2\2\u00e0,\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2")
        buf.write("\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4.\3\2\2\2\u00e5")
        buf.write("\u00e6\7-\2\2\u00e6\60\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8")
        buf.write("\62\3\2\2\2\u00e9\u00ea\7,\2\2\u00ea\64\3\2\2\2\u00eb")
        buf.write("\u00ec\7\61\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\7\'\2\2\u00ee")
        buf.write("8\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0:\3\2\2\2\u00f1\u00f2")
        buf.write("\7>\2\2\u00f2\u00f3\7/\2\2\u00f3<\3\2\2\2\u00f4\u00f5")
        buf.write("\7#\2\2\u00f5\u00f6\7?\2\2\u00f6>\3\2\2\2\u00f7\u00f8")
        buf.write("\7>\2\2\u00f8@\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fbB\3\2\2\2\u00fc\u00fd\7@\2\2\u00fdD\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ff\u0100\7?\2\2\u0100F\3\2\2")
        buf.write("\2\u0101\u0102\7\60\2\2\u0102\u0103\7\60\2\2\u0103\u0104")
        buf.write("\7\60\2\2\u0104H\3\2\2\2\u0105\u0106\7?\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107J\3\2\2\2\u0108\u0109\7*\2\2\u0109L\3\2\2")
        buf.write("\2\u010a\u010b\7+\2\2\u010bN\3\2\2\2\u010c\u010d\7]\2")
        buf.write("\2\u010dP\3\2\2\2\u010e\u010f\7_\2\2\u010fR\3\2\2\2\u0110")
        buf.write("\u0111\7.\2\2\u0111T\3\2\2\2\u0112\u0113\t\2\2\2\u0113")
        buf.write("V\3\2\2\2\u0114\u0118\t\3\2\2\u0115\u0117\t\4\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119X\3\2\2\2\u011a\u0118\3\2\2")
        buf.write("\2\u011b\u011d\5[.\2\u011c\u011e\5]/\2\u011d\u011c\3\2")
        buf.write("\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u0121")
        buf.write("\5_\60\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("Z\3\2\2\2\u0122\u0124\t\5\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\\\3\2\2\2\u0127\u012b\t\6\2\2\u0128\u012a\t\5\2")
        buf.write("\2\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c^\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u0130\t\7\2\2\u012f\u0131\t\b\2\2\u0130")
        buf.write("\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2")
        buf.write("\u0132\u0134\t\5\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136`")
        buf.write("\3\2\2\2\u0137\u013b\t\t\2\2\u0138\u013a\5c\62\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\t\t\2\2\u013f\u0140\b\61\2\2\u0140")
        buf.write("b\3\2\2\2\u0141\u0147\n\n\2\2\u0142\u0143\7^\2\2\u0143")
        buf.write("\u0147\t\13\2\2\u0144\u0145\t\f\2\2\u0145\u0147\t\t\2")
        buf.write("\2\u0146\u0141\3\2\2\2\u0146\u0142\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0147d\3\2\2\2\u0148\u0149\7%\2\2\u0149\u014a")
        buf.write("\7%\2\2\u014a\u014e\3\2\2\2\u014b\u014d\n\r\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0152\b\63\3\2\u0152f\3\2\2\2\u0153\u0155")
        buf.write("\t\16\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\b\64\3\2\u0159h\3\2\2\2\u015a\u015b\13\2")
        buf.write("\2\2\u015b\u015c\b\65\4\2\u015cj\3\2\2\2\u015d\u0161\t")
        buf.write("\t\2\2\u015e\u0160\5c\62\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0167\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7\17\2")
        buf.write("\2\u0165\u0168\7\f\2\2\u0166\u0168\t\17\2\2\u0167\u0164")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016a\b\66\5\2\u016al\3\2\2\2\u016b\u016f\t\t\2\2\u016c")
        buf.write("\u016e\5c\62\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\3")
        buf.write("\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\5o8\2\u0173\u0174")
        buf.write("\b\67\6\2\u0174n\3\2\2\2\u0175\u0179\t\20\2\2\u0176\u0177")
        buf.write("\7^\2\2\u0177\u0179\n\13\2\2\u0178\u0175\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179p\3\2\2\2\22\2\u0118\u011d\u0120\u0125")
        buf.write("\u012b\u0130\u0135\u013b\u0146\u014e\u0156\u0161\u0167")
        buf.write("\u016f\u0178\7\3\61\2\b\2\2\3\65\3\3\66\4\3\67\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    UNTIL = 10
    BY = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    ELIF = 16
    BEGIN = 17
    END = 18
    NOT = 19
    AND = 20
    OR = 21
    FOR = 22
    PLUS = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE = 26
    MODULUS = 27
    EQUAL = 28
    ASSIGNINIT = 29
    NOTEQUAL = 30
    LESS = 31
    LESSEQUAL = 32
    GREATER = 33
    GREATEREQUAL = 34
    CONCAT = 35
    EQUALITY = 36
    LPAREN = 37
    RPAREN = 38
    LBRACKET = 39
    RBRACKET = 40
    COMMA = 41
    NEWLINE = 42
    ID = 43
    NUMBER_LIT = 44
    STRING_LIT = 45
    COMMENTS = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'until'", "'by'", "'break'", 
            "'continue'", "'if'", "'else'", "'elif'", "'begin'", "'end'", 
            "'not'", "'and'", "'or'", "'for'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
            "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "FOR", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", "EQUAL", "ASSIGNINIT", 
            "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
            "CONCAT", "EQUALITY", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
            "COMMA", "NEWLINE", "ID", "NUMBER_LIT", "STRING_LIT", "COMMENTS", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "FOR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", 
                  "EQUAL", "ASSIGNINIT", "NOTEQUAL", "LESS", "LESSEQUAL", 
                  "GREATER", "GREATEREQUAL", "CONCAT", "EQUALITY", "LPAREN", 
                  "RPAREN", "LBRACKET", "RBRACKET", "COMMA", "NEWLINE", 
                  "ID", "NUMBER_LIT", "INTP", "DECP", "EXPP", "STRING_LIT", 
                  "ALLOWEDCHAR", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ILLEGAL" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRING_LIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[1:])

     


