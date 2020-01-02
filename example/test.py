from parasol import Tokenizer

t1 = Tokenizer(decompose=True)
t2 = Tokenizer(decompose=False)

texts = [
  "행운을 빌어요",
  "달이 기운 밤 퍼런빛이 스며든 골목을 걸어가던 길에 모퉁이에서 발이 엉켜 넘어져 그대로 좀 누워있었네",
  "고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야"
]

for text in texts:
  print(text)
  print(t1.tokenize(text))
  print(t2.tokenize(text))
  print()
