pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build application image') {
            steps {
                script {
                    def image = docker.build("online-shopping:${env.BUILD_NUMBER}")
                    // Keep the built image available on the Jenkins agent for a later deployment stage.
                    echo "Built ${image.id}"
                }
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
