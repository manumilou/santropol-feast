node('docker') { // <1>
    stage('Build') { // <2>
        checkout scm
        sh "pip install -r requirements.txt --user jenkins"
        sh "pip install pep8 --user jenkins"
    }
    stage('Test') {
        /* .. snip .. */
        sh "pep8 --count --show-source --exclude=migrations src/"
        sh "coverage run --omit=*.virtualenvs*,*virtualenv* src/manage.py test --settings=sous-chef.settings_test member meal order notification delivery note billing page"
        sh "coverage report -m"
    }
    stage('Deploy') {
        /* .. snip .. */
    }
}
