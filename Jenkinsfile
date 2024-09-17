node {
    def recipient = 'dharshan.s@digitap.ai,pratik.patil@digitap.ai'
    def sender = 'alerts@digitap.ai' // Specify the sender email address
    def body = """\
        <p>Build Status: ${currentBuild.currentResult}</p>
        <p>Job Name: ${env.JOB_NAME}</p>
        <p>Build Number: ${env.BUILD_NUMBER}</p>
        <p>Check the full build details at: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
    """

    // Set environment variables
    env.FUNCTION_NAME = 'helloworld-dev'
    env.SIGNING_PROFILE = 'test_signing_profile'
    env.BUCKET_NAME = 'code-signing-bucket'
    env.TODAY_DATETIME = new Date().format('yyyy-MM-dd_HH:mm:ss')
    env.BUCKET_KEY = "base_code/lambda_function_${env.TODAY_DATETIME}.zip"

    sh 'aws --version'
    sh 'aws s3api list-buckets'

    try {
        stage('Build Zip') {
            echo 'pwd'
            sh 'zip -r lambda_function.zip *'
        }

        stage('Push to S3') {
            sh """
                aws s3api put-object \
                --bucket ${env.BUCKET_NAME} \
                --key ${env.BUCKET_KEY} \
                --body lambda_function.zip
            """
            echo "Object URL: s3://${env.BUCKET_NAME}/${env.BUCKET_KEY}"
        }

        stage('Code Signing') {
            def response = sh(script: """
                aws signer start-signing-job \
                --source "s3={bucketName=${env.BUCKET_NAME},key=${env.BUCKET_KEY},version='null'}" \
                --destination "s3={bucketName=${env.BUCKET_NAME},prefix=signed_code/signed-}" \
                --profile-name ${env.SIGNING_PROFILE}
                """, returnStdout: true)

            def SIGNING_JOB_ID = sh(script: """
                                echo "${response}" | grep '"jobId":' | cut -d'"' -f4
                                """, returnStdout: true) // delimiter - " -> [f1:,][f2:jobId][f3::][f4-jobIdValue]

            echo "Job ID: ${SIGNING_JOB_ID}"

            def SIGNED_OBJECT_KEY = "signed_code/signed-${env.TODAY_DATETIME}-${SIGNING_JOB_ID}.zip"
            echo "Signed object url: ${SIGNED_OBJECT_KEY}"
        }

    } catch (Exception e) {
        throw e
    } finally {
        // Send email notifications with the Email Extension Plugin
        emailext subject: "${env.JOB_NAME} Pipeline Results: ${currentBuild.currentResult}",
                 body: body,
                 to: recipient,
                 from: sender,
                 attachLog: true,
                 mimeType: 'text/html'
    }
}