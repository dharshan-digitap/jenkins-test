// node {
//     stage('Process Webhook and Post Status to GitHub') {
//         def status = 'success' // Default status
//
//         try {
//             // Check the GitHub event type
//             if (env.x_github_event == 'pull_request') {
//                 // Extract values from environment variables
//                 def repoName = env.REPO_NAME
//                 def gitAPIURL = env.REPO_URL
//                 def branchName = env.BRANCH_NAME
//                 def author = env.AUTHOR ?: 'default-author'
//                 def commitSHA = env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH
//
//                 // Log extracted values
//                 echo "event_type: ${env.x_github_event}"
//                 echo "event_action: ${env.ACTION}"
//
//
//                 echo "Repo name: ${repoName}"
//                 echo "Repo url: ${gitAPIURL}"
//                 echo "Repo author: ${author}"
//                 echo "commit Sha: ${commitSHA}"
//
//
//                 // Post the build status to GitHub
//                 postBuildStatusToGitHub(status, env.BUILD_URL, gitAPIURL, commitSHA)
//             }
//         } catch (Exception e) {
//             // If any exception occurs, mark the status as 'failure'
//             status = 'failure'
//             echo "Error occurred: ${e.message}"
//             // Optionally, you can send a failure status to GitHub even if the pipeline encounters an error
//             postBuildStatusToGitHub(status, env.BUILD_URL, env.REPO_URL, env.COMMIT_SHA_FROM_PR ?: env.COMMIT_SHA_FROM_PUSH)
//         }
//     }
// }
//
// // Function to post build status to GitHub
// def postBuildStatusToGitHub(status, buildURL, gitAPIURL, commitSHA) {
//     withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
//         def description = status == 'success' ? 'Build completed successfully' : 'Build failed'
//         def context = 'continuous-integration/jenkins'
//
//         // Use a secure method to handle secrets
//         sh """
//             curl -X POST -H "Authorization: token \$GITHUB_TOKEN" \
//             -H "Content-Type: application/json" \
//             --data '{
//                 "state": "${status}",
//                 "target_url": "${buildURL}",
//                 "description": "${description}",
//                 "context": "${context}"
//             }' \
//             ${gitAPIURL}/statuses/${commitSHA}
//         """
//     }
// }

node {
    // Define environment variables for webhook details
    def action = '' // This will capture the action type from the webhook
    def ref = ''
    def prNumber = null

    // Trigger the pipeline based on the webhook event
    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'ref', value: '$.ref'],
                [key: 'action', value: '$.action'],               // For pull request events
                [key: 'pull_request', value: '$.pull_request.number'], // PR number if the event is a pull request
                [key: 'after', value: '$.after'],
                [key: 'repository_name', value: '$.repository.full_name']
            ],
            causeString: 'Triggered by $ref on $repository_name',
            token: 'your-webhook-token',
            printContributedVariables: false,
            printPostContent: false,
            silentResponse: true
        )
    }

    stage('Check Event Type') {
        steps {
            script {
                // If the action field is related to a pull request, skip the pipeline
                if (action == 'opened' || action == 'closed' || action == 'synchronize') {
                    echo "This is a pull request event. Skipping pipeline."
                    // Mark the build as not built and exit early
                    currentBuild.result = 'NOT_BUILT'
                    return
                } else {
                    echo "This is a push event. Proceeding with the pipeline."
                }
            }
        }
    }

    // Proceed with your regular pipeline for push events
    stage('Build and Test') {
        steps {
            echo "Building and testing for commit ${env.after}"
            // Add your build steps here
        }
    }
}
