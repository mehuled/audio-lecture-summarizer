#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in

file = "transcript.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 10)


with open('summary.txt', 'w') as f:
	for sentence in summary:
	    print sentence
	    f.write(str(sentence)+"\n")

