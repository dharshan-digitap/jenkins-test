node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Gitleaks Scan') {
        echo "Starting Gitleaks scan..."

        def status = sh(script: "gitleaks dir . --verbose", returnStatus: true)

        if (status != 0) {
            error("Gitleaks scan failed — secrets detected!")
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