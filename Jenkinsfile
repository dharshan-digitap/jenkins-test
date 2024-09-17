node {
    stage('Print Event Info') {
        // Print the branch name from the webhook payload
        echo "Branch Name: ${env.branch_name}"

        // If you extracted the repository name, print that too
        echo "Repository Name: ${env.repository_name}"

        // If you extracted the commit SHA, print it as well
        echo "Commit SHA: ${env.commit_sha}"
    }
}
