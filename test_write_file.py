from functions.write_file import write_file

def test() -> None:


    result_txt = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result_txt)

    result_pkg = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result_pkg)

    result_tmp = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result_tmp)

if __name__ =="__main__":
    test()




