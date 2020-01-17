try:
  import importlib.resources as pkg_resources
except ImportError:
  import importlib_resources as pkg_resources


import sentencepiece as spm
from . import compose

from parasol.resources import decomposed as decomposed_model
from parasol.resources import composed as composed_model

class Tokenizer(object):
  """Tokenize korean string

  Params
  ------
  decompose: bool
    If true, decompose -> tokenize -> compose. If false, just tokeinze
  """

  def __init__(self, decompose=True):
    self.decompose = decompose
    if decompose:
      self.composer = compose.Composer()

    # Load sentencepiece model
    self.spp = spm.SentencePieceProcessor()
    model_dir = decomposed_model if decompose else composed_model
    with pkg_resources.path(model_dir, 'bpe.model') as model:
      self.spp.load(model.as_posix())
    

  def tokenize(self, text):
    """Tokenize given text

    Inputs
    ------
    text: str
      String to be tokenized

    Outputs
    -------
    tokens: list(str)
    """
    processed_text = text.strip()
    if self.decompose:
      processed_text = self.composer.decompose(text)
    tokens = self.spp.encode_as_pieces(processed_text)
    if self.decompose:
      tokens = [ self.composer.compose(t) for t in tokens ]

    return tokens

 
if __name__=="__main__":

  tknzr = Tokenizer(decompose=True)
  tknzr.tokenize("안녕하세요")
  tknzr.tokenize("집에 가고 싶다.")
  tknzr.tokenize("달이 기운 밤 퍼런빛이 스며든 골목을 걸어가던 길에 모퉁이에서 발이 엉켜 넘어져 그대로 좀 누워있었네")
