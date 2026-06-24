import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:

        base_directory = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(base_directory, file_path))

        #Check if the file_path is outside the working directory
        if os.path.commonpath([base_directory, target_file_path]) != base_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
        #Check if the file_path points to an existing directory
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        #Make sure all parent directories of the file_path exist. 
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        #Write content to file
        with open(target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"


       