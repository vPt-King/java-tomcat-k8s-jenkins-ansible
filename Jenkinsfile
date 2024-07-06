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
                ansiblePlaybook credentialsId: 'thanh', installation: 'Ansible', inventory: '/home/thanhnga/Documents/learn/project/javaweb/inventory.ini', playbook: '/home/thanhnga/Documents/learn/project/javaweb/ansible.yaml', vaultTmpPath: ''
            }
        }
    }
}