from main import hello,subtract

def test_Add():
    assert hello(2,3) == 5
    print("The Add function works correctly")
def test_Subtract():
    assert subtract(6,3) == 3
    print("The subtract function works properly")

if __name__ == "__main__":
    test_Add()
    test_Subtract()