import groovy.json.JsonSlurper
node {
    stage('Print Event Info') {
        // Print the branch name from the webhook payload
        echo "Webhook Payload: ${env.x_github_event}"
        echo "Webhook Payload: ${env.PAYLOAD}"
        // Parse the JSON payload
        def jsonSlurper = new JsonSlurper()
        def payload = jsonSlurper.parseText(env.PAYLOAD)
        echo "Repository Name: ${payload.repository.name}"
           //
    }
}
