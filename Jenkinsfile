pipeline {
    agent any

    parameters {
        booleanParam(
            name: 'FORCE_TEST_FAILURE',
            defaultValue: false,
            description: 'Enable this to demonstrate a failed test'
        )
    }

    options {
        timestamps()
    }

    stages {
        stage('Source Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Dependency Installation and Build') {
            steps {
                echo 'Checking Python version and creating virtual environment'
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -m compileall -q exporter
                '''
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Running automated tests'
                script {
                    if (params.FORCE_TEST_FAILURE) {
                        withEnv(['FORCE_TEST_FAILURE=1']) {
                            sh '.venv/bin/python -m unittest discover -s tests -v'
                        }
                    } else {
                        sh '.venv/bin/python -m unittest discover -s tests -v'
                    }
                }
            }
        }

        stage('Deployment Packaging') {
            steps {
                echo 'Preparing deployment directory and ZIP artifact'
                sh '''
                    rm -rf deployment metrics-exporter.zip
                    mkdir -p deployment
                    cp -r exporter deployment/
                    cp requirements.txt deployment/
                    cp config.env.example deployment/
                    cp README.md deployment/
                    cd deployment && zip -r ../metrics-exporter.zip .
                '''
                archiveArtifacts artifacts: 'metrics-exporter.zip, deployment/**', fingerprint: true
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed. Check the stage logs.' }
    }
}