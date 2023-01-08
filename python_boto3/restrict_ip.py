{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": [
                        "0.0.0.0/32" #특정ip
                    ]
                },
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "true",
                    "aws:ViaAWSService": "false"
                }
            }
        }
    ]
}