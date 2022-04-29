# Twitter-Data-Analysis

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites (Linux)
- Python

```bash
sudo add-apt-repository ppa:jonathonf/python-3.7
sudo apt-get update
sudo apt-get install python3.7
```

- pip3

```bash
sudo apt update
sudo apt install python3-pip
```



## Installing

### For Development

1. Clone the Repo
   ```bash
    git clone https://github.com/Micky373/Twitter-Data-Analysis.git
   ```
2. cd into repo
   ```bash
   cd Twitter-Data-Analysis
   ```
3. Install Requirements
   ```bash
    pip3 install -r requirements.txt
   ```
4. Extract dataframe
   ```bash
   python3 extract_dataframe.py
   ```
5. Clean Extracted DataFrame
   ```bash
   python3 clean_tweets_dataframe
   ```
6. Run the App
   ```bash
    streamlit run dashboard.py

## Topic Modeling
Topic Modeling for twtter data can be found in twitter_modeling.ipynb jupyter notebook file.
## Unit Testing
The following code enables you ti run unit test
1. Get into Test Directory
```bash
   cd tests
   ```
2. Run Test
   ```bash
   python3 test_extract_dataframe.py
   ``