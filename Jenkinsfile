pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NehaAnalyticsHub/Mlops_Assignment1_i200677_i201853.git'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t a1_image .'
            }
        }

    }
}