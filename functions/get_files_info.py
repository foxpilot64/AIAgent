import os

def get_files_info(working_directory, directory=None):

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


    return f'Success: "{directory_to_check}" is within the working directory'
  
    