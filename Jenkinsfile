pipeline {
    agent any

    tools {
        python 'Python3'
    }

    triggers {
        githubPush() // 👈 Add this to force Jenkins to trigger on every GitHub push
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