terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "s3"{
    bucket = "enem-pyspark-athena-tfstate"
    key    = "terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "enem-pyspark-athena-tfstate"
    profile = "datasouls"

  }

}

provider "aws" {
  region  = var.region
  profile = var.profile
}