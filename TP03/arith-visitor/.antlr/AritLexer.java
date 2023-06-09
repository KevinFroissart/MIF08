// Generated from /home/etu/p2002504/Projets/mif08-2021/TP03/arith-visitor/Arit.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AritLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, SCOL=5, PLUS=6, MINUS=7, MULT=8, DIV=9, 
		ID=10, INT=11, COMMENT=12, NEWLINE=13, WS=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "SCOL", "PLUS", "MINUS", "MULT", "DIV", 
			"ID", "INT", "COMMENT", "NEWLINE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'set'", "'='", "'('", "')'", "';'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "SCOL", "PLUS", "MINUS", "MULT", "DIV", 
			"ID", "INT", "COMMENT", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public AritLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Arit.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20V\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3"+
		"\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\7\13\66\n"+
		"\13\f\13\16\139\13\13\3\f\6\f<\n\f\r\f\16\f=\3\r\3\r\7\rB\n\r\f\r\16\r"+
		"E\13\r\3\r\3\r\3\16\5\16J\n\16\3\16\3\16\3\16\3\16\3\17\6\17Q\n\17\r\17"+
		"\16\17R\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2\f"+
		"\f\17\17\4\2\13\13\"\"\2Z\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3"+
		"\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3"+
		"\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\63\3\2\2\2\27;\3\2\2\2\31?\3\2\2\2"+
		"\33I\3\2\2\2\35P\3\2\2\2\37 \7u\2\2 !\7g\2\2!\"\7v\2\2\"\4\3\2\2\2#$\7"+
		"?\2\2$\6\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2(\n\3\2\2\2)*\7=\2\2*\f"+
		"\3\2\2\2+,\7-\2\2,\16\3\2\2\2-.\7/\2\2.\20\3\2\2\2/\60\7,\2\2\60\22\3"+
		"\2\2\2\61\62\7\61\2\2\62\24\3\2\2\2\63\67\t\2\2\2\64\66\t\3\2\2\65\64"+
		"\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\26\3\2\2\29\67\3\2\2\2"+
		":<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\30\3\2\2\2?C\7%\2"+
		"\2@B\n\5\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2"+
		"\2FG\b\r\2\2G\32\3\2\2\2HJ\7\17\2\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\7"+
		"\f\2\2LM\3\2\2\2MN\b\16\2\2N\34\3\2\2\2OQ\t\6\2\2PO\3\2\2\2QR\3\2\2\2"+
		"RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\17\2\2U\36\3\2\2\2\b\2\67=CIR\3\b\2"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}