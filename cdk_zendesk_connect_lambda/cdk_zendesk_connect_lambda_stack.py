from aws_cdk import (
    Stack,
    aws_lambda,
    BundlingOptions
    )


from constructs import Construct
class CdkZendeskConnectLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_construct = aws_lambda.Function(
            self, 'ZendeskConnectLambda',
            handler='zendesk_trigger.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset('lambda',
            bundling=BundlingOptions(
                image=aws_lambda.Runtime.PYTHON_3_9.bundling_image,
                command=[
                    "bash", "-c",
                    "pip install --no-cache -r requirements_lambda.txt -t /asset-output && cp -au . /asset-output"
                        ],
                 ),
            )
        )


