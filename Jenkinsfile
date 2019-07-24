pipeline {
	agent any
	stages {
		stage ('build') {
			echo 'build'
		}
		stage ('test: integration-&-quality') {
			echo 'test integration'
		}
		stage ('test: functional') {
			echo 'test functional'
		}
		stage ('test: load-&-security') {
			echo 'test load'
		}
		stage ('approval') {
			echo 'approval'
		}
		stage ('deploy:prod') {
			echo 'deployment'
		}
	}
}
