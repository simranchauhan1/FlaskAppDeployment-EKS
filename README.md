## Step - 1 : Create EKS Management Host in AWS ##

1) Launch new Ubuntu VM using AWS Ec2 ( t2.micro )
## Install Unzip 
```
sudo apt update
sudo apt install unzip -y
```
2) Connect to machine and install kubectl using below commands  
```
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.36.2/2026-07-05/bin/linux/amd64/kubectl
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.36.2/2026-07-05/bin/linux/amd64/kubectl.sha256
sha256sum -c kubectl.sha256
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```
3) Install AWS CLI latest version using below commands 
```
curl -fsSL https://awscli.amazonaws.com/v2/install.sh | bash
curl -fsSL https://awscli.amazonaws.com/v2/install.sh | sudo bash -s -- --system
curl -fsSL https://awscli.amazonaws.com/v2/install.sh | bash -s -- --help
```

4) Install eksctl using below commands
```
# for ARM systems, set ARCH to: `arm64`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo install -m 0755 /tmp/eksctl /usr/local/bin && rm /tmp/eksctl
```
## Step - 2 : Create IAM role & attach to EKS Management Host ##

1) Create New Role using IAM service ( Select Usecase - ec2 ) 	
2) Add below permissions for the role <br/>
	- Administrator - acces <br/>
		
3) Enter Role Name (eksroleec2) 
4) Attach created role to EKS Management Host (Select EC2 => Click on Security => Modify IAM Role => attach IAM role we have created) 

## Step - 3 : Create EKS Cluster using eksctl ## 
**Syntax:** 

eksctl create cluster --name cluster-name  \
--region region-name \
--node-type instance-type \
--nodes-min 2 \
--nodes-max 2 \ 
--zones <AZ-1>,<AZ-2>

## N. Virgina: <br/>
```
eksctl create cluster --name ashokit-cluster4 --region us-east-1 --node-type t2.medium  --zones us-east-1a,us-east-1b
```
## Mumbai: <br/>
```
eksctl create cluster --name ashokit-cluster4 --region ap-south-1 --node-type t2.medium  --zones ap-south-1a,ap-south-1b
```

## Note: Cluster creation will take 5 to 10 mins of time (we have to wait). After cluster created we can check nodes using below command.

```
 kubectl get nodes  
```

### Note: We should be able to see EKS cluster nodes here. ##

### We are done with our Setup ###
	
## Step - 4 : After your practise, delete Cluster and other resources we have used in AWS Cloud to avoid billing ##

```
eksctl delete cluster --name ashokit-cluster4 --region ap-south-1
```
