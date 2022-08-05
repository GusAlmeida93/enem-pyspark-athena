
resource "aws_athena_database" "datasouls" {
  name   = "datasouls"
  bucket = aws_s3_bucket.athena.bucket
  depends_on = [
    aws_s3_bucket.athena
  ]
}











