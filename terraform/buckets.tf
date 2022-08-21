resource "aws_s3_bucket" "bronze" {
  bucket = "${var.project_name}-bronze"
  tags = {"Name" : "${var.tags["Name"]} Bronze",
          "Project" : var.tags["Project"]}
}

resource "aws_s3_bucket" "silver" {

  bucket = "${var.project_name}-silver"
  tags =  {"Name" : "${var.tags["Name"]} Silver",
           "Project" : var.tags["Project"]}
}

resource "aws_s3_bucket" "gold" {
  bucket = "${var.project_name}-gold"
  tags = {"Name" : "${var.tags["Name"]} Gold",
          "Project" : var.tags["Project"]}
}

resource "aws_s3_bucket" "athena" {
  bucket = "datasouls-athena-query-results"
  tags = {"Name" : "Athena Query Results",
          "Project" : var.tags["Project"]}
}

resource "aws_s3_bucket" "tfstate" {
  bucket = "${var.project_name}-tfstate"
  tags   = {"Name" : "${var.tags["Name"]} Tfstate", 
            "Project" : var.tags["Project"]}
}