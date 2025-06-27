pipeline {
    agent any

    triggers {
        githubPush() // 👈 Forces build on every push
    }

    tools {
        python 'Python3'
    }

    stages {
        stage('Install dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    behave
                '''
            }
        }
    }
}