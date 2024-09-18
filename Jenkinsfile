node {
    stage('Process Webhook and Post Status to GitHub') {
        // Extract values using jq from the environment variable directly
        def repoName = env.REPO_NAME
//         def branchName = sh(script: 'echo "${PAYLOAD}" | jq -r ".pull_request.head.ref"', returnStdout: true).trim()
//         def commitSHA = sh(script: 'echo "${PAYLOAD}" | jq -r ".pull_request.head.sha"', returnStdout: true).trim()
        def gitAPIURL = env.REPO_URL
        def branchName = env.BRANCH_NAME
        def author = env.AUTHOR ?: 'default-author'
        def commitSHA = env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH

        // Check if any of the extracted values are empty and fail the build if so
        echo "event_type: ${env.x_github_event}"
        echo "Repo name: ${repoName}"
        echo "Repo url: ${gitAPIURL}"
        echo "Repo author: ${author}"
        echo "commit Sha: ${commitSHA}"

        // Post the build status to GitHub
        withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
            def buildURL = env.BUILD_URL
            def status = currentBuild.currentResult == 'SUCCESS' ? 'success' : 'failure' // Modify as needed
            def description = status == 'success' ? 'Build completed successfully' : 'Build failed'
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
