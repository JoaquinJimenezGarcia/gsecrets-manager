# Import the Secret Manager client library.
from google.cloud import secretmanager

def create_secret():
    # GCP project in which to store secrets in Secret Manager.
    project_id = f"{project_id}"

    # ID of the secret to create.
    secret_id = f"{secret_id}"

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the parent name from the project.
    parent = f"projects/{project_id}"

    # Create the parent secret.
    secret = client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"automatic": {}}},
        }
    )

    # Add the secret version.
    version = client.add_secret_version(
        request={"parent": secret.name, "payload": {"data": b"hello world!"}}
    )

    print(version)

    # Access the secret version.
    response = client.access_secret_version(request={"name": version.name})

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    print(f"Plaintext: {payload}")


def access_secret_version(secret):
    # Create a client
    client = secretmanager.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager.AccessSecretVersionRequest(
        name=secret,
    )

    # Make the request
    response = client.access_secret_version(request=request)

    # Handle the response
    print(response.payload.data)

def list_secret_versions():
    # Create a client
    client = secretmanager.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager.ListSecretVersionsRequest(
        parent=f"projects/{project_id_number}/secrets/f{secret_id}",
    )

    # Make the request
    page_result = client.list_secret_versions(request=request)
    all_versions = []

    # Handle the response
    for response in page_result:
        all_versions.append(response.name)
    
    return all_versions[0]

def add_secret_version():
    # Create a client
    client = secretmanager.SecretManagerServiceClient()

    # Initialize request argument(s)
    request = secretmanager.AddSecretVersionRequest(
        parent="parent_value",
    )

    # Make the request
    response = client.add_secret_version(
        request={"parent": f"projects/{project_id_number}/secrets/f{secret_id}", "payload": {"data": b"created automatically"}}
    )

    # Handle the response
    print(response)


#access_secret_version(list_secret_versions())
add_secret_version()