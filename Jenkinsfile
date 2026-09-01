
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat 'whoami'
                bat 'docker --version'
                bat 'docker ps'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build --no-cache -t jenkins-cicd-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop jenkins-cicd-app || exit /b 0'
                bat 'docker rm jenkins-cicd-app || exit /b 0'
                bat 'docker run -d -p 8501:8501 --name jenkins-cicd-app jenkins-cicd-app:latest'
            }
        }
    }
}

