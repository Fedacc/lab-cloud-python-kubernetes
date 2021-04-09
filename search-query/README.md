# lab-cloud-python-kubernetes

## Run locally

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env` file following `.env.sample` as a template, add the proper credentials that can be obtained by registering with no charge at https://cloud.ibm.com/login and deploying an instance of [Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery)

Start the flask server locally

```bash
python run.py
```

Send the queries via POST request to the server with the following payload

```bash
{
    "query": "string to search"
}
```

## TO DO: deploy to Kubernetes

1. Create a Dockerfile for the application

2. [OPTIONAL] Test the container locally with something like

    ```bash
    docker run -p3000:3000 <IMAGE>:<TAG>
    ```

3. Build and push the image to the Container Registry

    ```bash
    ibmcloud cr build -t us.icr.io/<NAMESPACE_CR>/<IMAGE>:<TAG> .
    ```

4. [OPTIONAL] Check the container registry if there is the new image

5. Add an healthcheck to the flask app on the `/health` route

6. Add a configmap and a secret on the Kubernetes cluster with the proper values as from the **.env.sample** file

    ```bash
    kubectl create configmap query-config --from-literal=KEY=VALUE
    ```

    ```bash
    kubectl create secret generic query-secret --from-literal=KEY=VALUE
    ```

7. starting from the **sample.yaml**, create a **deployment.yaml** in the main directory, in particular update the image reference and add the secret and configmap variables.

    **Note**: for the moment, create the service with `NodePort` option so that it is easier to test it externally

8. Deploy on Kubernetes cluster



## Useful LOGIN commands

1. Log in to your IBM Cloud account

    ```bash
    ibmcloud login -a cloud.ibm.com -r <REGION> -g <RESOURCE_GROUP>
    ```

2. Set the Kubernetes context to your cluster for this terminal session

    ```bash
    ibmcloud ks cluster config --cluster <CLUSTER_NAME or CLUSTER_ID>
    ```

3. Login to your Container Registry Service on IBM Cloud

    ```bash
    ibmcloud cr login
    ```
