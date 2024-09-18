node {
    def status = 'success'
    def repoName = env.REPO_NAME
    def branchName = env.BRANCH_NAME
    def author = env.AUTHOR ?: env.AUTHOR_NAME_FROM_PR
    def commitSHA = env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH

    try {
        // Log extracted values
        echo "event_type: ${env.x_github_event}"
        echo "event_action: ${env.ACTION}"
        echo "Repo name: ${repoName}"
        echo "Repo author: ${author}"
        echo "commit SHA: ${commitSHA}"

        // Set environment variables
        env.FUNCTION_NAME = 'helloworld-dev'
        env.SIGNING_PROFILE = 'test_signing_profile'
        env.BUCKET_NAME = 'code-signing-bucket'
        env.TODAY_DATETIME = new Date().format('yyyy-MM-dd_HH:mm:ss')
        env.BUCKET_KEY = "base_code/lambda_function_${env.TODAY_DATETIME}.zip"

        // PR CLOSED JOBS
        if (env.x_github_event == 'pull_request' && env.ACTION == 'closed') {
            stage('Build Zip') {
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

                def jsonResponse = readJSON(text: response)
                def SIGNING_JOB_ID = jsonResponse.jobId
                echo "Job ID: ${SIGNING_JOB_ID}"

                env.SIGNED_OBJECT_KEY_PATH = "s3://${env.BUCKET_NAME}/signed_code/signed-${env.TODAY_DATETIME}-${SIGNING_JOB_ID}.zip"
                echo "Signed object URL: ${env.SIGNED_OBJECT_KEY_PATH}"
            }
        }

        // PUSH JOBS
        if (env.x_github_event == 'push' || (env.x_github_event == 'pull_request' && env.ACTION == 'closed')) {
//             stage('OWASP Dependency Check') {
//                 def dependencyCheckHome = tool 'OWASP Dependency-Check Vulnerabilities'
//                 sh "${dependencyCheckHome}/bin/dependency-check.sh --project EV_UANSTACK --scan . --format HTML --out dependency-check-report.html"
//             }
//
//             stage('SonarQube Analysis') {
//                 def scannerHome = tool 'SonarScanner'
//                 withSonarQubeEnv() {
//                     sh "${scannerHome}/bin/sonar-scanner"
//                 }
//             }
               stage('Code Scanning and Vulnerabilities check') {
                    echo 'Running Code Scanning and Vulnerabilities check'
               }
        }

    } catch (Exception e) {
        status = 'failure'
        echo "Error occurred: ${e.message}"
    } finally {
        if (env.x_github_event == 'pull_request' && env.ACTION == 'closed') {
            postBuildStatusToGitHub(status, commitSHA)
        }
        sendEmailAlert(status)
    }
}

// Function to post build status to GitHub
def postBuildStatusToGitHub(status, commitSHA) {
    withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
        def description = status == 'success' ? 'Build completed successfully' : 'Build failed'
        def context = 'continuous-integration/jenkins'

        sh """
            curl -X POST -H "Authorization: token \$GITHUB_TOKEN" \
            -H "Content-Type: application/json" \
            --data '{
                "state": "${status}",
                "target_url": "${env.BUILD_URL}",
                "description": "${description}",
                "context": "${context}"
            }' \
            ${env.REPO_URL}/statuses/${commitSHA}
        """
    }
}

def sendEmailAlert(status) {
    def recipient = 'dharshan.s@digitap.ai,pratik.patil@digitap.ai'
    def sender = 'alerts@digitap.ai'
    def body = """\
        <p>Build Status: ${status}</p>
        <p>Job Name: ${env.JOB_NAME}</p>
        <p>Build Number: ${env.BUILD_NUMBER}</p>
        <p>s3 signed object link at: <a href="${env.SIGNED_OBJECT_KEY_PATH}">${env.SIGNED_OBJECT_KEY_PATH}</a></p>
        <p>Check the full build details at: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
    """
    emailext subject: "${env.JOB_NAME} Pipeline Results: ${currentBuild.currentResult}",
           body: body,
           to: recipient,
           from: sender,
           attachLog: true,
           mimeType: 'text/html'
}
