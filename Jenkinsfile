pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Behave tests') {
            steps {
                sh 'source venv/bin/activate && behave'
            }
        }
    }
}
//testin
