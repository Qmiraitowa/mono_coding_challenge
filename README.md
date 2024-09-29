## Wedding Data Processor

This Python script imports user and wedding data from CSV files into a PostgreSQL database, queries for specific wedding events, and outputs the results to files.

### Requirements
- Python 3.x
- PostgreSQL
- `psycopg2` library

### Setup

1. Install the required Python packages:  `pip install psycopg2`
2. Ensure PostgreSQL is installed and running, and create a database (`wedding_db`).
3. Modify the database connection parameters in the script to match your setup.
4. Run the script: *wedding_data_processor.py*
5. The results will be saved to `june_2024_weddings.txt` and `upcoming_weddings.txt`.

### Unit Tests

Use the `unittest` framework to test the functions: *test.py*

