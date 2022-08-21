resource "aws_dynamodb_table" "tfstate" {
  name         = "${var.project_name}-tfstate"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = var.tags
}