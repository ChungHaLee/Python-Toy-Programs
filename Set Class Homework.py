class Set:
    def __init__(self, lst):
        self.lst = lst

    def add(self, elem):
        if len(self.lst) == 0:
            self.lst.append(elem)
        else:
            pass

    def discard(self, elem):  # 얕은 복사 --> 객체는 그대로 두면서 복사하는 방법
        while elem in self.lst:  # discard 함수 자체는 객체 자체에 접근해서 삭제해서 얕은 복사 할 필요 x
            self.lst.remove(elem)

    def clear(self):
        self.lst.clear()  # clear 함수 사용 --> 리스트 모든 원소 삭제

    def __len__(self):
        return len(self.lst)

    def __str__(self):  # Set 에 존재하는 원소를 문자열 형태로 반환
        stri = ''
        for i in self.lst:
            stri += str(i) + ', '
        stri = stri.rstrip(', ')
        return '{%s}' % stri


    def __contains__(self, elem):
        if elem in self.lst:
            return True
        else:
            return False


    def __le__(self, other):
        for i in self.lst:
            if i in other.lst:   # 에러코드: 'str' object has no attribute 'lst', 합집합에서 반환되는 값이 리스트가
                continue
            else:
                return False
        return True


    def __ge__(self, other):     # other 가 self 의 부분집합이면 참, 아니면 거짓
        for i in other.lst:
            if i in self.lst:
                continue
            else:
                return False
        return True

    def __or__(self, other):  # 1) 합집합 함수
        # 중복 되면 안됨!
        tmp = self.lst[:]  # 얕은 복사(원 객체를 복사)
        for b in tmp:
            if b in other.lst:  # while 구문 아니고 if 문 ㅎ (while 이 안되는 이유는 뭐지)
                tmp.remove(b)  # 리스트 원소 del 함수로 삭제하기
        tmp.extend(other.lst)  # append 아니고 extend 함수 사용 (리스트가 아니라 요소 자체를 추가)
        return Set(tmp)  # 진짜 중요: 객체로 다시 만들어주는 함수 Set.!!!!!!!!!!!!!!


    def __and__(self, other):  # 2) 교집합 함수
        tmp = self.lst[:]
        new_lst = []
        for i in tmp:
            if i in other.lst:
                new_lst.append(i)
            else:
                pass
        return Set(new_lst) # 진짜 중요: 객체로 다시 만들어주는 함수 Set.!!!!!!!!!!!!!!


    def __sub__(self, other):  # 3) 차집합 함수
        tmp = self.lst[:]
        new_lst = []
        for i in tmp:
            if i not in other.lst:
                new_lst.append(i)
            else:
                pass
        return Set(new_lst) # 진짜 중요: 객체로 다시 만들어주는 함수 Set.!!!!!!!!!!!!!!



a = Set([1, 2, 3, 4])
b = Set([2, 3, 4])

print(a)
print(b)
print()

a.discard(4)
b.discard(2)
print(a)
print(b)
print()


print(len(a))
print(1 in a)
print(1 in b)
print()


print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
print()

print(a <= b)
print(a <= a | b)
print(a >= b)
print(a >= a & b)
print()

b.clear()
print(b)