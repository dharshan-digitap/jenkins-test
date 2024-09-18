node {
    stage('Process Webhook and Post Status to GitHub') {
        // Extract values from the PAYLOAD using 'jq' without echo
        def repoName = sh(script: "jq -r '.repository.name' <<< '${env.PAYLOAD}' 2>/dev/null", returnStdout: true).trim()
        def branchName = sh(script: "jq -r '.pull_request.head.ref' <<< '${env.PAYLOAD}' 2>/dev/null", returnStdout: true).trim()
        def commitSHA = sh(script: "jq -r '.pull_request.head.sha' <<< '${env.PAYLOAD}' 2>/dev/null", returnStdout: true).trim()
        def gitAPIURL = sh(script: "jq -r '.repository.url' <<< '${env.PAYLOAD}' 2>/dev/null", returnStdout: true).trim()

        // Post the build status to GitHub
        withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
            def buildURL = env.BUILD_URL
            def status = 'success' // Modify this based on your pipeline result
            def description = 'Build completed successfully'
            def context = 'continuous-integration/jenkins'

            // Post the status to GitHub using curl
            sh """
                curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
                -H "Content-Type: application/json" \
                --data '{
                    "state": "${status}",
                    "target_url": "${buildURL}",
                    "description": "${description}",
                    "context": "${context}"
                }' \
                ${gitAPIURL}/statuses/${commitSHA}
            """
        }
    }
}