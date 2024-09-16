node {
    def recipient = 'dharshan.s@digitap.ai'
    def sender = 'alerts@digitap.ai' // Specify the sender email address
    def subject = "Pipeline Build Notification: ${currentBuild.result}"
    def body = """\
        <p>Build Status: ${currentBuild.currentResult}</p>
        <p>Job Name: ${env.JOB_NAME}</p>
        <p>Build Number: ${env.BUILD_NUMBER}</p>
        <p>Check the full build details at: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
    """

    try {
        stage('Build') {
            sh 'echo "hello build" > test.txt'
        }

        stage('Test') {
            echo 'Running tests...'
        }

        stage('Deploy') {
            echo 'Deploying application...'
        }

    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        // Send email notifications with the Email Extension Plugin
        emailext subject: subject,
                 body: body,
                 to: recipient,
                 from: sender, // Specify the sender email address here
                 attachLog: true, // Attach build log
                 attachmentsPattern: 'test.txt', // Attach the specific artifact
                 mimeType: 'text/html'

        // Archive artifacts
        archiveArtifacts artifacts: 'test.txt'
    }
}