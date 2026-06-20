from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result_main = get_file_content("calculator", "main.py")
print(result_main)

result_pkg = get_file_content("calculator", "pkg/calculator.py")
print(result_pkg)

#This should return an Error
result_bin = get_file_content("calculator", "/bin/cat")
print(result_bin)

#This should return an Error
result_no_pkg = get_file_content("calculator", "pkg/does_not_exist.py")
print(result_no_pkg)

