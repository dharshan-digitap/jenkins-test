import groovy.json.JsonSlurper

node {
    stage('Process Webhook and Post Status to GitHub') {
        // Print the branch name from the webhook payload
        echo "Webhook Payload: ${env.PAYLOAD}"

        // Parse the JSON payload
        def jsonSlurper = new JsonSlurper()
        def payload = jsonSlurper.parseText(env.PAYLOAD)
        def repoName = payload.repository.name
        def branchName = payload.pull_request.head.ref
        def commitSHA = payload.pull_request.head.sha

        echo "Repository Name: ${repoName}"
        echo "Branch Name: ${branchName}"
        echo "Commit SHA: ${commitSHA}"

        // Post the build status to GitHub
        withCredentials([string(credentialsId: 'github-token-id', variable: 'GITHUB_TOKEN')]) {
            def gitAPIURL = payload.repository.url
            def buildURL = env.BUILD_URL
            def status = 'success' // You can change this based on your pipeline result
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