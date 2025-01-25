from typing import List, Dict, Any
import os
from pathlib import Path
from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field

class AIFileAssistant:
    def __init__(self, base_directory: str = "."):
        """Initialize AIFileAssistant with a base directory."""
        self.base_directory = Path(base_directory).resolve()

    def get_tools(self):
        """Get all tools as a list of StructuredTool objects."""
        return [
            StructuredTool.from_function(
                func=self.list_files,
                name="list_files",
                description="List all files in the specified directory",
            ),
            StructuredTool.from_function(
                func=self.read_file,
                name="read_file",
                description="Read contents of a file",
            ),
            StructuredTool.from_function(
                func=self.write_file,
                name="write_file",
                description="Write content to a file",
            ),
            StructuredTool.from_function(
                func=self.delete_file,
                name="delete_file",
                description="Delete a file",
            ),
            StructuredTool.from_function(
                func=self.create_directory,
                name="create_directory",
                description="Create a new directory",
            ),
            StructuredTool.from_function(
                func=self.find_latest_file,
                name="find_latest_file",
                description="Find the latest file created in the specified directory",
            ),
        ]

    def list_files(self, directory: str = ".") -> List[str]:
        """
        List all files in the specified directory.
        
        Args:
            directory: The directory path relative to base_directory
            
        Returns:
            List of file names in the directory
        """
        target_dir = (self.base_directory / directory).resolve()
        if not target_dir.exists():
            raise ValueError(f"Directory {directory} does not exist")
        
        return [str(f.relative_to(self.base_directory)) for f in target_dir.glob("*")]

    def read_file(self, file_path: str) -> str:
        """
        Read contents of a file.
        
        Args:
            file_path: Path to the file relative to base_directory
            
        Returns:
            Contents of the file as a string
        """
        target_file = (self.base_directory / file_path).resolve()
        if not target_file.exists():
            raise ValueError(f"File {file_path} does not exist")
        
        with open(target_file, 'r') as f:
            return f.read()

    def write_file(self, file_path: str, content: str) -> str:
        """
        Write content to a file.
        
        Args:
            file_path: Path to the file relative to base_directory
            content: Content to write to the file
            
        Returns:
            Success message
        """
        target_file = (self.base_directory / file_path).resolve()
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(target_file, 'w') as f:
            f.write(content)
        
        return f"Successfully wrote to {file_path}"

    def delete_file(self, file_path: str) -> str:
        """
        Delete a file.
        
        Args:
            file_path: Path to the file relative to base_directory
            
        Returns:
            Success message
        """
        target_file = (self.base_directory / file_path).resolve()
        if not target_file.exists():
            raise ValueError(f"File {file_path} does not exist")
        
        os.remove(target_file)
        return f"Successfully deleted {file_path}"

    def create_directory(self, directory: str) -> str:
        """
        Create a new directory.
        
        Args:
            directory: Directory path to create relative to base_directory
            
        Returns:
            Success message
        """
        target_dir = (self.base_directory / directory).resolve()
        target_dir.mkdir(parents=True, exist_ok=True)
        return f"Successfully created directory {directory}"

    def find_latest_file(self, directory: str = '.') -> str:
        """
        Find the latest file created in the specified directory.
        
        Args:
            directory: The directory path relative to base_directory
        
        Returns:
            The name of the latest file created in the directory
        """
        target_dir = (self.base_directory / directory).resolve()
        if not target_dir.exists():
            raise ValueError(f"Directory {directory} does not exist")
        
        latest_file = max(target_dir.glob('*'), key=os.path.getctime, default=None)
        return str(latest_file.relative_to(self.base_directory)) if latest_file else 'No files found.' 