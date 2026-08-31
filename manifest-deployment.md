## Deployment through Manifest Files 

1. What we were trying to deploy
<img width="600" height="400" alt="ChatGPT Image Aug 31, 2026, 02_32_07 PM" src="https://github.com/user-attachments/assets/8ad27f6a-d4ce-4486-940c-fa6cac3380ed" />  


2. After creating the Eks cluster run these commands on the terminal
   Remember always start with Secrets -> configmap -> Mysql -> FlaskApp
```
cd /d/DevOpsProject/Project3/eks-manifests
kubectl apply -f mysql-secrets.yaml
kubectl apply -f mysql-configmap.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f mysql-service.yaml
kubectl apply -f two-tier-app-deployment.yaml
kubectl apply -f two-tier-app-svc.yaml

```
<img width="1481" height="320" alt="cloning-repo-04" src="https://github.com/user-attachments/assets/46c8cf2c-f2c9-4585-873e-c454699cbe50" />  
<br> 

<img width="1482" height="762" alt="applying-manifestfile-05" src="https://github.com/user-attachments/assets/8645d394-c986-4464-91e8-6beeb19c3ee9" />



3. Verify Everything is Running
```
# Check all pods
kubectl get pods

# Check all services
kubectl get svc

# Check all deployments
kubectl get deployments

# Check all resources
kubectl get all

# Check secrets
kubectl get secrets

# Check configmaps
kubectl get configmaps

```  

<img width="1487" height="763" alt="all-manifest-applied-06" src="https://github.com/user-attachments/assets/1d489021-355a-442b-9c3f-c99af2294b71" />


4. Access Your Application    


```
# Get the external IP (may take a few minutes)
kubectl get svc two-tier-app-service

# Wait for EXTERNAL-IP to be assigned
kubectl get svc -w

# Then access: http://<EXTERNAL-IP>:5000  
```
<img width="1477" height="763" alt="app-url-07" src="https://github.com/user-attachments/assets/9c276fa1-373c-4ebd-b4b7-06c0f301097e" />  

If all the configuration is right then the app will be running on the URL 


<img width="1917" height="976" alt="app-running-08" src="https://github.com/user-attachments/assets/c0402f22-2ba4-4da0-81e7-a17657747e62" />
<br>  

Upon Using , its working Fine also :)  
<br> 

<img width="1918" height="748" alt="app-working-09" src="https://github.com/user-attachments/assets/4833ed28-b90f-4be6-a8b9-951a060beae5" />
<br>  

## Debugging   

1. In mysql-svc.yaml, It was mentioned externalName: host.docker.internal which was wronge, it was supposed to be ClusterIP .
Under spec -> type , selector, port was suppose to be mentioned.
Earlier:
```
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  type: ExternalName
  externalName: host.docker.internal
```

After Correction: 
```
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  type: ClusterIP
  selector:
    app: mysql
  ports:
    - port: 3306
      targetPort: 3306
```


2. Flask Service: change from Minikube-style exposure to EKS LoadBalancer
For minikube we were using service type as NodePort but while dealing with eks we whould be using LoadBalancer

  


  

