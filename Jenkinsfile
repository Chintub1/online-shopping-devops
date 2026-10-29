pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test application') {
            steps {
                script {
                    // The test image runs the unit tests during its Docker build.
                    docker.build("online-shopping-test:${env.BUILD_NUMBER}", "-f Dockerfile.test .")
                }
            }
        }
        stage('Build application image') {
            steps {
                script {
                    def image = docker.build("online-shopping:${env.BUILD_NUMBER}")
                    // Keep the image available on the Jenkins agent for deployment below.
                    echo "Built ${image.id}"
                }
            }
        }
        stage('Deploy application') {
            steps {
                bat '''
                    docker rm -f online-shopping-app online-shopping-updated online-shopping-vscode 2>NUL
                    docker run -d --name online-shopping-app --restart unless-stopped -p 5000:5000 online-shopping:%BUILD_NUMBER%
                '''
            }
        }
    }

    post {
        success {
            echo 'Online Shopping System pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the stage log above to find the issue.'
        }
    }
}
