// Generated from /home/etu/p2002504/Projets/mif08-2021/MiniC/MiniC.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiniCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OR=1, AND=2, EQ=3, NEQ=4, GT=5, LT=6, GTEQ=7, LTEQ=8, PLUS=9, MINUS=10, 
		MULT=11, DIV=12, MOD=13, NOT=14, COL=15, SCOL=16, COM=17, ASSIGN=18, OPAR=19, 
		CPAR=20, OBRACE=21, CBRACE=22, TRUE=23, FALSE=24, IF=25, ELSE=26, WHILE=27, 
		RETURN=28, PRINTLN_INT=29, PRINTLN_STRING=30, PRINTLN_FLOAT=31, INTTYPE=32, 
		FLOATTYPE=33, STRINGTYPE=34, BOOLTYPE=35, ID=36, INT=37, FLOAT=38, STRING=39, 
		COMMENT=40, SPACE=41;
	public static final int
		RULE_prog = 0, RULE_function = 1, RULE_vardecl_l = 2, RULE_vardecl = 3, 
		RULE_id_l = 4, RULE_block = 5, RULE_stat = 6, RULE_assignment = 7, RULE_if_stat = 8, 
		RULE_stat_block = 9, RULE_while_stat = 10, RULE_print_stat = 11, RULE_expr_l = 12, 
		RULE_expr = 13, RULE_atom = 14, RULE_typee = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "function", "vardecl_l", "vardecl", "id_l", "block", "stat", 
			"assignment", "if_stat", "stat_block", "while_stat", "print_stat", "expr_l", 
			"expr", "atom", "typee"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'||'", "'&&'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'!'", "':'", "';'", "','", "'='", "'('", 
			"')'", "'{'", "'}'", "'true'", "'false'", "'if'", "'else'", "'while'", 
			"'return'", "'println_int'", "'println_string'", "'println_float'", "'int'", 
			"'float'", "'string'", "'bool'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OR", "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", "MINUS", 
			"MULT", "DIV", "MOD", "NOT", "COL", "SCOL", "COM", "ASSIGN", "OPAR", 
			"CPAR", "OBRACE", "CBRACE", "TRUE", "FALSE", "IF", "ELSE", "WHILE", "RETURN", 
			"PRINTLN_INT", "PRINTLN_STRING", "PRINTLN_FLOAT", "INTTYPE", "FLOATTYPE", 
			"STRINGTYPE", "BOOLTYPE", "ID", "INT", "FLOAT", "STRING", "COMMENT", 
			"SPACE"
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
	public String getGrammarFileName() { return "MiniC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	 
		public ProgContext() { }
		public void copyFrom(ProgContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ProgRuleContext extends ProgContext {
		public TerminalNode EOF() { return getToken(MiniCParser.EOF, 0); }
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgRuleContext(ProgContext ctx) { copyFrom(ctx); }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			_localctx = new ProgRuleContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==INTTYPE) {
				{
				{
				setState(32);
				function();
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
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

	public static class FunctionContext extends ParserRuleContext {
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	 
		public FunctionContext() { }
		public void copyFrom(FunctionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FuncDeclContext extends FunctionContext {
		public TerminalNode INTTYPE() { return getToken(MiniCParser.INTTYPE, 0); }
		public TerminalNode ID() { return getToken(MiniCParser.ID, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public TerminalNode OBRACE() { return getToken(MiniCParser.OBRACE, 0); }
		public Vardecl_lContext vardecl_l() {
			return getRuleContext(Vardecl_lContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RETURN() { return getToken(MiniCParser.RETURN, 0); }
		public TerminalNode INT() { return getToken(MiniCParser.INT, 0); }
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public TerminalNode CBRACE() { return getToken(MiniCParser.CBRACE, 0); }
		public FuncDeclContext(FunctionContext ctx) { copyFrom(ctx); }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		try {
			_localctx = new FuncDeclContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(INTTYPE);
			setState(41);
			match(ID);
			setState(42);
			match(OPAR);
			setState(43);
			match(CPAR);
			setState(44);
			match(OBRACE);
			setState(45);
			vardecl_l();
			setState(46);
			block();
			setState(47);
			match(RETURN);
			setState(48);
			match(INT);
			setState(49);
			match(SCOL);
			setState(50);
			match(CBRACE);
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

	public static class Vardecl_lContext extends ParserRuleContext {
		public Vardecl_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl_l; }
	 
		public Vardecl_lContext() { }
		public void copyFrom(Vardecl_lContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VarDeclListContext extends Vardecl_lContext {
		public List<VardeclContext> vardecl() {
			return getRuleContexts(VardeclContext.class);
		}
		public VardeclContext vardecl(int i) {
			return getRuleContext(VardeclContext.class,i);
		}
		public VarDeclListContext(Vardecl_lContext ctx) { copyFrom(ctx); }
	}

	public final Vardecl_lContext vardecl_l() throws RecognitionException {
		Vardecl_lContext _localctx = new Vardecl_lContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vardecl_l);
		int _la;
		try {
			_localctx = new VarDeclListContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTTYPE) | (1L << FLOATTYPE) | (1L << STRINGTYPE) | (1L << BOOLTYPE))) != 0)) {
				{
				{
				setState(52);
				vardecl();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class VardeclContext extends ParserRuleContext {
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
	 
		public VardeclContext() { }
		public void copyFrom(VardeclContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VarDeclContext extends VardeclContext {
		public TypeeContext typee() {
			return getRuleContext(TypeeContext.class,0);
		}
		public Id_lContext id_l() {
			return getRuleContext(Id_lContext.class,0);
		}
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public VarDeclContext(VardeclContext ctx) { copyFrom(ctx); }
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vardecl);
		try {
			_localctx = new VarDeclContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			typee();
			setState(59);
			id_l();
			setState(60);
			match(SCOL);
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

	public static class Id_lContext extends ParserRuleContext {
		public Id_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_l; }
	 
		public Id_lContext() { }
		public void copyFrom(Id_lContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IdListBaseContext extends Id_lContext {
		public TerminalNode ID() { return getToken(MiniCParser.ID, 0); }
		public IdListBaseContext(Id_lContext ctx) { copyFrom(ctx); }
	}
	public static class IdListContext extends Id_lContext {
		public TerminalNode ID() { return getToken(MiniCParser.ID, 0); }
		public TerminalNode COM() { return getToken(MiniCParser.COM, 0); }
		public Id_lContext id_l() {
			return getRuleContext(Id_lContext.class,0);
		}
		public IdListContext(Id_lContext ctx) { copyFrom(ctx); }
	}

	public final Id_lContext id_l() throws RecognitionException {
		Id_lContext _localctx = new Id_lContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_id_l);
		try {
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new IdListBaseContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(62);
				match(ID);
				}
				break;
			case 2:
				_localctx = new IdListContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				match(ID);
				setState(64);
				match(COM);
				setState(65);
				id_l();
				}
				break;
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

	public static class BlockContext extends ParserRuleContext {
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	 
		public BlockContext() { }
		public void copyFrom(BlockContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StatListContext extends BlockContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public StatListContext(BlockContext ctx) { copyFrom(ctx); }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		int _la;
		try {
			_localctx = new StatListContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << WHILE) | (1L << PRINTLN_INT) | (1L << PRINTLN_STRING) | (1L << PRINTLN_FLOAT) | (1L << ID))) != 0)) {
				{
				{
				setState(68);
				stat();
				}
				}
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class StatContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public If_statContext if_stat() {
			return getRuleContext(If_statContext.class,0);
		}
		public While_statContext while_stat() {
			return getRuleContext(While_statContext.class,0);
		}
		public Print_statContext print_stat() {
			return getRuleContext(Print_statContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_stat);
		try {
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				assignment();
				setState(75);
				match(SCOL);
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				if_stat();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 3);
				{
				setState(78);
				while_stat();
				}
				break;
			case PRINTLN_INT:
			case PRINTLN_STRING:
			case PRINTLN_FLOAT:
				enterOuterAlt(_localctx, 4);
				{
				setState(79);
				print_stat();
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

	public static class AssignmentContext extends ParserRuleContext {
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	 
		public AssignmentContext() { }
		public void copyFrom(AssignmentContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignStatContext extends AssignmentContext {
		public TerminalNode ID() { return getToken(MiniCParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(MiniCParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignStatContext(AssignmentContext ctx) { copyFrom(ctx); }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignment);
		try {
			_localctx = new AssignStatContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(ID);
			setState(83);
			match(ASSIGN);
			setState(84);
			expr(0);
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

	public static class If_statContext extends ParserRuleContext {
		public If_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stat; }
	 
		public If_statContext() { }
		public void copyFrom(If_statContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IfStatContext extends If_statContext {
		public Stat_blockContext then_block;
		public Stat_blockContext else_block;
		public TerminalNode IF() { return getToken(MiniCParser.IF, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public List<Stat_blockContext> stat_block() {
			return getRuleContexts(Stat_blockContext.class);
		}
		public Stat_blockContext stat_block(int i) {
			return getRuleContext(Stat_blockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MiniCParser.ELSE, 0); }
		public IfStatContext(If_statContext ctx) { copyFrom(ctx); }
	}

	public final If_statContext if_stat() throws RecognitionException {
		If_statContext _localctx = new If_statContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_if_stat);
		try {
			_localctx = new IfStatContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(IF);
			setState(87);
			match(OPAR);
			setState(88);
			expr(0);
			setState(89);
			match(CPAR);
			setState(90);
			((IfStatContext)_localctx).then_block = stat_block();
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(91);
				match(ELSE);
				setState(92);
				((IfStatContext)_localctx).else_block = stat_block();
				}
				break;
			}
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

	public static class Stat_blockContext extends ParserRuleContext {
		public TerminalNode OBRACE() { return getToken(MiniCParser.OBRACE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode CBRACE() { return getToken(MiniCParser.CBRACE, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public Stat_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat_block; }
	}

	public final Stat_blockContext stat_block() throws RecognitionException {
		Stat_blockContext _localctx = new Stat_blockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_stat_block);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OBRACE:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				match(OBRACE);
				setState(96);
				block();
				setState(97);
				match(CBRACE);
				}
				break;
			case IF:
			case WHILE:
			case PRINTLN_INT:
			case PRINTLN_STRING:
			case PRINTLN_FLOAT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				stat();
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

	public static class While_statContext extends ParserRuleContext {
		public While_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stat; }
	 
		public While_statContext() { }
		public void copyFrom(While_statContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class WhileStatContext extends While_statContext {
		public TerminalNode WHILE() { return getToken(MiniCParser.WHILE, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public Stat_blockContext stat_block() {
			return getRuleContext(Stat_blockContext.class,0);
		}
		public WhileStatContext(While_statContext ctx) { copyFrom(ctx); }
	}

	public final While_statContext while_stat() throws RecognitionException {
		While_statContext _localctx = new While_statContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_while_stat);
		try {
			_localctx = new WhileStatContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(WHILE);
			setState(103);
			match(OPAR);
			setState(104);
			expr(0);
			setState(105);
			match(CPAR);
			setState(106);
			stat_block();
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

	public static class Print_statContext extends ParserRuleContext {
		public Print_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stat; }
	 
		public Print_statContext() { }
		public void copyFrom(Print_statContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintlnintStatContext extends Print_statContext {
		public TerminalNode PRINTLN_INT() { return getToken(MiniCParser.PRINTLN_INT, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public PrintlnintStatContext(Print_statContext ctx) { copyFrom(ctx); }
	}
	public static class PrintlnstringStatContext extends Print_statContext {
		public TerminalNode PRINTLN_STRING() { return getToken(MiniCParser.PRINTLN_STRING, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public PrintlnstringStatContext(Print_statContext ctx) { copyFrom(ctx); }
	}
	public static class PrintlnfloatStatContext extends Print_statContext {
		public TerminalNode PRINTLN_FLOAT() { return getToken(MiniCParser.PRINTLN_FLOAT, 0); }
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public TerminalNode SCOL() { return getToken(MiniCParser.SCOL, 0); }
		public PrintlnfloatStatContext(Print_statContext ctx) { copyFrom(ctx); }
	}

	public final Print_statContext print_stat() throws RecognitionException {
		Print_statContext _localctx = new Print_statContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_print_stat);
		try {
			setState(126);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINTLN_INT:
				_localctx = new PrintlnintStatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				match(PRINTLN_INT);
				setState(109);
				match(OPAR);
				setState(110);
				expr(0);
				setState(111);
				match(CPAR);
				setState(112);
				match(SCOL);
				}
				break;
			case PRINTLN_FLOAT:
				_localctx = new PrintlnfloatStatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(114);
				match(PRINTLN_FLOAT);
				setState(115);
				match(OPAR);
				setState(116);
				expr(0);
				setState(117);
				match(CPAR);
				setState(118);
				match(SCOL);
				}
				break;
			case PRINTLN_STRING:
				_localctx = new PrintlnstringStatContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(120);
				match(PRINTLN_STRING);
				setState(121);
				match(OPAR);
				setState(122);
				expr(0);
				setState(123);
				match(CPAR);
				setState(124);
				match(SCOL);
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

	public static class Expr_lContext extends ParserRuleContext {
		public Expr_lContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_l; }
	 
		public Expr_lContext() { }
		public void copyFrom(Expr_lContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprListBaseContext extends Expr_lContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprListBaseContext(Expr_lContext ctx) { copyFrom(ctx); }
	}
	public static class ExprListContext extends Expr_lContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COM() { return getToken(MiniCParser.COM, 0); }
		public Expr_lContext expr_l() {
			return getRuleContext(Expr_lContext.class,0);
		}
		public ExprListContext(Expr_lContext ctx) { copyFrom(ctx); }
	}
	public static class ExprListEmptyContext extends Expr_lContext {
		public ExprListEmptyContext(Expr_lContext ctx) { copyFrom(ctx); }
	}

	public final Expr_lContext expr_l() throws RecognitionException {
		Expr_lContext _localctx = new Expr_lContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expr_l);
		try {
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				_localctx = new ExprListEmptyContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case 2:
				_localctx = new ExprListBaseContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(129);
				expr(0);
				}
				break;
			case 3:
				_localctx = new ExprListContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(130);
				expr(0);
				setState(131);
				match(COM);
				setState(132);
				expr_l();
				}
				break;
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

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class NotExprContext extends ExprContext {
		public TerminalNode NOT() { return getToken(MiniCParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class UnaryMinusExprContext extends ExprContext {
		public TerminalNode MINUS() { return getToken(MiniCParser.MINUS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public UnaryMinusExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AtomExprContext extends ExprContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public AtomExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class OrExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OR() { return getToken(MiniCParser.OR, 0); }
		public OrExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AdditiveExprContext extends ExprContext {
		public Token myop;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(MiniCParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(MiniCParser.MINUS, 0); }
		public AdditiveExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class RelationalExprContext extends ExprContext {
		public Token myop;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode GT() { return getToken(MiniCParser.GT, 0); }
		public TerminalNode LT() { return getToken(MiniCParser.LT, 0); }
		public TerminalNode GTEQ() { return getToken(MiniCParser.GTEQ, 0); }
		public TerminalNode LTEQ() { return getToken(MiniCParser.LTEQ, 0); }
		public RelationalExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MultiplicativeExprContext extends ExprContext {
		public Token myop;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULT() { return getToken(MiniCParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(MiniCParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(MiniCParser.MOD, 0); }
		public MultiplicativeExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class EqualityExprContext extends ExprContext {
		public Token myop;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(MiniCParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(MiniCParser.NEQ, 0); }
		public EqualityExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AndExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode AND() { return getToken(MiniCParser.AND, 0); }
		public AndExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				{
				_localctx = new UnaryMinusExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(137);
				match(MINUS);
				setState(138);
				expr(9);
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(139);
				match(NOT);
				setState(140);
				expr(8);
				}
				break;
			case OPAR:
			case TRUE:
			case FALSE:
			case ID:
			case INT:
			case FLOAT:
			case STRING:
				{
				_localctx = new AtomExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(141);
				atom();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(164);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(162);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new MultiplicativeExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(144);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(145);
						((MultiplicativeExprContext)_localctx).myop = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MULT) | (1L << DIV) | (1L << MOD))) != 0)) ) {
							((MultiplicativeExprContext)_localctx).myop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(146);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new AdditiveExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(147);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(148);
						((AdditiveExprContext)_localctx).myop = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((AdditiveExprContext)_localctx).myop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(149);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new RelationalExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(150);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(151);
						((RelationalExprContext)_localctx).myop = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GT) | (1L << LT) | (1L << GTEQ) | (1L << LTEQ))) != 0)) ) {
							((RelationalExprContext)_localctx).myop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(152);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new EqualityExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(153);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(154);
						((EqualityExprContext)_localctx).myop = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==EQ || _la==NEQ) ) {
							((EqualityExprContext)_localctx).myop = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(155);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new AndExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(156);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(157);
						match(AND);
						setState(158);
						expr(4);
						}
						break;
					case 6:
						{
						_localctx = new OrExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(159);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(160);
						match(OR);
						setState(161);
						expr(3);
						}
						break;
					}
					} 
				}
				setState(166);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	 
		public AtomContext() { }
		public void copyFrom(AtomContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParExprContext extends AtomContext {
		public TerminalNode OPAR() { return getToken(MiniCParser.OPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CPAR() { return getToken(MiniCParser.CPAR, 0); }
		public ParExprContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class BooleanAtomContext extends AtomContext {
		public TerminalNode TRUE() { return getToken(MiniCParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(MiniCParser.FALSE, 0); }
		public BooleanAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class IdAtomContext extends AtomContext {
		public TerminalNode ID() { return getToken(MiniCParser.ID, 0); }
		public IdAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class FloatAtomContext extends AtomContext {
		public TerminalNode FLOAT() { return getToken(MiniCParser.FLOAT, 0); }
		public FloatAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class IntAtomContext extends AtomContext {
		public TerminalNode INT() { return getToken(MiniCParser.INT, 0); }
		public IntAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}
	public static class StringAtomContext extends AtomContext {
		public TerminalNode STRING() { return getToken(MiniCParser.STRING, 0); }
		public StringAtomContext(AtomContext ctx) { copyFrom(ctx); }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_atom);
		int _la;
		try {
			setState(176);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPAR:
				_localctx = new ParExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(OPAR);
				setState(168);
				expr(0);
				setState(169);
				match(CPAR);
				}
				break;
			case INT:
				_localctx = new IntAtomContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(171);
				match(INT);
				}
				break;
			case FLOAT:
				_localctx = new FloatAtomContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(172);
				match(FLOAT);
				}
				break;
			case TRUE:
			case FALSE:
				_localctx = new BooleanAtomContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(173);
				_la = _input.LA(1);
				if ( !(_la==TRUE || _la==FALSE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case ID:
				_localctx = new IdAtomContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(174);
				match(ID);
				}
				break;
			case STRING:
				_localctx = new StringAtomContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(175);
				match(STRING);
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

	public static class TypeeContext extends ParserRuleContext {
		public TypeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typee; }
	 
		public TypeeContext() { }
		public void copyFrom(TypeeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BasicTypeContext extends TypeeContext {
		public Token mytype;
		public TerminalNode INTTYPE() { return getToken(MiniCParser.INTTYPE, 0); }
		public TerminalNode FLOATTYPE() { return getToken(MiniCParser.FLOATTYPE, 0); }
		public TerminalNode BOOLTYPE() { return getToken(MiniCParser.BOOLTYPE, 0); }
		public TerminalNode STRINGTYPE() { return getToken(MiniCParser.STRINGTYPE, 0); }
		public BasicTypeContext(TypeeContext ctx) { copyFrom(ctx); }
	}

	public final TypeeContext typee() throws RecognitionException {
		TypeeContext _localctx = new TypeeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_typee);
		int _la;
		try {
			_localctx = new BasicTypeContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			((BasicTypeContext)_localctx).mytype = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTTYPE) | (1L << FLOATTYPE) | (1L << STRINGTYPE) | (1L << BOOLTYPE))) != 0)) ) {
				((BasicTypeContext)_localctx).mytype = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 4);
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+\u00b7\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n"+
		"\2\f\2\16\2\'\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\4\7\48\n\4\f\4\16\4;\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6E"+
		"\n\6\3\7\7\7H\n\7\f\7\16\7K\13\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bS\n\b\3\t"+
		"\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n`\n\n\3\13\3\13\3\13\3\13"+
		"\3\13\5\13g\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0081\n\r\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\5\16\u0089\n\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0091"+
		"\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\7\17\u00a5\n\17\f\17\16\17\u00a8\13\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00b3\n\20\3\21\3\21\3\21"+
		"\2\3\34\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\b\3\2\r\17\3\2\13"+
		"\f\3\2\7\n\3\2\5\6\3\2\31\32\3\2\"%\2\u00c0\2%\3\2\2\2\4*\3\2\2\2\69\3"+
		"\2\2\2\b<\3\2\2\2\nD\3\2\2\2\fI\3\2\2\2\16R\3\2\2\2\20T\3\2\2\2\22X\3"+
		"\2\2\2\24f\3\2\2\2\26h\3\2\2\2\30\u0080\3\2\2\2\32\u0088\3\2\2\2\34\u0090"+
		"\3\2\2\2\36\u00b2\3\2\2\2 \u00b4\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2$\'\3\2"+
		"\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\2\2\3)\3\3\2\2\2*+\7"+
		"\"\2\2+,\7&\2\2,-\7\25\2\2-.\7\26\2\2./\7\27\2\2/\60\5\6\4\2\60\61\5\f"+
		"\7\2\61\62\7\36\2\2\62\63\7\'\2\2\63\64\7\22\2\2\64\65\7\30\2\2\65\5\3"+
		"\2\2\2\668\5\b\5\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\7\3"+
		"\2\2\2;9\3\2\2\2<=\5 \21\2=>\5\n\6\2>?\7\22\2\2?\t\3\2\2\2@E\7&\2\2AB"+
		"\7&\2\2BC\7\23\2\2CE\5\n\6\2D@\3\2\2\2DA\3\2\2\2E\13\3\2\2\2FH\5\16\b"+
		"\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\r\3\2\2\2KI\3\2\2\2LM\5\20"+
		"\t\2MN\7\22\2\2NS\3\2\2\2OS\5\22\n\2PS\5\26\f\2QS\5\30\r\2RL\3\2\2\2R"+
		"O\3\2\2\2RP\3\2\2\2RQ\3\2\2\2S\17\3\2\2\2TU\7&\2\2UV\7\24\2\2VW\5\34\17"+
		"\2W\21\3\2\2\2XY\7\33\2\2YZ\7\25\2\2Z[\5\34\17\2[\\\7\26\2\2\\_\5\24\13"+
		"\2]^\7\34\2\2^`\5\24\13\2_]\3\2\2\2_`\3\2\2\2`\23\3\2\2\2ab\7\27\2\2b"+
		"c\5\f\7\2cd\7\30\2\2dg\3\2\2\2eg\5\16\b\2fa\3\2\2\2fe\3\2\2\2g\25\3\2"+
		"\2\2hi\7\35\2\2ij\7\25\2\2jk\5\34\17\2kl\7\26\2\2lm\5\24\13\2m\27\3\2"+
		"\2\2no\7\37\2\2op\7\25\2\2pq\5\34\17\2qr\7\26\2\2rs\7\22\2\2s\u0081\3"+
		"\2\2\2tu\7!\2\2uv\7\25\2\2vw\5\34\17\2wx\7\26\2\2xy\7\22\2\2y\u0081\3"+
		"\2\2\2z{\7 \2\2{|\7\25\2\2|}\5\34\17\2}~\7\26\2\2~\177\7\22\2\2\177\u0081"+
		"\3\2\2\2\u0080n\3\2\2\2\u0080t\3\2\2\2\u0080z\3\2\2\2\u0081\31\3\2\2\2"+
		"\u0082\u0089\3\2\2\2\u0083\u0089\5\34\17\2\u0084\u0085\5\34\17\2\u0085"+
		"\u0086\7\23\2\2\u0086\u0087\5\32\16\2\u0087\u0089\3\2\2\2\u0088\u0082"+
		"\3\2\2\2\u0088\u0083\3\2\2\2\u0088\u0084\3\2\2\2\u0089\33\3\2\2\2\u008a"+
		"\u008b\b\17\1\2\u008b\u008c\7\f\2\2\u008c\u0091\5\34\17\13\u008d\u008e"+
		"\7\20\2\2\u008e\u0091\5\34\17\n\u008f\u0091\5\36\20\2\u0090\u008a\3\2"+
		"\2\2\u0090\u008d\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u00a6\3\2\2\2\u0092"+
		"\u0093\f\t\2\2\u0093\u0094\t\2\2\2\u0094\u00a5\5\34\17\n\u0095\u0096\f"+
		"\b\2\2\u0096\u0097\t\3\2\2\u0097\u00a5\5\34\17\t\u0098\u0099\f\7\2\2\u0099"+
		"\u009a\t\4\2\2\u009a\u00a5\5\34\17\b\u009b\u009c\f\6\2\2\u009c\u009d\t"+
		"\5\2\2\u009d\u00a5\5\34\17\7\u009e\u009f\f\5\2\2\u009f\u00a0\7\4\2\2\u00a0"+
		"\u00a5\5\34\17\6\u00a1\u00a2\f\4\2\2\u00a2\u00a3\7\3\2\2\u00a3\u00a5\5"+
		"\34\17\5\u00a4\u0092\3\2\2\2\u00a4\u0095\3\2\2\2\u00a4\u0098\3\2\2\2\u00a4"+
		"\u009b\3\2\2\2\u00a4\u009e\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a5\u00a8\3\2"+
		"\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\35\3\2\2\2\u00a8\u00a6"+
		"\3\2\2\2\u00a9\u00aa\7\25\2\2\u00aa\u00ab\5\34\17\2\u00ab\u00ac\7\26\2"+
		"\2\u00ac\u00b3\3\2\2\2\u00ad\u00b3\7\'\2\2\u00ae\u00b3\7(\2\2\u00af\u00b3"+
		"\t\6\2\2\u00b0\u00b3\7&\2\2\u00b1\u00b3\7)\2\2\u00b2\u00a9\3\2\2\2\u00b2"+
		"\u00ad\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2"+
		"\2\2\u00b2\u00b1\3\2\2\2\u00b3\37\3\2\2\2\u00b4\u00b5\t\7\2\2\u00b5!\3"+
		"\2\2\2\17%9DIR_f\u0080\u0088\u0090\u00a4\u00a6\u00b2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}