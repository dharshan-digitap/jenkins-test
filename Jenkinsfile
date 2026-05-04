node('asg-workers') {

    stage('Run ECR Image in Docker Agent') {

        docker.image('959812570231.dkr.ecr.ap-south-1.amazonaws.com/platform/jenkins-worker-agent:latest')
              .inside {

            stage('Verify Environment') {
                sh '''
                    echo "Inside container"
                    whoami || true
                    hostname
                '''
            }

            stage('Check Tools') {
                sh '''
                    java -version || true
                    git --version || true
                    aws --version || true
                    docker --version || true
                '''
            }

        }
    }
}