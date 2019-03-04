import org.antlr.v4.runtime.*;

public class InfixTranslator {
    public static void main(String[] args) throws Exception {
        CharStream input = CharStreams.fromFileName("../input.txt");
        InfixLexer lexer = new InfixLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        InfixParser parser = new InfixParser(tokens);
        parser.prog(); // parse the input stream!
    };
}