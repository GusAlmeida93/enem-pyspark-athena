resource "aws_iam_role" "crawler" {
    name               = "enem-pyspark-athena-glue-crawler"
    assume_role_policy = data.aws_iam_policy_document.policy_glue_service.json
}

resource "aws_iam_role_policy" "glue_gold_policy" {
    name = "enem-pyspark-athena-s3-gold"
    role = aws_iam_role.crawler.id
    policy = data.aws_iam_policy_document.policy_gold_bucket.json
}

data "aws_iam_policy_document" "policy_gold_bucket" {

    statement {

        effect = "Allow"

        actions = [

            "s3:GetObject",
            "s3:PutObject"
        ]

        resources = [
            "${aws_s3_bucket.gold.arn}*"
        ]
    }

}

data "aws_iam_policy_document" "policy_glue_service" {

    statement {

        effect = "Allow"
        actions = ["sts:AssumeRole"]

        principals {
            type        = "Service"
            identifiers = ["glue.amazonaws.com"]
        }
    }

}

resource "aws_iam_role_policy_attachment" "glue_service_role" {
  role       = aws_iam_role.crawler.id
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}