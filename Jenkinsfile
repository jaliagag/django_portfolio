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
            sh 'cd Proyecto1 && python manage.py runserver'
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