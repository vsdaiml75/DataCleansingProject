pipeline {
    agent any
    
    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/vsdaiml75/DataCleansingProject.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_USERNAME}/data-cleansing-image")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python test_clean_data.py'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy to Dev') {
            steps {
                script {
                    sh 'docker stop data-cleansing-container-dev || true && docker rm data-cleansing-container-dev || true'
                    dockerImage.run('-d --name data-cleansing-container-dev')
                }
            }
        }
        stage('Deploy to Staging') {
            steps {
                script {
                    // Check if tests passed
                    if (currentBuild.result == 'SUCCESS') {
                        sh 'docker stop data-cleansing-container-staging || true && docker rm data-cleansing-container-staging || true'
                        dockerImage.run('-d --name data-cleansing-container-staging')
                    }
                }
            }
        }
    }
    post {
        always {
            mail to: 'vsdaiml75@gmail.com',
                subject: "Pipeline ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                body: "Pipeline ${currentBuild.fullDisplayName} finished with status: ${currentBuild.currentResult}"
        }
    }
}
