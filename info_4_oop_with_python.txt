underscore method 는 기본으로 적용되어 있는 함수들이며
__init__, __str__ 이 있다.

    class dog:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"dog: {self.name}"

        def __getattribute__(self, name):
            return f"they want to get {name}.😂"


    kancho = dog("kancho")
    print(kancho)
    print(kancho.name)
    print(dir(kancho))

__getattr__: 인스턴스에 해당 attribute가 없을 경우 호출한다. 제일 후순위에 불러온다.
__getattribute__: 인스턴스를 호출시 제일 먼저 불러온다.