node{
    stage('Checkout') {
        checkout scm
    }
    stage('print environment'){
        echo "Build Parameters: ${env.BRANCH_NAME}"
    }
}
