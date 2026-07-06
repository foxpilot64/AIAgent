import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "executes python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "provides the file path of the python file",
                },
                "args": {
                    "type": "array",
                    "description": "Optional command line arguments passed to the file that is being executed.",
                    "items": {
                        "type": "string",
                       
                    }
                },
            },
            "required": [
            "file_path"
            ]
        },
    },
}

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
    
        base_dir = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(base_dir,file_path))

        #Check if the file_path is outside the working directory
        if os.path.commonpath([base_dir, target_file_path]) != base_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        #Check that file_path exists and points to a regular file
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        #Check if file name ends with .py, if not return Error
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
    
        #Build command list
        command = ["python", target_file_path] 
    
        if args is not None:
            command.extend(args)
    
        #Use subprocess function to run the command
        result = subprocess.run(
            command,
            cwd=base_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
        #create empty output list and append checks to it
        output = []
        #If process exited with a non-zero returncode:
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        #if both stdout and stderr contained no output:
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        #Add prefix text to stdout and stderr
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        
        return "\n".join(output)





    except Exception as e:
        return f"Error: executing Python file: {e}"

    
   