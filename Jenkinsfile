pipeline {
    agent any

    stages {
        stage('Set up virtual env') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Behave Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    behave
                '''
            }
        }
    }
}
