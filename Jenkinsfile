pipeline{
    agent { label "slave" }
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
        stage("ansible")
        {
            steps{
                ansiblePlaybook credentialsId: 'slave-ssh', installation: 'Ansible', inventory: '/home/thanh/jenkins/workspace/java_tomcat/inventory.ini', playbook: '/home/thanh/jenkins/workspace/java_tomcat/ansible.yaml', vaultTmpPath: ''
            }
        }
    }
}