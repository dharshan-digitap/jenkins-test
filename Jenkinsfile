node('asg-workers') {
    stage('Process Webhook and Post Status to GitHub') {
        try {
            sh 'whoami'
        } catch (Exception e) {
            status = 'failure'
            echo "Error occurred: ${e.message}"
        }
    }
}