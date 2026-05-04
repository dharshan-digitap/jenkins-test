node('asg-workers') {
    stage('Process Webhook and Post Status to GitHub') {
        try {
            runTest {

                echo "Running on node:"
                sh 'hostname -i'

                sh '''
                    echo "MySQL & Redis are available here"
                '''
            }
        } catch (Exception e) {
            status = 'failure'
            echo "Error occurred: ${e.message}"
        }
    }
}