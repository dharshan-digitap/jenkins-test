node('asg-workers') {

    stage('Prepare Workspace') {
        // Clean previous job workspace temp and build files
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

    stage('Post-Cleanup') {
        // Optional: clean workspace again to free disk
        cleanWs()
    }
}