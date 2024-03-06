# Bank-Term-Deposit-Prediction

## Workflow 

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py


## DVC Commands to run

`dvc init` 

`dvc repro` 


## How to do the Cloud Deployment 

1. Login to AWS Console

2. Create an IAM user

3. Attach the Policies

 - AmazonEC2ContainerRegistryfullAccess
 - AmazonEC2FullAccess

4. Save the access file to future use

5. Create ECR Repo to store/dave docker image
  - copy the URI

6. Create EC2 Machine (ubuntu)

  - launch the instance
  - save the machine
  - select instance type 
  - create key pair
  - allow http and https traffic from anywhere
  - configure storage 
  - click on launch instance anc check if instance is running

  - click on instance id - connect

  - Map the Port 
  - click on instance id and click on security 
  - click on security groups
  - check inbound rules and click on edit inbound rules 
  - click add rule - custom TCP - port number 8501 for streamlit apps and save

  - Connect to instance
  - Connect using EC2 Instance Connect - connect

7. Run the following commands 

```bash
 - sudo apt update
 - sudo apt-get update
 - sudo apt upgrade -y
 - sudo apt install git curl unzip tar make sudo vim wget -y

 - git clone "Your-repository"
 - sudo apt install python3-pip
 - pip3 install -r requirements.txt
   
   # Temporary running
 - python3 -m streamlit run app.py

   # Permanent running
 - nohup python3 -m streamlit run app.py 
```


