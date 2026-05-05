node('asg-workers') {

    stage('Checkout') {
        checkout scm
    }

    stage('pytest') {
        runTest {
            sh '''
            echo "PWD: $(pwd)"
            ls -la
            '''

            sh '''
            pip install -r requirements.txt
            pytest -v
            '''
        }
    }
}