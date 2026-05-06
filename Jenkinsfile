node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Trivy dependency vulnerability check') {
        // Use credentials to get the template content
        withCredentials([string(credentialsId: 'trivy-html-template', variable: 'TRIVY_TEMPLATE_CONTENT')]) {

            // Write the template to a .tpl file (required by Trivy)
            def templateFile = "${env.WORKSPACE}/trivy-template.tpl"
            writeFile file: templateFile, text: TRIVY_TEMPLATE_CONTENT

            // Run Trivy
            sh """
                trivy fs --scanners vuln . \\
                    --format template --template ${templateFile} \\
                    -o dependency_vulnerability_report.html \\
                    --exit-code 1 --severity CRITICAL,HIGH,MEDIUM
            """

            // If no vulnerabilities found, write a simple message
            sh """
                if [ ! -s dependency_vulnerability_report.html ]; then
                    echo "No dependency vulnerabilities found" > dependency_vulnerability_report.html
                fi
            """
        }

        // Archive the report
        archiveArtifacts artifacts: 'dependency_vulnerability_report.html', fingerprint: true
    }

//     stage('Pytest') {
//         def testCmd = """
//         python -m pip install --upgrade pip
//         pip install -r requirements.txt
//         pytest -v
//         """
//         runTest(testCmd)
//     }

//     stage('Vuln Checks') {
//         runVulnerabilityChecks()
//     }

    stage('Post-Cleanup') {
        cleanWs()
    }
}