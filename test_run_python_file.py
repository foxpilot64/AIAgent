from functions.run_python_file import run_python_file

def test() -> None:
    #Should print calculator's usage instructions
    result = run_python_file("calculator", "main.py")
    print(result)

    #Should run the calculator with a nasty rendered result
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    #Should run calculator's test successfully
    result = run_python_file("calculator", "tests.py")
    print(result)

    #Should return an error
    result = run_python_file("calculator", "../main.py")
    print(result)

    #Should return an error
    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    #Should return an error
    result = run_python_file("calculator", "lorem.txt")
    print(result)


if __name__ =="__main__":
    test()
