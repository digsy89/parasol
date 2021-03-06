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

## Experiment

The figure shows the results of the perplexity comparison experiment. `with decomposition` is tokenized with charactor decomposition and `no decomposition` is just tokenized.
Experiment source code is [here](notebooks/Experiment.ipynb).

![comparison_experiment_figure](https://user-images.githubusercontent.com/5267023/92320080-b3f2a280-f059-11ea-9ed9-a937a365d889.png)

## Usage

### Tokenizer

Use [SentencePiece](https://github.com/google/sentencepiece)'s BPE model as tokenizer and [hgtk](https://github.com/bluedisk/hangul-toolkit) for decomposition.

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

# Output as vocabulary id
>>> t1.tokenize("고가도로에 삐져나온 초록잎 아마 이 도시에서 유일히 적응 못한 낭만일 거야", as_id=True)
[17687, 2135, 36, 8351, 3904, 3842, 52, 12256, 27398, 3469, 30, 6105, 160, 3767, 198, 8953, 2345, 13164, 89, 6872]
```

### Composer

Hangul jamo composer

```python
from parasol import Composer

c = Composer()
```

then

```python
>>> c.compose("ㄷㅏㄹㅇㅣ ㄱㅣㅇㅜㄴ ㅂㅏㅁ ㅍㅓㄹㅓㄴㅂㅣㅊㅇㅣ ㅅㅡㅁㅕㄷㅡㄴ ㄱㅗㄹㅁㅗㄱㅇㅡㄹ ㄱㅓㄹㅇㅓㄱㅏㄷㅓㄴ ㄱㅣㄹㅇㅔ")
'달이 기운 밤 퍼런빛이 스며든 골목을 걸어가던 길에'
```

but it is not perfect, like..

```python
>>> c.compose("ㅎㅐㅇㅇㅜㄴㅇㅡㄹ ㅂㅣㄹㅇㅓㅇㅛㅎㅎ")
'행운을 빌어욯ㅎ'
```

which of original text is `행운을 빌어요ㅎㅎ`
