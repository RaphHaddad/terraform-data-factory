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
$ terraform apply
Apply complete!
```

## TODO

1. Create a blank terraform file with a storage account
1. Use remote state
1. Rename the storage account
1. Set Up Azure DevOps build
1. Parameterise resource group name
1. Ensure Terraform apply fails in CI if invalid tf