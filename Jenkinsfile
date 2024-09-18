node {
    try {
        def status = 'success'
        def repoName = env.REPO_NAME
        def branchName = env.BRANCH_NAME
        def author = env.AUTHOR ?: 'default-author'
        def commitSHA = env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH

        // Log extracted values
        echo "event_type: ${env.x_github_event}"
        echo "event_action: ${env.ACTION}"
        echo "Repo name: ${repoName}"
        echo "Repo author: ${author}"
        echo "commit Sha: ${commitSHA}"

        // stages
        if (env.x_github_event == 'push' || env.x_github_event == 'pull_request') {
            stage('Code Scanning') {
                // Post the build status to GitHub
                postBuildStatusToGitHub(status, commitSHA)
            }
        }

        if (env.x_github_event == 'pull_request' && env.ACTION == 'closed') {
            stage('Deploy') {
                echo 'Deploying and code scanning'
                postBuildStatusToGitHub(status, commitSHA)
            }
        }

    } catch (Exception e) {
        // If any exception occurs, mark the status as 'failure'
        status = 'failure'
        echo "Error occurred: ${e.message}"
        postBuildStatusToGitHub(status, env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH)
    }
}

// Function to post build status to GitHub
def postBuildStatusToGitHub(status, commitSHA) {
    withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
        def description = status == 'success' ? 'Build completed successfully' : 'Build failed'
        def context = 'continuous-integration/jenkins'

        // Use a secure method to handle secrets
        sh """
            curl -X POST -H "Authorization: token \$GITHUB_TOKEN" \
            -H "Content-Type: application/json" \
            --data '{
                "state": "${status}",
                "target_url": "${env.BUILD_URL}",
                "description": "${description}",
                "context": "${context}"
            }' \
            ${env.REPO_URL}/statuses/${commitSHA}
        """
    }
}
