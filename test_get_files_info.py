from functions.get_files_info import get_files_info

def test() -> None:

    result_current = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result_current)

    result_pkg = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result_pkg)

    result_bin = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result_bin)

    result_parent = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result_parent)

    result_main = get_files_info("calculator", "main.py")
    print("Result for 'main.py':")
    print(result_main)

if __name__ =="__main__":
    test()
    
