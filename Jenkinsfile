pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-v /tmp:/tmp'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'python main.py'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'python -m unittest test_main.py'
                }
            }
        }
    }
    post {
        always {
            // Clean up the workspace
            cleanWs()
            echo 'Workspace cleaned up!'
        }
        success {
            // Archive the main.py script as an artifact
            archiveArtifacts artifacts: 'main.py', fingerprint: true
            echo 'main.py archived as artifact.'

            // Sending an email notification (assuming Jenkins is configured with an SMTP server)
            mail to: 'team@example.com',
                 subject: "Success: ${currentBuild.fullDisplayName}",
                 body: "The build was successful! Build details: ${env.BUILD_URL}"
        }
        failure {
            // Sending an email notification on failure
            mail to: 'team@example.com',
                 subject: "Failure: ${currentBuild.fullDisplayName}",
                 body: "The build failed. Check out the details: ${env.BUILD_URL}"
        }
    }
}