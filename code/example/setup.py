import os
import zipfile
import gzip
import shutil
import numpy as np
import nltk
import fasttext
import gensim
import urllib.request
import networkx as nx
nltk.download('punkt') # one time execution
from nltk.tokenize import sent_tokenize
from lexrank import LexRank
from gensim.models.callbacks import CallbackAny2Vec
from summa.summarizer import summarize as summa_summarizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

example_text = """Mae Erthygl 25 o Ddatganiad Cyffredinol Hawliau Dynol 1948 y Cenhedloedd Unedig yn nodi: "Mae gan bawb yr hawl i safon byw sy'n ddigonol ar gyfer iechyd a lles ei hun a'i deulu, gan gynnwys bwyd, dillad, tai a gofal meddygol a gwasanaethau cymdeithasol angenrheidiol. "Mae'r Datganiad Cyffredinol yn cynnwys lletyaeth er mwyn diogelu person ac mae hefyd yn sôn yn arbennig am y gofal a roddir i'r rheini sydd mewn mamolaeth neu blentyndod. Ystyrir mai Datganiad Cyffredinol o Hawliau Dynol fel y datganiad rhyngwladol cyntaf o hawliau dynol sylfaenol. Dywedodd Uchel Gomisiynydd y Cenhedloedd Unedig dros Hawliau Dynol Navanethem Pillay fod y Datganiad Cyffredinol o Hawliau Dynol "yn ymgorffori gweledigaeth sy'n gofyn am gymryd yr holl hawliau dynol - sifil, gwleidyddol, economaidd, cymdeithasol neu ddiwylliannol - fel cyfanwaith anwahanadwy ac organig, anwahanadwy a rhyngddibynnol."""
example_summary = """Mae Datganiad Cyffredinol Hawliau Dynol 1948 yn dweud bod gan bawb yr hawl i safon byw digonol. Mae hynny yn cynnwys mynediad at fwyd a dillad a gofal meddygol i bob unigolyn. Dyma’r datganiad cyntaf o hawliau dynol"""

## Define summarizer models
          
# bottomline: return 1st sentence
def first_sent_summarize(article):
  return sent_tokenize(article)[0]

# lex_rank
def lex_rank_summarize(article):
  sentences = sent_tokenize(article)
  summary = LexRank(sentences).get_summary(sentences,
                              summary_size=int(len(sentences)/2), threshold=.1)
  return "\n".join(summary)

# text_rank
def text_rank_summarize(article):
  return summa_summarizer(article, ratio=0.5) #text

## Define Topline summarizers

def tfidf_summarize(article, ratio=0.5):
  sentences = sent_tokenize(article)
  # get similarity matrix
  sim_mat = cosine_similarity(TfidfVectorizer().fit_transform(sentences))
  scores = nx.pagerank_numpy(nx.from_numpy_array(sim_mat))
  top_ranked = sorted(scores.items(), key=lambda x: x[1], 
                      reverse=True)[:int(len(scores)*ratio)]
  summary = [sentences[i] for i,_ in top_ranked]
  return "\n".join(summary)

# generate sentence vectors
def getSentenceVectors(embeddings, sents) -> list:
  sent_vectors = []
  for sent in sents:
    if len(sent) != 0:
      vecs = []
      for w in sent.split():
        try:
          vecs.append(embeddings[w])
        except AttributeError:
          vecs.append(np.zeros((300,)))
      sent_vectors.append(np.mean(vecs, axis=0).reshape(1,300))
  return sent_vectors
  
def embed_summarize(article, embedding, ratio=0.5):  
  sentences = sent_tokenize(article)
  sentence_vectors = getSentenceVectors(embedding, sentences)
  nx_graph = nx.from_numpy_array(gen_similarity_matrix(sentence_vectors))
  scores = nx.pagerank_numpy(nx_graph)
  ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
  return "\n".join([s for _, s in ranked_sentences[:int(len(ranked_sentences)*ratio)]])

# build similarity matrix
def gen_similarity_matrix(sents):
  sim_mat = np.zeros([len(sents), len(sents)])
  for i in range(len(sents)):
    for j in range(len(sents)):
      if i != j:
        sim_mat[i][j] = float(cosine_similarity(sents[i], sents[j]))
        # sim_mat[i][j] = float(cosine_similarity(sents[i].reshape(1,300),
        #                                         sents[j].reshape(1,300)))
  return sim_mat

class EpochLogger(CallbackAny2Vec):
    """
    Callback to log information about training

    ** THIS MUST BE DEFINED BEFORE BEING ABLE TO LOAD IN MODELS **
    """
    def __init__(self):
        self.epoch = 0

    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1

# Unzipping files
def unzip(zipfilename):
  try:
    if zipfilename.endswith(".zip"):
      with zipfile.ZipFile(zipfilename, 'r') as zip_ref:
        zip_ref.extractall(zipfilename[:-4])
        print(f"'{zipfilename}' unzipped!")
    elif zipfilename.endswith(".gz"):
      with gzip.open(zipfilename, 'rb') as f_in:
        with open(zipfilename[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    else:
      print(f"Invalid file name: {zipfilename}! Must be a '.zip' or a '.gz'")
    os.remove(zipfilename)
  except FileNotFoundError:
    print(f"Cannot find '{zipfilename}' file")
