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
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }

        stage('QualityGate Analysis') {
            timeout(time: 10, unit: 'MINUTES') {
                def qualityGate = waitForQualityGate()
                if (qualityGate.status != 'OK') {
                    error "Pipeline aborted due to quality gate failure: ${qualityGate.status}"
                }
            }
        }

    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}