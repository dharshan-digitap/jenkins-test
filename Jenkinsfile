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

    stage('Vuln Checks') {
        runVulnerabilityChecks()
    }

    stage('Post-Cleanup') {
        cleanWs()
    }
}