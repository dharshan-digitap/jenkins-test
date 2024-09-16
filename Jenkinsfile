node {
    stage('Build') {
        sh 'echo "hello build" > test.txt'
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
}
