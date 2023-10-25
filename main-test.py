from main import hello

def TestAdd():
    assert hello(2,3) == 5
    print("The Add function works correctly")

if __name__ == "__main__":
    TestAdd()