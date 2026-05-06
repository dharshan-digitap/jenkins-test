node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Trivy Dependency Vulnerability Check') {
        withCredentials([string(credentialsId: 'trivy-html-template', variable: 'TRIVY_TEMPLATE_CONTENT')]) {
            def templateFile = "${env.WORKSPACE}/trivy-template.tpl"
            writeFile file: templateFile, text: TRIVY_TEMPLATE_CONTENT

            def status = sh(script: """
                trivy fs --scanners vuln . \
                    --format template --template @${templateFile} \
                    -o dependency_vulnerability_report.html \
                    --exit-code 1 --severity CRITICAL,HIGH,MEDIUM
            """, returnStatus: true)

            if (status != 0) {
                archiveArtifacts artifacts: 'dependency_vulnerability_report.html'
                error("Trivy found CRITICAL/HIGH/MEDIUM vulnerabilities! Check dependency_vulnerability_report.html in artifacts.")
            } else {
                echo "Trivy scan passed: no CRITICAL/HIGH/MEDIUM vulnerabilities found."
            }
        }
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