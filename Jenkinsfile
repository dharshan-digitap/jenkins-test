node('asg-workers') {

    stage('ECR Login') {
        sh '''
            aws ecr get-login-password --region ap-south-1 \
            | docker login --username AWS --password-stdin \
            959812570231.dkr.ecr.ap-south-1.amazonaws.com
        '''
    }

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