pipeline {
  agent any
  stages {
    stage('git-get-code') {
      steps {
        git(url: 'https://github.com/jaliagag/django_portfolio', branch: 'dev')
      }
    }

    stage('build') {
      parallel {
        stage('see') {
          steps {
            sh 'pwd && ls -la'
          }
        }

        stage('django-build') {
          steps {
            sh 'docker build -t leapp:latest .'
          }
        }

      }
    }

    stage('deploy') {
      steps {
        sh 'echo "some shit"'
      }
    }

  }
}