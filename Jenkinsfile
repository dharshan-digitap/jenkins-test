import groovy.json.JsonSlurper
import groovy.json.JsonOutput

node {
    def payload
    stage('Print Event Info') {
        // Print the branch name from the webhook payload
//         echo "Webhook Payload: ${env.x_github_event}"
//         echo "Webhook Payload: ${env.PAYLOAD}"

        // Parse the JSON payload using a non-serializable method
        def jsonSlurper = new JsonSlurper()
        def payload = jsonSlurper.parseText(env.PAYLOAD)
        echo "Repository Name: ${payload.repository.name}"
        echo "Branch Name: ${payload.pull_request.head.ref}"
        echo "Commit SHA: ${payload.pull_request.head.sha}"
    }

//     stage('Notify GitHub') {
//         // Extract required information
//         def repoName = payload.repository.full_name
//         def commitSha = payload.pull_request.head.sha
//         def buildStatus = currentBuild.currentResult.toLowerCase() // 'success' or 'failure'
//         def statusMessage = buildStatus == 'success' ? 'Build succeeded, ready to merge!' : 'Build failed, please fix issues before merging.'
//
//         // Define GitHub API URL
//         def githubApiUrl = "https://api.github.com/repos/${repoName}/statuses/${commitSha}"
//
//         // Set GitHub status context
//         def context = 'ci/build'
//
//         // Prepare the status payload as a plain map
//         def statusPayload = new LinkedHashMap<String, Object>()
//         statusPayload.put('state', buildStatus)          // 'success', 'error', 'failure'
//         statusPayload.put('target_url', "${env.BUILD_URL}")
//         statusPayload.put('description', statusMessage)
//         statusPayload.put('context', context)
//
//         // Convert the status payload to JSON
//         def jsonPayload = JsonOutput.toJson(statusPayload)
//
//         // Notify GitHub using the API
//         withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
//             sh """
//             curl -X POST -H "Authorization: token ${GITHUB_TOKEN}" \
//                 -H "Accept: application/vnd.github.v3+json" \
//                 -d '${jsonPayload}' \
//                 ${githubApiUrl}
//             """
//         }
//     }
}
