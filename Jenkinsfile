node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Gitleaks Scan') {
        def status = sh(script: "gitleaks detect --source=. --no-git --report-format=json --report-path=gitleaks-report.json", returnStatus: true)
        if (status != 0) {
            archiveArtifacts artifacts: 'gitleaks-report.json'
            error("Gitleaks scan failed! Check gitleaks-report.json in artifacts.")
        } else {
            echo "Gitleaks scan passed: no secrets detected."
        }
    }

    stage('Pytest') {
        def testCmd = """
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pytest -v
        """
        runTest(testCmd)
    }

    stage('Vuln Checks') {
        runVulnerabilityChecks()
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}