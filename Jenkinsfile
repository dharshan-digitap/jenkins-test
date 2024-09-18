if (env.x_github_event == 'push') {
    node {
        stage('Process Webhook and Post Status to GitHub') {
            def status = 'success' // Default status

            try {
                // Extract values from environment variables
                def repoName = env.REPO_NAME
                def gitAPIURL = env.REPO_URL
                def branchName = env.BRANCH_NAME
                def author = env.AUTHOR ?: 'default-author'
                def commitSHA = env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH

                // Log extracted values
                echo "event_type: ${env.x_github_event}"
                echo "Repo name: ${repoName}"
                echo "Repo url: ${gitAPIURL}"
                echo "Repo author: ${author}"
                echo "commit SHA: ${env.COMMIT_SHA_FROM_PUSH}"

                // Post the build status to GitHub
                postBuildStatusToGitHub(status, env.BUILD_URL, gitAPIURL, commitSHA)

            } catch (Exception e) {
                // If any exception occurs, mark the status as 'failure'
                status = 'failure'
                echo "Error occurred: ${e.message}"
                // Optionally, send a failure status to GitHub even if the pipeline encounters an error
                postBuildStatusToGitHub(status, env.BUILD_URL, gitAPIURL, commitSHA)
            }
        }
    }
}

// Function to post build status to GitHub
def postBuildStatusToGitHub(status, buildURL, gitAPIURL, commitSHA) {
    withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
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
