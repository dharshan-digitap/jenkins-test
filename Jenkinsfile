node {
    def recipient = 'dharshan.s@digitap.ai'
    def sender = 'alerts@digitap.ai' // Specify the sender email address
    def body = """\
        <p>Build Status: ${currentBuild.currentResult}</p>
        <p>Job Name: ${env.JOB_NAME}</p>
        <p>Build Number: ${env.BUILD_NUMBER}</p>
        <p>Check the full build details at: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
    """

    try {
        stage('Build') {
            sh 'echo "hello build" > test.txt'
            currentBuild.result = 'SUCCESS'
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
        emailext subject: "Pipeline Build Notification: ${currentBuild.currentResult}"
                 body: body,
                 to: recipient,
                 from: sender,
                 attachLog: true,
                 attachmentsPattern: 'test.txt',
                 mimeType: 'text/html'

        // Archive artifacts
        archiveArtifacts artifacts: 'test.txt'
    }
}