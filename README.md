# BDD-python-behave-test-automation
### ***This is a chrome version of automation testing***.
## Directoy Structure
* The ```.feature``` file goes under the **/features** directory.
* The implementation files go under the **/features/steps** directory. No importing or specifying is needed, behave uses all ```.py``` files under the directory.
* The resulting ```.json``` files will be saved to the **/results** directory. One with the cucumber format (converted using ```cucumber_json.py```) and one with the behave format.
* ```cucumber_json.py```: Copyright (C) 2013-2014 Oleg Pidsadnyi, Anatoly Bubenkov and others
```
.
├── features
│   ├── search_github.feature
│   ├── environment.py
│   └── steps
│       └── search_github.py
├── results
│   ├── behave.json
│   └── cucumber.json
├── util
│   ├── selenium_func.py
│   └── selenium_web.py
├── run-test.sh
├── README.md
├── requirments.txt
├── cucumber_json.py
└── chromedriver
```


## Run
Run the command under root directory to do the automation test: <br>
```./run-test.sh``` <br>

