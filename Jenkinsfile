node('asg-workers') {

    stage('Prepare Workspace') {
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Trivy dependency vulnerability check') {
        configFileProvider([configFile(fileId: 'trivy-html-template', variable: 'TRIVY_TEMPLATE')]) {
            sh """
                # Rename the temporary file to have .tpl extension for Trivy
                TEMPLATE_FILE="\${TRIVY_TEMPLATE}.tpl"
                cp "\$TRIVY_TEMPLATE" "\$TEMPLATE_FILE"

                # Run Trivy with the proper template
                trivy fs --scanners vuln . \
                    --format template \
                    --template \$TEMPLATE_FILE \
                    -o dependency_vulnerability_report.html \
                    --exit-code 1 --severity CRITICAL,HIGH,MEDIUM || true

                # If the report is empty, add a simple message
                if [ ! -s dependency_vulnerability_report.html ]; then
                    echo "No dependency vulnerabilities found" >> dependency_vulnerability_report.html
                fi
            """
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