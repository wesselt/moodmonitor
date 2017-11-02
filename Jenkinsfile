#!groovy

node ('master') {
  try {
    stage 'Checkout'
    checkout scm

    stage('Ansible lint') {
        sh 'ansible-lint mood-deploy.yml -x ANSIBLE0002,ANSIBLE0012'
    }

    stage('SonarQube analysis') {
        // requires SonarQube Scanner 2.8+
        def scannerHome = tool 'sonar';
        withSonarQubeEnv('sonar') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.exclusions=static/** -Dsonar.projectKey=Mood-monitor -Dsonar.sources=."
        }
    }
    stage 'Confirm deployment on prod'
    input message:'Deploy on production?'


        [$class: 'UsernamePasswordMultiBinding', credentialsId: 'svc_jenkins_user',usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']
        {
            sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook mood-deploy.yml -i inventory-test -e \"git_version=${env.BRANCH_NAME} ansible_ssh_user=${env.USERNAME} ansible_ssh_pass=${env.PASSWORD} ansible_become_pass=${env.PASSWORD}\" -v"
        }
    }

   } catch (InterruptedException x) {
      currentBuild.result = "ABORTED"
  } catch (e) {
      currentBuild.result = "FAILED"
      throw e
  }
}
