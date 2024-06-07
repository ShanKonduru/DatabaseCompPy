# Data Comparison Tool

This Python program compares two database tables to validate if the data from the source table and destination table are the same. It identifies any deviations or gaps and generates an HTML/CSS-based report that highlights:

1. Records that exist in the source table but not in the target table.
2. Records that exist in the target table but not in the source table.
3. Matching records that exist in both tables.

The structure of the source and target databases may be different, so the program reads the table and column mappings from an external file. The solution supports different databases (e.g., Oracle, SQL Server).

## Features

- Compare data between two database tables.
- Generate a detailed HTML report.
- Supports different database types.
- Reads table and column mappings from external files.

## Requirements

- Python 3.x
- Poetry for dependency management

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/data-comparison-tool.git
    cd data-comparison-tool
    ```

2. **Install Poetry** (if not already installed):
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install dependencies**:
    ```sh
    poetry install
    ```

## Configuration

1. **Database Configuration** (`db_config.json`):
    ```json
    {
        "source_db": {
            "type": "oracle",
            "user": "src_user",
            "password": "src_password",
            "dsn": "src_dsn"
        },
        "destination_db": {
            "type": "sql_server",
            "user": "dest_user",
            "password": "dest_password",
            "server": "dest_server",
            "database": "dest_db"
        }
    }
    ```

2. **Table and Column Mappings** (`mappings.json`):
    ```json
    {
        "source": {
            "table": "src_table",
            "columns": ["col1", "col2", "col3"]
        },
        "destination": {
            "table": "dest_table",
            "columns": ["colA", "colB", "colC"]
        },
        "key_columns": ["col1", "colA"]
    }
    ```

3. **HTML Report Template** (`templates/report_template.html`):
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Comparison Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
            table, th, td { border: 1px solid black; }
            th, td { padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Data Comparison Report</h1>
        <h2>Records in Source but not in Destination</h2>
        {{ src_only|safe }}
        <h2>Records in Destination but not in Source</h2>
        {{ dest_only|safe }}
        <h2>Matching Records</h2>
        {{ both|safe }}
    </body>
    </html>
    ```

## Usage

1. **Run the comparison**:
    ```sh
    poetry run python compare_tables.py
    ```

2. **Generated Report**:
    - The generated HTML report will be saved as `report.html` in the project directory.

## Directory Structure

data-comparison-tool/
├── main.py
├── db_config.json
├── mappings.json
├── pyproject.toml
├── README.md
├── templates
   ├── report_template.html


## Contributing

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## pyproject.toml for Poetry

Ensure your pyproject.toml includes the necessary dependencies. Here's a sample:

[tool.poetry]
name = "data-comparison-tool"
version = "0.1.0"
description = "A tool to compare database tables and generate a report."
authors = ["Your Name <youremail@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
cx_Oracle = "^8.3"
pyodbc = "^4.0.32"
pandas = "^1.4.2"
jinja2 = "^3.1.2"

[tool.poetry.dev-dependencies]
pytest = "^6.2"


this README.md file provides a comprehensive overview of your project, including installation, configuration, and usage instructions, while the pyproject.toml ensures that all necessary dependencies are managed by Poetry.

