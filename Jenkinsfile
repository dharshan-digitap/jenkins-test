node {
    stage('Process Webhook and Post Status to GitHub') {
        // Extract values using jq from the environment variable directly
        def repoName = env.REPO_NAME
//         def branchName = sh(script: 'echo "${PAYLOAD}" | jq -r ".pull_request.head.ref"', returnStdout: true).trim()
//         def commitSHA = sh(script: 'echo "${PAYLOAD}" | jq -r ".pull_request.head.sha"', returnStdout: true).trim()
        def gitAPIURL = env.REPO_URL

        // Check if any of the extracted values are empty and fail the build if so
        if (!repoName || !branchName || !commitSHA || !gitAPIURL) {
            error("One or more required fields are missing in the payload.")
        }

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
