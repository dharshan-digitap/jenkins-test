node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

//     stage('Pytest') {
//         def testCmd = """
//         python -m pip install --upgrade pip
//         pip install -r requirements.txt
//         pytest -v
//         """
//         runTest(testCmd)
//     }

    stage('SonarQube Debug throttle') {
        throttle(['dev-build-throttle']) {
            echo "ENTERED THROTTLE: ${env.BUILD_NUMBER} at ${new Date()}"
            sh "sleep 120"
        }
    }

    stage('SonarQube Analysis') {
        throttle(['dev-build-throttle']) {
            def scannerHome = tool 'SonarScanner'

            withSonarQubeEnv('sonarqube') {
                withCredentials([string(credentialsId: 'sonartoken', variable: 'SONAR_TOKEN')]) {
                    sh """
                        ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=my-python-app \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://10.0.3.217:9000 \
                        -Dsonar.token=$SONAR_TOKEN
                    """
                }
            }
        }
    }

    stage('QualityGate Analysis') {
        timeout(time: 2, unit: 'MINUTES') {
            def qualityGate = waitForQualityGate()
            if (qualityGate.status != 'OK') {
                error "❌ Pipeline failed due to Quality Gate: ${qualityGate.status}"
            }
        }
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}