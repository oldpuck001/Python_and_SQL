# iterator.py

# 生成器示例

class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))