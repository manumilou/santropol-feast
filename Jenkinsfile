node('docker') { // <1>
    stage('Build') { // <2>
        checkout scm
        sh "whoami"
        sh "pip install -r requirements.txt --user"
        sh "pip install pep8 --user"
        sh "pep8 --count --show-source --exclude=migrations src/"
    }
    stage('Test') {
        /* .. snip .. */
        sh "coverage run --omit=*.virtualenvs*,*virtualenv* src/manage.py test --settings=sous-chef.settings_test member meal order notification delivery note billing page"
        sh "coverage report -m"
    }
    stage('Deploy') {
        /* .. snip .. */
    }
}
