# OpenTargets Drug Information Retriever

This Python script allows users to retrieve drug information from the OpenTargets platform based on gene names. It utilizes the OpenTargets API to gather evidence for known drugs associated with specified genes.

## Usage

1. **Input**: Run the script and input gene names when prompted. The user can input one or more gene names separated by spaces.

2. **Data Retrieval**: The script converts the input gene names to Ensembl IDs using the MyGene package. Then, it queries the OpenTargets API to retrieve drug information associated with the provided genes.

3. **Output**: The script generates a JSON file containing drug information for genes associated with relevant diseases. If the retrieved data includes drugs associated with cardiovascular diseases (CVD), it filters and exports this subset of information to a JSON file named `kfile.json`.

## Dependencies

- `requests`: For making HTTP requests to the OpenTargets API.
- `numpy`: Required for array manipulation.
- `pandas`: Used for data manipulation and creating data tables.
- `mygene`: Enables querying gene information from MyGene.
- `json`: For handling JSON data.
- `csv`: Required for handling CSV files.

## Installation

Ensure all dependencies are installed using pip:

pip install requests numpy pandas mygene

## Running the Script

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:

python script.py

5. Follow the prompt to input gene names.
6. Wait for the script to retrieve and process the data.
7. Check the generated JSON files for drug information.

## Notes

- The script may take some time to run, depending on the number of gene names provided and the response time of the OpenTargets API.
- Ensure a stable internet connection for successful data retrieval.
- Review the generated JSON files for detailed drug information.

