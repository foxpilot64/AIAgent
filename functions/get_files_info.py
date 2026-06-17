import os

def get_files_info(working_directory, directory=None):
    try:

        working_directory_abs = os.path.abspath(working_directory)
   

        if directory is None:
            directory_to_check = "."
        else:
            directory_to_check = directory

    
        directory_to_check_abs = os.path.abspath(os.path.join(working_directory_abs, directory_to_check))


        if os.path.commonpath([working_directory_abs, directory_to_check_abs]) != working_directory_abs:
            return f'Error: Cannot list "{directory_to_check}" as it is outside the permitted working directory'

        if not os.path.isdir(directory_to_check_abs):
            return(f'Error: "{directory_to_check}" is not a directory')


    #Iterate over items in target directory and record name, file size, and if it is a directory.
        files_info = []
        for items in os.listdir(directory_to_check_abs):
            filepath = os.path.join(directory_to_check_abs, items)
            size = os.path.getsize(filepath)
            is_directory = os.path.isdir(filepath)
       
            formatted_string = f"- {items}: file_size={size} bytes, is_dir={is_directory}"

            files_info.append(formatted_string)
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error: {e}"