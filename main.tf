resource "random_id" "uniqufier" {
  byte_length = 8
}

resource "azurerm_resource_group" "rg" {
  name = "data-factory"
  location = "australiaeast"
}

terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state"
    storage_account_name = "terraform-state${azurerm_resource_group.rg.name}"
    container_name       = "tfstate.${azurerm_resource_group.rg.name}"
    key                  = "terraform.${azurerm_resource_group.rg.name}.${random_id.uniqufier.dec}.tfstate"
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_storage_account" "main" {
  name                     = substr("storage${random_id.uniqufier.dec}", 0, 23)
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}
