pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest'
                bat 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t jenkins-cicd-app .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop jenkins-cicd-app || exit 0'
                bat 'docker rm jenkins-cicd-app || exit 0'
                bat 'docker run -d -p 5000:5000 --name jenkins-cicd-app jenkins-cicd-app'
            }
        }
    }
}