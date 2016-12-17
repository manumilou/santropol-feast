node('docker') { // <1>
    stage('Build') { // <2>
        checkout scm
        sh "pip install -r requirements.txt --user jenkins"
    }
    stage('Test') {
        /* .. snip .. */
    }
    stage('Deploy') {
        /* .. snip .. */
    }
}
