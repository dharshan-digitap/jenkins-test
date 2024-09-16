node {
    try{
        stage('Build') {
            // Printing build information
            echo "Build Number: ${env.BUILD_NUMBER}"
            echo "Job Name: ${env.JOB_NAME}"
            echo "Build URL: ${env.BUILD_URL}"
            sh 'echo "hello build" > test.txt'

            echo "Build Status: ${currentBuild.currentResult}"
            currentBuild.result = 'SUCCESS'
        }
        if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                archiveArtifacts artifacts: 'test.txt'
            }

        stage('Test') {
            echo 'hello test'
        }
        stage('Deploy') {
            echo 'hello deploy'
        }
    } catch (Exception e) {
         currentBuild.result = 'FAILURE'
         throw e
    } finally {
         emailext subject: "Pipeline Build Notification : ${currentBuild.result}"
                  to: 'dharshan.s@digitap.ai',
                  attachLog: true,
                  attachmentsPattern: 'test.txt'
    }
}
