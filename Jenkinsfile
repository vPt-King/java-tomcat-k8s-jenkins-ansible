pipeline{
    agent any
    tools{
        maven 'maven'
    }
    stages{
        stage("clone")
        {
            steps{
                git 'https://github.com/vPt-King/java-tomcat-k8s-jenkins-ansible.git'
            }
        }
        stage("test")
        {
            steps{
                sh "mvn clean test"
            }
        }
        stage("build")
        {
            steps{
                sh "mvn clean install"
            }
        }
        stage("connect ansible")
        {
            steps{
                ansiblePlaybook credentialsId: 'thanhnga', installation: 'Ansible', inventory: '/var/lib/jenkins/workspace/java-tomcat/inventory.yaml', playbook: '/var/lib/jenkins/workspace/java-tomcat/ansible.yaml', vaultTmpPath: ''
            }
        }
    }
}