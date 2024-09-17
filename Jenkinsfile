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
        echo "Branch Name: ${payload.pull_request.head.ref}"
        echo "Commit SHA: ${payload.pull_request.head.sha}"

        // Extract required information
        def repoName = payload.repository.full_name
        def commitSha = payload.pull_request.head.sha
        def buildStatus = currentBuild.currentResult.toLowerCase() // 'success' or 'failure'
        def statusMessage = buildStatus == 'success' ? 'Build succeeded, ready to merge!' : 'Build failed, please fix issues before merging.'

        // Define GitHub API URL
        def githubApiUrl = "https://api.github.com/repos/${repoName}/statuses/${commitSha}"

        // Set GitHub status context
        def context = 'ci/build'

        // Prepare the status payload
        def statusPayload = [
            state: buildStatus,          // 'success', 'error', 'failure'
            target_url: "${env.BUILD_URL}",
            description: statusMessage,
            context: context
        ]

        // Convert the status payload to JSON string
        def jsonPayload = JsonOutput.toJson(statusPayload)

        // Notify GitHub using the API
        stage('Notify GitHub') {
            withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                script {
                    // Write the payload to a file to avoid serialization issues
                    def file = new File("${JENKINS_HOME}/workspace/${JOB_NAME}/payload.json")
                    file.text = jsonPayload

                    // Use 'sh' step with returnStdout to avoid exposing secrets
                    def result = sh(script: "curl -X POST -H \"Authorization: token ${GITHUB_TOKEN}\" -H \"Accept: application/vnd.github.v3+json\" -d @payload.json ${githubApiUrl}", returnStdout: true).trim()
                    echo "Curl result: ${result}"
                }
            }
        }
    }
}
