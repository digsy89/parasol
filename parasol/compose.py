from transitions import Machine
import hgtk

CONSONANT = 0 # 자음
VOWEL = 1 # 모음
EXCEPT = 2 # 그 외

def check_jamo(c):
  """ Check whether chracter is consonant or vowel

  Input
  -----
  c : str
    Chracter
  """

  # ㄱ ~ ㅎ
  if 12593 <= ord(c) <= 12622:
    return CONSONANT
  # ㅏ ~ 
  elif 12623 <= ord(c) <= 12643:
    return VOWEL
  else:
    return EXCEPT 


class Composer:

  # 0 is consonant. 1 is vowel.
  states = ["empty", "0", "01", "010"]

  def __init__(self):
    self.machine = Machine(model=self, states=Composer.states, initial='empty')
    self.buffer = []
    self.result = []

    # State = empty
    self.machine.add_transition("get_consonant", "empty", "0", after="collect")
    self.machine.add_transition("get_vowel"    , "empty", "empty", after="pass_char")
    self.machine.add_transition("get_except"   , "empty", "empty", after="pass_char")

    # State = 0
    self.machine.add_transition("get_consonant", "0", "0", before="process", after="collect")
    self.machine.add_transition("get_vowel"    , "0", "01", after="collect")
    self.machine.add_transition("get_except"   , "0", "empty", before="process", after="pass_char")

    # State = 01
    self.machine.add_transition("get_consonant", "01", "010", after="collect")
    self.machine.add_transition("get_vowel"    , "01", "empty", before="process", after="pass_char")
    self.machine.add_transition("get_except"   , "01", "empty", before="process", after="pass_char")

    # State = 010
    self.machine.add_transition("get_consonant", "010", "0", before="process", after="collect")
    self.machine.add_transition("get_vowel"    , "010", "01", before="process2", after="collect")
    self.machine.add_transition("get_except"   , "010", "empty", before="process", after="pass_char")


  def pass_char(self, char):
    self.result.append(char)

  def collect(self, char):
    self.buffer.append(char)

  def process(self, args=None):
    if len(self.buffer) > 1:
      char = hgtk.letter.compose(*self.buffer)
      self.result.append(char)
      self.buffer = []
    elif len(self.buffer) > 0:
      self.result.append(self.buffer.pop())
    else:
      pass

  def process2(self, args=None):
    char = hgtk.letter.compose(*self.buffer[:2])
    self.result.append(char)
    self.buffer = self.buffer[2:]

  def current_state(self):
    return "State : {}, Buffer : {}, Result : {}".format(
        self.state, self.buffer, ''.join(self.result))

  def init(self):
    self.result = []
    self.buffer = []
    self.to_empty()

  def compose(self, chars):

    self.init()

    for c in chars:
      code = check_jamo(c)
      if code == CONSONANT:
        self.get_consonant(c)
      elif code == VOWEL:
        self.get_vowel(c)
      else:
        self.get_except(c)

      #print(c, ord(c), code, self.current_state())

    self.process()

    return "".join(self.result)

  def decompose(self, text):
    decomposed = hgtk.text.decompose(text)
    decomposed = decomposed.replace(hgtk.text.DEFAULT_COMPOSE_CODE, '')
    return decomposed


if __name__ == "__main__":
  com = Composer()
  print(dir(com))

  texts = ["안녕하세요", "만나서 반가워", "ㅇㅋ 아니야", "1층으로 가자", "ㅋㅋㅋ큐ㅠㅠ", "미안ㅠㅠ"]
  for text in texts:
    print()
    print("Original text :", text)
    decomposed = hgtk.text.decompose(text)
    decomposed = decomposed.replace(hgtk.text.DEFAULT_COMPOSE_CODE, '')
    print("Decomposed text :", decomposed)
    composed = com.compose(decomposed)
    print("Composed text :", composed)

