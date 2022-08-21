
resource "aws_s3_bucket_acl" "bronze_acl" {
  bucket = aws_s3_bucket.bronze.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket.bronze
  ]
}

resource "aws_s3_bucket_acl" "silver_acl" {
  bucket = aws_s3_bucket.silver.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket.silver
  ]
}

resource "aws_s3_bucket_acl" "gold_acl" {
  bucket = aws_s3_bucket.gold.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket.gold
  ]
}

resource "aws_s3_bucket_acl" "athena_acl" {
  bucket = aws_s3_bucket.athena.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket.athena
  ]
}


resource "aws_s3_bucket_acl" "tfstate_acl" {
  bucket = aws_s3_bucket.tfstate.id
  acl    = "private"
  depends_on = [
    aws_s3_bucket.tfstate
  ]
}

resource "aws_s3_bucket_versioning" "tfstate_versioning" {
  bucket = aws_s3_bucket.tfstate.id
  versioning_configuration {
    status = "Enabled"
  }

  depends_on = [
    aws_s3_bucket.tfstate
  ]

}