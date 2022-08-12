resource "aws_glue_catalog_database" "glue_database" {
  name = "enem-pyspark-athena"
}


resource "aws_glue_crawler" "gold_crawler" {
  database_name = aws_glue_catalog_database.glue_database.name
  name          = "enem-pyspark-athena-gold"
  role          = aws_iam_role.crawler.arn

  s3_target {
    path = "s3://${aws_s3_bucket.gold.bucket}"
  }
}