
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
This command creates a copy of the config_template.py file and renames it to config.py.

### 2. Run the Tool
Execute the main runner file by running the following command:

   ```shell
   python3 runner.py 
   ```


## Methodology

Each WAF solution is tested against two data sets: legitimate and malicious. We then used a formula described below in detail to produce a single balanced score. The True positives are in the DB which then can be used to extract the model.

### Legitimate Data Set

The dataset can be found in the folder Data/Legitimate

### Malicious Data Set

- Log4Shell

## For larger datasets
Use the `dataset_splitter.py` to get manageable chunks to run attacks.


The malicious payloads were sourced from the WAF Payload Collection GitHub page that was assembled by mgm security. This repository serves as a valuable resource, providing payloads specifically created for testing Web Application Firewall rules. 

The dataset is available [here](https://github.com/openappsec/mgm-web-attack-payloads)

## Running the Tests
The main file for running the tests is `runner.py`. This script will send the HTTP requests, log the responses, and calculate the performance metrics for each WAF.


[MGM WAF Payload Collection](https://github.com/mgm-sp/WAF-Payload-Collection)


