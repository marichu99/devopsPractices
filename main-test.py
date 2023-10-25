from main import hello,subtract

def TestAdd():
    assert hello(2,3) == 5
    print("The Add function works correctly")
def TestSubtract():
    assert subtract(6,3) == 3
    print("The subtract function works properly")

if __name__ == "__main__":
    TestAdd()
    TestSubtract()