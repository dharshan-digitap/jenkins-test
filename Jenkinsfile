import groovy.json.JsonSlurper
node {
    stage('Process Webhook and Post Status to GitHub') {
        def payload_json = env.PAYLOAD.

        def jsonSlurper = new JsonSlurper()
        def payload = jsonSlurper.parseText(payload_json)

        def repoName = payload?.repository?.name ?: "Unknown Repository"
        def branchName = payload?.pull_request?.head?.ref ?: "Unknown Branch"
        def commitSHA = payload?.pull_request?.head?.sha ?: "Unknown SHA"
        def gitAPIURL = payload?.repository?.url ?: "Unknown URL"

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