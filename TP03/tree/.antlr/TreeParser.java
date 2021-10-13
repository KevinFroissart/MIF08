// Generated from /home/etu/p2002504/Projets/mif08-2021/TP03/tree/Tree.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TreeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, INT=3, WS=4;
	public static final int
		RULE_int_tree_top = 0, RULE_int_tree = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"int_tree_top", "int_tree"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "INT", "WS"
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

	@Override
	public String getGrammarFileName() { return "Tree.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TreeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Int_tree_topContext extends ParserRuleContext {
		public Int_tree_topContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_tree_top; }
	 
		public Int_tree_topContext() { }
		public void copyFrom(Int_tree_topContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TopContext extends Int_tree_topContext {
		public Int_treeContext int_tree() {
			return getRuleContext(Int_treeContext.class,0);
		}
		public TerminalNode EOF() { return getToken(TreeParser.EOF, 0); }
		public TopContext(Int_tree_topContext ctx) { copyFrom(ctx); }
	}

	public final Int_tree_topContext int_tree_top() throws RecognitionException {
		Int_tree_topContext _localctx = new Int_tree_topContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_int_tree_top);
		try {
			_localctx = new TopContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			int_tree();
			setState(5);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Int_treeContext extends ParserRuleContext {
		public Int_treeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_tree; }
	 
		public Int_treeContext() { }
		public void copyFrom(Int_treeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NodeContext extends Int_treeContext {
		public TerminalNode INT() { return getToken(TreeParser.INT, 0); }
		public List<Int_treeContext> int_tree() {
			return getRuleContexts(Int_treeContext.class);
		}
		public Int_treeContext int_tree(int i) {
			return getRuleContext(Int_treeContext.class,i);
		}
		public NodeContext(Int_treeContext ctx) { copyFrom(ctx); }
	}
	public static class LeafContext extends Int_treeContext {
		public TerminalNode INT() { return getToken(TreeParser.INT, 0); }
		public LeafContext(Int_treeContext ctx) { copyFrom(ctx); }
	}

	public final Int_treeContext int_tree() throws RecognitionException {
		Int_treeContext _localctx = new Int_treeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_int_tree);
		int _la;
		try {
			setState(17);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				_localctx = new LeafContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(7);
				match(INT);
				}
				break;
			case T__0:
				_localctx = new NodeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(8);
				match(T__0);
				setState(9);
				match(INT);
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(10);
					int_tree();
					}
					}
					setState(13); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__0 || _la==INT );
				setState(15);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6\26\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\6\3\16\n\3\r\3\16\3\17\3\3\3\3\5\3\24"+
		"\n\3\3\3\2\2\4\2\4\2\2\2\25\2\6\3\2\2\2\4\23\3\2\2\2\6\7\5\4\3\2\7\b\7"+
		"\2\2\3\b\3\3\2\2\2\t\24\7\5\2\2\n\13\7\3\2\2\13\r\7\5\2\2\f\16\5\4\3\2"+
		"\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21"+
		"\22\7\4\2\2\22\24\3\2\2\2\23\t\3\2\2\2\23\n\3\2\2\2\24\5\3\2\2\2\4\17"+
		"\23";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}