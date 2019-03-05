import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

public class InfixTranslator {
    public static void main(String[] args) throws Exception {
        CharStream input = CharStreams.fromFileName("../input.txt");
        InfixLexer lexer = new InfixLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        InfixParser parser = new InfixParser(tokens);
        InfixParser.ProgContext prog = parser.prog();// parse the input stream!

        ParseTreeWalker walker = new ParseTreeWalker();
        InfixListener listener = new InfixBaseListener();
        walker.walk(listener, prog);
    };
}