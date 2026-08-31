## Deployment throught Helm 

1. We already had a Eks cluster setup ready with helm installed on it.
  So, first I created a chart for mysql named it mysql-chart and the for the flask app named it flaskapp-chart.

  ```
helm creat mysql-chart
helm creat flaskapp-chart
  ```

2. After creating charts , I packeged them using commands 
```
helm install mysql ./mysql-chart
helm install flaskapp ./flaskapp-chart 
```


3. Access Application 
``` kubectl get svc ```  
<br>
<img width="1482" height="761" alt="helm-svc-11" src="https://github.com/user-attachments/assets/ddaf8677-450e-48c5-859c-f8f2f8a50cfc" />

<br>
<img width="1911" height="962" alt="helm-10" src="https://github.com/user-attachments/assets/5ddf5cd2-68a5-4169-b522-cd36ad2536a7" />


<br>
4. There will be a URL for the app we created , we can access the app upon hitting the generated url in the browser.

5. Debugging
   a) The first issue was simply a label naming mismatch
     Fix: helm upgrade mysql ./mysql-chart
          helm upgrade flaskapp ./flaskapp-chart
   b) DNS Name Mismatch: Your service is named mysql-service, but your Flask app is configured to connect to host mysql.
     Fix: Open mysql-chart/templates/service.yaml and set metadata.name explicitly to mysql, matching your pod selectors:
   c) Access Issue: flaskapp-chart is set to NodePort instead of LoadBalancer, meaning it lacks a public AWS URL (EXTERNAL-IP shows <none>).
     Fix: Open flaskapp-chart/templates/service.yaml and update spec.type to LoadBalancer.
           To make Helm create a service named mysql that successfully connects to your MySQL pod, inspect the content of templates/service.yaml.  
           Open templates/service.yaml in vim and update its structure to match your pod's labels and force the service name to mysql
   d) Port 80 was not open for loadBlancer Security goups.      
   
