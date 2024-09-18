node {
    stage('Process Webhook and Post Status to GitHub') {
        // Print the webhook payload for reference
//         echo "Webhook Payload: ${env.PAYLOAD}"

        // Extract values from the PAYLOAD using 'jq' in shell commands
        def repoName = sh(script: "echo '${env.PAYLOAD}' | jq -r '.repository.name'", returnStdout: true).trim()
        def branchName = sh(script: "echo '${env.PAYLOAD}' | jq -r '.pull_request.head.ref'", returnStdout: true).trim()
        def commitSHA = sh(script: "echo '${env.PAYLOAD}' | jq -r '.pull_request.head.sha'", returnStdout: true).trim()
        def gitAPIURL = sh(script: "echo '${env.PAYLOAD}' | jq -r '.repository.url'", returnStdout: true).trim()

        // Print the extracted information for debugging purposes
        echo "Repository Name: ${repoName}"
        echo "Branch Name: ${branchName}"
        echo "Commit SHA: ${commitSHA}"

        // Post the build status to GitHub
        withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
            def buildURL = env.BUILD_URL
            def status = 'success' // You can modify this based on your build result
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