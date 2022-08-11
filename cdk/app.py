#!/usr/bin/env python3
import os
from constructs import Construct
from aws_cdk import (
    App,
    Environment,
    Stack,
    Duration,
    aws_certificatemanager as acm,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
)


class OptimizelyEdgeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Determine domain name and sub domain from the context variables
        domain_name = self.node.try_get_context('domainName')
        subdomain = 'web.{}'.format(domain_name)

        # Assumption: Hosted Zone is created outside of this project
        # Fetch the Route53 Hosted Zone
        zone = route53.HostedZone.from_lookup(
            self, 'Zone',
            domain_name=domain_name,
        )

        # Bucket to store static website files, such as HTML and JavaScript
        bucket = s3.Bucket(self, 'Storage')

        # Copy local files to S3
        s3_deployment.BucketDeployment(
            self, 'Deployment',
            sources=[
                s3_deployment.Source.asset('./src/html'),
            ],
            destination_bucket=bucket,
            prune=False,
            retain_on_delete=False,
        )


app = App()
OptimizelyEdgeStack(app, 'OptimizelyEdge',
    env=Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    ),
)
app.synth()