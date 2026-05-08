node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    throttle(['sonar-scans']) {
        stage('SonarQube Analysis') {
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

        stage('QualityGate Analysis') {
            timeout(time: 10, unit: 'MINUTES') {
                def qualityGate = waitForQualityGate()
                if (qualityGate.status != 'OK') {
                    error "❌ Pipeline failed due to Quality Gate: ${qualityGate.status}"
                }
            }
        }
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}