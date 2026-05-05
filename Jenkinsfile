node('asg-workers') {

    stage('pytest') {
        runTest {
            sh '''
            pip install -r requirements.txt
            pytest -v
            '''
        }
    }
}