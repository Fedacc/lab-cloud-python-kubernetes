# Frontend component

Retrieves the input text from the user from a browser and sends it to the query component.
After that displays the results to the end user

## Configure parameters

- For local development, add a **.env** file in the main directory based on the sample **.env.sample**
- For Kubernetes deployment, create a configmap with the following command

    ```bash
    kubectl create configmap frontend-config --from-literal=KEY=VALUE
    ```

## Deployment on Kubernetes

The file **deployment.yaml** contains the deployment and service configuration, edit it with the proper reference to the image in the Container Registry and then apply it with the command

```bash
kubectl apply -f deployment.yaml
```