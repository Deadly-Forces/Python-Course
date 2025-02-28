# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosing -> Global -> Built-in

def func1():
    x = 7
    print(x)

def  func2():
    y = 10
    print(y)

func1()
func2()