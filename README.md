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
sudo apt update
```

```bash
 sudo apt-get update
 ```

 ```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone "Your-repository"
```

# cd your repository
# ls - check the directory

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```

```bash
pip3 install -r requirements_new.txt
```
   
# Temporary running

```bash
python3 -m streamlit run app.py
```

# Permanent running

```bash
nohup python3 -m streamlit run app.py 
```


## Docker Image

```bash

sudo apt-get update -y
```

```bash
sudo apt-get upgrade
```

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```

```bash
sudo sh get-docker.sh
```

```bash
sudo usermod -aG docker ubuntu
```

```bash
newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t gauravbhattacharya29/termdepositapp: latest .
```

```bash
docker images -a
```

```bash
docker run -d -p 8501:8501 gauravbhattacharya29/termdepositapp
```

```bash
docker ps
```

```bash
docker stop container_id
```


## SECRETS to setup

AWS_ACCESS_KEY_ID = 

AWS_SECRET_ACCESS_KEY = 

AWS_REGION = 

AWS_ECR_LOGIN_URI = 

ECR_REPOSITORY_NAME = 