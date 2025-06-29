import os

def get_files_info(working_directory, directory=None):

    working_directory_abs = os.path.abspath(working_directory)
   

    if directory is None:
        directory_to_check = "."
    else:
        directory_to_check = directory

    
    directory_to_check_abs = os.path.abspath(os.path.join(working_directory_abs, directory_to_check))


    if not directory_to_check_abs.startswith(working_directory_abs):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(directory_to_check_abs):
        return(f'Error: "{directory}" is not a directory')

    try:
        items = os.listdir(directory_to_check_abs)
        string_collection = []
    

        for item in items:
            full_path = os.path.join(directory_to_check_abs, item)
            size = os.path.getsize(full_path)
            formatted_line = f"-{item}: file_size={size} bytes, is_dir={os.path.isdir(full_path)}"
            string_collection.append(formatted_line)
    
        return "\n".join(string_collection)

    except Exception as e:
        return f"Error: {str(e)}"
    