resource "aws_s3_bucket" "bronze" {
  bucket = "enem-pyspark-athena-bronze"
  tags = {
    Name    = "ENEM Pyspark Athena Bronze"
    Project = "MBA XP Engenharia de Dados"
  }
}

resource "aws_s3_bucket" "silver" {
  bucket = "enem-pyspark-athena-silver"
  tags = {
    Name    = "ENEM Pyspark Athena Silver"
    Project = "MBA XP Engenharia de Dados"
  }
}

resource "aws_s3_bucket" "gold" {
  bucket = "enem-pyspark-athena-gold"
  tags = {
    Name    = "ENEM Pyspark Athena Gold"
    Project = "MBA XP Engenharia de Dados"
  }
}

resource "aws_s3_bucket" "athena" {
  bucket = "datasouls-athena-query-results"
  tags = {
    Name = "Athena Query Results"
  }
}