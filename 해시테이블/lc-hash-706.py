class MyHashMap:

    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        self.data[key] = value;
`
    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data[key]

    def remove(self, key: int) -> None:
        if key in self.data: del self.data[`key]