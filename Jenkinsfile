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
            sh '''
            echo "PWD: $(pwd)"
            ls -la
            '''

            // Safe pip install in root container user
            sh '''
            export HOME=/tmp
            export PATH=$HOME/.local/bin:$PATH
            pip install --user -r requirements.txt
            pytest -v
            '''
        }
    }

    stage('Post-Cleanup') {
        // Optional: clean workspace again to free disk
        cleanWs()
    }
}