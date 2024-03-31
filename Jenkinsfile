pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Clone repository
                    git 'https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853.git'
                    
                    // Build Docker image
                    sh 'docker build -t mlopsimage .'
                    
                }
            }
        }
    }
}
