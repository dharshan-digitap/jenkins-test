node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Gitleaks Scan') {
        echo "Starting Gitleaks scan..."

        // Run Gitleaks and capture exit code
        def status = sh(script: "gitleaks detect --source=. --verbose", returnStatus: true)

        if (status != 0) {
            echo "Gitleaks detected secrets! Exiting..."
            error("Gitleaks scan failed with exit code ${status}")
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

    stage('Post-Cleanup') {
        cleanWs()
    }
}