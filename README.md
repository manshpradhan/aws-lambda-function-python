**Automating CloudFront Cache Invalidation with AWS Lambda and CodePipeline**
**Introduction**
Invalidating the CloudFront cache is essential to ensure that users get the latest version of your content after a deployment. In this post, I'll walk you through a Lambda function designed to invalidate CloudFront cache automatically right after deployment, leveraging AWS CodePipeline.

**Prerequisites**
- AWS Account: Ensure you have an active AWS account.
- AWS CLI: Install and configure the AWS CLI.
- AWS Lambda: Familiarity with AWS Lambda and IAM roles.
- AWS CodePipeline: Basic understanding of AWS CodePipeline.

**Setting Up the Lambda Function**
Create Lambda Function:
- Go to the AWS Lambda console and create a new function.
- Copy the code provided in the file(lambda-function.py) into the function editor.
- Set up the necessary IAM role with CloudFrontFullAccess permission.

Environment Variable:
- Add an environment variable named DISTRIBUTION_ID with your CloudFront distribution ID.

**Integrating with AWS CodePipeline and EventBridge**
To trigger the Lambda function after a successful deployment using EventBridge, follow these steps:

Create or Update CodePipeline:
- Ensure your pipeline has a source, build, and deploy stage.

Set Up EventBridge Rule:
- Go to the EventBridge console and create a new rule.
- Configure the rule with the following event pattern to match the "SUCCEED" state of your CodePipeline deploy event.
- Add the following code in the eventbridge rule json editor:
  
  {
  "source": ["aws.codepipeline"],
  "detail-type": ["CodePipeline Pipeline Execution State Change"],
  "detail": {
    "state": ["SUCCEEDED"],
    "pipeline": ["<YourPipelineName>"]
  }
}

**Conclusion**
Automating CloudFront cache invalidation using AWS Lambda, CodePipeline, and EventBridge ensures that your users always receive the latest content. By following the steps above, you can seamlessly integrate this functionality into your deployment process, reducing manual overhead and potential errors.
