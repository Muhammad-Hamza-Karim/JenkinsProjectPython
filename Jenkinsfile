pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'muhammadhamzakarim/pythonapp:latest'
    }

    stages {
        stage('Git Checkout Code') {
            steps {
                 checkout scmGit(
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Muhammad-Hamza-Karim/JenkinsProjectPython'
                    ]] )
            }
        }

        stage('Hamza - Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Hamza - Login to Dockerhub') {
            steps {
                script {
                    echo 'Logging in to Docker Hub...'
                    sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
                }
            }
        }

        stage('Hamza - Push image to Dockerhub') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    sh "docker push ${IMAGE_NAME}"
                }
            }
        }
    }
}
