import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
    
        base_directory = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(base_directory, file_path))

        #Check if the file is within the same working directory
        if os.path.commonpath([base_directory, target_file_path]) != base_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        #Check if it is a valid file type
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"' 
    
        #Read up to 10000 chars in file:
        #open file in read mode and refer to it as f
        with open(target_file_path, "r") as f:
            content = f.read(MAX_CHARS)

        #Check if file was larger than Char limit
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    
    except Exception as e:
        return f"Error: {e}"