# FileAssistant

A Python-based intelligent file system assistant using LangChain and OpenAI's language models. This tool provides a natural language interface for common file operations, making it easy to manage files and directories through conversation.

## Features

- **Natural Language Interface**: Interact with your file system using plain English commands
- **File Operations**:
  - List files in directories
  - Read file contents
  - Write/create new files
  - Delete files
  - Create directories
  - Find latest modified files
- **Safety Features**:
  - Path resolution to prevent directory traversal attacks
  - Existence checks before file operations
  - Automatic parent directory creation for write operations

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FileAssistant.git
   cd FileAssistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the interactive assistant:
```bash
python example.py
```

### Example Commands

- List files: "What files are in the current directory?"
- Create file: "Create a new file called notes.txt with content 'Meeting at 3 PM'"
- Read file: "Show me what's in requirements.txt"
- Create directory: "Make a new folder called 'documents'"
- Find latest file: "What's the most recently created file?"
- Delete file: "Delete the file test.txt"

### Using FileAssistant in Your Code

```python
from file_assistant import FileAssistant

# Initialize FileAssistant
assistant = FileAssistant(base_directory=".")

# List files in a directory
files = assistant.list_files(".")

# Read a file
content = assistant.read_file("example.txt")

# Write to a file
assistant.write_file("new_file.txt", "Hello, World!")

# Create a directory
assistant.create_directory("new_directory")

# Find latest file
latest = assistant.find_latest_file(".")

# Delete a file
assistant.delete_file("old_file.txt")
```

## Project Structure

```
FileAssistant/
├── file_assistant.py   # Main FileAssistant class
├── example.py         # Interactive chat interface
├── requirements.txt   # Project dependencies
├── .env              # Environment variables
└── .gitignore        # Git ignore rules
```

## Safety Considerations

- The assistant operates only within its initialized base directory
- Path resolution prevents directory traversal attacks
- Existence checks are performed before file operations
- Parent directories are automatically created when needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 