pipeline {
	agent any
	stages {
		stage ('build') {
    steps {
      echo 'test integration'
    }
		}
		stage ('test: integration-&-quality') {
      steps {
        echo 'test integration'
        sh'''
        rm -rf testfile.json
        python test.py
        cat testfile.json
        '''
      }

		}
		stage ('test: functional') {
    steps {
      echo 'test functional'
    }
		}
		stage ('test: load-&-security') {
    steps {
      echo 'test load'
    }
		}
		stage ('approval') {
    steps {
      echo 'test approval'
    }
		}
		stage ('deploy:prod') {
    steps {
      sh'''
      rm -rf testfile.json
      '''
      echo 'test deploy'
    }
		}
	}
}
