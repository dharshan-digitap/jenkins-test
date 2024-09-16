node {
    stage('Build') {
        echo 'hello build' > test.txt
    }
    post{
        success {
            archiveArtifacts artifacts: 'test.txt'
        }
    }
    stage('Test') {
        echo 'hello test'
    }
    stage('Deploy') {
        echo 'hello deploy'
    }
}