node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Pytest') {
        def testCmd = """
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pytest -v
        """
        runTest(testCmd)
    }

    stage('SonarQube Analysis') {
        withSonarQubeEnv('sonarqube') {
            sh """
            sonar-scanner \
              -Dsonar.projectKey=my-python-app \
              -Dsonar.sources=. \
              -Dsonar.python.version=3 \
              -Dsonar.host.url=http://sonarqube:9000 \
              -Dsonar.login=${SONAR_TOKEN}
            """
        }
    }

    stage('Quality Gate') {
        timeout(time: 5, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
        }
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}