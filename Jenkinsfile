node('asg-workers') {
    stage('Process Webhook and Post Status to GitHub') {
        try {
            sh 'hostname -i'
        } catch (Exception e) {
            status = 'failure'
            echo "Error occurred: ${e.message}"
        }
    }
}