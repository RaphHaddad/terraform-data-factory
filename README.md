# README

An example Terraform directory to learn Terraform

## Setup

### Login to Azure

Locally this will be done like below, on Azure DevOps this will be done via an
Azure Service principal.

```cmd
$ az login # Login to Azure
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser.
$ az account list # Get list of available azure subscriptions
[
  {
    "cloudName": "AzureCloud",
    "id": "a-guid-here",
    "isDefault": false,
    "name": "Visual Studio Professional with MSDN",
    "state": "Enabled",
    "tenantId": "a-guid-here",
    "user": {
      "name": "raphael.haddad@something.net",
      "type": "user"
    }
  }
...
...
...
]
$ az account set -s a-guid
```

### Initialise the backend

Terraform needs a backend where it will track state. If it is not configured
it will default to `local` in the below example, it is using Azure Storage.

The storage account and container must be previously created.

```cmd
$ terraform init \ 
    -backend-config="resource_group_name=terraform-state" \
    -backend-config="storage_account_name=terraformstatef0fd47" \
    -backend-config="container_name=terraform-state-files" \
    -backend-config="key=data-factory.tfstate"
Initializing the backend...

Successfully configured the backend "azurerm"! Terraform will automatically
use this backend unless the backend configuration changes.
```

### Validate the template using `terraform plan`

Creates a plan and validates the template

```cmd
$ terraform plan
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:
...
...
...
```

### Provision the Infrastructure on Azure

```cmd
$ terraform apply -auto-approve
Apply complete!
```

## TODO

1. ✅ Create a blank terraform file with a storage account
1. ✅ Use remote state
1. Rename the storage account
1. Set Up Azure DevOps build
1. Parameterise resource group name
1. Ensure Terraform apply fails in CI if invalid tf

## Notes

- Terraform needs state, therefore, the Azure storage account and container
where Terraform stores the file need to be created prior to running
`terraform apply`.
- Terraform blocks provisioning into resource group. There's a one-to-one mapping
of state and the actual resources. This means that if someone edits something
manually, it needs to be reimported into Terraform.