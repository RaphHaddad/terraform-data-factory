resource "random_id" "uniqufier" {
  byte_length = 8
}

resource "azurerm_resource_group" "rg" {
  name = "data-factory"
  location = "australiaeast"
}

provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {}
}

resource "azurerm_storage_account" "main" {
  name                     = substr("storage${random_id.uniqufier.dec}", 0, 23)
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}
