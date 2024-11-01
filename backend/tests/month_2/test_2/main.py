class a:
    def __init__(self, a) -> None:
        self.a = a

    def run(self):
        print(f"run {self.a}")


class b:
    def run(self):
        print(f" no run {self.a}")


class d(a, b):

    def Run(self):
        print("hello")


e = d("adil")

print(e.run())
