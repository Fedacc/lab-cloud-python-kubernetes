# lab-cloud-python-kubernetes

## Run locally
Install dependencies

```
pip install -r requirements.txt
```

Create `.env` file following `.env.sample` as a template, add the proper credentials that can be obtained by registering with no charge at https://cloud.ibm.com/login and deploying an instance of [Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery)

Start the flask server locally
```
python run.py
```

Send the queries via POST request to the server with the following payload
```
{
    "query": "string to search"
}
```
