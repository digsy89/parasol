try:
  import importlib.resources as pkg_resources
except ImportError:
  import importlib_resources as pkg_resources


import sentencepiece as spm
from . import compose

class Tokenizer(object):

  def __init__(self, model="bpe", decompose=True):
    self.model = model
    self.decompose = decompose
    if decompose:
      self.composer = compose.Composer()

    self.spp = spm.SentencePieceProcessor()
    if decompose:
      with pkg_resources.path("parasol.resources.decomposed", 'bpe.model') as model:
        self.spp.load(model.as_posix())

  def tokenize(self, text):
    #print(text)
    decomposed = self.composer.decompose(text)
    #print(decomposed)
    tokens = self.spp.encode_as_pieces(decomposed)
    #print( ' / '.join( [ ''.join(t) for t in tokens ]))
    composed = [ self.composer.compose(t) for t in tokens ]
    #print( ' / '.join(composed))

    return composed

 
if __name__=="__main__":

  tknzr = Tokenizer(decompose=True)
  tknzr.tokenize("안녕하세요")
  tknzr.tokenize("집에 가고 싶다.")
  tknzr.tokenize("달이 기운 밤 퍼런빛이 스며든 골목을 걸어가던 길에 모퉁이에서 발이 엉켜 넘어져 그대로 좀 누워있었네")
