Parasol Tokenizer
================

Parasol tokenizes hangul after decomposition.
한글 자음,모음을 분해하여 토큰화합니다.

* __Original text__ : 고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야
* __Decomposed text__ : ㄱㅗㄱㅏㄷㅗㄹㅗㅇㅔ ㅃㅣㅈㅕㄴㅏㅇㅗㄴ ㅊㅗㄹㅗㄱㅇㅣㅍ ㅇㅏㅁㅏ ㅇㅣ ㄷㅗㅅㅣㅇㅔㅅㅓ ㅇㅠㅇㅣㄹㅎㅣ ㅈㅓㄱㅇㅡㅇ ㅁㅗㅅㅎㅏㄴ ㄴㅏㅇㅁㅏㄴㅇㅣㄹ ㄱㅓㅇㅑ
* __Tokens__ : ▁ㄱㅗㄱㅏ / ㄷㅗㄹㅗ / ㅇㅔ / ▁ㅃㅣ / ㅈㅕㄴ / ㅏㅇㅗㄴ / ▁ㅊ / ㅗㄹ / ㅗㄱ / ㅇㅣ / ㅍ / ▁ㅇㅏㅁㅏ / ▁ㅇㅣ / ▁ㄷㅗㅅㅣ / ㅇㅔㅅㅓ / ▁ㅇㅠㅇㅣㄹ / ㅎㅣ / ▁ㅈㅓㄱㅇㅡㅇ / ▁ㅁㅗㅅㅎㅏㄴ / ▁ㄴㅏㅇㅁㅏㄴ / ㅇㅣㄹ / ▁ㄱㅓㅇㅑ
* __Composed tokens__ : ▁고가 / 도로 / 에 / ▁삐 / 젼 / ㅏ온 / ▁ㅊ / ㅗㄹ / ㅗㄱ / 이 / ㅍ / ▁아마 / ▁이 / ▁도시 / 에서 / ▁유일 / 히 / ▁적응 / ▁못한 / ▁낭만 / 일 / ▁거야


## Installation

  pip install parasol-nlp

## Usage

```python
from parasol import Tokenizer

# tokenize after decomposition  
t1 = Tokenizer(decompose=True)
# tokenize without decomposition
t2 = Tokenizer(decompose=False)
```

then

```python
>>> t1.tokenize("고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야")
['▁고가', '도로', '에', '▁삐', '젼', 'ㅏ온', '▁ㅊ', 'ㅗ록', '잎', '▁아마', '▁이', '▁도시', '에서', '▁유일', '히', '▁적응', '▁못한', '▁낭만', '일', '▁거야']
>>> t2.tokenize("고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야")
['▁고가', '도로', '에', '▁삐', '져', '나온', '▁초록', '잎', '▁아마', '▁이', '▁도시', '에서', '▁유일', '히', '▁적응', '▁못한', '▁낭만', '일', '▁거야']
```
