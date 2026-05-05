node('asg-workers') {

    stage('Prepare Workspace') {
        // Clean previous job workspace temp and build files
        cleanWs()
    }

    stage('Checkout') {
        checkout scm
    }

    stage('Pytest') {
    runTest {
       sh 'echo hello'
    }

    }

    stage('Post-Cleanup') {
        // Optional: clean workspace again to free disk
        cleanWs()
    }
}