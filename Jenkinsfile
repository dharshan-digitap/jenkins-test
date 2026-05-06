node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Gitleaks Scan') {
        echo "Starting Gitleaks scan..."
        // Adjust path if Gitleaks is installed elsewhere
        sh """
        gitleaks detect --source=. --verbose
        """
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