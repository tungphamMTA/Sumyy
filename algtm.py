import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer

import nltk
nltk.download('punkt')




############################# LexRankSummarizer ###########################################
def lexrank_extract_sum(text, sentences_count):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))

  lex_rank_summarizer = LexRankSummarizer()
  lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=sentences_count)
  result = ""
  for sentence in lexrank_summary:
    result += "\n\u2022\r"
    result += str(sentence)
  return result 

############################# LexRankSummarizer ###########################################
def lexrank_extract_sum(text, sentences_count):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))

  lex_rank_summarizer = LexRankSummarizer()
  lexrank_summary = lex_rank_summarizer(my_parser.document,sentences_count=sentences_count)
  result = ""
  for sentence in lexrank_summary:
    result += "\n\u2022\r"
    result += str(sentence)
  return result 


############################# LsaSummarizer ##############################################
def lsa_extract_sum(text, sentences_count):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))
  lsa_summarizer=LsaSummarizer()
  lsa_summary= lsa_summarizer(my_parser.document,sentences_count=sentences_count)
  result = ""
  for sentence in lsa_summary:
    result += "\n\u2022\r"
    result += str(sentence)
  return result         #' '.join(text for text in lsa_summary)


############################### LuhnSummarizer ###########################################
def luhn_text_sum(text, sentences_count):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))
  luhn_summarizer=LuhnSummarizer()
  luhn_summary=luhn_summarizer(my_parser.document,sentences_count=sentences_count)
  result = ""
  for sentence in luhn_summary:
    result += "\n\u2022\r"
    result += str(sentence)
  return result 
############################# KLSummarizer ##############################################
def kl_extract_sum(text,sentences_count ):
  my_parser = PlaintextParser.from_string(text,Tokenizer('english'))
  kl_summarizer=KLSummarizer()
  kl_summary=kl_summarizer(my_parser.document,sentences_count=sentences_count)
  result = ""
  for sentence in kl_summary:
    result += "\n\u2022\r"
    result += str(sentence)
  return result 
