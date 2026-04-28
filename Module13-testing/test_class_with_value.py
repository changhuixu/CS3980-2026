class TestClassWithValue:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 0

    def test_three(self):
        a = "Hell" + str(self.value)
        assert a == "Hell0"
