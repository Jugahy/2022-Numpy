"""
import numpy as np

# 1차원 벡터 생성
np.array([1, 2, 3, 4, 5])


# 1차원 벡터의 합, 차, 곱, 나누기
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
a + b, a - b, a * b, a / b


# 2차원 행렬 생성
np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# 2차원 행렬의 합, 차, 곱, 나누기
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
a + b, a - b, a * b, a / b


# 행렬 곱(내적)
a.dot(b)
np.matmul(a, b)


# 행렬 형태 변경
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
np.array(a).reshape(4, 2)


# 리스트로 행렬 만들기
np.array(range(0, 10, 3))
np.arange(0, 10, 3)
np.linspace(0, 9, 4)  # 0~9 사이에 숫자 4개 생성
np.logspace(2, 3, 4)  # 2~3 사이에 Log10 스캐일 숫자 4개 생성
np.logspace(2, 3, num=4, base=2.0)  # 2~3 사이에 Log2 스캐일 숫자 4개 생성


# 단위행렬 만들기
np.eye(5)  # 대각성분이 1인 대각행렬
np.zeros((3, 4))  # 3x4 단위행렬 생성
np.ones((3, 4))  # 3x4 1로 채운 행렬 생성


# 행렬 슬라이싱 : 일부 행, 일부 열만 가져오기
a = np.arange(0, 100, 2)
a.shape = (10, 5)  # 1차원 배열을 10x5 2차원 배열로 만들기
a[3]  # 3행
a[3][2]  # 3행의 2열 성분
a[:3]  # 처음 행부터 3행까지
a[2:, 3:]  # 2x3 아래 성분 모두


# 행렬 연산
a + 3  # 모든 원소에게 +3
repr(a)  # 변수 또는 객체의 고유 표기 정보를 보여줌


# 행렬 인덱싱
b = np.array([[1, 2], [3, 4], [5, 6]])
b[0, 1]  # 0번쨰 행의 1번째 성분
b[0, 1] += 10  # 특정 성분에 +10
b > 3  # b11의 행렬 각각의 원소들이 3보다 큰지 확인
b[b > 3]  # b11의 행렬에서 3보다 큰 원소만 출력


# 자료형 dtype
b.dtype  # 원소의 자료형 출력


# 배열 연산
a = np.array([[1, 2], [3, 4]], dtype=np.float64)
b = np.array([[5, 6], [7, 8]], dtype=np.float64)
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.sqrt(a)


# 전치행렬
a.T


# 브로드캐스팅 : 더할수 없는 조건을 지키지 않아도 계산이 가능하다
a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,0,1])
aa = np.empty_like(a)

for i in range(2):
    aa[i,:] = a[i,:] + b

"""

