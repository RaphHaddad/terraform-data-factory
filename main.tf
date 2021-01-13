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

