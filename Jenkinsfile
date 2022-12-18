pipeline {
  agent any
  stages {
    stage('git-get-code') {
      steps {
        git(url: 'https://github.com/jaliagag/django_portfolio', branch: 'dev')
      }
    }

    stage('pwd-ls') {
      steps {
        sh 'pwd && ls -la'
      }
    }

  }
}