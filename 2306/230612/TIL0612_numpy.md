## Numpy

## [실습](./)

---

## 정리

### 2차원 배열 색인
- ndarray[m,n]
- 인덱싱, 슬라이싱, fancy, boolean

### 색인을 활용한 데이터 변경
- arr[m,n] = 값
- 인덱싱, 슬라이싱, fancy, boolean

### 얕은 / 깊은 복사
- 얕은 복사
    - ndarray[:]
- 깊은 복사
    - np.copy() / ndarray.copy()

### 다차원 열 / 행병합
- 다차원 열병합
    - np.hstack() / np.concatenate(1) / np.column_stack()
- 다차원 행병합
    - np.vstack() / np.concatenate(0) / np.row_stack()

### 다차원 열 / 행분할
- 다차원 열분할
    - np.hsplit() / np.split(1)

- 다차원 행분할
    - np.vsplit() / np.split(0)

### 범용함수(유니버셜 함수)
- 단항 유니버셜
    - np.abs / np.sqrt / np.reciprocal
    - np.around / np.round / np.rint / np.fix / np.ceil / np.floor / np.trunc
- 이항 유니버셜
    - np.add / np.subtract / np.multiply / np.divide / np.floor_divide / np.mod / np.power
    - np.maximum / np.minimum / np.greater / np.greater_equal / np.less / np.less_equal / np.equal / np.not_equal
- 문자열 범용함수 - np.char.func
    - add / multiply
    - capitalize / lower / upper / swapcase / title
    - center / ljust / rjust
    - encode / decode
    - join / split
    - strip / lstrip / rstrip
    - replace
    - find
    - count
    - startswith / endswith
    - equal / not_equal
    - islower / isupper / isalpha / isdigit

### 유틸리티 함수
- np.prod / np.cumprod / np.nanprod
- np.sum / np.cumsum / np.nansum
- np.mean / np.median / np.var / np.std
- np.max / np.argmax / np.min / np.argmin
- np.sort
- np.all / np.any
- ndarray.T / ndarray.transpose
- np.dot

### 차원증가
- ndarray.reshape((m,n))
- np.expand_dims
- ndarray[np.newaxis, :]

### 차원(하나)감소
- np.squeeze

### 1차원으로 감소
- ndarray.flattern
- ndarray.ravel