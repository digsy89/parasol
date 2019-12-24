import koto

t = koto.Tokenizer(decompose=True)

t.tokenize("안녕하세요")
t.tokenize("집에 가고 싶다.")
t.tokenize("달이 기운 밤 퍼런빛이 스며든 골목을 걸어가던 길에 모퉁이에서 발이 엉켜 넘어져 그대로 좀 누워있었네")
result = t.tokenize("고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야")
print(' / '.join(result))
