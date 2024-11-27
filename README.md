
## Setup Instructions
Follow the steps below to set up and run the tool:

Download the necessary python requirements
```shell
pip install -r requirements.txt
```

### 1. Copy the Configuration Template
Copy the configuration template file by running the following command in the project's root directory:

```shell
cp config_template.py config.py
```
This command creates a copy of the config_template.py file and renames it to config.py. After this, replace the URL with your OpenAppSec playground's URL, make sure the model is uploaded through their dashboard.

### 2. Run the Tool
Execute the main runner file by running the following command:

   ```shell
   python runner.py 
   ```

### 3. Fetch data from Database
Execute the database query file running the following command. This creates a .txt file that shows all querys that were not blocked by the WAF:

   ```shell
   python out_db.py 
   ```


## Methodology

Each WAF solution is tested against two data sets: legitimate and malicious. We then used a formula described below in detail to produce a single balanced score. The True positives are in the DB which then can be used to extract the model.

### Legitimate Data Set

The dataset can be found in the folder Data/Legitimate

### Malicious Data Set

- Log4Shell

## For larger datasets
Use the `dataset_splitter.py` to get manageable chunks to run attacks.

More datasets available [here](https://github.com/openappsec/mgm-web-attack-payloads)

## Running the Tests
The main file for running the tests is `runner.py`. This script will send the HTTP requests, log the responses, and calculate the performance metrics for each WAF.


