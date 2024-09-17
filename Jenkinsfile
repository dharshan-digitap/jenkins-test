import groovy.json.JsonSlurper
import groovy.json.JsonOutput

node {
    stage('Print Event Info') {
        // Print the branch name from the webhook payload
        echo "Webhook Payload: ${env.x_github_event}"
        echo "Webhook Payload: ${env.PAYLOAD}"

        // Parse the JSON payload
        def jsonSlurper = new JsonSlurper()
        def payload = jsonSlurper.parseText(env.PAYLOAD)
        echo "Repository Name: ${payload.repository.name}"
        echo "Branch Name: ${payload.ref}"
        echo "Commit SHA: ${payload.head_commit.id}"

        // Extract required information
        def repoName = payload.repository.name
        def branchName = payload.ref.replace("refs/heads/", "")
        def commitSha = payload.head_commit.id
        def buildStatus = currentBuild.currentResult.toLowerCase() // 'success' or 'failure'
        def statusMessage = buildStatus == 'success' ? 'Build succeeded, ready to merge!' : 'Build failed, please fix issues before merging.'

        // Define GitHub API URL
        def githubApiUrl = "https://api.github.com/repos/${payload.repository.full_name}/statuses/${commitSha}"

        // Set GitHub status context
        def context = 'ci/build'

        // Prepare the status payload
        def statusPayload = [
            state: buildStatus,          // 'success', 'error', 'failure'
            target_url: "${env.BUILD_URL}",
            description: statusMessage,
            context: context
        ]

        // Convert the status payload to JSON
        def jsonPayload = JsonOutput.toJson(statusPayload)

        // Notify GitHub using the API
        stage('Notify GitHub') {
            withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                sh """
                curl -X POST -H "Authorization: token ${GITHUB_TOKEN}" \
                    -H "Accept: application/vnd.github.v3+json" \
                    -d '${jsonPayload}' \
                    ${githubApiUrl}
                """
            }
        }
    }
}
