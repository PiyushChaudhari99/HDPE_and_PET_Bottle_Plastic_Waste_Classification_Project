# HDPE and PET bottle plastic waste classification project


## Workflows
1.Update config.yaml<br>
2.Update params.yaml<br>
3.Update the entity<br>
4.Update the configuration manager in src config<br>
5.Update the components<br>
6.Update the pipeline<br>
7.Update the main.py<br>
8.Update the dvc.yaml<br>
9.app.py<br>


# How to run?

### STEPS:
Clone the repository
```bash
https://github.com/PiyushChaudhari99/HDPE_and_PET_Bottle_Plastic_Waste_Classification_Project.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```
...
### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

Finally run the following command
```bash
python app.py
```

Now,
```bash
open up you local host and port
```



#### MLFLOW
[Documentation](https://mlflow.org/docs/latest/index.html)



##### cmd
- mlflow ui

### DagsHub
[DagsHub](https://dagshub.com/)


MLFLOW_TRACKING_URI= "https://dagshub.com/PiyushChaudhari99/HDPE_and_PET_Bottle_Plastic_Waste_Classification_Project.mlflow"

MLFLOW_TRACKING_USERNAME= "PiyushChaudhari99"

MLFLOW_TRACKING_PASSWORD= "e59ebc051282a6fc2df2e5953c71674e757a6587"


Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI= https://dagshub.com/PiyushChaudhari99/HDPE_and_PET_Bottle_Plastic_Waste_Classification_Project.mlflow
export MLFLOW_TRACKING_USERNAME= PiyushChaudhari99
export MLFLOW_TRACKING_PASSWORD= e59ebc051282a6fc2df2e5953c71674e757a6587
```