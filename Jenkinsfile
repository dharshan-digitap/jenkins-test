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
                    sh 'sleep 60'
                }
            }
        }
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}