import numpy as np

'''
    1. ndarray 속성
     print(dir(vector1))
'''

#
list_value = [10,20,30]
vector1 = np.array(list_value)
print(vector1, type(vector1), vector1.dtype)
print(dir(vector1))
'''
['__abs__', '__add__', '__and__', '__array__', '__array_finalize__', 
'__array_function__', '__array_interface__', '__array_prepare__', 
'__array_priority__', '__array_struct__', '__array_ufunc__', 
'__array_wrap__', '__bool__', '__class__', '__class_getitem__', 
'__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', 
'__delitem__', '__dir__', '__divmod__', '__dlpack__', '__dlpack_device__', 
'__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', 
'__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', 
'__imul__', '__index__', '__init__', '__init_subclass__', '__int__', 
'__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', 
'__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', 
'__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', 
'__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
'__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', 
'__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', 
'__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
'__xor__', 

'T', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 
'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 
'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 
'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 
'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 
'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 
'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 
'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 
'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 
'tostring', 'trace', 'transpose', 'var', 'view']
'''

print("1. 벡터의 차원(dimension,axis)갯수:", vector1.ndim) # 1
print("2. 벡터의 각 차원의 크기(shape):", vector1.shape) # tuple로 반환 (3,)
print("3. 벡터의 총 요소 갯수(size):", vector1.size)   # 3
print("4. 벡터의 저장 데이터 type(dtype):", vector1.dtype) # int32 (4 byte )

'''
vector1.dtype에 대해서...
np.array의 리턴타입이 ndarray이므로 vector1 = np.array(list_value)는 객체생성이라고 할 수 있다.
따라서 vector1.dtype는 인스턴스에 저장된 인스턴스 변수값을 의미한다.
vector1.ndim
vector1.shape
vector1.size 모두 같은 논리
'''
