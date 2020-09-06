pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('Start') {
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
            }
        }
        stage('Setup Container') {
            steps {
                sh 'make setup'
            }
        }
        stage('Linting') {
            steps {
                sh 'make lint'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'make unit'
            }
        }
    }
    post {
        success {
            slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
    }
}