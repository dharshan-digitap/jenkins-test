node{
    stage('Checkout') {
        checkout scm
    }
    stage('print environment'){
        echo "Branch: ${env.BRANCH_NAME}"
        echo "Commit: ${env.GIT_COMMIT}"
        echo "Commit Author: ${env.GIT_AUTHOR_NAME} (${env.GIT_AUTHOR_EMAIL})"
        echo "Committer: ${env.GIT_COMMITTER_NAME} (${env.GIT_COMMITTER_EMAIL})"
        echo "Git URL: ${env.GIT_URL}"
        echo "Previous Commit: ${env.GIT_PREVIOUS_COMMIT}"
    }
}